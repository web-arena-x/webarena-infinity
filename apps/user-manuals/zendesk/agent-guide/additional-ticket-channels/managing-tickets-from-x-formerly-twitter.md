# Managing tickets from X (formerly Twitter)

Source: https://support.zendesk.com/hc/en-us/articles/4408829618202-Managing-tickets-from-X-formerly-Twitter

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

Using Zendesk Support, you can monitor and interact with X (formerly Twitter) accounts and convert tweets into tickets. As an agent, you can reply to these tickets through X or by other means.

This article contains the following sections:

- [Understanding the X channel](#topic_ick_wvr_1fb)
- [Replying to tweets](#topic_ufp_2fj_rt)
- [Changing the requester](#topic_fsw_z4g_jt)
- [Selecting an account to reply from](#topic_qfl_z2j_rt)
- [Appending ticket links to outgoing tweets](#topic_vq2_y4g_jt)

## Understanding the X channel

When your admin configures Zendesk to work with X, one or more of the following capabilities are added:

- Tweets you like are automatically converted into tickets
- Incoming direct messages are automatically converted into tickets to allow customers to reach you privately
- Public tweets that mention your X handle (for example, @zendesk) are automatically converted into tickets

A ticket received from X behaves like a normal ticket in most ways. You can update the ticket properties and comment in the same way you would on any other ticket. You can also add internal notes that the external requester does not see.

## Replying to tweets

When you reply to a ticket from X, it will appear either as a direct message or a reply, depending on the type of ticket. For example, if the ticket was created from a direct message (DM), then your reply from within Zendesk will also be a DM. If the ticket was created from a tweet mentioning your X account name (for example @Zendesk), then your reply from within Zendesk will be a reply tweet, threaded to the senders original mention.

The only difference between a standard ticket and a ticket received from X is the appearance and your reply visibility. When you reply to a ticket with a tweet, you must stay within the X character limit of 280 characters.

Below is an example of what a ticket from X looks like:

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/twitteragent.image.png)

Depending on the settings your administrator has configured, you might be able to choose to add a URL to the tweet that contains a link to the ticket. Alternatively, your administrator might have configured this URL to be added automatically. See [Appending ticket links to outgoing tweets](#topic_vq2_y4g_jt).

Even though your comments will appear as replies or direct messages to the requester, you can still see all comments in the **Events** field of the ticket. If you have connected Zendesk to multiple X accounts, you might need to [Select an account to reply from](#topic_qfl_z2j_rt).

If you have connected multiple X accounts, replies by default will come from the X account that first received the tweet, mention, or direct message. However, you can choose which X account you want to reply from. To choose an account to reply from, you need to have at least two X accounts set up that have the option "Allow replies via this account".

### Changing the requester

You can update the properties of a ticket from X in the agent interface. This includes changing the requester. If you change the requester to a requester without an X account, you will no longer be able to respond to the ticket using tweets or X direct messages. The options to respond using X will be grayed out.

If you want to continue using X to interact with the ticket, you can:

- Add an X account to the new requester
- Choose a requester with an X account

Alternatively, you can continue to interact with the ticket using email or other channels you have configured.

## Selecting an account to reply from

If your Zendesk supports multiple X accounts, your admin can enable the **Allow replies via this account** setting so you can choose which account to use when replying to public tweets. You can select a different account from the **Reply as** list box underneath your reply. The account targeted by the tweet will be selected by default.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/twitter_allow_replies_via_account.png)

Note: You can only reply to direct messages (DMs) from the account to which the DM was initially sent.

## Appending ticket links to outgoing tweets

If your admin has enabled it, you can append a URL to link the requester to the ticket.
Alternatively, your admin might have configured Zendesk to automatically add the link.

To append ticket links to outgoing tweets, check the **Append ticket link** box at the bottom of the ticket. A URL will appear in the reply or direct message, but not in the Events field.

Note: This option is not available until your admin activates your help center.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/appendtwitter.png)

After clicking the link, the X user will be redirected to your Zendesk sign-in page. They can then take one of the following actions:

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/tweet_response.png)

- If this is the user's first ticket, Zendesk creates a new user profile with the name of the X account. The user will need to supply an email address and password to sign in and access the ticket.
- If the user has previously opened tickets using X, they must sign in using their previous username and password.
- If the user has previously opened tickets by email but has not used X to open a ticket, their X account will be linked to the account they previously created.