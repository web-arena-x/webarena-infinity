# Bulk importing user data with the data importer

Source: https://support.zendesk.com/hc/en-us/articles/4408893496218-Bulk-importing-user-data-with-the-data-importer

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

Verified AI summary ◀▼

Admins can bulk import user data using a CSV file to add or update users
and set roles and privileges. Before importing, ensure data imports are
enabled and organizations are imported first. Consider file size limits,
data updates, and email notifications. Use the data importer tool to
manage imports, ensuring correct field mapping and reviewing import details.

Location: 
Admin Center > Objects and rules > Tools > Data importer

Admins can add many users in a bulk import rather than adding users manually
one at a
time. To do this, you create a comma-separated values (CSV) file that
contains the
user's data. In addition to essential user data, such as email address
and phone number,
you can also set user roles, define an agent's privileges, and add users
to an
organization. You can use bulk import to either add new users or update
existing ones.
Bulk import through a CSV file only works for Support users and roles.

You must be an administrator to bulk import users and organizations.

Important:

- To protect the data in your Zendesk account, data imports
  are not enabled by
  default. The account owner or an admin must contact
  [Zendesk Customer Support](https://support.zendesk.com/hc/en-us/articles/4408843597850)
  to enable
  data exports and access to the imports
  page.
- If you want to bulk import both users and organizations,
  you must
  [import organizations](https://support.zendesk.com/hc/en-us/articles/4408885980186)
  first.

This article contains the following topics:

- [Considerations for bulk importing users](#topic_vpj_tl1_5cc)
- [Creating the CSV user data file](#topic_svw_jdl_dc)
- [Using the data importer to import user data](#topic_syb_lm1_5cc)

## Considerations for bulk importing users

There are a variety of limitations and considerations you should
review prior to bulk
importing users:

- [Limitations for bulk importing
  with the data importer](#id_j2z_vlx_2fc)
- [Updating existing user profile data](#topic_bck_td1_zg)
- [Deciding whether to send an email to users imported in bulk](#topic_cvj_4rx_jh)

### Limitations for bulk importing with the data importer

You can import a core set of data about users and organizations.
To import data not listed
in the table below, you must use the Zendesk REST API instead.
See
[Importing
users with the Zendesk API](https://developer.zendesk.com/rest_api/docs/core/users).

- When using the data importer, the import CSV file can't exceed
  1 GB in size. We
  recommend a maximum of 500,000 rows. That is one header row
  and up to 499,999 rows of
  data. Furthermore, each row can't exceed 128 KB in size.
- The import CSV file can contain a maximum of 200 columns.
- The import CSV file can't guarantee import order for rows.
- Don't include the same user or organization more than once
  within a CSV file. Doing so
  can cause your import to fail.
- There's no guarantee that records are created or updated
  in the order they appear in the
  CSV file.
- You can only import one CSV file at a time. Therefore, if
  you have more data than the
  maximum number of rows supported for the CSV file, you must
  create separate files for each
  batch and import them one after another. When you're not
  using the data importer, up to
  two batches are queued and run in the background. If you
  want to import more than two
  batches, you need to wait until the first batches are finished
  importing to add more.
- You cannot use the bulk importer to import contact information
  from end-user Facebook or
  X (formerly Twitter) accounts. Instead, use the Zendesk REST
  API. See
  [Importing
  users with the Zendesk API](https://developer.zendesk.com/rest_api/docs/core/users).

### Updating existing user profile data

When performing a bulk import, you can update existing users.
Be aware that some
data is replaced, and some is just appended to the existing data.

Note: To update an existing
user, the CSV file must include
the user's external\_id or email address so that Zendesk can
identify
them.

#### How data is updated by the data importer

When using the data importer, only the following user data
is appended (added
to the existing data):

- phone (added as a secondary phone number)
- email (added as a secondary email address)

All other data is replaced by the data importer.

### Deciding whether to send an email to users imported in bulk

Before you perform a bulk import of users, it's important to
[check your welcome email settings](https://support.zendesk.com/hc/en-us/articles/4408824350746).
When you add new users via a bulk import while Guide is enabled,
each user
receives the welcome email message. The welcome email contains
a link to verify
their email address, which prompts them to select a password
and then sign in.
You can prevent the welcome email from being sent to these users.

**To prevent the welcome email message being sent to users**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_people_icon.png)
   **People** in the sidebar, then select **Configuration > End users**.
2. In the **User welcome email**
   section, deselect
   **Also send a
   verification email when a new user is created by an agent or
   administrator**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/bulk_import_disable_welcome_email.png)
3. Click **Save**.

## Creating the CSV user data file

When you create a list of users to import, you'll probably generate
this list from
some other user management system, such as an employee database.
Most of these
systems have some facility for creating a CSV export file. If you
need to create the
list from scratch, you can use a program like Microsoft Excel or
OpenOffice.org
Calc.

Here are some important things to keep in mind when creating your
file:

- You can download a CSV template in Admin Center > Data
  importer > Import >
  **Download a CSV template**.
- The file must be properly formatted CSV and saved using UTF-8
  character
  encoding.
- The first row of the CSV file is the header row, and you
  must include it in
  the file.
- The header row must contain any required fields in the table
  below, plus any
  other fields listed in the table below that you want to include.
- Included fields must appear in the header row in the order
  they are listed
  below.
- If you are not importing data for a field, do not list it
  in the header row.
- Empty columns of data in the file will overwrite most existing
  data for that
  user. For exceptions, see
  [Updating existing user profile data](#topic_bck_td1_zg).
- Add line breaks to notes or multiline custom fields by pressing
  ALT+ENTER on
  Windows or CTRL+OPTION+RETURN on a Mac.

Note: Microsoft Excel cannot save
your file immediately. To
save your file, upload it to Google Sheets, re-download it, and
then upload it
to Zendesk. You can also use Open Office to save the file.

The following table lists the fields that you can include in the
file. The name,
email, and restriction fields are all required when importing new
users. When
existing users are updated via bulk import, only one unique identifier
is required
(such as an email or external ID).

Table 1. User import data

| Field | Description |
| --- | --- |
| name | *Required for importing new users.* User's full name. |
| emails | *Required for importing new users.* User's full email address (someuser@mycompany.com). If including more than one email address for a user, separate them by a pipe (|). For example: `first@yourcompany.com|second@yourcompany.com` |
| ticket\_restriction | *Required for importing new users.* Restriction sets the team member's or end user's privileges, the tickets they have access to, etc. This is required to import new users when the user's role is set to Agent. On non-Enterprise plans, the following restriction values are supported:  - **assigned**:   The team member can access only   tickets assigned to them. - **groups**:   The team member can access only   tickets within their group(s). To   add a team member   to a group, see   [Viewing and   managing team member group membership](https://support.zendesk.com/hc/en-us/articles/4408821536794)   or   use the   [Support   API](https://developer.zendesk.com/rest_api/docs/support/introduction). - **none**:   The user has no restrictions and   can   access all tickets. - **organization**:   The user can access only   tickets requested by them or other   users in their   organization. - **requested**:   The user can access only their own   tickets. They must be listed as the   ticket's   requester. Restriction values of **organization** and **requested** can be assigned when the user's role is set to End-user. All others apply only to team members. Note: On Enterprise plans, agent roles override the standard agent restrictions. This means that you can't use any of the standard restrictions listed in the table above to import or update an agent. You must specify an agent role. If you accidentally use a role name that doesn't exist in Support, the user's role defaults to Light Agent. |
| external\_id | If you have an ID other than the user's email address (such as an employee ID or customer reference number), you can include it here. External IDs must be unique for each user, or data will be overwritten. If you need to configure multiple email addresses or phone numbers for a single user, you can do so by creating multiple entries for the user in the CSV file and using the same external\_id column for all rows you want associated with a single user. With the exception of the additional email or phone numbers, the values in all other columns should remain the same for each row.  If any external ID, email address, or phone number matches more than one existing user, that row is rejected from the bulk import.  Note: If you import users with the external\_id field as their only identifier (meaning you're not also including email address), you still need to include the email field in the CSV file with no data. For example: |
| details | Detailed information concerning this user, such as an address. This information is visible to team members only, not to end users. |
| notes | Notes concerning this user. Notes are visible to team members only, not to end users. |
| phones | The user's telephone numbers. Unique phone numbers are added as direct lines. Phone numbers that already exist are added as secondary lines. If you're including more than one phone number for a user, separate the phone numbers with a pipe (|). [To work with Zendesk](https://support.zendesk.com/hc/en-us/articles/4408823756570), phone numbers should be formatted with the internationally standardized [E.164](https://en.wikipedia.org/wiki/E.164) format. |
| shared\_phone | The user's shared telephone number. [To work with Zendesk](https://support.zendesk.com/hc/en-us/articles/4408823756570), phone numbers should be formatted with the internationally standardized [E.164](https://en.wikipedia.org/wiki/E.164) format. |
| role | Case sensitive: **end-user** or **agent**. If you don't set a role, the user is set to **end-user**. |
| custom\_role | When the role is set to Agent, specify the custom role name, as listed on the [Roles page](https://support.zendesk.com/hc/en-us/articles/4409148517658) in Admin Center. **Light agent** is also accepted. |
| skip\_verify\_email | If you need to create users without sending out a verification email, set this value to **true**. |
| time\_zone | Consists of a string such as "Eastern Time (US & Canada)". For a list of valid names, view the Time zone list menu on the Localization page (Account > Appearance > Localization) in Admin Center. Example: If the menu lists "(GMT+02:00) Berlin", then use "Berlin" as the time\_zone name. |
| locale | The user's locale. A BCP-47 compliant tag for the locale (e.g. en-US). If both locale and locale\_id are present, locale\_id is ignored and only locale is used. |
| local\_id | The user's language identifier. |
| moderator | Boolean. Designates whether the user has forum moderation capabilities. |
| only\_private\_comments | Boolean. When set to **true**, the user can only create private comments. |
| remote\_photo\_url | A URL pointing to the user's profile picture. |
| signature | The user's signature. Only agents and admins can have signatures. |
| suspended | Boolean. Indicates whether the user is suspended. Tickets from suspended users are also suspended, and these users cannot sign in to the end-user portal. |
| alias | An alias displayed to end users. |
| organizations | The name of the organization that the user will be added to. The organization must already exist, or the import will fail. On Professional and Enterprise plans, you can add a user to multiple organizations by separating the organization names with a pipe character. For example: `Organization1|Organization2|Organization3`. A maximum of 50 organizations are allowed.  A user's default organization is set to the first organization alphabetically. It isn't possible to set a different default organization during a bulk import. However, the default organization for a user can be adjusted manually or with the [Support API - Set Membership as Default](https://developer.zendesk.com/rest_api/docs/support/organization_memberships#set-membership-as-default) endpoint. |
| default\_group\_id | New team members (admins and agents) are automatically added to the account's [default group](https://support.zendesk.com/hc/en-us/articles/4408828237722). However, you can use this field to specify alternative default groups for users during bulk imports.  End users can't be added to groups. |
| tags | When user and organization tagging has been enabled for Zendesk Support (see [Adding tags and users to organizations](https://support.zendesk.com/hc/en-us/articles/4408881573658)), you can add user tags. Separate each tag with a comma. |
| custom\_fields.*<field key>* | When you perform a bulk user import, you can import a custom user field by specifying the `custom_fields.` prefix and the field key. For example, for the field key `subscription_date`, use the following to set the imported values for this field.  ``` custom_fields.subscription_date ```  Custom field keys are case-sensitive and must be entered in lowercase letters.  If you are importing information into a checkbox, enter **true** to have it checked or **false** to leave it unchecked. To set the value of drop-down list options, use the tag you added when you created the drop-down list. For custom date fields, use either the YY/MM/DD or YYYY-MM-DD format.  To locate the key for a custom user field:  - In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click    **People** in the sidebar, then select **Configuration > User fields**.   Then, click the name of the custom   field.   The field key appears in the properties   panel on the   right.  If a field value is not formatted correctly, the import will fail, and you will receive an error report specifying which records failed to save.  Note: If the custom user field you're importing is a [lookup relationship field](https://support.zendesk.com/hc/en-us/articles/4591924111770), enter the ID of the related object as the value for this field. For example, for an organization, enter the organization's ID; for a user, enter the user's ID; for a custom object record, enter the record's ID. To find an organization, user, or custom object record ID, you can [export data from your account](https://support.zendesk.com/hc/en-us/articles/4408886165402) or use the [Organizations API](https://developer.zendesk.com/api-reference/ticketing/organizations/organizations/#list-organizations), [Users API](https://developer.zendesk.com/api-reference/ticketing/users/users/#list-users), or [Custom Object Records API](https://developer.zendesk.com/api-reference/custom-data/custom-objects/custom_object_records/#list-custom-object-records). |

## Using the data importer to import user data

You can use the data importer to import a CSV file that creates or
updates existing
users, and captures logs of all imports attempted through the Data
importer
page.

**To add or update users with the data importer**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_objects_rules_icon.png)
   **Objects and rules** in the sidebar, then select **Tools > Data importer**.
2. Click **Import**.
3. Under **Target destination**, select
   **Users**.
4. Under **Import type**, choose one
   of the following:
   - **Create only**: Only new
     users are added. Any data in the CSV
     file pertaining to existing users is ignored.
   - **Update only**: Update
     data for the existing users listed in
     your CSV file. The *external\_id*
     is required to update users.
     Any data pertaining to new users is ignored.
   - **Create and update**:
     Add new users and update data for the
     existing users listed in your CSV file.

   Note: If any external
   ID, email address, or phone
   number matches more than one existing user, that row
   is rejected from
   the bulk import. Check your
   [import history](https://support.zendesk.com/hc/en-us/articles/5789034291738).
5. Under **File upload**, drag and
   drop your file or **click to upload**
   and select your CSV file from the file browser.

   If you need to change the
   file you've selected, click the delete icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sell_icon_trashcan.png))
   next to the file name.
6. Click **Next**.
7. Review the **Field mapping** list.
   - If the field mapping is correct, click
     **Next**.
   - If the field mapping isn't correct, click
     **Back**. Edit your CSV
     file to adhere to the
     [format requirements](#topic_svw_jdl_dc),
     then reupload the file.
8. Review the summary of import details in the confirmation
   dialog and then
   click **Start import**.

   After the import starts, the imported changes
   can't be reverted. To check the status of an import,
   check your
   [import history](https://support.zendesk.com/hc/en-us/articles/5789034291738).