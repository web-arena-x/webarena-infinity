# Spread Cash Flow Forecasts in Portfolio Financials and Capital Planning

Source: https://v2.support.procore.com/product-manuals/portfolio-financials/tutorials/spread-cash-flow-forecasts-in-portfolio-financials-and-capital-planning

---

##### Â Legacy

This information is intended for accounts with the [Portfolio Financials](/product-manuals/portfolio-financials/) and [Capital Planning](/faq-what-is-capital-planning) products in Procore. Please reach out to your Procore point of contact for more information.

## Background

Cash Flow Forecasting is a feature exclusive to the Capital Planning product in Procore that allows you to reforecast budgets as project costs and timelines change over time. The 'Spread' feature for Cash Flow Forecasting provides you with the ability to automatically spread (or generate) cash flows, rather than having to input values manually for all periods. There are four different methods available to choose for the spread: *Straight Line*, *Bell Curve*, *Front Loaded*, and *Back Loaded*.

## Things to Consider

- **Required User Permissions**:

  - 'Full Access' to the project or higher.
- **Additional Information**:

  - This feature requires the **Capital Planning** product added on to your organization's account in Portfolio Financials. Please reach out to your Procore point of contact  with any questions.

## Prerequisites

- [Create a Cash Flow Forecast in Portfolio Financials and Capital Planning](/product-manuals/portfolio-financials/tutorials/create-and-publish-a-cash-flow-forecast-in-portfolio-financials)

## Steps

1. Navigate to the **Cost Tracker** section of the **Project Page**.
2. Click the **Cash Flow** tab.
3. Click **Edit Cash Flow**.
4. Click the **vertical ellipsis**  icon for a line item and select **Spread**.
5. Enter the following information in the 'Spread' window:

   - **Select Spreading Method**: Click the forecasting option you want to use:

     - **Straight Line**: An even spread of the Forecast to Complete Value over the selected timeline.
     - **Front-Weighted Curve**: More is spent at the beginning of the selected timeline, and less is spent near the end of the selected timeline.
     - **Back-Weighted Curve**: Less is spent at the beginning of the selected timeline, and more is spent near the end of the selected timeline.
     - **Bell Curve**: A balanced spread, where less is spent at the beginning and end of the selected timeline, but more is spent in the middle.
   - **Select Date Range**: Select a **Start Month** and **End Month**, or enter the number of months in the **Duration** field.
   - **Amount to Spread**: This section shows the spreadable amount, which is equal to the Budget minus (-) all past Actuals. The Forecast to Complete represents the costs that are expected to be incurred in the future, excluding any costs that have already been paid.
6. Click **Spread**.  
    The values will spread automatically.

   ##### Â Important

   You can manually adjust values as needed after the automatic spread by clicking into the cells. However, other values in the row will NOT be automatically adjusted.

- Click **Publish** to save this version of the Cash Flow and update the Capital Plan.
- Enter a name and explanation (optional) for the version.
- Click **Publish**.