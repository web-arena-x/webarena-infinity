# Preparing an SSL certificate for upload to Zendesk

Source: https://support.zendesk.com/hc/en-us/articles/4408832106522-Preparing-an-SSL-certificate-for-upload-to-Zendesk

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

Note: Zendesk can provide a free SSL certificate for your host-mapped domain or domains on Team, Professional, or Enterprise plans, see [Getting a Zendesk-provisioned SSL certificate](https://support.zendesk.com/hc/en-us/articles/4408838571930#topic_zvd_zbk_rw).

You can buy an SSL certificate and upload it to your Zendesk account to configure host mapping. Host mapping is the process of mapping a subdomain of your own domain (such as support.mycompany.com), to your default Zendesk address, see [Changing the address of your support website on Zendesk](https://support.zendesk.com/hc/en-us/articles/4408838571930).

Zendesk only supports SNI-based SSL certificates, and not support IP-based SSL certificates. The certificate must *not* be password protected and must be one of the supported certificate types:

- `ECDSAWithSHA256`
- `SHA256WithRSA`
- `SHA1WithRSA` (not recommended)

Before you buy, make sure your certificate authority supports SHA-2 encryption and that the CSR file generated uses SHA-2 encryption. This is also applicable to an intermediate certificate if used.

After purchasing an SNI-based SSL certificate, in most cases, the certificate authority will send you an email or direct you to a location where you can download your certificate. The email or download location may contain a single SSL certificate or multiple SSL certificates.

The certificate authority's instructions are often unclear about which files you really need and whether you should prepare them before uploading them to Zendesk. This article helps you determine which files to upload to Zendesk.

The following steps help you determine which files to upload to Zendesk:

1. [Identifying your certificate files](#step1)
2. [Creating a certificate bundle for upload](#step2)
3. [Getting a key file for upload](#step3)

## Step 1: Identifying your certificate files

You purchased a SSL certificate and received an email or download location. Here's what you should do next.

1. Read the instructions provided by the certificate authority.

   These instructions should help you identify what files are attached or downloadable and ultimately required.
2. Check for a .PEM file.

   If your email or download link contains a file identifying itself as a *certificate bundle* and the file has a **.PEM** file extension, you're in luck. You only need this single file.

   Download the .PEM file and skip to [Step 3: Getting a key file for upload](#step3) below.
3. If you don't have a .PEM file, download the primary server certificate.

   By default, the certificate authority should always provide you with a *primary server certificate*. This is the SSL certificate that you purchased. It's also the only certificate file that is unique to your subdomain or domain. Typically, this file has a **.CRT** file extension and is named something like "yourdomain.crt" or contains your unique subdomain in the file name.
4. Determine if you also need an intermediate certificate.

   In some cases, the instructions or documentation from the certificate authority explicitly state that you need to download and install an *intermediate certificate* or certificates along with your primary server certificate.

   If your instructions don't mention an intermediate certificate, skip to [Step 3: Getting a key file for upload](#step3) below.

   Otherwise, find out where the certificate authority is serving the intermediate certificate and download the file or files. An intermediate certificate is normally a .CRT file and contains either the word "Intermediate" or the name of the certificate authority in the file name.
5. Determine if you also need a root certificate.

   Your instructions or documentation may explicitly state that you must download and install a *root certificate* with your SSL certificate.

   If your instructions don't mention a root certificate, go to [Step 2: Creating a certificate bundle for upload](#step2) below.

   Otherwise, find out where the certificate authority is serving the root certificate and download the file. A root certificate is normally a .CRT file and contains the name of the certificate authority in the file name.

## Step 2: Creating a certificate bundle for upload

In the previous step, you downloaded an intermediate certificate and possibly a root certificate with your primary server certificate. This section describes how to prepare the files for upload to Zendesk. The process involves combining the files into a single file, which is often referred to as a *certificate bundle*.

Note: If your certificate authority provided you with a .PEM file, or if you didn't have to download an intermediate or root certificate, skip to [Step 3: Getting a key file for upload](#step3).

Important: If you have more than three certificates in your bundle, continue with the steps in this article to create and upload the PEM file, then [contact Zendesk Customer Support](https://support.zendesk.com/hc/en-us/articles/4408843597850) so we can finish the upload process for you. You can also contact Zendesk Customer Support if the upload status remains in pending for an hour or more. When submitting the ticket to Zendesk, don't include any attachments other than the PEM file. Confirm with your issuer if you aren't sure about the correct certificate position in the PEM bundle.

**To create a certificate bundle for upload**

1. Open each downloaded certificate file in a text editor.

   The contents of each file should contain a block of encoded text that begins with `-----BEGIN CERTIFICATE-----` and ends with `-----END CERTIFICATE-----`.
2. Create a blank text file in the editor.
3. Add the contents of each certificate into the new file in the following order:

   1. Primary server certificate
   2. Intermediate certificate(s)
   3. Root certificate

   If you only have the primary and intermediate, don't worry about the root certificate.

   Don't leave any spaces between the certificate blocks, as shown below:

   ```
    -----BEGIN CERTIFICATE-----
    (Your primary SSL certificate)
    -----END CERTIFICATE-----
    -----BEGIN CERTIFICATE-----
    (Your intermediate certificate)
    -----END CERTIFICATE-----
    -----BEGIN CERTIFICATE-----
    (Your root certificate)
    -----END CERTIFICATE-----
   ```
4. Remove any leading or trailing spaces in the formatting.
5. Save the file with a .PEM file extension.

   If necessary, select "All File Types" from the Save options of your editor, then save the file using the .PEM file extension. Example: `mycertificatebundle.pem`.

   If the editor won't let you save the file with a .PEM extension, don't worry. Simply save the file, locate it in your drive, and change the extension to .PEM.

After creating your certificate file, go to [Step 3: Getting a key file for upload](#step3) below.

## Step 3: Getting a key file for upload

Before uploading your certificate file to Zendesk, find out if you also need to upload a private key (.key file), with the certificate.

To determine if you need a key file, ask yourself the following question: When I went through the process of generating a *certificate signing request* (CSR), did I generate it in Zendesk, or did I generate it somewhere else?

- If you generated the CSR in Zendesk, you don't need a .key file. The certificate file is all you need to upload.
- If you generated the CSR somewhere else, you'll need to upload your private key with the certificate. The .key file is always generated at the same time as your CSR. It should be located where you generated your CSR.

After you've assembled the necessary files - the certificate file and, if applicable, a .key file - you can upload them to Zendesk. For instructions, see [Uploading the certificate](https://support.zendesk.com/hc/en-us/articles/4408838571930#topic_wtp_kqk_j4b).