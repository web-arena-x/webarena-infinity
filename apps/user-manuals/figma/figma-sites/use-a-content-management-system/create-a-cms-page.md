# Create a CMS page

Source: https://help.figma.com/hc/en-us/articles/35222938006679-Create-a-CMS-page

---

Who can use this feature

Available on [all plans](https://help.figma.com/hc/en-us/articles/360040328273)

Requires edit access to the site file

![Cursor clicks the slug in the webpage header and chooses a different option; the page content updates dynamically.  ](https://help.figma.com/hc/article_attachments/36434249908887)

A CMS page is a dynamic webpage that displays individual items from a collection. It lets you design a single layout and automatically populate it with content—such as an article, product, or case study—pulled directly from your CMS.

This means you can publish multiple pages using the same design template without duplicating, rebuilding or adjusting the layout each time.

In a CMS page, each item’s **slug** is appended to the webpage’s URL path. For example, if you convert the `/reviews` page into a CMS page, each item will appear at a URL like `/reviews/sgt-peppers-lonely-hearts-club-band`.

**What’s the difference between a CMS page and a CMS list?**

![](https://help.figma.com/hc/article_attachments/36434235461783)

Suppose you’re working on a cooking website with lots of recipes.

A **CMS list** displays multiple items from a collection—like a grid of recipe previews with titles, images, and short descriptions. Visitors can browse through the list to find what they’re interested in.

A **CMS page** shows all the details for a specific item: the ingredients, steps, and photos. Each CMS page uses the same design template, but the content updates automatically based on the selected recipe.

## Insert a pre-built CMS page block

**Note**: You’ll need to [create a CMS collection](https://help.figma.com/hc/en-us/articles/36165345510551) before you can add CMS blocks.

If you’re starting from a blank webpage for your CMS, we recommend inserting a pre-built CMS page block. This block is already connected to your CMS, and just needs to be styled:

1. Click  **Insert** from the left navigation bar.
2. From the **Blocks** tab, click **CMS**.
3. Drag a CMS page onto the canvas for the relevant collection.
4. Style the elements containing your content, and add any new design elements as needed.

**Tip:** If your collection contains a rich text field, [learn more about how to style it](https://help.figma.com/hc/en-us/articles/36165352090775).

## Create your own CMS page

If your webpage already contains design elements, you can convert it into a CMS page by connecting it to a collection, then connecting its layers to fields in the collection.

**Note:** You can’t turn the **Home** page into a CMS page.

To create a CMS page:

1. Select the webpage on the canvas.
2. In the right sidebar, click  **CMS** and select a collection.

**Tip:** You can also create a CMS page from **Connect view.** Click  **CMS** in the left navigation bar, then switch to the **Connect** tab at the top of the left sidebar. Hover over a collection name, click **Connect,** and select **Full page**. Then, click your webpage to connect it.

![Cursor switches to a different item in the webpage header. Nothing happens because the page's layers aren't connected yet. ](https://help.figma.com/hc/article_attachments/36434235462039)

With the page connected, you can now switch between collection items in the webpage header. Notice how the page content doesn’t change as you switch between items? To make it dynamic, follow the steps below to connect the CMS collection to layers on the page.

## Connect layers to CMS fields

After your webpage is connected to a collection, connect individual layers to CMS fields so the design updates automatically for each item.

**Note**: You can only connect CMS fields to layers within a CMS page or in a CMS list.

### Connect layers from the right sidebar

![A layer is selected on the canvas and the cursor is connecting it to the CMS from the properties panel.](https://help.figma.com/hc/article_attachments/36434235465495)

You can quickly connect layers from the right sidebar while working on the webpage. This process is similar to [working with variables](https://help.figma.com/hc/en-us/articles/15339657135383).

**Connect to a text layer**

1. Select a layer. For text layers, make sure you select the actual text layer and not any parent layers, like a frame.
2. At the top of the right sidebar, click  **Apply variable or CMS field,** then select a field.

**Connect to an image fill**

You can connect an image field to any layer with a fill, like shapes and frames.

1. Select a layer with a fill within the CMS page.
2. In the **Fill** section of the right sidebar, click  **Add fill**.
3. Select the **CMS** tab, then select an image field in the collection to connect it.

**Connect a link**

You can connect a link field to any linkable element, like text, frames, or shapes.

1. Select a layer within the CMS list.
2. In the right sidebar, click  **Add link**.
3. Enter a link, or open the  dropdown menu to select an existing webpage from your site.

**Tip**: This is how you [link a CMS list to a CMS page](https://help.figma.com/hc/en-us/articles/36165334984855).

### Connect layers in Connect view

![In connect view, a cursor is selecting different fields in the left sidebar and connecting them to layers in a webpage. ](https://help.figma.com/hc/article_attachments/36434235465623)

**Connect** view helps you wire up an existing layout or review what’s already connected. In this view, you choose a field, then select the target layer in the webpage to connect it.

**Note:** Certain field types only connect to compatible layer types. For example, you can’t connect a text field to a shape or frame.

1. Click  **CMS** in the left navigation bar.
2. Select the **Connect** tab.
3. Click a field in the collection, then click a target layer in the CMS page to connect it.
4. Repeat for additional fields and layers.

**Note**: If you can’t connect a field to a layer, make sure you’ve already [created the CMS page](#h_01KAD2SZMAKBWFVP67Z75MR4VJ).

**Tip:** While in **Connect** view, double click a connected design on the canvas to edit the field values for the current item.

## Preview items in the CMS page

Once layers are connected, you can preview how the page looks for different items in the collection.

Click the **slug** in the header of the CMS webpage to switch between items.

**Tip:** You can also click  **Preview** to view the page in a full screen preview, or press `Shift` `Space` to open the inline preview.

**Note**: You can’t preview a CMS page while in **Connect** view.

## Remove a connection

To disconnect a layer or CMS page:

1. From the left navigation bar, click  **CMS** and switch to the **Connect** tab.
2. Click the collection name in the header of the webpage, or a connected layer, and select  **Remove connection**.

When you remove a connection, the disconnected page or layer keeps its last known content but no longer updates dynamically.

**Tip**: You can also disconnect a layer from the properties panel. Select it on the canvas, then click  **Remove connection** in the right sidebar.

## Frequently asked questions

**What happens if an item has an empty field when connected to a layer?**

- An empty text or date field causes the text layer to render with no content.
- An empty image field translates to an empty, transparent fill on the frame or shape. To make sure an image always shows, apply a fallback fill *below* the connected fill, so an image still appears if the CMS field is empty.

**Can I connect components to CMS fields?**

You can connect component **instances** in a CMS page to fields in a collection. Connect their text layers, image fills, and linkable parts as needed. You can’t connect a main component, as these aren’t allowed inside webpages.

**What happens if I duplicate a connected layer?**

Duplicated layers remain connected unless they are duplicated outside of the CMS page or list. You can always [remove the connection](#h_01KAD2SZMAS2M6T9KXB8ZXXWPP) and reconnect to a different field as needed.

**What happens if I move a connected layer outside the CMS page?**

When a connected layer is moved outside the CMS page—onto the canvas or into a different webpage—it loses its CMS connection. The layer retains its last known content but will no longer update dynamically.