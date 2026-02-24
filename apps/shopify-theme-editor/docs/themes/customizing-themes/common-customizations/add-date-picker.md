# Add a delivery date picker to your cart

Source: https://help.shopify.com/en/manual/online-store/themes/customizing-themes/common-customizations/add-date-picker

---

# Add a delivery date picker to your cart

You can include a calendar on your cart page that allows customers to specify a delivery date for their order.

## On this page

* [Include jQuery in your theme.liquid](add-date-picker.md#include-jquery-in-your-theme-liquid)
* [Create a delivery date snippet](add-date-picker.md#create-a-delivery-date-snippet)
* [Include the snippet in your cart page](add-date-picker.md#include-the-snippet-in-your-cart-page)

## Include jQuery in your theme.liquid

For this customization to work, some themes require that a script tag for jQuery is added to the theme.liquid layout file. If you use a free Shopify theme, then you might need to follow the next step:

1. In the **Layout** directory, click `theme.liquid`.
2. [Find](https://help.shopify.com/en/manual/shopify-admin/productivity-tools/keyboard-shortcuts#find) the closing `</head>` tag in the code. On a new line above the closing `</head>` tag, paste the following code:

```
{{ '//ajax.googleapis.com/ajax/libs/jquery/2.2.3/jquery.min.js' | script_tag }}
```

3. Click **Save**.

## Create a delivery date snippet

To create a snippet for your delivery date picker:

Desktop

1. From your Shopify admin, go to **Online Store** > [**Themes**](https://admin.shopify.com/themes).
2. Find the theme you want to edit, click the **…** button to open the actions menu, and then click **Edit code**.
3. In the **Snippets** directory, click **Add a new snippet**:
4. Create the snippet:
5. Name your snippet `delivery-date`.
6. Click **Create snippet**. The new snippet file will open in the code editor.
7. In your new `delivery-date.liquid` snippet, paste the following code:

```
{{ '//code.jquery.com/ui/1.9.2/themes/base/jquery-ui.css' | stylesheet_tag }}
<script src="https://ajax.googleapis.com/ajax/libs/jquery/2.2.3/jquery.min.js"></script>
<script src="https://ajax.googleapis.com/ajax/libs/jqueryui/1.9.2/jquery-ui.min.js"></script>

<div style="width:300px; clear:both;">
  <p>
    <label for="date">Pick a delivery date:</label>
    <input id="date" type="text" name="attributes[date]" value="{{ cart.attributes.date }}" />
    <span style="display:block" class="instructions"> We do not deliver during the weekend.</span>
  </p>
</div>

<script>
  document.addEventListener('DOMContentLoaded', function() {
    if (window.jQuery) {
      $(function() {
        $("#date").datepicker({
          minDate: +1,
          maxDate: '+2M',
          beforeShowDay: $.datepicker.noWeekends
        });
      });
    }
  });
</script>
```

6. Click **Save**.
Mobile

1. From the [Shopify app](https://www.shopify.com/install/detect), tap
   .
2. In the **Sales channels** section, tap **Online Store**.
3. Tap **Manage themes**.
4. Find the theme you want to edit, tap the **…** button to open the actions menu, and then tap **Edit code**.
5. In the **Snippets** directory, tap **Add a new snippet**:
6. Create the snippet:
7. Name your snippet `delivery-date`.
8. Tap **Create snippet**. The new snippet file will open in the code editor.
9. In your new `delivery-date.liquid` snippet, paste the following code:

```
{{ '//code.jquery.com/ui/1.9.2/themes/base/jquery-ui.css' | stylesheet_tag }}
<script src="https://ajax.googleapis.com/ajax/libs/jquery/2.2.3/jquery.min.js"></script>
<script src="https://ajax.googleapis.com/ajax/libs/jqueryui/1.9.2/jquery-ui.min.js"></script>

<div style="width:300px; clear:both;">
  <p>
    <label for="date">Pick a delivery date:</label>
    <input id="date" type="text" name="attributes[date]" value="{{ cart.attributes.date }}" />
    <span style="display:block" class="instructions"> We do not deliver during the weekend.</span>
  </p>
</div>

<script>
  document.addEventListener('DOMContentLoaded', function() {
    if (window.jQuery) {
      $(function() {
        $("#date").datepicker({
          minDate: +1,
          maxDate: '+2M',
          beforeShowDay: $.datepicker.noWeekends
        });
      });
    }
  });
</script>
```

8. Tap **Save**.

## Include the snippet in your cart page

To include the delivery date snippet in your cart page:

1. In the **Sections** directory, click `main-cart-items.liquid`.
2. [Find](https://help.shopify.com/en/manual/shopify-admin/productivity-tools/keyboard-shortcuts#find) the closing `</form>` tag in the code. On a new line above the closing `</form>` tag, paste the following code:

```
{% render 'delivery-date' %}
```

3. Click **Save**.

You now have a delivery date input field on your cart page. When you click inside the text field, a calendar will appear:

The date picker used in this customization is a widget from the [jQuery UI library](https://api.jqueryui.com/datepicker).