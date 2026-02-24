# Corporate Email Routing (Engage Legacy)

Source: https://support.zendesk.com/hc/en-us/articles/9731437701914-Corporate-Email-Routing-Engage-Legacy

---

Local Measure Engage leverages Amazon Simple Email Services (SES) in order to enable the Email channel. In this scenario, all emails will be routed via Amazon Connect contact flows.

The following AWS regions currently support receiving emails and one of these must be utilized when configuring SES:

- US East (N. Virginia)
- US West (Oregon)
- Europe (Ireland)

‍

## Email Solution

As mentioned earlier, emails are received via Amazon Simple Email Services (SES), which implies a receiving mailbox within SES. In most scenarios, the client will already have a fully functional mail server and won't be able to publish an MX record changing the mail server to SES as this will result in ALL email for ALL mailboxes being delivered in SES. What is needed is for selective corporate email addresses to be delivered in SES.

To overcome this challenge, an "intermediate” mailbox is configured and utilized within SES and the solution is configured in such a way that the end client is never aware of this. So, while emails are received in SES/Amazon Connect via the “intermediate” mailbox, the end client sends emails to an email address on the corporate mail server and agent (or system responses) are also sent from the email address configured on the corporate mail server.

## Solution Architecture

The below diagram illustrates the email solution:

![](https://support.zendesk.com/hc/article_attachments/9731474572698)

In the above scenario the following occurs:

1. The client sends an email to support@corporatedomain.com
2. The corporate mail server receives the email and then redirects the email to support@intermediateDomain.foo, it is critical that the email be redirected with the original to and from fields intact.
3. The original email is now received on support@intermediateDomain.foo in Amazon SES and queued for routing. As the email was redirected with original to and from fields intact, the agent can see the required details and respond back to the original sender.

In order to implement the above solution, the following actions must be taken:

1. An “intermediate domain” (intermediate.foo in the example above) must be purchased and configured in Route 53. This domain will never be visible to an end client and can therefore be any domain.
2. This new domain must be configured as a verified identity in SES.
3. An MX record must be added to the hosted zone associated with the intermediate domain, in Route 53, which will ensure that emails sent to email addresses for the new domain are handled by SES. The following table lists the settings, for the existing SES endpoints, which will be required for the MX record:

| Region | MX record entry |
| --- | --- |
| US East (N. Virginia) | 10 inbound-smtp.us-east-1.amazonaws.com |
| US West (Oregon) | 10 inbound-smtp.us-west-2.amazonaws.com |
| Europe (Ireland) | 10 inbound-smtp.eu-west-1.amazonaws.com |

The following link provides an overview of the required MX record configuration. Note that for this use case the record must be configured within Amazon Route 53 (Refer to section Instructions for creating MX records for various providers):

<https://docs.aws.amazon.com/ses/latest/dg/receiving-email-mx-record.html>

1. For any new SES environment, a case must be opened with AWS to move the SES instance from a Sandbox to a Production environment.
2. At this point the Local Measure CloudFormation stack can be updated to support email routing.
3. The corporate mail server must be configured to redirect - keeping the original to and from fields intact - incoming emails, targeting the original mailbox, to the email address configured in SES.
4. Lastly, the original email address (support@corporatedomain.com in the example above) must be configured as a verified identity in SES. This will allow Engage agents to send replies from the original email address, meaning that the intermediate domain is never visible to end clients. Clients will therefore send emails to support@corporatedomain.com and will also receive agent responses from support@corporatedomain.com.

## Authentication

Many enterprise email servers will have authentication enabled to ensure that other entities cannot send mail on their behalf. The three common authentication methods are DKIM, SPF, and a combination of the two, DMARC. If these authentication methods are present on the mail server, when an email is received by a customer, it has the potential to be marked as spam if authentication checks do not pass. The following sections will explain DKIM and SPF, as for SES purposes we just need DKIM and SPF configured to allow you to use DMARC.

Note: If you do not have authentication configured, please do not follow these steps. If you change authentication for emails at a later date, these steps can be followed after the fact.

### DKIM

DKIM, or DomainKeys Identified Mail, is a way to use public key cryptography to ensure that mail sent is authorized to come from your domain. DKIM works as follows:

1. Message signing: The sending email server adds a digital signature to the outgoing email message. This signature is generated using a private key associated with the sender's domain.
2. DNS record publication: The sender's domain publishes a special DNS (Domain Name System) record called the DKIM record. This record contains the public key that corresponds to the private key used for signing the emails.
3. Receiving server verification: When an email is received, the receiving server can perform DKIM verification by retrieving the public key from the sender's domain's DNS records.
4. Signature verification: The receiving server uses the public key to decrypt the signature attached to the email. It then recalculates the hash value of the email's content and compares it to the decrypted signature.
5. Hash comparison: If the recalculated hash matches the decrypted signature, it indicates that the email's content hasn't been modified during transit, and the sender's domain is validated.
6. Handling the verification result: The receiving server checks the DKIM verification result and can take different actions based on the outcome. For example, it may mark the email as authenticated, increase its trustworthiness, or apply specific rules for further processing.

Steps 2, 3, 4, 5, and 6 require the correct DKIM record to be set on your DNS server. Step 1 is handled automatically by Amazon SES after DKIM configuration is complete and a new verified identity is added.

### SPF

SPF is another mechanism to authenticate that mail comes from a server that you trust. SPF works in the following way:

1. When an email is received, the receiving mail server performs an SPF check by retrieving the SPF record of the sender's domain from the DNS.
2. In the SPF record, when the include mechanism is encountered (e.g., include:amazonses.com), the receiving server looks up the SPF record of the included domain (amazonses.com) instead of continuing the evaluation with the current domain.
3. The receiving server retrieves the SPF record of the included domain (amazonses.com) from the DNS.
4. The receiving server evaluates the included domain's SPF record, checking if the sending server's IP address matches any of the authorized servers specified in the included SPF record.
5. SPF result: Based on the evaluation of the included domain's SPF record, the receiving server determines whether the SPF check passes or fails for the included domain.

### Setup

For configuration with Amazon SES, we need to do the following:

**Create the DKIM Key Pair**, a 1024 to 2048 bit RSA Key Pair. From a bash terminal, run the following commands to generate the keypair:

- openssl genrsa -f4 -out private.key 2048
- openssl rsa -in private.key -outform PEM -pubout -out public.key

After generating the key pair, you need to **add the public key** to the sending domain’s DNS server

- Name: *selector*.\_domainkey.*example.com* (Replace *selector* with a unique key name and replace*example.com* with the sending domain)
- Type:  TXT
- Value:  p=*yourPublicKey* (Replace *yourPublicKey* with the public key generated in the previous step)

Next, if you have an existing SPF record, **change the DNS settings** to include Amazon SES before the terminating clause

- Add include:amazonses.com before the end of your record. For example, if you have a record like:  
   “*v=spf1 include:\_spf.example.com -all*”  
   It should be changed to: “*v=spf1 include:\_spf.example.com include:amazonses.com -all*”

After configuring the DNS record, you need to create a domain with a verified identity

- Follow the steps found in the verify domain instructions: <https://docs.aws.amazon.com/ses/latest/dg/creating-identities.html#verify-domain-procedure>

- Ensure that at Step 8, you follow the ‘BYODKIM’ instructions.

After this setup, we are ready to move on to configuration of email as a channel. Please notify the Local Measure Team that the set up is complete to enable them to complete the required steps for the Email channel in Engage for Amazon Connect.