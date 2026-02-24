# Using the context panel

Source: https://support.zendesk.com/hc/en-us/articles/4408836526362-Using-the-context-panel

---

The Zendesk context panel provides valuable information you can use to get a better understanding of your customer and solve tickets quickly. This article describes how to use the context panel.

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

The Zendesk context panel provides valuable information you can use to get a better
understanding of your customer and solve tickets quickly. This article describes how to use
the context panel.

This article includes these sections:

- [About the context panel](#topic_j3r_2lz_n4b)
- [Opening and closing the panel](#topic_ehj_pqz_n4b)
- [Resizing the context panel](#topic_jr5_lbq_prb)

## About the context panel

When you’re working on a ticket, it’s often useful to have contextual information
that falls outside the basic ticket content. For example, you might want to know more about
the customer who requested the ticket or start a side conversation associated with the
ticket. In addition, you may need to open Zendesk apps that can help you solve the ticket or
search for articles in your help center that are relevant to the ticket.

The Zendesk Agent Workspace includes a context panel on the side of the ticket to
help you view and manage this information. The icons that appear in the context panel vary
depending on which features your admin has enabled for your account. For example, you need
to have a help center to use the knowledge features.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/uc_cc_panel_annotated_sm_sc.png)

## Opening and closing the panel

You can open and close the panel as needed to do your work. You can also switch
between views.

**To open and close the panel**

1. In a ticket, click any context icon in the right sidebar to open the
   panel.

   You can click the icon again to close the panel.
2. When the panel is open, click an icon to switch between views.

   For example, if apps
   (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/icon_omnipanel_apps.png)) are showing, click the user icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/icon_omnipanel_user.png)) to view user information.

   In the panel, you
   can:

   | Icon | Name | Description |
   | --- | --- | --- |
   |  | User | View contact information about the customer and the customer’s interaction history. Social media contact information, if any, is also included. See [Viewing customer context in a ticket](https://support.zendesk.com/hc/en-us/articles/4408829170458). |
   |  | Record preview | View details of object records that are related to the ticket. To see this icon, your account must have at least one active lookup relationship field pointing to a custom object on your ticket form. See [Interacting with related object records in tickets](https://support.zendesk.com/hc/en-us/articles/6097369527322). |
   |  | Knowledge | Search for content in your help center that might help your customers solve issues, view suggestions for articles based on ticket content, or add feedback to flag existing articles. See [Searching, linking, and quoting content in tickets](https://support.zendesk.com/hc/en-us/articles/4408826700570) and [Flagging articles in Knowledge](https://support.zendesk.com/hc/en-us/articles/4408826160922). |
   |  | Side conversations | Create or view side conversations associated with the ticket. See [About side conversations](https://support.zendesk.com/hc/en-us/articles/4408844206746). To see this icon, side conversations must be [activated](https://support.zendesk.com/hc/en-us/articles/4408832279962) in your account by an admin. |
   |  | Related tickets | Find similar tickets related to the ticket you're currently working on and view merge suggestions for related tickets. See [Finding tickets similar to the current ticket](https://support.zendesk.com/hc/en-us/articles/6154115110170) and [Merging related tickets based on suggestions](https://support.zendesk.com/hc/en-us/articles/6885971957914). |
   |  | Approval requests | Create and manage an approval request for the ticket you're currently working on. See [Creating approval requests](https://support.zendesk.com/hc/en-us/articles/8481158639770), [Responding to an approval request as an agent](https://support.zendesk.com/hc/en-us/articles/8481193191322), and [Responding to an approval request as an end user](https://support.zendesk.com/hc/en-us/articles/4408837910426#topic_ay1_m3h_zfc). |
   |  | Tasks | Add and manage lists of tasks for the ticket you're currently working on. See [Using task lists within tickets](https://support.zendesk.com/hc/en-us/articles/9676934427418). |
   |  | Apps | Open a list of [public](https://www.zendesk.com/apps/) or private apps to help you solve tickets. You only see apps that have been installed by your admin. See [Managing your installed apps](https://support.zendesk.com/hc/en-us/articles/4409155972378). |
   |  | IT asset management | Assign an asset to the ticket requester. See [Using assets in ticket workflows](https://support.zendesk.com/hc/en-us/articles/9817279885466). |

## Resizing the context panel

In some cases, you may want to change the width of the context panel to give you
a better view of customer context, sidebar apps, or Knowledge articles.

**To resize the context panel**

1. In a ticket, open the context panel.
2. Hover your mouse pointer over the shared border between the context panel and the ticket
   comments, until a resize icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_resize_icon.png)) appears and the panel border turns blue.
3. Drag the border to the left or right to change the context panel width.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/context_panel_resize.gif)

   These adjustments you
   make remain when you switch between views in the context panel, or when you open or
   close the panel. Your changes are maintained across tickets, until you do a hard
   refresh.

Tip: In addition to resizing the context panel, Agent Workspace users can also
change the ticket layout by [resizing the ticket properties panel](https://support.zendesk.com/hc/en-us/articles/4418444462618).

### Preparing your apps for context panel resizing

If your company is developing sidebar applications for the Zendesk Agent
Workspace, make sure your application developer uses the flexible property in the
application manifest file (**flexible = true**) to take advantage of changes to the
context panel width.

If the flexible property isn't specified in the application manifest file,
Zendesk assumes the property is set to **flexible = true**. This default makes it
easier for your apps to be set as flexible, but it's always a good idea to specifically
include it. If you don't want your app to be responsive to changes in the context panel
width, set the property to **flexible=false**.