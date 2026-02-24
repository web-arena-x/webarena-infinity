# Set up tax approvals and payments for Gatekeeper mobile app users

Source: https://central.xero.com/s/article/Set-up-tax-approvals-and-payments-for-Gatekeeper-mobile-app-users

---

## Overview

- Set up mobile app job management in Xero Practice Manager.
- Set up payment approvals for clients who use Gatekeeper mobile.
- Allow on the go tax approvals for clients.

### About Gatekeeper mobile

Gatekeeper uses a two-touch approval interface to send tax approvals and payments to clients who use the Gatekeeper mobile app. This allows clients to approve returns that are ready to submit such as IRP6 and EMP201.

### Set up mobile app job management in Xero Practice Manager

Tip

Under **Client Setup**, click **SARS Settings** and ensure that the client has both a valid connection to SARS and a Xero business plan to continue the setup.

To track the client’s status when using the Gatekeeper mobile app, you’ll need to have the **Awaiting Client Approval** and **Client Declined Approval** job states set up in Xero Practice Manager (XPM).

To check this:

1. In the **Business** menu, select **Settings**.
2. Click **Job Settings**, then select the **Job State** tab.

If you can’t see the **Awaiting Client Approval** and **C****lient Declined Approval** job states [you’ll need to create them](https://xero.lightning.force.com/s/article/Create-edit-or-delete-job-states?userregion=true).

You can set up white-labelling in Gatekeeper to customise what your clients will see in Gatekeeper mobile. Make sure you have the right job states in XPM to enable job status updates.

To set up white-labelling in Gatekeeper:

1. Log in to Gatekeeper.
2. Click your organisation's name in the top left corner, then select **Practice settings**.
3. Click **White label settings**.
4. To include a **Practice logo**, click **Choose File**, then click **Upload Image**.
5. To add a greeting title for your clients, enter the title in the field under **Greeting Title**.
6. To add a greeting message for your clients, enter the message in the field under **Greeting Message**.
7. To edit the colour palette, click the colour icon  under each option to change the colour for that option.
8. Review the sample, then click **Save**.

### Set up your clients on the mobile app

You can set up your clients from your Gatekeeper dashboard:

1. Log in to Gatekeeper.
2. Click **Client Setup**.
3. Under **Mobile settings**, select the settings icon .
4. Under the tax type you want to add the client to, click **Add**.
5. Enter the client email address, then click **Add**.
6. Repeat for each tax type you want to add the client to.

An email will be sent to the client’s email address instructing them to download the Gatekeeper mobile app for Android or iOS.

Once the client has downloaded the mobile app, they’ll need to open the app and create an account using the email address assigned to them in Gatekeeper.

### Send a tax approval

Each time you submit a tax type via Xero or Gatekeeper, the client will be asked to approve or decline the request.

The client's email address needs to be assigned to the tax type in the Gatekeeper mobile app settings. Any returns submitted via Xero or Gatekeeper will show a **PENDING** status until the client has taken action.

If the client:

- Approves a request – the return will be submitted to SARS and the job state in XPM will change from **Awaiting Client Approval** to **Submitted**
- Declines a request – the return will revert to a non-submitted state and the job state will change from **Awaiting Client Approval** to **Client Declined Approval**

If a client declines a request, an email will be sent to the correspondence email address in your Gatekeeper practice settings.

### About payment requests

On approval, the payment is immediately loaded for authorisation in their bank and a confirmation email is sent informing them to check their bank account.

Once the client:

- Approves – the return is submitted to SARS and a credit push is initiated
- Pays – the job status changes to **Paid** in XPM

## What's next?

You can [build a diagram and display live representations of beneficial ownership](Set-up-the-Gatekeeper-beneficial-ownership-tool.md) to help submit the information to CIPC.