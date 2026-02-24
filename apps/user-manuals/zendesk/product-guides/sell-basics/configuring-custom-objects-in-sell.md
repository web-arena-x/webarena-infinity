# Configuring custom objects in Sell

Source: https://support.zendesk.com/hc/en-us/articles/4408846681882-Configuring-custom-objects-in-Sell

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

![Available on all Sell plans](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/plan_available_sell_all.png)

Note: You need a Sunshine license to work with custom objects in Sell.

Sell has
three native object types: Leads, Contacts, and Deals. These are valuable ways to
organize your business data, but don’t necessarily represent all of your business
context. Sell only supports legacy custom objects. Use legacy custom objects if you’d
like to adjust your Sell data to better meet your needs.

With legacy custom objects you can define new object types in Sell that are specific to
your business, and then associate them with your leads, contacts, and deals. This means
you can ensure your users have all the sales context available to them directly from the
lead, contact, and deals cards.

To configure this feature you must be an admin in Support.

Taking full advantage of legacy custom objects in Sell takes three steps: Define your
custom object, link it to a lead, contact, or a deal, then create records around it.

This article covers the following process:

- [Defining your legacy custom
  object](#topic_dmk_pd2_dpb)
- [Linking a legacy custom object to
  a lead, contact, or deal](#topic_gb4_knc_2qb)
- [Creating object
  records](#topic_zps_pd2_dpb)

Related articles:

- [Adding and removing related items in
  Sell](https://support.zendesk.com/hc/en-us/articles/4408846678810)
- [How a customs object app is built for
  Sell](https://developer.zendesk.com/documentation/apps/build-an-app/how-a-custom-objects-app-is-built-for-sell)
- [Getting started with legacy custom
  objects](https://developer.zendesk.com/documentation/custom-data/custom-objects/getting-started-with-custom-objects/)

## Defining your legacy custom object

Important: This workflow requires the use of legacy custom objects. However, you might still want to switch to the new custom object experience. See [Understanding the new custom
objects](https://support.zendesk.com/hc/en-us/articles/5914453843994).

You can use legacy custom objects to represent almost anything in
Sell, such as the data of your delivery companies, contract, contractors, or
products. For example, if you sell physical goods, and you want to keep information
about delivery companies in your system, then you need to define what information to
store for each delivery company, defining how your object should be named, and what
fields it should store data for.

**To define a legacy custom object**

1. Click **Zendesk Products** (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/admin_center_product_icon.png)) in the top bar, then select **Admin
   Center**.
2. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_objects_rules_icon.png)
   **Objects and rules** in the sidebar, then select **Custom objects > Legacy
   objects**.
3. Click **Add object**.
4. In the **Object name** field, enter a name for your object, for
   example *delivery\_company*.

   Note: For multiple words you must use an
   underscore between words instead of spaces.
5. In **Add object**, click **Add property**.
6. In **Add property**, in the **Name** field, enter the name of the
   property, for example *display\_name*.

   Note: If you want your object
   records to have labels, you must define the
   `display_name` attribute. In this scenario, if
   the lead used multiple delivery companies, then you would store the
   name of the delivery companies in the `display_name`
   attribute. Then your sales reps could immediately see the names of
   the different delivery companies that are associated with that
   lead.
7. In the **Type** field, choose from the drop-down menu or leave it as
   `string` if applicable.
8. (Optional) In the **Description** field you can add a brief
   explanation.
9. (Optional) Select the **Required** check box if you want to make sure
   this field is filled in for all of the object records.
10. Click **Add**.
11. Repeat steps 6-9, but in the **Name** field enter *plan* and do
    not select **Required**.
12. Specify the order you want the attributes displayed by dragging and
    dropping the attributes into the order you want your reps to see
    them.
13. Click **Save**.

## Linking a legacy custom object to a lead, contact, or deal

Now you have added an object and decided how you want it displayed, you can think
about how it relates to objects that already exist in Sell. It is an important step
because it defines where the objects will be displayed in the system, for example on
Leads, Contacts, or Deals cards.

**To link your custom object to a lead, contact, or deal**

1. Click **Relationships > Add relationship**.
2. In the field **Relationship name**, enter a name for your relationship,
   for example *delivery\_company*.

   The relationship name is displayed in
   the widget of an object card, so ensure your label is something that
   your reps will understand.

   Note: You must define the relationship
   name using an underscore between words instead of spaces.
3. In the **Source** field, choose where you want the objects to be
   displayed, in this scenario, choose **zen:lead**.
4. In the **Relationship type** drop-down menu, choose either **1:1** or
   **1:Many**.

   If your company has multiple delivery companies, add
   1:Many so there are multiple object fields, if your company uses just
   one delivery company, then choose 1:1.

   ![Sell Custom Objects add a relationship 2](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sell_co_add_relationship2.png)
5. In the **Target** field, choose your newly created type of object. For
   example, **delivery\_company**.
6. Click **Save**.

   After you have created the objects and relationships,
   they should look similar to the following example in the related objects
   widget for your sales reps.

   ![Sell Related Objects widget](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sell_related_objects_widget.png)

Note: The related object widget only supports 10 relationship types. For each
relationship type, your rep can add a maximum of 50 related objects. If you need
more, then you must implement your own custom app.

## Creating objects records

After you have set up your data structure, you must create specific object records
for your reps to use. For example, if you want your reps to add multiple delivery
companies to their deals, then you must create a separate object record for each
company.

There are two ways to create an object record:

- Use the Zendesk API (you’ll probably need a developers' help, or use a REST
  API client )
- Use one of the apps available in Zendesk Marketplace (such as the Sunshine
  Data Editor)

You can create object records via the Zendesk REST API, which is especially handy if
you want to use custom objects to integrate with other systems, and to ensure the
information is available for your reps on the Leads, Contacts, or Deal cards. By
storing information from another system in custom objects, you can have a
minimal-code integration.

**To create custom objects via the Zendesk REST API**

- Work with your developer to store and manage customer data (see [Getting started with legacy custom
  objects](https://developer.zendesk.com/documentation/custom-data/custom-objects/getting-started-with-custom-objects)).

Note: The related object widget only supports 200 custom objects records for a given
object type. If you need more, you must write a custom app (see [How a custom objects app is built for
Sell](https://developer.zendesk.com/documentation/apps/build-an-app/how-a-custom-objects-app-is-built-for-sell/)).