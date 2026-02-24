# Bulk importing user data (legacy)

Source: https://support.zendesk.com/hc/en-us/articles/10077720640026-Bulk-importing-user-data-legacy

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

Verified AI summary ◀▼

Admins can bulk import user data using a CSV file to add or update user information, including roles and organization memberships. Before importing, ensure data imports are enabled and organizations are imported first. Note limitations like a 2,000-row maximum per file and the inability to import certain data types. Consider your welcome email settings to manage notifications for new users.

Location: Admin Center > Objects and rules > Tools > Data importer

Zendesk recommends using the [data importer](https://support.zendesk.com/hc/en-us/articles/4408893496218) to import user data instead of the legacy Bulk actions page described in this article. However, if you prefer, you can still use the Bulk actions page to import new or updated user information.

Admins can add many users in a bulk import rather than adding users manually one at a time. To do this, you create a comma-separated values (CSV) file that contains the user's data. In addition to essential user data, such as email address and phone number, you can also set user roles, define an agent's privileges, and add users to an organization. You can use bulk import to either add new users or update existing ones.
Bulk import via a CSV file only works for Support users and roles.

You must be an administrator to bulk import users and organizations.

Important:

- To protect the data in your Zendesk account, data imports are not enabled by default. The account owner or an admin must contact [Zendesk Customer Support](https://support.zendesk.com/hc/en-us/articles/4408843597850) to enable data exports and access to the imports page.
- If you want to bulk import both users and organizations, you must [import organizations](https://support.zendesk.com/hc/en-us/articles/4408885980186) first.

This article contains the following sections:

- [Considerations for bulk importing users (legacy)](#topic_py1_5kx_2fc)
- [Creating the CSV user data file (legacy)](#topic_svw_jdl_db)
- [Using a bulk actions import to import user data (legacy)](#topic_nly_lm1_5cc)

## Considerations for bulk importing users (legacy)

There are several limitations and considerations you should review before bulk importing users.

### Limitations for bulk importing users and organizations (legacy)

You can import a core set of data about users and organizations. For example, you can import the data described in the table below. However, you can't import time zones, photos, language preferences, and other data. To import data not listed in the table below, you must use the Zendesk REST API instead. See [Importing users with the Zendesk API](https://developer.zendesk.com/rest_api/docs/core/users) or [Importing organizations with the Zendesk API](https://developer.zendesk.com/rest_api/docs/core/organizations#content).

- When using the Bulk actions pages, the import CSV data file can contain a maximum of 2,000 rows. That is, one header row and up to 1,999 rows of data.
- Don't include the same user or organization more than once within a CSV file. Doing so can cause your import to fail.
- There's no guarantee that records are created or updated in the order they appear in the CSV file.
- You can only import one CSV file at a time. Therefore, if you have more data than the maximum number of rows supported for the CSV file, you must create separate files for each batch and import them one after another. When you're not using the data importer, up to two batches are queued and run in the background. If you want to import more than two batches, you need to wait until the first batches are finished importing to add more.
- You cannot use bulk importing to import contact information from end-user Facebook or X (formerly Twitter) accounts. Instead, use the Zendesk REST API. See [Importing users with the Zendesk API](https://developer.zendesk.com/rest_api/docs/core/users).

### How data is updated by the bulk actions import (legacy)

When using the legacy bulk actions page to import user data, the following user data is replaced:

- name
- external\_id
- role
- restriction
- organization
- custom fields
- tags (only when using the data importer)

The following user data is appended (added to the existing data):

- details
- notes
- tags
- phone (added as a secondary phone number)
- email (added as a secondary email address)

### Deciding whether to send an email to users imported in bulk (legacy)

Before you perform a bulk import of users, it's important to [check your welcome email settings](https://support.zendesk.com/hc/en-us/articles/4408824350746).
When you add new users via a bulk import while Guide is enabled, each user receives the welcome email message. The welcome email contains a link to verify their email address, which prompts them to select a password and then sign in.
You can prevent the welcome email from being sent to these users.

**To prevent the welcome email message being sent to users**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_people_icon.png)
   **People** in the sidebar, then select **Configuration > End users**.
2. In the **User welcome email** section, deselect **Also send a verification email when a new user is created by an agent or administrator**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/bulk_import_disable_welcome_email.png)
3. Click **Save**.

## Creating the CSV user data file (legacy)

When you create a list of users to import, you'll probably generate this list from some other user management system, such as an employee database. Most of these systems have some facility for creating a CSV export file. If you need to create the list from scratch, you can use a program like Microsoft Excel or OpenOffice.org Calc.

Here are some important things to keep in mind when creating your file:

- The file must be properly formatted CSV and saved using UTF-8 character encoding.
- The first row of the CSV file is the header row, and you must include it in the file.
- The header row must contain any required fields in the table below, plus any other fields listed in the table below that you want to include.
- Included fields must appear in the header row in the order they are listed below.
- If you are not importing data for a field, do not list it in the header row.
- Empty columns of data in the file will overwrite most existing data for that user. For exceptions, see [How data is updated by the bulk actions import](#topic_mpt_fxg_g2c).
- Add line breaks to notes or multiline custom fields by pressing ALT+ENTER on Windows or CTRL+OPTION+RETURN on a Mac.

Note: Microsoft Excel cannot save your file immediately. To save your file, upload it to Google Sheets, re-download it, and then upload it to Zendesk. You can also use Open Office to save the file.

The following table lists the fields that you can include in the file. The name, email, and restriction fields are all required when importing new users. When existing users are updated via bulk import, only one unique identifier is required (such as an email or external ID).

Table 1. User import data

| Field | Description |
| --- | --- |
| name | **Required for importing new users**. User's full name. |
| email | **Required for importing new users**. User's full email address (someuser@mycompany.com). The email field accepts a blank or empty value. If the email field is blank or empty, the system still creates the user profile. |
| restriction | **Required for importing new users**. Restriction sets the team member's or end user's privileges, the tickets they have access to, etc. This is required to import new users when the user's role is set to *Agent* On non-Enterprise plans, the following restriction values are supported: - **assigned**: The team member can access only   tickets assigned to them. - **groups**: The team member can access only   tickets within their group(s). **Note**: To add a   team member to a group, see [Viewing and   managing team member group membership](https://support.zendesk.com/hc/en-us/articles/4408821536794) or   use the [Support   API](https://developer.zendesk.com/rest_api/docs/support/introduction). - **none**: The user has no restrictions and can   access all tickets. - **organization**: The user can access only   tickets requested by them or other users in their   organization - **requested**: The user can access only their own   tickets. They must be listed as the ticket's   requester. - (not data importer) **Light Agent**: The user is   given the same [restrictions](https://support.zendesk.com/hc/en-us/articles/4408846501402#topic_p5d_zcr_pv)   as a light agent. Restriction values of "organization" and "requested" can be assigned when the user's role is set to "End-user". All others apply only to team members. Note: On Enterprise plans, agent roles override the standard agent restrictions. This means that you can't use any of the standard restrictions listed in the table above to import or update an agent. You must specify an agent role. If you accidentally use a role name that doesn't exist in Support, the user's role defaults to Light Agent. |
| external\_id | If you have an ID other than the user's email address (such as an employee ID or customer reference number), you can include it here. External IDs must be unique for each user, or data will be overwritten. If you need to configure multiple email addresses or phone numbers for a single user, you can do so by creating multiple entries for the user in the CSV file and using the same external\_id column for all rows you want associated with a single user. With the exception of the additional email or phone numbers, the values in all other columns should remain the same for each row. If any external ID, email address, or phone number matches more than one existing user, that row is rejected from the bulk import. Note: If you import users with the external\_id field as their only identifier (meaning you're not also including email address), you still need to include the email field in the CSV file, with no data. For example: |
| details | Detailed information concerning this user, such as an address. This information is visible to team members only, not to end users. |
| notes | Notes concerning this user. Notes are visible to team members only, not to end users. |
| phone | The user's telephone numbers. Unique phone numbers are added as direct lines. Phone numbers that already exist are added as secondary lines. [To work with Zendesk](https://support.zendesk.com/hc/en-us/articles/4408823756570), phone numbers should be formatted with the internationally standardized [E.164](https://en.wikipedia.org/wiki/E.164) format. |
| shared\_phone\_number | If this is a shared phone number, set to "true". A shared phone number cannot be used as a [user identity](https://developer.zendesk.com/api-reference/ticketing/users/user_identities/). |
| role | Case sensitive: **End-user**, **Agent**, or **Admin**. If you don't set a role, the user is set to **End-user**. |
| organization | The name of the organization that the user will be added to. The organization must already exist, or the import will fail. On Professional and Enterprise plans, you can add a user to multiple organizations by separating the organization names with a pipe character. For example: `Organization1|Organization2|Organization3` A user's default organization is set to the first organization alphabetically. It isn't possible to set a different default organization during a bulk import. However, the default organization for a user can be adjusted manually or with the [Support API - Set Membership as Default](https://developer.zendesk.com/rest_api/docs/support/organization_memberships#set-membership-as-default) endpoint. |
| tags | When user and organization tagging has been enabled for Zendesk Support (see [Adding tags and users to organizations](https://support.zendesk.com/hc/en-us/articles/4408881573658)), you can add user tags. Separate each tag with a comma. |
| brand | If the account has multiple brands, you can specify a brand subdomain. The brand subdomain you specify determines the brand of the welcome email sent to the user, as long as that brand is active and has an enabled help center. If the brand subdomain you specify is not active, doesn't have an enabled help center, or doesn't exist, the column is ignored, and the welcome email is sent using the default brand. Brand subdomains are case-sensitive and must be an exact match to be imported. Specify only the name of the brand subdomain. For example, use **mydomain** and not **mydomain.zendesk.com**. |
| custom\_fields.*<field key>* | When you perform a bulk user import, you can import a custom user field by specifying the **custom\_fields.** prefix and the field key. For example, for the field key **subscription\_date**, use the following to set the imported values for this field. ``` custom_fields.subscription_date ``` Note that custom field keys are case-sensitive and must be entered in lowercase letters. If you are importing information into a checkbox, enter 'true' to have it checked or 'false' to leave it unchecked. To set the value of drop-down list options, use the tag you added when you created the drop-down list. For custom date fields, use either the YY/MM/DD or YYYY-MM-DD format. To locate the key for a custom user field: - In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click    **People** in the sidebar, then select **Configuration > User fields**.Then click the name of the custom field. The field   key appears in the properties panel on the   right. If a field value is not formatted correctly, the import will fail, and you will receive an error report specifying which records failed to save. Note: If the custom user field you're importing is a [lookup relationship field](https://support.zendesk.com/hc/en-us/articles/4591924111770), enter the ID of the related object as the value for this field. For example, for an organization, enter the organization's ID; for a user, enter the user's ID; for a custom object record, enter the record's ID. To find an organization, user, or custom object record ID, you can [export data from your account](https://support.zendesk.com/hc/en-us/articles/4408886165402) or use the [Organizations API](https://developer.zendesk.com/api-reference/ticketing/organizations/organizations/#list-organizations), [Users API](https://developer.zendesk.com/api-reference/ticketing/users/users/#list-users), or [Custom Object Records API](https://developer.zendesk.com/api-reference/custom-data/custom-objects/custom_object_records/#list-custom-object-records). |

## Using a bulk actions import to import user data (legacy)

Although Zendesk recommends using the data importer, you can still use the Bulk actions pages to import new and updated information for users.

**To import the CSV user data**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_people_icon.png)
   **People** in the sidebar, then select **Bulk actions > Import users**.
2. Select import options:
   - **Create new users**: This is selected by default and cannot be deselected. This is because users listed in the CSV file that don't exist in your Zendesk account are always created.
   - **Update existing users**: Select this import option if you also want to modify data for existing users.

     An external\_id or email address must be included in the CSV file for each user so that they can be identified. Other than user identification fields, only include the fields you want to update in your CSV file. If you don't enter a value for a field in your CSV file, that value is overwritten for the existing user.

     If any external ID, email address, or phone number matches more than one existing user, that row is rejected from the bulk import.

   Note: If you don't want to add new users, you must use the [data importer](https://support.zendesk.com/hc/en-us/articles/4408893496218). When using the Bulk actions pages, if your CSV file contains information about new users, they are always added, regardless of the import option you select.
3. (Optional) Select **Include external ID in CSV output file**.

   When the import process is complete, you will receive an email notification that includes a link to a separate CSV import results file. Use this link to download the file and view the results of your import. The file shows the status of the user data that you attempted to import (Created, Updated, Failed, Unchanged). If you select this option, the report includes the email address or an external ID for each user that is created or updated.

   If you don't select this option, external IDs are excluded from the CSV import results file. Instead, only the user's email address is listed for each user that is created or updated.
4. Click one of the following: **Choose File** or **Let me paste in data instead**.
5. Click **Import**.

Your import is added to the queue, and the users are added to Zendesk Support when the import process is complete. You'll receive an email when the import is complete.