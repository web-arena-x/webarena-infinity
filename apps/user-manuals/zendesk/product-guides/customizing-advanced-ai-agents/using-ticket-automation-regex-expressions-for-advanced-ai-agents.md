# Using ticket automation RegEx expressions for advanced AI agents

Source: https://support.zendesk.com/hc/en-us/articles/8357758835098-Using-ticket-automation-RegEx-expressions-for-advanced-AI-agents

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **Add-on** | AI agents - Advanced |

In this article, we will be covering RegEx expressions specifically for Ticket Automation

Unlike messaging, there is a lot of content in the email that could just be noise and adds no value to the conversation for the AI to process. You can however find [generic RegEx examples](https://support.zendesk.com/hc/en-us/articles/8357756811162) here too.

Some examples of this include:

- [Signatures / Email Sign-offs](#h_01GE4BC8Z80B1ZP85N7H54H0NW)
- [Remove Text After Attachments](#h_01GE4JJJ5NFJCAEXRPB0ZZY0TF)
- [Consistent Formatting to be Ignored](#h_01GE4JJRC1DQYNH9TT5FK2K8ST)

## Email sign-offs

The end of the email is usually worthless from a content perspective for the AI agent to infer an understanding of the conversation. Remove/hide everything after the client has signed off / ended the email. For example "best regards", "sincerely", " kinds regards" etc. We have a preset that you can add called `---` which takes the common email sign-offs to remove that text and the subsequent information which could be the thread of the email, a reply from a newsletter or other post-signature information.

## Remove Text After Attachments

Typically images are attached to the end of the email but there may be signature or policy information. Alternatively, your customers may respond to marketing communication or a forwarded email and thus those previous/forwarded messages follow afterward, so it can be better to cancel everything after the attachments are out from AI processing.

- `Attachment(s)(.|\n|\t)+`

## Consistent Formatting to be Ignored

This could be data from your web forms around whether a user was logged in or other recurring information at the beginning of the ticket you would like to ignore. Let's say I have a text that tells me key information about the user starting with Pages Viewed and then I know all of that fluff ends with a unique term like Comment, I can hide it with a RegEx like.

`Pages Viewed(.|\n|\t)+Comment`

This can be done in any part of the message as long as unique terms can be determined and then you can cancel noise at the beginning, middle and end of the message with this method.

## CleanContent mode

Ticket noise decreases the success of the intent recognition and with that the overall performance of your email AI agents. We define ticket noise as any kind of content that doesn’t include meaningful information to identify the intent, language, or context of a request. It can be forwarded/replied emails, attached images, signatures, compliance warnings, etc. When enabled, CleanContent mode will ensure that only relevant information is used by the email AI agent for improved intent training and recognition performance. This feature works for all the languages we support.

The CleanContent Mode currently considers attachment entities as ticket noise. For Zendesk users, it is possible to use the CleanContent Mode while still being able to access attachment entities. Here are the few steps to follow in order to set this up:

Create a Zendesk trigger to identify and tag emails with attachments.

![Screenshot 2023-08-31 at 16.02.17.png](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/bots_13594727747090.png)

Move the trigger up in the Zendesk hierarchy.

![Screenshot 2023-09-08 at 16.22.03.png](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/bots_13594727753490.png)

In AI agents - Advanced, create an AI agent level action that absorbs all the tags.

![Screenshot 2023-08-31 at 16.01.48.png](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/bots_13594717690130.png)

Finally, add a conditional block to the dialogue builder in order to identify if the attachment tag is present or not and set up the needed reply.

![Screenshot 2023-08-31 at 16.01.30.png](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/bots_13594727774482.png)

This is a newly launched feature that we are still closely monitoring. For that reason, you can’t activate it by yourself just yet. Please contact your Customer Success Manager so they can do it for you.