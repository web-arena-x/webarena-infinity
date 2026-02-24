# Rates and Rate Hierarchies

Source: https://help.clio.com/hc/en-us/articles/9289801180187-Rates-and-Rate-Hierarchies

---

Billing clients is not always simple. It depends on who they work with, how long or loyal a client they have been, what type of time and resource commitment that particular matter has been, and more. Clio’s flexibility comes in handy, enabling you to charge clients as you need. When capturing time in Clio Manage, you can set specific rates for a variety of reasons or scenarios. These rates have a hierarchy that affects which rate will override the others in the event of conflicting rates. The rate hierarchy is as follows, from highest, or what takes priority, to lowest:

1. Custom rate
2. Flat fee rate
3. Matter-based rate
4. Client-based rate
5. Activity category custom rate
6. User default rate

## Set custom rate

You can set a custom rate by manually adjusting the Rate field when creating a new time entry. This action will override all other rates previously set.

**Important:** If you set a custom rate on a time entry and then change the matter or activity category, the custom rate will be overridden by the matter or activity category rate.

## Apply flat fee rate

You can create a flat rate for matters where you are charging a flat fee for the case. Perhaps this is something your firm does for all will and estate planning cases if the time commitment is generally the same client-to-client. This feature automatically creates time entries and bills for the flat fee and tracks time at 0.00/hr. That way, your time is still being measured without a dollar figure attached to each minute or expense, unless desired.

Learn more about the flat fee billing workflow in [this article](https://help.clio.com/hc/en-us/articles/13719345938843).

## Set matter-based rate

The matter-based rate can be specified when editing a matter. When you select a matter while creating a time entry, the rate field will automatically update to reflect the matter rate. To set a matter rate:

1. Create a new matter or edit an existing matter.
2. Scroll down to **Billing preferences**.
3. Select **Hourly** and click **Add a custom rate**.

   **Note:** If the firm uses [multiple currencies](https://help.clio.com/hc/en-150/articles/14078692470427/live_preview/01JR9CQE4AS71Y7FV0DBYT3KGN#h_01HWB4DXQQFR77T4E71K9X1JZW), you can select a currency for the rate.
4. You can specify a rate for a specific user, a group, or the entire firm for this matter.
5. Click **Save matter**.

## Set client-based rate

The client-based rate can be specified when editing a contact. When you select a contact while creating a time entry, the rate field will automatically update to reflect the client rate. To set a client rate:

1. Create a new contact or edit an existing contact.
2. Scroll down to **Billing preferences**.
3. Under **Hourly** billing, click **Add a custom rate**.

   **Note:** If the firm uses [multiple currencies](https://help.clio.com/hc/en-150/articles/14078692470427/live_preview/01JR9CQE4AS71Y7FV0DBYT3KGN#h_01HWB4DXQQFR77T4E71K9X1JZW), you can select a currency for the rate.
4. You can specify a rate for a specific user, a group, or the entire firm for this matter.
5. Click **Save contact**.

## Set activity category custom rate

You can set a custom hourly rate or flat fee rate for activity categories when creating or editing activity categories. Activity categories with flat rates will override all rates except custom rates that are set when creating a time entry. Learn more about creating and editing activity categories in [this article](https://help.clio.com/hc/en-us/articles/9289744400667).

**Note:** If the firm uses [multiple currencies](https://help.clio.com/hc/en-150/articles/14078692470427/live_preview/01JR9CQE4AS71Y7FV0DBYT3KGN#h_01HWB4DXQQFR77T4E71K9X1JZW), you will only be able to select activity categories for a matter if the currency of the rate set for the the activity category matched [the currency used in the matter](https://help.clio.com/hc/en-150/articles/9285959663131-Create-Matters#billing-preference).

## Set user default billing rate

The user default rate is the rate used throughout Clio Manage for time entries for that user. This default is the lowest in the rate hierarchy, meaning that it will only be used if no other defaults (Custom rate, Flat-fee rate, Matter-based rate, Client-based rate, Activity category custom rate) have been applied.

Learn how to set or change user default billing rates [here](https://help.clio.com/hc/en-150/articles/9285360193819-Permissions-and-Billing-Rates#h_01HC36VG3ZFC6EQAKYW8B8FE3P).