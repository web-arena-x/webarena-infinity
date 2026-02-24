# Creating custom layouts to improve agent workflow

Source: https://support.zendesk.com/hc/en-us/articles/5447837546138-Creating-custom-layouts-to-improve-agent-workflow

---

Ticket layouts control the look and feel of the ticket interface. Zendesk comes with a default ticket layout that you can use immediately out-of-the-box. You can also use layout builder to create your own custom layouts to use with tickets. With custom layouts, you can optimize the ticket interface to maximize your agents’ efficiency. For more information, seeAbout custom layouts.

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support** | Professional or Enterprise |

Location:  Admin Center > Workspaces > Agent tools > Layouts

Enterprise plans can have multiple layouts active at the same time for
different types of tickets. Professional plans can have only one active layout. See [Plan requirements for custom layouts](https://support.zendesk.com/hc/en-us/articles/5447690090138#topic_bt5_nq1_4bc).

Ticket layouts control the look and feel of the ticket interface. Zendesk comes
with a default ticket layout that you can use immediately out-of-the-box. You can also use
layout builder to create your own custom layouts to use with tickets. With custom layouts, you
can optimize the ticket interface to maximize your agents’ efficiency. For more information,
see [About custom layouts](https://support.zendesk.com/hc/en-us/articles/5447690090138).

You must have the Zendesk Agent Workspace [activated](https://support.zendesk.com/hc/en-us/articles/4581758611866-) and be an admin to create custom layouts.

This article describes how to create custom layouts for your tickets. Topics
include:

- [Creating a new layout](#topic_eyp_5rl_znb)
- [Adding and removing components in a layout](#topic_tb4_tcv_qwb)
- [Resizing and moving components in a layout](#topic_nrx_tcv_qwb)
- [Stacking components in a layout](#topic_y3x_vcv_qwb)
- [Undoing and redoing layout changes](#topic_cck_xsh_xwb)
- [Managing components in the context panel](#topic_zyc_xcv_qwb)

**Related articles**

- [About custom layouts with layout builder](https://support.zendesk.com/hc/en-us/articles/5447690090138)
- [Viewing and managing custom layouts](https://support.zendesk.com/hc/en-us/articles/5447837810714)
- [Configuring the conversation flow and composer location in
  tickets](https://support.zendesk.com/hc/en-us/articles/6070249202202)

## Creating a new layout

You can create a new layout by using a layout template or editing an existing layout.
You must be an admin to create custom layouts.

**To create a new layout**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_workspaces_icon.png)
   **Workspaces** in the sidebar, then select **Agent tools > Layouts**.

   A list of layouts appears.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/custom_layouts_list2.png)
2. Click **Create layout**.

   A new layout appears in layout builder with a default set
   of components.
3. Enter a **Name** and **Description** for your layout.
4. If you want to make this new layout the [default layout](https://support.zendesk.com/hc/en-us/articles/5447837810714#topic_dl4_nmp_qwb), click **Set as default
   layout**.

   This will apply the custom layout for all your agents. Otherwise, leave it
   unchecked.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/custom_layout_set_default.png)
5. Click **Customize layout**.

   To customize your layout, you can:

   - Add or remove components. See [Adding and removing components in a layout](#topic_tb4_tcv_qwb).
   - Resize and move components. See [Resizing and moving components in a layout](#topic_nrx_tcv_qwb).
   - Stack components. See [Stacking components in a layout](#topic_y3x_vcv_qwb).
   - Move components to the context panel. See [Managing components in the context panel](#topic_zyc_xcv_qwb).
6. When you're finished, click **Preview** to see how your layout looks with real ticket
   data.
7. When you're done creating your layout, **Save** your changes.

   If you want to set a
   custom layout for a specific brand, group of agents, set of ticket forms, and so
   on, you can assign it to a [contextual workspace](https://support.zendesk.com/hc/en-us/articles/4408833498906-).

## Adding and removing components in a layout

As you create your new layout, you can choose which components to include.
Components can include *system* components and *optional* components.

- **System components**: Components that are integral to the ticket layout
  and cannot be removed, but they can be moved to the context panel. This includes the
  conversation thread, customer context, and ticket fields.
- **Optional components**: Components you can include in a layout, but are
  not required. This includes Zendesk apps, such as Knowledge and side conversations, or
  third-party applications. You can include these optional components anywhere in the
  layout, inside or outside of the context panel.

  You can use layout builder to remove third-party apps. To remove Zendesk apps, you need to turn them off using [context panel configuration settings](https://support.zendesk.com/hc/en-us/articles/4408828503450) in Admin Center, which
  will remove them from all layouts in your account.

When you open the layout builder, the Components area on the right side of your
screen represents all the components available for you to create custom layouts .

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/layout_builder_component_area.png)

**To add components to a layout**

1. Open a layout for [editing](https://support.zendesk.com/hc/en-us/articles/5447837810714#topic_rsb_zlp_qwb).
2. Refer to the **Components** area of layout builder.

   This area shows components you
   can add to the layout.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/custom_layout_add_components2.png)
3. Select the component you want to add, then drag and drop it into the layout.

   You can drag the component into an empty section of the layout to add it, or
   you can drag it over an existing component to replace it.

   You can also
   click the Add icon (+) next to the component to add it.
4. After you add the component, you can make changes to the component by rearranging it
   within the layout, resizing it, or making other updates.

   See [Resizing and moving components in a layout](#topic_nrx_tcv_qwb).
5. When you’re finished, **Preview** the layout and **Save** your changes.

**To remove a component**

To free up room in your layout, you can resize or remove components. You cannot
remove system components from a ticket layout, but you can move them into the context panel.

1. Open a layout for [editing](https://support.zendesk.com/hc/en-us/articles/5447837810714#topic_rsb_zlp_qwb).
2. In the layout canvas, select the component you want to remove, then click the remove
   component icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/builder_icon_remove_component.png)).

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/layout_remove_component.png)

   You can also
   select the component, then drag to the bottom of the layout to remove it.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/layout_remove_component.gif)
3. Confirm the deletion, then **Save** your changes.

## Resizing and moving components in a layout

After you’ve added components to your layout, you can fine-tune the layout by making
adjustments.

**To adjust components in a layout**

1. Open a layout for [editing](https://support.zendesk.com/hc/en-us/articles/5447837810714#topic_rsb_zlp_qwb).
2. Select a component in the canvas area of the layout.

   A list of actions you can take
   on the component appears on the right side of the layout builder. See [Component actions](#topic_fm4_5bw_qwb).

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/builder_component_actions.png)
3. Click an action to change your component, including moving it, resizing it, or replacing
   it.

   You can also hover your mouse pointer over a component, then drag a resize handle
   (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/layout_resize_handle.png)) to resize it.
4. When you’ve finished editing components, **Save** your changes.

### Component actions

When you select a component, these are the actions you can take:

|  |  |  |
| --- | --- | --- |
| **Icon** | **Description** | **Actions** |
|  | Move left | Move the component to the left. |
|  | Move right | Move the component to the right. |
|  | Move down | Move the component down. Available for [stacked](#topic_y3x_vcv_qwb) components. |
|  | Move up | Move the component up. Available for [stacked](#topic_y3x_vcv_qwb) components. |
|  | Increase width | Increase the component width. |
|  | Decrease width | Decrease the component width. |
|  | Increase height | Increase the component height. |
|  | Decrease height | Decrease the component height. |
|  | Replace component | Select the component you want to replace, then select a new component from the Replace component drop-down. |
|  | Move to context panel | You cannot remove system components but you can move them to the context panel. |
|  | Remove component | Remove the component. |

## Stacking components in a layout

You can save layout space by stacking one component under another. You can have two
components in a stack.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/stacking_components.gif)

**To stack a component**

1. Open a layout for [editing](https://support.zendesk.com/hc/en-us/articles/5447837810714#topic_rsb_zlp_qwb).
2. Select the component you want to stack.
3. Drag the component below or above another component in the layout until a blue
   target icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/builder_icon_blue_target.png) ) appears.
4. Release the component.

   The components are stacked one under the
   other

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/stacked_components2.png)

   When
   a component is stacked, you can select the component and use the up or down arrows to
   increase or decrease the component height. You can also use the double up or down arrows
   to reorder components in the stack.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/stacking_actions2.png)
5. **Save** your changes.

**To unstack a component**

1. Open a layout for [editing](https://support.zendesk.com/hc/en-us/articles/5447837810714#topic_rsb_zlp_qwb).
2. Select a component in a stack.
3. Drag the component to the left or right of the stack until a blue target icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/builder_icon_blue_target.png)) appears.
4. Release the component.
5. **Save** your changes.

## Undoing and redoing layout changes

As you are creating your layout, you can undo a change you made. For example, if
you removed or swapped a component by mistake. You can undo and redo multiple changes, up
until the point where you first started editing the layout. After you save the layout, the
undo and redo stack is cleared until you make another change.

**To undo a change**

- Click the undo icon at the top of the layout.

  ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/layout_builder_undo.png)

**To redo a change**

- Click the redo icon at the top of the layout.

  ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/layout_builder_redo.png)

## Managing components in the context panel

When you create a layout, in addition to managing components in the main ticket workspace,
you can also use layout builder to manage components in the [context panel](https://support.zendesk.com/hc/en-us/articles/4408836526362). For example, you can move an application out of the
context panel and into the main ticket workspace to make it easier for agents to access.
Alternatively, you can move components into the context panel or remove them completely.

Note: To completely remove standard Zendesk components (Knowledge, Side conversations, and All
Apps), you must configure context panel settings in Admin Center. See [Configuring the context panel](https://support.zendesk.com/hc/en-us/articles/4408828503450).

**To manage components in the context panel**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_workspaces_icon.png)
   **Workspaces** in the sidebar, then select **Agent tools > Layouts**.

   A list of layouts appears.
2. Click the options menu icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/uc_options_icon.png)) next to the layout you want to edit, then select **Edit**
   from the options menu.

   The layout opens in layout builder.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/layout_builder_edit_context_panel2.png)
3. Click **Customize layout**.
4. In the **Components** area of the layout builder, click **Manage context panel.**

   Layout details for the context panel appear.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/layout_context_panel_edit2.png)
5. Make any of the following layout changes:
   - To add a component to the context panel, click + **Add component**,
     then select a component from the drop-down menu.
   - To move a component out of the context panel and into the main layout, click the
     **Move to layout** icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/builder_icon_move_to_layout.png))
   - To move a component out of the main layout and into the context panel, select the
     component in the main layout, then click the **Move to context panel**icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/builder_icon_move_to_context_panel.png)).
   - To select which component appears when you first open the context panel,
     select a component from the **Default selection** menu.
   - The **All components** list determines the order components appear in
     the context panel sidebar. To reorder the components, position your cursor over the
     grabber at the end of the component you want to reorder, then drag the component to
     another position within the component list.
   - To completely remove a component, select the component and click the
     remove icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/builder_icon_remove_component.png)).
6. **Save** your changes.