# Activity Categories

Source: https://help.clio.com/hc/en-us/articles/9289744400667-Activity-Categories

---

Activities are billable and non-billable events that form a bill. They are split into time entries and expense entries. Expenses are further broken down into hard costs and soft costs. Additionally, firms using LEDES billing can [enable UTBMS codes](https://help.clio.com/hc/en-us/articles/9289762435099) for time and expense entries. LEDES is the Legal Electronic Data Exchange Standard. It’s more commonly used in practice areas that involve third party corporations or clearinghouses, like insurance companies to essentially ensure consistency across invoices.

Activity categories are the labeled groups or drop-down options to label time and expenses using a consistent description and rate across the firm. All firm users can create activity categories in Clio at any time. You can also set permissions for activity categories if you want to restrict which firm users can use certain categories.

**Note:** There is no limit to the number of activity categories that you can create; however, too many activity categories can impact performance.

## Create time entry and flat rate categories

Time entry categories are templates for events that a firm user spends time on and charges for. Some examples include court appearance, call with a client, case review, and document preparation. See [below](#h_01H08F2H0F6TVKR21F3DN5T3YB) for additional examples. When selecting the billing method for your time entry categories, you can choose your user default rate, a custom rate, or a flat rate. You can create a flat rate activity category to add a flat rate time entry to hourly matters. If you need to create a flat rate matter, learn more [here](https://help.clio.com/hc/en-us/articles/13719345938843-Contingency-Fee-and-Flat-Rate-Matters#create-and-manage-flat-rate-matters-0-1).

1. Go to **Activities** > **Manage categories**.
2. Click **New category**.
3. Under **Category type**, select **Time entry category**.
4. Name your activity category. You can use the name to easily identify the category in a list. The name will also show in a bill.
5. Choose the **Billing method** to associate with your new activity category. The following options are available.
   - **User default rate:** A time entry using this option will use the default rate and currency for the user. Learn how to edit or set the user rate and currency [here](https://help.clio.com/hc/en-150/articles/9285360193819-Permissions-and-Billing-Rates#h_01HC36VG3ZFC6EQAKYW8B8FE3P). If multiple rates are defined for a user in different currencies, the rate relevant to the currency of the matter will appear when they use this category to create time entries.
   - **Custom rate:** When choosing this option, also fill the **Currency** field and custom **Hourly rate** field.
   - **Flat rate:** When choosing this option, also fill the **Currency** field and **Rate field**.
6. Under **Permission groups**, search for permission groups and users specific to your firm. Only these groups and people will have access to this activity category. If you do not enter any group or name, all firm members will be able to use the activity category.
7. *Optional:* Check the box for **Visible to co-counsel** if you want [Clio for Co-Counsel](https://help.clio.com/hc/en-us/articles/9290191798683) users to be able to choose this category when entering their time entries.
8. Click **Save category**.

**Note:** You can create a “no charge” time entry category by setting the **Billing method** to **Flat rate** and setting the rate to 0.00.

## Create expense categories

Expense categories are templates for reimbursable expenses a firm has for a particular case. Some examples include court filing fees, medical records, photocopies, and postage costs. See [below](#h_01H08F2H0F6TVKR21F3DN5T3YB) for additional examples.

1. Go to **Activities** > **Manage categories**.
2. Click **New category**.
3. Under **Category type**, select **Expense category**.
   - If you select the UTBMS expense category, you can add an expense category for specific UTBMS codes. UTBMS stands for a uniform task-based management system, which is used to standardize categories across a firm to make for more efficient analysis and billing. Learn more about enabling and using UTBMS codes in activities [here](https://help.clio.com/hc/en-us/articles/9289762435099).
4. If enabled, under **Expense type**, select **Hard cost** or **Soft cost**.
   - Hard costs are expenses that you would pay for on behalf of your client, such as court filing fees. Soft costs are expenses that are not directly attributable to third party vendors, such as photocopy expenses. Learn more about enabling hard and soft cost expenses [here](https://help.clio.com/hc/en-us/articles/9289745356571).
5. Name your activity category. You can use the name to easily identify the category in a list. The name will also show in a bill.
6. Enter the rate for the expense category.
7. Under **Permission groups**, search for permission groups and users specific to your firm. Only these groups and users will have access to this activity category. If you do not enter any group or name, all firm users will be able to use the activity category.
8. Under **Tax rate**, choose how you want tax to be associated with this category The selected tax option will be applied to all expense entries created under this category. 
   - You can choose to not apply any tax or apply your primary tax, your secondary tax, or both your primary and secondary tax rates. Learn more about setting up tax rates [here](https://help.clio.com/hc/en-us/articles/9285437408667).
   - If you select **Use tax applied to invoice** or if you do not select any option, expenses created under this category will inherit the tax setting chosen when generating a bill.
9. Click **Save category**.

## Activity category examples

If you are unsure about the types of time and expense categories you want to create, see below for a list of some examples.

| Time entry categories | Expense categories |
| --- | --- |
| Call with client | Clerical services |
| Case research | Continuance fee |
| Case review | Court filing fees |
| Consultation | Court reporting fees |
| Conveyance | Delivery services/messengers |
| Correspondence to opposing counsel | Deposition expenses |
| Court appearance | Electronic data storage |
| Document preparation | Expert witness fees |
| Document review | Fax costs |
| Draft agreement | Hearing transcript fees |
| Draft contract | Interview costs |
| Draft correspondence | Laboratory fees |
| Draft pleading | Legal research costs |
| Email client | Meal with client |
| Flat fee for initial deposit | Medical record expenses |
| Meeting with client | Online/database research |
| Real estate transfer | Photocopying |
| Research | Postage |
| Trademark application | Process serving fees |
| Trial preparation | Travel |
| Will preparation | Witness fees |

## Set and remove default time entry category

You can choose which activity category is the default for yourself. This ensures that the most often used category is the first one that appears when you are adding a new time entry. The default activity category only applies to each user and does not affect the whole firm.

**Note:** If you select a flat rate category as your default time entry category, the category will override other billing rates. Learn more about the billing rate hierarchy in [this article](https://help.clio.com/hc/en-us/articles/9289801180187).

1. Go to **Activities** > **Manage categories**.
2. Under **Time entry categories**, find your time entry category.
3. Click the down arrow next to **Edit** and select **Set as my default**. A green **My default** tag will show which category is your default.
4. You can remove your default category by clicking the down arrow next to **Edit** and selecting **Remove as my default**.

## Edit activity categories

When you edit an activity category, you can change the name, billing method and rate, and the permission groups and users that the category is visible to. Bills already generated will not be affected by any of these changes.

**Important:** Unbilled activities will be affected if the category’s name is changed. The billing method, rate, and permission groups will remain unchanged for unbilled activities.

1. Go to **Activities** > **Manage categories**.
2. Find your category and select **Edit**.
3. After making changes, click **Save category**.

## Delete activity categories

When you delete an activity category, existing unbilled and billed activities will not be affected.

**Note:** You can only delete time entry categories and unused expense categories. Expense categories that have previously been used cannot be deleted.

1. Go to **Activities** > **Manage categories**.
2. Click the down arrow next to **Edit** and select **Delete**.
3. When the warning prompt appears, select **Delete activity category**.