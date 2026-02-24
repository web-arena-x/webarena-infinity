# Working with datatips

Source: https://support.zendesk.com/hc/en-us/articles/4408838176538-Working-with-datatips

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support with** | Explore Professional or Enterprise |

After you create a report, *datatips* (sometime called *tooltips*) appear when you hover over a data point in the results. In this example, you can see a datatip showing the number of tickets for the Voice ticket channel.

![Explore datatips example](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_datatips_1.png)

By default, datatips contain the value of the data point you hover over. In this article, you'll learn how to customize datatips and *comparison lines* which highlight your results by comparing metrics or by displaying the difference between a data point and the highest value in the chart.

Tip: If you want to use datatips with tables, add a [color gradient](https://support.zendesk.com/hc/en-us/articles/4408846733722-Adding-metrics-and-attributes-to-queries#topic_esg_kmb_y5) to one or more of your metrics.

This article contains the following topics:

- [Customizing datatips](#topic_ibf_gl4_dkb)
- [Changing the text in your datatips](#topic_d3v_tm4_dkb)

## Customizing datatips

While datatips are generated automatically with your report, there are a number of settings you can configure to change their look and feel.

**To customize your datatips**

1. With a report open, click chart configuration (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_chart_configuration.png)).
2. From the **Chart configuration** menu, choose **Datatips**.
3. On the **Datatips** panel, configure the following values as required:
   - **Show datatip:** Turns the display of the datatips on or off.
   - **Mode:** Choose between **Datatips** or **Comparison line**. Comparison lines highlight your results as shown below.

     For area, dot, and line charts:

     ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_line_datatip.png)

     For tables, column, and bar charts:

     ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_datatips_column.png)
   - **Line color:** If you selected **Comparison line**, this changes the color of the dotted comparison line.
   - **Background color:** Changes the background color of the datatip box.

For details of how to change the text displayed by a datatip, see the [next section](#topic_d3v_tm4_dkb).

## Changing the text in your datatips

As well as changing the color and style of your datatips, you can also change the text that is displayed in it.

**To change the text in your datatip**

1. With a report open, click chart configuration (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_chart_configuration.png)).
2. From the **Chart configuration** menu, choose **Datatips**.
3. On the **Datatips** panel, in the text box, type the text you want to display. You can highlight text and choose from formatting controls for text size, bold, italics, underline, justification, and color.
4. Typically, you'll want to include data from your report results in the datatip. To do this, position the cursor where you want the report result. Then, click **Select an element to add**.
5. Choose from the list of metrics and attributes you used in your report. The value is inserted into your datatip text.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_datatips_add_element.png)

   Note: If you want to add a metric to your datatip, but didn't use it in your report, you can add the metric as a datatip (see [Adding metrics as datatips](https://support.zendesk.com/hc/en-us/articles/4408846733722#topic_wd2_kmb_y5)).
6. When you are finished, click the chart configuration (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_chart_configuration.png)) to close the **Datatips** panel.

**Example**

You want to change the original datatip used in this article to read "You got 322,559 tickets in your Voice channel."

![Explore datatips example](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_datatips_1.png)

To do this, enter this text into the datatip text box:

![Explore datatips example](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_datatips_2.png)

This will give the following results when you hover over a data point:

![Explore datatips example](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_datatips_3.png)