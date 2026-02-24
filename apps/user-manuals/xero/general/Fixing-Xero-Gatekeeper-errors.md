# Resolve issues with Gatekeeper

Source: https://central.xero.com/s/article/Fixing-Xero-Gatekeeper-errors

---

## Overview

- Fix issues when setting up and using Gatekeeper.

## Unable to log in or connect Gatekeeper to Practice Manager

If you’re unable to log in to Gatekeeper or connect Gatekeeper to Practice Manager, it might be due to one of the following reasons:

- You don’t have an active Practice Manager account.
- You don’t have the correct [user permission in Practice Manager](About-staff-privileges-in-Practice-Manager.md) to connect Gatekeeper to Practice Manager. Check that you have the Connect third-party add-ons permission.
- The staff member who previously set up the connection has changed their email address, their user permission has been removed, or no longer has access to the Practice Manager account.

## The VAT number in SARS doesn’t match the VAT number in Xero

If you get this error message when you try to connect a client to SARS (South African Revenue Service), check if the VAT number entered in the [financial settings](/s/article/Set-up-your-organisation-s-financial-details-SA) of the client’s Xero organisation is correct.

## Tax types are blank under Submission Details

Once you connect your client to SARS, some tax types might appear blank under **Submission Details**. The connection only imports tax types from the SARS ISV user's tax profile where the client’s company, or individual's income tax numbers are saved.

## Job states aren’t updating in Practice Manager

A job's state might not update if:

- The client isn’t connected to SARS.
- **Update jobs and calendar events with SARS** wasn't selected on the return type in Gatekeeper.
- The default job state has been edited or deleted. You’ll need to [edit the job](About-jobs.md) back to the default settings in Practice Manager.
- The return hasn't been marked as submitted or updated in SARS. Once the return is updated in SARS, the job state will to **Submitted** within 24 hours.

## Jobs in Practice Manager aren’t being created

Jobs might not create if:

- The client isn’t connected to SARS.
- The due date on the job creation timeline hasn’t passed yet in SARS.
- The return type wasn’t selectedto create jobs when setting up Gatekeeper.
- The default job template name or category has been edited or deleted. You’ll need to [edit the job](About-jobs.md) back to the default settings in Practice Manager.

## Client is already connected before you connect them in Gatekeeper

The client organisation might be connected to Gatekeeper through the Xero App Store. To fix this, you need to disconnect them:

1. Go to the client’s Xero organisation, then select **Settings**.
2. Under **General**, select **Connected Apps**.
3. Disconnect the Gatekeeper app.
4. Once disconnected, you’ll need to [reconnect the Gatekeeper app](Getting-started-with-Xero-Connected-Apps.md).

## Client downloaded the Gatekeeper mobile app but can't create an account

The client might not be able to create an account if an incorrect email address has been added in Gatekeeper.

To check this from your Gatekeeper dashboard:

1. Click **Client setup**.
2. Click **Mobile settings**.
3. Check the correct email address is added for the client.

The email address needs to be the same as the one being used to create an account.

## Can't find client's bank details when trying to set up tax payments in Gatekeeper

Check the client’s SARS eFiling profile has been set up correctly.

To do this, log in to SARS eFiling and ensure that there’s a bank account that has been set up for credit pushes.

See [SARS eFiling guidance](https://www.sars.gov.za/individuals/how-do-i-pay/efiling-payments-credit-push/) for information on how to set up credit pushes.

## What's next?

If you're still having problems, log in to [Partner Central](https://central.xero.com/s/partners) in Xero Central, then select the **Dashboard** tab to find out who to contact.