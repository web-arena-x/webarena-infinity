# Setting up advanced encryption (ADPP add-on)

Source: https://support.zendesk.com/hc/en-us/articles/5517626234138-Setting-up-advanced-encryption-ADPP-add-on

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **Add-on** | Advanced Data Privacy and Protection (ADPP) |

Location:  Admin Center > Account > Security > Advanced encryption

Advanced encryption allows your company to encrypt your Service Data using your own enterprise Key Management Service (KMS), ensuring data stored in Zendesk can’t be read in plaintext by an external party and is decrypted just in time to enable Zendesk services. This feature strengthens your security posture and helps you comply with data protection and privacy obligations. See [About advanced encryption](https://support.zendesk.com/hc/en-us/articles/5043582015898) to learn more.

This article helps you set up advanced encryption in your Zendesk account:

- [Supported Key Management Services](#topic_w45_gvk_12c)
- [Step 1: Request access to advanced encryption](#topic_l1b_f4p_jcc)
- [Step 2: Create a Secure Configuration Portal account](#topic_a1p_h4p_jcc)
- [Step 3: Configure KMS access keys](#topic_nnm_j4p_jcc)
- [Step 4: Activate advanced encryption](#topic_udb_l4p_jcc)

## Supported Key Management Services

Before you begin, you must have a KMS in place that is supported by Zendesk for advanced encryption:

- [AWS KMS](https://aws.amazon.com/kms/)
- [Azure Key Vault](https://azure.microsoft.com/en-us/products/key-vault)
- [Google Cloud KMS](https://cloud.google.com/security-key-management)
- [Thales CipherTrust Manager](https://cpl.thalesgroup.com/encryption/ciphertrust-manager)

## Step 1: Request access to advanced encryption

Start the setup process by requesting access to advanced encryption. Ensure the [ADPP add-on](https://support.zendesk.com/hc/en-us/articles/6561144266906) is turned on in your account.

**To request access to advanced encryption**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_account_icon.png) **Account** in the sidebar, then select **Security > Advanced encryption**.
2. Click **Request access** in the lower right.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/AE_request_access_new.png)

   After a few moments, you'll receive an invitation email.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/AE_invitation_email_new.png)
3. Click **Get Started** in the email message.

   A page opens, prompting you to create an account in the Secure Configuration Portal. Continue to [Step 2](#topic_a1p_h4p_jcc).

   You have seven days from receiving the invitation email before it expires. Click **Resend email request** to receive a new email if the previous invitation has expired.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/AE_resend_email_request.png)

## Step 2: Create a Secure Configuration Portal account

Create an account in the Secure Configuration Portal to manage your KMS configurations.

**To create a Secure Configuration Portal account**

1. After clicking **Get Started** in the invitation email, an account creation page appears. Create your account credentials, then click **Create account**.

   If you manage multiple accounts, including sandboxes, choose a descriptive company name and domain to uniquely identify the account.

   - Enter your name, email address, and create a password for your account.
   - For Company Name, enter your Zendesk [subdomain](https://support.zendesk.com/hc/en-us/articles/4408883411354#topic_swn_h2f_3xb).
   - For Company Domain, enter `yoursubdomain.zendesk.com`, where *yoursubdomain* is your Zendesk subdomain. If you're testing on a sandbox first,add the sandbox subdomain.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/security_ae_create_config.png)
2. Your account recovery token displays. Click **Download** to download the token. It's important to store the token in a safe location, such as a password manager. If you forget your password, you'll be prompted to use this token.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/AE_account_recovery_token_new.png)
3. Click **Confirm and close**.

   A login page appears.
4. Enter the email and password you just created, then click **Login**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/security_ae_login.png)

## Step 3: Configure KMS access keys

Next, you'll configure the KMS access keys. This is a 3-step process:

1. [Create encryption keys in your KMS](#topic_vjz_hxp_jcc)
2. [Add your KMS configuration in the Secure Configuration Portal](#topic_hny_3xp_jcc)
3. [Create the KMS configuration assignment](#topic_qyq_jxp_jcc)

### Create encryption keys in your KMS

In your [Zendesk-supported KMS](#topic_w45_gvk_12c), create your encryption keys by following the KMS-specific instructions.

After creating encryption keys in your KMS, make a backup copy. It's important to back up your encryption keys for business continuity and disaster recovery. Zendesk won't have access to your KMS and can't assist with disaster recovery. See the documentation for your KMS for instructions.

### Add your KMS configuration in the Secure Configuration Portal

Next, add your KMS credentials in the Secure Configuration Portal and configure which key to use when encrypting your data.

**To add your KMS configuration**

1. Go to <https://advanced-encryption.zendesk.com> and log in to the Secure Configuration Portal.
2. On the Secure Configuration Portal dashboard, click the icon for your KMS under Add Config.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/security_ae_add_config.png)
3. Add your access credentials and configure the key to use when encrypting your data. The steps to do this depend on which KMS you are using. Click **NEED HELP?** to open a step-by-step guide for your KMS.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/security_ae_create_Thales_config.png)
4. After you finish adding your access credentials, click **Encrypt and save**.
5. Click **Yes** to set the new configuration as the primary configuration.
6. The configuration is displayed on the KMS Configurations page. Note the **KMS Config ID**. You’ll need this ID for the next step.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/AE_key_leasing_enabled_default_2.png)

   Note: Key leasing is turned on by default, which reduces the cost of using the KMS and request latency. Key leasing is an extra layer of key wrapping so the advanced encryption service doesn’t need to make a request to your KMS on every key wrap and unwrap operation. Instead, it leases a key, wrapping it using your KMS, and it uses that key for a period of time to wrap and unwrap the keys that encrypt application data. The key is checked for validity with the KMS every 10 minutes. If the key is no longer valid, it’s destroyed.

### Create the KMS configuration assignment

Create the KMS configuration assignment, which allows Zendesk to use the KMS configuration to protect your data. If you added multiple KMS configurations, you must create an assignment for each.

**To create the KMS configuration assignment**

1. In the Secure Configuration Portal, click **KMS Config Assignments** in the left pane.
2. Click the plus icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/security_ae_plus_icon.png)) to add a config assignment.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/security_ae_add_config_assign.png)
3. Complete the following fields on the Assign KMS Configuration page:
   - Organization: Enter the Zendesk subdomain you're setting up for advanced encryption.   
     For example, if your support address is *support@mondocam.zendesk.com*, enter **mondocam**.
   - KMS Config ID: Enter the KMS config ID that was created after you [added the KMS configuration](#topic_hny_3xp_jcc).

     ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/security_ae_assign_KMS_config.png)
4. Click **Save**.

## Step 4: Activate advanced encryption

The last step in the setup process is to activate advanced encryption.

**To activate advanced encryption**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_account_icon.png) **Account** in the sidebar, then select **Security > Advanced encryption**.
2. Click **Next**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/AE_AC_activate_encryption.png)
3. Select each checkbox to confirm you understand what will happen when you activate advanced encryption.

   After all checkboxes are selected, the **Activate encryption** button becomes active.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/AE_confirm.png)
4. Click **Activate encryption**.

A progress bar displays the status of the data encryption process. The progress bar appears green when complete, and an Activated entry appears in the Encryption history table.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/AE_progress_activity.png)