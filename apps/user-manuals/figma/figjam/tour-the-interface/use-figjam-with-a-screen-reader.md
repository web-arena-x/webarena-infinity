# Use FigJam with a screen reader

Source: https://help.figma.com/hc/en-us/articles/14477051168791-Use-FigJam-with-a-screen-reader

---

Before you start

Who can use this feature

Supported on [any team or plan](https://help.figma.com/hc/en-us/articles/360040328273-Plans-and-teams-in-Figma).

Anyone with `can edit` access can add objects to the board.

New to FigJam? Check out our [Guide to FigJam](https://help.figma.com/hc/en-us/articles/1500004362321).

You can navigate and edit a FigJam file using a screen reader on a desktop device.

- Move focus around the board, its objects, and their menus
- Read the content of objects like sections, stickies, shapes, and alt text
- Create and edit objects and their contents

[Learn how to create accessible FigJam boards →](https://help.figma.com/hc/en-us/articles/14477101678359)

## Screen reader settings

The FigJam board is not screen reader accessible by default. To enable accessibility:

1. Open the quick actions menu by pressing `⌘Command``/` or `⌘Command``P` on a Mac or `Control``/` and `Control``P` on Windows.
2. Type “Accessibility settings” and press `Return`/`Enter`.

This will open the accessibility settings dialog, where you can enable the FigJam board contents to be accessible.

Note: To make the FigJam board accessible, we rely on certain web HTML types. To that end, make sure your screen reader will read groups, regions, headings, and text.

## Navigate a FigJam file

A FigJam file has several top-level regions. Use keyboard shortcuts to cycle focus throughout them:

Focus next region:

- Mac: `F6`
- Windows: `Control``F6`

Focus previous region:

- Mac: `⇧Shift``F6`
- Windows: `Shift``Control``F6`

Regions are ordered as such:

- **Board**: This is the FigJam board itself, which contains objects like sections, stickies, and text
- **Selection properties menu**: This region is rendered if there is an object selected on the board, with buttons to modify various properties (font, color, etc.) of the selection. If there is nothing selected on the board, this region is not available and is skipped when cycling through objects.
- **Top left panel**: A toolbar containing a collapsible  main menu, file name, and [page creation and navigation](https://help.figma.com/hc/en-us/articles/24005082123159). The first button is the Figma menu. To navigate the main menu, use `↑` and `↓` keys, `Enter` or `Space` to select a menu object or open a submenu, and `Tab` to close a submenu.
- **Top right panel**: A toolbar containing entry points for multiplayer tools ([spotlight](https://help.figma.com/hc/en-us/articles/5025214483351), [audio calls](https://help.figma.com/hc/en-us/articles/1500004414622)), [FigJam AI](https://help.figma.com/hc/en-us/articles/18706554628119), [templates](https://help.figma.com/hc/en-us/articles/1500004414082), [comments](https://help.figma.com/hc/en-us/articles/1500004290941), meeting tools ([timer](../run-meetings/stay-on-track-with-the-timer-in-figjam.md#01H8M5H8K84D10PPQDRVXPJSBA), [music](../run-meetings/stay-on-track-with-the-timer-in-figjam.md#01H8M5H8K852G65TRD7BHE5HQP), and [voting](https://help.figma.com/hc/en-us/articles/9359912208663)), and [sharing](https://help.figma.com/hc/en-us/articles/360040531773).
- **Creation tools**: A toolbar with buttons to switch your current creation tool. This toolbar is primarily meant to be used with a mouse, so for keyboard-only users, we recommend creating nodes using the [quick actions menu](https://help.figma.com/hc/en-us/articles/360040328653) by pressing `⌘Command``/` or `⌘Command``P` on a Mac or `Control``/` and `Control``P` on Windows.
- **Bottom right region**: Use the  and  to adjust your zoom of the board. This region also includes the Help Widget, a collapsible menu with a  containing resources and references for using FigJam like the Figma Help Center and keyboard shortcuts.

## Navigate the board

The board contains all the content from you and your collaborators. Objects like stickies, shapes, and images can be placed anywhere on the 2D board, and can be organized with sections. Objects placed inside a section are considered children of that section, and siblings of each other. All objects placed directly on the board (and not nested within sections) are also considered siblings of each other.

Navigate objects by selecting them with the keyboard shortcuts:

- `Tab` to select the next sibling object
- `⇧Shift``Tab` to select the previous sibling object
- If you’re editing text, `Tab` will select the next editable text field on the board

Note

Tabbing will not select objects in different hierarchies.

- Press `Return`/`Enter` to select all the children of the currently selected parent object.
- Press `Shift``Return` / `Enter` to select the parent of the currently selected child object.

## Add objects to the board

Add objects to the board via the quick actions menu. Quick actions allow you to update settings and perform actions, using just your keyboard. This includes actions and settings that don’t have keyboard shortcuts.

Access the quick actions menu by pressing `⌘Command``/` or `⌘Command``P` on a Mac, or `Control``/` or `Control``P` on Windows.

Note

The shortcut for accessing the quick actions menu varies by keyboard layout. [Learn more about using the quick actions menu →](https://help.figma.com/hc/en-us/articles/360040328653-Use-shortcuts-and-quick-actions#Quick_actions)

To create an object, type “Create new <object type>” in the quick actions menu and press enter. For example, to create a new sticky note, type “Create new sticky note” and press `Return`/`Enter`.

The new object will be created in the center of the screen, or if a section is selected, in the center of that section.

If you have an object selected, you can also press `⌘Command``Return`/`Control``Enter` to create a new instance of that object next to the original.

Tip

When you open quick actions, you’ll see the last three actions you performed during that session. Recent actions reset when you close the tab or leave the file. Use the `↑` and `↓` keyboard shortcuts to cycle between recent actions, then press `Return`/`Enter` to perform them again.

## Add stamps and comments

You can create stamps and comments, which are objects that are attached to another object.

### Stamps

Press `E` to activate the stamp wheel. You can then focus a particular stamp, and press `Return`/`Enter` to activate stamping mode with that stamp. Use `Tab` to select an object on the board, then press `⌘Command``Return`/`Control``Enter` to place the stamp on the selected object. Stamps can only be added to selected objects. Press `Esc` to exit stamp mode.

[Learn more about using stamps →](https://help.figma.com/hc/en-us/articles/1500004290981)

### Comments

To add comments:

1. Select the object you want to comment on.
2. Press `⌘Command``/` or `⌘Command``P` on a Mac, or `Control``/` or `Control` `P` on Windows to open the quick actions menu.
3. Type **create new comment**.
4. Press `Return`/`Enter` to start composing your comment attached to your selection.
5. Press `Return`/`Enter` again to submit your comment.

[Learn more about comments in FigJam →](https://help.figma.com/hc/en-us/articles/1500004290941)

## Edit content

### Move objects

When an object is selected, use the arrow keys move it around the board. Use `⇧Shift` with arrow keys make the nudge movement larger.

### Edit text

For objects that allow for text editing (such as sticky notes, shapes with text, and plain text objects), select the object then press `Return`/`Enter` to start editing text. Press `Esc` to leave text editing, and return to selecting the object.

[Learn more about formatting text in FigJam →](https://help.figma.com/hc/en-us/articles/1500004291281)

### Edit properties

To edit a selected object’s properties, press `Fn``F6` on Mac or `Control``F6` on Windows to focus on the selection’s properties menu. The menu contains options to adjust properties like font, background color, and more depending on the selected object type.

## Features supported with screen readers

| Feature | Supported |
| --- | --- |
| Sections | ✓ |
| Stickies | ✓ |
| Shapes | ✓ |
| Tables | ✓ |
| Text objects | ✓ |
| Text formatting | ✓ |
| Links | ✓ |
| Comments | ✓ |
| Stamps | ✓ |
| Code blocks | ✓ |
| Audio calls | ✕ |
| Timer and music | ✕ |
| Stickers | ✕ |
| Spotlight | ✕ |
| FigJam on iPad | ✕ |
| Voting | ✕ |
| Emotes | ✕ |
| Connectors | ✕ |
| Lines | ✕ |
| Highlights | ✕ |
| Washi tape | ✕ |
| Cursor chat | ✕ |
| Widgets | ✕ |

Share your feedback

We're actively working on making FigJam more accessible. Let us know how we're doing in the [Figma Community Forum →](https://forum.figma.com/t/making-figjam-accessible-to-screen-readers/43380)