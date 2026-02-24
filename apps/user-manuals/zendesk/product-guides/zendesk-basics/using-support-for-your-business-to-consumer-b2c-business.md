# Using Support for your Business-to-Consumer (B2C) business

Source: https://support.zendesk.com/hc/en-us/articles/4408832607130-Using-Support-for-your-Business-to-Consumer-B2C-business

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

Mega Pets is an online pet supply retail website that sells pet-related items to consumers.

Robin ordered an XL dog kennel for their Swiss Mountain Dog from Mega Pets.
When it arrived at their home in San Francisco, it was an XS (better for a Yorkie).

They needs to contact a customer service representative who can help arrange a return and expedite a replacement.

This article contains the following sections:

- [How can views help my B2C business?](#topic_afj_j5z_hlb)
- [How can organizations and groups help my B2C business?](#topic_hqz_k5z_hlb)
- [How can ticket fields help my B2C business?](#topic_ib1_l5z_hlb)
- [How can business rules help my B2C business?](#topic_fdw_d21_3lb)
- [How can macros help my B2C business?](#topic_n5w_d21_3lb)
- [How can a help center help my B2C business?](#topic_zln_r21_3lb)
- [How can apps and integrations help my B2C business?](#topic_op5_v21_3lb)
- [How can Web Widget (Classic) help my B2C business?](#topic_dql_nf1_3lb)
- [How can support addresses help my B2C business?](#topic_egx_jcj_nlb)

## How can views help my B2C business?

Views are a way to organize your tickets by grouping them into lists based on certain criteria. Using views can help you determine which tickets need attention from you or your team and plan accordingly.

As a business dealing largely with consumers, you probably have a large number of tickets that deal with specific customer issues or actions, such as returns, online orders, and customer complaints. You can organize tickets according to these common customer needs.

### Example

Let’s take a look at an example.

When a customer submits a ticket, you can configure a [custom field](https://support.zendesk.com/hc/en-us/articles/4408883152794) named “Type of product issue” so that they can choose the reason for the ticket, in this case “Product returns”. A trigger automatically assigned these tickets to the “Product returns” group. You can create a [view](https://support.zendesk.com/hc/en-us/articles/4408888828570) to help you see only these requests.

Here’s a simple example:

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Views_b2c_1.png)

In this example, the view is configured to display only tickets with the type of product issue “Product returns” that are in the group “Product returns”. You can configure the information that the view displays by choosing the columns you want. Additionally, you can configure which of your agents can see the view in their Support console. Here’s an example:

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Views_b2c_2.png)

### Related articles

- [Creating views to manage ticket workflow](https://support.zendesk.com/hc/en-us/articles/4408888828570)

## How can organizations and groups help my B2C business?

Organizations are collections of your users (both end users and agents).
Groups collect agents together based on criteria those agents have in common.

As a B2C business, you will probably use organizations and groups to organize the people in your Zendesk Support account.

Organizations and groups are often used to:

- Escalate tickets based on complexity
- Support service-level agreements
- Provide support by expertise
- Support customers by location and language

You may also want to use organizations to tightly manage your workflow and create security boundaries by funneling tickets directly to agents who have restricted access.

### Example

Let’s say you are Mega Pets, an online retailer that sells pet supplies directly to consumers.

You may not use organizations much since your customers have different spending patterns and motivations. However, you may want to create groups based on departments or divisions in your company (for example, Legal, Marketing, Sales, Shipping, Returns, and Website). You can add “actions” based on groups to triggers, automations, and macros, but not views.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/b2c_people_groups2.png)

### Related articles

- [About organizations and groups](https://support.zendesk.com/hc/en-us/articles/4408886146842)
- [About triggers and how they work](https://support.zendesk.com/hc/en-us/articles/4408822236058)
- [About automations and how they work](https://support.zendesk.com/hc/en-us/articles/4408832701850)
- [Using macros to update tickets](https://support.zendesk.com/hc/en-us/articles/4408887656602)
- [Creating views to manage ticket workflow](https://support.zendesk.com/hc/en-us/articles/4408888828570)

## How can ticket fields help my B2C business?

Ticket fields include data that agents need in order to solve a problem. In order to use ticket fields effectively, it’s important to learn about the different types of ticket fields—there are system fields and custom ticket fields. Also, make sure you understand what kinds of permissions you can set on a ticket field, the relationship between ticket fields and ticket forms, and where ticket fields will appear for your agents and end users.

Ticket fields and ticket forms are highly customizable. It’s worth spending some time to figure out how to use them in a way that works best for you. This often reduces resolution times and improves customer satisfaction.

As a B2C business, when you get a request, you want to know certain information right away. You don’t want to have to go back to the customer and ask for more information. That takes time and can slow down resolution.

### Example

Let’s say you are Mega Pets, an online retailer that sells pet supplies directly to consumers.

You have a custom ticket field called “Inquiry type.” It’s a drop-down list that includes options for **Billing**, **Returns**, **Exchanges**, and **General questions**. It’s part of your default ticket form.

Here’s what your customer sees when they go to submit a request:

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/b2c_dropdown_ex.png)

You also have a trigger that automatically routes tickets to agents in the Returns group.

When a customer submits a support request for a return, the ticket is immediately assigned to the Returns group, and can be processed quickly.

### Related articles

- [About ticket fields](https://support.zendesk.com/hc/en-us/articles/4408886739098)
- [Adding custom fields to your tickets and support request form](https://support.zendesk.com/hc/en-us/articles/4408883152794)

## How can business rules help my B2C business?

You can create triggers and automations to intelligently process tickets, reduce redundant work, and save agents' time. Triggers are **event-based** business rules you define that run immediately after tickets are created or updated.
Automations are **time-based** business rules that perform an action in your account based on time elapsed.

Common uses of triggers and automations include:

- Routing new requests to the right team
- Sending notifications to customers or agents
- Escalating tickets in need of a response

By automating stages throughout the ticket lifecycle, you can decrease ticket handling times and reduce the number of reassignments from one agent to the next. This ultimately helps you deliver a better experience for both your customers and agents. Your agents now spend their time helping customers instead of performing repetitive tasks.

As a B2C business, business rules can help you by automatically replying to customers when their request is received or when their request is updated, notifying customers about your standard operating hours (business hours), and helping you remind customers when they don’t reply to agent requests for more information.

### Trigger example

For example, this trigger automatically sends customers an email when they request a refund and lets them know how long it will take to get their refund.
The trigger also automatically routes the ticket to agents in the Returns group so they can process it quickly.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/b2c_trigger_conditions.png)![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/b2c_trigger_actions.png)

Here’s what the email received by the customer looks like:

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/b2c_trigger_email.png)

### Automation example

In this example, the automation automatically increases a ticket’s priority to Urgent if the refund hasn’t been processed in over two days. It also warns the Returns agents that the three-day refund window is at risk.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/b2c_automation_conditions.png)

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/b2c_automation_actions.png)

Here’s what the email received by agents in the Returns group looks like:

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/b2c_automation_email.png)

### Related articles

- [About triggers and how they work](https://support.zendesk.com/hc/en-us/articles/4408822236058)
- [About automations and how they work](https://support.zendesk.com/hc/en-us/articles/4408832701850)
- [Routing and automation options for incoming tickets](https://support.zendesk.com/hc/en-us/articles/4408831658650)

## How can macros help my B2C business?

Macros are a pre-defined set of actions that agents apply to a ticket with one click. You can create macros to address support requests that can be answered with a single, standard response, and embed macros within tickets to help agents quickly provide consistent responses. This saves your agents the time and effort of crafting a separate response to each customer with the same issue.

**Macros can:**

- Add comment text
- Update ticket fields (drop-down and checkboxes)
- Add or remove ticket tags
- Add CCs
- Change the assignee
- Set the ticket subject (title)
- Add attachments to ticket comments

### Example

In this example, agents in the Returns group can apply a Wrong item shipped macro to a ticket. When a Returns agent sees a ticket that mentions a shipping mistake, the agent can open the ticket and apply this macro. This macro adds an internal, private comment to the ticket that notifies the Shipping department about the mistake. When Shipping sees this comment, they can check their inventory and look for mistakes in their order processing flow. The macro also adds a `wrong_item_shipped` tag to the ticket. The Shipping department can use this tag to generate reports on how many items were wrongly shipped over a given period of time.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/b2c_macro.png)

### Related articles

- [Creating macros](https://support.zendesk.com/hc/en-us/articles/4408844187034)
- [Using macros to update tickets](https://support.zendesk.com/hc/en-us/articles/4408887656602)
- [Macros resources](https://support.zendesk.com/hc/en-us/articles/4408824631578)

## How can a help center help my B2C business?

A [help center](https://support.zendesk.com/hc/en-us/articles/4408846795674) provides a smart knowledge base for better self-service. You can set up your knowledge base to contain information (articles) covering frequently-asked questions, policies, product details, and more, to help users find the information they need, without having to raise a support ticket.

As a B2C business, you can create FAQs or What’s New topics, for example, that contain articles about return and shipping policies, sizing guides, and any type of information you want to present to help answer common customer questions.

### Example

As a real-life example, [Magnolia Market](https://help.magnolia.com/hc/en-us) has a beautiful help center, displaying topics with the most commonly-asked questions, and a prominent search bar.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/b2c_hc_customer_site.png)

To create your own help center, you’ll need to first [enable your help center in setup mode](https://support.zendesk.com/hc/en-us/articles/4408846795674#topic_ndf_fpf_mk), then create and add content before you [activate it](https://support.zendesk.com/hc/en-us/articles/4408846795674#topic_ckn_wc4_qy).

You can start small with just a few articles that answer your customer’s most commonly-asked questions. For example, you could write an article explaining the returns policy, your store opening hours, or shipping prices. The more articles you write, the more your Support agents can concentrate on answering the tricky questions and problems. You need to be a Knowledge admin or an agent with [management permissions](https://support.zendesk.com/hc/en-us/articles/4408827952538) to create an article.

If you create an article describing how customers can initiate a return, then Robin could search and find this information without even having to raise a ticket. You can add labels like **returns** and **policy** to the article to boost it in search results (labels are not available on Suite Team).

Your article might look like this in draft format:

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/b2c_hc_draft_article.png)

### Related articles

- [Getting started with your help center](https://support.zendesk.com/hc/en-us/articles/4408846795674)
- [Creating and editing an article](https://support.zendesk.com/hc/en-us/articles/4408839258778)

## How can apps and integrations help my B2C business?

B2C companies are using a variety of apps in the [Zendesk Marketplace](https://www.zendesk.com/apps/) and integrations to customize their platform or solution. Here are a few apps which can support your B2C business.

### Shopify for Zendesk app

For businesses that use the Shopify ecommerce platform, the [Shopify for Zendesk app](https://www.zendesk.com/apps/support/shopify-for-support/)
connects Support or Chat to your Shopify site.

In the following example, the app displays the Robin’s Shopify order associated with the Support ticket. This reduces context-switching for the support agent, and improves productivity by enabling customer details to be displayed.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/b2c_shopify.png)

For more information about the app, see the [Shopify integration](https://support.zendesk.com/hc/en-us/sections/360005927234).

### Five Most Recent app

The [Five Most Recent app](https://www.zendesk.com/apps/support/five-most-recent/?source=app_directory) displays the five most recent tickets the customer has submitted, so an agent has more context around past support requests made by a customer.

In this example, the support agent can see in the ticket editor previous tickets for MegaPets' customer Robin.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/b2c_fivemostrecent.png)

### Out of Office app

The [Out of Office app](https://www.zendesk.com/apps/support/shopify-for-support/) helps your business with customer support by managing the availability of agents in Support. It updates all pending, on-hold, solved, and open tickets with a tag when an agent is unavailable. This allows business rules to be created which acts on ticket updates when an agent is unavailable. The app installs a default rule which unassigns tickets which have unavailable assignees when the ticket status is "open". The app can also prevent manual assignment of tickets to an unavailable agent.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/b2c_outofoffice.png)

To learn more about the app, see [Installing and using the Out of Office v2 app](https://support.zendesk.com/hc/en-us/articles/4408828358682).

## How can Web Widget (Classic) help my B2C business?

[Web Widget (Classic)](https://support.zendesk.com/hc/en-us/articles/4408833907354) is a separate web application that is embedded in a web page. It gives customers access to your help center and the agents in your Zendesk support channels.

By embedding Web Widget (Classic) in your website, it encourages customers to self-serve by searching for help center articles and the widget providing article suggestions. It can also make it easier to get help from an agent by displaying ticket forms for support requests, request a call back, and start a chat.

Using the [Web Widget APIs](https://developer.zendesk.com/embeddables/docs/widget/introduction), you can perform a variety of advanced customizations to widget to suit your business. For example, you can choose which channels you would like to show on a particular web page, or modify the widget launcher style and position to suit your website.

### Example

Web Widget (Classic) can be configured in your [Support Admin](https://support.zendesk.com/hc/en-us/articles/4408838063258).

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/b2c_webwidget.png)

Zendesk also provides [Web Widget APIs](https://developer.zendesk.com/embeddables/docs/widget/introduction) to extensively configure and customize the widget to suit your requirements. In this example, on the product returns web page, all channels globally enabled in the Web Widget (Classic) are suppressed except for the ticket form. This is configured using the [suppress API](https://developer.zendesk.com/embeddables/docs/widget/settings#suppress) to suppress all the channels which are not needed. The script along with the widget snippet is added to the product returns source page.

```
<script type="text/javascript">
 window.zESettings = {
    webWidget: {
      chat: {
        suppress: true
      },
      contactForm: {
        suppress: false
      },
      helpCenter: {
        suppress: true
      },
      talk: {
        suppress: true
      },
      answerBot: {
        suppress: true
      }
    }
 };
</script>
 
 <!-- Start of {your_subdomain} Zendesk Widget script -->
             
<script id="ze-snippet"
 src="https://static.zdassets.com/ekr/snippet.js?key={your_widget_snippet_key}"> </script>
                
 <!-- End of YOUR_DOMAIN Zendesk Widget script -->
```

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/b2c_webwidget_suppress.png)

### Related articles

- [Providing omnichannel support using Web Widget (Classic) for the Suite](https://support.zendesk.com/hc/en-us/articles/4408844047898)
- [Web Widget (Classic)
 resources](https://support.zendesk.com/hc/en-us/articles/4408833907354)
- [Using Web Widget (Classic) to embed customer service in your website](https://support.zendesk.com/hc/en-us/articles/4408836216218)

## How can support addresses help my B2C business?

Support addresses are email addresses that allow your users to submit support tickets. Support addresses can be variations of your Zendesk email address, or your external email addresses. Any email address you want to use to receive support request as tickets (whether it's a Zendesk address or an external address)
must be added to your Zendesk as a support address.

By creating multiple support addresses, a B2C company can route support tickets directly to agents, or groups of agents, who are trained to handle the issue at hand. Support addresses can be based on task or department (Billing or Returns, for example., location (such as city, time zone, or region), or language -- really, anything that works for your business.

You can create as many support email addresses as your business needs. They can be used throughout your Zendesk to help you organize and direct your support requests to your agents:

- [Create views](https://support.zendesk.com/hc/en-us/articles/4408888828570) that organize tickets based on which address received them.
- [Customize email notifications](https://support.zendesk.com/hc/en-us/articles/4408886168090) for each email address, to automatically reply to incoming requests.
- [Build triggers](https://support.zendesk.com/hc/en-us/articles/4408886797466), using email addresses as a condition. For example, you can add tags or priority levels to tickets, or assign them to specific groups or agents, based on which email address received them.
- [Create reports](https://support.zendesk.com/hc/en-us/articles/4408821589530) to monitor how many tickets are generated through email addresses, and write custom formulas to break down how each address is performing.

### Example

Here’s how having an issue-specific support address might work for your customer:

Robin goes to the Mega Pets website and clicks the “Contact Us” link.
On the web page, they see a list of potential reasons for contacting Mega Pets, each with a different email address associated with it:

Billing problem? Contact [billing@megapetsinc.com](mailto:billing@megacomputersinc.com)

Need to return something? Contact [returns@megapetssinc.com](mailto:returns@megacomputersinc.com)

Something else you want help with? Contact [support@megapetssinc.com](mailto:other@megacomputersinc.com)

Robin clicks [returns@megapetsinc.com](mailto:returns@megacomputersinc.com), fills out the support form, and clicks **submit**. All tickets sent through that email address are routed to a view monitored by the returns department, and they are contacted by an agent who helps them repackage the tiny crate for return and expedites the delivery of a replacement.

### Related articles

- [Adding support addresses for users to submit tickets](https://support.zendesk.com/hc/en-us/articles/4408842868506)
- [Top feature recommendations for business-to-consumer (B2C) support](https://support.zendesk.com/hc/en-us/articles/5195414870938-Top-feature-recommendations-for-business-to-consumer-B2C-support-)