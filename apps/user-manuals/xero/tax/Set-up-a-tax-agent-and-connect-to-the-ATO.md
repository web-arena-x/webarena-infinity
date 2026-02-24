# Set up a tax agent and connect to the ATO

Source: https://central.xero.com/s/article/Set-up-a-tax-agent-and-connect-to-the-ATO

---

## Overview

- Create a tax agent profile so your practice can lodge tax returns and activity statements on behalf of your clients using Xero Tax.
- Connect the agent in Xero Tax to the ATO so that you can lodge standard business reporting (SBR) forms.

How it works

- Add a tax agent so your practice can lodge tax returns and activity statements on behalf of your clients using Xero Tax.
- Connect the tax agent to the ATO to lodge SBR returns. Do this by setting the agent up with cloud software authentication and authorisation (CAA).
- Prior-year individual tax returns are submitted to the ATO using the Practitioner Lodgment Service (PLS). You no longer need to set up a separate ELS profile in Xero Tax.
- You don't need to upload an AUSkey to Xero Tax to lodge activity statements and tax returns with the ATO, as CAA is now used instead.

Add a tax agent

### Add a tax agent

A staff member must be registered as a [tax agent](https://www.tpb.gov.au/register-individual-tax-agent) (ATO website) or a [BAS agent](https://www.tpb.gov.au/bas-agent-registration) (ATO website) before you add them as a tax agent. They might also need to register for cloud authorisation and authentication (CAA).

To add a new tax agent:

1. In the **Business**menu, select **Settings**.
2. Under the **Practice** heading, click **Client Settings**.
3. Select the **Agent** tab, then click **Add Agent**.
4. Enter the agent details. The **Agent Name**, **Agent Number**, and **ABN** fields are mandatory.
5. Click **Save**.

Under **Bank Account**, you can select the checkbox to prevent manual bank details being entered in tax returns. When selected, the option to manually type in bank details doesn't show. This is an extra security measure to prevent fraud where a refund is requested to a bank account other than the client's and the agent's account.

Connect a tax agent to the ATO

You’ll need to contact the ATO to authorise each tax agent to use cloud software authentication and authorisation (CAA). You can [read more about CAA](https://www.ato.gov.au/General/Gen/Cloud-software-authentication-and-authorisation/) on the ATO website.

### Before you start

You’ll need the following information:

- Your registered agent number
- Software provider: **XERO AUSTRALIA PTY LTD**
- Software ID of Xero Tax

To get the Software ID from Xero:

1. In the **Business**menu, select **Settings**.
2. Under the **Practice** heading, click **Client Settings**.
3. Select the **Agent** tab.
4. Click the name of the relevant agent to nominate.
5. Under **Tax Information**, you’ll see the **Software ID**.

### Nominate Xero to lodge to the ATO on behalf of an agent

#### **Step 1**

Each agent who lodges using SBR will need to be nominated separately.

Login to Access Manager and go to **My hosted SBR software services**. [Follow the instructions](https://www.ato.gov.au/general/online-services/access-manager/access-manager-for-business-software-users/#NotifyusofyourhostedSBRsoftwareservices) on the ATO website.

If you're unable to do this using Access Manager, call the ATO on 1300 852 232 and follow the instructions provided.

Make sure you get confirmation before moving to the next steps.

#### **Step 2**

1. From the agent profile page, select the checkbox next to **Software ID registered with ATO for this agent:.**
2. Click **Save**.

Edit a tax agent's details

1. In the **Business** menu, select **Settings**.
2. Under the **Practice** heading, click **Client Settings**.
3. Select the **Agent** tab.
4. Click the name of the agent whose details you want to edit
5. Make changes, then click **Save**.

Under **Bank Account**, you can select the checkbox to prevent manual bank details being entered in tax returns. When selected, the option to manually type in bank details doesn't show. This is an extra security measure to prevent fraud where a refund is requested to a bank account other than the client's and the agent's account.

Delete a tax agent

Before you can delete a tax agent, you’ll need to make sure the tax agent isn’t assigned to any current or archived clients in Xero Tax or Practice Manager.

You can’t delete a tax agent profile if it’s linked to previously deleted clients. Unlike archived clients, there’s no option to retrieve a full list of deleted clients and edit them in Practice Manager. We recommend you remove the tax agent from the client details page before you delete a client.

To check if the tax agent is assigned to any current or archived clients, create a custom Client and Contact report using [Report Builder](Create-reports-with-Report-Builder.md). You can then report on the **[Client] Client** and **[Client] Tax Agent** fields and filter the results based on the tax agent name.

If there are clients associated with the tax agent, you’ll need to [edit the client’s details](https://central.xero.com/s/article/Edit-a-client-in-Practice-Manager-NZ-AU) and remove the tax agent from the **Agent** field, then save the changes.

Once there are no clients associated with the tax agent:

1. Click **Business**, then select **Settings**.
2. Under the **Practice**heading, click **Client Settings**.
3. Select the **Agent**tab.
4. Click the name of the agent you want to delete.
5. Click **Delete Agent**.

If a tax agent profile has previously been used to lodge returns, we don't recommend deleting the tax agent.

## What's next?

Once your tax agent is created, you can [add new tax clients](/s/article/Create-a-client-in-Practice-Manager-AU) for the agent to be assigned to.