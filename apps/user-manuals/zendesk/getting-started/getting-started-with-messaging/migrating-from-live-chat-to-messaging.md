# Migrating from live chat to messaging

Source: https://support.zendesk.com/hc/en-us/articles/4408821531162-Migrating-from-live-chat-to-messaging

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

Zendesk's own messaging functionality allows you to deliver rich, modern, and
automated conversation experiences on your website and mobile apps.

This article describes how to migrate your account from Zendesk live chat to
messaging.

This article includes the following sections:

- [Pre-migration tasks](#topic_c1g_2fq_wnb)
- [Preparing for migration](#topic_m1x_qhq_nkb)
- [Migrating from live chat to messaging](#topic_cyn_4lq_nkb)
- [After the migration](#topic_lwk_2xq_nkb)

Related articles:

- [Resources for migrating from live chat to messaging](https://support.zendesk.com/hc/en-us/articles/4408845841946)
- [About messaging](https://support.zendesk.com/hc/en-us/articles/4408846454682)
- [Enabling messaging](https://support.zendesk.com/hc/en-us/articles/4408832031898)

## Pre-migration tasks

Before starting the migration process, we recommend you do the following:

- **Evaluate your account**. Use our checklist to determine whether your account is in
  good shape for migrating to messaging. See [Evaluating your account for migration from live chat to
  messaging](https://support.zendesk.com/hc/en-us/articles/4408838065434).
- **Compare messaging and live chat**. Messaging and Zendesk Chat share many
  of the same capabilities, and messaging offers features that aren’t available in Zendesk
  Chat. For a complete assessment of feature parity, see [Why migrating from live chat to messaging is the right choice](https://support.zendesk.com/hc/en-us/articles/4408834108186).
- **Understand how migrating to messaging may impact your workflow**. If you
  set up messaging to adopt the live chat conversational style there are minimal impact to
  your workflows. If you choose to adopt other conversational styles there is a possibility
  your workflows could be affected. See [About conversational support with messaging](https://support.zendesk.com/hc/en-us/articles/4408846454682).
- **Review how messaging impacts your functionality.** Activating messaging
  can impact features across your account, including the Web Widget, mobile SDKs, automated
  conversations, and Agent Workspace. See [Understanding how activating messaging changes your
  account](https://support.zendesk.com/hc/en-us/articles/4408832031898#topic_nbq_ftm_jnb).
- **Learn about automated conversations**. When you migrate to messaging, an
  AI agent can be your first responder for customer requests. See [Creating an AI agent for your web and mobile channels](https://support.zendesk.com/hc/en-us/articles/4408824263578).

## Preparing for migration

Before migrating, we recommend taking the time to make sure your account meets the
requirements for using messaging, take a look at your customer service needs, and prepare
your agents for their new work environment.

### Checking your account requirements

If your account meets the requirements for using messaging, you'll see
an in-product message on your account's Channels page in the Admin Center.

To migrate to messaging, you *must* have an account with:

- Zendesk Suite OR Support + Chat (Team plan or higher) with the Agent
  Workspace activated. See [Activating and deactivating the Zendesk Agent Workspace](https://support.zendesk.com/hc/en-us/articles/4581758611866).

Before migrating to messaging, we *recommend* you have an account
with:

- An active help center, with at least 10 articles that cover
  commonly-asked questions.

  Note: A help center is *required* if you plan to [reference help center content](https://support.zendesk.com/hc/en-us/articles/4408821281818#topic_ewc_cmf_j4b) in AI agent
  responses.

See [About conversational support with messaging](https://support.zendesk.com/hc/en-us/articles/4408846454682) for
more information.

### Preparing your agents for messaging

Share the links below with your agents, to introduce them to messaging and how
their workflows may change.

- [Agent Workspace for messaging](https://support.zendesk.com/hc/en-us/articles/4408821905434) introduces agents
  to their main screen, where they’ll be interacting with customers in real time, as well
  as working with Support tickets.
- [Managing conversation handoff and handback](https://support.zendesk.com/hc/en-us/articles/4408824482586)
  explains how messaging conversations are passed from your conversation bot to agents, as
  well as how and when a conversation ends.
- [Translating conversations in the Zendesk Agent
  Workspace](https://support.zendesk.com/hc/en-us/articles/4408832500506) explains the automatic translation feature, how it works and how
  agents can manage it.

## Migrating from live chat to messaging

When you’re ready, you can begin the move from live chat to messaging. In this
section, we’ll offer a high-level guide to the tasks you may need to perform to migrate to
and set up messaging. Use the links below for detailed information and specific
instructions.

Note that you can [test how your messaging configuration performs](https://support.zendesk.com/hc/en-us/articles/4408835784602) before launching it
in your production instance.

Important: If you are converting a Web Widget (Classic) over to the messaging
Web Widget, any active live chats will end and any in-progress tickets will remain
pending. Before doing so, we recommend that you close out any active live chats, take
agents offline, be aware of any pending tickets, and consider making this change in an
off-peak period.

1. [Activate messaging at the account level](https://support.zendesk.com/hc/en-us/articles/4408832031898).
2. [Update your Chat settings](https://support.zendesk.com/hc/en-us/articles/4408832031898#topic_tgg_5xj_knb) to ensure a smooth
   transition from live chat to messaging
3. Make sure your tickets get to your agents:
   - [Organize agents into groups](https://support.zendesk.com/hc/en-us/articles/4408821752346)
   - [Configure ticket routing](https://support.zendesk.com/hc/en-us/articles/4408829019162)
4. Activate messaging on your channels:
   - [Working with messaging in the Web Widget](https://support.zendesk.com/hc/en-us/articles/4408828655514)
   - [Working with messaging in your Android and iOS
     apps](https://support.zendesk.com/hc/en-us/articles/4408834810394)

## After the migration

Messaging is functional as soon as it is enabled, as described in the
previous section. After migration, you can refine your messaging setup in the following
ways:

- [Creating an out-of-office message for
  messaging](https://support.zendesk.com/hc/en-us/articles/4408842866074)
- [Designing an AI agent](https://support.zendesk.com/hc/en-us/articles/6970583409690)
- [Allowing customers to continue their conversation over email](https://support.zendesk.com/hc/en-us/articles/4408829095706)
- [About the CSAT (customer satisfaction) user experience for email and messaging](https://support.zendesk.com/hc/en-us/articles/4408886173338)
- [Messaging reporting in Zendesk Agent Workspace](https://support.zendesk.com/hc/en-us/articles/4408822342938)

For all the messaging resources, see [Messaging resources](https://support.zendesk.com/hc/en-us/articles/4408836242714).