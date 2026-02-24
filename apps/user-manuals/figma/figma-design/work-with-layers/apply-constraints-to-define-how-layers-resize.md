# Apply constraints to define how layers resize

Source: https://help.figma.com/hc/en-us/articles/360039957734-Apply-constraints-to-define-how-layers-resize

---

Who can use this feature

Available on [all plans](https://help.figma.com/hc/en-us/articles/360040328273).

Anyone with `can edit` access can apply and edit constraints.

Constraints tell Figma how layers should respond when you resize their frames. This helps you to control how designs look across different screen sizes and devices.

You can check out the video below, or continue reading to find out more.

## Horizontal and vertical constraints

You can apply constraints along both the x (horizontal) and y (vertical) axis.

We set a layer's constraints to **Top** and **Left** by default.

### Horizontal

Horizontal constraints define how a layer behaves, as you resize the frame along the x axis.

- **Left** maintains the layer’s position, relative to the left side of the frame.
- **Right** maintains the layer’s position, relative to the right side of the frame.
- **Left and right** maintains the layer’s size and position relative to both sides of the frame. This may cause layers to grow or shrink along the x axis, when resized.
- **Center** maintains the layer’s position, relative to the horizontal center of the frame.
- **Scale** will define the layer’s size and position as a percentage of the frame's dimensions. It will then maintain those proportions as you resize it. 
    

 For example: The frame's width is 100px and the layer's width is 70px, so the layer takes up 70% of its parent frame. If we resize the frame to 200px wide, Figma will resize the layer to a width of 140px, 70% of 200px.

![Figma constraints panel showing X and Y position with Left and Scale settings selected.](https://help.figma.com/hc/article_attachments/25953942136599)

### Vertical

Vertical constraints define how a layer behaves, as you resize the frame along the y axis.

- **Top** maintains the layer’s position, relative to the top of the frame.
- **Bottom** maintains the layer’s position, relative to the bottom of the frame.
- **Top and bottom** maintains the layer’s size and position relative to the top and bottom of the frame. This may cause layers to grow or shrink along the y axis, when resized.
- **Center** maintains the layer’s position, relative to the vertical center of the frame.
- **Scale** will define the layer’s size and position as a percentage of the frame's dimensions. It will then maintain those proportions as you resize it.

![Position panel showing horizontal constraint set to "Scale" and vertical constraint set to "Top" with x and y values at 50.](https://help.figma.com/hc/article_attachments/25953923047447)

Note: Depending on the layer’s position, more than one constraint may achieve the same result.

## Apply constraints to a layer

You can apply constraints to any layer within a frame. It's not possible to apply constraints to layers outside of a frame, or layers in an [auto layout frame](https://help.figma.com/hc/en-us/articles/360040451373).

- You can also apply constraints to frames you have nested within other frames.
- You can apply both **horizontal** and **vertical** constraints to layers.
- You can't apply constraints to groups. A group will inherit its bounds from the layers contained within it. They aren't considered a single layer with bounds.

**Note:** If you apply constraints to a group, Figma applies constraints to the individual layers.

To set the constraints for a layer:

1. Select the layer or parent within the frame. The blue dotted line on the canvas shows which constraints are currently applied.
2. Click [icon] **Constraints** from the **Position** section of the right sidebar.
3. Adjust the vertical and horizontal constraints.
   - Use the drop down menus to set the layer's constraints.
   - Or, click on the lines in the interactive diagram to select a constraint.

**Tip!** Hold down `Shift` to select or apply more than one constraint at a time. For example: left and right constraints.

## Ignore constraints

Sometimes you may want to resize a frame or layer, without using the constraints that are applied to it. You can temporarily ignore any constraints applied to a layer by holding down a modifier key.

- **Mac:** Hold down `Command` when you resize
- **Windows:** Hold down `Ctrl` when you resize

**Constraints and layout guides**

Constraints give you a basic framework for positioning layers within a frame. When it comes to more complex designs, we need more precise control and flexibility. This ensures our designs behave when resized.

That’s where guides come into play. When you use a guide within a frame, Figma aligns any layers within the frame to that guide. Learn how to **[work with constraints and layout guides →](https://help.figma.com/hc/en-us/articles/360039957934)**