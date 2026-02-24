# Organizing  drop-down field values into nested lists

Source: https://support.zendesk.com/hc/en-us/articles/4408829395738-Organizing-drop-down-field-values-into-nested-lists

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

You can create drop-down lists that contain multiple levels of organization (up to 66). This is referred to as a nested drop-down list and can be accomplished with the same technique used to categorize macros (see [Categorizing macros](https://support.zendesk.com/hc/en-us/articles/4408884166554#topic_dpr_k1j_mw)).

For information about creating custom drop-down fields, see [Adding custom ticket fields](https://support.zendesk.com/hc/en-us/articles/4408883152794), [Adding custom fields to users](https://support.zendesk.com/hc/en-us/articles/4408822051866), and [Adding custom fields to organizations](https://support.zendesk.com/hc/en-us/articles/4408842677786).

The values of your custom field options contain the categories and selection value separated by double colons (::). For example: `Digital SLR
Cameras::Professional::Mondocam XD 80` has three layers, with the last value being the one reflected in the field when selected.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/custom_dd_field_organize.png)

In this example, if the user selected *Digital SLR cameras*, then selected *Professional*, and finally selected *Mondocam XD 80*, the field value would be *Mondocam XD 80*.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/custom_dd_field_value.png)

Expanding on the digital camera example, other drop-down values might be:

| Value |
| --- |
| Digital SLR Cameras::Professional::Mondocam XD 80 |
| Digital SLR Cameras::Professional::Mondocam XD 89 |
| Digital SLR Cameras::Consumer::Mondocam HD 1000 |
| Digital SLR Cameras::Consumer::Mondocam HD 2000 |
| Digital Compact Cameras::Buddah XS 18-M |
| Digital Compact Cameras::Buddah ZD-89 |

You can create up to 2,000 values in a custom drop-down list, with a maximum length of 255 characters per field.

When creating or editing a drop-down field values you can use the Preview panel, on the right, to test the experience.