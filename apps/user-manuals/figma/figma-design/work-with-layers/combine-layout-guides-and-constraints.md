# Combine layout guides and constraints

Source: https://help.figma.com/hc/en-us/articles/360039957934-Combine-layout-guides-and-constraints

---

Before you start

Who can use this feature

Available on [all plans](https://help.figma.com/hc/en-us/articles/360040328273)

Users with `can edit` to a file can use layout guides and constraints

**Note**: The Figma feature "layout grid" has been renamed to "layout guide" as of May 2025, and is a different feature from the [grid option in auto layout](https://help.figma.com/hc/en-us/articles/31289469907863).

**Constraints** allow you to define how objects react when you resize their parent frame. [Constraints](https://help.figma.com/hc/en-us/articles/360039957734) can control both an object's relative position and size.

**Layout guides** are visual aids that help you align objects within frames. When you use a [layout guide](https://help.figma.com/hc/en-us/articles/360040450513) within a frame, Figma aligns objects in that frame to the guide.

You can combine layout guides with constraints to create powerful and flexible layouts. This gives you more granular control over how objects respond as you resize them.

Layout guides can have **fixed** dimensions or **stretch** as you resize the frame. The type of layout guide will determine whether Figma prioritizes the guide or any constraints.

In our example below, we have applied **center** constraints to the plus icon in our cards. We can see how Figma determines that object's position, depending on the type of layout guide we use.

![Three side-by-side screens comparing stretch layout guide, fixed layout guide, and constraints only, highlighting layout differences.](https://help.figma.com/hc/article_attachments/31937313347863)

## Stretch layout guide

If your guide is set to **Stretch**, Figma will base an object’s constraints on the guide's nearest column or row.

**Stretch** layout guides adapt to the size of the frame. This allows your designs to respond when you resize the frame. Figma will set the **width** and **height** of the guide so that it corresponds to the frame size.

When you use stretch, Figma takes into account the object's constraints, relative to the layout guide.

In our example below, the cards in our design uses a stretch layout guide. Our left screen uses the frame preset for the iPhone 11 Pro, and the right uses the iPad Pro 11".

We can see that Figma has stretched the layout guide to match the card's new dimensions. We can also see that the plus icon is still in the center of the right guide column.

![Two screens show a stretch layout guide in Figma, adapting design elements for iPhone and iPad Pro dimensions.](https://help.figma.com/hc/article_attachments/360081519974)

## Fixed layout guide

**Fixed** layout guides let you choose how many columns and rows are in your guide. You can then define both the **width** of the columns and the **height** of the rows.

You can then fix the position of a fixed layout guide in the parent frame:

- **Row:** Fix the guide to the **top** or **center** of the frame.
- **Column:** Fix the guide to the **left** or the **center** of the frame.

When you use a fixed layout guide, Figma will honor constraints in relation to the frame and not the guide.

In our example below, the cards in our design use a fixed layout guide. Our left screen uses the frame preset for the iPhone 11 Pro, and the right uses the iPad Pro 11".

Our plus icon uses **center** constraints. We can see that Figma has set the object's position in relation to the frame and not the layout guide.![iPhone and iPad screens using fixed layout guides; plus icon centers within each card's frame, independent of guide.](https://help.figma.com/hc/article_attachments/360082650673)

**Tip**: You can nest frames within other frames for even greater control. This allows you to define different behavior between Frames or objects. 
 
If you’re familiar with HTML, this works like a **<div>** element works in a webpage. Learn more about [Grid Systems for screen design](https://www.figma.com/blog/grid-systems-for-screen-design/).