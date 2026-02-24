# Use code snippets in Dev Mode

Source: https://help.figma.com/hc/en-us/articles/15023202277399-Use-code-snippets-in-Dev-Mode

---

Before you Start

Who can use this feature

Available on [all paid plans](https://help.figma.com/hc/en-us/articles/360040328273)

Requires a [Full or Dev seat](https://help.figma.com/hc/en-us/articles/360039960434)

Users on the Organization or Enterprise plans with a Full or Dev seat can also access Code Connect snippets

Code snippets appear in Dev Mode’s Inspect panel when an object is selected on the canvas. The **Code** section provides relevant component details and generates code based on the selection and language preferences set in Inspect:

- When text is selected, the **Code** section displays a typographic preview, followed by layout, typography, and content information.
- With all other selections, a box model is displayed with margin, border, and padding details, along with layout and style information.

**Note:**  You can use Figma’s [Code Connect](#h_01HV7C474N11MGDBSTMP1A13MJ) tool to customize code snippets for design system components. With Code Connect, developers will see connected design system code from their libraries instead of auto-generated code when inspecting components in Dev Mode.

[Learn more about implementing Code Connect in our API docs →](https://www.figma.com/developers/code-connect)

# Set language preferences

You can choose a preferred language and unit for code snippets in the **Code** section of the Inspect panel. These settings apply to all generated code snippets for objects selected on the canvas.

To set a default language and unit:

1. Deselect all objects on the canvas.
2. Select an option from the **Language** dropdown:
   - **CSS** (Web)
   - **SwiftUI** or **UIKit** (iOS)
   - **Compose** or **XML** (Android).
3. From the **Unit** dropdown, select a unit. Available units depend on the language selection.

## Change language and unit preferences

Once you have an object selected, you can override the default language and unit.

1. In the **Code** section, select a language from the dropdown.
2. Select a unit under Settings in the dropdown menu.

## Set unit scale

Unit scaling allows you to set unit dimensions relative to a specified size. For example, you can set a root font size for CSS rems, or set a scale factor for scaling dimensions into iOS points.

To adjust the unit scale for your selected language and unit:

1. Select an object on the canvas.
2. In the **Code** section of the Inspect panel, click [inspect settings icon] **Inspect settings** next to the language dropdown.
3. Select **Set unit scale…**
4. Depending on the unit preference, enter or select the scale in the **Unit scale** modal.
5. Click .

### Supported unit types by platform

**CSS**

- **px:** Logical pixels defined by the browser.
- **rem:** Relative to the root font size (e.g. `1rem = 16px` by default).

**iOS**

- **px:** Canvas pixels.
- **pt:** Resolution-independent points used in UIKit and SwiftUI.

**Android**

- **px:** Physical screen pixels.
- **dp (density-independent pixels):** Scales consistently across screen sizes.
- **sp (scale-independent pixels):** Like dp, but also scales with the user’s font size preferences (used for text).

# 

# View code snippets

Code snippets are generated when you select an object on the canvas while in Dev Mode. The **Code** section displays relevant information depending on the type of object and language selected.

While most objects on the canvas will generate similar code snippets, text selections vary slightly. The Code section will display a typographic view instead of a box model, followed by code snippets of relevant typography information.

Any variables assigned to a selected object will also appear in the code snippet. Code syntax allows you to represent variables in code using valid variable names to support a seamless handoff experience.

[Learn more about code syntax and variables in Figma Design ->](https://help.figma.com/hc/en-us/articles/15339657135383)

Tip: You can extend the functionality of code snippets with plugins or create custom code snippets for development using Figma’s Plugin API.

## Copy code snippets

You can copy a code snippet and transfer it to a text editor. To copy a code snippet:

1. Select the object you want to generate code for.
2. Find the code snippet you want to copy under the **Code** section of the Inspect panel.
3. Hover over the code snippet and click **Copy** in the top-right corner.

## Code Connect

Code Connect is a tool for design systems and engineering teams to bring component code into Dev Mode. When inspecting a component with connected code snippets, developers will see design system code from their libraries instead of auto-generated code.

Code Connect builds on the Figma API and is fully customizable to support multiple design systems, products, and languages.

[Check out the Code Connect hub to learn how to sync custom code snippets to components →](https://help.figma.com/hc/en-us/articles/23920389749655)

Once Code Connect is implemented, your Dev Mode code snippets will say **connected** and will show snippets from your organization’s library.