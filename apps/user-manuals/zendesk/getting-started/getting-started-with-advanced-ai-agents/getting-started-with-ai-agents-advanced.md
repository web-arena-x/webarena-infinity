# Getting started with AI agents - Advanced

Source: https://support.zendesk.com/hc/en-us/articles/8724978128282-Getting-started-with-AI-agents-Advanced

---

WithAI agents - Advanced, you can create advanced AI agents across messaging and email channels. Using generative AI, these advanced AI agents can have back-and-forth conversations with your customers, potentially resolving requests without ever requiring a human agent. You can even script conversation flows so an AI agent handles certain types of conversations with more fine-tuned control.

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **Add-on** | AI agents - Advanced |

Note: For an equivalent article about [AI agents - Essential](https://support.zendesk.com/hc/en-us/articles/6970583409690), see [Getting started with AI agents - Essential](https://support.zendesk.com/hc/en-us/articles/6478272212506).

With [AI agents - Advanced](https://support.zendesk.com/hc/en-us/articles/8725042447002), you can create advanced AI agents across messaging and email channels. Using generative AI, these advanced AI agents can have back-and-forth conversations with your customers, potentially resolving requests without ever requiring a human agent. You can even script conversation flows so an AI agent handles certain types of conversations with more fine-tuned control.

In cases where a human agent is still needed, the AI agent can gather information during the handoff that helps human agents get up to speed quickly and resolve customer issues more efficiently.

This article gives you an overview of how to start using the most important functionality included in AI agents - Advanced.

This article contains the following topics:

- [Step 1: Optimize your help center content for advanced AI agents](#topic_pl5_xc2_fhc)
- [Step 2: Configure the channels you want your advanced AI agent to work on](#topic_g2t_zc2_fhc)
- [Step 3: Create and configure your advanced AI agent](#topic_k5n_1d2_fhc)
- [Step 4: Connect your advanced AI agent to your chosen channels](#topic_tn3_bd2_fhc)
- [Step 5: Monitor your advanced AI agent’s performance](#topic_bjh_cd2_fhc)

## Step 1: Optimize your help center content for advanced AI agents

Advanced AI agents can use generative AI to create replies based on your help center content. The better your help center content is, the better your AI agents will be able to answer customer questions.

If you're just getting started with your help center, first review tickets and other resources to find issues to populate your knowledge base. See [Best practices for finding customer issues to start your knowledge base](https://support.zendesk.com/hc/en-us/articles/4408828230554).

If you already have a help center, consider optimizing your content. See [Best practices: Preparing your help center for generative AI](https://support.zendesk.com/hc/en-us/articles/9067636151834).

## Step 2: Configure the channels you want your advanced AI agent to work on

AI agents work across messaging and email channels to deliver answers to customers.
But before they can do that, you need to set up the channels you want your AI agent to work on.

If you haven't already configured these channels, see the following resources:

- **Messaging**: [Getting started with messaging for your website, help center, and mobile apps](https://support.zendesk.com/hc/en-us/articles/4408827701530)
- **Email**: [A complete guide to understanding email in Zendesk](https://support.zendesk.com/hc/en-us/articles/4887918604058)

## Step 3: Create and configure your advanced AI agent

With your help center optimized and your channels configured, it’s time to create and configure your advanced AI agent. As part of creating your AI agent, you’ll select:

- A name for your AI agent
- The type of channel it should work on (messaging or email)
- The industry you’re in
- The main language the AI agent should support

See [Creating an advanced AI agent to automatically resolve customer issues](https://support.zendesk.com/hc/en-us/articles/8357749415066).

After you create an advanced AI agent, you should also configure additional settings for it, including:

- [Step 3.1: Configure an AI agent persona to establish an identity](#topic_crt_dd2_fhc)
- [Step 3.2: Import a knowledge source to power AI-generated answers](#topic_uys_fd2_fhc)
- [Step 3.3: Create use cases to identify customer requests](#topic_ybv_gd2_fhc)
- [Step 3.4: Create generative procedures or dialogues to control responses](#topic_fv3_3d2_fhc)
- [Step 3.5: Create actions, entities, and API integrations to increase automation (Optional)](#topic_s3r_jd2_fhc)
- [Step 3.6: Configure additional AI agent settings to fine-tune behavior (Optional)](#topic_ehv_kd2_fhc)

### Step 3.1: Configure an AI agent persona to establish an identity

An AI agent’s persona controls the identity of the AI agent and how it presents itself to your customers. A persona gives the AI agent the context of who it’s working for, what your company does, what your products are, and so on.

Note: This step is required. If you don’t configure an AI agent persona, a technical error appears for every message received by the AI agent.

See [Customizing the persona, tone of voice, and pronoun formality for an advanced AI agent](https://support.zendesk.com/hc/en-us/articles/8357758773658).

### Step 3.2: Import a knowledge source to power AI-generated answers

For an AI agent to respond to customer questions with AI-generated answers, it must have access to at least one knowledge source. The knowledge source can be a help center, Confluence site or space, CSV file, or web-crawled website.

See [Importing knowledge sources for an advanced AI agent](https://support.zendesk.com/hc/en-us/articles/8357749301658).

### Step 3.3: Create use cases to identify customer requests

Next, create use cases that allow the AI agent to understand customer requests and follow the correct generative procedures or dialogues (see the next section). If you don’t create any use cases, the AI agent forms responses using only the content of your imported knowledge source, not procedures or dialogues.

See [Creating use cases for advanced AI agents](https://support.zendesk.com/hc/en-us/articles/9041901679130).

### Step 3.4: Create generative procedures or dialogues to control responses

The most powerful step in AI agent setup is to create generative procedures.
These procedures should reflect your business policies so that the AI agent can resolve customer requests in line with your policies. Procedures require less setup and maintenance from you, but they also offer you less direct control over very fine details.

See [Creating generative procedures for AI agents with agentic AI](https://support.zendesk.com/hc/en-us/articles/8979864563610).

Note: Advanced *email* AI agents can't use generative procedures, and must use dialogues instead.

In addition to generative procedures, you can also create dialogues that allow the AI agent to respond to customer requests according to scripted conversation flows. Dialogues give you a lot of control, but also require more maintenance than a procedure.

See [Using the dialogue builder to create conversation flows for advanced AI agents](https://support.zendesk.com/hc/en-us/articles/8357749494810).

AI agents that use both generative procedures and dialogues are sometimes referred to as hybrid AI agents. You can decide which use cases should use the more flexible generative procedures, and which should use more prescriptive dialogues.

See [Configure whether a use case uses a dialogue or generative procedure](https://support.zendesk.com/hc/en-us/articles/9041911005850#topic_elk_mcf_52c).

### Step 3.5: Create actions, entities, and API integrations to increase automation (Optional)

To leverage helpful details in either generative procedures or dialogues, you can create:

- **Actions** that allow the AI agent to perform actions based on the details of the session or your customer relationship management (CRM)
 system. See [Creating and adding actions for advanced AI agents](https://support.zendesk.com/hc/en-us/articles/8357756623770).
- **Entities** that hold pieces of information in customer messages that have specific meaning, such as the user’s email address. See [Creating entities in conversation flows for advanced AI agents](https://support.zendesk.com/hc/en-us/articles/8357749740698).
- **API integrations** that leverage information from other backend systems you use during your workflows. To create these API integrations, you use the integration builder. See [About the integration builder for advanced AI agents](https://support.zendesk.com/hc/en-us/articles/8357756844442).

 Note: For APIs to be used by an AI agent at the right time and in the right context, it’s extremely important to add a clear description to your APIs while building them in the integration builder.

### Step 3.6: Configure additional AI agent settings to fine-tune behavior (Optional)

At any point, you can always continue configuring the AI agent’s settings. See [Accessing and viewing settings for advanced AI agents](https://support.zendesk.com/hc/en-us/articles/8357756721178).

## Step 4: Connect your advanced AI agent to your chosen channels

At this point, your AI agent is ready to start answering customer questions. All you need to do is add it to the channels where you want it to engage with customers.
Once you do this, it begins answering customers’ questions on that channel.

For advanced messaging AI agents, the AI agent is automatically connected to Zendesk messaging, but you can [configure which messaging channels](https://support.zendesk.com/hc/en-us/articles/8357757911834) it should be the default responder for.

For advanced email AI agents, the AI agent must be [manually connected](https://support.zendesk.com/hc/en-us/articles/8357750858010) to Zendesk Support.

## Step 5: Monitor your advanced AI agent’s performance

The final and ongoing step in creating an advanced AI agent is to monitor its performance and continue to improve its efficiency. The Analytics dashboard gives you insights into key automation metrics, reports on the value of AI agent outcomes, and helps you make data-driven decisions to improve future efficiency.

See [Analyzing advanced AI agent performance with the Analytics dashboard](https://support.zendesk.com/hc/en-us/articles/9510024609178).