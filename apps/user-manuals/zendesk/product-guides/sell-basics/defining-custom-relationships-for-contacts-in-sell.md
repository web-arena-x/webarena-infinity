# Defining custom relationships for contacts in Sell

Source: https://support.zendesk.com/hc/en-us/articles/4408846642202-Defining-custom-relationships-for-contacts-in-Sell

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

![Available on all Sell plans](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/plan_available_sell_all.png)

In Sell, a contact can have two types of relationships:

- A company-employee relationship
- A company hierarchy relationship

These are valuable ways to organize your business data but don’t necessarily represent all of your business contexts. For example, the contact may be an agency relationship, or a 3rd party consultant that you cooperate with, or perhaps you need to store information about resellers or brokers in Sell?

Creating custom relationships for contacts means you can represent any type of contact relationship so that it's relevant for your business context.

The following scenario represents a company-broker relationship, where you can store both companies and brokers as contacts in Zendesk Sell.

**To add a new custom relationship**

1. Click the Zendesk Products icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/admin_center_product_icon.png)) in the top bar, then select **Admin Center**.
2. Click the Sunshine icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/admin_center_sunshine_icon.png)) in the left sidebar, then click **Relationships > Add relationship**.

   ![Sell custom objects add a relationship](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sell_co_add_relationship.png)
3. In the **Relationship name** field, enter a name to label your relationship, for example *broker*.

   Ensure your label is something that your reps will understand because the relationship name is displayed in the widget of an object card. Another consideration is that relationships are also sorted alphabetically in the related objects widget.

   Note: You must define the relationship name using an underscore between words instead of spaces (for example *broker\_name*).
4. In **Source**, choose where you want the objects to be displayed, in this scenario, choose **zen:contact**.
5. In **Relationship type**, you can choose either **1:1** or **1:Many**, depending on the nature of the relationships. If one company has multiple brokers, add 1:Many, if the company has just one broker, then choose 1:1.
6. In the **Target** field, choose **zen:contact**.
7. Click **Save**.

The relationship is displayed on the object card in the related objects widget.

Note: The related object widget only supports up to 10 relationship types and your rep can add add up to 50 related objects for each relationship type.

![Sell custom objects add relationship details](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sell_co_add_relationship_details.png)