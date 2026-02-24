# Troubleshooting Sell email integration errors

Source: https://support.zendesk.com/hc/en-us/articles/4408829007514-Troubleshooting-Sell-email-integration-errors

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

![Available on all Sell plans](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/plan_available_sell_all.png)

This article describes the errors that might occur when setting up an email integration in Sell (see [Integrating email with Zendesk Sell](https://support.zendesk.com/hc/en-us/articles/4408821242266)), including why they occurred and what you can do to fix the problem.

This article covers the following email integration errors:

- [001: We couldn't reach your email server](#topic_upl_tsm_h4b)
- [002: We reached your email server but couldn't connect](#topic_mkj_ytm_h4b)
- [003: An unknown error occurred while trying to connect to your email server. Try again but if issues persist, please contact support](#topic_i4t_j5m_h4b)
- [004: No TLS or SSL certificate found on your email server](#topic_ifq_w5m_h4b)
- [005: We located your SSL certificate, but it's not secure](#topic_v1x_mwm_h4b)
- [006: The hostname on your SSL/TLS certificate does not match your email server's hostname](#topic_hf4_xwm_h4b)
- [007: We couldn't verify the presence of a valid SSL/TLS certificate](#topic_jvm_cxm_h4b)
- [008: We couldn't establish a secure connection due to an issue with your SSL/TLS certificate](#topic_srp_3xm_h4b)
- [009: We couldn't log in to your email server using given credentials](#topic_zd3_mxm_h4b)
- [Authentication: Cannot authenticate](#topic_ovp_txm_h4b)
- [First sync running](#ariaid-title12)
- [You need to reconnect the same account](#topic_gqd_4cw_z4b)

## 001: We couldn't reach your email server

**What Happened:** We use the email credentials you provided to first find your email server and then to make a connection to your email server (to sync and send emails in Sell). This error indicates we were unable to complete the first step – we couldn't find or reach your email server.

| | What does that mean? | What can I do about it? |
| --- | --- | --- |
| Possibility #1 | In most cases, this error is a result of a typo. | Check that your IMAP and SMTP settings are spelled correctly. These settings include: 1. IMAP server name 2. IMAP port 3. SMTP server name 4. SMTP port Access your email account to locate these IMAP & SMTP settings or contact your IT. |
| Possibility #2 | Another reason could be that your email domain (i.e. name@companyname.com) stopped working. | Check that you can access your email account outside of Sell. |

## 002: We reached your email server but couldn't connect

**What Happened**: We use the email credentials you provided to first find your email server and then to make a connection to your email server (to sync and send emails in Sell). This error indicates that we were able to find your email server, but unable to make a connection with the server.

| | What does that mean? | What can I do about it? |
| --- | --- | --- |
| Possibility #1 | The port number you entered is not correct. You have an incoming mail server (IMAP) and an outgoing mail server (SMTP). Both of these servers have ports. We use the port numbers you provide to connect to your email server. | Check the settings in your email account to ensure you're entering the correct port numbers. You have a IMAP port and a SMTP port - check both. |
| Possibility #2 | A firewall is restricting us from making a connection to your email server. | You might need to adjust any firewalls in place on your email server. We recommend contacting your IT team for assistance. For more information, see [Configuring allowlist IP addresses](https://support.zendesk.com/hc/en-us/articles/4408831676442). |
| Possibility #3 | Your server is down, very slow, or not responding. | Disable any firewalls you have in place on your email server. |

## 003: An unknown error occurred while trying to connect to your email server. Try again but if issues persist, please contact support

**What Happened**: We use the email credentials you provided to first find your email server and then to make a connection to your email server (to sync and send emails in Sell). This error indicates that we were able to find your email server, but unable to make a connection with the server.

| | What does that mean? | What can I do about it? |
| --- | --- | --- |
| Possibility #1 | We didn't anticipate the error and we are unsure of the cause. | Try again. If you get the same error after multiple attempts, contact [Sell Support.](https://support.getbase.com/hc/requests/new) |

## 004: No TLS or SSL certificate found on your email server

**What Happened**: We have two requirements for integrating your email in Sell:

- A valid 3rd party SSL certificate or TLS protocol (either)
- IMAP & SMTP settings (must have both enabled on your server)

When you set up the email integration, we verify that you meet these two requirements, which are in place for security reasons. This error indicates that we couldn't verify one of these two requirements. Specifically, we could not verify the presence of a SSL certificate or TLS connection on your email server.

| | What does that mean? | What can I do about it? |
| --- | --- | --- |
| Possibility #1 | You don't have a SSL certificate (or TLS). | Purchase a SSL certificate. [See a list of recommended certificates](https://www.sslshopper.com/certificate-authority-reviews.html). |
| Possibility #2 | You have a SSL certificate (or TLS) but it is misconfigured on your email server so that when we check for this, no certificate is returned. | If you have a SSL certificate, check that it's configured correctly on your email server. [Use SSL Checker to learn more about your SSL configuration](https://www.sslshopper.com/ssl-checker.html). |
| Possibility #3 | Your server is not supporting SSL (or TLS) on the correct port. | Check that you're entering the correct IMAP and SMTP ports when setting up the integration. |
| Possibility #4 | Your certificate isn't properly assigned to the SMTP or IMAP services. | Verify which services are assigned to your SSL/TLS certificate and add your SMTP or IMAP service if necessary. For example, see [Microsoft's documentation on Assigning certificates to Exchange server services.](https://docs.microsoft.com/en-us/exchange/architecture/client-access/assign-certificates-to-services?view=exchserver-2019) |

## 005: We located your SSL certificate, but it's not secure

**What Happened**: We have two requirements for integrating your email in Sell:

- A valid 3rd party SSL certificate or TLS protocol (either)
- IMAP & SMTP settings (must have both enabled on your server)

When you enable the email integration we verify that you meet these two requirements during setup, which are in place for security reasons. This error indicates that we found a SSL certificate on your email server, but it's not a legitimate or trusted certificate.

This error indicates an issue on your side and related to the SSL certificate. You will need to make a change to set up the email integration successfully. Try the suggested solutions below, but if possible contact your IT team with this information.

| | What does that mean? | What can I do about it? |
| --- | --- | --- |
| Possibility #1 | You have a SSL certificate but it's self-signed. In other words, your SSL certificate is not validated by a trusted Certificate Authority (companies who provide valid 3rd party SSL certificates); therefore it's considered insecure. | Provide a valid and trusted SSL certificate from a known provider. [See a list of recommended certificate providers](https://www.sslshopper.com/certificate-authority-reviews.html). |
| Possibility #2 | You have a SSL certificate, but it's not installed correctly. | [Use SSL Checker to learn more about your SSL configuration](https://www.sslshopper.com/ssl-checker.html). |

## 006: The hostname on your SSL/TLS certificate does not match your email server's hostname

**What Happened**: We have two requirements for integrating your email in Sell:

- A valid 3rd party SSL certificate or TLS protocol (either)
- IMAP & SMTP settings (must have both enabled on your server)

When you enable the email integration we verify that you meet these two requirements during setup, which are in place for security reasons. This error indicates that we found an issue when verifying the first requirement relating to a valid SSL/TLS certificate. Specifically, we found that the hostname, or in other words your domain name, on the SSL certificate does not match the email you're attempting to integrate in Sell.

Every certificate is assigned a specific domain or group of domains. We compare the domain/hostname on the certificate with the email domain you're integrating in Sell to ensure they are the same. This error indicates that the domain on the certificate is not the same as the domain you're trying to connect to Sell. For example, attempting to connect the email "email.zendesk.com" with a certificate with the hostname"futuresimple.com" will not work.

| | What does that mean? | What can I do about it? |
| --- | --- | --- |
| Possibility #1 | The incorrect certificate was used. | Ensure the correct certificate is configured on your email server. |
| Possibility #2 | The certificate was signed with the wrong domain (or didn't include subdomains). | Ensure that the hostname/domain on your certificate matches the email domain you're integrating in Sell. |

## 007: We couldn't verify the presence of a valid SSL/TLS certificate

**What Happened**: We have two requirements for integrating your email in Sell:

- A valid 3rd party SSL certificate or TLS protocol (either)
- IMAP & SMTP settings (must have both enabled on your server)

When you enable the email integration we verify that you meet these two requirements during setup, which are in place for security reasons. This error indicates that we found an issue when verifying the first requirement relating to a valid SSL/TLS certificate.

| | What does that mean? | What can I do about it? |
| --- | --- | --- |
| Possibility #1 | We sometimes can't verify certificates because the certificate is signed by an authority that is not trusted. | Check that your SSL/TLS certificate is provided by a trusted Certificate Authority. If you need more help, contact [Sell Support](https://support.getbase.com/hc/requests/new) and provide: 1. IMAP servername 2. IMAP port 3. SMTP servername 4. SMTP port 5. Name of your certificate provider |
| Possibility #2 | We sometimes can't verify certificates because the certificate is signed by an authority that is not trusted. | You may be using a certificate from a provider that we're not yet aware of. Contact [Sell Support](https://support.getbase.com/hc/requests/new) and provide: 1. Name of your certificate provider 2. IMAP servername 3. IMAP port 4. SMTP servername 5. SMTP port |
| Possibility #3 | The certificate is missing some information, preventing us from verifying that it is valid or not. | Ensure the certificate includes the required information. If you need help, contact [Sell Support](https://support.getbase.com/hc/requests/new) and provide: 1. IMAP servername 2. IMAP port 3. SMTP servername 4. SMTP port |

## 008: We couldn't establish a secure connection due to an issue with your SSL/TLS certificate

**What Happened**: We have two requirements for integrating your email in Sell:

- A valid 3rd party SSL certificate or TLS protocol (either)
- IMAP & SMTP settings (must have both enabled on your server)

When you enable the email integration we verify that you meet these two requirements during setup, which are in place for security reasons. This error indicates that we found an issue when checking the first requirement relating to a SSL/TLS certificate.

| | What does that mean? | What can I do about it? |
| --- | --- | --- |
| Possibility #1 | When checking for a valid SSL/TLS certificate, we encountered a general SSL/TLS error, preventing us from establishing a secure connection between your email server and Sell. Without a secure connection, your email messages would be sent as unencrypted, which would put your sensitive data at risk. | Contact [Sell Support](https://support.getbase.com/hc/requests/new) and provide: 1. a screenshot of the error 2. IMAP servername 3. IMAP port 4. SMTP servername 5. SMTP port |

## 009: We couldn't log in to your email server using given credentials

**What Happened**: We successfully connected to your email server, but we couldn't sign in using the username and password provided.

| | What does that mean? | What can I do about it? |
| --- | --- | --- |
| Possibility #1 | Your username and/or password are incorrect. | Check that you typed your username and/or password correctly. You might need to provide a custom username (other than your email). You can do that by clicking **Edit** next to the **User Name** field. If you need to provide separate usernames and/or passwords for IMAP and/or SMTP, click **View SMTP & IMAP settings** to enter them separately. |
| Possibility #2 | You have SSO active. | We currently don't support SSO (Single Sign-On) for email integration. |
| Possibility #3 | Your IMAP/SMTP access is disabled. | Check with your email server administrator to ensure that you have IMAP and/or SMTP enabled for your account. |
| Possibility #4 | Your server doesn't support compatible authentication methods. | We support only *LOGIN* and *PLAIN* authentication methods, for both IMAP and SMTP. Check with your email server administrator to ensure that your server supports at least one of these methods. |

## Authentication: Cannot authenticate

This error message means the OAuth application for Office 365 was successful. However, there was an SMTP AUTH error when logging in to the server.

- Check that the **Username** and **Primary email address** fields match those set in the Microsoft admin settings.

 ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sell_office365_user_email_address.png)
- Also check that the Office 365 email [admin has enabled **OAuth** and **SMTP AUTH**](https://docs.microsoft.com/en-us/exchange/clients-and-mobile-in-exchange-online/authenticated-client-smtp-submission#use-the-microsoft-365-admin-center-to-enable-or-disable-smtp-auth-on-specific-mailboxes) on your Office 365 email account.

 ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sell_office365_email_apps.png)
- Finally, start integrating your Office 365 email with Zendesk Sell (see [Connecting your email with Zendesk Sell](https://support.zendesk.com/hc/en-us/articles/4408821242266)).

Important: The SMTP protocol is usually disabled in Office 365 by default, therefore an email admin must activate both the [SMTP and IMAP settings](https://support.zendesk.com/hc/en-us/articles/4408829062170) and the [SMTP AUTH](https://docs.microsoft.com/en-us/exchange/clients-and-mobile-in-exchange-online/authenticated-client-smtp-submission#use-the-microsoft-365-admin-center-to-enable-or-disable-smtp-auth-on-specific-mailboxes) for your mailbox (Sell uses these protocols to synchronize and send emails in your account).

## First sync running

This error message is due to email authentication errors from Microsoft. This is a known issue that Microsoft Office 365 accounts may encounter in the Communication Center. As it is a Microsoft issue, you must solve this error by following the steps in the article, [When I try to sign in with Microsoft I am getting a Cannot authenticate error message](https://support.zendesk.com/hc/en-us/articles/4408823174042-When-I-try-to-Sign-in-with-Microsoft-I-am-getting-a-Cannot-Authenticate-error-message).

## You need to reconnect the same account

If your account is de-authorized due to a password change, you must reconnect then try to sign in again with a different email and password.