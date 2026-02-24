# Create a CMS list

Source: https://help.figma.com/hc/en-us/articles/36165334984855-Create-a-CMS-list

---

Who can use this feature

Available on [all plans](https://help.figma.com/hc/en-us/articles/360040328273)

Requires edit access to the site file

A **CMS list** is a repeating design block that displays multiple items from a collection. It provides a simple, dynamic way for visitors to browse your content, and it updates automatically as new content is added to your collection.

Common examples of CMS lists include:

- Recent blog posts
- Customer testimonials
- Team profiles
- Features and benefits

**What’s the difference between a CMS page and a CMS list?**

![](https://help.figma.com/hc/article_attachments/36434853447831)

Suppose you’re working on a cooking website with lots of recipes.

A **CMS list** displays multiple items from a collection—like a grid of recipe previews with titles, images, and short descriptions. Visitors can browse through the list to find what they’re interested in.

A **CMS page** shows all the details for a specific item: the ingredients, steps, and photos. Each CMS page uses the same design template, but the content updates automatically based on the selected recipe.

### How it works

A CMS list has two parts:

- A **main component** that controls styling of the repeating list elements.
- A **CMS list** layer that contains repeating instances of the component. The child layers of these instances are connected to fields in your CMS collection.

![CMS list component with no connected content on the left; a connected CMS list layer displaying case studies with images and titles on the right.](https://help.figma.com/hc/article_attachments/36434853447959)

There are two main ways to create a CMS list:

- [Insert a pre-built CMS list block](#h_01KAD5VTQNQSCH6STZ0BR0XG1V)
- [Create your own CMS list from an existing design](#h_01KAD5VTQNKQFCSB0ZKRFJ4AZN)

## Insert a pre-built CMS list block

**Note**: You’ll need to [create a CMS collection](https://help.figma.com/hc/en-us/articles/36165345510551) before you can add CMS blocks.

If you don’t have a design yet, you can drop in a pre-built CMS list block. This block includes a main component and a CMS list layer with instances of the component inside. The layers are already connected to fields in the collection.

1. Click **Insert** from the left navigation bar.
2. From the **Blocks** tab, click **CMS**.
3. Drag a **CMS list** onto the canvas for the relevant collection.

When you edit the main component, all instances within the CMS list layer update automatically.

## Create your own CMS list

The easiest way to convert a design into a CMS list is from **Connect** view.

1. Click **CMS** in the left navigation bar.
2. Select the **Connect** tab.
3. Hover over a collection, click **Connect**, then choose **Part of a page**.
4. Select the parent frame on the canvas.

There are a few additional ways ways to convert a design, depending on its structure:

![](https://help.figma.com/hc/article_attachments/36434853448215)

**A parent frame with repeating child layers**

1. Select the parent frame.
2. In the right sidebar, click **Connect to CMS** and select a collection.

What happens:

- The parent frame changes to a CMS list layer.
- Figma generates a new main component of the repeating layers if one doesn’t exist already.
- The repeating layers become instances of the component.

![](https://help.figma.com/hc/article_attachments/36434906401431)

**A frame containing a design you want to repeat**

1. Select the parent frame.
2. In the right sidebar, click **More.**
3. Select **Connect to CMS**, then select a collection.

What happens:

- Figma turns the frame into a main component if it isn’t one already.
- Figma creates a CMS list layer and populates it with instances of the component.

![](https://help.figma.com/hc/article_attachments/36434853448599)

**Two identical layers**

1. Select any two identical layers.
2. In the right sidebar, click **Connect to CMS** and select a collection.

What happens:

- Figma wraps the layers in a new CMS list layer.
- Figma generates a new main component based on the identical layers if one doesn’t exist already.
- The identical layers become instances of the component.

**Note**: If you create a CMS list from design elements in a webpage with multiple breakpoints, Figma will create a component variant for each unique design. This helps you style the list for different devices and screen widths.

[Learn more about creating and working with responsive components.](https://help.figma.com/hc/en-us/articles/31242826664983)

**Note**: It’s not possible to create a CMS list from designs in an [auto layout grid flow](https://help.figma.com/hc/en-us/articles/31289469907863).

## Connect layers to CMS fields

Once you’ve created the CMS list, connect its layers to fields in your collection.

**Note**: You can only connect CMS fields to layers within a CMS page or in a CMS list.

### Connect layers from the right sidebar

You can quickly connect layers from the right sidebar while working on the CMS list. This process is similar to [working with variables](https://help.figma.com/hc/en-us/articles/15339657135383).

**Connect to a text layer**

1. Select a text layer in the CMS list. For text layers, make sure you select the actual text layer and not any parent layers, like a frame.
2. At the top of the right sidebar, click **Apply variable or CMS field,** then select a field.

**Connect to an image fill**

You can connect an image field to any layer with a fill, like shapes and frames.

1. Select a layer with a fill within the CMS list.
2. In the **Fill** section of the right sidebar, click **Add fill**.
3. Select the **CMS** tab, then select an image field in the collection to connect it.

**Connect a link**

You can connect a link field to any linkable element, like text, frames, or shapes.

1. Select a layer within the CMS list.
2. In the right sidebar, click **Add link**.
3. Enter a link, or click the dropdown menu to select an existing webpage from your site.

**Tip**: This is how you [link a CMS list to a CMS page](#h_01KAD5VTQP1MTX39Y2Y2RMTQHW).

### Connect layers in Connect view

![Cursor is selecting fields in connect view in the left sidebar and connecting them to layers in the CMS list](https://help.figma.com/hc/article_attachments/36434853449111)

The **Connect** view lets you quickly wire up an existing layout or review what’s already connected. In this view, you choose a field, then select the target layer in the CMS list to connect it.

**Note:** Certain field types only connect to compatible layer types. For example, you can’t connect a text field to a shape or frame.

1. Click **CMS** in the left navigation bar.
2. Select the **Connect** tab.
3. Click a field in the collection, then click a target layer in the CMS list to connect it. All items in the list will automatically update.
4. Repeat for additional fields and layers.

**Note**: You can only connect fields to layers in the CMS list, not the main component.

![Cursor double clicks connected layers in a CMS list, opening a right sidebar for editing the selected item.](https://help.figma.com/hc/article_attachments/36434853449367)

**Tip:** While in **Connect** view, double click a connected design on the canvas to edit the field values for the current item.

## Set the number of items in the CMS list

By default, Figma includes all items in a collection in a CMS list—but you can limit the number if needed.

1. Select the **CMS list layer** in the **Layers** section of the left sidebar.
2. Select a value from the **Limit** property at the top of the right sidebar.

**Note**: Filtering or sorting a CMS list isn’t currently supported.

## Reorder items in the CMS list

Reordering items in the table view of your collection updates their order across all CMS lists.

1. Click **CMS** in the left navigation bar.
2. Hover over the item whose position you want to change.
3. Click and drag the icon at the very left of the row and move the item to a new position.

## Link a CMS list to a CMS page

It’s common to link items in a CMS list to their corresponding CMS page. For example, you might create a list of blog posts on the **Home** page that link to each post. To add a link to a CMS list:

1. Select the element in the list you want to turn into a link.
2. From the right sidebar, click **Add link.**
3. Open the **dropdown menu** and select the CMS page template you’d like to use. It will be listed under the name of the collection and have a URL path that ends with `/slug` .

## Remove a connection from the CMS list

To disconnect a layer in a CMS list:

1. From the left navigation bar, click **CMS** and switch to the **Connect** tab.
2. Click a connected layer’s annotation, then click **Remove connection**.

When you remove a connection, the disconnected layers will keep their content from the last known-connected state.

**Tip**: You can also disconnect a layer from the properties panel. Select it on the canvas, then click **Remove connection** in the right sidebar.

## Frequently asked questions

**Can I add a CMS list to a CMS page?**

Yes. For example, you could add a CMS list at the bottom of a blog post to display a list of other posts to read.

**What happens if an item has an empty field when connected to a layer?**

- An empty text or date field causes the text layer to render with no content.
- An empty image field translates to an empty, transparent fill on the frame or shape. To make sure an image always shows, apply a fallback fill *below* the connected fill, so an image still appears if the CMS field is empty.

**Why can’t I move layers out of a CMS list?**

A CMS list is made up of component instances. The number of component instances is controlled by the CMS list layer. To change the number of items in the list, select the main CMS list layer and then adjust the limit property at the top of the right sidebar.

To update the design of layers in the list, edit the main component.