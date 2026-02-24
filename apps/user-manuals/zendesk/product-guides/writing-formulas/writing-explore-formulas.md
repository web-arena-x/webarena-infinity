# Writing Explore formulas

Source: https://support.zendesk.com/hc/en-us/articles/4408836190362-Writing-Explore-formulas

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support with** | Explore Professional or Enterprise |

You can create custom metrics and attributes to use in your report that help you present your
business data just how you want it. To do this, you'll need to learn how to write formulas.
Formulas perform comparisons, calculations, and manipulations on your data, and help you
evaluate conditions.

This article contains the following sections:

- [Understanding Explore formulas](#topic_xlg_dpx_wtb)
- [Creating a formula](#topic_qxz_mrn_dhb)
- [Adding metrics and attributes to your formula](#topic_l1j_fxn_dhb)
- [Adding functions to your formula](#topic_a5p_pcd_dx)
- [Adding comments to your formula](#topic_jtq_zh4_vyb)

For more information about formulas, see [Formula writing resources](https://support.zendesk.com/hc/en-us/articles/4408845804314).

## Understanding Explore formulas

Formulas are generally constructed with two pieces:

- **Metrics and attributes** that contain your Zendesk information
- **Functions** that perform operations on those metrics and attributes

Formulas in Explore are read from left to right, and follow the mathematical order of
operations. A formula can contain multiple statements, each containing a combination of
metrics, attributes, and functions that are used to define the data you're looking for.

Within a formula, functions, such as IF/THEN, are often contained within parentheses
`()`, much like algebra, so that they don't affect the rest of the formula.
If a formula has only one function, parentheses might not be necessary.

Metric and attribute names are contained within brackets `[]`. Metric and
attribute values, expressed as text strings, are contained in quotation marks, and must
match the values exactly. For example, "End-user" and "end user" are two different values.
(For more on attribute values in formulas, see [How do I find an attribute value?](https://support.zendesk.com/hc/en-us/articles/4615913739418)) Operators are used to connect
attribute names and values, or to perform additional calculations.

Putting this all together, a simple formula might read as follows:

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/explore_formula_annotated.png)

Tip: Now that you understand the basics of a formula, you
can dig into more advanced information about data types within formulas (see [Working with data types in Explore formulas](https://support.zendesk.com/hc/en-us/articles/5784398875802)), or continue
reading below to learn how to create a formula in Explore.

## Creating a formula

Now that you know that an Explore formula is made up of metrics, attributes, and functions,
you'll learn how to create the example formula above.

It can be helpful to write down the logic of a formula to help you create it and find the
right functions you need. In this case, the formula flow is "If the ticket channel is email,
show me the ticket ID." You'll see later that this is very similar to the formula you'll end
up with.

**To create a formula that displays tickets from the email channel**

1. In Explore, [create a new report](https://support.zendesk.com/hc/en-us/articles/4408821589530) or [open an existing report for editing](https://support.zendesk.com/hc/en-us/articles/4408823403546).
2. Open the calculations menu (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_calculations.png)).

   Important: If two editors are creating or editing
   different reports in the same dataset, only the first person who opened a report can
   access the Calculations menu. The other editor will see the message “This resource is
   locked because it is currently being edited by <name>”. Once the first person
   closes the report, the Calculations menu will become available to the next
   editor.
3. Click **Standard calculated attribute**. A new blank attribute opens.
4. Enter a name for the attribute like **Tickets received by email**.
5. In the formula window, start entering your formula. There are a number of ways you can
   do this, but for now, under functions, click **Add**.
6. Search for **IF THEN ELSE Conditional expression**. Either use the search box, click
   **Filter** to scope the values down to the **Logical** category, or scroll through
   the list until you find the function you want.
7. Next to **IF THEN ELSE Conditional expression**, click **+**.

   Explore adds a
   template IF THEN ELSE formula to the window. The values in the formula shown in blue
   (beginning with an \_ character) are placeholders that you must replace with the values
   you need.

   ![Explore template formula](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_formula_1.png)

   Tip: Notice the error message prefixed with (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/formula_error_icon.png)) above the formula. This indicates a problem and its location
   in the formula. For now, you can ignore the error. It's appearing because your formula
   is still using placeholders.
8. Next, you'll replace **\_boolean\_condition** with the Explore attribute you want to
   test. Either highlight **\_boolean\_condition** and then choose **Ticket channel**
   from the **Fields** menu, or amend the formula manually to add the attribute.
9. Now, add the rest of the condition. To search for the string "Email", we add that to the
   existing condition.

   Your formula should now read **IF ([Ticket channel]="Email") THEN
   \_value\_if\_true ELSE \_value\_if\_false ENDIF**
10. Next, add what you want to do if the condition is true, in this case return the ID of
    the ticket. Replace **\_value\_if\_true** with **[Ticket ID]**. Notice that as you type
    **[Ticket ID]** that Explore automatically suggests matches to what you are typing.
    If the metric or attribute you want is shown, hit return to immediately complete entry of
    it.
11. The ELSE clause shown in the template ticket can be used to provide an alternative
    action that will apply if the first condition is not true. In this case, we don't need it,
    so remove **ELSE \_value\_if\_false**.
12. You've now completed the formula. If all is well, you'll see something like the screen
    below. Additionally. note that the error has gone and is replaced with a green check mark
    to indicate that the formula is valid.

    ![Explore formula example](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_formula_2.png)
13. Finally, click **Save**. The attribute you created can now be accessed by any of your
    Explore reports that use the same dataset. You can find it by clicking **Add** in any
    attribute panel and expanding **Calculated attributes**.

## Adding metrics and attributes to your formula

It's likely that most of the formulas you write with Explore will use metrics or attributes
from the dataset you are currently using. In the example above you used the attribute
**Ticket channel**, but there are many hundreds more you can choose from.

While it can feel intimidating at first, most of these metrics and attributes have
descriptive names that will help you to find what you need. Also, experiment with creating
basic reports in Explore to learn more about what the various metrics and attributes do.

You can find a full list of all the metrics and attributes you can use in the [Understanding Explore datasets](https://support.zendesk.com/hc/en-us/articles/4408839218842-Zendesk-Explore-metric-and-attribute-reference).

**To add a metric or attribute to your formula**

1. In the Explore formula window, click **Select a field**.
2. Either scroll through the list, or type the first few letters of the metric or attribute
   you want, to filter the list.

   ![Explore choose a field list](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_formula_3.png)
3. Click the metric or attribute you want and it is added to the formula. In this case,
   Ticket ID was chosen. Note how it is surrounded with brackets [].

   ![Ticket ID sample formula](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_formula_4.png)

   The brackets indicate to Explore that this is a metric or attribute. An
   alternative method to enter a metric or attribute is to simply begin typing. Explore
   recognizes the brackets, and suggests the appropriate values to choose
   from.

   ![Explore field auto-suggest](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_formula_5.png)

If you want to add an aggregator to your metric or attribute, enter the text in capitals
before the first bracket, for example **COUNT[Ticket ID]**.

## Adding functions to your formula

To add functions to your formula, click **Add** under **Functions** or type in a
function name. As with metrics and attributes, Explore suggests auto-complete results for
any functions you type in.

When you click **Add**, the **Functions** window opens. This window is useful if you
are not sure which function is applicable to the calculated element you want to create. All
functions in the window contain a brief explanation of their purpose. For a list of all
functions and many examples, see [Explore functions reference](https://support.zendesk.com/hc/en-us/articles/4408834558746-Using-dates-in-functions).

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/navigating_calculation31.png)

If you are looking for a specific function, you can search for functions or filter by
function type.

**To filter functions**

1. In the **Functions** window, click **Filter**.
2. Type in a category or select a category from the drop-down list.

   ![Explore function categories](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_formula_6.png)
3. Click the **x** next to the category name to remove the filter.

## Adding comments to your formula

You can add comments to your formulas to explain how it works. This is helpful if you want
to collaborate on formulas with other users, or if you want to make notes for yourself on
why you built the formula the way you did.

**To add a comment in a formula**

1. Find the place in a formula where you want to insert a comment.
2. Type a forward slash and an asterisk (/\*), type your comment, and then type an asterisk
   and a forward slash (\*/).

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/explore_formula_with_comment.png)

   Warning: Clicking **Format** removes all comments.
   If you click **Format** and want to restore your comments, click anywhere outside
   the panel to close it without saving your changes.