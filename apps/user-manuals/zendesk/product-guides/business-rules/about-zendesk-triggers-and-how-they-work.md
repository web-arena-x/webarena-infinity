# About Zendesk triggers and how they work

Source: https://support.zendesk.com/hc/en-us/articles/4408822236058-About-Zendesk-triggers-and-how-they-work

---

Zendesk has a variety of business rules that can be used to automate record updates and
notifications across products. Triggers are business rules you define that run
immediately after a record, such as a ticket, is created or updated and automatically
perform actions if specified conditions are met. This article explains the different
types of Zendesk triggers and essential facts about them.

This article contains the following topics:

- [Types of Zendesk triggers](#topic_pnv_xsq_4bc)
- [Essential facts about Zendesk triggers](#topic_xzp_zsq_4bc)
- [Anatomy of triggers](#topic_ahv_3lx_4bc)

## Types of Zendesk triggers

Triggers are managed separately by Zendesk product.

The following trigger types exist, organized by Zendesk product:

**Support**

- **Ticket triggers**: The first and most common type of trigger, running
  any time a ticket is created or updated. There are several [standard ticket triggers](https://support.zendesk.com/hc/en-us/articles/4408828984346) that
  Zendesk provides to help you get started with your Support
  workflows.

  Although ticket triggers are traditionally thought of as
  only applying to email tickets (including tickets submitted through web
  forms and APIs), tickets are also created for live chats, messaging
  conversations, and calls. Ticket triggers support a "Ticket channel is
  {channel}" condition that allows you to select most of the Zendesk [channels](https://developer.zendesk.com/documentation/ticketing/reference-guides/via-types/). Because of this, it
  can be helpful to think of chat and messaging triggers as a subset of
  ticket triggers that just happen to be managed on a separate page in
  Admin Center.

  See [Creating ticket triggers for
  automatic ticket updates and notifications](https://support.zendesk.com/hc/en-us/articles/4408886797466).
- **Object triggers**: Run any time a record is created or updated for the
  specified [custom object](https://support.zendesk.com/hc/en-us/articles/5914453843994). Requires you to
  activate and [create](https://support.zendesk.com/hc/en-us/articles/5392409465370) at least one custom
  object.

  See [Understanding object
  triggers](https://support.zendesk.com/hc/en-us/articles/6294230624410).

Managed on Admin Center > Objects and rules > Business rules >
Triggers.

**Chat**

- **Chat triggers**: Run when a selected event occurs. When creating
  a chat trigger, admins must specify a single event that causes the trigger
  to run. There are several [standard chat triggers](https://support.zendesk.com/hc/en-us/articles/4408834380442) that
  Zendesk provides to help you get started with your live chat
  workflows.

  Managed on the Chat dashboard: Admin Center > Objects and rules > Business rules > Chat
  triggers.

  See [Working with chat
  triggers](https://support.zendesk.com/hc/en-us/articles/4408884148762).
- **Messaging triggers**: Messaging triggers function the same way chat
  triggers do. When creating a messaging trigger, admins must specify a single
  event that causes the trigger to run. There are several [standard messaging triggers](https://support.zendesk.com/hc/en-us/articles/5973077601562#topic_x3c_btn_q5b) that
  Zendesk provides to help you get started with your messaging
  workflows.

  For some accounts, messaging triggers are managed in Admin
  Center > Objects and rules > Business rules > Messaging triggers. If you
  don't see this page, your messaging triggers are still created and
  managed on the Chat dashboard: Admin Center > Objects and rules > Business rules > Chat
  triggers.

  See [Working with messaging
  triggers](https://support.zendesk.com/hc/en-us/articles/6058753945242).

## Essential facts about Zendesk triggers

This section distills some essential facts about triggers as a whole. These are
explained in greater detail in the documentation. See [Triggers resources](https://support.zendesk.com/hc/en-us/articles/4408843730458-Triggers-resources).

- Triggers are created from conditions and actions. Conditions set the qualifications needed for
  the trigger to fire, and actions represent what will be performed when those
  qualifications are met.
- Triggers always run, or check the conditions, immediately after the qualifying event happens.
  For ticket and object triggers, qualifying events are record creation and updates.
  For chat, messaging, and sale triggers, the qualifying event is defined by an admin
  when configuring a trigger.
  - The one exception is ticket triggers don't run or fire on tickets after they
    are closed. However, ticket triggers can fire when a ticket is being set to
    closed, except when the ticket is automatically closed by the system after
    28 days.
- Changes that automations make to tickets can cause triggers to run. Configure
  triggers and automations with the understading that changes made by automations can
  impact triggers and vice versa. See [About automations and how they work](about-automations-and-how-they-work.md)
- Triggers only fire, or apply their actions, if the trigger's set conditions are met.
- Actions applied by one ticket trigger can affect how other triggers run and fire for a ticket.
  However, other types of triggers run simultaneously without this looping
  behavior.
- Triggers, like all business rules, must be smaller than 65 KB.

## Anatomy of triggers

Triggers are comprised of two parts: conditions and actions. You combine these to
create ‘if’ and ‘then’ statements. *If* the record contains a certain set of
conditions, *then* the actions make the updates to the record and can send
notifications. Chat, messaging, and sales triggers also require an admin to specify
the event that must occur for the trigger to run.

### Conditions

Condition statements are the "if" part of a trigger. They're structured as a
condition (sometimes called *category*), an operator, and a value.

The available condition options vary by type of trigger. For ticket triggers,
messaging triggers, and chat triggers, there are predefined lists of supported
conditions. For object triggers, the supported conditions depend on the custom
object's fields.

There are two types of conditions – *all* conditions and *any*
conditions. In practice, all of the *all* conditions must be true in order
for the trigger's conditions to be met, while one or more of the *any*
conditions must be true in order for the trigger's conditions to be met. For
ticket triggers and object triggers, you can use a combination of *all* and
*any* conditions. However, for chat and messaging triggers, you must
choose between using *all* and *any* conditions.

For more information, see:

- [Building ticket trigger condition
  statements](https://support.zendesk.com/hc/en-us/articles/4408893545882#topic_i3y_fkz_1cb)
- [Building object trigger condition
  statements](https://support.zendesk.com/hc/en-us/articles/7313293784218#topic_ey3_bbb_fzb)
- [Chat and messaging trigger
  conditions](https://support.zendesk.com/hc/en-us/articles/4408842880282#topic_d3p_q5f_rhb)
- [Creating sales triggers](https://support.zendesk.com/hc/en-us/articles/4418343631002)

### Actions

Action statements describe what happens when a trigger's conditions are met.
These are the "then" parts of a trigger. When we say a trigger *fires*, we
mean it's applying the actions.

Action statements are structured as an action and a value.

Similar to conditions, the available actions vary by type of trigger. A
predefined list of supported actions are available for ticket triggers,
messaging triggers, and chat triggers. For object triggers, there are some
predefined notification actions, but the rest of the available actions depend on
the custom object's fields.

For more information, see:

- [Building ticket trigger action
  statements](https://support.zendesk.com/hc/en-us/articles/4408893545882#topic_ncz_4kz_1cb)
- [Building object trigger action
  statements](https://support.zendesk.com/hc/en-us/articles/7313293784218#topic_rzv_bbb_fzb)
- [Chat and messaging trigger
  actions](https://support.zendesk.com/hc/en-us/articles/4408842880282#topic_hxz_q5f_rhb)
- [Creating sales triggers](https://support.zendesk.com/hc/en-us/articles/4418343631002)

### Run events

When we say a trigger *runs*, we mean the trigger's conditions are evaluated
and, if met, the specified actions occur. Ticket triggers and object triggers
run automatically any time a ticket or a custom object's record, respectively,
is created or updated. However, chat, messaging, and sales triggers only run
when a user-specified event occurs. When creating one of these triggers, an
admin must select the run event from a drop-down.

For more information, see:

- [Chat and messaging trigger run
  events](https://support.zendesk.com/hc/en-us/articles/4408842880282#topic_pgr_rsj_d4b)
- [Creating sales triggers](https://support.zendesk.com/hc/en-us/articles/4418343631002)