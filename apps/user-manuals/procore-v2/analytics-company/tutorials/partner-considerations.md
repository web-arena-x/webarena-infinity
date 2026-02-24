# Partner Considerations

Source: https://v2.support.procore.com/product-manuals/analytics-company/tutorials/partner-considerations

---

Please review the following partner considerations below:

### Consulting Partners

1. **Permissions**: When using Analytics 2.0, the token you generate will pull data from all companies that your Procore login has access to. **If you work with multiple customers, you need to create a separate Procore login for each customer to avoid inadvertently sharing data across customers. Do not use the same login (token)** **for different customers**.
2. **Support**: The partner must provide support related to their datasets and reports.

### App Partners

1. **Bulk access**: Whether you expose your data via API or a Power BI custom connector, youâll need a security model that returns data across all projects with each endpoint. Power BI is geared towards bulk data ingestion and will not be able to scale if it needs to iterate datasets by a project or other unique identifier.
2. **Multiple datasets**: It's common to expose separate datasets for each reportable data entity. Each of these should support the same security model and return data in bulk.
3. **Security**: Youâll need to implement a solution that enables bulk reading of the data with a single set of secure credentials.
4. **Power BI template**: Your Power BI template should work out of the box with any customer who uses it. The Power BI template is loaded into the clientâs Power BI tenant. They will configure the datasets with the credentials you provide them.