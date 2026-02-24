# Using your own theme assets for help center

Source: https://support.zendesk.com/hc/en-us/articles/4408829155226-Using-your-own-theme-assets-for-help-center

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Growth, Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support with** | Guide Professional or Enterprise |

Location:  Knowledge admin > Customize design (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/guide_icon_customize.png)) > select theme > Edit > Assets

You can upload assets, such as images and files, to any of your help center themes.

This article contains the following sections:

- [Uploading an asset for your theme](#topic_dyl_ncf_dbb)
- [Using uploaded assets in the theme's code](#topic_azx_ncf_dbb)
- [Replacing an asset in your theme](#topic_vp4_fcl_fdb)
- [Deleting a theme asset](#topic_ec2_gdf_dbb)

## Uploading an asset for your theme

You can upload assets such as images and files to your help center. The assets are stored in
a web cache in a cloud delivery network (CDN). Web caches reduce bandwidth requirements and
server load and improve response times.

There are a number of allowable file types for themes. See [Allowable file types for theme assets](#topic_u41_tdt_vhb).

**To upload your own theme assets**

1. In [Knowledge admin](https://support.zendesk.com/hc/en-us/articles/9041943683354#topic_b5q_nwn_s2c), click **Customize design**
   (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/guide_icon_customize.png)) in the sidebar.
2. Click **Customize** on the theme you want to edit.
3. Click **Edit code**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/theming_asset_edit_code.png)
4. In the **Files** section, click **Add new**, then select **Asset**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/theming_addnew_asset.png)
5. Browse to select your file. Theme asset names must be unique and cannot be more than
   50 characters. Asset names can contain any of the following: letters, numbers, dot,
   minus, plus, underscore, and dash. Asset names are *not* case sensitive, so you
   cannot have an asset named asset.jpg and Asset.jpg.

   The asset file is added to your list of asset files.

### Allowable file types for theme assets

The following table shows the file types that are allowed as theme assets. The allowable
file types for assets are limited to the types used in the theming of a help
center.

| Asset type | File types allowed |
| --- | --- |
| Images | jpg, jpeg, png, gif, svg, webp, tiff, tif, bmp, ico, webm |
| Fonts | woff2, woff, eot, otf, ttf, svg |
| Text files | js, css, html, json, txt, xml |
| Other | mp4, swf, wav, ogg. mp3 |

Rich content files types, such as Microsoft PowerPoint, Microsoft Word and PDFs, can be
article attachments but cannot be theme assets.

## Using uploaded assets in the theme's code

You can reference an uploaded asset in the theme's **style.css** file or in its
templates. In **style.css**, you use asset path variables provided by Guide. In
templates, you use the Curlybars [asset helper](https://developer.zendesk.com/apps/docs/help-center-templates/helpers#asset-helper).

Using asset variables and helpers in your code lets you easily replace the assets in the
theme without editing the theme code. See [Replacing an asset in your theme](#topic_vp4_fcl_fdb).

Note: You can't use the path variables or the helper in the theme's **script.js** file.

**To use an uploaded asset in your theme code**

1. In [Knowledge admin](https://support.zendesk.com/hc/en-us/articles/9041943683354#topic_b5q_nwn_s2c), click **Customize design**
   (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/guide_icon_customize.png)) in the sidebar.
2. Click **Customize** on the theme you want to edit.
3. Click **Edit Code**.
4. In the **Assets** section, click the asset file you want to use.

   Various
   expressions for the asset appear.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/theming_copy_asset.png)
5. Click **Copy** to copy the asset expression you need in the Clipboard.
6. Paste the asset expression in your theme code.

### Examples

**style.css**

```
.class-name { 
  background: url($assets-backpack2-jpeg);
}
```

The value `assets-backpack2-jpeg` is a variable that contains the relative
path to the asset.

**.hbs files**

In html markup:

```
<img src="{{asset 'backpack2.jpeg'}}">
```

In a style tag:

```
<style>
  .class-name { 
    background: url("{{asset 'backpack2.jpeg'}}");
  }
</style>
```

In a script tag:

```
<script>
  var assetsBackpack2 = "{{asset 'backpack2.jpeg'}}";
</script>
```

While you can insert the asset helper in a script tag in a template, you can't use it in
the **script.js** file.

For more information on editing your theme code, see [Customizing your help center theme](https://support.zendesk.com/hc/en-us/articles/4408846524954).

## Replacing an asset in your theme

Using asset variables and helpers as described in [Using uploaded assets in the theme's code](#topic_azx_ncf_dbb) above lets you replace an asset in the theme dynamically without editing
the theme code. You can update the theme just by selecting a new asset file on your
system.

**To replace an asset**

1. In [Knowledge admin](https://support.zendesk.com/hc/en-us/articles/9041943683354#topic_b5q_nwn_s2c), click **Customize design**
   (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/guide_icon_customize.png)) in the sidebar.
2. Click **Customize** on the theme you want to edit.
3. Click **Edit code**.
4. In the **Assets** section, locate the asset file you want to replace.
5. Click the options menu at the end of the asset file name, then select
   **Replace**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/theming_replace_asset.png)
6. Select a new asset on your system.

   Once uploaded, the theme is updated
   dynamically by any variable or helper that references the asset. The change is
   immediate.

   The asset is not replaced if you used the full URL of the asset in
   the HTML source of published help center pages. The link to the asset will break
   because replacing an asset changes the asset's published URL. As a result, avoid
   using the published asset URL in a theme, a page template, or an external web
   page.

## Deleting a theme asset

You can easily delete any theme asset you're no longer using in your theme.

**To delete a theme asset**

1. In [Knowledge admin](https://support.zendesk.com/hc/en-us/articles/9041943683354#topic_b5q_nwn_s2c), click **Customize design**
   (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/guide_icon_customize.png)) in the sidebar.
2. Click **Customize** on the theme you want to edit.
3. Click **Edit code**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/theming_asset_edit_code.png)
4. In the **Assets** section, locate the asset file you want to delete.
5. Click the options menu at the end of the asset file name, then select **Delete
   asset**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/theming_delete_asset.png)
6. Confirm that you want to delete the asset.

   The asset is removed from your assets
   list.