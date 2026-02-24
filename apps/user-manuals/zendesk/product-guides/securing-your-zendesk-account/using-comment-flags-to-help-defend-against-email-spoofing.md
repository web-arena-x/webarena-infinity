# Using comment flags to help defend against email spoofing

Source: https://support.zendesk.com/hc/en-us/articles/4850370022938-Using-comment-flags-to-help-defend-against-email-spoofing

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

Because email is a major ticket channel, tickets are subject to email phishing attacks. Email spoofing is a form of phishing attack where an attacker attempts to trick a victim into thinking a message came from a trusted source. The email might also try to lure the recipient into clicking a link or attachment that takes them to a fraudulent web page or deploys malicious software on their system.

One of the best defenses against email spoofing is your front-line staff working on tickets. While some spoofing attempts are clearly recognizable, accurately recognizing every attempt is not possible for busy agents working in fast-paced environments. Zendesk helps by flagging comments sent by a user whose identity may have been spoofed. These flags notify agents when a potential attack has been detected in a ticket conversation.

This article covers the following topics:

- [Understanding the email spoofing flags in tickets](#topic_az4_vrj_k5b)
- [Actions agents can take on flagged comments](#topic_ftz_y2k_k5b)

Related articles:

- [Working with email address conflicts in ticket replies](https://support.zendesk.com/hc/en-us/articles/4408843970842)
- [Configuring CC and following permissions](https://support.zendesk.com/hc/en-us/articles/4408843795482)

## Understanding the email spoofing flags in tickets

Zendesk displays a warning icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/flagged_message_icon.png)) beside each comment in a ticket conversation that might be an email phishing attempt. Flags display only for ticket comments that were created from email. They don't display for comments created from other channels such as messaging, chat, Web Widget, or the help center request form.

The flag brings attention to the potential risk without affecting the workflow of your end users and agents. The ticket is not flagged in any ticket views. You cannot remove the flag.

Click the warning icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/flagged_message_icon.png)) to display the warning message. You can also hover over the warning flag for more information. The following four email spoofing messages might appear.

- Possible "Reply to end user" spoof: If the agent replies to the comment, the reply might not be sent to the displayed end user. Mismatched From: and Reply-To: headers are a common attribute of email used legitimately by many individuals and organizations. Zendesk only flags the comment when there is suspected malicious intent.

 ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/v1-support-ticket-phishing-reply-to-end-user.png)
- Possible "Reply to agent" spoof: If the agent replies to the comment, the reply might not be sent to the displayed agent. See [Working with email address conflicts in ticket replies](https://support.zendesk.com/hc/en-us/articles/4408843970842) for more information.

 ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/replyto_conflict_warning.png)
- Potential comment spoof: The comment might not have been sent by the displayed email address, or email authentication might have failed.

 ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/flagged_message_warning.png)
- Possible "Other user update": An unknown user who isn't a CC on the ticket might have joined the conversation with a comment. See [Configuring CC and follower permissions](https://support.zendesk.com/hc/en-us/articles/4408843795482-Configuring-CC-and-follower-permissions) for more information.

 ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/unexpected_sender_flag.png)

## Actions agents can take on flagged comments

Depending on the policies of the organization, an agent can take different actions when a potential email spoof has been detected, including:

- Solving the ticket with due caution
- [Marking the ticket as spam and suspending the user](https://support.zendesk.com/hc/en-us/articles/4408842999066)
- Reassigning the ticket to a security group for further review