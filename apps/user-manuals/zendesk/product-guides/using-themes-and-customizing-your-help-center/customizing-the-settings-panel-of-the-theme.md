# Customizing the Settings panel of the theme

Source: https://support.zendesk.com/hc/en-us/articles/4408846524954-Customizing-the-Settings-panel-of-the-theme

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Growth, Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support with** | Guide Professional or Enterprise |

When you [download a theme](https://support.zendesk.com/hc/en-us/articles/4408828976538#topic_udw_zdc_hbb), the exported files include a file named **manifest.json**. The file defines the Settings panel of the theme in Guide:

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/hc_settings_manifest.png)

This guide describes the manifest file and what you can do with it. It also provides a reference of its specification. For an example, export your theme and open the **manifest.json** file in a text editor.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/hc_manifest_file.png)

Topics covered:

- [Understanding the manifest.json file](#understanding-the-manifest-json-file)
- [Using settings in manifest.json as variables](#using-settings-in-manifest-json-as-variables)
- [Modifying the manifest.json file](#modifying-the-manifest-json-file)
- [Manifest object](#manifest-object)
- [Setting object](#setting-object)
- [Variable object](#variable-object)
- [Type property](#type-property)
- [File type](#file-type)
- [List type](#list-type)
- [Range type](#range-type)
- [Translations](#translations)

### Understanding the manifest.json file

When you export a theme, the exported files include a file named **manifest.json**. You can use the manifest file to define the theme's [Settings panel](https://support.zendesk.com/hc/en-us/articles/4408824139546) in Guide.

You can modify existing settings in the panel or create new ones. In the following example, the manifest file assigns a default value of "#30aabc" to the **color\_brand\_text** setting:

```
"settings": [
 {
    "label": "Colors",
    "variables": [
      {
        "identifier": "color_brand_text",
        "type": "color",
        "description": "color_brand_text_description",
        "label": "color_brand_text_label",
        "value": "#30aabc"
      },
      ...
    ]
 },
 ...
]
```

After [importing the theme](https://support.zendesk.com/hc/en-us/articles/4408828976538#topic_jpd_zdc_hbb) into Guide, the **color\_brand\_text** setting appears in the Settings panel with the label **Brand text color**, as specified by the "label" property in the manifest file, and the default hex value of the color picker is #30aabc, as specified by the "value" property:

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/hc_theme_setting_example.png)

### Using settings in manifest.json as variables

Settings are also called *variables* because you can use a setting's identifier as a variable in the theme's files. Changing a value in the Settings panel updates the value in all the files that use the variable.

Note: If you encounter a variable error when importing your Guide theme, there may be an issue with your formatting. For more information, see the article: [Error: The property ‘#/settings/X/variables/X’ of type object did not match any of the required schemas](https://support.zendesk.com/hc/en-us/articles/5631140006298-Error-The-property-settings-X-variables-X-of-type-object-did-not-match-any-of-the-required-schemas).

You can insert a variable in the theme's **style.css** file using the `$identifier` syntax, or in a page template using the `settings.identifier` helper in Curlybars. Examples:

**style.css**

```
input:focus {
 border: 1px solid $color_brand_text;
}
```

You can also use single curly brackets to embed the helper in a CSS expression, as follows:

```
max-width: #{$search_width}px;
```

**Page template**

```
<div style="background-color:{{settings.color_brand_text}}">
```

### Modifying the manifest.json file

The **manifest.json** file is not included in the list of files in the Edit Code page in Help Center. To edit the **manifest.json** file, you must export the theme to files, make changes to the manifest file on your system, then import the theme in Guide.

**To export the theme**

- See [Downloading a help center theme](https://support.zendesk.com/hc/en-us/articles/4408828976538#topic_udw_zdc_hbb).

**To import the modified theme**

- See [Importing a help center theme](https://support.zendesk.com/hc/en-us/articles/4408828976538#topic_jpd_zdc_hbb).

### Manifest object

The manifest's document root object has the following properties:

| Name | Type | Comment |
| --- | --- | --- |
| name | string | Theme name |
| author | string | The person, team, or organization who created the theme |
| version | string | Theme version that follows the [Semantic versioning 2.0.0](https://semver.org/) standard |
| api\_version | string | Templating API version |
| settings | array | List of setting objects. See [Setting object](#setting_object) |

#### Example

```
{
 "name": "My second theme",
 "author": "Jane Doe",
 "version": "1.0.1",
 "api_version": 3,
 "settings": [
    ...
 ]
}
```

### Setting object

The settings in both the [manifest file](#manifest-object)  and the Settings panel in Guide are organized into groups such as Colors or Fonts. Each setting group is defined in the manifest file by a *setting object*. Each object consists of a label and one or more settings, such as Brand Color and Text Color.

You can modify setting objects or create your own. The objects are reflected in the theme's Settings panel when you import the theme in Guide.

Each setting object has the following properties:

| Name | Type | Comment |
| --- | --- | --- |
| label | string | A translation property name. See [Translations](#translations). Displays a title for a group of settings. |
| variables | array | List of settings in the group. Also called variables. See [Variable object](#variable-object). The manifest file can have a maximum quantity of 200 variable objects. See [Guide product limits for your help center](https://www.google.com/url?q=https://support.zendesk.com/hc/en-us/articles/4408831783962-Guide-product-limits-for-your-help-center%23topic_cnb_vnd_dcb&sa=D&source=docs&ust=1686667397108455&usg=AOvVaw2sZuLqHt-h3BnM2FgIGRWb) (Total number of settings in manifest.json). |

#### Example

```
"settings": [
 {
    "label": "colors_group_label",
    "variables": [{...}, ...]
 },
 {
    "label": "fonts_group_label",
    "variables": [{...}, ...]
 },
 {
    "label": "brand_group_label",
    "variables": [{...}, ...]
 },
 {
    "label": "banners_group_label",
    "variables": [{...}, ...]
 }
]
```

Note: The value of the `"label"` properties are translation property names. See [Translations](#translations).

The example creates the following categories in the Settings panel:

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/hc_settings_panel_modified.png)

### Variable object

Each [setting object](#setting-object) has a `variables` array that lists the actual settings. They're called variables because you can insert them as variables in Help Center templates or in CSS. See [Guide product limits for your help center](https://www.google.com/url?q=https://support.zendesk.com/hc/en-us/articles/4408831783962-Guide-product-limits-for-your-help-center%23topic_cnb_vnd_dcb&sa=D&source=docs&ust=1686667397108455&usg=AOvVaw2sZuLqHt-h3BnM2FgIGRWb) (Total number of settings in manifest.json).

You can define any variable you want. However, the manifest file must contain two file variables with the following identifiers: "logo" and "favicon". See [Required variables](#required-variables).

Each variable has the following properties:

| Name | Type | Comment |
| --- | --- | --- |
| identifier | string | Variable name that you can use in CSS or Curlybars expressions. Must be 30 characters or less and contain only alphanumeric characters and \_ (underscore) |
| type | string | UI control in the Settings panel in Guide to get the value from the user. One of `text`, `list`, `checkbox`, `color`, `file`, or `range`. See [Type property](#type-property) |
| label | string | The name of the setting that gets displayed next to the UI control in the Settings panel. Must be 40 characters or less. To translate this value, use a translation property name. See [Translations](https://support.zendesk.com/hc/en-us/articles/5865881240858#translations). Translations do not have a limit of characters. |
| description | string | A brief description of the setting that gets displayed next to the UI control in the Settings panel. Must be 80 characters or less. To translate this value, use a translation property name. See [Translations](https://support.zendesk.com/hc/en-us/articles/5865881240858#translations). Translations do not have a limit of characters. |
| value | string | The setting's default value |
| options | array | For the `list` type only. An array of list items. See [Option object](#option-object) |
| min | integer | For the `range` type only. The minimum value of the range |
| max | integer | For the `range` type only. The maximum value of the range |

#### Example

```
"variables": [
 {
    "identifier": "color_brand",
    "type": "color",
    "label": "color_brand_label",
    "description": "color_brand_description",
    "value": "#0072EF"
 },
 ...
]
```

The example creates the following label and control in the Settings panel:

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/hc_settings_panel_variable.png)

#### Required variables

You must specify the following two variables in the manifest file or the file will be rejected on import:

- logo - the `identifier` must be "logo" and the `type` must be "file"
- favicon - the `identifier` must be "favicon" and the `type` must be "file"

**Example**

```
"variables": [
 {
    "identifier": "logo",
    "type": "file",
    "description": "logo_description",
    "label": "logo_label"
 },
 {
    "identifier": "favicon",
    "type": "file",
    "description": "favicon_description",
    "label": "favicon_label"
 }
]
```

### Type property

Each [variable object](#variable-object) has a `type` property that specifies a UI control to set the setting value in the Settings panel in Guide. The property can have one of the following values:

- `text` - Text input field. Each text field has a limit of 1000 characters.
- `list` - Dropdown list. Includes a list of option objects for the list items. See [List type](#list-type)
- `checkbox` - Checkbox. See [Checkbox type](#checkbox-type)
- `color` - Color picker
- `file` - File uploader. See [File type](#file-type)
- `range` - Range input field. See [Range type](#range-type)

#### Example

```
{
 "identifier": "color_headings",
 "type": "color",
 ...
}
```

### List type

If the [type](#types) of a variable object is "list", then the object includes an `options` array to populate the dropdown list. Each option in the list has the following properties:

| Name | Type | Comment |
| --- | --- | --- |
| label | string | Friendly text displayed for the list item. Must be 40 characters or less. To translate this value, use a translation property name. See [Translations](https://support.zendesk.com/hc/en-us/articles/5865881240858#translations). Translations do not have a limit of characters. |
| value | string | Underlying value of the list item |

You must specify more than one option in the array or importing the theme will fail. The number of options should not exceed 20. See [Guide product limits for your help center](https://support.zendesk.com/hc/en-us/articles/4408831783962-Guide-product-limits-for-your-help-center#topic_cnb_vnd_dcb) (Total number of options in a list type setting).

#### Example

```
{
 "identifier": "font_headings",
 "type": "list",
 "label": "Heading",
 "description": "Font for headings",
 "value": "Arial, 'Helvetica Neue', Helvetica, sans-serif",
 "options": [
    {
      "label": "Arial",
      "value": "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    },
    {
      "label": "Copperplate Light",
      "value": "'Copperplate Light', 'Copperplate Gothic Light', serif"
    },
    {
      "label": "Baskerville",
      "value": "Baskerville, 'Times New Roman', Times, serif"
    }
 ]
}
```

### Checkbox type

If the [type](#types) of a variable object is "checkbox", use the object's **value** property to specify the value that's set when the user selects the checkbox. The value must be a boolean.

| Name | Type | Comment |
| --- | --- | --- |
| value | boolean | `true` or `false` |

#### Example

```
{
 "identifier": "scoped_hc_search",
 "type": "checkbox",
 "description": "scoped_help_center_search_description",
 "label": "scoped_help_center_search_label",
 "value": true
}
```

### File type

A variable object with a [type](#types) of "file" adds a file uploader control in the Settings panel. This type of variable doesn't have a **value** property. Example:

```
{
 "identifier": "community_image",
 "type": "file",
 "description": "community_image_description",
 "label": "community_image_label"
}
```

The value is a file URL determined by the system.

You must provide a default file for the theme to use until a user uploads a different file. The name of the default file must match the variable's identifier. Place the file in the **settings** folder in your theme files. Example:

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/hc_settings_default_file.png)

Use file variables where URLs are expected in the theme files. Examples:

**style.css**

```
.community_banner {
    background-image: url($community_image);
}
```

**Page template**

```
<img src="{{settings.community_image}}">
```

### Range type

A variable object with a type of "range" adds a slider control in the Settings panel. Example:

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/hc_settings_range_type.png)

A range variable includes a **min** and a **max** property to specify the range of values that the user can set when they move the slider. The values must be integers.

#### Example

```
{
 "identifier": "font_size",
 "type": "range",
 "description": "font_size_description",
 "label": "font_size_label",
 "min": 70,
 "max": 150,
 "value": 100
}
```

### Translations

The visible strings in the Settings panel are all defined in *translations*. A translation consists of a property name and value. Example:

`"text_color_label": "Text color"`

The property names are arbitrary. You can specify any name you like.

The translations are stored in language-specific JSON files in the **translations** folder in the theme's root folder:

```
/ translations
   - en-us.json
   - es.json
   - fr.json
   - ...
```

Each file consists of a JSON object with a list of translations:

**en-us.json**

```
{
 "brand_color_description": "Brand color for major navigational elements",
 "brand_color_label": "Brand color",
 ...
}
```

The translations are used to specify the labels and descriptions in the Settings panel.

**To specify strings for labels and descriptions**

1. In the **translations** folder, locate the JSON file for the default language of your Help Center. Example: **en-us.json**.
2. Update the values of existing properties or add new properties. Example:

   ```
   {
     "text_color_label": "Text color",
     "text_color_description": "Text color for body and heading elements",
     ...
   }
   ```
3. In variables, use the translation property name as the value of `"label"` or `"description"` attributes.

   ```
   "variables": [
     {
       "identifier": "color_text",
       "type": "color",
       "label": "text_color_label",
       "description": "text_color_description",
       "value": "#0072EF"
     },
     ...
   ]
   ```

   See [Variable object](#variable-object). If you create a property or change a property name, make sure to update your variables.

You can localize the labels and descriptions in the Settings panel. You need to provide the localized strings yourself.

**To localize labels and descriptions**

1. In the **translations** folder, locate the JSON file for each extra language you want to support.
2. Copy the property names defined in your default translation file. Example:

   ```
   {
     "text_color_description": "",
     "text_color_label": "",
     ...
   }
   ```
3. Specify a localized string for each property. Examples:

   **fr.json**

   ```
   {
     "text_color_description": "Couleur du texte pour les éléments du titre et du corps",
     "text_color_label": "Couleur du texte",
     ...
   }
   ```