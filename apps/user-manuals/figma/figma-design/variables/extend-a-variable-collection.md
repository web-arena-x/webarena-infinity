# Extend a variable collection

Source: https://help.figma.com/hc/en-us/articles/36346281624471-Extend-a-variable-collection

---

**The entry point to the variables modal is moving!** Currently, the variables modal is not discoverable if you have a layer selected. We're slowly rolling out a new left navigation bar to users in Figma Design, which will include the entry point to the variables modal so you can access your variable collections anytime.

![navigation-bar-variables-entry-point.png](https://help.figma.com/hc/article_attachments/37506155851415) 

The variables modal will also be edge-to-edge in your window by default, called **variables view**, so that you can see more of your variables and modes at once. You can still minimize to a modal view like before.

[Learn more about the new navigation bar.](https://help.figma.com/hc/articles/360039831974)

Before you Start

Who can use this feature

 

Available on the [Enterprise plan](https://help.figma.com/hc/en-us/articles/360040328273-Choose-a-Figma-Plan)

Anyone with `can edit` access to a file can extend a variable collection

Extended collections help you manage multi-brand design systems. With extended collections, design systems authors can create a parent collection, then extend it to create an instance for each brand. Designers can then override variables within the extended collection to match their brand-specific themes.

An extended collection is tied to its parent collection and will inherit updates made to any variables that have not been explicitly overridden. This allows the extended collection to stay up-to-date with the parent collection, while maintaining brand colors and values.

You can migrate your existing variable collections to the new extended collection format. The migration workflow you use depends on how you’ve organized your brand themes:

- [**Single collection**](#h_01KAF55ARK4A7SV4Q4YFQMKNBK): All brand themes live in one collection
- [**Multi-collection**](#h_01KAF5NSSZEZAKE1AHNQ571KJZ): Brand themes are spread across multiple collections

**Note:** To prevent performance issues, we recommend performing the migration workflow directly on your main branch, rather than creating a separate branch.

## Single collection migration workflow

If you organize your brand themes in a single collection, you can use the following workflow to migrate them to the extended collection format.

### Step 1: Export and delete brand-specific modes

1. Open the Variables modal, then select the collection you want to extend.
2. Select a brand mode from your list of modes, then right-click on it and choose **Export mode**. The variables will be exported to a JSON file.
3. Once exported, right-click on the mode again and select **Delete mode**.
4. Repeat this process for each brand mode until just the parent collection’s modes remain.

![](https://help.figma.com/hc/article_attachments/36458226603543)

### Step 2: Create an extended collection for each brand

1. Select the parent collection from your list of collections, then right-click on it and choose **Extend collection**.
2. Double-click on the extended collection to rename it.
3. Repeat this process for each brand.

![](https://help.figma.com/hc/article_attachments/36458235329303)

### Step 3: Import your brand modes to their extended collection

1. Open an extended collection.
2. Select a mode column, then right-click on it and choose **Import mode**. Select the corresponding JSON file to import over the existing values.

![](https://help.figma.com/hc/article_attachments/36458226608023)

Any values that differ from the parent collection are highlighted in blue. Click on a variable to modify its value, or click **Reset change** to revert the override back to the parent collection’s values.

**Note:** An extended collection’s mode and variable names, settings, and order are inherited from the parent collection. You cannot add additional variables or modes, or change a variable’s description or scope from an extended collection. Open the parent collection to modify these settings.

![](https://help.figma.com/hc/article_attachments/36458235333015)

### Step 4: Publish library updates and reapply modes

Once your extended collections are configured, you’ll need to [publish the library updates](../create-and-share-libraries/publish-a-library.md#h_01J688PTA7SPRDKBNDJ5RYVSP4) to make these changes available in other files.

Accepting the library updates will remove any previously set variable modes from your designs. You will need to reapply your variable modes again using the new extended collection.

![](https://help.figma.com/hc/article_attachments/36458226611991)

## Multi-collection migration workflow

If your brand themes are organized in individual collections, you can use the following workflow to migrate them to the extended collection format.

### Step 1: Export all modes from brand-specific collections

1. Open the variables modal, then select a brand collection.
2. Right-click on each mode and choose **Export mode**. The variables will be exported to a JSON file.
3. Repeat this process for each mode.

![](https://help.figma.com/hc/article_attachments/36458235338519)

### Step 2: Create a new extended collection for each brand

1. Choose a collection to be used as the parent collection, then right-click on it and select **Extend collection**.
2. Double-click on the extended collection to rename it.
3. Repeat this process for each brand.

![](https://help.figma.com/hc/article_attachments/36458235339415)

### Step 3: Import your brand modes to their extended collection

1. Open the extended collection.
2. Select a mode column, then right-click on it and choose **Import mode**. Select the corresponding JSON file to import over the existing mode.

![](https://help.figma.com/hc/article_attachments/36458226617495)

Any values that differ from the parent collection are highlighted in blue. Click on a variable to modify its value, or click **Reset change** to revert the override back to the parent collection’s values.

**Note:** An extended collection’s mode and variable names, settings, and order are inherited from the parent collection. You cannot add additional variables or modes, or change a variable’s description or scope from an extended collection. Open the parent collection to modify these settings.

![](https://help.figma.com/hc/article_attachments/36458226618263)

### Step 4: Update the original brand collection

To prevent designers from accidentally using the original collection, do the following:

First, delete each mode in the brand collection except the original mode:

1. Open the original collection
2. Right-click on each mode except the first, then choose **Delete mode**.

![](https://help.figma.com/hc/article_attachments/36458226619671)

Then, create an alias for each variable in the original collection that references the parent collection. Learn more about [aliasing variables](create-and-manage-variables-and-collections.md#alias).

Finally, deselect the **Show in all supported properties** checkbox on the **Scope** tab of the variable settings. Learn more about [scoping variables](create-and-manage-variables-and-collections.md#h_01H32HZB74TE7MJXYBWEBBQWJV).

![](https://help.figma.com/hc/article_attachments/36458232456599)

### Step 5: Publish library updates and reapply modes

Once your extended collections are configured, you’ll need to [publish the library updates](../create-and-share-libraries/publish-a-library.md#h_01J688PTA7SPRDKBNDJ5RYVSP4) to make these changes available in all consuming files.

Accepting the library updates will remove any previously set variable modes from your designs. You will need to reapply your variable modes again using the new extended collection format.

![](https://help.figma.com/hc/article_attachments/36458232459543)