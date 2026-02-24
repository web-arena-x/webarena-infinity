# Use hosted S/MIME to keep Gmail messages more secure

Source: https://support.google.com/mail/answer/7023606

---

If you're using a work account and the option has been turned on by your organization, you can keep your email messages more secure by using Secure/Multipurpose Internet Mail Extensions (S/MIME).

To use S/MIME, you need a S/MIME certificate uploaded to your account. Your Administrator may provide a certificate for you, or you may have to upload a Public-Key Cryptography Standards (PKCS) #12 certificate to Gmail through the Gmail settings. The certificate can be used to sign outgoing messages during transport. Other senders can use the public key to send you encrypted messages.

## Manage account certificates

[The next section](#get-certs), describes how to generate a PKCS #12 certificate file, sometimes called a “private certificate.” PKCS #12 is a bundle that includes your certificate and your private key. The certificate has your public key and email address, and it should be signed by a Certificate Authority (CA).

To use S/MIME, you or your system administrator have to upload the PKCS #12 file to your Gmail account. This section explains how you can upload certificates from the Gmail settings.

When you receive a message that is digitally signed with S/MIME, Gmail automatically associates the public key with a contact. You don't have to manually create a contact.

When you send a message, if there is a public key associated with the recipient in your contacts, Gmail automatically encrypts the message.

If you add more than one PKCS #12 certificate to your Gmail account, you need to set a default S/MIME certificate that Gmail will use to sign outgoing messages.

## Why would you upload more than one certificate?

One reason you might want to upload more than one certificate is if your current certificate is about to expire and you want to add a new one. You’d upload the new certificate and keep the previous one on your Gmail account. Gmail uses all the uploaded certificates to decrypt incoming messages. So if people who only have your previous public key send you encrypted emails, Gmail will be able to decrypt them.

Upload a certificate

**To upload a PKCS #12 file with your certificate and private key:**

1. In Gmail, click Settings ![Settings](//lh3.googleusercontent.com/p3J-ZSPOLtuBBR_ofWTFDfdgAYQgi8mR5c76ie8XQ2wjegk7-yyU5zdRVHKybQgUlQ=h36) ![and then](//lh3.googleusercontent.com/QbWcYKta5vh_4-OgUeFmK-JOB0YgLLoGh69P478nE6mKdfpWQniiBabjF7FVoCVXI0g=h36) **See all settings**.
2. At the top, click the **Accounts and Import** or **Accounts** tab.
3. In the **Send mail as** section, click **edit info** next to your work account.
4. Click **Upload a personal certificate**. A window opens showing the files available on your system. 
     
   You might not have this option if your organization doesn’t allow it.
5. Select the certificate file.
6. Enter the password and click **Add Certificate**.

## Change the default certificate

1. In the **Edit email address** window, locate the entry for the certificate.
2. Select the certificate to make it the default.

## Remove a certificate

You can remove certificates that are expired, revoked, or otherwise no longer required.

1. In the **Edit email address** window, locate the entry for the certificate and click **remove**.
2. Click **Remove Certificate**.

## How do I get certificates?

Your certificate should be signed by a Certificate Authority (CA).

There are 2 primary ways to get a PKCS #12 certificate file:

- Your system administrator will generate it for you. In this case, they can either directly upload it to Gmail or they can give it to you and you'll upload it using the [S/MIME Settings in Gmail](/mail/answer/7023606).
- You can use a CA to generate a PKCS #12 file. This section explains what you need to do to create the PKCS #12 file that you'll upload using the [S/MIME Settings in Gmail](/mail/answer/7023606).

**To generate a PKCS #12 file that includes your certificate and your private key:**

1. First, go to the web site of a trusted CA to request a certificate. Certificates have to adhere to certain public-key cryptography standards to be trusted. When you request a certificate, your browser will generate a public/private key pair and will send the public key to the CA
2. The CA will generate a signed certificate containing your public key and your email address. Most CAs will send you a link with the certificate file to download. This file often has a .pem or .crt extension.
3. Generate the PKCS #12 file on the **same machine and browser** that you used to request the certificate. The steps are different for each platform:

Generate a PKCS #12 file on Macintosh OS/X with Chrome 55

1. Open the certificate file provided by your CA by double clicking on the file. This opens the **Keychain Access utility** of the MAC OS. Add the certificate to the keychain ‘login’.
2. Go to **chrome://settings**.
3. At the bottom, click **Show advanced settings**.
4. Scroll to the HTTPS/SSL section and click **Manage certificates**.
5. The **Keychain Access utility** will open. Chrome uses it to manage digital certificate. Under 'Keychains' on the left, select 'Login' and click 'My Certificates' in the 'Category' column. Then select the certificate that was provided by your CA.
6. On the top menu, click **File > Export Items**.
7. Select the file format 'Personal Information Exchange (.p12)', enter a name for the file and click the **Save** button.
8. A window appears, prompting you to **enter a password** to protect the exported file.

Certificates for Chrome 51 on Ubuntu

1. Go to **chrome://settings**.
2. At the bottom, click **Show advanced settings**.
3. Scroll to the HTTPS/SSL section and click **Manage certificates**.
4. Click the **Import** button. Select the certificate file provided by your CA. Click open. The certificate will be added to Chrome.
5. The window will close. Scroll to the HTTPS/SSL section again and click **Manage certificates**.
6. Click the certificate to select it. Click **Export**. Select a name and a password for the PKCS #12 file that will contain both your certificate and private key.

Certificates for Internet Explorer 11 on Windows 10

1. The CA-provided certificate is saved on the browser's certificate store.
2. Open Internet Explorer.
3. From the menu bar, click **Tools** or click Settings ![Settings](//lh3.googleusercontent.com/p3J-ZSPOLtuBBR_ofWTFDfdgAYQgi8mR5c76ie8XQ2wjegk7-yyU5zdRVHKybQgUlQ=h36) at the top.
4. From the drop-down menu, select **Internet options**.
5. On the **Content** tab, select **Certificates**.
6. Click on a certificate to select it.
7. Click **Export** to open the export wizard and then click **Next**.
8. Select **Yes, export the private key**. 
     
   **Note**: If this option doesn’t appear, verify that you selected the correct certificate in the previous steps.
9. Click **Next**.
10. Select **.pfx** and click **Next**.
11. Select the **Password** box, enter and confirm your password, and click **Next**.
12. Enter the name of the file and click **Next**.
13. Review settings and click **Finish**.

**Note**: Be sure to enter a password when you generate the PKCS #12 file because it will contain your private key. Do not use your Gmail password. You'll need to enter this password when you upload the file to the Gmail settings.

## Can I generate a PKCS #12 file on Chrome OS?

No, Generating a PKCS #12 file on Chrome OS is not currently supported.