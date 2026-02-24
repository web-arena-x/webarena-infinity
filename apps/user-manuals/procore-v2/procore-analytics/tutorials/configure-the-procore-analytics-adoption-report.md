# Configure the Procore Analytics Adoption Report

Source: https://v2.support.procore.com/product-manuals/procore-analytics/tutorials/configure-the-procore-analytics-adoption-report

---

## Things to Consider

- **Required User Permissions**:

  - Must be a Power BI Workspace Admin

## Steps

The Configuration report page for the Procore Analytics Adoption report has several configuration options. To access your configuration options, complete the steps below:

1. Navigate to your Procore Analytics Adoption report.
2. Click the **Configuration** tab or the **settings**  icon.
3. Choose which settings you would like to configure:

- Tools to report usage on
- Email Domains
- Collaborator Record Creation Target Percentage

### Tools to report usage on

This enables a user to determine which tools to include in their analysis.

1. Select or deselect options to include in your analysis.

### Email Domains

To determine which records are created by your company's employees, you will need to configure the email domains' **Power BI** report parameter. This is a semi-colon delimited list of domain names in the format of *@yourcompany.com*. Any records created by users other than this defined list will be considered collaborators.

1. Navigate to **Power BI Service**.
2. Go to **Settings for the Procore Adoption** dataset.
3. Expand the **Parameters** section.
4. Replace the default email with your company's domain name(s).
5. Click **Apply**.  
   *Note*: After your next scheduled refresh of the report, this setting will take effect.

### Collaborator Record Creation Target Percentage

This is the percentage of overall records that you expect your collaborators or partners to generate. The Collaborator Analysis page leverages this metric.

1. Navigate to the **Power BI Service**.
2. Go to **Settings** **for the Procore Adoption** dataset.
3. Expand the **Parameters** section.
4. Go to the **Collaborator Record Creation Target %** area.
5. Replace '0.3' with your desired value.  
   *Note*: Percents should be represented with a decimal.
6. Click **Apply**.  
    After your next scheduled refresh of the report, this setting will take effect.