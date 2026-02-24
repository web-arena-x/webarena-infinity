# Using personalization tokens in Contact Center

Source: https://support.zendesk.com/hc/en-us/articles/9696137593626-Using-personalization-tokens-in-Contact-Center

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **Add-on** | Zendesk for Contact Center |

Verified AI summary ◀▼

Personalization tokens let you add customer and company details into messages, templates, and snippets. Enclose tokens in double curly brackets to autofill fields, like `{{customer.FirstName}}`. If an attribute is missing, use a fallback with `{{contact.first_name || "Unknown"}}`. This feature helps tailor interactions by using available customer data, enhancing the support experience.

Personalization tokens are placeholders within Zendesk for Contact Center that can be used to add customer and company attributes into several areas such as snippets, welcome messages, task templates, and utilities.

When a personalization token is used, it gets replaced by the value stored for that attribute, associated to the customer profile or contact.

This article contains the following topics:

- [Using personalization tokens](#topic_gdd_sgg_rgc)
- [Personalization token reference](#topic_nnq_sgg_rgc)

## Using personalization tokens

Personalization tokens can be used to autofill task template fields or within snippets. They must be enclosed in double curly brackets.

For example:

```
Hello {{customer.FirstName}}, welcome to Cloud Company. My name is {{user.first_name}}, how can I help you today?
```

If the attribute doesn’t exist or is empty, by default the token wont be replaced. However, you can provide a fallback in the template using this syntax:

```
{{contact.first_name || "Unknown"}}
```

## Personalization token reference

The table below lists all of the available personalization tokens.

| | | |
| --- | --- | --- |
| **Category** | **Personalization token** | **Description** |
| user | {{user.first\_name}} | The Contact Center user's first name |
| user | {{user.last\_name}} | The Contact Center user's last name |
| user | {{user.full\_name}} | The Contact Center user's full name |
| customer | {{customer.ProfileId}} | The customer profile ID |
| customer | {{customer.AccountNumber}} | The customer profile's account number |
| customer | {{customer.AdditionalInformation}} | The customer profile's additional information |
| customer | {{customer.BirthDate}} | The customer profile's date of birth |
| customer | {{customer.BusinessEmailAddress}} | The customer profile's business email address |
| customer | {{customer.BusinessName}} | The customer profile's business name |
| customer | {{customer.BusinessPhoneNumber}} | The value set in the customer profile's business phone number |
| customer | {{customer.EmailAddress}} | The customer profile's email address |
| customer | {{customer.FirstName}} | The customer profile's first name |
| customer | {{customer.Gender}} | The customer profile's gender |
| customer | {{customer.HomePhoneNumber}} | The customer profile's home phone number |
| customer | {{customer.LastName}} | The customer profile's last name |
| customer | {{customer.MiddleName}} | The customer profile's middle name |
| customer | {{customer.MobilePhoneNumber}} | The customer profile's mobile phone number |
| customer | {{customer.PartyType}} | The customer profile's party type |
| customer | {{customer.PersonalEmailAddress}} | The customer profile's personal email address |
| customer | {{customer.PhoneNumber}} | The customer profile's phone number |
| customer | {{customer.ShippingAddress}} | The customer profile's shipping address |
| customer | {{customer.Address}} | The customer profile's address |
| customer | {{customer.BillingAddress}} | The customer profile's billing address |
| customer | {{customer.MailingAddress}} | The customer profile's mailing address |
| customer | {{customer.my\_custom\_attribute}} | The customer profile's custom attributes, |
| contact | {{contact.contactId}} | The CTR contact ID for the active contact |
| contact | {{contact.my\_custom\_attribute}} | The value set as a custom attribute in the contact (for example, a set contact attributes block in the contact flow). Replace *my\_custom\_attribute* with the name of the custom attribute |