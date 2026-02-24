# Set up Gatekeeper

Source: https://central.xero.com/s/article/Set-up-Xero-Gatekeeper

---

## Overview

- Set up Gatekeeper to connect Xero Practice Manager to South African Revenue Service (SARS).
- Gatekeeper automatically creates and updates jobs in Practice Manager with information from SARS.

What you need to know

### About Gatekeeper

Gatekeeper is a bridging tool that connects Practice Manager to SARS. Gatekeeper uses this connection to automatically create jobs and update job statuses in Practice Manager.

Gatekeeper is only available if you have a Practice Manager account and a practice in South Africa. Practice Manager creates jobs automatically from client tax information in the tax agent’s SARS profile. As client information gets updated in SARS, Gatekeeper updates this information in real time in Practice Manager. Upcoming jobs in SARS show on the **I****mportant dates** dashboard in Practice Manager.

### Practice Manager jobs in Gatekeeper

You need to use the default job templates in Practice Manager for Gatekeeper to create and update jobs. If you edit the name, state or category of a job template, it doesn't create or update the jobs. You can [edit jobs](About-jobs.md) back to their default settings in Practice Manager.

The default job category is **C****ompliance**. The default job states include:

- Planned
- In Progress
- Awaiting Client Response
- Awaiting Management Review
- Submitted
- Client Declined Approval
- Awaiting Client Approval

The default jobs which Gatekeeper uses are:

- CIPC – Annual Return
- VAT201 – Value-Added Tax Return
- EMP201 – Monthly Employer Declaration
- EMP501 – Bi-Annual Employee Verification
- IRP6 – Provisional Tax Return
- IT12 – Individual Income Tax Return
- T14 – Company Income Tax Return

To automate jobs not listed above, set up [recurring jobs](Recurring-jobs.md). If you accidentally delete a job in Practice Manager you’ll have to manually re-add it.

You can [build a diagram and display live representations of beneficial ownership](Set-up-the-Gatekeeper-beneficial-ownership-tool.md) to help submit the information to CIPC.

For clients who use Gatekeeper mobile, [set up mobile app job management in XPM](Set-up-tax-approvals-and-payments-for-Gatekeeper-mobile-app-users.md) to allow on the go approvals.

Set up a connection between Practice Manager and Gatekeeper

### Set up Xero as an ISV in SARS

To connect to Gatekeeper, you need to activate Xero as an ISV through SARS eFiling. This won't remove any previous ISV connections outside of Xero.

To activate Xero:

