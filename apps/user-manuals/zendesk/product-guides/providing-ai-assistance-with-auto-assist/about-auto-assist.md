# About auto assist

Source: https://support.zendesk.com/hc/en-us/articles/9945148867866-About-auto-assist

---

Auto assist is an AI-powered assistant for your agents. Using large language model (LLM) technology, auto assist understands the contents of submitted tickets and makes suggestions to your agents on how to solve them.

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **Add-on** | Copilot |

Verified AI summary ◀▼

Auto assist is an AI-powered tool that helps agents handle tickets by suggesting replies and actions based on procedures, help center articles, and similar solved tickets. It reduces repetitive tasks and ensures consistent responses. Agents review and approve suggestions, which are tailored to the conversation's tone. Auto assist uses ticket fields and procedures to provide relevant guidance and actions.

Auto assist is an AI-powered assistant for your agents. Using large language model (LLM)
technology, auto assist understands the contents of submitted tickets and makes
suggestions to your agents on how to solve them.

With auto assist, agents spend less time on repetitive tickets, solve tickets in a more
consistent way, and ultimately close more tickets.

Watch the demo video below to see auto assist in action, or read on for more information
about auto assist.

*Zendesk agent copilot featuring auto assist (4:43)*

This article contains the following topics:

- [Understanding auto assist and how it works](#topic_vc1_r1h_b3c)
- [Understanding procedures for auto assist](#topic_rkr_344_xcc)
- [Understanding how auto assist makes suggestions](#topic_gfy_bbh_pgc)

Related articles

- [Turning on and configuring auto
  assist](https://support.zendesk.com/hc/en-us/articles/8013454025114)

## Understanding auto assist and how it works

Auto assist makes suggestions to your agents based on the following sources:

- Procedures that [you've created](https://support.zendesk.com/hc/en-us/articles/7924047699738) or that have been
  [automatically generated](https://support.zendesk.com/hc/en-us/articles/10140109521178)
- Generic information from its LLM training
- Your public help center articles
- [Similar solved tickets](https://support.zendesk.com/hc/en-us/articles/8036381366426#topic_vlg_33v_xyb)

These suggestions can be replies that the agent should send to the customer or
actions that the agent should take.

Auto assist suggestions appear in tickets in the Agent Workspace interface in place
of the composer. Any replies or actions suggested by auto assist require an agent’s
approval before being sent to the customer or performed, and are sent or performed
under the agent’s name. The customer isn’t aware of auto assist during their
interactions with the human agent.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ai_auto_assist_approve.png)

When using auto assist, agents don’t have to compose replies or execute actions
themselves, except when following [instructions you've defined](https://support.zendesk.com/hc/en-us/articles/9422234636698). Instead, agents review and
approve the replies or actions suggested by auto assist. Replies suggested by auto
assist are [automatically adapted to the conversation's tone
and writing style](https://support.zendesk.com/hc/en-us/articles/8761641980698#topic_eck_hmp_22c) so that agents can reduce the time spent editing
responses. When making suggestions, auto assist takes into account all public ticket
comments in the conversation, including previously generated comments approved by
the agent. Suggestions are made in response to end-user comments only, though, not
agent comments.

If your procedures include direct instructions for agents, then auto assist suggests
the instructions to agents when they need them based on the flow of their
conversation. Instructions are steps that agents should perform manually. For
example, your procedures might include instructions for checking your internal stock
management system if auto assist can't access it.

To learn more about the agent experience with auto assist, see [Using auto assist to solve tickets](https://support.zendesk.com/hc/en-us/articles/7051314237466).

Note: Auto assist doesn’t work on [AI agent tickets](https://support.zendesk.com/hc/en-us/articles/9204149016346).

## Understanding procedures for auto assist

A procedure is a set of written steps that tells auto assist how to advise an agent
in solving a user's request. Auto assist can suggest replies on any topic, but to
achieve best performance, creating procedures is essential. You can [write your own procedures,](https://support.zendesk.com/hc/en-us/articles/7924047699738#topic_vs3_j44_xcc) or review,
edit, and publish [AI-generated procedures](https://support.zendesk.com/hc/en-us/articles/10140109521178).

You can link the following directly in procedures to ensure that auto assist makes
the right suggestion or performs the correct action for a user's request:

- [Standard actions](https://support.zendesk.com/hc/en-us/articles/9174548349978#topic_ubt_qyr_k2c)
- [Custom actions](https://support.zendesk.com/hc/en-us/articles/9174548349978#topic_a5n_ryr_k2c)

  Custom actions are
  currently limited to changing the ticket status and ticket assignee,
  standard and custom ticket field updates, tag updates, custom API actions,
  [action flows](https://support.zendesk.com/hc/en-us/articles/8855513857306), and certain Shopify
  actions.
- Macros, if they're available to all agents
- [Agent instructions](https://support.zendesk.com/hc/en-us/articles/9422234636698), which tell agents
  how to manually perform steps that auto assist can't
- Public help center articles or other procedures

  See [About help center content in procedures](#topic_trn_d23_b3c).

You can also reference [certain ticket
fields](#topic_mgt_xvz_13c) in your procedures.

Auto assist knows which procedures to follow for a given customer request as a result
of its LLM training. You don’t need to map specific procedures to specific intents
or other ticket metadata in order for auto assist to suggest replies or actions.
Instead, auto assist understands the content of a customer’s request out of the box
and can map it to an existing procedure, if one has been created that addresses the
topic the customer is asking about.

### About ticket fields in procedures

Auto assist has access to read the following standard ticket fields:

- Assignee email
- Assignee name
- Brand
- Priority
- Requester email
- Requester name
- Status
- Subject
- Type
- Tags (can read and update but not remove)

The Priority, Type, and Tags standard fields can be updated by auto assist.

Additionally, auto assist can read all custom ticket field types (except for
lookup relationship fields) and update the following custom field types:

- Checkbox
- Date
- Decimal
- Dropdown
- Number
- Regex

You can write procedures in plain language that references these ticket fields
and auto assist will use this information to suggest the best responses.

For example, you can leverage ticket fields in auto assist procedures in the
following ways:

- Brand-aware procedures
  - Select the correct refund duration from an existing procedure based
    on the ticket brand (for example, Brand X is 20 days, but Brand Y is
    30 days).
  - Use the account verification procedure for Brand X because the
    ticket brand is X.
- Email confirmation
  - If the requester’s email address is example@acme.com, proceed with
    the refund process.

### About help center content in procedures

You can insert the following help center content in a procedure:

- **Articles**: You can insert public, published articles in a procedure.
  When you insert an article, you can choose which locale will be used.

  By
  inserting an article in a procedure, you're telling auto assist that the
  content of the article is important in the context of the procedure.

  For example, say that a customer's order must be verified before
  approving a refund. You can enter a step to gather information from an
  article with the following wording:

  "Before approving the refund,
  verify if the customer's order is meeting the requirements listed in
  <inserted article>"

  Keep in mind that auto assist can't
  comprehend images, URLs, or videos in articles. If an article relies on
  this type of content, then auto assist won't be able to understand the
  full picture.

  It's recommended to keep your help center articles
  up to date so that auto assist can make the most accurate
  suggestions.
- **Procedures**: You can insert published procedures in a procedure. When
  you insert a procedure within a procedure, you're telling auto assist to
  follow the steps in the linked procedure.

  For example, say that a customer
  indicated they want to upgrade their subscription plan. You can enter a
  step that links to a specific procedure based on some conditions with
  the following wording:

  "If the customer indicated they want to
  upgrade their subscription plan, follow step X of <inserted
  procedure>"

You can insert up to four pieces of help center content into a procedure. For
example, add a mix of articles and procedures, such as three articles and one
procedure.

## Understanding how auto assist makes suggestions

Auto assist can suggest replies and actions based on the information provided in
procedures and its generic LLM training information. It can also suggest replies
based on your public help center articles, or similar solved tickets, when a
relevant procedure or article isn't available. It can't suggest replies or actions
based on other sources.

Auto assist can suggest replies on any topic based on the following sources:

1. AI-generated procedures or procedures that you've created. Procedures are
   essential to achieving the best performance.

   Auto assist uses this procedure
   content, along with its built-in LLM training, to generate suggested replies
   or actions, which it then presents to agents as they work on tickets in the
   Agent Workspace.

   Procedure content can also include direct agent
   instructions. These types of instructions are steps that agents should
   follow and perform manually.
2. If a relevant procedure isn't found, then auto assist uses your public help
   center articles to generate suggested replies. Only articles with a brand and
   language matching the ticket brand and language are used for reply generation.
   For example, if the brand on a ticket is Obscura, then only articles with the
   Obscura brand are considered.
3. If a relevant procedure or help center article isn’t available, then auto assist
   uses similar solved tickets to generate suggested replies.

Auto assist suggestions appear in tickets in the Agent Workspace interface in place
of the composer. If you have permission, you can view the source auto assist used to
generate the suggestion. See [Viewing sources for auto assist
suggestions](https://support.zendesk.com/hc/en-us/articles/7051314237466#topic_abz_r5t_khc) to learn more.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/copilot_auto_assist_suggestion_sources.png)

If you don't have permission to view an auto assist suggestion's source, then refer
to the list above to understand what source may have been used to generate the
suggestion.

Examples where auto assist can suggest replies include:

- Advising the customer on buying a product or service sold by your company
- Explaining a business policy to the customer
- Helping the customer troubleshoot a problem with a product

Examples of procedures where auto assist can suggest replies and actions include:

- Checking the status of a current order in Shopify, or canceling and refunding
  specific items or whole orders in Shopify
- Querying and modifying your own internal business systems or performing
  third-party actions via API

Examples of procedures where auto assist can suggest direct agent instructions you've
written include:

- Telling an agent to check your internal stock management system and adding a
  refunded item as 'back in stock'
- Instructing an agent on how to create and validate a new user account in
  your company's human resources system