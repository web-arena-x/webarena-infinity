# Creating and Managing Snippets (Engage Legacy)

Source: https://support.zendesk.com/hc/en-us/articles/9731437731354-Creating-and-Managing-Snippets-Engage-Legacy

---

Snippets are predefined responses that can be easily accessed using shortcut commands. Snippets are perfect for defining common responses such as greetings or answers to frequently asked questions.

Use snippets to shorten the time spent typing by your agents thereby enabling faster responses, increasing efficiency, and improving the customer experience.

You will need Administrator access in Engage for Amazon Connect in order to configure snippets.

‍

## Creating a new snippet

To access the **Administrator settings** in Engage for Amazon Connect, click on the cogs icon on the left-hand side of the screen.

![](https://support.zendesk.com/hc/article_attachments/9731498573210)

Click on the  **Snippets** tab and select the **Add new snippet** button.

![](https://support.zendesk.com/hc/article_attachments/9731462067098)

To create snippets, you will need:

- A name for the snippet.
- Your snippet text.
- Content types restrictions: This is where you would like them to appear - external replies, internal notes or tasks. A snippet can be made available to as many content types as you like.
- Queue restrictions: This is where you can restrict the use of the snippet to selected queues. If you select no queues, then the snippet is available to everyone.

![](https://support.zendesk.com/hc/article_attachments/9731498611482)

Once you have entered all the relevant information, click on **Create Snippet** to save your snippet.

## Personalization tokens

The snippet responses can be customized using personalization tokens to improve customer experience. They can be thought of as placeholders that will be used to include stored attributes such as the customer’s name, phone number, account ID or other information.

The format used is *{{user.attribute}}* as shown below.

![](https://support.zendesk.com/hc/article_attachments/9731449685146)

### Setting a fallback

If the attribute doesn’t exist or is empty, by default the token wont be replaced. However, you can provide a fallback in the template using this syntax:

{{contact.first\_name || "dude"}}

## Restrictions

Restrictions limit use of the snippet depending on the case. This can be set under Content Type and Queue Restriction. Limiting the snippets to certain content or queues is helpful for separating and organizing your snippets.

1. Navigate to **Settings** and click on the **Snippets** tab.
2. Click on the snippet you wish to edit.
3. Select the restrictions.
4. Click the **Save snippet** button.

‍

![](https://support.zendesk.com/hc/article_attachments/9731466193050)

‍