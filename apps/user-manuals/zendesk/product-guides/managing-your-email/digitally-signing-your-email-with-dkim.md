# Digitally signing your email with DKIM

Source: https://support.zendesk.com/hc/en-us/articles/4408822303386-Digitally-signing-your-email-with-DKIM

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

Verified AI summary ◀▼

Digitally sign your email using DKIM to prevent spoofing and ensure authenticity. Update your DNS records with domain keys to verify signatures, and enable digital signatures to avoid email delivery issues. This setup helps maintain trust and security for your outbound emails. Ensure all steps are completed in order to prevent delivery failures.

It's easy for some people to spoof email -- that is, send email that pretends to be from somebody else. To combat spoofing, you can digitally sign outbound email from Zendesk to prove that an email actually came from somebody in your organization and not somebody pretending to be from your organization.

Digitally signing outbound email is supported only if you use an external email domain for your Zendesk email, as described in [Forwarding incoming email from your existing email address to Zendesk Support](https://support.zendesk.com/hc/en-us/articles/4408886828698) and [Allowing Zendesk to send email on behalf of your email domain](https://support.zendesk.com/hc/en-us/articles/4408832543770).

Zendesk Support allows [DKIM](https://dkim.org/) (Domain Keys Identified Mail) and [DMARC](https://dmarc.org/) (Domain-based Message Authentication, Reporting & Conformance) authentication. Email service providers that support DKIM or DMARC, such as Gmail and Yahoo!, check inbound email to see whether an organization that claimed to have signed a message actually did. The signature is associated with the organization's registered domain name.

If the message is properly signed, the email service provider delivers the message normally. If the message is not signed or is improperly signed, you can encounter delivery issues, depending on the email service provider's requirements. For example, you may experience delays or rejections in outbound sending, or users may receive a caution message.

Note: Third parties are not permitted to send email on behalf of any Zendesk subdomain. You'll still be able to forward messages to your external support address. However, you cannot send emails from name@subdomain.zendesk.com.
Email recipients will reject any email with a Zendesk subdomain that was not sent from one of Zendesk's servers.

You need to perform the following configuration steps to digitally sign your email:

- [Updating your DNS records to use the Zendesk domain key](#topic_sg5_ct5_rk)
- [Enabling digital signatures in Zendesk](#topic_dlr_rfv_rk)

## Updating your DNS records to use the Zendesk domain key

Before you can digitally sign your outbound email from Zendesk, you must update the Domain Name System (DNS) records of each of the external domains you are using with Zendesk so that the Zendesk domain key can be located and used to verify signatures. The DNS update creates a redirect to the domain key on the Zendesk domain. When an email service provider receives an email with your domain name, the provider looks up the Zendesk domain key to verify the signature of the email.

As an added security measure, Zendesk rotates its DKIM encryption keys every quarter. As long as you use the method described below to add domain keys to your DNS record, you won't have to make any changes when the keys are updated. The lookup will automatically locate the current Zendesk domain keys.

Note: Working with domain names can be confusing because it's something most of us rarely do. Consult your system administrator, if you have one, before proceeding.

The UI and terminology may vary depending on your registrar, but the concepts are the same.

**To add the domain key to your DNS records**

1. Log in to your domain registrar's control panel.

   Use the login name and password that you created when you registered the domain name.
2. Look for the option to change DNS records.

   The option might be called something like DNS Management, Name Server Management, or Advanced Settings.
3. Locate the CNAME records for your domain.

   A CNAME record, or Canonical Name record, is a type of alias used by the Domain Name System (DNS). CNAME records let you point to the Zendesk domain to use its domain key.
4. Look for an option to add a CNAME record.
5. Create a CNAME record with the following values:
   - In the **Host Record** field (or equivalent), enter:

     ```
     zendesk1._domainkey.your_email_domain.com
     ```

     where *your\_email\_domain.com* is the external email domain you use for your Zendesk email. Example: "mondocam.com". The domain can have a different [top-level domain](https://en.wikipedia.org/wiki/List_of_Internet_top-level_domains), such as .net, .org, or .ca.

     Example host record value:

     ```
     zendesk1._domainkey.mondocam.com
     ```
   - In the **Points To** field (or equivalent), enter:

     ```
      zendesk1._domainkey.zendesk.com
     ```

     Example:

     ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/email_sign_cname.png)
6. Create a second CNAME record with the following values:
   - In the **Host Record** field, enter:

     ```
      zendesk2._domainkey.your_email_domain.com
     ```

     where *your\_email\_domain.com* is the external email domain you use for your Zendesk email.

     Example host record value:

     ```
     zendesk2._domainkey.mondocam.com
     ```
   - In the **Points To** field, enter:

     ```
      zendesk2._domainkey.zendesk.com
     ```

Note: It takes time for changes to the DNS system to be implemented.
Typically, it can take anywhere from a few hours to a day, depending on your Time To Live (TTL) settings in the registrar's control panel.

## Enabling digital signatures in Zendesk

Enable digital signatures in Zendesk after you've updated your DNS records.

Warning: Enabling digital signatures must be the *final* step in the configuration process. Enabling this feature before adding the CNAME records for your domain will cause delivery failures.

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_channels_icon.png)
   **Channels** in the sidebar, then select **Talk and email > Email**.
2. In the Email settings section, select **Custom domain for DKIM**.
3. Click **Save**.

You can use third-party validation tools to confirm that DKIM is enabled and running properly. See [How do I know if my DKIM records are configured correctly?](https://support.zendesk.com/hc/en-us/articles/4408834262682) for more information.