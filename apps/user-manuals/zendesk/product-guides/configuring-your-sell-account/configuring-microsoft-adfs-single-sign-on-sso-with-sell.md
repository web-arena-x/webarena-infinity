# Configuring Microsoft ADFS Single Sign On (SSO) with Sell

Source: https://support.zendesk.com/hc/en-us/articles/4408839272986-Configuring-Microsoft-ADFS-Single-Sign-On-SSO-with-Sell

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

![Available on Sell Enterprise plans](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/plan_available_sell_e.png)

If your organization uses Microsoft ADFS, you can configure Zendesk Sell for SSO. This article explains how to set up the ADFS connection, create claim rules in Sell, edit your trust settings, and configure SSO in Sell.

 This article contains the following topics:

- [Setting up a relying party trust](#h_72d113b4-f769-4d5b-bb3e-8e6dc2904c0e)
- [Creating claim rules](#h_d3b245d3-d7ff-4c3b-adf3-03cebb093ead)
- [Setting the secure hash algorithm](#h_eb7c9bd5-1807-4932-acb4-757111dc0f09)
- [Configuring SSO in Sell](#h_33655216-465c-42ef-8d78-4529683d5928)

## Setting up a Relying Party Trust (RPT)

The connection between ADFS and Sell is defined using a Relying Party Trust (RPT).  You set this up in ADFS using a wizard.

**Set up an RPT**

1. Launch Microsoft AD FS Management.  From the Actions side bar, select the Relying Party Trusts folder, and click Start. This starts the configuration wizard for a new trust.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Sell_ADFS_1.png)
2. In the Select Data Source screen, select the last option: Enter Data About the Party Manually.  Click Next.
3. Enter a display name that you'll recognize in the future, and any notes, and click Next.
4. Select AD FS profile, and click Next.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sell_ADFS_4.png)
5. Click Next to keep the default certificate settings.
6. Check Enable support for the SAML 2.0 WebSSO protocol.

   The service URL is your Zendesk Sell Service Provider Assertion Consumer Service URL.  See [Setting up Single Sign On (SSO) with Zendesk Sell](https://support.zendesk.com/hc/en-us/articles/4408833582746) to find the service URL.

   Note: Remove any trailing slash at the end of the URL.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sell_ADFS_6.png)
7. Add a relying party trust identifier using your Zendesk Sell Service Provider Issuer ID and click Next.
8. Select whether you want to configure multi-factor authentication and click Next.
9. Select the option to permit all users to access this relying party, and click Next.
10. On the next two screens, the wizard displays an overview of your settings. Click through to the final screen. Close to save and exit and open the Claim Rules editor.

## Creating claim rules

You can create the claim rules and update the RPT with minor changes that you did not configure in the previous wizard. Configure the claim rules according to your current ADFS setup.

## Setting the secure hash algorithm

**Set the secure hash algorithm for the RPT**

1. In Microsoft AD FS Management, from the Actions side bar, select Properties while you have the RPT selected.
2. Select the Advanced tab and set **SHA-256 or SHA-1** as the secure hash algorithm.

## Configuring SSO in Sell

The final task is to configure SSO in Sell.  See [Setting up Single Sign On (SSO) with Zendesk Sell](https://support.getbase.com/hc/en-us/articles/206408215) for details.