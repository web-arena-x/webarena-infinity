# Set up a client for filing AIM with Practice Manager

Source: https://central.xero.com/s/article/File-AIM-with-Practice-Manager

---

## Overview

- Set up a client so you can use Practice Manager to calculate their provisional tax using the accounting income method (AIM).

Warning

We no longer support AIM returns for clients with foreign exchange transactions. AIM returns still support clients without foreign exchange transactions.

## Before you start

Make sure you’ve [set up a tax agent or bookkeeper to file AIM returns](Set-up-a-tax-agent-or-bookkeeper-to-file-AIM-returns-in-Practice-Manager.md).

[Check the tax settings](/s/article/Edit-a-client-in-Practice-Manager-NZ-AU) of each client you want to submit AIM returns for:

- **IRD Number** – The client's IRD number
- **Balance date** – The client's balance date
- **Return type** – Leave blank
- **Tax Agent** – Select a tax agent
- **We hold a signed authority to act as a tax agent** checkbox – Leave empty

[Map your practice's report codes](IR10-and-AIM-mapping-from-Xero-to-Practice-Manager.md) to the client's chart of accounts.

## Create a job for preparing and submitting the AIM return

1. [Create a new job](Create-or-edit-a-job.md) for your client with the job state set to **Planned**.
2. In the **Information** tab, under **Tax**, select **New AIM**.
3. Select the period and ending date.
4. To allow a mid-year AIM enrolment, select the **Do you wish to enroll for AIM during the financial year?** checkbox.
5. Click **Save**. Xero performs an AIM eligibility check with IR and pre-populates the following fields in the client's return with data retrieved from IR:
   - **Losses brought forward (section 68)**
   - **20xx tax paid (section 74)**
6. Click **Options**, then select **Update from Xero**.

You'll be notified when the Xero data has successfully downloaded into the AIM return.

## What's next?

You're now ready to [prepare and submit the AIM return](Prepare-an-AIM-return.md) for your client.