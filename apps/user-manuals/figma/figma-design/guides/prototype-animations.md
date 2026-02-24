# Prototype animations

Source: https://help.figma.com/hc/en-us/articles/360040522373-Prototype-animations

---

Before you start

Who can use this feature

 

Users on [any team or plan](https://help.figma.com/hc/en-us/articles/360040328273).

Users with can edit access can create prototypes.

New to Prototyping? Check out our [Getting Started with Prototyping](guide-to-prototyping-in-figma.md) guide.

Animations can be used to create smooth transitions between pages and define the behavior for actions like expanding a menu, swiping between pages, or opening a gallery.

## Instant

The Instant transition will immediately display the **Destination** Frame, when the hotspot is interacted with (clicked, hovered over, or pressed).

![Mobile interface showing a photo gallery app with albums previewed. The screen smoothly transitions between views.](https://d33v4339jhl8k0.cloudfront.net/docs/assets/5aa962fe2c7d3a2c4983093d/images/5c7edcba04286350d088aa24/file-ZurWTwFCqH.gif)

## Dissolve

The Dissolve transition will fade in the **Destination** frame, on top of the original frame.

Supports:

- Duration
- Easing

![Mobile interface showing albums with a dissolve transition effect, illustrating ease and duration settings.](https://d33v4339jhl8k0.cloudfront.net/docs/assets/5aa962fe2c7d3a2c4983093d/images/5c7eddb904286350d088aa2f/file-CE2Faj9XWB.gif)

## Smart Animate

Smart Animate looks for matching layers that exist across multiple frames. For layers that match, we recognize what's changed and apply transitions to seamlessly move between them.

Supports:

- Duration
- Easing

![Mobile app screen demonstrating a smart animate transition with matching layers in the navigation panel retaining their position.](https://s3.amazonaws.com/helpscout.net/docs/assets/5aa962fe2c7d3a2c4983093d/images/5d950b322c7d3a7e9ae1f7a2/file-aI3r9NOwPe.gif)

## Move In / Move Out

The Move transition will slide the **Destination** frame **into** or **out of** view, above the original frame.

Supports:

- Easing
- Direction
- Duration

![Transition demonstrating the Move feature with direction, easing, and duration, sliding the Destination frame onto the canvas.](https://d33v4339jhl8k0.cloudfront.net/docs/assets/5aa962fe2c7d3a2c4983093d/images/5c7edeab04286350d088aa38/file-0NUbcVCx2Q.gif)

## Push

The Push transition will push out the original frame, as the **Destination** frame is moved into view. This is the perfect transition for replicating a swiping gesture.

Supports:

- Direction
- Easing
- Duration

![Push transition animation demonstrating swiping effect, moving one album grid off-screen as the next slides in with direction and easing.](https://d33v4339jhl8k0.cloudfront.net/docs/assets/5aa962fe2c7d3a2c4983093d/images/5c7edfc82c7d3a0cb93242f4/file-KFVnV7nW0F.gif)

## Slide In / Slide Out

The Slide will move the **Destination** frame **into** or **out of** view. Slide will slowly offset the frame as it dissolves, while the Move transition keeps the original frame stationary.

Supports:

- Direction
- Easing
- Duration

![Slide transition moves and dissolves albums smoothly with direction, easing, and duration adjustments on mobile UI.](https://d33v4339jhl8k0.cloudfront.net/docs/assets/5aa962fe2c7d3a2c4983093d/images/5c7ee04d04286350d088aa49/file-7QvwXDb8s9.gif)

Tip! Use [prototype easing and spring animation curves](https://help.figma.com/hc/en-us/articles/360040315773) to give your animations a unique and natural feel.