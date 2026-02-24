# Installing and using the Linked Ticket app

Source: https://support.zendesk.com/hc/en-us/articles/4408820849434-Installing-and-using-the-Linked-Ticket-app

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

The [Linked Ticket](https://www.zendesk.com/marketplace/apps/support/6272/linked-ticket/) app enables you to create a child ticket from an existing parent ticket and link the two tickets together. This is particularly useful when you need to have two separate conversations around the same issue.

The app is not recommended for [light agents](https://support.zendesk.com/hc/en-us/articles/4408846501402). When light agents create a child ticket, the parent ticket shows blank values for the linked child ticket because light agents can't edit ticket properties unless they're the requester.

This article contains the following topics:

- [Installing the Linked Ticket app](#Installing)
- [Creating a child ticket from a parent ticket](#Creating)
- [Creating a view for child tickets](#h_01GAGQERNK7SST662T0Z9KNW34)
- [Using business rules with the Linked Ticket app](#Using)
- [This ticket form is missing the linked data field](#error)
- [Legacy Reference Field (existing or old installations only)](#legacy)

## Installing the Linked Ticket app

The Linked Ticket app is installed from the [Zendesk Marketplace](https://www.zendesk.com/marketplace/apps/support/6272/linked-ticket/).

**To install the app**

1. In [Admin Center](../account-administration/using-zendesk-admin-center.md#topic_hfg_dyz_1hb), click the **Apps and integrations** icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_apps_integrations_icon.png)) in the sidebar, then select **Apps > Zendesk Support** apps.
2. Click **Marketplace** at the top of the page and then search for "Linked Ticket" in the **Filter apps** search bar.
3. Click **Install** in the upper-right of the page.
4. Select the subdomain of the account you want to install the app.
5. Configure any app settings as needed.
6. Click **Install** to complete the setup  
     
   The app is installed in your Zendesk.

If you have [ticket forms](../ticket-customization/managing-your-ticket-forms.md) enabled on your account, go to [Admin Center](../account-administration/using-zendesk-admin-center.md#topic_hfg_dyz_1hb) > **Objects and rules** (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_objects_rules_icon.png)) > **Tickets > Forms**. [Add](https://support.zendesk.com/hc/en-us/articles/4408883152794-Adding-custom-fields-to-your-tickets-and-support-request-form) the automatically created **Linked Data**field to each active ticket form.

## Creating a child ticket from a parent ticket

To create a child ticket from a parent ticket, open the Apps sidebar in the ticket, and click **Create a ticket***.*

![Create a ticket through the Linked Ticket app](https://support.zendesk.com/hc/article_attachments/4858878420890)

Fill in each of the ticket fields, and check **Copy current ticket description** if you want to carry the ticket description from the parent ticket through to the child ticket. Ticking this option only brings over public replies, not internal notes. The description of the parent ticket moves to the child ticket as a public reply.

![Copy current ticket description Linked Ticket app](https://support.zendesk.com/hc/article_attachments/4858977312282)

Once the child ticket is created, the app displays a link to the parent ticket if the child ticket is open and a link to the child ticket if the parent ticket is open.

![This_ticket_has_a_child_ticket.png](https://support.zendesk.com/hc/article_attachments/4858915949722)![This ticket has a parent ticket](https://support.zendesk.com/hc/article_attachments/4858979574810)

If you update the status of one of the tickets, the status of the related ticket won't automatically update.

Tags from the parent ticket are automatically added to the Linked Ticket app and passed to the child ticket. These tags may cause fields to be set, including conditional field requirements that are not fulfilled. This can cause the creation of the child ticket to fail. To avoid this, adjust the conditional requirements or remove the tags in question.

## Creating a view for child tickets

During the [installation step](#Installing), you can add a child tag to be added to the created child ticket, for example, `child_ticket`.

![tag child ticket](https://support.zendesk.com/hc/article_attachments/4858937421082)

To track child tickets, you can [create a view](https://support.zendesk.com/hc/en-us/articles/4408888828570-Creating-views-to-manage-ticket-workflow) that meets the condition **Tags | Contains at least one of the following |** `child_ticket`.

**To create the view**

1. In [Admin Center](../account-administration/using-zendesk-admin-center.md#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_workspaces_icon.png) **Workspaces** in the sidebar, then select **Agent tools > Views**.
2. Click **Add view**.
3. Under **Tickets must meet all of these conditions to appear in the view**, add:
   - **Tags | Contains at least one of the following | child\_ticket**
   - **Status | Less than | Solved**

![Child_tickets_view.png](https://support.zendesk.com/hc/article_attachments/4859342808858)

The Linked Ticket app doesn't automatically add tags to the parent ticket. However, you can manually add the tag to each parent ticket and follow this workflow to track all parent tickets.

## Using business rules with the Linked Ticket app

You can set up [triggers](https://support.zendesk.com/hc/en-us/articles/4408843730458-Triggers-resources) and [automations](../business-rules/about-automations-and-how-they-work.md) for parent and child tickets using the tags above. However, it's not possible to set up business rules to make two linked tickets interact with each other. For instance, it's not possible to set up a trigger to automatically solve a parent ticket once the child ticket is solved.

## This ticket form is missing the linked data field

The error **This ticket form is missing the linked data field** means that the **Linked Data** field wasn't added to the ticket form. The error displays the name and ID of the ticket field required:

![This ticket form is missing the linked data field](https://support.zendesk.com/hc/article_attachments/4859405605530)

**To solve this issue**

1. In [Admin Center](../account-administration/using-zendesk-admin-center.md#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_objects_rules_icon.png) **Objects and rules** in the sidebar, then select **Tickets > Fields**.
2. Click the ticket form you want to edit.  
     
   The ticket form opens in edit mode.
3. Drag and drop the **Linked Data** field into the ticket form and click **Save**.   
   ![Drag and drop Linked Data](https://support.zendesk.com/hc/article_attachments/4859464866842)

If you have [ticket forms](../ticket-customization/managing-your-ticket-forms.md) enabled on your account, go to [Admin Center](../account-administration/using-zendesk-admin-center.md#topic_hfg_dyz_1hb) > **Objects and rules** (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_objects_rules_icon.png)) > **Tickets > Forms**. [Add](https://support.zendesk.com/hc/en-us/articles/4408883152794-Adding-custom-fields-to-your-tickets-and-support-request-form) the automatically created **Linked Data**field to each active ticket form.

## Legacy ReferenceField (existing or old installations only)

Note: The **Reference Field** only applies to existing or older installations of the Linked Ticket app. If you are installing a new instance of the Linked Ticket app, you don't have to populate this field.

The **Reference Field** in the settings of the Linked Ticket app is the ID of the field **Linked Data**. This is a manually created ticket field that contains the data to link tickets together in the app. This field must be on all active ticket forms.

![](https://support.zendesk.com/hc/article_attachments/4408851933082)

When installing:  
![](https://support.zendesk.com/hc/article_attachments/4408851932698)

Warning: Deleting the **Reference field** will erase all links between tickets and they can't be recovered. Zendesk recommends that you leave the field in your account if it exists.