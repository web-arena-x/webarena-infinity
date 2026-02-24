# Using SQL to filter reports

Source: https://support.zendesk.com/hc/en-us/articles/6467453826202-Using-SQL-to-filter-reports

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support with** | Explore Professional or Enterprise |

Note: This information is intended only for users who are
comfortable working with SQL (Structured Query Language). Other users should use the
Explore report builder UI to [filter](https://support.zendesk.com/hc/en-us/articles/4408825475354) reports instead.

For advanced reporting users, Explore offers a SQL-based way to filter reports without
using the typical Metrics, Columns, Rows, and Filters panels of the report builder.

Specifically, the SQL options panel gives you fine-grained control over the ORDER BY and
LIMIT clauses of the generated SQL query.

**To use SQL to filter a report**

1. In Explore, [create a new report](https://support.zendesk.com/hc/en-us/articles/4408821589530) or [open an existing one](https://support.zendesk.com/hc/en-us/articles/4408823403546).
2. In the **Result manipulation** (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_result_manipulation.png)) menu, select **SQL options**.
3. Construct the SQL query using the following fields as needed:
   - **‘Order by’ clause**: Specify how results should be sorted.
   - **‘Limit’ clause**: Specify how many results to return.
4. (Optional) In the **Replace NULL by** field, select **NULL** to replace blanks
   in your report with the word “NULL” to improve readability.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/explore_sql_options_menu.png)
5. Click **Apply**. Your report results appear in the report builder.

Note: During [account assumption](https://support.zendesk.com/hc/en-us/articles/4408824477082) only, the SQL options menu includes
additional information about the SQL query that helps Zendesk Customer Support
troubleshoot issues.