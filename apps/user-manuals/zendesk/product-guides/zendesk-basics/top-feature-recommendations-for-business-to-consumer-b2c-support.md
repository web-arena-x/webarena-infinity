# Top feature recommendations for business-to-consumer (B2C) support 

Source: https://support.zendesk.com/hc/en-us/articles/5195414870938-Top-feature-recommendations-for-business-to-consumer-B2C-support

---

When you provide products or services to consumers, this is known as a business-to-consumer (or B2C) service.

Zendesk supports many B2C businesses. When we look at feature usage across all the businesses in that user segment, there are three features that B2C businesses, just like yours, are using disproportionately more than the other business types, business-to-business (B2B) and business-to-employee (B2E).

Based on feature usage across B2C businesses, we recommend these features to optimize your setup:

- [Macros](#topic_m1k_4td_dwb), to provide quick replies to customers and make agents more efficient.
- [Additional email addresses](#topic_pjt_4td_dwb), to make it easier for consumers to contact you.
- [CSAT](#topic_y15_4td_dwb), to enable your customers to give feedback on your support.

B2C businesses rely on these features, in addition to the [core feature setup](https://support.zendesk.com/hc/en-us/articles/4408824587802) recommended for all business types. Also, be sure to check out these [examples for basic setup for B2C businesses](https://support.zendesk.com/hc/en-us/articles/4408832607130).

## Create macros to respond quickly to customers

As a B2C business, you probably have a high volume of support requests from customers. You can create [macros](https://support.zendesk.com/hc/en-us/articles/4408844187034) to quickly handle tickets that can be answered with a single, standard response. This saves your agents the time and effort of crafting a separate response to each customer with the same issue. You can also use macros to automate simple actions on tickets.

To learn more about macros, see [Creating macros for tickets](https://support.zendesk.com/hc/en-us/articles/4408844187034) to learn more.

### Example

In this example, agents in the Returns group can apply a Wrong item shipped macro to a ticket. When a Returns agent sees a ticket that mentions a shipping mistake, the agent can open the ticket and apply this macro. This macro adds an internal, private comment to the ticket that notifies the Shipping department about the mistake. When Shipping sees this comment, they can check their inventory and look for mistakes in their order processing flow. The macro also adds a `wrong_item_shipped` tag to the ticket. The Shipping department can use this tag to generate reports on how many items were wrongly shipped over a given period of time.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/b2c_macro.png)

### How to

Use this procedure to create a macro that answers a common question automatically, saving the agent time.

**To create the macro**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://lh6.googleusercontent.com/MpuvRm4tbP2KmSY2jiqkPKECAJhRaZVpn3jYsDA5TOrk-ACvJfC8PRuy1bxuoNI-uwYqhuB55dNHq5ZmPEd6s-Nc3uwqyb90rGItQOqNpwwREHC2SuMnB-BAWDaWADAiTUYSTX61KHaUUq3kzJKn-_bM3ZyFd-S3QG2L_XOn_V8GXTilUMp2-cJGlo1JpA) **Workspaces** in the sidebar, then select **Agent tools > Macros**.
2. Click **Add macro**.
3. Enter a name for your macro, such as "Driver support", and an optional description.
4. From the **Available for** dropdown list, select who can use this macro, for example, **All agents** or **Me only**.
5. Click **Add action** to configure what this macro does.
6. From the list of actions, select **Comment/description** and add the following text:

   "For information about downloading drivers for your laptop computer, see our support website."
7. When you're finished, click **Create**.

   You've now finished creating the macro and can run it on any ticket.

### Pro tip

If you're not sure which macros to start with, look at your one-touch tickets; tickets that were solved with only one agent reply. They present a great opportunity for using a macro to make responding to this type of ticket even faster. See [this Explore recipe](https://support.zendesk.com/hc/en-us/articles/4408843225370) that helps you to examine your one-touch tickets.

## Create additional email addresses for your customers to contact you

When you set up Zendesk Support, you have one related email address:
support@*yoursubdomain*.zendesk.com. Emails received at this address become tickets.

As a B2C business, you probably want to create additional email addresses for your customers to contact you. Any email address you want to use to receive support requests as tickets (whether it's a Zendesk address or an external address)
must be added to your Zendesk account as a support address.

By creating multiple support addresses, a B2C company can route support tickets directly to agents, or groups of agents, who are trained to handle the issue at hand. Support addresses can be based on task or department, Billing or Returns, for example, location (such as city, time zone, or region), or language -- really, anything that works for your business.

To learn more about adding email addresses, see [Adding support email addresses for users to submit tickets](https://support.zendesk.com/hc/en-us/articles/4408842868506).

### Example

Here’s how having an issue-specific support address might work for your customer:

Robin goes to the Mega Pets website and clicks the “Contact Us” link.
On the web page, they see a list of potential reasons for contacting Mega Pets, each with a different email address associated with it:

Billing problem? Contact [billing@megapetsinc.com](mailto:billing@megacomputersinc.com)

Need to return something? Contact [returns@megapetssinc.com](mailto:returns@megacomputersinc.com)

Something else you want help with? Contact [support@megapetssinc.com](mailto:other@megacomputersinc.com)

Robin clicks [returns@megapetsinc.com](mailto:returns@megacomputersinc.com), fills out the support form, and clicks **submit**. All tickets sent through that email address are routed to a view monitored by the returns department, and they are contacted by an agent who helps them repackage the tiny crate for return and expedites the delivery of a replacement.

### How to

Use this procedure to add a new support address to your account.

**To add the new support address**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://lh5.googleusercontent.com/f5EtgH3Cu1-pFq7VoCN4Fzm2Q4liWJNIUixaloVq56_i9kmjE-Lk6Dn99F8zzGNpsPxfp_pXjQvr-tVg9LyTb4rejojwZRvQviEIUBL8zTDe-OOLV_9m9O-J5LmTYb08Vp_POo-7rxBTKzL7ENac5qeOBsKqUiBSIr06GKdL9X-_FfBMeVHi0l1joQcXFg)**Channels** in the sidebar, then select **Talk and email > Email**.
2. In the Support addresses section, click **Add address**, then select **Create new Zendesk address**.
3. Enter an address you want to use for receiving support requests, in this case, "returns@megapets.zendesk.com".
4. Click **Create now**.

   The new email address is added to your list of support addresses.

### Pro tip

You can route tickets based on the support address they were sent to.
For more information, see [Routing options for incoming tickets](https://support.zendesk.com/hc/en-us/articles/4408831658650).

## Enable Customer satisfaction (CSAT) to get feedback

Note: Customer satisfaction ratings are not available on the suite's Team plan.

When you enable [CSAT (customer satisfaction ratings)](https://support.zendesk.com/hc/en-us/articles/4408822875034), end users are prompted to rate the support they received by answering a brief survey indicating whether they were or were not satisfied. You can also configure satisfaction reasons to ask customers who give a negative rating to select a reason.

As a B2C business, you can review CSAT ratings and reasons to improve your customer support and make customers happier.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/csr_question.png)

To learn more about CSAT, see [Enabling and using CSAT](https://support.zendesk.com/hc/en-us/articles/4408822875034).

### How to

Use this procedure to enable CSAT for your account.

**To enable customer satisfaction ratings**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://lh3.googleusercontent.com/1aDkiKjS8H-aHepppOicxxAOR5n45RHhlneeVIFIzSsztPLpM86f7UwpVOHAfXcYMpoLFtyrlyZoBGIRLuCJi70hbWW5rSDAoFDXK8__sU-fWxXYJWfrrurM09gilmZXMIdhjrrC3w4rn6i0-5b6m8gxb9mdYm7Rbg2Zxgg8WV6ffLlRBmdTpDTeeXZO2w) **People** in the sidebar, then select **Configuration > End users**.
2. On the **Satisfaction** tab, click **Allow customers to rate tickets**.
3. Click **Save tab** at the bottom of the page.

   **Zendesk Support** sends your end users the customer satisfaction rating survey in an email *24 hours* after the related ticket has been marked as *Solved*.

   **Zendesk messaging** (if used in your account) sends your end users the survey in the messaging web or mobile interface *immediately* after the related ticket is marked as *Solved*.

### Pro tip

You can create a trigger to notify a manager or group about tickets that receive bad ratings, and then you can proactively follow up. Customers will appreciate the care and personal touch, which might improve customer loyalty.