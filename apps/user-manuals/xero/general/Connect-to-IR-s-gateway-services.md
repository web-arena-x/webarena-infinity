# Connect to IR’s gateway services

Source: https://central.xero.com/s/article/Connect-to-IR-s-gateway-services

---

## Overview

- Connect your practice's tax agents to Inland Revenue’s (IR) gateway services (GWS) to file returns.
- Practice Manager uses GWS to exchange information with IR.

How it works

Inland Revenue (IR) uses gateway services (GWS) for filing tax returns. See IR's [explanation of gateway services](https://www.ird.govt.nz/topics/intermediaries/gateway-services) for more information.

Each tax agent in your practice needs a GWS connection to file tax returns for their clients. If your connection to GWS changes, you might need to disconnect and reconnect your tax agents.

Practice Manager uses GWS to send information to and retrieve information from IR automatically.

Connect a tax agent to GWS

1. In the **Business** menu, select **Settings**.
2. Under **Practice**, click **Client Settings**.
3. Select the **Tax Agent** tab.
4. Select the tax agent you want to connect to GWS.
5. Click **Connect to IRD** and enter your myIR credentials.
6. Click **Login**.
7. Click **Authorise** so Practice Manager can send and receive data on your behalf.

If you've connected a tax agent to GWS but they're experiencing issues with the connection, try reconnecting them.

Reconnect a tax agent to GWS

If your connection to GWS changes, you might need to reconnect your tax agents. This might be because IR changes its connection services.

To reconnect a tax agent, you first need to disconnect them:

1. In the **Business** menu, select **Settings**.
2. Under **Practice**, click **Client Settings**.
3. Select the **Tax Agent** tab.
4. Select the tax agent you want to disconnect from GWS.
5. Click **Disconnect from IRD**.

After a tax agent is disconnected, you can reconnect them to GWS again. You’ll need to do this for each tax agent you want to reconnect.

Tip

You can also use this process to disconnect a user that leaves your practice.

How Practice Manager uses gateway services

Practice Manager checks for signed tax returns with a filing date of today or earlier and uses GWS to send them to IR. It does this from 6:00 am until midnight every day, including non-business days.

Warning

If you mark an electronically filed tax return as signed after 6:00 am, you can't recall it.

Every 30 minutes, Practice Manager checks with IR for the following information it can retrieve:

- Confirmation reports
- Notices of assessment

## What's next?

[Set up your practice's START connection](Set-up-your-practice-s-START-connection-with-Inland-Revenue.md) with IR so you can submit income tax returns.