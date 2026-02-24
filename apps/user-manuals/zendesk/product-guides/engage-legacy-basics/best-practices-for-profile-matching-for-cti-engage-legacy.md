# Best Practices for Profile Matching for CTI (Engage Legacy)

Source: https://support.zendesk.com/hc/en-us/articles/9731474421914-Best-Practices-for-Profile-Matching-for-CTI-Engage-Legacy

---

## Enable Salesforce Contact ID matching rule

This will mean the Connect Customer Profile will match based on the Contact Attribute.

![](https://support.zendesk.com/hc/article_attachments/9731461899802)

## Linking records in Engage

‍

If a profile is not linked to a Salesforce Contact (ie. has no **sfdcContactId**), the agent will see a banner prompting them to link the profile to the Contact they are looking at in Salesforce. Once this is done, the **sfdcContactId** is added to the profile.

![](https://support.zendesk.com/hc/article_attachments/9731437552154)

‍