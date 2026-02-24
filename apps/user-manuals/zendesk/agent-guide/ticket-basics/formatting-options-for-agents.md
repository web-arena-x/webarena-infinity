# Formatting options for agents

Source: https://support.zendesk.com/hc/en-us/articles/4408884153242-Formatting-options-for-agents

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

This article describes how admins can allow agents to add bolding, italics, lists,
and other formatting, as well as images and color text, to their ticket comments
and macros. Formatting can help make tickets and the email notifications that are
sent to requesters easier to read and understand.

This article includes the these sections:

- [Formatting content in the agent interface](#topic_qgg_xqm_hpb)
- [Formatting limitations](#topic_ets_cbl_btb)
- [Turning on or turning off color text](#topic_lw5_xb1_fsb)

## Formatting content in the agent interface

The formatting options described in this section are available automatically in
the agent interface and are applied to your whole account. Your agents have
a combination of formatting options within the same rich content editor,
CKEditor. You don’t have to choose between a Rich content editor and a
Markdown editor for your agents.

Agents can format from the toolbar:

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/formatting_toolbar_aw.png)

Agents can also enter Markdown commands:

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/formatting_markup_aw_cropped.gif)

This editor is available to agents when they create new tickets, add [ticket comments](https://support.zendesk.com/hc/en-us/articles/4408831849882), make [bulk editing](https://support.zendesk.com/hc/en-us/articles/4408886890906) changes to tickets,
and update any tickets created from integrations that use the Zendesk [Channel Framework](https://support.zendesk.com/hc/en-us/articles/4408824097050#topic_amm_zbh_bhb).

Both rich content and markdown formatting options are enabled automatically in
your account.

### Formatting limitations

This section describes some limitations for using the
combined rich content and Markdown editor in the Zendesk Agent
Workspace.

- This combined experience is not available in the
  macro editor.
- Rich-content formatting inside code blocks is not
  supported.
- Using the down arrow key to escape the code block
  is not supported. To escape a code block, press the Return
  key three times.
- Image resizing using the up and down arrow keys is
  not supported.
- Horizontal rule elements will always be on their
  own line. They cannot be inside of other elements.
- You can only indent a list item if it is at the
  same level as a previous list item. You can’t indent
  blockquotes. You can only indent the text inside of
  blockquotes.
- Using the markdown underline symbol (\_) for underlined text
  is not supported. For example, typing
  `_Important_` does not appear as
  Important. You can use underline symbols (\_)
  in addition to asterisks (\*) to make text bold or italic.
  For example, typing `_Note_` and
  `__Caution__` appears as *Note*
  and **Caution**.

## Turning on or turning off color text

In the [Zendesk Agent Workspace](https://support.zendesk.com/hc/en-us/articles/4408821259930), admins
can use formatting options to turn color text on or off. This account-wide
setting enables admins to control whether or not agents can add text color
and background color in ticket comments. See [Changing text color](https://support.zendesk.com/hc/en-us/articles/4408831849882#topic_vpl_wfh_1qb). Color text
is on by default in the Zendesk Agent Workspace. When color text is turned
off, agents will not see a color picker in the text toolbar.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/aw_color_picker.png)

Color text is available only in the Zendesk Agent Workspace, not the standard
agent interface.

**To turn off color text**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_objects_rules_icon.png)
   **Objects and rules** in the sidebar, then select **Tickets > Settings**.
2. Click **Comment options for agents** to expand it.
3. Deselect **Allow agents to change the text color**.

   Later, if
   you want to turn color text back on, select **Allow
   agents to change the text color**.