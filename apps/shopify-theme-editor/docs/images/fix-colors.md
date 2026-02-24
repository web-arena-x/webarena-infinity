# Fix the colors of uploaded images

Source: https://help.shopify.com/en/manual/online-store/images/fix-colors

---

# Fix the colors of uploaded images

When you upload an image to Shopify, the colors in the uploaded image might look different from the original. This can occur when the image has a color profile, which is a set of data stored in a file with a `.ICC` or `.ICM` extension. Color profiles are often embedded into images to help standardize the way that the colors display on different devices. When images are uploaded to Shopify, their color profile is removed.

Color profiles are removed for two reasons:

* When an uploaded image doesn't include a color profile, sRGB (the most common color profile used to display images on the web) is assumed by the web browser. This ensures that your images look the same across all major web browsers.
* Color profiles can take up large amounts of disk space, which can result in heavy loading times.

## On this page

* [Remove the color profile from your image](fix-colors.md#remove-the-color-profile-from-your-image)

## Remove the color profile from your image

You can save your image without the color profile before uploading it to Shopify. This process varies depending on your image editing program. If you use an Adobe product, then follow the steps below:

### Remove a color profile using Adobe Illustrator or Adobe Photoshop

1. Click **Edit**, then **Assign Profile**.
2. Select **Don’t Color Manage This Document**.
3. Click **OK**.

### Remove a color profile using Adobe InDesign

1. Click **Edit**, then **Assign Profile**.
2. For RGB Profile and CMYK Profile, select **Discard (Use Current Working Space)**.
3. Click **OK**.

For more detailed information, you can view the [Adobe documentation on color profiles](https://helpx.adobe.com/photoshop/using/working-with-color-profiles.html).