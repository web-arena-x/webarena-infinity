# Procore Analytics Embedded

Source: https://v2.support.procore.com/product-manuals/procore-analytics-embedded/faq-or-troubleshooting

---

Table of Contents

## FAQ/Troubleshooting

### What are the main differences between viewing Procore Analytics reports in the embedded app and viewing the reports in the Power BI service?

One main difference in using the Procore Analytics Embedded app is that reports are connected to projects individually and are not grouped together in a portfolio location. Another difference is that editing capabilities from the Power BI service are not supported in the Procore Analytics Embedded app.

### Who can view reports using the Procore Analytics Embedded app?

If one or more Procore Analytics Embedded reports have been added to a project, all users added to that project's Directory can view a list of the reports in the 'Select an App' menu. Users need to log in to the Power BI service within the Procore web application using their Power BI login credentials and need to have the appropriate workspace access within the Power BI service to access the project's reports.

### Can I view a report for multiple projects at the same time using the Procore Analytics Embedded app?

Yes. Follow these steps to add data from one or more projects to a report:

1. [Launch a Procore Analytics Embedded Report from a Project](/product-manuals/procore-analytics-embedded/tutorials)
2. Click the Filters tab and scroll to the 'id' filter.
3. Select one or more project IDs to add more projects to your current report's view. A project's ID is its unique identifier in Procore. See [How do I find the project ID?](/faq-how-do-i-find-the-project-id)

*Note*: This filter resets each time you open the report, meaning the report will always default to only show data from the project you selected it from in Procore.

### Can I embed dashboards from the Power BI service in a Procore project?

No, dashboards cannot be embedded.

### How does Row-level Security from the Power BI service work in the Procore Analytics Embedded app?

Any RLS rules configured for users in the Power BI service will carry over when they access a report in the Procore Analytics Embedded app.