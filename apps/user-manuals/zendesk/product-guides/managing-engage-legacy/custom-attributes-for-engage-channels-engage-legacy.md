# Custom Attributes for Engage Channels (Engage Legacy)

Source: https://support.zendesk.com/hc/en-us/articles/9731449668890-Custom-Attributes-for-Engage-Channels-Engage-Legacy

---

Any conversations on Engage Channels (Social, email or SMS) have custom attributes set that can be used for routing in contact flows.

This page lists the custom attributes set by Local Measure Bridge or used to power features within Engage

‍

## Voice

| Attribute | Purpose | Remarks |
| --- | --- | --- |
| recording | Indicates whether the contact is being recorded. Possible values are “true” and “false” | This attribute is used in Engage to show pause call recording button if recording is “true” |

## Email

| Attribute | Purpose | Remarks |
| --- | --- | --- |
| \_hidden\_contact\_origin | Customer’s email address |  |
| \_hidden\_contact\_destination | Destination email address |  |
| \_hidden\_message\_id | Used in building agent reply message |  |
| \_hidden\_references | Used in building agent reply message |  |
| subject | Email subject |  |
| from\_email | Customer’s email address | This needs to be deprecated. Replaced by \_hidden\_contact\_origin |
| to\_email | Destination email address | This needs to be deprecated. Replaced by \_hidden\_contact\_destination |
| EmailAddress | Customer’s email address |  |
| FullName | Customer’s full name |  |
| user\_type | Indicates messaging platform | value is “ses” |

## Facebook & Instagram

| Attribute | Purpose | Remarks |
| --- | --- | --- |
| FullName | Customer’s full name |  |
| \_hidden\_contact\_origin | Customer’s FB Page Scoped ID | This page scoped id is a unique ID for the customer and specific page. These means that if a client has multiple pages linked a single customer would have different IDs when they are interacting with each page. |
| \_hidden\_contact\_destination | Contact Center FB account ID |  |
| user\_type | Indicates messaging platform | value is “facebook” |
| \_message\_type | Indicates if the message is a story mention or a story reply so that the contact flow designer can handle them differently | instagram\_story\_reply instagram\_story\_mention |
| \_messenger\_ref | This will be added if the message ref is present | https://developers.facebook.com/docs/messenger-platform/discovery/m-me-links |

## WhatsApp

| Attribute | Purpose | Remarks |
| --- | --- | --- |
| PhoneNumber | Customer’s phone number |  |
| \_hidden\_contact\_origin | Customer’s phone number prefixed with “whatsapp:” |  |
| \_hidden\_contact\_destination | Contact Center phone number prefixed with “whatsapp:” |  |
| user\_type | Indicates messaging platform | value is “whatsapp” |
| phone | Customer’s phone number | To be deprecated. Replaced by PhoneNumber. |

## SMS

| Attribute | Purpose | Remarks |
| --- | --- | --- |
| PhoneNumber | Customer’s phone number |  |
| \_hidden\_contact\_origin | Customer’s phone number |  |
| \_hidden\_contact\_destination | Contact Center phone number |  |
| user\_type | Indicates messaging platform | value is “sms” |
| phone | Customer’s phone number | To be deprecated. Replaced by PhoneNumber. |

## X (Twitter)

| Attribute | Purpose | Remarks |
| --- | --- | --- |
| \_hidden\_contact\_origin | Customer Twitter ID |  |
| \_hidden\_contact\_destination | Contact Center Twitter ID |  |
| FullName | Customer’s full name |  |
| user\_type | Indicates messaging platform | value is “twitter” |

## Tasks

| Attribute | Purpose | Remarks |
| --- | --- | --- |
| \_created\_by\_agent\_id | Agent ID for the user that creates the task | Can be used in a Set Working Queue Block to route the task back the same agent |