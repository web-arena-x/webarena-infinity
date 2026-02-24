# Displaying your last 100 satisfaction ratings

Source: https://support.zendesk.com/hc/en-us/articles/4408894103706-Displaying-your-last-100-satisfaction-ratings

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Growth, Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support** | Professional or Enterprise |

Displaying your last 100 customer satisfaction ratings is more advanced to set up than using the ratings box widget to display totals. For more information on the ratings box widget, see [Displaying satisfaction ratings totals and an overall score](https://support.zendesk.com/hc/en-us/articles/4408832723866).

Zendesk provides your satisfaction ratings in JSON format. It looks something like this, where 1 is a positive rating, 0 is a negative rating:

```
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, ...]
```

As you can see, it is very basic. It's up to you to decide how to display the data.

You must be an administrator to use this feature.

## Accessing your last 100 ratings

You need to turn on satisfaction ratings, if you haven't already done so. Then you can access your last 100 satisfaction ratings.

**To turn on satisfaction ratings and access your ratings**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4408838272410), click the **People** icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_people_icon.png))
   in the sidebar, then select **Configuration > End users**.
2. Click the **Satisfaction** tab.
3. Make sure that **Allow customers to rate tickets** is selected and that you have at least 100 ratings.

   If you don't have at least 100 ratings, you'll see the following message.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sat_rating_lessthan100.png)
4. Select **Allow me to display public satisfaction statistics**.
5. Click **Save Tab**.

   The page updates with more information, including statistics based on your last 100 customer satisfaction ratings.
6. Go to http://*subdomain*.zendesk.com/satisfaction.json (where *subdomain* is your Zendesk account) to access the JSON file with your ratings.

## Displaying your last 100 ratings

The easiest way to display your ratings on a page is to use images to represent responses.

In this example, a happy Buddha face represents a positive rating, and an unhappy Buddha face represents a negative rating.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/satisfaction_rating_laughing_bud.png)

Here is the jQuery for this example (you can use any framework or language you'd like):

```
<div id="last_100_ratings"></div>
<script type="text/javascript">
$.ajax({
 url: "https://support.zendesk.com/satisfaction.json",
 dataType: "jsonp",
 cache: false,
 success:function(data){
    elem = $("#last_100_ratings"); // Change where you want the ratings rendered
    for (i=0;i<data.length;i++) {
      if (data[i] == 1) {
        elem.append('<div class="satisfaction_good"><img src="https://assets.zendesk.com/images/satisfaction/happy_buddhy.png?131..."/></div>')
      } else {
        elem.append('<div class="satisfaction_bad"><img src="https://assets.zendesk.com/images/satisfaction/sad_buddhy.png?13171..."/></div>')
      }
    }
 }
});
</script>
```

This code snippet gets your last 100 ratings from your Zendesk Support instance, then iterates through the entire length of the response (which will always be 100) and puts a smiley or sad face in the
#last\_100\_ratings element.

Other options for using this data include:

- Add this data to a graph using jCharts or a similar program.
- Collect and store your ratings data daily so you can review historical data.
- Generate an image from it to use in email newsletters or signatures.