# Analytics: Using 'AND' Filtering in Custom Reports

Source: https://support.joinhandshake.com/hc/en-us/articles/360000867668-Analytics-Using-AND-Filtering-in-Custom-Reports

---

Handshake only filters and supports 'OR' logic when filtering on multiple dimensions within a single field in the Analytics tool. However, you can build your own calculations if you need to add 'AND' filtering to your report!

## Set up an 'AND' calculation

In order to utilize 'AND' logic, you will need to set up a calculation within the Analytics report.

To experience the steps, open this [example report](https://app.joinhandshake.com/analytics/explore_embed?insights_page=ZXhwbG9yZS9nZW5lcmF0ZWRfaGFuZHNoYWtlX3Byb2R1Y3Rpb24vc3R1ZGVudHM_cWlkPTJ1cTNCZkYxYzQ3M3hYRE1pVGRycGsmZW1iZWRfZG9tYWluPWh0dHBzOiUyRiUyRmFwcC5qb2luaGFuZHNoYWtlLmNvbSZ0b2dnbGU9Zmls) that uses a calculation on two unique institution labels. Please note that unless you have these particular labels at your institution, you probably won't see any results. We'll just use this as an example to work from!

On the example report, notice this **Calculations** section is highlighted:

![Screen_Shot_2018-03-27_at_10.28.23_AM.png](https://support.joinhandshake.com/hc/article_attachments/25997410659351)

Click the Calculations box, which will open a Table Calculations dialogue:

![Screen_Shot_2018-03-27_at_10.29.19_AM.png](https://support.joinhandshake.com/hc/article_attachments/25997430551447)

We filtered specifically for 2 particular labels - "fall 2017 graduate" and "work study eligible".  The way this calculation is setup, if a student has both of those labels, it will return a "yes" in this column on our report:

![Screen_Shot_2018-03-27_at_10.36.37_AM.png](https://support.joinhandshake.com/hc/article_attachments/25997430554391)

Here is an example of the syntax that we used:

if(contains(${added\_institution\_labels\_on\_students.name\_list},"fall 2017 graduate")AND(contains(${added\_institution\_labels\_on\_students.name\_list},"work study eligible")),yes,no)

You can use this as a template for any labels that you need 'AND' filtering for, and you can also build any other calculations you need! For more information on these table calculations, explore this [Looker documentation](https://docs.looker.com/exploring-data/creating-looker-expressions/looker-functions-and-operators).

If you wish, you can exclude any 'No' rows from the visualization, which will mean filtering the data within Excel post-download won't be required. To do so, click the gear icon from the calculation field, then click **Hide "No's" from Visualization**:

![image__46_.png](https://support.joinhandshake.com/hc/article_attachments/25997410665751)

We'd also love for you to share any tips in our [Handshake Community](https://support.joinhandshake.com/hc/en-us/community/topics). This is a place for you and your team to connect with other career centers to share best practices and learn from each other on how to make the most out of Handshake!