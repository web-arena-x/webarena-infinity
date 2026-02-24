# Restricting agent ticket access by brand (department spaces)

Source: https://support.zendesk.com/hc/en-us/articles/7584022494874-Restricting-agent-ticket-access-by-brand-department-spaces

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Enterprise or Enterprise Plus |

| | |
| --- | --- |
| **Support** | Enterprise |

Verified AI summary ◀▼

Restrict agent ticket access by brand using department spaces to enhance data privacy and focus support efforts. Assign agents to specific brands, allowing them to view and manage tickets only within those brands. This segmentation promotes specialized knowledge and control over ticket visibility. Consider workflow impacts when removing access, and remember that admins have access to all brands by default.

If you support [multiple brands](https://support.zendesk.com/hc/en-us/articles/4408829476378), Zendesk allows team members (agents) to manage tickets associated only with their assigned brands. By assigning agents to brands, administrators can control which tickets agents can access based on their brand membership, ensuring focused support, enhancing data privacy, and promoting specialized product knowledge. Segmenting access to branded tickets this way is called *department spaces.*

If all agents are assigned to all brands, then department spaces is not in use, and brand does not control agent visibility of tickets. Removing agents from brands removes their ability to view, search, and access tickets with that brand.

Consider how removing access might impact your workflow. If you don't want to use this feature, you don't have to take any action because team members are assigned to all brands by default. You can ensure team members are assigned to all brands by [viewing their brand memberships](#topic_skc_frx_xbc).

Watch the video below to learn more about department spaces.

Department spaces: Segment access to tickets by brand or department (3:30)

This article covers the following topics:

- [Limitations](#topic_ck2_br2_fdc)
- [Understanding brand membership](#topic_eqt_crx_xbc)
- [Viewing team member brand memberships](#topic_skc_frx_xbc)
- [Filtering team members by brand](#topic_ms4_sky_jfc)
- [Adding or removing team members from brands](#topic_p4k_grx_xbc)
- [Viewing and updating brand memberships from the agent profile](#topic_wsw_b3f_rgc)
- [Configuring brand membership settings for new team members](#topic_yb2_whp_ngc)

Related articles:

- [Setting up multiple brands](https://support.zendesk.com/hc/en-us/articles/4408829476378)
- [Multibrand resources](https://support.zendesk.com/hc/en-us/articles/4408833921306)

## Limitations

- Restricting agent ticket access by brand (also called department spaces) cannot be used with the following:
 - Legacy messaging through Chat
 - [Legacy Talk plans](https://support.zendesk.com/hc/en-us/articles/4408833956122#topic_fmk_lmf_mnb)
- Triggers can assign tickets to agents that shouldn't have access to the ticket.
 When this occurs, the agent will see a message stating they don't have access to the ticket. See [Why can't I access this ticket?](https://support.zendesk.com/hc/en-us/articles/4603876353818) for more information.

## Understanding brand membership

You can assign team members to brands, which sets their brand membership. Team members can only view, search, and access tickets within their assigned brands.
Assigning a team member to all brands gives them access to tickets across all brands. If they aren't assigned to any brands, then they won't have access to tickets. See [Considerations](#topic_bnt_drx_xbc) for exceptions.

Initially, new team members are assigned to all brands and, therefore, will have access to all tickets. Administrators can control which tickets agents can access by removing them from the brands they shouldn't have access to. Admins are automatically assigned to all brands and can access all tickets across all brands.
When a new brand is created, all admins are automatically added to it and cannot be removed.

A team member’s role can further refine their access. For example, a team member’s role might limit them to only tickets in their groups.

When creating and updating tickets, the **Brand** drop-down field in the Agent Workspace is limited to the brands for which the agent is a member. Agents in [a custom role with permission](https://support.zendesk.com/hc/en-us/articles/4408882153882) can assign tickets to any brand, including brands they don’t belong to.

Tip: When using department spaces to restrict agent ticket access by brand, it is recommended to [require a brand selection before saving tickets](https://support.zendesk.com/hc/en-us/articles/4408826557082#topic_vrf_w1v_sgc) to prevent tickets from being saved without a brand.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_teammember_brand_choose.png)

### Considerations

- An [upgraded agent](https://support.zendesk.com/hc/en-us/articles/4408883470106) initially belongs to no brands and, therefore, will have no access to tickets. You must [add the agent to brands](#topic_p4k_grx_xbc) to give them access to tickets within those brands.
- Team members can be CC’d or added as followers on tickets outside their brand membership. When this happens, they will only have access to the specific ticket, not all tickets within that brand.
- If an agent in a custom role has permission to manage suspended tickets, they can manage the suspended tickets in their brands only, plus any suspended tickets without a brand.
- Tickets shared via a direct link are inaccessible if the agent isn’t a member of the ticket’s brand.
- [Omnichannel routing](https://support.zendesk.com/hc/en-us/articles/4409149119514) respects the brand memberships of your agents. If you’re using this feature, tickets are only assigned to agents who are members of the ticket's brand.

## Viewing team member brand memberships

Brand memberships for all your team members appear on the Team members page. You can also [filter the list of team members](#topic_ms4_sky_jfc) by brand.

**To view brand memberships**

- In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_people_icon.png)
 **People** in the sidebar, then select **Team > Team members**.

 The brand associated with each team member appears in the **Brand** column.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_teammember_brand_view.png)

If a team member belongs to multiple brands, click the **+more** link to view additional brand memberships.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_teammember_more_brands.png)

## Filtering team members by brand

Filtering the team list by brand helps you verify that team members have the appropriate brand memberships. For example, you might periodically filter for team members with no brand memberships to ensure that no one's brand membership has been accidentally removed.

**To filter the team list by brand membership**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_people_icon.png)
   **People** in the sidebar, then select **Team > Team members**.
2. Click **Filter**.
3. Under **Brand membership**, select the brands by which you'd like to filter team members.

   Selecting multiple brands filters team members who are part of all the selected brands. To filter team members with no brand memberships, select **No brand**.
4. Click **Apply filters**.

## Adding or removing a team member from brands

When you add team members to brands, they can view, search, and access tickets within their assigned brands. Removing a team member from brands removes their access to tickets within that brand.

You cannot remove admins from brands. Admins must be members of all brands.

Important: If you remove a team member from all brands, they will have no ticket access.

**To add or remove brand memberships**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_people_icon.png)
   **People** in the sidebar, then select **Team > Team members**.

   The team member page opens.
2. [Search](https://support.zendesk.com/hc/en-us/articles/4408843830938#topic_prc_1qj_35b) for the team members you want to update, then select them in the list.

   You can select one or many team members. Admins are members of all brands and will be excluded from any bulk operations.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/zug_team_member_select_2.png)
3. Click **Manage brand membership**.

   The **Manage brand membership** link displays at the bottom of the page after you select team members.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_teammember_brand_manage.png)
4. In **Add to brand** and **Remove from brand**, select the brands you'd like to add or remove the team member.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_teammember_brand_addremove.png)
5. Click **Save**.

## Viewing and updating brand memberships from the agent profile

To view or update brand memberships for a single agent, you can do so from the agent's profile.

**To view or update brand memberships from an agent's profile**

1. In [Support](https://support.zendesk.com/hc/en-us/articles/4408838272410), click the **Search** icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/search_icon.png)) in the upper-right of the top toolbar.
2. Begin typing the agent's name, then select the agent from the drop-down list.
3. Click the **Brands** menu in the left pane to expand it, then select or deselect brands for the team member.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/brands_selection_profile2.png)

## Configuring brand membership settings for new team members

Admins can configure brand assignments for new team members and [upgraded users](https://support.zendesk.com/hc/en-us/articles/4408883470106), ensuring team members get relevant brand access from the start.

By default, new team members are assigned to all brands, but this setting can be changed. For example, you may want team members to have no brand assignments initially, requiring a manual selection each time.

**To configure brand membership settings for new team members**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_account_icon.png)
   **Account** in the sidebar, then select **Brand management > Brands**.
2. Click **Manage settings**.
3. Select an option for **Choose how new team members get assigned to brands**.

   This setting only controls the *default selection* when adding new team members. You can still change brand assignments when adding a team member.
   - **Manually assign brands**: No brands are pre-selected.
   - **Assign new team members to all brands**: All brands (active and inactive) are pre-selected.
4. Select an option for **Choose how end users are assigned to brands when upgraded to team member**. This setting will automatically assign the upgraded user to brands based on your selection.
   - **Assign to no brands**: The upgraded team member will have no brand assignments.
   - **Assign upgraded team member to previously assigned brands**: The upgraded team member will be assigned to the brands they were originally assigned to before they were downgraded to an end user.
   - **Assign new team members to all brands**
5. Click **Save**.