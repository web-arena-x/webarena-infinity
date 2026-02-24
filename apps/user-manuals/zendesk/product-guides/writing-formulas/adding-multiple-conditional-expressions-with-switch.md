# Adding multiple conditional expressions with SWITCH

Source: https://support.zendesk.com/hc/en-us/articles/4408831957658-Adding-multiple-conditional-expressions-with-SWITCH

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support with** | Explore Professional or Enterprise |

Use the SWITCH function in your formulas to create several different conditional expressions as an alternative to nesting IF THEN ELSE functions. This article describes the function and provides examples. For a list of all Explore functions, see [Explore functions reference](explore-functions-reference.md).

This article contains the following topics:

- [About the SWITCH function](#topic_oth_xk2_fhb)
- [Using the SWITCH function](#topic_kxb_yk2_fhb)

## About the SWITCH function

The SWITCH function uses the following format:

```
SWITCH testedElement { 
CASE value1: returnValue 
CASE value2: returnValue 
DEFAULT: defaultReturnValue }
```

SWITCH tests if the case values exist within the tested element. Your tested element can be a metric, attribute, or calculation. If your case value exists within the tested element, then the return value is displayed. If it does not, your default value is displayed. If your case value does not exist in the tested element and there is no entered default value, "NULL" is returned.

SWITCH is often used to insert metrics such as targets and goals into datasets. They can then be used in other calculations or in comparison visuals such as KPI, bullet, and gauge charts.

## Using the SWITCH function

This example uses the SWITCH function to show first reply time targets for each ticket type. You can duplicate this example using any attribute and target number.

**To insert numbers into your data**

1. Open a new report using the **Support: Tickets** dataset.
2. In the calculations menu (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_calculations.png)), click **Standard calculated metric**.
3. Name your calculated metric. This example uses **Target FTR**.
4. Under **Functions**, click **Add**.
5. Select the **SWITCH** function and click **+**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_switch_function.png)
6. Double-click **\_tested\_element** to highlight it.
7. Select the attribute containing the values you want to test from the **Fields** drop-down list or type in the attribute name. This example uses the **Ticket type** attribute.
8. In **CASE \_value1**, enter the value you're testing for.
9. In **\_return\_value**, enter the result returned if the value is true. This example uses the value of the **Ticket type** attribute to test and the first reply time targets as the returned result.
10. Enter your other cases. If you have more than two cases, you will need to manually type out additional CASE expressions. The formula for this example looks like the image below.

    ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_switch_formula.png)
11. Click **Save**.
12. Click the **+** button on metrics to add your calculated metric to your report.
13. If your tested element is an attribute, click the **+** button on any attribute location and select your tested element.