# Personalization Tokens for Engage CTI (Engage Legacy)

Source: https://support.zendesk.com/hc/en-us/articles/9731450441114-Personalization-Tokens-for-Engage-CTI-Engage-Legacy

---

Sometimes you will need to reference information for a Salesforce object with Engage's other features such as Snippets or Tasks. Personalization Tokens in Engage CTI act as placeholders that pull real-time data from Salesforce records as an Agent browses.

## Available Tokens

These tokens allow you to read information the Agent looking at in Salesforce.

1. **cti.current\_type:** Displays the object type (e.g., contact, lead, task).
2. **cti.current\_name:** Shows the name of the object.
3. **cti.current\_id:** Provides the Salesforce ID.
4. **cti.current\_url:** Gives the link to the Salesforce page.

## Example Use-Cases

### Referencing Case details in Notes

By using some or all of these Personalisation Token in a [Snippet](https://support.zendesk.com/hc/en-us/articles/9731500513562), Agents can easily add details of a Case they have just created in a Note. This might be useful when looking historical conversation, or for an agent they are transferring a call to.

![](https://support.zendesk.com/hc/article_attachments/9731499773338)

‍

### Performing Backend Processing using a Task

The options for [Tasks](https://support.zendesk.com/articles/using-task-templates) are endless but could include:

- Enriching Cases with information from the Transcript or Previous Conversations
- Sending an Email with details of the Case
- Sending an Internal notification about a new Lead based on a Call

![](https://support.zendesk.com/hc/article_attachments/9731467004314)