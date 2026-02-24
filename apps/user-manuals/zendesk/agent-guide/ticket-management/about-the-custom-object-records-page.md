# About the custom object records page

Source: https://support.zendesk.com/hc/en-us/articles/6088606067866-About-the-custom-object-records-page

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support** | Enterprise |

The Custom object records page in [Support](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb) provides a comprehensive list of
custom object records an agent has permission to access. From this page, agents and
admins can [add](https://support.zendesk.com/hc/en-us/articles/5402508938778), [view](https://support.zendesk.com/hc/en-us/articles/6093145333786#topic_skh_wwz_pyb), [search for](#topic_bxl_dxq_fyb), and [manage](https://support.zendesk.com/hc/en-us/articles/6093145333786) custom object records.

This article contains the following topics:

- [Accessing and using the Custom object records page](#topic_hzp_x1p_mwb)
- [Searching for custom object records](#topic_bxl_dxq_fyb)

## Accessing and using the Custom object records page

Agent permissions to view records are defined per role for each custom object. This
means agents in different roles likely have different levels of access to custom
object records. On Enterprise plans, admins can set permissions for every role on
each object. On all other plans, agent access to records is predefined. On all
plans, light agents and contributors have view-only access to custom object
records.

When an account has no defined custom objects or an agent doesn't have permission to
view any custom object records, the Custom objects icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/icon_custom_objects_records_page.png)) used to access the page isn't displayed in the
sidebar. When accessing the records page, you must select a custom object from the
list to see its records. The objects are displayed in alphabetical order, and only
objects you have permission to view records of are included. If an object has no
records yet, an empty list is returned.

If your account has more than 100,000 records, you might experience delays between
creating the record and seeing it in the list on the Custom object records page
because the list is updated every 6 hours.

**To access the Custom objects records list**

1. In [Support](https://support.zendesk.com/hc/en-us/articles/4408838272410), click **Custom
   objects** (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/icon_custom_objects_records_page.png)) in the sidebar.
2. Select the custom object for which you'd like to [search](#topic_bxl_dxq_fyb), [view](https://support.zendesk.com/hc/en-us/articles/6093145333786#topic_skh_wwz_pyb), [add](https://support.zendesk.com/hc/en-us/articles/5402508938778), or [manage](https://support.zendesk.com/hc/en-us/articles/6093145333786) records.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/custom_object_record_page.png)

### Data visible in the custom object records list

The custom object records list always displays the record's *name*,
*created at*, and *last updated* data. The list can be sorted by
these columns.

In addition to this standard data, the first three of a [custom object's custom fields](https://support.zendesk.com/hc/en-us/articles/5392409465370#topic_cq4_1sn_lwb) are used
as additional columns for the record list. These columns can't be used for
sorting.

### Data visible in a custom object record

When viewing a record, the details are arranged in three parts:

- A panel with all of the object's fields with the record's values.
- A Related objects tab that lists all related records, grouped by object.
  Visible by default.
- An Events tab that lists events pertaining to the record, such as its
  creation and any updates to it. See [Viewing custom object record
  events](https://support.zendesk.com/hc/en-us/articles/9174563278874).

## Searching for custom object records

As an agent, there are a variety of situations in which you might encounter a custom
object and need to search for records. For example, a lookup relationship field on a
ticket might point to a custom object or you might see custom objects mentioned on a
user's profile under the Related tab. In these cases, you might need to perform a
search to find what you're looking for.

The following details are important to understand when searching for custom object
records:

- Search queries check against all text-based fields within the records. That
  means queries can match against the Name field value and values in fields of
  the following types: Text, Regex, or Multi-line.
- Search queries match on the beginning of words only. In multi-word values,
  queries can match against the beginning of any word in the value.

You can search for custom object records in lookup relationship fields and the Custom
object records list. When searching for values in [lookup relationship fields](https://www.google.com/url?q=https://support.zendesk.com/hc/en-us/articles/4591924111770), a list of
auto-completed matches is displayed as you type.