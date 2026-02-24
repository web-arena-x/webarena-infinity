# Creating and managing Contact Center resolution codes

Source: https://support.zendesk.com/hc/en-us/articles/9696174546970-Creating-and-managing-Contact-Center-resolution-codes

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **Add-on** | Zendesk for Contact Center |

Verified AI summary ◀▼

Learn how to add resolution codes to your Contact Center, which help categorize interactions and enhance reporting insights. You can manually create codes or use a bulk upload via CSV or XML files. Admin access is required. Additionally, you can restrict codes to specific queues and set up workflows to ensure codes are selected before ending contacts.

Learn how to add resolution codes in Zendesk for Contact Center using two different methods: manual creation or bulk upload.

Resolution codes, often labeled as disposition or wrap-up tags, are essential for categorizing interactions and gathering insights during reporting.

Resolution codes can be added to Contact Center in two ways:

- Users can manually create resolution codes
- Using a bulk upload

You need admin access in Contact Center to add resolution codes.

This article contains the following topics:

- [Adding resolution codes manually](#topic_rc1_frc_qgc)
- [Adding resolution codes from a file](#topic_dr3_frc_qgc)
- [Restricting resolution codes to a specific queue](#topic_hkh_4rc_qgc)
- [Using trigger workflow actions](#topic_vcm_4rc_qgc)

## Adding resolution codes manually

**To manually add resolution codes**

1. To access the **Administrator settings** in Contact Center, click the cogs icon on the left-hand side of the screen.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/cc_rc_10.png)
2. Click the Resolution Codes tab.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/cc_rc_9.png)
3. At the bottom of the page you will see 2 buttons, **Add code** and **Add folder**. Depending on how many resolution codes you want to enter, it might be a good idea to start by adding a folder to store them. Enter a name for your new folder and click the green tick to save it.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/cc_rc_8.png)
4. Click the folder you created, and then click **Add Code**. button.
5. Enter the name of your resolution code, select a color from the color options and click the green tick to save your new code.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/cc_rc_7.png)
6. Once you have added all your codes, click **Save Draft** and then click **Publish** to publish your codes and make them available for your company to use.

## Adding resolution codes from a file

You can bulk upload Contact Center categories and codes using a *.csv* or *.xml* file. This is useful if you have a large number of categories and codes.

**To add resolution codes from a file**

1. Make sure that the resolution code bulk upload template has the following fields:
   - **ID:***Optional*. This can be a numeric or alphanumeric code.
   - **Name:** Name of the code or description.
   - **Color Swatch Name:** Choose one of nine available colors (illustrated below). Teal is the default color.
   - **Category Level One:***Optional.* This creates the first level category.
   - **Category Level Two:***Optional.* This creates the second level category.
   - **Category Level Three:***Optional.* This creates the third level category.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/cc_rc_6.png)
2. You can use colors for your codes to help differentiate them. The template contains a column labeled *Color swatch name*. Use this column as a reference for the names. You can enter the hex code or the common name in the template.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/cc_rc_5.png)

## Restricting resolution codes to a specific queue

Resolution codes can be restricted to specific queues. Admins can enable queue restriction on top-level categories (folders). These categories, including all subcategories and codes, will only appear for agents who have these queues in their routing profile.

**To restrict categories by queue**

1. In Contact Center settings, click the **Resolution Codes** tab.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/cc_rc_4.png)
2. Hover over the required folder. You will see that icons appear to the right.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/cc_rc_3.png)
3. Click the visibility (eye) icon.
4. A pop-up will appear, prompting you to select the relevant queues.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/cc_rc_2.png)
5. Select the queues you want and then click **Save queues**.
6. Make sure that your changes are saved by clicking **Save Draft** and then **Publish***.*

## Using trigger workflow actions

If you want to ensure that resolution codes are selected before ending the contact, this can be enabled within workflows. You will need Administrator access in Zendesk for Contact Center.

**To configure trigger workflow actions‍**

1. In Contact Center, navigate to **Settings** and click the **Workflows** tab.
2. Click **Edit** for the required workflow.
3. In the section After Contact Work, under Resolution Codes, select Required.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/cc_rc_1.png)