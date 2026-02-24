# Guide to prototyping in Figma

Source: https://help.figma.com/hc/en-us/articles/360040314193-Guide-to-prototyping-in-Figma

---

Before you start

Who can use this feature

 

Supported on [any team or plan](https://help.figma.com/hc/en-us/articles/360040328273-Plans-and-teams-in-Figma).

Anyone with can edit access can create prototypes.

Anyone with can view access can play back prototypes in Presentation view.

Figma’s prototyping features allow you to create interactive flows that explore how a user may interact with your designs.

Prototypes are a fantastic way to:

- Preview interactions and user flows
- Share and iterate on ideas
- Get feedback from collaborators
- Test interactions with users
- Present your designs to stakeholders

Watch our video on prototyping below. Or, check out our [Prototype & Collaboration Playlist](https://www.youtube.com/playlist?list=PLXDU_eVOJTx7aqRW3Skp1aRT9ktC3ctqA) on Youtube.

**Tip!** For an even more efficient workflow, you can quickly toggle between the **Design** and **Prototype**tabs using the keyboard shortcut `Shift` `E`.

## Flows and starting points

With prototyping in Figma, you can create multiple flows for your prototype in one page to preview a user's full journey and experience through your designs.

A flow is the network of frames and connections in a single page. A prototype can map out a user's entire journey through your app or website, or it can focus on a specific segment of it via its own flow. For example: your prototype covers all possible interactions on an eCommerce site. Within the prototype, you have flows for creating an account, adding items to a cart, and checking out.

Figma creates a flow starting point when you add your first connection between two frames. There are a few other ways to add a flow starting point to your prototype:

- With the starting frame selected, click in the **Flow starting point** section of the right sidebar.
- Right-click on the frame, then click **Add starting point**.
- Duplicate a frame with an existing starting point.

When it's time to test your designs, you can share the entire prototype or [copy the link to a flow starting point](https://help.figma.com/hc/en-us/articles/360039823894).

**[Learn more about starting points and flows →](https://help.figma.com/hc/en-us/articles/360039823894)**

Note: A top-level frame can be part of multiple flows, but can only have one starting point. Frames nested within a top-level starting frame can have connections that navigate the user around multiple flows. For example, Log in and Sign up buttons can be nested in the same starting point frame, then be connected to frames in separate flows for each experience.

## Create connections

1. Select the hotspot for the connection.
2. Click to create the connection.
3. Drag it to the destination.
4. If there are no existing connections, Figma will make the first frame a starting point.

![Anatomy of a connection between two frames](https://help.figma.com/hc/article_attachments/4404146549271)

Tip! You can create connections from multiple objects to the same destination frame at the same time—saving you time and effort when building out your prototype flows. To do so, select multiple starting hotspots on your canvas, then click and drag the icon to the destination.

**[Learn more about creating and editing connections in bulk →](https://help.figma.com/hc/en-us/articles/360040315773-Prototype-interactions-and-animations)**

## Create interactions and animations

1. Open the **Prototype** tab in the right sidebar
2. Add **interactions**
3. Set interaction details
4. Apply an **animation**
5. **Preview** your animation

![Create interactions and animations](https://help.figma.com/hc/article_attachments/4404153733655)

## Adjust prototype settings

1. Select a **Device** and **Model**
2. **Preview** your prototype
3. Select **Background** color
4. Set the prototype's **Starting Frame**

![Prototype tab of right sidebar with device preview background and flow settings](https://help.figma.com/hc/article_attachments/4404153736087)

## Learn more about prototyping

### Get started

- [Create prototype interactions and animations](https://help.figma.com/hc/en-us/articles/360040315773)
- [Select a starting point for your prototype](https://help.figma.com/hc/en-us/articles/360039823894)
- [Customize your prototype device](https://help.figma.com/hc/en-us/articles/360039823894)
- Prototype [actions](https://help.figma.com/hc/en-us/articles/360040035874), [triggers](https://help.figma.com/hc/en-us/articles/360040035834) and [animations](https://help.figma.com/hc/en-us/articles/360040522373)

### Advanced interactions

- [Create overlays in your prototypes](https://help.figma.com/hc/en-us/articles/360039818254)
- [Create advanced animations with Smart Animate](https://help.figma.com/hc/en-us/articles/360039818874)
- [Prototype scroll interactions with overflow behavior](https://help.figma.com/hc/en-us/articles/360039818734)
- [Add video to prototypes](https://help.figma.com/hc/en-us/articles/8878274530455)
- [Add animated GIFs to prototypes](https://help.figma.com/hc/en-us/articles/360041486873)
- [Use variables in prototypes](https://help.figma.com/hc/en-us/articles/14506587589399)
- [Use expressions in prototypes](https://help.figma.com/hc/en-us/articles/15253194385943)
- [Multiple actions and conditionals](https://help.figma.com/hc/en-us/articles/15253220891799)
- [Variable modes in prototypes](https://help.figma.com/hc/en-us/articles/15253268379799)

### Share and collaborate

- [View prototype connections](https://help.figma.com/hc/en-us/articles/4411431245335)
- [Set prototype presentation view options](https://help.figma.com/hc/en-us/articles/360040318013)
- [Share your prototype](https://help.figma.com/hc/en-us/articles/360039822654)
- [View prototypes on a mobile device](../view-prototypes/view-prototypes-on-a-mobile-device.md)
- [Give feedback on prototypes with comments](https://help.figma.com/hc/en-us/articles/360039824594)

## Glossary

- A **hotspot** is where the Interaction takes place. A hotspot can be any object within the original frame, such as a link, button, image or icon, etc.
- **Connections** are the blue arrows or "noodles" that connect the hotspot to the destination. We apply the interaction and animation settings via the connection.
- A **flow** is the network of connected frames that form a path through a prototype. Each flow has its own **starting point**. You can have multiple flows within a prototype.
- The**starting point** is the first frame of a flow. Set multiple starting points to show different flows of the prototype in Presentation view.
- The **trigger** determines what type of interaction with the hotspot will cause the prototype to advance. This could be a mouse or touch interaction, such as a tap, drag, click, hover, etc.
- The **destination** is where the transition ends. This must be a top-level frame - a frame that is added directly to the canvas - and not an object within a frame. If we think of moving from A to B, **A** is the hotspot and **B** is the destination.
- The **action** defines the type of progression is occurring in the prototype. For example, the action could be to navigate to another frame, or open an external URL.
- The **animation** settings determine how the prototype moves from one frame to the other. You can control the type of animation, as well as the speed and direction.
- A **transition** is the type of animation. This defines how the action moves to the destination.
- The **direction** controls the direction that the transition comes from. Choose between left, right, top or bottom.
- The **duration** controls the time it takes to complete the animation. The shorter the duration, the faster the transition. Select a duration between 1ms and 10000ms (10 seconds).
- **Easing** affects the acceleration of the animation—whether it starts slow or fast. This allows you to build animations that feel more natural.
- **Overlays** are frames that appear above the current screen or frame. You can use overlays to create tool-tips, interactive menus, alerts, or confirmations.
- **Overflow behavior** allows you to define how your prototype responds to scrolling. This allows you to create more advanced user interactions, such as carousels, galleries, or interactive maps.
- Choose which **device** will be shown when presenting your prototype. Define both the device and the model.
- The **background color** lets you define the color in the background of your prototype.
- If you have a prototype with portrait and landscape frames, you can select an **orientation**. The orientation is set for the entire prototype. It's not possible to switch between portrait and landscape view within a prototype.
- A **preview** will show you how something will look or work in the prototype. We show previews for both **animations** and prototype **device** settings.