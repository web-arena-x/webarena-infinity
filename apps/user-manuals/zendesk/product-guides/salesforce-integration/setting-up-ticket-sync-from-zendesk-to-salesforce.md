# Setting up ticket sync from Zendesk to Salesforce 

Source: https://support.zendesk.com/hc/en-us/articles/4408828449050-Setting-up-ticket-sync-from-Zendesk-to-Salesforce

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

Verified AI summary ◀▼

This article guides you through setting up ticket sync from your platform to Salesforce, enabling ticket reporting and business workflows in Salesforce cases. Key steps include installing the ticket sync package, configuring field mappings, and setting up triggers. Important considerations include testing in sandbox accounts and understanding field mapping limitations. Ensure all required fields are mapped to avoid sync failures.

The Zendesk for Salesforce integration syncs Zendesk tickets to Salesforce cases,
enabling ticket reporting and business workflows in Salesforce. When the ticket sync
package is installed, Zendesk maps most of the standard ticket fields to Salesforce case
fields.

You can also display a view of Zendesk tickets on a Salesforce Case page. See [Setting up ticket view in Salesforce](https://support.zendesk.com/hc/en-us/articles/4408834115738).

This article contains the following sections:

- [Important
  considerations](#topic_gzc_s1q_vzb)
- [Recommendations before setting up](#ubm_jsk_sjb)
- [Setting up ticket sync](#id_vwx_prk_sjb)
- [Creating a Salesforce case record type](#topic_cp1_qrk_sjb)
- [Installing the ticket sync package in Admin Center](#topic_d3d_qrk_sjb)
- [Configuring Zendesk tickets to Salesforce cases sync](#topic_ek2_qrk_sjb)
- [Configuring the Sync tickets to Salesforce trigger](#topic_ogj_qrk_sjb)
- [Standard field mappings](#topic_spk_qrk_sjb)
- [Custom field mappings](#topic_llg_dnl_sjb)
- [Configuring organization matching](#topic_p35_l5l_sjb)
- [Configuring ticket requester matching](#topic_zpv_l5l_sjb)
- [Checking if ticket sync has successfully installed](#topic_gr3_yc4_ckb)
- [Checking your ticket sync setup](#topic_esv_hd4_ckb)

Related articles:

- [Salesforce integration resources](https://support.zendesk.com/hc/en-us/articles/4408827957274)
- [About triggers and how they work](https://support.zendesk.com/hc/en-us/articles/4408822236058)
- [Troubleshooting the Salesforce
  integration](https://support.zendesk.com/hc/en-us/articles/4408828717466)

## Important considerations

- Zendesk ticket attachments do not sync to Salesforce.
- Closed tickets do not sync to Salesforce. If a ticket has not synced and is
  already closed, you'll need to find an alternate method of creating a
  corresponding case within Salesforce, such as the Salesforce API.
- This ticket sync feature only guarantees syncing into cases created by the
  sync itself. Cases created separately might not match through sync for a
  variety of reasons.

## Recommendations before setting up

Ticket sync is an advanced feature, and it's important to understand the behavior
before setting it up in your production accounts. We recommend the following tasks:

- Test ticket sync in your Salesforce and Zendesk sandbox accounts before setting
  it up in your production account.
- If you have data sync turned on and you're testing with Salesforce sandbox and
  Zendesk production accounts, it's recommended to turn off **Create if no match
  found** in Ticket Organization Matching and Ticket Requester Matching to
  prevent duplicate organization and user records in Zendesk.

## Setting up ticket sync

Setting up ticket sync requires performing a number of tasks to the Salesforce case
object, Zendesk triggers, and in Admin Center.

**To set up ticket sync from Zendesk to Salesforce**

1. [Connect your Salesforce organization to
   Zendesk](https://support.zendesk.com/hc/en-us/articles/4408821555482).
2. [Create a Salesforce case record
   type](#topic_cp1_qrk_sjb).
3. [Install the ticket sync package in
   Admin Center](#topic_d3d_qrk_sjb).
4. [Configure the Zendesk tickets to
   Salesforce cases sync](#topic_ek2_qrk_sjb).
5. [Configure and activate Saleforce
   triggers in Zendesk Support](#topic_ogj_qrk_sjb).

## Creating a Salesforce case record type

Record types are used to implement a custom business process in Salesforce. It's not
mandatory to create a record type. However, if you are using your Salesforce case
object for another process, the record type ensures the Zendesk tickets are kept
separate.

Note: The admin connecting the Salesforce integration from Admin Center
must have access to the Salesforce case record type.

**To create a Salesforce case record type**

1. In Salesforce, click the Setup icon in the upper right.
2. Click **Object Manager**.
3. On the Object Manager page, click **Case**.
4. Click **Record Types** in the left navigation pane.
5. Click **New** in the upper right of the page.
6. Follow the steps on the Salesforce page to create a record type. It's
   recommended to name your **Record Type Label**: `Zendesk Ticket
   Sync`.   
   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/salesforce_ticket_sync_record_type.png)

## Installing the ticket sync package in Admin Center

The ticket sync package creates standard Zendesk ticket fields in the case object and
maps them to standard case fields.

For the ticket sync package to create case fields, the authenticated user must have
permission to modify the Salesforce metadata API.

**To install the ticket sync package**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_apps_integrations_icon.png)
   **Apps and integrations** in the sidebar, then select **Integrations >
   Integrations**.
2. On the Integrations page, click **Salesforce**.
3. Click the **Data sync** tab.
4. In Ticket sync, click **Configure**.
5. In Ticket sync package, click **Install**.

## Configuring Zendesk tickets to Salesforce cases sync

After the steps in the previous sections are completed, ticket sync allows mapping
and syncing of Zendesk fields to Salesforce cases.

**To configure settings for sending tickets to Salesforce cases**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_apps_integrations_icon.png)
   **Apps and integrations** in the sidebar, then select **Integrations >
   Integrations**.
2. On the Integrations page, click **Salesforce**.
3. Click the **Data sync** tab.
4. In Ticket sync, click **Configure**.
5. Select the **Enable ticket sync** checkbox, and configure the settings for
   sending Zendesk tickets to Salesforce cases.
6. In Record type, enter the Record type ID created earlier. You can find the [Record type ID](https://help.salesforce.com/articleView?id=000321696&language=en_US&type=1&mode=1) in your Salesforce
   account by clicking the  **Setup icon**, then **Object Manager** >
   **Case** > **Record Types**, and clicking on the record type to
   find the ID in the URL.   
   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/salesforce_ticket_sync_record_id.png)
7. In Custom ticket field mapping, map Zendesk ticket fields with the Salesforce
   case fields you want populated. Standard field mapping is provided and the
   ability to customize mapping.

   Note: You must map all required Salesforce case
   fields. If a required field is not mapped, the sync will fail. Drop-down
   fields mapped to picklists must have all possible values from Zendesk mapped
   to options in Salesforce. For more information, see [Standard field mappings](#topic_spk_qrk_sjb) and [Custom field
   mappings](#topic_llg_dnl_sjb).
8. In Organization matching, configure how Zendesk organizations are synced to
   Salesforce accounts. See [Configuring organization matching](#topic_p35_l5l_sjb).
9. In Ticket requester matching, configure how Zendesk ticket requesters are synced
   to Salesforce contacts or leads. See [Configuring ticket requester matching](#topic_zpv_l5l_sjb).
10. Click **Save**.

The first time you save your configuration, the following Salesforce [webhook](https://support.zendesk.com/hc/en-us/articles/4408839108378) and [Zendesk trigger](https://support.zendesk.com/hc/en-us/articles/4408822236058) are created in Support:

- **Webhook:** (Salesforce Integration) Sync tickets to Salesforce
- **Trigger:** (Salesforce Integration) Sync tickets to Salesforce

Important: Do not delete or rename the webhook and trigger.

Webhooks are used to send notify external applications when a ticket is created or
updated. Triggers are business rules that are defined in Zendesk.

## Configuring the Sync tickets to Salesforce trigger

[Zendesk triggers](https://support.zendesk.com/hc/en-us/articles/4408822236058) are created from
conditions and actions. They run immediately after Zendesk tickets are created or
updated. Review the trigger conditions for the Sync tickets to Salesforce trigger as
needed.

**To configure the trigger**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_objects_rules_icon.png)
   **Objects and rules** in the sidebar, then select **Business rules >
   Triggers**.
2. Click the **(Salesforce Integration) Sync tickets to Salesforce** trigger to
   edit it.   
   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/salesforce_activate_trigger.png)
3. Modify the trigger conditions as needed. Use the conditions as a filter to set
   which tickets should be sent to Salesforce. Do not rename the trigger.
4. Click **Save** to save your trigger settings.

## Standard field mappings

When the ticket sync package is installed, Zendesk creates and maps most of the
standard ticket fields to Salesforce case fields, as shown in the following table.
Most of the standard fields in the table cannot have their mappings changed and
therefore don't appear in Admin Center when you're mapping fields. Only the Type,
Priority, and Status standard fields can have their mappings changed (though you can
still [map custom fields](#topic_llg_dnl_sjb)).

Warning: Do not change the Zendesk ticket field type, as this may cause
the sync to fail.

|  |  |
| --- | --- |
| **Zendesk ticket field** | **Salesforce case field** |
| Type | Type |
| Priority | Priority |
| Status | Status |
| Zendesk Ticket ID | Zendesk\_Support\_Ticket\_ID\_\_c |
| Subject | Subject |
| Description | Description |
| Requester ID | ContactId |
| Requester Name | Zendesk\_Support\_Ticket\_Requester\_Name\_\_c |
| Requester Email | Zendesk\_Support\_Ticket\_Requester\_Email\_\_c |
| Organization ID | AccountId |
| Organization Name | Zendesk\_Support\_Ticket\_Organization\_Name\_\_c |
| Brand Name | Zendesk\_Support\_Ticket\_Brand\_Name\_\_c |
| Zendesk Assignee | Zendesk\_Assignee\_\_c |
| Assignee Name | Zendesk\_Support\_Ticket\_Assignee\_Name\_\_c |
| Assignee Group | Zendesk\_Support\_Ticket\_Group\_Name\_\_c |
| Tags | Zendesk\_Support\_Ticket\_Tags\_\_c |
| URL | Zendesk\_Support\_Ticket\_URL\_\_c |
| Ticket form name | Zendesk\_Support\_Ticket\_Form\_Name\_\_c |
| Date/Time created | Zendesk\_Support\_Ticket\_Created\_At\_\_c |
| Date/Time updated | Zendesk\_Support\_Ticket\_Updated\_At\_\_c |
| Date/Time solved | Zendesk\_Support\_Ticket\_Solved\_At\_\_c |
| Date/Time initially assigned | Zendesk\_Support\_Ticket\_Initial\_Assigned\_\_c |
| Resolution time (calendar) | Zendesk\_Support\_Ticket\_Resolution\_Cal\_\_c |
| Resolution time (business) | Zendesk\_Support\_Ticket\_Resolution\_Bus\_\_c |
| Comment | Ticket comments are not synced to a case field. However, you can set up Ticket View in Salesforce cases to view ticket comments. See [Setting up Ticket View in Salesforce](https://support.zendesk.com/hc/en-us/articles/4408834115738). |
| (The Salesforce user who connected the integration.) | Case Owner |

## Custom field mappings

The following standard fields are mapped automatically and don't require mapping:

- Requester wait time (calendar)
- Requester wait time (business)
- Agent wait time (calendar)
- Agent wait time (business)
- On-Hold time (calendar)
- On-Hold time (business)
- First Reply time (calendar)
- First Reply time (business)

If you'd like to sync custom fields, you can set up custom field mapping. Custom
field mapping allows Zendesk ticket fields to be mapped to fields on the Salesforce
case object (either a system field or a custom field). This mapping takes place in
the Zendesk Admin Center within the ticket sync settings.

The table below shows which Zendesk field types can be mapped to Salesforce field
types for ticket sync.

[View full size](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/salesforce_ticket_mapping.png)
![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/salesforce_ticket_mapping.png)

The following Zendesk field types are not supported with ticket sync:

- Multi-line
- Credit card
- Regex
- Lookup relationship

Mapping a multi-select Zendesk field will cause errors whenever that field has a
value. Do not map multi-select fields to sync to Salesforce.

The following Salesforce field types are not supported with ticket sync:

- EncryptedString
- ID
- MultiPicklist
- Percent
- Reference
- TextArea
- URL

Case origin picklist fields in Salesforce cannot be mapped.

**To map custom Zendesk ticket fields to the Salesforce case object**

1. In Salesforce, click the **Setup** icon in the upper right.
2. Click **Object Manager**.
3. On the Object Manager page, click **Case**.
4. Click **Fields & Relationships** in the left navigation pane, then click
   **New**.   
   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/salesforce_ticket_sync_custom_fields.png)
5. Select a **Data Type** for your new field, then click **Next**. See table
   above for which field types can be mapped between Zendesk and Salesforce.

   Note: When mapping a drop-down field in Zendesk to a text
   field in Salesforce, the tag values will show, not the field values. For
   more information on how tags work with custom ticket fields, see [Understanding custom ticket fields, tags,
   and business rules](https://support.zendesk.com/hc/en-us/articles/4408834953114#id_kxq_ydx_qcb).
6. Enter a **Field Label**. It is preferred to match the **Field Label** to
   the **Zendesk Custom Field Name**.
7. Complete the other mandatory fields, then click **Save**.
8. Repeat steps 4-7 to create additional custom fields.
9. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_apps_integrations_icon.png)
   **Apps and integrations** in the sidebar, then select **Integrations >
   Integrations**.
10. In Salesforce integration, click **Configure** > **Data sync** >
    **Ticket sync** > **Configure**  >  **Custom ticket field
    mapping**. The custom case fields previously created appear in the
    Salesforce fields.
11. Map your Zendesk fields to Salesforce fields, then click **Save**.

After mapping, when a ticket is sent into Salesforce, custom field data is
automatically populated according to the field mappings.

## Configuring organization matching

When configuring ticket sync, there are two options for setting the matching criteria
for organizations:

- If your Accounts to Organizations data sync is disabled, use default matching
  criteria and field mappings. The default matching criteria is **Organization
  Name to Account Name**. By default, when Zendesk sends ticket information
  to Salesforce, if an exact email match is not found between the ticket’s
  organization and account, a new account is created in Salesforce.
- If your Accounts to Organizations data sync is enabled, the custom matching
  criteria configured is used to match the ticket’s organization with Salesforce
  accounts. You can view your custom matching criteria in **Admin Center** >
  **Integrations** > **Integrations** > **Salesforce**, then
  navigate to > **Configure** > **Data sync** >**Ticket Sync**
  > **Configure**. See [Organization syncing options](#topic_aws_53c_tjb).

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/salesforce_ticket_sync_org_matching_2.png)

### Organization syncing options

The organization syncing section provides the following configuration
options:

- **Sync to existing Accounts** syncs the organization to the existing
  Salesforce account based on the matching criteria.
- **Sync to existing Accounts and create if no match** lets you map the
  Zendesk organization ID to a Salesforce account field. You can select from
  any standard and custom Salesforce account fields. This one-way sync is
  useful for displaying which Salesforce account is linked to a Zendesk
  organization.

  If you have required fields on the Salesforce account for
  creation, those fields need to be populated from the Zendesk
  organization by [mapping them](https://support.zendesk.com/hc/en-us/articles/4408828539290) in the Accounts
  to Organizations sync page. This applies even if the account sync isn't
  active.
- **Salesforce default Account** lets you enter an existing account as the
  default account in Salesforce if no organization exists in Zendesk. Setting
  a default account prevents orphaned accounts from being created.

  Note: The
  Organization field in Salesforce does not inherit the account of the
  contact in the Requester field. This Organization field only populates
  based on the organization information present on the ticket within
  Zendesk.

## Configuring ticket requester matching

When configuring ticket sync, there are two options for setting the matching criteria
for the ticket requester:

- If your Contact or Lead to User data sync is disabled, use default matching
  criteria and field mappings. By default, when Zendesk sends ticket information
  to Salesforce, and an exact email match is not found between the ticket
  requester and a contact, a new contact is created in Salesforce.
- If your Contact or Lead to User data sync is enabled, the custom matching
  criteria configured is used to match the ticket requester with Salesforce
  contacts or leads. You can view custom matching criteria in **Admin Center >
  Integrations > Integrations > Salesforce**, then select **Configure
  > Data Sync > Ticket Sync**> **Configure**.  
  ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/salesforce_ticket_sync_requester_2.png)

### Requester syncing options

The ticket requester section provides the following configuration options:

- **Sync to existing Contacts/Leads** syncs the requester to the existing
  Salesforce contact or lead based on the matching criteria.
- **Sync to existing Contacts/Leads and create if no match** lets you map
  the ticket requester's user ID to a Salesforce contact or lead field. Select
  from any standard and custom Salesforce contact or lead field. This one-way
  sync is useful for displaying which Salesforce contact or lead is linked to
  a Zendesk user.

  If you have required fields on the contact or lead for
  creation, they must be populated from the Zendesk user by [mapping them](https://support.zendesk.com/hc/en-us/articles/4408828539290) in the
  Contacts/Leads to Users sync page. This applies even if the contact sync
  isn't active.
- **Salesforce default Contact/Lead** lets you enter an existing contact or
  lead as the default contact or lead for new contacts if you opt to create
  new contacts for unmatched ticket requesters and no user exists in Zendesk.
  Enter the Salesforce contact or lead ID in the provided field.

## Checking if ticket sync has successfully installed

The following procedure helps you check if ticket sync has been successfully
installed in Salesforce.

**To check if ticket sync has successfully installed**

1. Go to **Salesforce** > **Setup** > **Deployment Status**.  
   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/salesforce_ticket_view_check1.png)
2. Check for a deployment time for when you installed the package to see if the
   deployment was successful or failed. If the deployment failed, Salesforce will
   provide you with detailed errors. Review the errors and resolve them. If you
   cannot resolve them, [contact Zendesk Support](https://support.zendesk.com/hc/en-us/articles/4408843597850) and provide a
   screenshot of the error.
3. Go to **Salesforce** > **Object Manager** > **Case** >
   **Fields & Relationships**. Check if additional case fields were
   created in your Salesforce case object, as shown below for each standard Zendesk
   ticket field.   
   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/salesforce_ticket_sync_check.png)
4. Once you have confirmed steps 2 and 3 were successful, continue with setting up
   ticket sync.

## Checking your ticket sync setup

Use the following checklist to check your data sync is set up correctly:

- Confirm the [Sync tickets to
  Salesforce](#topic_ogj_qrk_sjb) trigger is configured correctly.
- Confirm the trigger JSON body has not been edited and is as shown below. Any
  change to the JSON body causes the sync to
  fail.

  ```
  {"ticket_id": {{ticket.id}}, "salesforce_org_id": "YOUR_SFDC_ORG_ID"}
  ```

    
  ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/salesforce_ticket_sync_setup_check.png)
- Confirm you have entered the correct Record Type ID. If the Record Type ID is
  incorrect, the sync will fail. Note: Record Type ID is *not* your
  Salesforce Org ID.
- Confirm that all required Salesforce case fields are included in custom ticket
  field mappings. If you don't map all required fields, the sync will fail.