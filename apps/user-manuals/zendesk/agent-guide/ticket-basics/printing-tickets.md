# Printing tickets

Source: https://support.zendesk.com/hc/en-us/articles/4408836523930-Printing-tickets

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

Verified AI summary ◀▼

You can print individual tickets to create a printer-friendly version for easy reading. While bulk printing isn't available, you can include internal notes, side conversations, and ticket priority in your printout. For lengthy tickets, consider using the Ticket Comments API for efficiency. To print side conversations separately, access them through the context panel and select the print option.

You can create a printer-friendly version of any ticket. You can print individual tickets only – there is no bulk printing option. If your Zendesk plan includes [side conversations](https://support.zendesk.com/hc/en-us/articles/4408844206746), you can include them on the printed ticket, or print them separately.

Note that this feature was designed to create for printouts of tickets to be read by humans. If you are printing very lengthy tickets, the [Ticket Comments API endpoint](https://developer.zendesk.com/api-reference/ticketing/tickets/ticket_comments/) or [Side Conversations API endpoint](https://developer.zendesk.com/api-reference/ticketing/side_conversation/side_conversation/) is a more efficient way to collect and archive those ticket comments. While there is no specific limit on printing tickets using the method described in this article, timeouts may occur when printing tickets with excessive ticket comments, high character count, or with the inclusion of side conversations.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/support_print_ticket_sample.png)

**To print a ticket**

1. Open the ticket that you want to print.
2. Click the Ticket options menu in the upper right, then select **Print ticket**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ticket-options-menu.png)
3. Select the content you want to include.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/print_ticket_confirmation.png)

   - **Include internal notes** displays private, agent-only notes on the printout.

     - **Include side conversations** (Suite Professional and above) displays all related side conversations on the printout.
   - **Include ticket priority** displays the ticket's priority status on the printout.
4. Click **Print ticket**.

   A version of the ticket prints, showing all ticket fields that have values. Fields that do not have values are not printed.

   Note: If you've re-ordered ticket fields in Admin Center, see [What order are ticket fields displayed on the printer-friendly version of a ticket?](https://support.zendesk.com/hc/en-us/articles/5190664797082).

**To print a side conversation (Suite Professional and above only)**

1. In a ticket, open the [context panel](https://support.zendesk.com/hc/en-us/articles/4408836526362) and click the **Side conversations** (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/icon_omnipanel_side_conversations.png)) icon.
2. Click a side conversation to open it.
3. Click the options menu in the upper right, then select **Print**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/side_conv_print.png)

   A printer-friendly version of the side conversation opens.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/side_conv_printer_friendly.png)
4. Click **Print**.