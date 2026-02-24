# Viewing and using the Team members page

Source: https://support.zendesk.com/hc/en-us/articles/4408843830938-Viewing-and-using-the-Team-members-page

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

Verified AI summary ◀▼

The Team members page lets you manage your team by adding or exporting agents and admins, adjusting roles, and viewing agent seat usage. You can search and filter team members by name, email, role, brand, group, and last sign-in, and sort them by sign-in or creation date. This central hub helps you efficiently organize and customize your support team.

Location:  Admin Center > People > Team > Team members

The **Team members** page in Zendesk Admin Center provides a central place
for administrators to add and manage team members (your staff, agents, and admins).

The Team members page provides a list of all [agents, admins, and the account owner](https://support.zendesk.com/hc/en-us/articles/4408883763866#topic_nqx_cbp_cc). It does
not display end users. If you're looking for more information about end users (also
called customers), see [Adding end users](https://support.zendesk.com/hc/en-us/articles/4408893585178).

The page also displays information about how many of your [agent seats](https://support.zendesk.com/hc/en-us/articles/4408834934554) you’ve used and a link to add additional seats.
For eligible [sales-assisted accounts](https://support.zendesk.com/hc/en-us/articles/4408833931674) and [self-service accounts](https://support.zendesk.com/hc/en-us/articles/4408833931674), you can instantly add more agent
seats from this page (see [Adding agents on-the-fly](https://support.zendesk.com/hc/en-us/articles/4408881540506#topic_wh1_qgf_5cb)).

Agents make up the majority of your team. They interact with your end users and
resolve tickets. Admins define the roles and privileges for agents and manage and
customize your Zendesk instance.

From the team members page, you can [add agents and admins](https://support.zendesk.com/hc/en-us/articles/4408886939930), [export team members](https://support.zendesk.com/hc/en-us/articles/5407034434842), [manage brand membership](https://support.zendesk.com/hc/en-us/articles/7584022494874), [manage group membership](https://support.zendesk.com/hc/en-us/articles/4408821536794#topic_dy3_zg3_zdc), search for team
members, and access their profiles to manage a team member's role and email addresses.
You can also access your own profile and manage your email addresses.

The following topics are covered in this article:

- [Accessing the Team members page](#topic_bgk_lfn_lqb)
- [Finding team members](#topic_prc_1qj_35b)

**Related articles**

- [Understanding Zendesk Support user roles](https://support.zendesk.com/hc/en-us/articles/4408883763866)
- [Adding agents and admins](https://support.zendesk.com/hc/en-us/articles/4408886939930)
- [Editing team member user profiles](https://support.zendesk.com/hc/en-us/articles/4408832485914)
- [Restricting agent ticket access by
  brand](https://support.zendesk.com/hc/en-us/articles/7584022494874)

## Accessing the Team members page

You’ll find the Team members page in Admin Center.

**To open the Team members page**

- In [Admin
  Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_people_icon.png)
  **People** in the sidebar, then select **Team > Team
  members**.

  The team members page opens.

  ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_teammember_brand_view.png)

## Finding team members

The list of team members can be searched by user profile properties, such as name and
email address, filtered by product roles, brand and group membership, and last
sign-in, and sorted by last sign-in and creation date. Additionally, you can modify
settings for any team member from the list.

### Searching for team members

Searching by name or email address is the quickest way to find a team member. You
can search the whole list, or you can filter the list and search only the
filtered results.

**To search for team members**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_people_icon.png)
   **People** in the sidebar, then select **Team > Team members**.
2. Enter a team member’s name, partial name, or email address in the search
   bar.

   Alternatively, you can search by other user properties, such as
   group assignments and status. For example, to search for all suspended
   team members, enter **is\_suspended:true** in the search bar.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/team_member_suspended.png)

   For a list of all
   the search parameters you can use to search team members, see [Searching users](https://support.zendesk.com/hc/en-us/articles/4408883318554#topic_duj_sbb_vc).

### Filtering the list of team members

You can filter the list by a team member’s role assignment per product,
by [brand membership](https://support.zendesk.com/hc/en-us/articles/7584022494874) if you support
multiple brands, by group membership, or by the date they last signed in.

Tip: If there is a certain filter or
combination of filters you think you’ll reuse, you can save and come back to
them later. To do so, apply the filters and bookmark the page in your
browser. You can then access the applied filters from the bookmark you
created in your browser.

**To filter the team list by product role**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_people_icon.png)
   **People** in the sidebar, then select **Team > Team members**.
2. Click **Filter**.
3. Use the **Product** and **role** fields to select **Any role** or a
   specific role type by product.

   More than one product and role can be
   selected. If you select roles for different products, the list will show
   team members who fill both of those roles. However, if you select
   multiple roles for a single product, the list will be filtered to show
   all team members with one of those roles. For example, filtering by
   Support Agent and Knowledge Agent would return team members who are
   agents for both Support and Knowledge, but if you filter by Support
   Agent and Support Admin, the list would reflect team members who are
   either agents or admins for Support.
4. Click **Apply filters**.

**To filter the team list by brand membership**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_people_icon.png)
   **People** in the sidebar, then select **Team > Team members**.
2. Click **Filter**.
3. Under **Brand membership**, select the brands by which you'd like to
   filter team members.

   Selecting multiple brands filters team members who
   are part of all the selected brands. To filter team members with no
   brand memberships, select **No brand**.
4. Click **Apply filters**.

**To filter the team list by group membership**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_people_icon.png)
   **People** in the sidebar, then select **Team > Team members**.
2. Click **Filter**.
3. Under **Group membership**, select the groups by which you'd like to
   filter team members.

   Selecting multiple groups filters team members who
   are part of all the selected groups. If a team member belongs to some of
   the selected groups, but not all, they won't show up in the filtered
   list.
4. Click **Apply filters**.

**To filter the team list by last sign-in**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_people_icon.png)
   **People** in the sidebar, then select **Team > Team members**.
2. Click **Filter**.
3. Under **Last sign-in**, select the time period for which you want to see
   the most recent sign-ins. You can also select **Never** to see a list of
   team members who haven't signed in yet.
4. Click **Apply filters**.

### **Sorting the list of team members**

Filtering doesn't change the order of the list. By default, the team list is
organized alphabetically by team member name, but you can sort it by team
member's last sign-in. If you sort the list by last sign-in before searching,
the set sort order is retained in the search results.

You can also use the search bar to sort team members by creation date, in either
ascending or descending order (see [Sorting search results](https://support.zendesk.com/hc/en-us/articles/4408886879258#topic_lhr_wsc_3v)).

**To sort the team list by last sign-in**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_people_icon.png)
   **People** in the sidebar, then select **Team > Team members**.
2. At the top of the **Last sign-in** column, click the sort icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/icon-sort.png)) to sort the list by most
   recent to least recent (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/icon-sort-path-up.png)) or vice versa (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/icon-sort-path-down.png)).

**To sort the team list by profile creation date**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_people_icon.png)
   **People** in the sidebar, then select **Team > Team members**.
2. In the search bar, enter **order\_by:created** to sort the team
   list.

   The team list is sorted in ascending order by default.
3. To sort the team list in descending order, enter **order\_by:created
   sort:desc**.