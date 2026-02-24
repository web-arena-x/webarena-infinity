# Targeted Emails Performance Overview

Source: https://support.joinhandshake.com/hc/en-us/articles/360009603273-Targeted-Emails-Performance-Overview

---

After a Targeted Email has been sent, performance details are tracked and viewable directly in Handshake. Results can take up to an hour to fully update after the initial send, and data is updated continuously as more actions occur.

To access these tabs, click **Emails** from the left navigation bar, then click the desired sent email from To Students or To Contacts.

- *If your team sent emails via our legacy tool, you can access historical engagement data. For details, refer to [View Legacy Emails Engagement Data](https://support.joinhandshake.com/hc/en-us/articles/4405598310935)!*

![select_to_students_or_to_contacts.png](https://support.joinhandshake.com/hc/article_attachments/25998877363479)

While viewing the email, performance details can be viewed via two tabs:

- [Email](#h_01FC689TBF04ATAZ8M5H4TJAJ4)
  - Delivered
  - Open rate
  - Click rate
  - Unique URL clicks
    - A breakdown of each unique URL click (if applicable)
  - Handshake Activation Rate
  - All actions
- [Recipients](#h_01FC689Z3T0M8KA05MNG6CJ3DW)
  - Search by name or keyword
  - Filters
  - Excluded recipients

## Email

The Email tab displays high-level performance (open rate and click rate) and the actions that were taken on the Handshake components included in the email.

### Delivered

- The amount of emails that were successfully sent to students (delivered*emails are calculated by the recipients minus recipients that had previously unsubscribed from Handshake emails minus any bounced emails)*

![Delivered_emails_equation.png](https://support.joinhandshake.com/hc/article_attachments/25998877376663)

If the recipient didn't receive the email due to a “bounce” or if they chose to unsubscribe from receiving Handshake emails, they will not be included in the equation. Only emails that are successfully delivered are included in these statistics.

### Open rate

- The count of students that opened this email *(Open percentage is calculated by the unique number of opens divided by the number of emails successfully delivered)*

![Open_rate_equation.png](https://support.joinhandshake.com/hc/article_attachments/25998866849175)

If a recipient received an email and forwards it to someone else, and that person opens the email, then that open will only count once as the original recipient. This is why it's considered "unique" and not total.

In order to track opens, we attach an image "sensor" that is basically hidden to the email recipient. This "sensor" is at the very bottom of the sent email, which can impact the open rate in Targeted Emails:  

- If students don't scroll to the bottom of the email, it could result in the open sensor not being triggered
- If you have content in excess of 100kb, it can result in the message being clipped from some mail providers, which can also reduce the open rate
- If an individual blocks images on their email client, then the image "sensor" is never loaded, so the open will never be counted

### Unique URL clicks

- The count of unique recipients that clicked one or more links from the email. This number will display the total number of unique clicks across all links in the email
- The percentage will represent the rate that recipients have clicked on each individual URL link *(unique click percentage is calculated by the number of students that clicked the link(s) divided by the number of emails successfully delivered)*

![Unique_URL_click_rate_equation.png](https://support.joinhandshake.com/hc/article_attachments/25998877373719)

Similar to unique opens, if a recipient received an email and forwarded it to someone else, and that person clicked a link within the email, then that click will only count once as the original recipient.

All links that had unique clicks within the email will show on the results page. If a link does not show, it is likely the link didn't have any clicks.

### Handshake account activations

- The count of students that activated their Handshake accounts after clicking a link in this email *(Handshake account activation percentage is calculated by the number of students that activated  divided by the number of emails successfully delivered)*

![Handshake_account_activations_rate_equation.png](https://support.joinhandshake.com/hc/article_attachments/25998866849943)

**Note**: this requires that the student activate their account via the link that was clicked in the email. For example, if the student clicks the link, closes the tab, then pulls up Handshake by navigating to the site and activates, this will not count as an activation.

### All actions

- Actions on the Handshake Content that was added to the Targeted Email *(percentages are all calculated by dividing the number of students who took an action by the number of emails successfully delivered)*

![Rate_of_actions_taken_equation.png](https://support.joinhandshake.com/hc/article_attachments/25998877370903)

Actions can be:

- Event Registrations
- Career Fair Registrations
- Job Applications

![Targeted_Email_Stats_Overview.png](https://support.joinhandshake.com/hc/article_attachments/25998877372695)

![All_Actions.png](https://support.joinhandshake.com/hc/article_attachments/25998877377303)

## Recipients

The Recipients tab provides details about the students or contacts who were sent the selected email.

- Recipient names and email addresses are listed in table format on the page. Student recipients will also display their designated Major(s) and School Year.
- Search by name or keyword on the left of the page to identify specific recipients.
- Click **Download Recipients** to download a .csv file with activity details per recipient.
- Filters applied to the selected email's recipient list are listed on the left of the page, below the Download Recipients button.

![recipients_tab.png](https://support.joinhandshake.com/hc/article_attachments/25998877365015)

### Excluded recipients

Students that are unsubscribed from Targeted Emails will be listed as "Excluded". In the recipients list, a red oval to the far right in the row will indicate **Excluded**.

![excluded_example.png](https://support.joinhandshake.com/hc/article_attachments/25998877364247)

Use the filter "Show excluded only", on the left of the page, to identify all recipients that are unsubscribed.

![show_excluded_only.png](https://support.joinhandshake.com/hc/article_attachments/25998866847127)

*For more information on re-subscribing to Handshake emails, refer to [Re-Subscribe to Handshake Emails](re-subscribe-to-handshake-emails.md).*

**Note**: emails are sent from the domain "mail.joinhandshake.com". If recipients are not unsubscribed from this domain but still not receiving Targeted Emails, it's possible Handshake email domains need to be unblocked. For more information, refer to [Email Delivery: Unblocking Handshake Email](https://support.joinhandshake.com/hc/en-us/articles/360012324954).