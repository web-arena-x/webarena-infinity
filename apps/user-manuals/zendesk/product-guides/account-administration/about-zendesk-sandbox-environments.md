# About Zendesk sandbox environments

Source: https://support.zendesk.com/hc/en-us/articles/6150628316058-About-Zendesk-sandbox-environments

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Enterprise or Enterprise Plus |

| | |
| --- | --- |
| **Support** | Enterprise |

Verified AI summary ◀▼

Use sandbox environments to test and experiment without affecting your live setup. Sandboxes replicate your settings and data, allowing you to try new workflows, integrations, and train agents safely. Note that some features like SMS and advanced encryption aren't supported, and data isn't continuously synced. Regularly update sandboxes to keep them current, and remember changes in sandboxes don't impact your live environment.

A sandbox is a test environment with the replicated configurations and data from your production environment. You can use the sandbox to test, learn, and make mistakes without affecting your production environment.

This article contains the following topics:

- [Essential facts about sandboxes](#topic_ldj_1md_5yb)
- [Working with sandboxes](#topic_eyb_2pd_5yb)

## Essential facts about sandboxes

Consider the following information when using sandboxes:

- The availability of sandbox environments vary by plan:
 - Support Enterprise includes one sandbox.
 - Suite Enterprise and Enterprise Plus include two sandboxes.
 - Support Professional and above and Suite Growth and above can purchase sandbox environments. Contact your sales representative or [Zendesk Customer Support](https://support.zendesk.com/hc/en-us/articles/4408843597850)
    to purchase sandboxes as an add-on.

 Note: On Suite Growth and Support Enterprise plans and above, you can also contact [Zendesk Customer Support](https://support.zendesk.com/hc/en-us/articles/4408843597850)
 to request a sandbox trial of a different plan or add-on with your existing account configurations. These sandbox trials aren't counted as regular sandboxes and you can't deploy changes from sandbox trials to production.
- The production instance owner is listed as the sandbox owner by default.
 This is true even if another admin creates or replaces the sandbox.
- To provide a more realistic testing environment, all sandboxes take the following settings from your production instance of Zendesk Support:
 - Templates (standard emails, welcome emails, etc.)
 - Branding (colors, account names, etc.)
 - Settings (channels, agent permissions, etc.)

 A lot of your production content is also replicated, including tickets and their associated end users. See [Understanding data replication](#topic_n2f_gsm_tgb).
- In sandbox environments, closed tickets are automatically archived after three days.
- The activation status of the Zendesk Agent Workspace is replicated in all new sandbox environments.
- Some security settings aren't replicated in sandbox environments.
 However, if you're using two-factor authentication (2FA), that will continue to work in your sandbox, too, as long as the user has a password set in the production account.
- Sandboxes reflect a moment in time for your production account settings and data. Replicating settings and data isn't instantaneous and the data doesn't stay synchronized with production after the sandbox is created.
 However, is it possible to [deploy configurations](https://support.zendesk.com/hc/en-us/articles/9474556880922)
 from production to your sandbox, and you can [sync product and add-on subscription changes](https://support.zendesk.com/hc/en-us/articles/7414296161818).
- We recommend deleting your old sandboxes and creating new ones regularly to keep your sandbox environment up to date.
- Deleting a sandbox is a permanent change and can't be recovered.
- Changes you make in a sandbox don't affect your production environment.
- You can start trials for other Zendesk products in your sandbox.
 Any trial is subject to limitations and a fixed time limit, as specified when you sign up for the trial.
 - Sandboxes created after May 2023 include a Talk trial of an unlimited duration, as long as the production account has an active Talk subscription or trial. The sandbox Talk trial is suspended when the credits run out.
- When a sandbox is provisioned, two advanced AI agents are automatically created for you, one for messaging and one for email.
 - The messaging AI agent is automatically integrated with Zendesk messaging, but you can [configure which messaging channels](https://support.zendesk.com/hc/en-us/articles/8357757911834)
    it should be the default responder for and [manage settings](https://support.zendesk.com/hc/en-us/articles/10050437105946)
    related to messaging channels.
 - The email AI agent must be [manually connected](https://support.zendesk.com/hc/en-us/articles/8357750858010)
    to Zendesk Support.
 - If needed, you can [clone additional advanced AI agents](https://support.zendesk.com/hc/en-us/articles/8357749415066#topic_mkr_hb3_23c)
    from your production environment into your sandbox or [create a new AI agent](https://support.zendesk.com/hc/en-us/articles/8357749415066#topic_nyf_s12_fhc)
    in your sandbox environment.
- SMS text messaging isn't supported in sandbox environments.
- Sandbox environments can't be created after activating [advanced encryption](https://support.zendesk.com/hc/en-us/articles/5043582015898).

## Working with sandboxes

Sandboxes provide a test environment that closely mirrors your production instance in configuration and data. This enables you to more accurately test updates to workflows, experiment with integrations and new business rules, and train agents without affecting production.

When creating a sandbox, you can choose how many tickets are replicated, up to 10,000. The end users associated with the tickets are also replicated.

Additionally, the following content is replicated:

- Brands
- Dynamic content
- Ticket fields
- Ticket forms
- User fields
- Organizations
- Organization fields
- Targets (set to inactive in the sandbox by default)
- Groups
- Custom roles
- Shared views
- Shared macros
- Triggers
- Trigger categories
- Automations
- Agents
- Group memberships
- Support addresses (Internal support addresses, such as *help@mybusiness.zendesk.com*, are copied with slight modification to contain the brand's unique subdomain within the sandbox. If you've configured external support addresses, such as *help@mybusiness.com*, they're converted to internal addresses when replicated to a sandbox using the following structure:
 *help-at-mybusiness-com@sandboxsubdomain.zendesk.com*.
 If you've set an external support address as the default, the sandbox reverts to using the original default internal address:
 *support@mybusinesssandbox.zendesk.com*.)
- Webhooks (set to inactive in the sandbox by default)
- Apps (only free [Marketplace apps](https://www.zendesk.com/marketplace/apps/)
 that don't require authentication or additional configuration at installation)
- [Custom objects](https://support.zendesk.com/hc/en-us/articles/5914453843994)
 (this doesn't include custom object records, lookup fields related to custom objects, or legacy custom objects)
- (Optional, with [Copilot add-on](https://support.zendesk.com/hc/en-us/articles/7908817636378))
 Guide default brand and [auto assist procedures](https://support.zendesk.com/hc/en-us/articles/7924047699738)

For more information about how data replication works and limitations of the replicated data, see [Understanding data replication in sandboxes](#topic_n2f_gsm_tgb).

### Understanding how data replication works

Replication occurs automatically when you create a sandbox through [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb).
The replication retrieves data from the production instance and creates the configuration and content in the sandbox, creating a new subdomain. The process will not affect the performance of your production instance. Data is only retrieved from the production instance, so nothing will be added, updated, or deleted there. For a complete list of the data that is replicated, see [Working with sandboxes](#topic_eyb_2pd_5yb).

The configuration of your sandbox instance will change rapidly while the replication is occurring, so we recommend waiting to use it until the replication completes. The time it takes for a replication to complete varies depending on the amount of content involved. A small amount of fields, business rules, and data takes less time, ranging from a few minutes to a couple hours, while a full copy with up to 100,000 tickets, a million organizations, and the related users can take up to a week or more to complete. When the replication is complete, the status of the sandbox changes to *Active* . To expedite the creation of sandboxes, you can use the express sandbox setting to reduce the amount of organization data that is replicated.

To complete the replication, Zendesk creates an internal copy of the data to be migrated. Once this migration is complete, this copy is deleted.

After a sandbox is created, you can [update the product and add-on subscriptions](https://support.zendesk.com/hc/en-us/articles/7414296161818)
to reflect changes to your production account and snapshots to [deploy configuration changes](https://support.zendesk.com/hc/en-us/articles/9474556880922).
No other replicated data can be updated after a sandbox is created.

You can view creation reports to help you better understand exactly what was and wasn't replicated and why. See [Generating a creation report for a sandbox](https://support.zendesk.com/hc/en-us/articles/7502268225690).

#### Data retention policies for sandboxes

You can perform a maximum of 10 replications per month.

When team members don't log in or otherwise use your sandbox for 90 days, the sandbox and its data are deleted after the specified data retention period.

#### Limitations of replicated data

The replication will be as close of an exact copy of the production instance as possible. However, there are several situations where the copy cannot be exact:

- Sandbox test environments include Zendesk Support functionality in Zendesk Suite only. They do not include, for example, Talk or Guide.

 Note: There is one exception to this if you have the [Copilot add-on](https://support.zendesk.com/hc/en-us/articles/7908817636378), in which case, you can choose to replicate your default Guide brand and [auto assist procedures](https://support.zendesk.com/hc/en-us/articles/7924047699738)
 in sandboxes.
- Brands are replicated, but because brand names need to be unique across all Zendesk instances, they cannot be an exact match. The brand names will be modified to contain a unique string.
- Webhooks are replicated. However, all webhooks are deactivated in the Sandbox by default to prevent unintended interactions with the live APIs they're designed to connect to.
- User emails will be invalidated before being added to the sandbox instance by the use of the @example.com domain. This is to prevent emails from being inadvertently sent to your users.
 This includes both agents and end-users. An administrator can reverse the invalid emails for testing by editing the users' email addresses.
- APIs are enabled, but API tokens must be recreated.
- Apps and EAP functionality in production are deactivated within the sandbox upon creation but can be manually enabled.
- Side conversations are deactivated within the sandbox upon creation but can be manually enabled.
- Non-closed tickets that haven't been updated in the last six months, closed tickets, linked incident tickets, and ticket sharing agreements are not replicated.
- [Targets](https://support.zendesk.com/hc/en-us/articles/4408883282458)
 requiring a password will be replicated, but they will have invalid credentials and be in a disabled state.
- Invalid rules and objects that reference unsupported configurations aren't replicated. Examples include:
 - Conditions that reference ticket agreements
 - Conditions that reference a deleted option or inactive field
 - Unsupported conditions or conditions with dependencies that haven't been set up, such as a condition referencing custom objects or certain channels and integrations
- Inactive configurations are replicated, but business rules (for example, triggers and automations) that have conditions or actions which reference an inactive ticket field are not replicated.
- External email addresses are not copied to the sandbox.
- Changes made within a sandbox are not copied automatically into the production account and must be manually reproduced within the production account.
- Only the items identified in this article are replicated.
- Legacy agents can't be replicated. If you want them to be replicated, you must assign new roles to them.
- Views, triggers, and automations may appear in a different order in the sandbox. Personal views and macros aren't replicated.
- Only the first 100 comments are replicated per ticket.
- Skills used for skills-based routing aren't replicated.
- Custom object records can't be replicated. Tickets with lookup relationship fields that reference custom objects and business rules that reference custom objects can't be replicated either.
- Not all apps are replicated when you create a sandbox. To be replicated, an app must be a free app installed from the [Zendesk Marketplace](https://www.zendesk.com/marketplace/apps/)
 and it can't require authentication or additional configuration during installation.