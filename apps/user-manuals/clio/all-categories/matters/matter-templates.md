# Matter Templates

Source: https://help.clio.com/hc/en-us/articles/18353050138651-Matter-Templates

---

In Clio Manage, you can streamline your matter creation process using matter templates. Matter templates contain preset information that will automatically populate when you create a new matter or edit an existing matter. This allows you to spend less time entering common data into matters and helps with consistency across newly created matters.

You can configure the following sections of a matter template:

- **Matter details** (template matter description, responsible attorney, originating attorney, responsible staff, location, practice area permissions, and matter status)
- **Custom fields** (see [Create custom fields in Clio Manage](https://help.clio.com/hc/en-us/articles/9285496802331-Create-Custom-Fields))
- **Billing preference** (billable or non-billable, billing method)
- **Personal injury preferences** (order of settlement deductions)
- **Document folder structures** (folder name and category)
- **Task lists** (see [task lists](../tasks/task-lists.md))

**Note:** Matter templates are not available on all subscription plans. To upgrade your firm's plan, see which plans have matter templates [here](https://www.clio.com/pricing/). An administrator can follow the directions [here](https://app.clio.com/nc/#/subscriptions).

## Create matter templates

The Primary subscriber and Administrators can create new matter templates. The firm's account can have up to 200 matter templates. Once created, any firm user can select a matter template when creating a new matter to speed up their matter-creation workflow.

**Tip:** Learn more about each section in the matter form [here](https://help.clio.com/hc/en-us/articles/9285959663131#h_01GEK791XBF1JJ0VYC8BQTG9MW).

1. Go to **Matters** and select **Matter Templates**.
2. Click **New matter template**.
3. In the **Template information** section, name your matter template.
   - *Optional:* If you want this template to automatically be applied when creating all new matters, turn the **Use as matter default template** toggle to the on position. You can only have one default matter template across your firm account. You can always change the default template by editing a matter template.
4. Under the remaining matter form sections, enter the information that you want to preset in the empty fields.
   - When a firm user creates a new matter, these fields will pre-populate in the matter form. The fields are not locked in and can be changed when creating a matter.
   - Learn more about each section of the matter form [here](https://help.clio.com/hc/en-us/articles/9285959663131#h_01GEK791XBF1JJ0VYC8BQTG9MW).
5. Click **Save template**.

## Edit matter templates

The Primary subscriber and Administrators can edit existing matter templates. Changes made to an existing template will not affect any matters that were previously created using the template.

1. Go to **Matters** and select **Matter Templates**.
2. Find the template that you want to edit.
3. Under the **Actions** column, click the pencil icon. Alternatively, you can click on the template name in the **Template** column.
4. Make any necessary changes. You can also change your firm's default template by turning the **Use as matter default template** toggle to the on position.
5. Click **Save template**.

## Set default matter template

The Primary subscriber and Administrators can set a default matter template. Your firm account can only have one default matter template. Once set, this template will automatically be applied to all new matters that firm users create. When you create a new matter template and set it as the default template, it will automatically replace any other matter template set as the default template. You can also manually set a new default template from your list of existing matter templates.

1. Go to **Matters** and select **Matter Templates**.
2. Find the template that you want to be your firm's new default template.
3. Under the **Actions** column, click the pencil icon.
4. Under the **Template information** section, turn the **Use as matter default template** toggle to the on position.
5. Click **Save template**.

## Remove default matter template

The Primary subscriber and Administrators can remove default matter template.

**Note:** You do not need to remove a default matter in order to set a new default. [Setting a new default](#h_01H91GYDA1YCQHVGE9T2QKM71R) will replace the existing default.

If you previously set a default matter template and want to remove it:

1. Go to **Matters** and select **Matter Templates**.
2. Find the default template (marked with a **Default** tag), then under the **Actions** column, click the more actions icon (three horizontal dots).
3. Select **Remove as default**.

## Delete matter templates

The Primary subscriber and Administrators can delete existing matter templates. Once a matter template is deleted, it will no longer be available for use by any firm user and the template cannot be restored.

**Note:** If you use [automated workflows](https://help.clio.com/hc/articles/35132279298843-Clio-Manage-Automated-Workflows), make sure that the matter template you want to delete is not used by one of your workflows.

1. Go to **Matters** and select **Matter Templates**.
2. Find the template that you want to delete.
3. Under the **Actions** column, click the more actions icon (three horizontal dots).
4. Select **Delete**.
5. When prompted to confirm the action, click **Delete**.

## Use matter templates

Use matter templates to quickly create new matters with great consistency or to edit existing matters.

Create new matter from template Apply template to existing matter

In Clio Manage, you can create a matter from the main **Matters** tab, the main **Contacts** tab, or by using the **Create new** button from the header. [Create matters in Clio Manage](n%20create%20a%20matter%20frhttps://help.clio.com/hc/en-us/articles/9285959663131-Create-Matters#h_01GZM1JHCP2M0CCVQT3P5JXGDR) provides instructions for each of these options. For each of these options, when you arrive to the [New matter](https://app.clio.com/nc/#/matters/new) page:

1. Under the **Template information** section, select **Use an existing template** from the dropdown.
2. Select the template to populate the fields from the template.
3. Fill in any additional information and click **Save matter**.

In some cases it may be useful to retroactively apply a matter template to an existing matter. For example, once you [converted a matter from Clio Grow to Manage](filter-export-and-convert-matters.md#h_01HE14ZHP2770AWH19EYXPT6ST), you can apply a matter template to the existing matter to quickly and consistently add information to the matter fields.

1. In Clio Manage, click **Edit** next to the matter name.
2. Under the **Template information** section, select **Use an existing template** from the dropdown.
3. Select the template.
   - Fields from the template will populate any unfilled fields in the existing matter. These fields will be highlighted to enable the user to easily review the added information. Matter fields that were previously filled will remain unchanged.
4. Fill in any additional information and click **Save matter**.