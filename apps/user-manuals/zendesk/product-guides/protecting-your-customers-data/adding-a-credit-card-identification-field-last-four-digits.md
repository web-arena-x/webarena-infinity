# Adding a credit card identification field (last four digits)

Source: https://support.zendesk.com/hc/en-us/articles/4408842751002-Adding-a-credit-card-identification-field-last-four-digits

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Enterprise or Enterprise Plus |

|  |  |
| --- | --- |
| **Support** | Enterprise |

If your agents or end users need to use the last four digits of a credit card number in tickets for verification purposes, you can add a credit card field to the ticket form.

In addition to describing how to add a credit card identification field, this article makes additional recommendations to make your Zendesk more secure. The recommendations won’t make your Zendesk PCI-compliant, but they will help make it more secure.

Topics covered:

- [Adding the credit card number field to your ticket form](#topic_fmm_rsl_lw)
- [Recommendation: Enable automatic redaction for other fields](#topic_vrt_v5l_lw)

## Adding the credit card number field to your ticket form

You can use the credit card number field within tickets, allowing end users and agents to enter the last four digits of the credit card number for identification purposes.

This section describes how to add the field and outlines its limitations.

**To add the credit card number field**

1. Sign in to your Zendesk account as an administrator.
2. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_objects_rules_icon.png) **Objects and rules** in the sidebar, then select **Tickets > Fields**.
3. Click **Add field** on the right side.
4. Click the **Credit card** field.
5. Set the following field properties and click **Save**.

   | Field property | Values |
   | --- | --- |
   | Title | Any name |
   | Read-only for end users | Unchecked (see note below) |
   | Editable for end users | Unchecked |

### Limitations

The following are the known limitations with the credit card number field.

**Product limitations**

- Zendesk Support Mobile App - The field is read-only.
- Web Widget - The field is not supported.
- Mobile SDK - The field only accepts 4 digits.
- App framework apps - If the field is built into an app installed from the Zendesk Marketplace. Apps could view the outgoing field contents in the browser console before it’s redacted by Zendesk. Evaluate any apps for this vulnerability before activating them.
- Ticket sharing - The field can’t be shared between Zendesk accounts.

**Other limitations**

- Zendesk Support doesn’t store a full credit card number.
- PCI allows storing the first 6 and last 4 digits of a credit card, but the credit card field in Zendesk Support can retain only the last 4.
- Only numbers can be stored in the credit card number field. All other characters entered into the field are removed when the input is saved.
- Out-of-the-box functionality to support other fields related to credit card authentication data is not available. This includes but isn’t limited to expiration date, card verification value (CVV), or personal identification number (PIN) fields. To use Zendesk Support in a PCI-compliant manner, you should not request this information from your end users in the comments of support tickets. PCI DSS only allows this information to be used during the credit card authorization process, and Zendesk Support is not a payment processing application.
- Additional features implemented by the administrator may affect the security of the credit card field.

## Recommendation: Enable automatic redaction for other fields

There’s no guarantee end users or agents will always use the credit card number field. They might enter a credit card number in the ticket comments or in another custom ticket field. To redact these numbers as well, see [Automatically redacting credit card numbers from tickets](https://support.zendesk.com/hc/en-us/articles/4408822124314) in Help Center.

Note: This feature is not PCI-compliant at this time. It’s offered as an additional layer of security to prevent cardholder data from spreading in your Zendesk account and email notifications.