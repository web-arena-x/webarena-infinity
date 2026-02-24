# Personalization Tokens (Engage Legacy)

Source: https://support.zendesk.com/hc/en-us/articles/9731499735706-Personalization-Tokens-Engage-Legacy

---

Personalization tokens are a set of placeholders within Engage that can be used to add customer and company attributes attributes into various areas such as snippets, welcome messages, task templates and utilities.

‍

## Using personalization tokens

When a personalization token is used, it gets replaced by the value stored for that attribute, associated to the customer profile or contact.

## Example usage

Personalization tokens can be used to autofill Task template fields or within Snippets. They need to be enclosed in double curly brackets. Here's an example Snippet:

Hello {{customer.FirstName}}, welcome to Cloud Company. My name is {{user.first\_name}}, how can I help you today?

## Setting a fallback

If the attribute doesn’t exist or is empty, by default the token wont be replaced. However, you can provide a fallback in the template using this syntax:

{{contact.first\_name || "dude"}}

## List of personalization tokens

Below is a list of available personalisation tokens:

| Category | Personalization token | Description |
| --- | --- | --- |
| user | {{user.first\_name}} | The value set in the Engage user’s first name |
| user | {{user.last\_name}} | The value set in the Engage user’s last name |
| user | {{user.full\_name}} | The value set in the Engage user’s full name |
| customer | {{customer.ProfileId}} | The value set in the Customer Profile’s ID |
| customer | {{customer.AccountNumber}} | The value set in the Customer Profile’s account number |
| customer | {{customer.AdditionalInformation}} | The value set in the Customer Profile’s additional information |
| customer | {{customer.BirthDate}} | The value set in the Customer Profile’s date of birth |
| customer | {{customer.BusinessEmailAddress}} | The value set in the Customer Profile’s business email address |
| customer | {{customer.BusinessName}} | The value set in the Customer Profile’s business name |
| customer | {{customer.BusinessPhoneNumber}} | The value set in the Customer Profile’s business phone number |
| customer | {{customer.EmailAddress}} | The value set in the Customer Profile’s email |
| customer | {{customer.FirstName}} | The value set in the Customer Profile’s first name |
| customer | {{customer.Gender}} | The value set in the Customer Profile’s gender |
| customer | {{customer.HomePhoneNumber}} | The value set in the Customer Profile’s home phone number |
| customer | {{customer.LastName}} | The value set in the Customer Profile’s last name |
| customer | {{customer.MiddleName}} | The value set in the Customer Profile’s middle name |
| customer | {{customer.MobilePhoneNumber}} | The value set in the Customer Profile’s mobile phone number |
| customer | {{customer.PartyType}} | The value set in the Customer Profile’s party type |
| customer | {{customer.PersonalEmailAddress}} | The value set in the Customer Profile’s personal email address |
| customer | {{customer.PhoneNumber}} | The value set in the Customer Profile’s phone number |
| customer | {{customer.ShippingAddress}} | The value set in the Customer Profile’s shipping address |
| customer | {{customer.Address}} | The value set in the Customer Profile’s address |
| customer | {{customer.BillingAddress}} | The value set in the Customer Profile’s billing address |
| customer | {{customer.MailingAddress}} | The value set in the Customer Profile’s mailing address |
| customer | {{customer.my\_custom\_attribute}} | The value set in the Customer Profile’s custom attributes, note that the my\_custom\_attribute part of the token needs to be updated based on the name of the custom attribute |
| contact | {{contact.contactId}} | The CTR Contact ID for the active contact |
| contact | {{contact.my\_custom\_attribute}} | The value set as a custom attribute in the contact (eg. via a Set Contact Attributes block in the Contact Flow), note that the my\_custom\_attribute part of the token needs to be updated based on the name of the custom attribute |