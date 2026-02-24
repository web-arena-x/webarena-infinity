# Chart types for displaying workflow

Source: https://support.zendesk.com/hc/en-us/articles/4408834701210-Chart-types-for-displaying-workflow

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support with** | Explore Professional or Enterprise |

When looking at your company's results, there are chart types available to best display the workflow of your organization. These chart types focus on demonstrating how results progress rather than comparing results.

The following are the workflow chart types available:

- [Funnel](#topic_idr_prf_z5)
- [Relational](#topic_w4p_prf_z5)
- [Parallel sets](#topic_axv_4rf_z5)
- [Word cloud](#topic_gl5_4rf_z5)

## Funnel

Similar to a pie chart, a funnel chart can be constructed in two ways:

- A metric broken down by a categories (attributes).
- Multiple metrics making up a natural whole combined metric.

Unlike a pie chart, a funnel chart organizes data based on your sorting filters. If you have applied sorting filters, the funnel chart provides a good way to organize your results.
For example, the funnel chart below displays the progression of solved tickets in each quarter. The report uses the Value Descending sorting filter (see [Sorting results](https://support.zendesk.com/hc/en-us/articles/4408839379482)) .

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Exlpore_funnel_attribute.png)

If you want to view how multiple metrics make up a natural whole, add the relevant metrics in the order you would like them to appear in your workflow. Below is a report comparing different ticket metrics to show how total number of tickets is produced.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_funnel_metric.png)

When you select a funnel chart, you can change the following customization options in the Chart configuration menu:

- In **Chart**, you can change the shape of your funnel by either measuring the percentage of area or height. You can select a new shape from the **Funnel type** drop-down list.
- You can also select the type of percentage results show, by either calculating the percentage of the total or the percentage of the first element in the metric or attribute. You can edit this result in **Chart** > **Computation method**.
- In **Colors**, you can change the color for each segment.

## Relational

The relational chart is less about showing numeric results and more about showing the structure of your organization. In the image below the relational chart displays the connections between group and assignee.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_relational.png)

You can create a relational chart by adding attributes to Columns and a normal metric. The metric will only be displayed as a datatip. You can add datatips in **Chart configuration** > **Datatips**, then select your metric under **Select an element to add**.

You can also add color or size encoded metrics. If you add a size or color encoded metric, and do not have datatips added, you will be able to see the results by hovering over points.
In the image below, Full Resolution Time In Minutes is a color encoded metric. For more information on adding color encoded metrics, see [Adding color and size encoded metrics](https://support.zendesk.com/hc/en-us/articles/4408846733722/#topic_esg_kmb_y5).

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_relational_color.png)

When you select a relational chart, you can change the following customization options in the Chart configuration menu:

- In **Chart**, you can edit the layout strategy. There are two types of layout strategies: radial and cartesian. Radial is the default layout, shown above. A cartesian layout can display results from left-to-right or top-to-bottom. In the image below, Year and Quarter are displayed in a cartesian layout.

 ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/workflow_5.png)
- In **Chart**, you can also edit the Link Display (the lines connecting your nodes), your node shape, and your node size. If you are using an encoded metric, you can check the **Encode the intermediate nodes** to view inside nodes in the encoded color or size.
- In **Colors**, you can edit the link, circle, and legend colors.

## Parallel sets

Parallel set charts work best when you are segmenting a metric by several attributes and would like to see the results for every value combination. You must add at least two attributes to create a parallel set.

Parallel sets can be used to show the flow of results among attributes. The report below progresses from Ticket Group to Year to Quarter. The colored lines represent the connections between the attribute values.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_parallel_set.png)

When you hover over a line you will see the measure's results divided by the combination of values. In the image below, the metric is divided by Support and the Year 2014.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_parallel_set_tip.png)

In a parallel set, the attributes are referred to as *dimensions*. The attribute's values are referred to as *categories*. If you hover over a dimension or category title, the related results are highlighted and appear as a datatip.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_parallel_category.png)

When you select parallel set, you can edit the following customization options in the Chart configuration menu:

- In **Chart**, you can edit the dimension and category text style. You can also select **Curve** to show your lines as curved. A parallel set with curved lines will look like the image below:

 ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_parallel_curve.png)
- In **Colors**, you can select a custom line color or choose from one of Explore's predefined color palettes.

## Word cloud

Word clouds are primarily used to see text results relating to tags, groups, agent names, etc.

Your word cloud is based on the attribute added to Columns. The attribute chosen will return the type of text displayed. For example the report below uses the attribute Submitter name, so all of the results returned will be the different submitter names related to the metric.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/workflow_10.png)

The individuals with the more results will appear larger than individuals with less results. You can hover over a word to view the exact number of results.

When you select word cloud, the following customization options are available in the Chart configuration menu:

- In **Chart**, you can edit the orientation of your results. Your words can be oriented in a series of different ways, depending on the number you enter into the **Number of orientations** text box. Alternatively, you can edit the orientation degree values.

 Below, is the same word cloud but with five orientations instead of the default two.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/workflow_11.png)

- In **Chart** you can change the cloud shape. By default your cloud will be shaped in an oval, but you can shape your cloud as rectangle instead.
- You can also edit the scale type, the size, and the padding between words in **Chart**.