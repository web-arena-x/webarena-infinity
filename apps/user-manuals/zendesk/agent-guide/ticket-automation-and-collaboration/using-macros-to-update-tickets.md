# Using macros to update tickets

Source: https://support.zendesk.com/hc/en-us/articles/4408887656602-Using-macros-to-update-tickets

---

A macro is a prepared response or action that an agent can manually apply when they are creating or updating tickets (seeAbout macros). If youcreated macrosfor support requests that can be answered with a single, standard response or action, agents can evaluate tickets and apply macros manually as needed.

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

A macro is a prepared response or action that an agent can manually apply when they are creating or updating tickets (see [About macros](https://support.zendesk.com/hc/en-us/articles/4408844187034#topic_zlk_nf1_dsb)). If you [created macros](https://support.zendesk.com/hc/en-us/articles/4408844187034) for support requests that can be answered with a single, standard response or action, agents can evaluate tickets and apply macros manually as needed.

Macros can be applied to one or more tickets by selecting them from the Apply macro menu or by using a keyboard shortcut in ticket comments.

Tip: Learn how to improve your agents' productivity in Graeme Carmichael's [Giving different responses based on ticket content](https://support.zendesk.com/hc/en-us/community/posts/360036926874).

This article contains the following sections:

- [Macros to get you started](#topic_lty_vgx_tb)
- [Applying macros from the menu](#topic_kda_eew_uf)
- [Applying macros with a keyboard shortcut](#topic_agl_vdf_2vb)
- [Notes about applying macros](#topic_fqb_yjz_j3c)
- [Previewing macros](#topic_cz5_hrn_r3b)
- [Using macros to update problem and incident tickets](#topic_abf_z5m_n1c)

Related articles:

- [Creating macros for tickets](https://support.zendesk.com/hc/en-us/articles/4408844187034)
- [Building macro action statements](https://support.zendesk.com/hc/en-us/articles/4408832783642)
- [Creating macros from existing tickets](https://support.zendesk.com/hc/en-us/articles/4408886850586)
- [Organizing and managing your macros](https://support.zendesk.com/hc/en-us/articles/4408884166554)

## Macros to get you started

There are a number of macros you can use to get started, including:

- **Close and redirect to topics**

 This sets the ticket status to Closed. If it is an incident of a known problem, the requester will be informed via a comment that the ticket has been closed and recommended that they visit the forums for more information about the incident.
- **Requester not responding**

 This is a reminder that can be sent to the requester if they have not responded to a request for more information on a pending ticket.
- **Downgrade and inform**

 This tells the requester that the priority of their request has been downgraded to low and that there may be some delay in resolving their request.
- **Take it!**

 This macro is a shortcut for agents to assign a new request to themselves.

These macros can be used as is, edited, or cloned, so you can modify and repurpose them as needed.

### Additional macros for employee services

On Employee Service Suite plans, the following macros are predefined for common HR and IT use cases:

- **[SAMPLE] Start onboarding process for new hire**

 This provides a list of forms that must be completed for new hires before IT can allocate a laptop and software access.
- **[SAMPLE] Hardware/software request for new hire**

 This requests a laptop for a new hire.
- **[SAMPLE] Laptop approval**

 This requests approval for a replacement laptop for an employee.
- **[SAMPLE] Laptop request pending approval**

 This lets the requester know the laptop request was received.
- **[SAMPLE] Laptop approved and shipped**

 This lets the requester know that their laptop request was approved and has been shipped to them.
- **[SAMPLE] Laptop troubleshooting**

 This sends the requester some basic troubleshooting advice and points them to more information on the company's website.
- **[SAMPLE] Forgot password**

 This sends the requester instructions on resetting their password.
- **[SAMPLE] Parental leave policy**

 This tells the requester where to find the company's parental leave policy.
- **[SAMPLE] Payroll schedule**

 This tells the requester where to find the company's payroll schedule.

See [Using the sample data for employee services](https://support.zendesk.com/hc/en-us/articles/9012803758362).

## Applying macros from the menu

You can manually apply one or more macros to a ticket at the same time. Keep in mind that what one macro does can easily be undone by another macro.

Just as you can make bulk updates to many tickets at once, you can also apply a macro to more than one ticket using your views. See [Managing tickets in bulk](https://support.zendesk.com/hc/en-us/articles/4408886890906).

So why would you apply more than one macro? A typical use case is a ticket that contains more than one question or issue—let's say two in this example. You might have set up two macros that both insert a comment into a ticket to answer each issue separately. By applying each macro to the ticket, you add two comments and address both issues in a single response.

You can view which macros were applied in the [ticket's events log](https://support.zendesk.com/hc/en-us/articles/4408829602970).

**To apply a macro from the menu**

1. In a ticket, click **Apply macro** in the bottom toolbar.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/apply_macro_button.png)
2. Select a macro from the list. You can filter the list by typing the beginning of a macro's name. By default, the list of macros is displayed alphabetically. You can change the order of this list. See [Reordering macros manually](https://support.zendesk.com/hc/en-us/articles/4408884166554#topic_dgr_jhv_zbc).

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/apply_macros_small.png)

   Typically, your five most commonly used macros from the past week appear at the top of the macros list. The most-used macros display can be disabled, in which case, you'll only see the all macros list. See [Disabling the most-used macros option](https://support.zendesk.com/hc/en-us/articles/4408884166554#topic_jf5_2cc_dx).

   If your [macros are categorized](https://support.zendesk.com/hc/en-us/articles/4408884166554#topic_dpr_k1j_mw), you can click through the levels of categorization to apply a macro.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/macro_assign_by_category1.png)

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/macro_assign_by_category2.png)

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/macro_assign_by_category3.png)

   Note: Macros cannot be set up for specific channels.

   The actions defined in the macro are applied. If the macro updated the ticket comment, you can edit the text before submitting the ticket.

   If you have a macro that inserts text into a ticket comment, you can set an insertion point in the ticket comment first, before you apply a macro. This enables you to control exactly where the macro text appears.
3. To apply another macro, click **Apply macro** again and select another macro.

   Tip: Check out how we use macros to manage tickets with Brett Bowser's [Improve escalation workflows using macros](https://support.zendesk.com/hc/en-us/community/posts/360004412707).
4. Submit the ticket.

## Applying macros with a keyboard shortcut

If you have [Agent Workspace](../ticket-basics/about-the-zendesk-agent-workspace.md) activated, you can apply macros using a keyboard shortcut in a ticket comment. Using a macro keyboard shortcut can save you typing time by applying a macro to a ticket with just a few keys.

Macro keyboard shortcuts are activated by default. To deactivate macro keyboard shortcuts, see [Activating and deactivating macros keyboard shortcuts](https://support.zendesk.com/hc/en-us/articles/4984951994778).

For more information about other keyboard shortcuts, see [Viewing and deactivating keyboard shortcuts](https://support.zendesk.com/hc/en-us/articles/4408832849946).

**To apply a macro with a keyboard shortcut**

1. In a ticket, type a slash (/) in the ticket’s comment.

   Note: If you want to exit the Macros menu after typing a slash (/), press the space bar.

   Typically, your seven most used macros from the past week appear at the top of the macros list, including both shared macros and any personal macros you may use.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/macros_keyboard_shortcut.png)

   Note: If your account has Chat or Messaging activated, the list displays both macros and shortcuts. See [Using shortcuts in Chat](https://support.zendesk.com/hc/en-us/articles/4408824439194#topic_kd5_klb_x3b).

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Macros_Shortcuts_menu.png)
2. Select one of these or begin typing a macro name to filter the list.
3. Click the macro name to apply it to the ticket.

   The actions defined in the macro are applied. If the macro updated the ticket comment, you can edit the text before submitting the ticket.
4. To apply another macro, type a slash (/) in the ticket comment.

## Notes about applying macros

In some cases your macro may not apply as expected. If this happens, check the following:

- If you're applying a macro that updates a ticket field, the ticket field must appear on the ticket form in order for the macro to apply.
- Sometimes tickets are updated simultaneously from multiple sources. For example, a workflow may be making updates in the background or multiple agents might be working on the ticket. When this occurs, macros can't be applied until the latest changes are showing in the ticket. If you try to apply a macro to a ticket that doesn't have the latest data, then an error appears prompting you to wait and try again.
- If the macro updates the ticket comment but the ticket tab is closed before the ticket is submitted, the text of the macro will still appear in the composer when you return to the ticket. However, after submitting the ticket, only the comment is updated and the macro isn't shown in the events log for the ticket.
- If you apply a macro but you don't have permission to make the change made by the macro, then the action won't occur. Ask your admin to check your [role permissions](https://support.zendesk.com/hc/en-us/articles/4408883763866-Understanding-Zendesk-Support-user-roles).
- If you apply a macro, then manually revert changes made by the macro or apply another macro that performs a contradicting action, the initial macro actions may not look like they were applied.
- Triggers or automations can conflict with a ticket update, causing tag collisions. Check the [ticket's events log](https://support.zendesk.com/hc/en-us/articles/4408829602970) to ensure this behavior isn't happening.

## Previewing macros

You can preview a macro from the Apply macro menu before applying it to a ticket.

**To preview and apply a macro from the menu**

1. In a ticket, click **Apply macro** in the bottom toolbar.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/apply_macro_button.png)
2. Find the macro you want to use in the list.
3. Click the **Open preview** icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/macro_preview_eye.png)).

   Alternatively, hover your cursor over the macro to display its description tooltip. From the tooltip, you can view the macro's description (if one exists) and access its preview by pressing Shift + Enter.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/macro_preview_description.png)

   The preview shows the macro's title and description (if one exists), as well as the fields and elements the macro will change, add, or remove, including:

   - Ticket fields
   - Comments, replies, or notes (including placeholders and dynamic content)
   - Attachments

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/macro_preview_screen.png)
4. If the macro looks correct, click **Apply Macro**.

   You can also click **Cancel** to return to the ticket screen, or click **Open in Settings** to view the macro's settings in Admin Center.

## Using macros to update problem and incident tickets

Use caution when applying macros with placeholders to [problem and incident tickets](https://support.zendesk.com/hc/en-us/articles/4408835103898). It's easy to accidentally populate the wrong values in ticket comments when using macros with placeholders in this scenario. To avoid this, you often need use a backward slash (\) to escape the placeholder so that it populates the appropriate value within the related incident tickets.

For example: `Hello \{{ticket.requester.first_name}}`