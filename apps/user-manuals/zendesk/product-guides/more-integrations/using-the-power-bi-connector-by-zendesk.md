# Using the Power BI Connector by Zendesk

Source: https://support.zendesk.com/hc/en-us/articles/6700481028634-Using-the-Power-BI-Connector-by-Zendesk

---

Disclaimer: Zendesk doesn't provide support for Power BI. See the [Microsoft documentation](https://learn.microsoft.com/en-us/power-bi/) if you need assistance.

Power BI by Microsoft is a collection of software services, apps, and connectors that work together to turn your unrelated sources of data into interactive insights. Using the Power BI Connector by Zendesk allows you to import your Zendesk data to Power BI.

This article covers the following topics:

- [Overview of the Power BI Connector by Zendesk](#h_01J04AFGEYQ1TRA1VJ3JNNDMG8)
- [Signing in](#h_01HNXDDB13R3F5RF3BTBAYE21E)
- [Using the Power Query M language to query data](#h_01HNXDFZAVQPFT9284740HYXBS)

Related articles:

- [Microsoft Power BI error message: The downloaded data is HTML, which isn't the expected type](https://support.zendesk.com/hc/en-us/articles/7389055394586)

## Overview of the Power BI Connector by Zendesk

The existing Zendesk Power BI connector by Microsoft has a [known issue](https://learn.microsoft.com/en-us/power-query/connectors/zendesk#limitations-and-issues) where it can’t retrieve records for more than 1000 rows. For example, if an account has more than 1000 tickets, it returns the following 422 error:

![](https://support.zendesk.com/hc/article_attachments/6700435341082)

Zendesk has developed a new Power BI connector named **Zendesk Data** that solves this issue. The new connector uses Cursor Based Pagination (CBP) to retrieve data from the Zendesk API.

![](https://support.zendesk.com/hc/article_attachments/6700481026330)

![BetaLegacy2.jpeg](https://support.zendesk.com/hc/article_attachments/9484173199514)

## Signing in

The sign in experience is the same as the legacy connector.

![](https://support.zendesk.com/hc/article_attachments/6700435342106)

![](https://support.zendesk.com/hc/article_attachments/6700481027610)

![](https://support.zendesk.com/hc/article_attachments/6700435343130)

After you sign in, you’ll see all existing endpoints are available in the new connector.

![](https://support.zendesk.com/hc/article_attachments/6700435343386)

## Using the Power Query M language to query data

Disclaimer: Zendesk doesn't provide support for the Power Query M language. See the [Microsoft documentation](https://learn.microsoft.com/en-us/power-bi/transform-model/desktop-query-overview) if you need assistance.

If you are using the Power Query M language to query data, there’s a slight difference in the beginning part of the query. The legacy connector uses **Zendesk.Tables()** to initialize the Source:

```
let  
    Source = Zendesk.Tables("https://yoursubdomain.zendesk.com"),  
    views = Source{[Key="tickets"]}[Data]  
in  
    views
```

The new connector uses **ZendeskData.Contents()** to initialize the Source:

```
let  
    Source = ZendeskData.Contents("https://yoursubdomain.zendesk.com", []),  
    Users = Source{[Name="Users"]}[Data]  
in  
    Users
```

If you have existing queries using the legacy connector, change the Source initialization part and the rest of the code will work properly.

If you are using the Power BI connector in any other way, please contact [Zendesk Customer Support](https://support.zendesk.com/hc/en-us/articles/4408843597850), and we will provide a migration path.