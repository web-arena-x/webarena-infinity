# Turning off ticket management in your help center to allow email-only support

Source: https://support.zendesk.com/hc/en-us/articles/4408888722842-Turning-off-ticket-management-in-your-help-center-to-allow-email-only-support

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

Verified AI summary ◀▼

To enable email-only support, disable ticket management in your help center. This allows users to submit requests without signing in, using channels like email, chat, or social media. Adjust settings to allow ticket submissions, remove ticket links from notifications, and hide sign-in options in your help center. This approach limits user interactions but maintains communication through email.

Note: This article offers various methods to prevent users from signing
in to your help center, allowing you to primarily handle support requests through email.
While these suggestions remove sign-in opportunities for end users, Zendesk cannot assure
these methods will completely prevent end users from creating an account.

Some Zendesk customers prefer not requiring their end users to sign in. Removing the sign-in
requirement means end users can't view or track their requests on your help center, and they
can't follow or vote on help center articles. These tasks require users to sign in. Instead,
all communication between agents and end users occurs using other channels.

To provide support primarily through email, you need to understand the impact of this change
on your customers, and then work through the items described in this article.

This article includes the following topics:

- [Understanding how email-only support
  impacts customers](#topic_uk2_xvh_4y)
- [Allowing anyone to submit
  tickets](#topic_msc_mes_yb)
- [Removing links to ticket pages in your
  email notifications](#topic_rrs_1vt_tl)
- [Removing sign-in links from your help
  center](#topic_odm_ans_yb)

## Understanding how email-only support impacts your users

When turning off ticket management in your help center, end users can still request support
without signing in by using any of the following channels:

- Sending email directly to your support email address (for example,
  support@*mycompany*.zendesk.com)
- Submitting a support request using the Web Widget (Classic)
- Chatting with an agent
- Leaving a voicemail
- Sending a request through social media

Regardless of the channel by which new requests are submitted, requests become tickets that
agents manage using views, creating and applying macros, generating reports, and so on. All
communication between agents and end users is captured on those tickets, and emails are sent
back and forth between both parties.

End users can still access your help center to search for answers. You can promote this
self-service support option by providing your end users with the link to your knowledge base
(for example, https://*mycompany*.zendesk.com/hc).

## Allowing anyone to submit tickets

To allow requests without requiring end users to sign in to Zendesk Support, you need to
modify your end-user settings. Only administrators can make these changes.

For information on making these modifications, see [Enabling anyone to submit tickets](https://support.zendesk.com/hc/en-us/articles/4408881989018).

When an unregistered end user submits a request for the first time, they are added to your
Zendesk Support as a new end user. They receive the request confirmation email but not the
verification request email. They remain unverified in Zendesk Support.

Note: You can leave the **Allow users to view and edit their profile data** and **Allow
users to change their password** options turned on since your email-only end users will
never be able to sign in to do either of these things. Both are still relevant to your
administrators and agents.

## Removing links to ticket pages from your email notifications

Users must sign in to view ticket pages in your help center. Because you don't want to
require end users to sign in, you need to remove any links to ticket pages from any email
notifications sent to end users. Some of your default triggers create notifications with
ticket links.

### Removing ticket links from your notifications

Remove any links to ticket pages from the default triggers that send email notifications
to requesters. Here are the triggers you need to modify:

- Notify requester and CCs of received request
- Notify requester and CCs of comment update

You'll also need to modify any similar notification triggers (if any) that you created.
Only administrators can edit the triggers.

You might also need to modify triggers that send email notifications to requesters and
CCs, as well as the follower email template. See [Customizing default email notifications for CCs and
followers](https://support.zendesk.com/hc/en-us/articles/4408843866394)

**To remove ticket links from email notification triggers**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_objects_rules_icon.png)
   **Objects and rules** in the sidebar, then select **Business rules >
   Triggers**.
2. Click the **Notify requester and CCs of received request** trigger to open it for
   editing.
3. Remove the {{ticket.id}} and {{ticket.url}} placeholders from the text in the email
   body. For example, below are before and after versions of the email text in the
   **Notify requester and CCs of received request**
   trigger.

   Before:

   ```
   Your request (#{{ticket.id}}) has been received, and is being reviewed by our support staff. 

   To review the status of the request and add additional comments, follow the link below:
   http://{{ticket.url}}
   ```

   After:

   ```
   Your request has been received, and is being reviewed by our support staff. 

   We'll contact you as soon as we have an answer for you.
   ```
4. Click **Save**.
5. Repeat for the **Notify requester and CCs of comment update** trigger.

## Removing sign-in links from your help center

In your help center, removing elements that link to the sign-in page involves deleting or
hiding template components. You must be a Knowledge admin to edit template components.

Note: Customizing your help center theme is not available on the Suite Team plan.

Your agents, like your end users, will no longer see a sign-in link for your help center.
To access the sign-in page, your agents need to use the following URL:
*mycompany*.zendesk.com/access. This is the sign-in page.

Removing the ability to sign in means that every visitor to your help center is treated as
an anonymous user with limited privileges. Anonymous users can view the public areas of your
help center and share links to content. They can't comment on articles or participate in the
community. Because anonymous users can't participate in the community, consider [disabling your help center community](https://support.zendesk.com/hc/en-us/articles/4408821744026), if you have one.

**To remove the links to the sign-in page**

1. In [Knowledge admin](https://support.zendesk.com/hc/en-us/articles/9041943683354#topic_b5q_nwn_s2c), click **Customize design**
   (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/guide_icon_customize.png)) in the sidebar.
2. Hover your mouse over the theme you want to edit, then click **View theme**.
3. Click **Edit code** to open the code editor.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/theming_menu_option_edit_code.png)
4. From the list of templates, click **header.hbs**.
5. From the code, comment out the `sign_in` fragment, like
   this:

   ```
   {{!--
     {{#link "sign_in" class="sign-in"}}
       {{t 'sign_in'}}
     {{/link}}
   --}}
   ```

   If
   you are using an old theme, you might see a `user_info` in place of a
   `sign_in` fragment. Comment this out
   instead:

   ```
   <!-- {{user_info}} -->
   ```

   This component
   displays a sign-in button on the right side of the header.
6. Select the **article\_page.hbs** template and delete or comment out the following
   classes:

   ```
   <div class="article-comments">
   <div class="article-votes">
   ```

   The
   vote component and the article-comments section prompt users to sign in.
7. Click **Publish**.