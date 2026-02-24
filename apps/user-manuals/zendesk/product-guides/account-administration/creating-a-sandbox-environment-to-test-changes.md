# Creating a sandbox environment to test changes

Source: https://support.zendesk.com/hc/en-us/articles/4408822049818-Creating-a-sandbox-environment-to-test-changes

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Enterprise or Enterprise Plus |

|  |  |
| --- | --- |
| **Support** | Enterprise |

Verified AI summary ◀▼

Create a sandbox environment to test changes without affecting your live setup. Sandboxes mirror your production instance, allowing you to experiment with workflows, integrations, and train agents safely. You can replicate various data types, including tickets and user fields. Choose how much ticket data to replicate and access a detailed creation report to review replication success.

Location:  Admin Center > Account > Sandbox > Environments

[Sandbox environments](https://support.zendesk.com/hc/en-us/articles/6150628316058) provide a test environment that closely
mirrors your production instance in configuration and some data. This allows you to
accurately test updates to workflows, experiment with integrations, and provide training
for new agents in an environment that reflects your production environment.

This article contains the following topics:

- [Overview of sandbox data replication](#topic_nxm_rkf_5yb)
- [Creating a sandbox](#topic_sbh_crm_tgb)

## Overview of sandbox data replication

The availability of sandbox environments vary by plan:

- Support Enterprise includes one sandbox.
- Suite Enterprise and Enterprise Plus include two sandboxes.
- Support Professional and above and Suite Growth and above can purchase sandbox
  environments. Contact your sales representative or [Zendesk Customer Support](https://support.zendesk.com/hc/en-us/articles/4408843597850) to purchase
  sandboxes as an add-on.

The following data is replicated in sandboxes:

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
- Support addresses (Internal support addresses, such as
  *help@mybusiness.zendesk.com*, are copied with slight modification to
  contain the brand's unique subdomain within the sandbox. If you've configured
  external support addresses, such as *help@mybusiness.com*, they're converted to
  internal addresses when replicated to a sandbox using the following structure:
  *help-at-mybusiness-com@sandboxsubdomain.zendesk.com*. If you've set an
  external support address as the default, the sandbox reverts to using the original
  default internal address: *support@mybusinesssandbox.zendesk.com*.)
- Webhooks (set to inactive in the sandbox by default)
- Apps (only free [Marketplace apps](https://www.zendesk.com/marketplace/apps/) that don't require authentication or
  additional configuration at installation)
- [Custom objects](https://support.zendesk.com/hc/en-us/articles/5914453843994) (this doesn't include
  custom object records, lookup fields related to custom objects, or legacy custom
  objects)
- (Optional, with [Copilot add-on](https://support.zendesk.com/hc/en-us/articles/7908817636378)) Guide default brand and [auto assist procedures](https://support.zendesk.com/hc/en-us/articles/7924047699738)

For more information about data replication process and limitations, see [About Zendesk
sandbox environments](https://support.zendesk.com/hc/en-us/articles/6150628316058). To understand exactly what data was and wasn't
successfully replicated for a particular sandbox, see [Generating a sandbox creation report](https://support.zendesk.com/hc/en-us/articles/7502268225690).

After a sandbox is created, you can [update the product and add-on subscriptions](https://support.zendesk.com/hc/en-us/articles/7414296161818) to reflect
changes to your production account and use the [Configuration Management EAP](https://support.zendesk.com/hc/en-us/articles/8712690572442) to update configuration
changes. No other replicated data can be updated after a sandbox is created.

## Creating a sandbox

Replication occurs automatically when you create a sandbox through [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb). The replication retrieves
data from the production instance and creates the configuration and content in the
sandbox, creating a new subdomain. The process will not affect the performance of
your production instance. Data is only retrieved from the production instance, so
nothing will be added, updated, or deleted there. For a complete list of the data
that is replicated, see [Understanding how data replication
works](https://support.zendesk.com/hc/en-us/articles/6150628316058#topic_n2f_gsm_tgb).

The configuration of your sandbox instance will change rapidly while the
replication is occurring, so we recommend waiting to use it until the replication
completes. The time it takes for a replication to complete varies depending on the
amount of content involved. A simple copy with a small amount of fields, business
rules, and ticket and user data takes less time, ranging from a few minutes to a few
days. A copy with 100,000 tickets and the related users, organizations, and business
rules can take up to a week or more to complete. When the replication is complete,
the status of the sandbox changes to *Active*.

**To create a sandbox**

1. Before creating a new sandbox, make sure you've [configured a default group](https://support.zendesk.com/hc/en-us/articles/4408828237722) for your
   account.
2. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_account_icon.png)
   **Account** in the sidebar, then select **Sandbox > Environments**.
3. Click the **Create Sandbox** button.
4. Enter a **Name** that describes your sandbox.
5. Select how much ticket data you want to replicate: **0**, **500**,
   **5,000**, or **10,000** tickets.

   An equal number of non-closed
   tickets that have been updated within the last six months can also be
   replicated, and end users associated with all replicated tickets are also
   replicated in the sandbox.
6. (Optional) If you have the [Copilot add-on](https://support.zendesk.com/hc/en-us/articles/5524125586330), under **Train your
   agents in Guide with Sandbox**, you can select **Turn on** to replicate
   your Guide default brand and [auto assist procedures](https://support.zendesk.com/hc/en-us/articles/7924047699738).

   The
   replication of auto assist procedures provides a more realistic and
   efficient training environment for agents outside of production. However, no
   other Guide data is replicated.
7. Click **Create**.

   You will see a message that your sandbox is being
   created. When your sandbox is successfully created, a message appears at the
   top of the page, and the status of the sandbox becomes *Active.* The
   sandbox has a unique URL with a ten-digit number after your domain
   name.

   You can access a creation report for 30 days following the
   creation of a sandbox. This report contains details about most of the
   production data that Zendesk attempted to replicate in the sandbox,
   including explanations for anything that failed to replicate. See [Generating a creation report for a
   sandbox](https://support.zendesk.com/hc/en-us/articles/7502268225690).

With your newly-replicated sandbox, you will have an environment that
closely mirrors your production instance. This enables you to test out new
workflows, give your agents a safe place to train, and provide a high-quality
environment for development purposes. See [Managing sandboxes](https://support.zendesk.com/hc/en-us/articles/4408824434586).

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_account_sandbox_create_6.png)