1. Log in to the [SARS eFiling portal](https://secure.sarsefiling.co.za/app/login).
2. Click **Organisations** at the top of the page.
3. On the organisations page, click **Organisation** in the menu on the left, then select **ISV Activation**.
4. Next to **ISV Application**, select **Xero**.
5. Click **Activate**.

This creates a **SARS ISV** **Login** and **Login key**, which you need to enter when you connect SARS to Gatekeeper.

### Allow Gatekeeper to connect to Practice Manager

Select a staff member in the practice to have API access to connect Gatekeeper to Practice Manager.

1. Log in to Practice Manager.
2. In the **Business** menu, select **Settings**.
3. Under **Practice**, select **Staff**.
4. Select the staff member to give access to.
5. Select the **Permissions** tab, then select **Practice administration**.
6. Select **Connect third-party add-ons**.
7. Click **Save**.

### Connect Gatekeeper to Practice Manager

1. Go to the [Gatekeeper website](https://xerogatekeeper.com/).
2. Click **Sign in with Xero**.
3. Select the account you want to allow access to.
4. Select **Allow Access**.

If you have more than one Xero practice connected to Gatekeeper, you’ll need to select a practice to connect to when you log in again.

Automate jobs with Gatekeeper in Practice Manager

### Connect a client’s SARS profile

SARS settings show the status of the SARS connection to Xero. To create the connection:

1. Log in to Gatekeeper.
2. Click **Client Setup**.
3. Under **SARS settings**, click the connection icon next to the client you want to connect.
4. Under **SARS eFiling access**, enter your client’s **SARS ISV login name**, **SARS ISV login key** and **SARS registered income tax number**.
5. Select **Connect**.
6. If the client:

- - Has a Xero organisation, under **Xero authorisation** click **Set up connection**, select the organisation, then click **Allow access**.
 - Doesn’t have a Xero organisation, under **Xero authorisation**, click **manual connection** and enter the details manually. Click **Save manual details**.

7. Under **Submission details**, the **Registered information** is automatically displayed.

The connection icon turns green when SARS and Xero are connected.

### Connect a client’s payroll provider

You can connect to your client’s payroll provider, Simplepay and PaySpace so payroll submissions can use Gatekeeper. You’ll need an API key to connect to the payroll provider.

You can only enter the payroll settings if the client is connected to Xero. **Payroll Settings** are greyed out if there's a manual connection in **SARS settings**.

To connect your payroll provider:

1. Log in to Gatekeeper.
2. Click **Client Setup**.
3. Under **Payroll settings**, click the connection icon next to the client you want to connect.
4. Select your payroll provider and enter your payroll provider's API information.

   - For [SimplePay](https://www.simplepay.co.za/help/accounting/advanced-options/xero-gatekeeper-simplepay-access-key/), enter your **Simplepay access key**
   - For [PaySpace](https://www.payspace.com/wp-content/uploads/2023/06/PaySpace-Xero-Integration.pdf), enter your **PaySpace ClientID and PaySpace Client Secret**
5. Click **Save**.

The connection icon turns green when it’s connected.

### Select client jobs

Select the return jobs your client needs to submit. Gatekeeper automatically creates the jobs you select in Practice Manager.

You need to connect to SARS settings and their payroll provider before you can select your return jobs.

Select the jobs you want created in Practice Manager:

1. Log in to Gatekeeper.
2. Click **Client Setup**.
3. Under **Practice Manager**, select the settings icon next to the client you want to manage settings for.
4. For each return type, select **On** if you want to:

   - **Create return jobs in Practice Manager** – the **Staff Allocation** tab allows you to assign a staff member’s calendar for SARS to populate jobs.
   - **Update jobs and calendar events with SARS data** – automatically update the job status based on your timeline settings and the SARS API for submitted jobs.
   - **Tax bill/inv creation**– if your client is connected to Xero, this tab will allow you to create a tax bill in Xero once the return has been submitted.
5. Click **Save** once you’ve organised your settings.

### Timeline to create a job

Select the job creation period and job time allocation for each job.

The timeline set for the job creation period is the amount of time before the SARS deadline. It also displays under **Planning** in the **Important Dates** section of the Practice Manager dashboard. The job time allocation is the amount of time before the job's work should be in progress.

To edit the job creation period and time allocation:

1. Log in to Gatekeeper.
2. Click your organisation's name in the top left corner, then select **Practice settings**.
3. Select **Practice Manager preferences**.
4. Enter the **Job creation period** and **J****ob t****ime allocation** for each return type.

Once you’ve entered these settings, they apply across the practice.

### Clients in Gatekeeper

Clients with Xero accounts that have been connected to Gatekeeper are shown with a Xero icon . Clients that aren’t connected to a Xero account in Gatekeeper or don’t have a Xero organisation have the CloudConvert icon . Click the CloudConvert icon to go to the [CloudConvert website](https://xero.cloudconvert.co.za/convert-to-xero-now/) to convert the data from your client’s legacy accounting software into Xero. You can then connect them to Gatekeeper.

Removing a client from Practice Manager also removes the client from Gatekeeper and all the connections. They won’t be on your SARS ISV profile, all connections will be disconnected, and new jobs won’t be created and existing jobs won’t update.

Set up eFiling for EMP201s in Gatekeeper

1. Log in to Gatekeeper.
2. Click **Client Setup**.
3. Under **Payroll settings**, click the connection icon next to the client you want to connect.
4. Under **EMP201 submission settings**, select **On** for **EMP201 auto-filing**.
5. Click **Save**.

​​​If you off-board a client, EMP201 eFiling through Simplepay and Payspace will stop if the EMP201 tax type is no longer part of the SARS profile.

## What's next?

If you’re having problems setting up Gatekeeper, [see some possible reasons why](Fixing-Xero-Gatekeeper-errors.md).