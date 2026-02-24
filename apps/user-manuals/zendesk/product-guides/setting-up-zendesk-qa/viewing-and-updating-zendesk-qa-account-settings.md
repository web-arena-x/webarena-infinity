# Viewing and updating Zendesk QA account settings 

Source: https://support.zendesk.com/hc/en-us/articles/7043669430426-Viewing-and-updating-Zendesk-QA-account-settings

---

In Zendesk Quality assurance (QA) account settings, admins can configure settings that apply to the entire account and all workspaces.

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **Add-on** | Quality Assurance (QA) or Workforce Engagement Management (WEM) |

Verified AI summary ◀▼

Admins can manage account settings to enhance quality assurance processes. Configure general settings like default workspaces and automatic scoring, manage connections for data integration, and set up notifications for user engagement. Utilize scorecards and spotlight insights to evaluate agent performance and identify improvement areas. AI insights offer advanced evaluation tools for deeper analysis and learning opportunities.

Location:  Zendesk QA > Settings

In Zendesk Quality assurance (QA) account settings, admins can configure settings
that apply to the entire account and all workspaces.

This article contains the following sections:

- [Accessing account settings](#topic_hd5_w15_fgc)
- [Managing general settings](#topic_wsw_cly_ydc)
- [Managing connection settings](#topic_ym1_wnf_zdc)
- [Managing account notification
  settings](#topic_trv_wnf_zdc)
- [Managing scorecard, category, and root
  cause settings](#topic_fbm_xnf_zdc)
- [Managing AI insights settings](#topic_ekx_yxq_mfc)

Related article:

- [Viewing and updating personal settings in Zendesk QA](https://support.zendesk.com/hc/en-us/articles/8557785343898)

## Accessing account settings

Admins can access account settings from the settings menu.

**To access the account settings page**

1. In [Quality assurance](https://support.zendesk.com/hc/en-us/articles/4408838272410), click your profile icon in the top-right
   corner.
2. Click **Settings** (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/zqa_settings.png)).
3. From account settings, view and manage the following:
   - [General settings](#topic_wsw_cly_ydc)
   - [Connections](#topic_ym1_wnf_zdc)
   - [Notifications](#topic_trv_wnf_zdc)
   - [Scorecards](#topic_fbm_xnf_zdc)
   - [AI](#topic_ekx_yxq_mfc)

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/zqa_account_settings.png)

## Managing general settings

General account settings allow you to define the experience for all workspaces.

On the General account settings page, admins can view and configure all of the following:

|  |  |
| --- | --- |
| **Setting or action** | **Description** |
| Default workspace | [Once given access to Zendesk QA](https://support.zendesk.com/hc/en-us/articles/10093676975898#topic_bqv_vqn_shc), all new users are automatically assigned to the account’s default workspace. You cannot remove users from the account’s default workspace. However, you can [create additional workspaces](https://support.zendesk.com/hc/en-us/articles/9202963091866) and then [change the default workspace](https://support.zendesk.com/hc/en-us/articles/10345461586586) if needed. |
| Start of the week | Day the week starts on in Zendesk QA. Options are Monday or Sunday. |
| Automatic scoring with AutoQA | Turns [autoscoring](https://support.zendesk.com/hc/en-us/articles/7043747123354) on or off.  Turning on automatic scoring with AutoQA allows Zendesk QA to automatically evaluate and score agents.  Turning it off means user interactions are not automatically scored.  Automated scores contribute to the [auto quality score (AQS)](https://support.zendesk.com/hc/en-us/articles/9019507481242), but the [internal quality score (IQS)](https://support.zendesk.com/hc/en-us/articles/7043724913690#ariaid-title3) remains based solely on manual reviews. Participating agents must be Zendesk QA users and members of the workspaces where AutoQA categories are configured. Autoscoring categories are indicated by a hologram icon (). |
| LLM-based AutoQA | Controls whether Auto-QA processing by large language models (LLMs) is on or off. Turning on LLM-based AutoQA allows it to [automatically score](https://support.zendesk.com/hc/en-us/articles/7043747123354#understanding_autoscoring_categories) user interactions with AI.  Turning off [LLM integration](https://support.zendesk.com/hc/en-us/articles/6059285322522) doesn’t turn off the AutoQA feature completely. When it’s turned off, the following data remains:  - [AutoQA categories](https://support.zendesk.com/hc/en-us/articles/7043747123354) powered by the AI   model remain on the scorecard but are no longer automatically scored. - Manually added [root causes](https://support.zendesk.com/hc/en-us/articles/7043759820826) remain but not LLM-based   root causes. - Historical data remains on the [AutoQA dashboard](https://support.zendesk.com/hc/en-us/articles/9019507481242).  When this option is turned off, [AI insights based on custom prompts](https://support.zendesk.com/hc/en-us/articles/9224552305946), some [spotlight insights](https://support.zendesk.com/hc/en-us/articles/7043759586074#topic_lmq_fvh_xdc), and some AutoQA categories language options won't function.  AutoQA uses AI and large language models (LLMs) to automatically score specific categories. Your data is processed under a strict Data Processing Agreement (DPA) and is never used to train any models. [Learn about generative AI at Zendesk](https://support.zendesk.com/hc/en-us/articles/6059285322522-About-generative-AI-features-in-Zendesk). |
| Hide reviewer identities from agents | Controls whether reviewer anonymization is on or off. Turning on this option means [agents can’t identify the reviewer](https://support.zendesk.com/hc/en-us/articles/9228986629786) giving them an evaluation. This can help ensure unbiased feedback and foster a fair and constructive QA process. |
| Deleted conversations | Allows you to manage or delete reviews associated with deleted tickets in Zendesk QA.  Deleting a ticket in Zendesk Support (or [another help desk](https://support.zendesk.com/hc/en-us/articles/7043712839450)) doesn't affect associated conversation reviews. You can still access a review using the ticket ID. Deleting reviews in Zendesk QA removes the ticket and all related review data. |

## Managing connection settings

Connection settings allow you to add, manage, and monitor connected data sources.

On the Connection settings page, admins can view and configure the following:

|  |  |
| --- | --- |
| **Setting or action** | **Description** |
| Custom integration | Allows you to add a new connection with a [custom integration](https://support.zendesk.com/hc/en-us/articles/7043669282714). A custom integration allows you to use an API to import data about conversations or users in bulk and export statistical data. Some technical experience may be required. |
| Create connection | Allows you to [add and configure](https://support.zendesk.com/hc/en-us/articles/7043712839450) advanced options for help desk connections in Zendesk QA.  Note: You must contact your [Zendesk Sales Representative](https://support.zendesk.com/hc/en-us/articles/4408843597850#h_01FB4BHCQN7EX10B0FK7JBTS78) before adding a new connection. |
| Edit connection | Allows you to update a connection, including the name, account ID, and token. |
| Delete connection | Allows you to remove a connection from Zendesk QA. This action is irreversible. Deleting a connection removes all help desk-related data for this connection from Zendesk QA, including conversations, fields, and tags. Submitted reviews are not affected and remain visible in specific views. |

## Managing account notification settings

Notification settings allow you to define the default notification behavior for new users.

Notifications are sent in the [user's UI language](https://support.zendesk.com/hc/en-us/articles/4408884044058).

On the Notification settings page, admins can view and configure the following:

|  |  |
| --- | --- |
| **Setting or action** | **Description** |
| Override settings for all users | Allows you to prevent users from [customizing their personal settings](https://support.zendesk.com/hc/en-us/articles/8557785343898). |
| Email reports | Allows users to receive automated email reports with statistics about given and received reviews. Options include the following:  - Daily - Weekly - Monthly |
| Notifications | Allows users to receive notifications for newly received reviews, replies in threads, mentions in comments, and disputes related to them. When you configure a new notification schedule, the system first checks whether a notification of the same type has been sent within a similar time frame. If it finds such a notification, it holds the new notification and schedules it to be sent later. If no matching notification is found, the system sends the new notification immediately.  For example, when you configure notifications to be sent Every 3 hours, the system checks whether a notification of the same type has been sent within the past 3 hours. If it finds such a notification, it holds the new notification and schedules it to be sent later. If no matching notification is found, the system sends the new notification immediately.  Options for each notification type include the following:  - Instantly - Every 3 hours - Every 6 hours - Daily - Weekly - Monthly - Off |
| Reminders | Allows you to send automated weekly reminders to users who haven’t done any reviews. Reminders are sent at the [start of the week](https://support.zendesk.com/hc/en-us/articles/7043669430426#topic_wsw_cly_ydc) if users haven't completed any reviews. |
| Slack integrations | Allows you to set up an integration so users can [receive notifications directly in Slack](https://support.zendesk.com/hc/en-us/articles/7043747899674). |

## Managing scorecard, category, and root cause settings

[Scorecards](https://support.zendesk.com/hc/en-us/articles/8875998154906) are a powerful tool for evaluating agent performance,
identifying areas for improvement, and ensuring that your team meets organizational goals.
Scorecard settings allow you to create and manage scorecards, categories, and root causes.
All scorecards, categories, and root causes are listed here.

On the Scorecards page, admins can view and configure the following:

|  |  |
| --- | --- |
| **Setting or action** | **Description** |
| Settings | Allows you to view or update the following [scorecard settings](https://support.zendesk.com/hc/en-us/articles/8875998154906#topic_ufd_t3n_zfc):  - Using emojis instead of numbers. - Letting people skip categories. All rating scales within existing   scorecards will include N/A as an option. |
| Create | Allows you to [create a new scorecard](https://support.zendesk.com/hc/en-us/articles/7043760215194) or [create a new category](https://support.zendesk.com/hc/en-us/articles/7043712922522). |
| Scorecards | Allows you to [view and manage scorecards](https://support.zendesk.com/hc/en-us/articles/8875998154906). |
| Categories | Allows you to [view and manage categories](https://support.zendesk.com/hc/en-us/articles/8992409602842). |
| Root causes | Allows you to [view and manage root causes](https://support.zendesk.com/hc/en-us/articles/7043759820826). |
| Automatic scoring with AutoQA status | Allows you to see the AutoQA status. Provides shortcuts to access the [AutoQA account settings](#topic-1__ul_k2h_j15_fgc) and [AutoQA dashboard](https://support.zendesk.com/hc/en-us/articles/9019507481242). |

## Managing AI insights settings

[AI insights](https://support.zendesk.com/hc/en-us/articles/9224552305946) automatically surface valuable
improvements and learning opportunities, speeding up the evaluation process. AI insights
settings allow you to create and manage AI insights.

On the AI settings page, admins can view and configure the following:

|  |  |
| --- | --- |
| **Setting or action** | **Description** |
| Create new AI insights | Allows you to create AI insights, including the following:  - [Creating AI prompt-based rating   categories](https://support.zendesk.com/hc/en-us/articles/9277382490138) - [Creating AI prompt-based spotlight   insights](https://support.zendesk.com/hc/en-us/articles/9327313916570) - [Creating exact text-match custom rating   categories](https://support.zendesk.com/hc/en-us/articles/9302967236890) - [Creating exact text-match AI insights   spotlights](https://support.zendesk.com/hc/en-us/articles/9486586566170) |
| View and manage system, exact text-match, and prompt-based categories and spotlights | Allows you to manage AI insights, including the following:  - [Managing autoscoring categories](https://support.zendesk.com/hc/en-us/articles/8992409602842) - [Managing AI spotlight insights](https://support.zendesk.com/hc/en-us/articles/9483275885466) |