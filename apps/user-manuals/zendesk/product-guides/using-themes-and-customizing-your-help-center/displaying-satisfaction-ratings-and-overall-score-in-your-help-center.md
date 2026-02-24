# Displaying satisfaction ratings and overall score in your help center

Source: https://support.zendesk.com/hc/en-us/articles/4408832723866-Displaying-satisfaction-ratings-and-overall-score-in-your-help-center

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Growth, Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support with** | Guide Professional or Enterprise |

Note: Support + Guide customers who are not on a Suite plan must have Support Professional or
Enterprise with any Guide plan to display satisfaction ratings and overall score in your
help center.

You can display satisfaction ratings in your help center. This lets you
show quick statistics based on your last 100 satisfaction ratings. The following data is
shown:

- Number of positive ratings
- Number of negative ratings
- Overall score (percentage of good ratings)

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/satisfaction_ratingswidetbox.png)

The numbers are based on your last 100 ratings, so it's a sliding window that is recalculated
every time you receive a rating. The appearance and wording is customizable.

## Getting the code for the ratings box

You add the ratings box by pasting a code snippet into the HTML of a page or template. You
must be an admin to get the code.

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_people_icon.png)
   **People** in the sidebar, then select **Configuration > End users**.
2. Click the **Satisfaction** tab.
3. Make sure that **Allow customers to rate tickets** is selected and that you have at
   least 100 ratings.

   If you don't have at least 100 ratings, you'll see the following
   message. In that case you have to wait until you get more ratings to use the ratings
   box.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sat_rating_lessthan100.png)
4. Select **Allow me to display public satisfaction statistics**.
5. Click **Save Tab**.

   The page updates with more information, including statistics
   based on your last 100 customer satisfaction ratings.
6. Under **How do I use it**, copy all the HTML code in the box. You'll only see this
   HTML code if you if have 100 or more satisfaction ratings.

## Adding the ratings box in the help center

Knowledge admins can add the ratings box to articles or to the home page of the help center.

**To add the ratings box to the home page of your help center**

1. In [Knowledge admin](https://support.zendesk.com/hc/en-us/articles/9041943683354#topic_b5q_nwn_s2c), click **Customize design**
   (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/guide_icon_customize.png)) in the sidebar.
2. Click the theme you want to edit to open it.
3. Click **Edit Code**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/theming_menu_option_edit_code.png)
4. In the **Templates** section, open the home page template.
5. Paste the code for the ratings box in the template.
6. Click **Save**.
7. Click **Preview** to preview the effect of your changes on the page.

**To add the ratings box to an article in the help center**

1. In [Knowledge admin](https://support.zendesk.com/hc/en-us/articles/9041943683354#topic_b5q_nwn_s2c), click the **Settings** icon
   (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/guide_icon_settings.png)) in the sidebar.
2. Ensure the **Display Unsafe Content** setting is enabled.

   In this case, you want
   to allow unsafe content like script tags.
3. Back in the help center, navigate to the article where you want the ratings box to appear.
4. Click **Edit article**.
5. Switch to the HTML editor by clicking **Source code** button on the editor's toolbar.
6. Paste the code for the ratings box in the page and click **Save**.

The ratings box appears wherever you paste the code. If you want to customize the wording, the
CSS, or place the box in a specific element on the page, see [Customizing the ratings box](#topic_zbn_2r4_zf).

## Customizing the ratings box

You can customize the satisfaction ratings box by changing the wording, changing the look,
or setting where it appears on the page.

### Customizing the wording

If you don't like the default wording that appears under the three numbers in the ratings
box, you can change it. In the ratings box code, look for the following values:

```
Satisfaction.show({
    strings: {
      goodRatings:      "Said good",
      badRatings:       "Weren't so sure",
      score:            "Overall happiness",
      zendeskPlug:      "Powered by <a href=\"http://www.zendesk.com/\">Zendesk</a>"
    }
});
```

You can edit the values in quotes.

### Customizing the look

The code you pasted into your HTML imports a CSS stylesheet:

```
 @import url(https://support.zendesk.com/stylesheets/public_satisfaction.css);
```

If you want to customize the look of the ratings box, you an add your own CSS to the page where
you put the ratings box, overwriting the CSS defined in the Zendesk stylesheet.