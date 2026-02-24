# Guide for screen reader users switching from Basic HTML view to Standard view in Gmail

Source: https://support.google.com/mail/answer/14297617

---

The default Standard view in Gmail has more features and usability improvements over Basic HTML view. In Standard view, Gmail is a web application with keyboard shortcuts to quickly perform actions and navigate the interface. A web application is when the application shortcuts are used to navigate and interact with the site, while a web page is when screen reader shortcuts (or commands) are used to navigate and interact with the page.

If you’re familiar with Gmail in Basic HTML view, use this guide to learn how to use Standard view in Gmail as a web page with your screen reader.

**Tips**:

- For help with Gmail in Standard view as a web application, visit [Use Gmail with a screen reader](90559-use-gmail-with-a-screen-reader.md).
- ChromeVox and VoiceOver can’t be customized to reliably use Gmail as a web page. If you use one of these screen readers, visit [Use Gmail with a screen reader](90559-use-gmail-with-a-screen-reader.md).
- If you prefer, you can use Gmail with an email client application that supports IMAP and POP, such as Outlook or Apple Mail.
  - [Learn how to read Gmail messages using IMAP](7126229-add-gmail-to-another-email-client.md).
  - [Learn how to read Gmail messages using POP](7104828-read-gmail-messages-on-other-email-clients-using-pop.md).

## Update your settings

If you use a screen reader with Basic HTML view, update your settings for Standard view.

### Use "Compact" view in Gmail

If you also use a screen magnifier, you can use a compact view of your Inbox that’s similar to Basic HTML view.

In the top header, to open the "Quick settings" menu, tab to the "Settings" button and press Enter. You can also use screen reader button navigation commands.

When "Quick settings" is open, tab to the radio buttons and choose "Compact."

## Update Inbox settings

To locate additional Inbox settings:

1. Open the "Quick settings" menu.
2. Tab (or Shift + Tab) to the "See all settings" button.
3. Press Enter.
   - This opens a page with more settings than Basic HTML view.
   - The focus is set to the "General" tab.
4. From "General," tab twice to the "Inbox" tab.
5. Press Enter.

### Remove Inbox categories

In the "Inbox" tab:

1. Use your screen reader virtual cursor or Browse mode to navigate checkboxes.
2. Press Space to uncheck:
   - "Promotions"
   - "Social"
   - "Updates"
   - "Forums"

After you remove Inbox categories, all emails are grouped in the primary Inbox.

