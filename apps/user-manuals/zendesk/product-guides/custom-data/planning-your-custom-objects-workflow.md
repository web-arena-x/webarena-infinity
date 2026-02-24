# Planning your custom objects workflow

Source: https://support.zendesk.com/hc/en-us/articles/6070642803610-Planning-your-custom-objects-workflow

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support** | Enterprise |

Important: This article doesn't apply to [legacy custom objects](https://support.zendesk.com/hc/en-us/articles/4408834725402).

Admins can create custom objects to capture data that doesn't fit into the standard
objects in Zendesk. Extending the Zendesk data model with custom objects enables you to
seamlessly integrate your custom data with tickets, triggers, and Explore analytics.
However, deciding when and how to use custom objects to best meet your needs can be
challenging. This article guides you through questions you can use to inform this
decision.

This article contains the following topics:

- [Identifying your custom data goals](#topic_l44_4r3_myb)
- [Understanding your data](#topic_xgn_zr3_myb)
- [Planning your data model](#topic_gxg_2tj_myb)
- [Leveraging your custom data model](#topic_l4n_b13_4yb)

## Identifying your custom data goals

To resolve a ticket, agents usually pivot between Zendesk and external systems to get
the necessary information. Custom objects let you include data from external systems
in Zendesk, reducing the need to bounce between systems. To provide your agents with
this streamlined experience, you first need to identify the information they are
seeking in external systems and when they need it.

The best way to approach using custom data in your Zendesk workflow is to identify
your goals and let that guide which custom data you start with. For example, are you
trying to:

- Reduce the time agents spend on tickets?
- Improve customer satisfaction?
- Upsell products?
- Save costs by consolidating system licenses?
- Something else?

After you identify your top priorities and goals, work with your agents and team
leads to understand what data they need to work toward each goal. The following
questions are a good starting point:

- What systems currently house the data?
- At what point in their current process do they reference the data in the
  external system?
- How do they use the data after they retrieve it?
- Are there any data gaps that could be filled to further assist in meeting
  your goals?
- Do they want to use this data in reporting or business rules? (Custom
  objects are an option regardless of the answer, but if you don't plan to use
  custom data in reporting and business rules, a [custom sidebar app](https://developer.zendesk.com/documentation/apps/app-design-guidelines/support/sidebar-apps-support/) might also meet
  your needs.)

## Understanding your data

If you've determined that custom objects are the right solution for you, it's
important to understand [plan-based limitations](https://support.zendesk.com/hc/en-us/articles/5914453843994#topic_jvp_ryv_jyb) on the number of
custom objects you can create and lookup relationships fields you can define. You
should also consider your data model before creating custom objects. Sketching out a
plan before you start will save you time in the long-run.

A good way to start visualizing your data model is to create a simple spreadsheet for
each custom object. Start with a type or category of data you think might work well as an
object. All records have a *Name* field, which is text-based, so start with
that as the label for the first column. Then, continue labeling the columns with the
other data you need. These will become your custom object's fields. For example, if
your custom object is *Rental property*, your spreadsheet might look similar to
the following:

| Rental property | | | | | | |
| --- | --- | --- | --- | --- | --- | --- |
| Name | Street address | City state | Zip code | Property manager | Renter | Lease start |
| Royal Heights - 203 | 203 Herrick Lane | Richmond, VA | 23059 | John Doe | Christopher Garvey | January 17, 2023 |

Continuing with this example, you might also want an *Appliance* custom object,
which is related to your rental property object. So you'd create a second
spreadsheet similar to this:

| Appliance | | | |
| --- | --- | --- | --- |
| Appliance ID | Type | Apartment | Last Maintenance |
| RF12345 | Refrigerator | Royal Heights - 203 | 21 December 2022 |

Continue to create spreadsheets for each custom object you want to create and
populate them with your data and how the data is related to other objects in
Zendesk.

## Planning your data model

After determining which custom objects you want to create and the data those objects
need to capture, you're ready to figure out how it will work in Zendesk. You've
already identified the names of the objects and the data you want to capture, but
now you need to create the objects and add each field within Zendesk. Consider the
following:

- [Decisions you'll make when creating your custom objects](#topic_lt2_ld3_4yb)
- [Seeding your initial data](#topic_mlb_yb3_4yb)

### Decisions you'll make when creating your custom objects

When you [create a custom object](https://support.zendesk.com/hc/en-us/articles/5392409465370), you're
defining a new schema. The object has unique characteristics and relationships
to other objects and data within Zendesk. As such, you need to be intentional
when [defining an object's
fields](#topic_c5x_sd3_4yb) and [relationships](#topic_vb5_5xh_4yb).

#### Determining field types

Next, decide what field types to use. For example, when creating the Rental
property object in Zendesk, the *Street address* and *City state*
might be text or drop-down fields. *Zipcode* could be a number field,
and *Lease start* would be a date field. The *Property manager*
and *Renter* fields would be lookup fields that define the object's
relationship to users. However, these lookup fields could be defined on the
custom object or as a user field. See [Defining relationships](#topic_vb5_5xh_4yb).

Something else to consider when deciding which field types to use is
discoverability of the data. When agents [search for custom data](https://support.zendesk.com/hc/en-us/articles/6088606067866#topic_bxl_dxq_fyb) in Zendesk,
only text-based fields are checked for matches.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/custom_object_fields.png)

#### Defining relationships

[Lookup fields](https://support.zendesk.com/hc/en-us/articles/4591924111770) are how you build
relationships in Zendesk. They are the cornerstone of how your data from
standard and custom objects work together to create your data model. They're
most useful when used to define many-to-one (Many:1) relationships. For
example, each rental property will have at least one *Renter*, but you
need to decide if that relationship should be defined as the custom object's
field or as a user field. If you define the relationship as one of the
Rental property object's fields, you can only relate each rental property
record to a single user, designated as the renter. However, if you add the
lookup field to users and specify the rental property object as the related
object, you open up the possibility of defining multiple renters associated
with a single property record. Typically defining the lookup field on the
"many" side of the relationship gives you the most flexibility.

Another example would be appliances. Each rental property probably has
multiple appliances—refrigerator, stove, dishwasher. Therefore, it makes
sense to define the lookup field as one of the Appliance object's
fields.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/custom_object_lookup_appliance_to_property.png)

In both cases above, the lookup field is defined on one object and points to
the Rental property object. In this case, each Rental property record will
display lists of renters and appliances under the Related tab.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/custom_object_record_rental_apt.png)

You'll also need to think about how your objects are related to tickets and
can be used to meet your custom data goals.

### Seeding your initial data

Bulk importing records enables you to move data from an external system into
Zendesk to reflect your data at that point in time, but it won't stay
synchronized. If you continue to store and update the data externally, the
records in Zendesk will become outdated; likewise, any updates agents make to
the records in Zendesk won't be reflected on the external system. After you
create the object and import your initial data, we recommend maintaining the
data (records) in Zendesk going forward. However, if it will continue to be
maintained in an external system, you should define a plan for periodic bulk
imports.

To make it easier to get up and running with custom objects, you can perform bulk
imports to seed the initial records after you create your custom objects. If you
already compiled all of an object's records into a spreadsheet and mapped it to
the fields you defined when creating the object in Zendesk, you can probably
download or export the data into a comma-separated value (.CSV) file. Most
spreadsheet software has this option, as do many other systems that might
currently house your data. See [Bulk uploading custom object
records](https://support.zendesk.com/hc/en-us/articles/6100391508250).

Note: If your spreadsheet included data that you defined as a lookup on another
object, remove that data from your spreadsheet before importing the data. After
you've imported the custom object records, you can perform separate bulk uploads
to seed data into the lookup fields on other objects.

## Leveraging your custom data model

After you create your custom objects and seed your record data, it's time to use that
data to meet your goals. Usually, this involves [adding custom fields to your tickets](https://support.zendesk.com/hc/en-us/articles/4408883152794) and support request
forms. As with other relationships you might have identified and created earlier,
you'll also use [lookup relationship fields](https://support.zendesk.com/hc/en-us/articles/4591924111770) to do this. By surfacing
custom objects in tickets, agents can set and view relevant data without leaving the
ticket interface. Keeping the data up-to-date and accessible without
context-switching to different systems means your agents can work faster and more
effectively to meet your customers' needs.