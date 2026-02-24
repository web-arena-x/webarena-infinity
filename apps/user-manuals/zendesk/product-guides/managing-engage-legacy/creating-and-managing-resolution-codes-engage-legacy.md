# Creating and Managing Resolution Codes (Engage Legacy)

Source: https://support.zendesk.com/hc/en-us/articles/9731437715738-Creating-and-Managing-Resolution-Codes-Engage-Legacy

---

Resolution codes—often labeled as disposition or wrap-up tags—are essential for categorizing interactions and gathering insights during reporting.

## Adding resolution codes

Resolution codes can be added to Engage for Amazon Connect in two ways:

- Users can manually create resolution codes
- Using a bulk upload

You will need Administrator access in Engage for Amazon Connect in order to add Resolution Codes.

## Adding resolution codes manually

To access the **Administrator settings** in Engage for Amazon Connect, click on the cogs icon on the left-hand side of the screen.

![](https://support.zendesk.com/hc/article_attachments/9731466137370)

Click on the  **Resolution Codes** tab.

![](https://support.zendesk.com/hc/article_attachments/9731498573722)

At the bottom of the page you will see 2 buttons, **Add code** and **Add folder**. Depending on how many resolution codes you want to enter, it might be a good idea to start by adding a folder to store them.

Enter a name for your new folder and click on the green tick to save.

![](https://support.zendesk.com/hc/article_attachments/9731474606490)

Now click on the created folder and select the **Add Code** button. Enter the name of your resolution code,  select a color from the color options and click on the green tick to save your new code.

![](https://support.zendesk.com/hc/article_attachments/9731498606106)

Once you have added all your codes, click on **Save Draft** and then on the **Publish** button to publish your codes and make it available for your company to use.

## Uploading resolution codes in bulk

Engage for Amazon Connect allows you to bulk upload categories and codes using a *.csv* or *.xml* file. This is suitable for code structures with large amounts of categories and codes.

The resolution code bulk upload template needs to have the following fields:

![](https://support.zendesk.com/hc/article_attachments/9731437801370)

- **ID:** *Optional*. This can be a numeric or alphanumeric code.
- **Name:** Name of the code or description.
- **Color Swatch Name:** Choose one of nine available colors (illustrated below). Teal is the default.
- **Category Level One:** *Optional.* This creates the first level category.
- **Category Level Two:** *Optional.* This creates the second level category.
- **Category Level Three:** *Optional.* This creates the third level category.

Use colors for your codes  to help differentiate them. The template contains a column labeled *Color Swatch Name*. Use this as a reference for the names (Teal is the default color if left blank). You can enter the Hex Code or the Common name in the template.

![](https://support.zendesk.com/hc/article_attachments/9731466189338)

## Queue restriction

Resolution codes can be restricted to specific queues. Admins can enable queue restriction on top level categories (folders). These categories, including all subcategories and codes, will only appear for agents that have these queues in their routing profile.

‍

To restrict categories by queue:

‍

1. Navigate to **Settings** and click on the **Resolution Codes** tab.

![](https://support.zendesk.com/hc/article_attachments/9731498573722)

1. Hover over the desired folder, you will see that icons appear to the far right.

![](https://support.zendesk.com/hc/article_attachments/9731462124954)

1. Click on the visibility (eye 👁️) icon.
2. A pop-up will appear, prompting you to select the relevant queue(s).

![](https://support.zendesk.com/hc/article_attachments/9731449714202)

1. Select the queue(s) and then click **Save queues***.*
2. Ensure your changes are saved by clicking **Save Draft** and then **Publish***.*

‍

## Trigger workflow actions

If you would like to ensure that resolution codes are selected before ending the contact, this can be enabled within workflows. You will need Administrator access in Engage for Amazon Connect.

‍

1. Navigate to **Settings** and click on the **Workflows** tab.
2. Select **Edit** on the desired workflow.
3. In the section After Contact Work, under Resolution Codes, select Required.

‍

![](https://support.zendesk.com/hc/article_attachments/9731462162714)

‍