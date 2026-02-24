# Explore product limits

Source: https://support.zendesk.com/hc/en-us/articles/5133326635162-Explore-product-limits

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support with** | Explore Light, Professional, or Enterprise |

This article details the product limits that are in place for Explore. As more product limits are added to Explore, this article will continue to be updated. To ensure that you’re kept up to date on all changes, click Follow at the top of this article.

This article covers the following topics:

- [Limits for reports](#topic_sh5_ljz_nvb)
- [Limits for dashboards](#topic_nj4_rjz_nvb)

## Limits for reports

The following tables show the maximum strict and recommended limits for Explore reports.

### Strict limits

Strict limits are programmatically enforced by Explore and cannot be overridden by the user.

| | |
| --- | --- |
| **Item** | **Maximum** |
| Loading timeout | 2 minutes The more complex a report is, the longer it takes to load. If a report cannot be loaded within 2 minutes, its execution is canceled. |
| Rows | 50,000 If a report has more than 50,000 rows, results are truncated at the first 50,000 rows. Rows that are processed as part of a [formula](https://support.zendesk.com/hc/en-us/articles/4408845804314) also count toward this limit. As a result, reports with complex formulas might encounter this limit even if the final report has fewer than 50,000 rows. When you export report data, the export is restricted to a maximum of 50,000 rows. However, the overall size of the report data can also affect the export process. If an export fails despite remaining within the limit of 50,000 rows, consider reducing the number of attributes or applying additional filters to decrease the total row count. |
| Explosions | 30 |
| Attributes within each drill in level | 20 |
| SQL query length (Calculation complexity) | 1 million characters If your report’s calculations are too complex, the following message appears: “Calculations are too complex. Simplify calculated metrics and attributes or remove some of them.” This limit is reached when the underlying SQL query generated for the report has more than 1 million characters. |
| Nested calculations | 3 levels |

### Recommended limits

Zendesk cannot guarantee reports will be successfully executed if they are in breach of the following recommended limits.

| | |
| --- | --- |
| **Item** | **Maximum** |
| Columns | Visualizations have different column limits:   - 100: Pie, Funnel, Bullet, Gauge, Picto,   Radar, Parallel sets - 500: Table, Word cloud - 1,000: Auto, Treemap, Relational,   Sunburst, Sparkline, Dot - 3,000: Area, Column, Line, KPI, Bubble,   Waterfall |
| Metrics and attributes | 40 This is the maximum number of combined metrics and attributes that can be added to a report. For example, a report can have 10 metrics and 30 attributes. |
| Filters | 10 |
| Nested calculated attributes | Nesting calculated attributes inside of other calculated attributes or metrics is not recommended. Doing so exponentially increases the complexity of the report, resulting in potentially poor performance. |
| Conditions per formula or calculation | 200 This is the maximum recommended number of conditions that can be added to formulas or used in UI-based calculations (like [groups and sets](https://support.zendesk.com/hc/en-us/articles/4408836227866)). |

## Limits for dashboards

The following table shows the maximum strict and recommended limits for Explore dashboards.

### Strict limits

Strict limits are programmatically enforced by Explore and cannot be overridden by the user.

| | |
| --- | --- |
| **Item** | **Maximum** |
| Live dashboards open per account | 100 See [Live data limits for Explore dashboards](https://support.zendesk.com/hc/en-us/articles/4408846310810). |
| Applied filters on a live dashboard | 5 attribute values per filter |
| Scheduled deliveries email attachments | 20 MB |
| Scheduled deliveries timeout | 20 minutes |
| Dashboard restrictions | - 10 for Professional plans - 500 for Enterprise plans   See [Dynamically adapting dashboard data based on viewer](https://support.zendesk.com/hc/en-us/articles/5282695803290). |

### Recommended limits

Zendesk cannot guarantee dashboards will load successfully if they are in breach of the following recommended limits.

| | |
| --- | --- |
| **Item** | **Maximum** |
| Tabs per dashboard | 10 |
| Reports per tab | 35 |