# Setting up your X (formerly Twitter) channel

Source: https://support.zendesk.com/hc/en-us/articles/4408883122714-Setting-up-your-X-formerly-Twitter-channel

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

Location: Admin Center > Channels > Messaging and social > X Corp accounts

All Zendesk Suite and Zendesk Support customers can add at least one X (formerly Twitter) account so that public messages, such as public mentions, public replies to your tweets, and public likes to tweets, become tickets. Your agents will be able to see and respond to these tickets from the agent interface, just like any other ticket.

Additionally, Zendesk Suite customers can add multiple accounts and they can receive public messages *and* private messages from those accounts.

| | |
| --- | --- |
| **Zendesk Support plans** | One X handle with public messages only. Private messages are not supported. |
| **Zendesk Suite plans** | Up to 5 X handles with public *and* private messages. |

You must be an administrator to add an X (formerly Twitter) channel.

This article describes adding an X (formerly Twitter) channel for *public messaging* with your customers. To set up a channel for *private messaging* with your customers, see [Adding X (formerly Twitter) DM channels](https://support.zendesk.com/hc/en-us/articles/4408832388250).

This article includes these sections:

- [How the X (formerly Twitter) channels works](#topic_e3j_zxv_rkb)
- [Adding X (formerly Twitter)
 accounts to Support](#topic_n23_wcp_2g)
- [Editing X (formerly Twitter) account settings](#topic_5bj_ffp_2g)
- [Removing X (formerly Twitter) accounts](#topic_lt2_rsv_4r)
- [Appending ticket links to outgoing tweets](#topic_wph_t2x_2g)
- [Managing X (formerly Twitter) tickets with business rules](#topic_kyz_pkp_2g)
- [Understanding why your X (formerly Twitter) account might be deauthorized](#topic_zx1_ngk_gp)

## How the X (formerly Twitter) channels works

Zendesk monitors X (formerly Twitter) accounts and converts tweets to tickets as needed. All tweet activity between agents and X (formerly Twitter) users is added as ticket comments. You can do the following:

- Convert a tweet into a ticket and respond to the user with a tweet, or move the conversation to email
- Bulk convert multiple tweets into tickets in one step
- Convert tweets to tickets outside of Zendesk by liking a tweet
- Automatically capture public mentions and direct messages as tickets
- Append ticket links to outgoing tweets
- Select which of your accounts agents are allowed to use when sending outgoing tweets
- Monitor and take action on activity using business rules

Only administrators have access to the incoming tweets. However, once tweets have been converted to tickets, all agents have access to the tickets, unless you have restricted agent access to certain types of tickets.

Once a tweet becomes a ticket, it behaves just like any other ticket in Zendesk, except that you have the option of replying back to the user with a public tweet or moving the conversation to email.

You can control if and how incoming tweets become tickets. The approach you take might be based on your overall traffic or the number of agents you have available. Here are several scenarios for managing incoming tweets:

- **Likes.** Convert tweets outside of Zendesk by liking them in your X client. This approach allows you to manually choose tweets to convert before they ever reach Zendesk.
- **Mentions and direct messages.** Automatically create tickets from public tweets that contain your X handle or from direct messages. Sometimes, tickets that are not support requests and that don't need follow-up are created. You can manage these out of your ticket queue by manually solving and closing or deleting them. Group direct messages are not supported and do not create tickets.
- **Triggers.** Use one or more triggers to monitor new support requests that originate from your X channel.
 You can use the trigger condition Ticket Channel, which has the following three sources: X Corp, X Corp DM (direct message), and X Corp Like. The advantage to this approach is that you have much more control over the creation and management of X-based tickets. See [Managing X (formerly Twitter) tickets with business rules](#topic_kyz_pkp_2g).

Note the following limits:

- It can take up to 15 minutes for a ticket to be created from a tweet.
- Each X ticket has a limit of 5,000 comments. After reaching the limit, Zendesk stops importing new tweets as comments on the ticket.

## Adding X (formerly Twitter) accounts

You can add an X (formerly Twitter) account to your Zendesk account so that tweets become tickets, and your agents can see and respond to these tickets, just like any other ticket.

The number of handles and the type of messaging supported by your account depends on your plan type.

| | |
| --- | --- |
| **Zendesk Support plans** | One X handle with public messages only. Private messages are not supported. |
| **Zendesk Suite plans** | Up to 5 X handles with public *and* private messages. |

**To add an X (formerly Twitter) account**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_channels_icon.png)
   **Channels** in the sidebar, then select **Messaging and social > X Corp accounts**.
2. Select the **X Corp accounts** tab.
3. Click **Add your first X Corp account**.
4. You'll be prompted to log in to X Corp and then authorize Zendesk to use your account. Enter your login information and then click **Authorize App**.

You'll want to edit the account's settings to control how tweets to this account are handled (see [Editing X (formerly Twitter) account settings](#topic_5bj_ffp_2g)).

## Editing X (formerly Twitter) account settings

After you've added an X (formerly Twitter) account, you can edit the account's settings to control how tweets to this account are handled.

You can choose to automatically convert public mentions and direct messages into tickets. If you enable these, the option to manually convert tweets to tickets will no longer be available for that account.

By default any responses to a tweet will be from the account the tweet was directed to. You can select a different account from the **Reply as** drop-down list under the ticket reply box.
If you want to automatically respond from one account, you can disable **Allow replies via this account** when editing your other X accounts.

**To edit settings for an X (formerly Twitter) account**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_channels_icon.png)
   **Channels** in the sidebar, then select **Messaging and social > X Corp accounts**.
2. Select the **X Corp accounts** tab.
3. Click **Edit** beside the account you want to edit.
4. Update settings as needed.

   The settings are described in the following table.
5. Click **Update X Corp account**.

| Setting | Description |
| --- | --- |
| Allow replies via this account | This setting allows agents to use this account when replying to an X ticket. Agents can select the account below the reply box on an X ticket:    Replies to tickets from X retain the original inbound format. For example, if the ticket was created from a public message, then the agents reply from within Zendesk will also be a reply to that public message. If the ticket was created from a tweet mentioning your X handle (for example @Zendesk), then the agents reply from within Zendesk will be a reply tweet, threaded to the senders original mention. |
| Make this the default account | Note: This setting appears when **Allow replies via this account** is set to **yes**. Use this account by default to reply to tickets that were created from tweets to your other X accounts that don’t allow replies. When **yes**, the **Reply as** drop-down list shows the name of this account by default. However, agents can still choose a different reply-enabled account from the drop-down list, if desired and available. You can only have one default account at a time. Your old default account becomes a non-default account when set to **no**. **Bulk updating tickets** Setting a default X account can affect bulk ticket updates in a few ways. When a customer replies to an X account that allows replies:   - If the X account is the default account, agent   replies are sent from that account. - If a different, separate X account is the   default account, agent replies are sent from the   default account instead of the account that the   customer initially replied to.   When a customer replies to an X account that doesn't allow replies:   - If there is a default X account, agent replies   are sent from the default account. - If there is no default X account, an error   appears because the account doesn't allow   replies.   For information about how to bulk update tickets, see [Bulk updating tickets](../../agent-guide/ticket-management/managing-tickets-in-bulk.md#topic_oth_lkp_gk). |
| Capture public mentions as tickets | This automatically converts any public tweet containing your X handle (for example, @mondocam) to a ticket. |
| Capture incoming direct messages as tickets | This automatically converts incoming direct messages into tickets so that your customers can contact you privately rather than publicly. Depending on your X account settings, you can either receive direct messages from anyone *or* only from users you follow. You can reply to anyone who sends you a direct message. If you add [an X (formerly Twitter) DM channel](https://support.zendesk.com/hc/en-us/articles/4408832388250), disable this setting. Otherwise duplicate tickets are created when a private message is received. |
| Track Likes | This automatically converts a tweet that you like to a ticket. For example, if you're managing your X stream using X.com, you have the option of manually liking the tweet by clicking the heart icon. |

## Removing X (formerly Twitter) accounts

You can remove an X (formerly Twitter) account by deactivating it or unlinking it. If you deactivate an account, it is inactive in Zendesk but you can reactivate it at any time. If you unlink an account, it is removed from Zendesk.

**To deactivate an X (formerly Twitter) account**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_channels_icon.png)
   **Channels** in the sidebar, then select **Messaging and social > X Corp accounts**.
2. Select the **X Corp accounts** tab.
3. Click **Deactivate** beside the account you want to deactivate.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/twitter_deactivate_account.png)

   The account is deactivated. It will not turn tweets into tickets and you cannot reply using it. You can reactivate account at any time.

**To unlink an X (formerly Twitter) account**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_channels_icon.png)
   **Channels** in the sidebar, then select **Messaging and social > X Corp accounts**.
2. Select the **X Corp accounts** tab.
3. Click **Unlink** beside the account you want to remove from your X (formerly Twitter) channel.
4. Click **OK** to confirm.

   The account is unlinked.

## Appending ticket links to outgoing tweets

Note: You must have an account with an [activated help center](https://support.zendesk.com/hc/en-us/articles/4408846795674)
to use this feature and you must have [enabled Twitter social SSO](https://support.zendesk.com/hc/en-us/articles/4408885847962#topic_nxw_j4m_h3) for end users.

Another option for your outgoing tweets is to append a shortened URL to the ticket you created from the tweet. This allows the X (formerly Twitter) user to access the help center ticket page via their X (formerly Twitter) account. In other words, remote authentication is used to log in through X (formerly Twitter) to Zendesk (end users must sign in to Zendesk to see the ticket page).

Once an X user has access to the ticket page, they can add a longer comment than the 280 character limit of a tweet. They can also update their user profile (adding their email address for example).

You have the option of allowing the agent to decide if a shortened or the original URL is used in the response. And, you can choose one of several URL shortening services to use.

**To append ticket links to outgoing tweets**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_channels_icon.png)
   **Channels** in the sidebar, then select **Messaging and social > X Corp accounts**.
2. Select the **General settings** tab.

   You must have [activated help center](https://support.zendesk.com/hc/en-us/articles/4408846795674) to see this tab.
3. Click **Yes** next to **Append ticket links to outgoing tweets?** to enable the ticket links.

   You must have [enabled Twitter social SSO](https://support.zendesk.com/hc/en-us/articles/4408885847962#topic_nxw_j4m_h3) for end users to see this setting.
4. If you want agents to decide when to use shortened URLs, deselect the **Always include shortened ticket URL** option. It is selected by default.
5. Click **Save tab**.

## Managing X (formerly Twitter) tickets with business rules

A number of conditions are available to manage your X (formerly Twitter)
tickets using business rules.

As with other channels, you can detect a ticket's source using the Ticket Channel condition in automations, reports, triggers, and views.
There are three source types you can use in the Ticket Channel condition: X Corp, X Corp DM (direct message), and X Corp Like.

If, for example, you wanted to create separate views of each of the source types, you simply choose the Ticket Channel condition and then select the type.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/twitter_view.png)

In addition to the channel source types, three other X conditions are available in triggers:

- Requester's number of X Corp followers...
- Requester's number of tweets...
- Requester is verified by X Corp

The first two conditions help you to determine how active and potentially influential a user is, which may influence how you manage their tweets. For example, you might want to set X tickets from more highly visible users to Urgent so that you respond as quickly as possible. Here's an example of what a trigger like that might look like:

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/twitter_trigger.png)

The **Requester is verified by X Corp** condition is a special type of X account that has had its identity verified. Knowing that an account has been verified may be important to you in determining how to handle tickets from that account.

## Understanding why your X (formerly Twitter) account might be deauthorized

Zendesk constantly monitors your X (formerly Twitter) accounts for new public mentions and direct messages. If Zendesk cannot connect with your account, it will send an email notification to all admins on your Zendesk account.

Common reasons your X (formerly Twitter) account might become deauthorized include:

- The password on your account has changed.
- The account no longer permits Zendesk to view its timeline and tweet on its behalf. This can happen if Zendesk has been removed from the list of allowed apps in your X account.
- Zendesk receives a consistent response from X Corp indicating that Zendesk is not authorized to access your X account’s content. This should only happen due to an error in the X Corp platform.

If you receive notification that an X account has become deauthorized, you need to reauthorize the affected account in Zendesk.

**To reauthorize your X (formerly Twitter) account**

- In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_channels_icon.png)
 **Channels** in the sidebar, then select **Messaging and social > X Corp accounts**.