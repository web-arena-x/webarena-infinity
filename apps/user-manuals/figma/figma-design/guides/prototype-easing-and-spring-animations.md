# Prototype easing and spring animations

Source: https://help.figma.com/hc/en-us/articles/360051748654-Prototype-easing-and-spring-animations

---

Before you start

Who can use this feature

 

Available on [any plan](https://help.figma.com/hc/en-us/articles/360040328273-Plans-and-teams-in-Figma).

Anyone with can edit access can create prototypes.

New to Prototyping? Check out our [Getting Started with Prototyping](guide-to-prototyping-in-figma.md) guide.

Prototypes have many moving parts. Add easing and spring animation presets, or customize the easing of transitions, to communicate movement, emotion, and make your prototype more like the real thing.

Easing determines the acceleration of the transition between a starting frame and its destination, also known as keyframes, by using a mathematical function. Keyframes can be two frames in an interaction, like the transition from one screen to another, or the beginning and end states of a single frame, like an object changing color.

In the example animations below, easing is represented by a curve on a graph where time is applied to the x axis and the transition, such as Move In, Slide, or Smart Animate is on the y axis. The keyframes are represented by the beginning and end points of the line of curve in the graph.

[Learn more about adding interactions to prototypes.](https://help.figma.com/hc/en-us/articles/360040315773)

Tip: Hover over the preview window in the **Interaction details** modal to see a preview of your animation.

## Easing Bezier presets

### Linear

This is the default acceleration and is applied in a constant straight line. As objects in nature rarely move at a constant speed, linear curves can look unnatural or robotic.

![Linear easing animation example with a constant straight line graph, showing motion at uniform speed.](https://help.figma.com/hc/article_attachments/360084136913)

### Ease In

Creates an animation that starts slowly and accelerates as it reaches the end of its duration. This works well for smoothly transitioning objects out of view. One downside is it can feel sluggish.

![Ease In curve illustration showing animation acceleration from slow start to fast end, with a Bezier graph on the right.](https://help.figma.com/hc/article_attachments/360084136973)

### Ease Out

Ease Out is the opposite of an **Ease In** curve, where the animation starts fast and slows down as it reaches the end of its duration. It works well for moving objects into view and reinforcing important visual information.

![Animation demonstrating Ease Out curve with a graph showing a fast start and slowing end.](https://help.figma.com/hc/article_attachments/360082959854)

### Ease In And Out

Starts the animation slowly, accelerates in the middle, and slows at the end of its duration. For most motion, it feels smooth and responsive, but can feel unnatural or too perfect when applied to everything.

![Animated circle demonstrates Ease In and Out easing curve, showing smooth start and end transitions on a graph.](https://help.figma.com/hc/article_attachments/360082959894)

### Ease In Back

**Ease In Back** is when the animation goes past the initial keyframe’s value and then accelerates as it reaches the end. This creates a bounce in the animation that serves as an anticipatory action, preparing the audience for and reinforcing the main action. Much like **Ease In**, **Ease In Back** can work well for smoothly transitioning objects out of view.

![Animation of a circle moving out of view with an Ease In Back curve, showing a bounce past the initial keyframe on a graph.](https://help.figma.com/hc/article_attachments/360082959834)

### Ease Out Back

Is the opposite of **Ease In Back**. The animation starts fast, then slows and goes past the ending keyframe's value. This creates a bounce in the animation that serves as a settle that creates a smooth ending transition for the main action. Similar to **Ease Out**, **Ease Out Back** works well for moving objects into view.

![Ease Out Back animation graph showing bounce effect as the object slows and passes the ending keyframe’s value.](https://help.figma.com/hc/article_attachments/360084136933)

### Ease In And Out Back

Starts the animation slowly as it overshoots the initial keyframe’s value, then accelerates quickly before it slows and overshoots the ending keyframes value. This creates an anticipatory bounce at the start, a quick motion, with a rebounding motion before the final state.

![Animation illustrating the "Ease In And Out Back" curve with a graph showing anticipatory bounce and rebounding motion.](https://help.figma.com/hc/article_attachments/360084136953)

## Custom easing Bezier

Select the **Custom bezier** option from the Curve menu to manually set and adjust easing values. Figma will show a graph, or Bézier curve editor, based on the preset you have previously selected.

You can use the Bézier curve editor to adjust the curve of an existing preset, or to create an easing curve of your own.

You can copy and paste numerical values to other interactions to replicate easing. It's not possible to save a custom easing curve for future use.

1. A cubic Bézier curve is defined by four points. These points are represented by the square perimeter in the graph.
2. The graph's axes represent a curve on a graph where time is applied to the x axis and the transition, such as Move In, Slide, or Smart Animate is on the y axis.
3. There are two keyframes that indicate the start and end state of the animation. These are fixed at `0,0` and `1,1`. Click the keyframe to reset the Bézier handles.
4. A continuous curve shows the object's values over the duration of the animation. This is the easing curve.
5. The adjustable handles allow you to change the values of the curve. If you're customizing an easing curve with no handles, click and drag the keyframe to activate the handles.
6. You can use this field to enter numerical values.

![Custom Bezier curve settings in Figma interaction panel, illustrating graph adjustments for easing values.](https://help.figma.com/hc/article_attachments/31145916828567)

Tip! You can use these numerical values when translating the Bézier curve to CSS notation: `cubic-bezier(x1, y1, x2, y2)`

Note: It's possible to extend the curve beyond the graph's dashed perimeter. You can use this to create an anticipatory bounce at the beginning, or a rebounding effect at the end of the animation. The [**Ease In and Out Back**](#h_01EF10YAE8MPP9YBSPS41WKZC8) preset shows both of these effects in action.

## Spring animation presets

Combine spring animations with Figma’s animated transitions.

![Spring animation diagram with a graph showing a curve representing bouncing motion dynamics in Figma.](https://help.figma.com/hc/article_attachments/5983821900695)

You can pick from the following presets or create your own:

- **Gentle**: A gentle animation is the most neutral option of the spring curves. Great for subtle spring movement when scaling content.
- **Quick**: A bit more spring great for toasts and notifications.
- **Bouncy**: A quirky preset for delightful animations like a heart bounce.
- **Slow**: A steady, natural way to scale up fullscreen content.
- **Custom**: Set your own spring animation curves ↓

## Custom spring curves

Customize your spring animation by editing the **Stiffness**, **Damping**, and **Mass** values in the **Interaction details** modal and by dragging the animated graph.

![Custom spring animation settings in Figma's Interaction panel with adjustable stiffness, damping, and mass values.](https://help.figma.com/hc/article_attachments/31145900307223)

- **Stiffness:** influences the number of “bounces” in the animation and can be adjusted by dragging the graph.
- **Damping:** influences the level of spring in the animation and can be adjusted from the graph.
- **Mass:** influences the speed of the animation and height of the bounce. You’ll need to manually adjust the value in the **Mass** field. Adjusting mass also changes the millisecond value for the duration setting.

You can copy and paste numerical values to other interactions to replicate spring animation curves. It's not possible to save a custom curve for future use.

[Learn how to create interactions and adjust animations.](https://help.figma.com/hc/en-us/articles/360040315773)