# Configuring data sync from Salesforce to Zendesk

Source: https://support.zendesk.com/hc/en-us/articles/4408828539290-Configuring-data-sync-from-Salesforce-to-Zendesk

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

Verified AI summary ◀▼

Configure a one-way data sync from Salesforce to manage customer records. Sync Salesforce accounts to organizations and contacts or leads to users, ensuring updates in Salesforce reflect in your support system. Set up involves API configuration, field mapping, and sync filtering. Note that sync is one-way, and certain Salesforce fields aren't supported. Ensure unique identifiers to avoid sync issues.

The Zendesk for Salesforce integration provides one-way data sync from Salesforce to Zendesk
Support. This article describes how to set up two types of data sync:

- Salesforce accounts to Zendesk organizations — Zendesk organizations in Support are
  automatically created and updated when Salesforce accounts are created or modified.
- Salesforce contacts or leads to Zendesk users — Zendesk users in Support are
  automatically created and updated when Salesforce contacts or leads are created or
  modified.

Data sync is available between one Salesforce organization and one Zendesk account. This
feature doesn't support multi-instance connections.

This article contains the following sections:

- [Understanding the data sync process](#topic_ec4_kr4_rjb)
  - [Salesforce accounts to Zendesk Organizations sync](#topic_j5g_jv4_rjb)
  - [Salesforce contacts or leads to Zendesk users sync](#topic_udd_pv4_rjb)
- [Setting up a data sync](#topic_s3c_xv4_rjb)
  - [Configuring your Salesforce API settings and permissions](#topic_mpl_nw4_rjb)
  - [Configuring Salesforce accounts to Zendesk Organizations sync](#topic_sns_fy4_rjb)
  - [Configuring Salesforce contacts or leads to Zendesk users sync](#topic_tsc_py4_rjb)
- [Understanding sync filtering](#topic_tyr_h1p_rjb)
- [Understanding matching criteria](#topic_cjz_s1p_rjb)
- [Understanding field mapping](#topic_kqp_x1p_rjb)
  - [Salesforce accounts to Zendesk organizations field mapping](#topic_myy_kbp_rjb)
  - [Salesforce contacts or leads to Zendesk users field mapping](#topic_psn_qbp_rjb)
- [Checking your data sync setup](#topic_sxg_xls_sjb)

Related articles:

- [Salesforce integration resources](https://support.zendesk.com/hc/en-us/articles/4408827957274)
- [Why do phone numbers synced from Salesforce lose
  their country code?](https://support.zendesk.com/hc/en-us/articles/4468066453274)

## Understanding the data sync process

A data sync is triggered when a mapped field is updated in an existing Salesforce
record, or a new record is created. Any unmapped fields that are updated do not
trigger the sync.

When a Salesforce record is created or changed, the syncing process determines
whether to create a new record or update an existing record in Zendesk Support. This
is done by comparing field values based on the defined criteria.

Once a successful match of existing records has been made, or a new record has been
created in Support, the Salesforce and Support records are linked. This means that
subsequent updates to the record in Salesforce don't use matching criteria but
instead update the linked record in Support.

If more than one matching result is found, the sync cannot determine which record
needs to be updated. Because this is a background process, the ongoing sync won't
update records and logs an unsuccessful sync event.

If a Salesforce user updates a mapped field indirectly through a Salesforce flow, sales process, or Apex trigger, the field may not sync to Zendesk if the user who triggered the indirect update does not have edit permission to the mapped field.

A sync is triggered to Zendesk when records are created or updated to a mapped field
using the Salesforce API.

Because data syncing is one-way, any changes applied in Zendesk are not reflected in
Salesforce.

### Salesforce accounts to Zendesk Organizations sync

The Salesforce account to Zendesk organization sync is a one-for-one sync that
uses account name to organization name for matching records by default. However,
not all Salesforce implementations adhere to this rule. If you have duplicate
account names, you can change this to another unique account field. This might
not be a suitable feature if you don't have unique account fields.

This data sync has the following limitations:

- Data sync consumes Salesforce streaming API governor limits. For example, if
  you have a large amount of data to be synced, this exceeds the governor
  limit, and data may not sync.
- Salesforce Person accounts are imported as Zendesk Organizations. If you'd
  prefer a Salesforce Person account to be added as a Zendesk user, you can
  perform a [bulk import of users](https://support.zendesk.com/hc/en-us/articles/4408893496218) or use the
  [Create user API](https://developer.zendesk.com/api-reference/ticketing/users/users/#create-or-update-user) with
  Salesforce-specific
  information.

### Salesforce contacts or leads to Zendesk users sync

The sync from Salesforce contacts or leads to Zendesk users is one-for-one, based
on unique email addresses. However, not all Salesforce implementations adhere to
these rules, so consider whether this feature suits your needs.

This data sync has the following limitations:

- For security reasons, data sync will not sync a Salesforce contact to a
  Zendesk user if the Zendesk user is an agent or admin.
- Data sync consumes Salesforce streaming API governor limits. For example, if
  you have a large amount of data to be synced, this exceeds the governor
  limit, and data may not sync.

Note: If you have multiple Salesforce contacts with the same email address belonging
to different accounts and want to sync to a user in Zendesk, use the multiple
organizations feature in Support. See [Using the multiple organizations feature in
the Salesforce integration](https://support.zendesk.com/hc/en-us/articles/4408832217882).

## Setting up a data sync

Setting up a data sync requires several tasks in Salesforce and Zendesk Admin Center.

**To set up data sync for your integration**

1. [Connect your Salesforce organization to Zendesk](https://support.zendesk.com/hc/en-us/articles/4408821555482).
2. Configure [Salesforce API settings
   and permissions for syncing.](#topic_mpl_nw4_rjb)
3. In Admin Center, configure sync settings for [Salesforce accounts to Zendesk organizations](#topic_sns_fy4_rjb) and [Salesforce contacts or leads to
   Zendesk users](#topic_tsc_py4_rjb).

### Configuring your Salesforce API settings and permissions

Before setting up a data sync, some Salesforce APIs settings and permissions must
be enabled for data sync to be successful. The information in the following
procedures is described for the Salesforce Lightning edition.

**To enable the Salesforce API**

1. On the Salesforce **Setup** page, select **Administration** >
   **Users** > **Profiles**.
2. Select **System Administrator** or the authenticated user's profile.
3. Click **System Permissions** and select the **API enabled**
   checkbox.  
   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/salesforce_data_sync_api_enabled.png)

**To set streaming API channel permissions**

1. On the Salesforce **Setup** page, select **Administration** >
   **Users** > **Profiles**.
2. Select the user profile of the admin setting up the integration.
3. Click  **Object Settings** > **Streaming Channels**, and under
   **Object Permissions**, select the **Read** checkbox.  
   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/salesforce_data_sync_object_perm.png)

**To set PushTopic permissions**

1. On the Salesforce **Setup** page in the left sidebar, select
   **Administration** > **Users** > **Profiles**.
2. Select the user profile of the admin setting up the integration.
3. Click **Object Settings** > **Push Topic**, and click
   **Edit**.
4. Under **Object Permissions**, select the **Read** checkbox, and click
   **Save**.   
   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/salesforce_data_sync_push_topic.png)

**To enable Streaming API**

1. On the Salesforce **Setup** page in the left sidebar, select **Platform
   tools** > **User Interface** > **User Interface**.
2. Under **Setup**, select the **Enable Streaming API** checkbox.   
   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/salesforce_data_sync_streaming_api.png)

### Configuring Salesforce accounts to Zendesk Organizations sync

The following procedure explains setting up a sync so Zendesk organizations in
Support are automatically created and updated when Salesforce accounts are
created or modified.

Important: This is an advanced feature. Once
data is synced from Salesforce to Zendesk, it is not reversible. We highly
recommend that you test this feature first.

**To configure Salesforce accounts to Zendesk organization sync**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_apps_integrations_icon.png)
   **Apps and integrations** in the sidebar, then select **Integrations >
   Integrations**.
2. On the Integrations page, click **Salesforce**.
3. Click the **Data sync** tab.
4. In **Accounts to Organizations sync**, click **Configure**.
5. Select the **Enable syncing** checkbox, and configure the settings for
   which accounts and account fields are synced to Zendesk.
6. In **Sync filtering**, configure conditional filters to define which
   Salesforce accounts are synced to Zendesk. For more information, see [Understanding sync filtering](#topic_tyr_h1p_rjb).
7. In **Matching criteria**, set the criteria for matching Salesforce
   accounts to Zendesk organizations. For more information, see [Understanding matching criteria](#topic_cjz_s1p_rjb).
8. In **Field mapping**, map which Salesforce account fields you want to
   populate with the Zendesk organization field. For more information, see
   [Understanding field mapping](#topic_kqp_x1p_rjb).
9. In **Synced organization mapping**, you can choose to map the Zendesk
   organization to a Salesforce account. Select any standard or custom
   Salesforce account field. This one-way sync is useful for displaying a
   Zendesk user linked to a Salesforce account.

   Note: This mapping field is a
   place for Zendesk to send the Organization ID. Choose a field where
   you'd want to see this data written. It will overwrite any information
   that might have been there previously. The Salesforce integration only
   writes the Organization ID into the synced organization mapping field on
   the first successful sync. Subsequent syncs do not populate this field
   within Salesforce.
10. In **Zendesk external ID**, select the checkbox if you want the external
    ID to populate the Zendesk organization external ID field. This can only be
    set to the Salesforce Account ID.

    Note: Any existing external ID values are
    overridden and cannot be reverted. This may impact other applications
    that rely on this field. This change is only applied when you click
    **Save**.
11. Click **Save** to save your configuration. Confirmation of saved settings
    is displayed.

### Configuring Salesforce contacts or leads to Zendesk users sync

The following procedure explains configuring a sync so Zendesk users in Support
are automatically created and updated when Salesforce contacts or leads are
created or modified.

Note: For Zendesk user records to be automatically mapped to their corresponding
organizations upon a users sync, both **Contacts/Leads to Users sync** and
**Accounts to Organizations sync** must be
enabled.

**To configure Salesforce contacts or leads to Zendesk user sync
settings**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_apps_integrations_icon.png)
   **Apps and integrations** in the sidebar, then select **Integrations >
   Integrations**.
2. On the Integrations page, click **Salesforce**.
3. Click the **Data Sync** tab.
4. In **Contacts/Leads to User sync**, click **Configure**.
5. Select the **Enable syncing** checkbox, and configure the settings for
   which contacts or leads and associated fields are synced to Zendesk.
6. In **Sync Type**, select if you want Zendesk users to be created based on
   Salesforce contacts or leads. Note that you can only select one.
7. In **Sync Filtering**, configure conditional filters to choose which
   Salesforce contacts or leads accounts are synced to Zendesk. For more
   information, see [Understanding sync filtering](#topic_tyr_h1p_rjb).
8. In **Matching criteria,** set the criteria for matching Salesforce
   contacts or leads to Zendesk users. For more information, see [Understanding matching criteria](#topic_cjz_s1p_rjb).
9. In **Field mapping**, map which Salesforce contact or lead fields you
   want to populate with Zendesk organization field. For more information, see
   [Understanding field mapping](#topic_kqp_x1p_rjb).
10. In **Synced user mapping**, you can choose to map the Zendesk user to a
    Salesforce contact or lead. Select any standard or custom Salesforce contact
    or lead field. This one-way sync is useful for displaying a Zendesk user
    linked to a Salesforce contact or lead.

    Note: This mapping field is a place
    for Zendesk to send the User ID. Choose a field where you'd want to see
    this data written. It will overwrite any information that might have
    been there previously. The Salesforce integration only writes the User
    ID into the synced user mapping field on the first successful sync.
    Subsequent syncs do not populate this field within Salesforce.
11. In **Zendesk external ID**, select the checkbox if you want the external
    ID to populate the Zendesk user external ID field. This can only be set to
    the Salesforce Contact ID.

    Note: Any existing external ID values are
    overridden and cannot be reverted. This may impact other applications
    that rely on this field. This change is only applied when you click
    **Save**.
12. In **General options**, select the **Send welcome email** checkbox to
    send a welcome email to new users in Support. For more information, see
    [Customizing the welcome email and the
    account verification email](https://support.zendesk.com/hc/en-us/articles/4408824350746).
13. Click **Save** to save your configuration. Confirmation of saved settings
    is displayed.

## Understanding sync filtering

In the **Data Sync** > **Sync Filtering** section, you can filter which
Salesforce accounts are synced to Zendesk or choose which Salesforce contacts or
leads accounts are synced to Zendesk. You can control the sync by building
conditional statements. If no filters are set, all accounts are in scope for
syncing.

To create a sync filter condition, specify the field, the operator, and the
value:

- **Meet ALL of the following conditions**: All conditions added to this
  section must be met to include the Salesforce record in the sync.
- **Meet ANY of the following conditions**: One or more conditions in this
  section must be met to include the Salesforce record in the sync.

Note: You are limited to three ALL and three ANY conditions
due to Salesforce PushTopic limitations.

Sync filtering has the following rules:

- All values are case-sensitive.
- Multiple values in a condition can be separated by a comma with no spaces.
- When using a Salesforce picklist field in the sync filter, the value must be the
  API name of the picklist options.
- The **Account Record Type** field in Salesforce is not supported.
- When a checkbox type field is used as a condition, enter a **true** or
  **false** value.  
  ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/salesforce_data_sync_filtering_2.png)

The following Salesforce fields are not supported for filtering:

- Formula field
- Lookup field
- Long text area field
- Currency fields

## Understanding matching criteria

In the **Data sync** > **Matching criteria** section, the criteria is set
for matching Salesforce accounts to Zendesk organizations, or Salesforce contacts or
leads to Zendesk users. When a record in Salesforce is created or changed, the
syncing process checks whether a new organization or user record in Support should
be created, or an existing organization or user record should be updated. This is
done by comparing the values set in the matching criteria that you set. When a match
is found, the corresponding fields are updated according to your field mapping
settings.

The options in the Zendesk field drop-down vary according to the type of field you
select in the Salesforce drop-down. Standard and custom fields are supported for
matching.

**Note**:

- Only one matching criterion is supported.
- If more than one matching result is found, the sync won't be successful since it
  can't determine which record needs to be updated. In this case, ongoing sync
  won't update records and logs an unsuccessful sync event.
- The Phone field in Salesforce cannot be used as matching criteria to Zendesk
  fields.

## Understanding field mapping

The field mapping sections enable Salesforce fields to be mapped to Zendesk fields.
Every Salesforce account, contact, or lead field should be mapped to a standard or
custom Zendesk field. Mapped fields are updated during the sync.

The Salesforce data is the "source of truth" for mapped fields. If a mapped Zendesk
field contains data upon sync, it is overwritten with the Salesforce data. If you
don't want to overwrite data in Zendesk, don't map the field. If a field is mapped
to a text field in Zendesk, an empty value in Salesforce will sync over to remove
the Zendesk value.

The Tags, Email, and Phone fields are exceptions. These fields are *appended*
with Salesforce values upon sync. Salesforce email addresses added to Zendesk during
sync are added as secondary addresses.

When a multi-picklist Salesforce field is selected for mapping, a **Mapped
values** link is displayed. The link opens a window to map multiple Salesforce
fields to Zendesk fields.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/salesforce_data_sync_picklist_2.png)

In this instance, avoid mapping multiple Salesforce fields to a single field in
Zendesk. Otherwise, only the last Salesforce field mapped will be synced.

The following Salesforce fields are not supported for mapping:

- Text area (long)
- Text area (rich)
- Text area (encrypted)
- Lookup field — Salesforce lookup fields cannot be mapped to Zendesk because the
  lookup fields values are stored in a related Salesforce object
- Record type ID

### Salesforce accounts to Zendesk organizations field mapping

In **Data Sync** > **Accounts to Organizations sync**, the **Field
mapping** section maps the Salesforce account fields you want to populate
with Zendesk organization fields. This controls which field in the Salesforce
account record is synced as its related organization name. By default, this is
set to **Account Name to Organization Name**.

The drop-down options in the Zendesk field vary according to the type of field
you select in the Salesforce drop-down. The following table shows which
Salesforce field types can be mapped to Zendesk field types.

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| **Salesforce field type** | **Text** | **Drop-down** | **Decimal** | **Checkbox** | **Date** | **Numeric** |
| ID | ✓ |  |  |  |  |  |
| String | ✓ |  |  |  |  |  |
| Phone | ✓ |  |  |  |  |  |
| Picklist | ✓ | ✓ |  |  |  |  |
| Currency | ✓ |  | ✓ |  |  |  |
| Boolean | ✓ |  |  | ✓ |  |  |
| Checkbox |  |  |  | ✓ |  |  |
| Date/Time | ✓ |  |  |  | ✓ |  |
| Number | ✓ |  |  |  |  | ✓ |
| Double | ✓ |  | ✓ |  |  |  |
| Date | ✓ |  |  |  | ✓ |  |
| Multi  picklist | ✓ |  |  |  |  |  |
| Email | ✓ |  |  |  |  |  |

### Salesforce contacts or leads to Zendesk users field mapping

In **Data Sync** > **Contacts/Leads to users sync**, the **Field
mapping** section maps Salesforce contact or lead fields you want to
populate with Zendesk user fields. This identifies which field in the Salesforce
contact or lead account record is synced as its related user. By default, field
mapping is set to **Email to Email**.

The drop-down options in the Zendesk field vary according to the type of field
you select in the Salesforce drop-down. The following table shows which
Salesforce field types can be mapped to Zendesk field types.

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| **Salesforce field type** | **Text** | **Drop-down** | **Decimal** | **Checkbox** | **Date** | **Numeric** |
| ID | ✓ |  |  |  |  |  |
| String | ✓ |  |  |  |  |  |
| Phone | ✓ |  |  |  |  |  |
| Picklist | ✓ | ✓ |  |  |  |  |
| Currency | ✓ |  | ✓ |  |  |  |
| Boolean | ✓ |  |  | ✓ |  |  |
| Checkbox |  |  |  | ✓ |  |  |
| Date/Time | ✓ |  |  |  | ✓ |  |
| Number | ✓ |  |  |  |  | ✓ |
| Double | ✓ |  | ✓ |  |  |  |
| Date | ✓ |  |  |  | ✓ |  |
| Multi  picklist | ✓ |  |  |  |  |  |
| Email | ✓ |  |  |  |  |  |

## Checking your data sync setup

Use the following checklist to help check your data sync is setup correctly:

1. Ensure you have the correct [Salesforce API settings](#topic_mpl_nw4_rjb) requirements for the
   integration.
2. Confirm you have only connected one Salesforce account to one Zendesk
   account.
3. Sync filter: Confirm you aren't using unsupported Saleforce fields
   such as Formula Field and Lookup field.
4. Sync filter: Confirm you're using the correct syntax in the sync
   filter values. These are case-sensitive and must exactly match the Salesforce
   field value. If you're using a Salesforce picklist field for filtering, the
   value is the API name.
5. Sync field mapping: Check the field mapping includes **Name to
   Name**. This is mandatory because organizations can't be created in
   Zendesk without a name.
6. Sync field mapping: If you added or removed Zendesk dropdown field options or
   Salesforce picklist options, you may need to remove and remap the field to
   resolve sync errors or add new options.
7. When testing the sync, did you make updates to the Salesforce fields that are
   mapped to Zendesk? Sync is only triggered when a mapped field is updated.
8. If you have **Validate user phone numbers** enabled on the [End users page in Admin Center](https://support.zendesk.com/hc/en-us/articles/4408883052442#validate_phone),
   Zendesk verifies that all phone numbers synced from Salesforce use a valid [international E.164 format](https://www.twilio.com/docs/glossary/what-e164). To avoid phone number
   validation errors in Zendesk Support, format phone numbers using the E.164
   format in Salesforce, which includes the plus sign (**+**). For more
   information, see [Why do phone numbers synced from Salesforce
   lose their country code?](https://support.zendesk.com/hc/en-us/articles/4468066453274)
9. Picklist values: If there are straight quotes (") in the API Name of a picklist
   value, Salesforce causes the sync to fail with an error. Replace straight quotes
   with curly quotes instead.