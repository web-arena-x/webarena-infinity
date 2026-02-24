# Complying with Privacy and Data Protection Law in standalone Chat accounts

Source: https://support.zendesk.com/hc/en-us/articles/4409155522330-Complying-with-Privacy-and-Data-Protection-Law-in-standalone-Chat-accounts

---

This guide describes how certain features and functionality in Zendesk
Chat created in Support and in Zendesk Message can assist with your
obligations under privacy law.

To learn more about meeting your obligations in other Zendesk products,
see [Complying with Privacy and Data
Protection Law in Zendesk products](https://support.zendesk.com/hc/en-us/articles/4408834005530).

A Zendesk Chat account can be created in Zendesk Support or can exist
as a standalone account. For Chat accounts created in Zendesk Support, see
[Complying with Privacy and Data
Protection Law in Zendesk Chat](https://support.zendesk.com/hc/en-us/articles/4409148563098). If you are using web,
mobile, or social messaging, please follow the processes outlined in [Complying with Privacy and Data
Protection Law in Zendesk Support](https://support.zendesk.com/hc/en-us/articles/4408823195930). In standalone Chat
accounts, both agents and end users are managed in Chat.

In this guide, *users* can be End-Users or Agents as the terms are
defined in the [Zendesk Customer Agreement](https://www.zendesk.com/company/agreements-and-terms/zendesk-customer-agreement/).

Topics covered in this article:

- [Meeting an access obligation](#topic_qdm_yhk_gs)
- [Meeting a correction obligation](#topic_ezm_pcv_4v)
- [Meeting an erasure or deletion obligation](#topic_p3p_zhk_gs)
- [Meeting a data portability obligation](#topic_ekz_13k_gs)
- [Meeting the objection obligation](#topic_gcn_swl_ycb)
- [Meeting a consent or disclosure obligation](#topic_p3w_4fy_fvb)
- [Disclaimer](#topic_ddy_2yf_gdb)

## Meeting an access obligation

Individuals from certain regions have a *right of access*. On request, you may
have an obligation to inform an end user or agent where their personal data is being
held and for what purposes.

If you receive a request for access to personal data, you can export data
as described in [Meeting a data portability obligation](#topic_ekz_13k_gs)
below.

## Meeting a correction obligation

Individuals from certain regions have a *right to rectification*, or the right to have
inaccuracies in their personal data corrected. On request, you may have an
obligation to provide the individual with their personal data and fix inaccuracies
or add missing information.

To update the personal data of end users and agents, see the following
topics in this guide:

- [Updating end users](#topic_hmx_d2b_cdb)
- [Updating agents](#topic_vn3_f2b_cdb)

You must be an admin to update end users and agents.

### Updating end users

**To update the personal data of an end user**

1. From the dashboard, select **History** and perform a
   search for the chats involving the end user.
2. Select each chat in the results, click the **User
   Info** tab, and make your updates.
3. Repeat step 2 for each chat involving the end user.

### Updating agents

**To update the personal data of an agent**

- In the dashboard, select **Settings** >
  **Agent**.

## Meeting an erasure or deletion obligation

Individuals from certain regions have a *right to erasure*, or the right to be forgotten or
deleted. On request, you may have an obligation to delete the personal data of an
individual.

The workflow for deleting the personal data of a end user or agent in
standalone Chat accounts is as follows:

1. Delete chats.
2. Delete the user from the account.

The order of operations is important because user data might be needed to
find chats or messages containing personal data.

**To delete chats**

See the following topics in the article for Zendesk Chat:

- [Deleting
  chats](https://support.zendesk.com/hc/en-us/articles/4409155522330#topic_lbr_pfj_1db)
- [Permanently deleting
  chats (preview)](https://support.zendesk.com/hc/en-us/articles/4409155522330#topic_fhk_pgt_ycb)
- [Deleting chats with
  the API](https://support.zendesk.com/hc/en-us/articles/4409155522330#topic_tsw_c3j_1db)

**To delete an agent**

See the following topic in this guide:

- [Deleting agents](#topic_lj3_1jb_cdb)

### Deleting agents

**To delete one or more agents**

1. Go to your dashboard and select **Settings > Agents**.
2. Select the check box next to one or more agents.
3. Select the **Actions** drop-down menu at the top of
   the list and choose **Delete selected**.
4. Click **Delete** on the window that appears to
   confirm.

The agent is soft deleted, meaning the agent profile is no longer
accessible in the user interface. It still exists in the
data store. The system keeps the name to display in chat
transcripts. You can remove the name by deleting the
chat.

## Meeting a data portability obligation

Individuals from certain regions have a *right to data portability*. On request, you may
have an obligation to provide an individual with their personal data or to transmit
the data to another organization.

The following topics describe how to export personal data from Chat:

- [Exporting visitors with the Chat API](#topic_xjy_yqb_cdb)
- [Exporting agents with the Chat API](#topic_stk_r3r_cdb)

### Exporting visitors with the Chat API

**To export end users**

- `GET
  /api/v2/visitors/{visitor_id}`

See [Get a
Visitor](https://developer.zendesk.com/rest_api/docs/chat/visitors#get-a-visitor) in the Chat API docs.

You can get the visitor id from chat records. See [Chats](https://developer.zendesk.com/rest_api/docs/chat/chats) in the
developer docs.

Note: The Chat API has a different endpoint format than the
Support API. For details, see [Introduction](https://developer.zendesk.com/rest_api/docs/chat/introduction)
in the Chat API docs.

### Exporting agents with the Chat API

**To export agents**

- `GET /api/v2/agents`
- `GET /api/v2/agents/{agent_id}`
- `GET
  /api/v2/agents/email/{email_id}`

See [Get All
Agents](https://developer.zendesk.com/rest_api/docs/chat/agents#get-all-agents), [Get Agent by
ID](https://developer.zendesk.com/rest_api/docs/chat/agents#get-agent-by-id), and [Get Agent by Email
ID](https://developer.zendesk.com/rest_api/docs/chat/agents#get-agent-by-email-id) in the Chat API docs.

Note: The Chat API has a different endpoint format than the Support
API. For details, see [Introduction](https://developer.zendesk.com/rest_api/docs/chat/introduction)
in the Chat API docs.

## Meeting the objection obligation

Individuals from certain regions have a *right of objection*, or the right to object to
direct marketing. You may have an obligation to stop processing personal data for
direct marketing purposes when you receive an objection from an individual.

## Meeting a consent or disclosure obligation

Disclosure or notification obligations within the Zendesk
widgets can be met in a number of different ways:

- Users of Zendesk messaging in the Web Widget may
  include a [default messaging
  response](https://support.zendesk.com/hc/en-us/articles/4500737327258-Configuring-messaging-responses-for-web-and-mobile-channels#topic_kzg_ync_gnb) or provide a link to your company’s
  privacy notice.
- Users of bot-enhanced messaging in the Web Widget may
  use bot builder to include custom messages at any stage in
  the conversation, including at the transfer step before a
  conversation is handed off from the bot to an agent (which
  is when transcript creation begins).
- Users of bot-enhanced messaging in the Web Widget may
  include the name of “bot” in their selection of the name of
  the bot. Users may also include a pre-chat introduction.
- Users of live chat in Web Widget (Classic) or the
  legacy chat widget may enable a [pre-chat form](https://support.zendesk.com/hc/en-us/articles/4408882974234)
  or configure [the concierge or chat
  badge](https://support.zendesk.com/hc/en-us/articles/4408828059546) accordingly.
- If you wish to control the launching of a widget
  itself on the basis of your cookie tool, our In-Product
  Cookie Policy [here](https://support.zendesk.com/hc/en-us/articles/4408824378650-Zendesk-In-Product-Cookie-Policy) includes
  instructions on how to control each of Zendesk’s web chat
  widgets by this method. [This article](https://support.zendesk.com/hc/en-us/articles/4408834944154)explains how to install a cookie bot into a Zendesk
  help center.

See [Nofitying end users of legal terms
in Zendesk's web-based widgets](https://support.zendesk.com/hc/en-us/articles/5018479936922) for more
information.

## Disclaimer

This document is for informational purposes only and does not constitute legal advice. Readers should always seek legal advice before taking any action with respect to the matters discussed herein.