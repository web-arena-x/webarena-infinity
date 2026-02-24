# Add, select, and edit objects across multiple breakpoints

Source: https://help.figma.com/hc/en-us/articles/31242788601879-Add-select-and-edit-objects-across-multiple-breakpoints

---

Figma Sites was released in [open beta](https://help.figma.com/hc/en-us/articles/4406787442711) at Config 2025. [Learn more about what’s included in the beta.](https://help.figma.com/hc/en-us/articles/4406787442711)

Who can use this feature

Available on [all plans](https://help.figma.com/hc/en-us/articles/360040328273)

Requires edit access to the file

If your webpage uses more than one breakpoint, you can add, select, and edit objects across all breakpoints simultaneously.

## Understanding primary and secondary breakpoints

![Animation showing a cursor selecting and changing an object on a desktop layout, mirroring the action on a mobile layout.](https://help.figma.com/hc/article_attachments/31918969283863)

Every new webpage starts with a **primary breakpoint**—usually the desktop breakpoint.

When you add additional breakpoints, any changes made to objects in the primary breakpoint cascade to the other—secondary—breakpoints. In contrast, changes made in a secondary breakpoint apply only to that specific breakpoint.

For example, if you drag a hero section into a primary breakpoint, it will immediately appear in all secondary breakpoints. If you add the hero section to a secondary breakpoint, it will only appear on that breakpoint.

This behavior applies to adding, selecting, and editing objects.

### Change the primary breakpoint

The desktop breakpoint is set as the primary breakpoint by default, but you can change it at any time. This is useful if you prefer to use a different screen size as the base of your design, like when taking a mobile-first approach. Changing the primary breakpoint won’t change the order of the breakpoints in the webpage—you’ll just see the **Primary** label switch to the new breakpoint.

To change the primary breakpoint:

1. Right-click a non-primary breakpoint in a webpage.
2. Select **Set as primary breakpoint**.

## Add an object to multiple breakpoints

What happens when you add an object to a webpage with multiple breakpoints depends on whether you add it to a primary or secondary breakpoint.

![Cursor dragging an object into the primary desktop breakpoint, also appearing in tablet and mobile breakpoints.](https://help.figma.com/hc/article_attachments/31918969284503)

**Add to the primary breakpoint**

When you add an object to the primary breakpoint, it is automatically added to all secondary breakpoints.

![Cursor dragging "Earthling" into the tablet breakpoint; absent in desktop and mobile breakpoints.](https://help.figma.com/hc/article_attachments/31918969284887)

**Add to a secondary breakpoint**

When you add an object to a secondary breakpoint, it is visible on that specific breakpoint and hidden in the other breakpoints. This helps maintain a shared hierarchy in the webpage.

**Tip**: Instead of adding and then manually tweaking a design across multiple breakpoints, you can add a [responsive component](https://help.figma.com/hc/en-us/articles/31242826664983) that automatically matches the right variant to its corresponding breakpoint.

## Select a matching object across breakpoints

Like adding an object, what happens when you select an object in a webpage depends on whether you select it in the primary or secondary breakpoint.

![Cursor clicking an object on the desktop layout and the same object is also selected on tablet and mobile views.](https://help.figma.com/hc/article_attachments/31918972970903)

**Select an object in the primary breakpoint**

When you select an object in the primary breakpoint, Figma automatically selects matching objects in all secondary breakpoints.

**Tip**: If you want to select an object on the primary breakpoint without selecting its matching layers in other breakpoints, turn off **Always select matching layers** at the top of the right sidebar. This limits your selection to the primary breakpoint only.

![Cursor clicking on an object in the tablet layout; no selections in other breakpoints.](https://help.figma.com/hc/article_attachments/31918969287063)

**Select an object in a secondary breakpoint**

When you select an object in a secondary breakpoint, Figma only selects the object in that breakpoint.

**Tip**: If you select an object on a secondary breakpoint and want to select its matching layers in other breakpoints, click **Select matching layers** at the top of the right sidebar.

## Edit an object across breakpoints

What happens when you edit an object across breakpoints will depend on whether the object has been previously edited on a secondary breakpoint.

When you edit an object in the primary breakpoint, Figma checks each of the object’s properties.

- If a specific property has been modified in a secondary breakpoint, an edit in the primary breakpoint will only apply in breakpoints where that property hasn’t been modified.
- If the property hasn’t been modified in a secondary breakpoint, the edit will apply across all breakpoints.

### Example

![Animation showing three squares on desktop, tablet, and mobile views, illustrating property overrides across the breakpoints.](https://help.figma.com/hc/article_attachments/31918972973335)

Suppose you have a frame in desktop, tablet, and mobile breakpoints.

1. Change the fill color of the frame in the mobile breakpoint.
2. Then change the fill color in the primary (desktop) breakpoint.

Notice the updated fill color will only appear in the desktop and tablet breakpoints because the mobile breakpoint’s fill property was previously modified.

Other changes to the frame—like adjusting its height in the primary breakpoint—will apply across all breakpoints, because the height property has not been overridden in any secondary breakpoints.

**Tip**: If you’ve edited an object in a secondary breakpoint and want it to match the primary breakpoint version again, right-click on the object and select **Reset all changes.** The object will inherit edits on the primary breakpoint for all the reset properties once more.

### Some things to be aware of when editing an object on the secondary breakpoints

Behind the scenes, Figma tries to keep layer organization consistent between all the breakpoints. This means there are some extra restrictions to keep in mind when editing on a secondary breakpoint:

- Deleting objects in a secondary breakpoint will just hide it. You can find hidden objects in the layers panel with the **hidden** icon.
- It’s not possible to move a layer into or out of other layers from a secondary breakpoint. Grouping or framing objects is not supported from a secondary breakpoint.
- You cannot move a layer out of the webpage from a secondary breakpoint.