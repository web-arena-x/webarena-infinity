# Top feature recommendations for business-to-business (B2B) support 

Source: https://support.zendesk.com/hc/en-us/articles/5194505387674-Top-feature-recommendations-for-business-to-business-B2B-support

---

When you provide products or services to another business, this is known as a
business-to-business (or B2B) service.

Zendesk supports many B2B businesses. When we look at feature usage across all the
businesses in that user segment, there are three features that B2B businesses, just like
yours, are using disproportionately more than the other business types, B2E and B2C.

Based on feature usage across B2B businesses, we recommend these features to optimize
your setup:

- [Organizations](#topic_nhw_tpj_dwb), to help you keep
  track of what businesses are requesting.
- [Organization fields](#topic_alw_3gg_jwb) help to
  keep customer information right where you need it.
- [Service level agreements](#topic_r1z_5qj_dwb), to
  help you deliver predictable support.
- [Integrate other business
  services](#topic_kxz_5qj_dwb), to expand the capabilities of the suite.

B2B businesses rely on these features, in addition to the [core feature setup](https://support.zendesk.com/hc/en-us/articles/4408824587802) recommended for all business types. Also,
be sure to check out these [examples for basic setup for B2B businesses](https://support.zendesk.com/hc/en-us/articles/4408825510938).

## Create organizations to effectively manage users

As a B2B organization, you might deal with multiple businesses. By arranging your end
users into [Organizations](https://support.zendesk.com/hc/en-us/articles/4408886146842) (typically a company name),
you can more efficiently keep track of what those organizations are requesting.
Organizations are usually collections of your end users, but they can also include
agents.

### Example

Let’s say you’re part of MegaCorp's IT department.

You may want to create organizations for each of the departments and
divisions in your company. Or, maybe you want to base your organizations on
geographic areas, so requests can be routed to local IT analysts and fixed
faster. You can add “conditions”, based on MegaCorp's organizations, to
triggers, automations, macros, and views to make it easier to work with your
tickets.

Each of these organizations is a department at your company:

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/b2e_people_orgs.png)

You may want to create groups based on common types of IT requests such
as computers and equipment, software, urgent care, meeting rooms, or internet
and security. You can add “actions” based on groups to triggers, automations,
and macros, but not views.

Each of these groups is for types of requests you frequently get:

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/b2e_people_groups.png)

### How to

Use this procedure to create an organization for the MegaCorp company.

**To create an organization**

1. In [Support](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click the
   **Organizations** icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/organizations_icon.png)) in the sidebar.
2. Click **Add organization**. Alternatively, hover over the **+Add** tab
   in the top toolbar, then select **Organization.**

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/add_buttons_support_3.png)
3. Enter a unique **Name** for the organization, in this case,
   "MegaCorp".
4. If you want to set up [user mapping](https://support.zendesk.com/hc/en-us/articles/4408882246298#topic_nxl_vdt_bc), in **Domains**,
   enter an email domain, in this case, "megacorp.com." This means that any new
   users who submit a ticket from the megacorp.com domain will automatically be
   added to the MegaCorp organization.
5. Click **Save**.
6. Now, on the **Organizations** page, you can click the **MegaCorp**
   organization to see all tickets from that domain.

### Pro tip

You can create organizations that mirror the [service level agreements](https://support.zendesk.com/hc/en-us/articles/4408829459866) that you've
established with your customers rather than mirroring a company or location. For
example, your paying customers are guaranteed a faster response than those who
use your free services and you want to distinguish between the two.

## Put customer information at your fingertips with organization fields

Building on organizations, [organization fields](https://support.zendesk.com/hc/en-us/articles/4408842677786) enable you to store further
information about an organization that cannot be stored using the built-in fields.
Storing this information can save time for both you and your customers as you won't
have to keep asking customers for information every time they contact you.

### Example

As an admin for MegaCorp, you provide support to organizations from around the
world. To help you address issues quicker, you want to add information about the
country of each organization and the main contact name for that organization.
You can do this with organization fields.

To add the country to your organization, you can create a drop-down field
containing the countries you interact with. Then, you can easily select the
country for each organization.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/cross_product_feature_recs_b2b.png)

To add the main contact name, you can add a text field to the organization.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/cross_product_feature_recs_b2b2.png)

Now, for each organization, you can select a country and enter a contact
name.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/cross_product_feature_recs_b2b3.png)

### How to

Use this procedure to create new fields for your organizations.

**To create an organization field**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_people_icon.png)
   **People** in the sidebar, then select **Configuration > Organization
   fields**.
2. Click **Add field**.
3. Select a **field type**, then enter a **Display name**.
4. Verify that the **field key** is the value you want it to be. This field
   is populated by the field name, but you can edit it. You can't change the
   field key after the custom field is created. The field key can be used to
   reference the custom field in placeholders and the API.
5. Enter Field options to include in the list. Click the **X** to remove a
   value.
6. Click **Save** or, to create another custom field, click the drop-down
   icon and select **Save and add another**.
7. Your new fields are active by default and are added to all
   organizations.

### Pro tip

Custom fields work great with triggers. Using the example above, you could set up
a trigger that automatically sets tickets from an organization in France to
high priority:

1. Set the trigger condition to **Country** > **Is** >
   **France**.
2. Set the trigger action to **Priority** > **High**.

For help with triggers, see [About triggers and how they work](https://support.zendesk.com/hc/en-us/articles/4408822236058).

## Deliver predictable support with Service level agreements

A [Service Level Agreement, or SLA](https://support.zendesk.com/hc/en-us/articles/4408829459866), is an
agreed-upon measure of the response and resolution times your support team delivers
to your customers. This ensures that you're delivering measured and predictable
service. As a B2B business you'll likely want to make sure that incoming tickets are
addressed by your agents as quickly as possible. You can use SLAs to quickly
identify areas of your support that could be improved.

To learn more about SLAs, see [Defining and using SLA policies](https://support.zendesk.com/hc/en-us/articles/4408829459866).

### Example

Let's say that you are dealing with a business named, "MegaPets." You've agreed
with MegaPets that you'll reply to all tickets they submit within 24 hours. You
can use an SLA to learn which tickets are waiting more than 24 hours for a
response and use this information to improve you support response.

You can set up an SLA with a condition that applies to all tickets in the
MegaPets organization. Tickets must have a priority set in order for the SLA to
process.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/b2b1.png)

You can then set targets for the SLA, in this case using the **First reply time
metric**:

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/b2bsla_targets.png)

### How to

Use these instructions to learn how to set up an SLA policy.

**To set up an SLA policy**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_objects_rules_icon.png)
   **Objects and rules** in the sidebar, then select **Business rules >
   Service level agreements**.
2. Click **Add policy**.
3. Enter a name in the **Policy Name** field.
4. Optionally, enter a description in the **Description** field.
5. In the **Conditions** section, select the conditions for this policy.
   Start typing the condition to auto-complete or select an option from the
   drop-down menu.
6. In the **Targets** section, enter a time target for each metric and
   ticket priority.
7. When you're finished, click **Save**.

   The SLA will now run on any new
   tickets (with a priority set) that are created.

You can use [Zendesk Explore](https://support.zendesk.com/hc/en-us/articles/4408835960602) to monitor whether you
are meeting your SLAs or not. See [this recipe](https://support.zendesk.com/hc/en-us/articles/4408835960602) for instructions.

### Pro tip

To get the best from SLAs and learn new tips, read [Fine Tuning: Succeeding with SLAs--why, when,
and how!](https://support.zendesk.com/hc/en-us/articles/4408822410650)

## Taking things further

If you rely on external services to help you manage parts of your business,
you can integrate many of these into your Zendesk account. This saves you time by
giving you a single view on your business information.

For example, if you also use Salesforce, JIRA, or Slack, you can manage
user data and ticket flows across those applications. You can also add apps from the
Zendesk Marketplace to integrate with popular services such as SurveyMonkey.

Examples of the available integrations include:

- [Salesforce](https://support.zendesk.com/hc/en-us/articles/4408954250010-Salesforce-integration): Enables Zendesk tickets to
  be viewed in Salesforce from an Account, Contact, Lead, or Opportunity page. You
  can also create and edit Zendesk tickets and sync Salesforce accounts to Zendesk
  organization data.
- [JIRA](https://support.zendesk.com/hc/en-us/articles/4408946742298-JIRA-integration): Enables near real-time syncing
  of data between Zendesk Support and Jira.
- [Slack](https://support.zendesk.com/hc/en-us/articles/4408954276890-Slack-integration): Connects a Zendesk subdomain to
  one or more Slack workspaces enabling you to interact with Zendesk Support
  tickets in your Slack channels.

For more details, see [Integrations](https://support.zendesk.com/hc/en-us/sections/4405303723802).