Tip: If you prefer to group email into these categories, [learn how to set up Inbox categories](90559-use-gmail-with-a-screen-reader.md#categories).

### Turn off the reading pane

When focus is on a message in your conversation list, the reading pane shows the contents of a message. To improve responsiveness and simplify navigation, you should turn off the reading pane.

In the "Inbox" tab:

1. Tab to the "Enable reading pane" checkbox.
2. Press Space to uncheck.

### Turn off importance markers

If you leave importance markers on, the importance status is announced in Standard view, and adds an extra checkbox to the conversation list. Since importance markers weren’t announced in Basic HTML view due to default punctuation level reading, you may want to turn them off.

In the "Inbox" tab:

1. Tab to the "Show markers" radio button.
2. To select "No markers," press the down arrow.

### Save changes

After you update your Inbox settings, press Tab to the "Save changes" button and press Enter. Focus returns to the Gmail conversation list.

## Adjust screen reader settings

Modern screen readers automatically adjust to web applications like Gmail by following keyboard focus when it moves. While it may be helpful, it also disables the screen reader’s single letter keyboard shortcuts used for navigating Gmail as a web page.

To prevent your screen reader from automatically adjusting to Gmail:

- JAWS: Update settings to turn off Auto Forms Mode.
- NVDA: Update Browse mode settings to turn off responsiveness to focus and caret movement.

With these changes, you should still be able to use Gmail in Standard view as a web page with JAWS or NVDA.

For ChromeVox and Voiceover, to use Gmail as a web application, visit [Use Gmail with a screen reader](90559-use-gmail-with-a-screen-reader.md).

After you update these settings, your screen reader may reset its virtual or browse focus to the top of the page in Gmail. When this happens, navigate back to your previous location.

### Turn on & explore new keyboard shortcuts

To enhance your experience in Standard view, turn on and use keyboard shortcuts. Make sure the screen reader virtual cursor or Browse mode is off and that the focus isn’t on an edit field.

To display the keyboard shortcuts dialog in Gmail:

1. Press Shift + slash.
   - You may hear an alert about enabled or disabled keyboard shortcuts.
2. To navigate to the link named either "Enable" or "Disable," press Tab.
   - If the link says "Disable," keyboard shortcuts are available to use.
   - If the link says "Enable," press Enter to turn on keyboard shortcuts.

To open the list of keyboard shortcuts in a new window:

1. From the same page, press Tab to the link named "Open in a new window."
2. Press Enter.
   - This opens the help page titled [Keyboard shortcuts for Gmail](6594-keyboard-shortcuts-for-gmail.md).
   - There are several collapsible sections on the help page. To expand a section on the help page, navigate to the button with the section name and press Enter.

You can also explore the keyboard shortcuts dialog with your screen reader’s web reading commands:

- The content is presented in multiple tables, where the first column is the keyboard shortcut and the second column is the action it performs.
- Some of the shortcuts use punctuation characters. You may need to adjust your screen reader’s punctuation settings.
- You can also carefully review each shortcut by character.
- After the "Enable" / "Disable" link, you can find a list of shortcuts that you need to turn on to use. Many of these shortcuts are single letters that conflict with your screen reader’s web navigation. For example, the letter "X" toggles a selection of a conversation instead of the screen reader command to navigate by checkbox.

## Navigate Gmail in Standard view

Compared to Basic HTML view, there are some differences in how you navigate Gmail in Standard view.

### Conversation lists

Like your Inbox, conversation lists are presented in a table, with a checkbox in the first column of each conversation. However, the same information is now presented in more columns:

- "Star" follows the selection checkbox (where it was previously combined with the checkbox). Instead of navigating to "More actions," you can toggle the "Star" button directly in the column.
- Instead of showing as punctuation in the sender field, "Importance" follows "Star." If not disabled, you can toggle the "Importance" checkbox in the column.
- Instead of being combined with "Subject," "Attachment" follows "Subject."

To review another set of conversations like "Sent," "Drafts," or "All mail," you can use the screen reader command to navigate a list of links and then activate the corresponding link.

There are also web application keyboard shortcuts to directly navigate to:

- All mail: g, then a
- Sent: g, then t
- Inbox: g, then i

To learn more, visit [Use labels to organize mail](90559-use-gmail-with-a-screen-reader.md#uselabels).

### Navigate your conversations

Standard view still has checkboxes for each conversation item in a table, so the checkbox navigation still goes to each message. Checkbox navigation also reads the sender, the subject, the message snippet, and when the message was sent.

- To quickly scan your messages, navigate by checkbox instead of also navigating to the subject.
- To take action, toggle one or more checkboxes.
- Keep in mind that the unread status of a message is also read.

To open a conversation:

1. Use your screen reader’s "Next link" navigation to the subject.
2. To activate the link, press Enter.

### Use action buttons

Like in Basic HTML view, after checking one or more messages, a set of action buttons appears before the table of messages.

In Standard view, the action buttons don’t follow the table, and each conversation now has a button to "star" a message. To use these action buttons, navigate to the top of the table, then navigate previous buttons to get to the action buttons.

An easier way to perform actions on one or more messages:

1. To select the message, toggle the checkbox.
2. To open the context menu, press Shift + F10.
3. To select an action, in the menu, press Arrow down.
4. Press Enter.

Tip: Depending on your screen reader settings, after performing the action, you may have to toggle to virtual or Browse mode and navigate back to the table.

If you choose to "Label as" or "Move to" a label, focus moves to an entry field. Type the part of the label and then arrow down to matches, or keep typing for the full name of a new label. Or, you can press the Up arrow to the "Manage labels" option and create a new label.

### Read an email

Rather than using Tab then Enter to open an email with your screen reader, use the "next link" command and press Enter. The subject of the email is still a link, but it’s removed from the tab order to make navigating around the page easier.

If you navigate the conversation list as a web application, arrow down the conversation and press Enter to open the email.

To learn how to read new messages in a conversation with web application shortcuts, visit [Read an email](90559-use-gmail-with-a-screen-reader.md#reademail). The article also describes how to navigate and read those conversations as a web page.

### Reply to an email

When you read an email, at the top, there’s a "Reply" button that follows the sender heading. To forward, delete, or perform other actions on the email, tab over to the "More" button next to the "Reply" button and press Enter.

Important: "Quick reply" is no longer available in Standard view. There are now application-defined single letter shortcuts for reply, forward, and more, and the old shortcuts are no longer available.

### Address an email

When you reply, forward, or compose an email, there are multiple ways to add a new recipient. When focus is in the Search field, you can type part of a name or an email address and then arrow down to the matching person. The person can be from your contacts, collected addresses, or company directory.

- To move focus to the "CC" field, press the Ctrl + Shift + c shortcut.
- To move to the "BCC" field, press the Ctrl + Shift + b shortcut.

In the tab order, there are also "To", "CC", and "BCC" buttons that precede the Search fields. When you activate these buttons, it displays a "Select contacts" dialog that can be used to populate the field.

After you add a contact to the Search field, it’s transformed into a button that can be deleted or activated to modify. Rather than navigating through every character of the address, the left and right arrow keys navigate to each contact.

To emphasize that you added a recipient in the body of the message.

1. Enter a plus sign followed by a part of the name or email address.
2. Down arrow to the matching person.
   - The text you enter turns into a link and adds your recipient to the "To" line.

Tip: To add someone to the "CC" line, use the at-sign in place of the plus sign.

### Compose an email

For web application shortcuts, visit [Compose & reply to emails](90559-use-gmail-with-a-screen-reader.md#composereplyemails).

If you navigate Gmail as a web page, "Compose" is the first button in the "Navigation" landmark (region).

After you compose an email:

- To send the email, press Ctrl + Enter.
- To discard the draft, press Ctrl + Shift + d.

Below the message, "Send" and "Discard" are available as buttons. You can also access additional formatting option buttons between the "Send" and "Discard" buttons.

### Search and filter

For additional tips, visit [Search for messages](90559-use-gmail-with-a-screen-reader.md#searchformessages).

With your screen reader, to navigate to the Search field, use the "previous edit field" command.

Rather than using a link to the "Filter" section of "Settings," you can turn a search into a filter in Standard view.

## Related resources

- [Use Gmail with a screen reader](90559-use-gmail-with-a-screen-reader.md)
- [Use accessibility features with Gmail](6115187-accessibility-in-gmail.md)