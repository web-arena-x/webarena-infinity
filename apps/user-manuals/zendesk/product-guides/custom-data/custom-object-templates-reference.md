# Custom object templates reference

Source: https://support.zendesk.com/hc/en-us/articles/10134429187610-Custom-object-templates-reference

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support** | Enterprise |

With
[custom objects](https://support.zendesk.com/hc/en-us/articles/5914453843994),
admins can create custom
objects to capture data that doesn't fit into standard objects. To make
it easier,
Zendesk provides templates for the most common types of custom objects.

This article describes the templates you can use when creating custom
objects. However,
all of the predefined values and fields in the templates are customizable.
For more
information about creating new custom objects, see
[Creating custom objects to integrate with custom data](https://support.zendesk.com/hc/en-us/articles/5392409465370).

The following object templates are available:

- [Contracts](#topic_ipt_4gn_whc)
- [Orders](#topic_bxc_gcf_whc)
- [Products](#topic_cy4_ly2_whc__ul_ptx_dcf_whc)
- [Projects](#topic_xxz_gcf_whc)
- [Subscriptions](#topic_uhm_hcf_whc)

## Contracts template

When using the contracts template, the object is automatically named
*Contracts*
and the following fields are automatically defined for the custom
object:

| Field name | Field type |
| --- | --- |
| Name | Text This is the standard custom object *name* field. |
| Contract ID | Text This is the standard custom object *external ID* field. |
| Organization | Lookup relationship |
| Start date | Date |
| End date | Date |
| Status | Drop-down Predefined values: Active, Inactive, Completed, Superceeded, Renewed, Expired |
| Owner | Lookup relationship |
| Total contract value | Decimal |
| Contract term (months) | Number |
| Special terms | Text |

## Orders template

When using the orders template, the object is automatically named
*Orders* and
the following fields are automatically defined for the custom object:

| Field name | Field type |
| --- | --- |
| Order name | Text This is the standard custom object *name* field. |
| Order ID | Text This is the standard custom object *external ID* field. |
| Order status | Drop-down Predefined values: Shipped, Processing, Delivered |
| Quantity | Integer |
| Price at purchase | Decimal |
| Total amount | Decimal |
| User | Lookup relationship |
| Order date | Date |
| Shipping address | Multi-line |
| Description | Multi-line |

## Products template

When using the products template, the object is automatically named
*Products*
and the following fields are automatically defined for the custom
object:

| Field name | Field type |
| --- | --- |
| Product name | Text This is the standard custom object *name* field. |
| Product ID | Text This is the standard custom object *external ID* field. |
| Description | Multi-line |
| Product category | Text |
| Quantity available | Integer |
| Creation date | Date |
| Last updated | Date |

## Projects template

When using the projects template, the object is automatically named
*Projects*
and the following fields are automatically defined for the custom
object:

| Field name | Field type |
| --- | --- |
| Project name | Text This is the standard custom object *name* field. |
| Project ID | Text This is the standard custom object *external ID* field. |
| Project description | Multi-line |
| Start date | Date |
| End date | Date |
| Project status | Dropdown Predefined values: Planned, In progress, On hold, Completed |
| Project manager | Lookup relationship |

## Subscriptions template

When using the subscriptions template, the object is automatically
named
*Subscriptions* and the following fields are
automatically defined for the
custom object:

| Field name | Field type |
| --- | --- |
| Subscription name | Text This is the standard custom object *name* field. |
| Subscription ID | Text This is the standard custom object *external ID* field. |
| Organization ID | Lookup relationship |
| Start date | Date |
| End date | Date |
| Status | Drop-down Predefined values: Active, Canceled, Draft, Expired |
| Subscription type | Drop-down Predefined values: Trial, Standard, Enterprise, Starter, Monthly, Yearly |
| Contract term | Integer |
| Description | Multi-line |