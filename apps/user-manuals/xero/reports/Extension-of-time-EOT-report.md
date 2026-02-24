# Create an extension of time report

Source: https://central.xero.com/s/article/Extension-of-time-EOT-report

---

## Overview

- Check the extension of time (EOT) setting at the tax year level for your clients before you create terminal payment letters.
- You set EOT at client level, but you can change this for a particular tax year.

Your [user privileges](About-staff-privileges-in-Practice-Manager.md) will determine whether you can create and view this report.

Run this report before you create terminal tax letters for your clients to check EOT settings are correct for the tax year.

1. In the **Reports** menu, select **Report Builder**.
2. Select the **Custom reports** tab, then click **New report**.
3. For **Report type**, select **Tax Statement** and for **Report layout**, select **Table**.
4. Click **Create**.
5. In **1. Report**, change the title to something meaningful for your practice.
6. In **2. Fields**, select these fields:
   - **[Client] Client**
   - **[Tax Statement] Tax Name**
   - **[Tax Statement] Tax Year**
   - **[Tax Statement] Period To**
   - **[Tax Statement] Extension of Time**
7. In **3. Criteria**, select these fields:
   - **[Tax Statement] Extension of Time** – includes **No EOT - Deferred**
   - **[Tax Statement] Tax Year** – equals [**tax year just completed**]
   - **[Tax Statement] Tax Name** – includes **Income Tax**
8. In ****4. Publish**:**
   - If you have staff who don't have the **Report Builder** user privilege but you want them to see this report, select their names in the field **Select the staff members who can view this report**. All staff with the **Report Builder** user privilege can view this report.
   - Select the grouping, display and editing rights options you want for this report.
9. Click **Preview Report** and check the setting is correct for each client listed. Clients listed on this report don’t have an extension of time for the selected year, with the report stating **No EOT - Deferred**.
10. If you need to [change the setting for a client](Manage-extension-of-time-EOT.md) so their terminal tax letter generates at a later date, do this in their client record.
11. When you're happy with the report, click the back button on your browser to return to the report criteria screen, then click **Save**.

## What's next?

Visit the [Manage extension of time (EOT)](Manage-extension-of-time-EOT.md) page to update the EOT arrangements in Practice Manager for your clients to file their tax returns.