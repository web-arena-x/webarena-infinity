# Using the multiple organizations feature in the Salesforce integration

Source: https://support.zendesk.com/hc/en-us/articles/4408832217882-Using-the-multiple-organizations-feature-in-the-Salesforce-integration

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Growth, Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support** | Professional or Enterprise |

Location: Admin Center > Apps and integrations > Integrations >
Integrations

Zendesk and Salesforce have fundamental differences in the way they store users. In Zendesk, each user must have a unique email address. This is not required for Salesforce contacts or leads.

In order for multiple Salesforce contacts that share an email address to sync to Zendesk, the integration uses a Support feature that [allows users to belong to multiple organizations](https://support.zendesk.com/hc/en-us/articles/204281436-Enabling-multiple-organizations-for-users-Professional-and-Enterprise-).

This article explains the syncing behavior for the Salesforce integration when multiple organizations is turned on. You can request permission to turn on multiple organization sync by contacting [Zendesk Customer Support](https://support.zendesk.com/hc/en-us/articles/4408843597850). Permission is granted on a per-account basis.

This article contains the following sections:

- [Understanding the multiple organization syncing process](#topic_rfg_k2q_hnb)
- [Account relationship syncing](#topic_fbc_clr_3tb)
- [Syncing behavior when multiple organizations is turned on or off](#topic_x2s_p2q_hnb)

Related information:

- [Enabling multiple organizations for users](https://support.zendesk.com/hc/en-us/articles/4408838140314-Enabling-multiple-organizations-for-users-Professional-and-Enterprise-)
- [Salesforce integration resources](https://support.zendesk.com/hc/en-us/articles/4408827957274)

## **Understanding the multiple organization syncing process**

When the multiple organizations feature is turned on, multiple Salesforce contacts or leads with the same email address in different Salesforce accounts can be connected in Zendesk Support to a single user. Zendesk users can be members of multiple organizations.

In Salesforce, when multiple contacts or leads share an email address, the first contact or lead linked to an account is considered the syncing record. The syncing record is the primary Salesforce record and is identified by a user account during syncing.

The syncing record updates its corresponding user entry in Zendesk during a sync when changes have been made to the user fields in Salesforce.

The following rules govern the syncing behavior between Salesforce and Zendesk:

- If an organization doesn’t exist in Zendesk, organization memberships aren't created.
- Organization memberships are only added, not deleted.
- Mapped fields are synced if the Salesforce primary account-contact relationship matches the user’s default organization in Zendesk.
- An organization membership in Zendesk is created only if a Salesforce contact is linked to a Salesforce account.
- The integration respects existing default memberships, which are manually assigned.
- The following features must all be turned on to sync secondary relationships:
 - Accounts to Organizations sync
 - Contacts/Leads to Users sync
 - Primary relationship syncing
 - [Allow users to belong to multiple organizations](https://support.zendesk.com/hc/en-us/articles/204281436-Enabling-multiple-organizations-for-users-Professional-and-Enterprise-) in Support
 - Secondary relationships in Salesforce.

## Account relationship syncing

There are two types of account relationship syncs: primary and secondary. The primary account relationship refers to the main (primary) account that a Salesforce contact belongs to. A secondary account relationship refers to all other accounts that a Salesforce contact may belong to. Performing a primary account relationship sync can change the Zendesk user's primary organization.

**To turn on account relationship syncing**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_apps_integrations_icon.png)
   **Apps and integrations** in the sidebar, then select **Integrations >
   Integrations**.
2. On the Integrations page, click **Salesforce**.
3. Click the **Data sync** tab.
4. In **Accounts to Organizations sync**, click **Configure**.
5. Select **Enable syncing** and click **Save**.
6. Back on the Salesforce integrations page, click the **Data sync** tab.
7. Under **Contacts/Leads to Users sync**, click **Configure**.
8. Select **Enable syncing**, and under **Sync type**, select **Contacts**.
9. Select **Sync primary relationship** and, optionally, **Sync secondary relationships**.

   If you don't see these options, contact [Zendesk Customer Support](https://support.zendesk.com/hc/en-us/articles/4408843597850) to give you access.

   Note: When performing the initial sync of Salesforce contacts to Zendesk users, secondary account relationship sync must be disabled. Because a Salesforce contact may have a large number of secondary relationships, this could exceed Zendesk rate limits. After the initial primary relationship sync is performed, the secondary account relationship sync can be turned on.
10. Click **Save**.

## Syncing behavior when multiple organizations is turned on or off

To understand what happens during syncing, the following examples describe some scenarios and the actions and results when you turn on the multiple organizations feature in Support and configure different account relationship syncing.

- [Scenario 1](#topic_p3p_h5r_3tb)
- [Scenario 2](#topic_kth_mvr_3tb)
- [Scenario 3](#topic_szw_f5y_3tb)
- [Scenario 4](#topic_q5h_t5y_3tb)
- [Scenario 5](#topic_lxr_1vy_3tb)
- [Scenario 6](#topic_a3k_fvy_3tb)
- [Scenario 7](#topic_zzm_lvy_3tb)

### Scenario 1

- Salesforce contact without a linked account is synced to Zendesk.
- Salesforce contact is matched with an existing user in Zendesk.

| Settings enabled | Sets the user's organization in Zendesk (normal contact sync) | Creates organization memberships (primary/secondary) | Syncs contact's mapped fields |
| --- | --- | --- | --- |
| - None | N/A | N/A | Yes |
| - Allow multiple organizations | N/A | N/A | Yes |
| - Primary account relationship | No | N/A | Yes |
| - Allow multiple organizations - Primary account relationship | No | No | Yes |
| - Allow multiple organizations - Primary account relationship - Secondary account relationships | No | No | Yes |

### Scenario 2

- Salesforce contact without a linked account is synced to Zendesk.
- Salesforce contact is not matched with an existing user in Zendesk.

| Settings enabled | Sets the user's organization in Zendesk (normal contact sync) | Creates organization memberships (primary/secondary) | Syncs contact's mapped fields |
| --- | --- | --- | --- |
| - None | N/A | N/A | Yes (new user created) |
| - Allow multiple organizations | N/A | N/A | Yes (new user created) |
| - Primary account relationship | No | N/A | Yes (new user created) |
| - Allow multiple organizations - Primary account relationship | No | No | Yes (new user created) |
| - Allow multiple organizations - Primary account relationship - Secondary account relationships | No | No | Yes (new user created) |

### Scenario 3

- Salesforce contact with a linked account is synced to Zendesk.
- The contact is matched to an existing user in Zendesk.
- The account is linked to an existing organization in Zendesk.
- The organization is the matched user’s default organization.

| Settings enabled | Sets the user's organization in Zendesk (normal contact sync) | Creates organization memberships (primary/secondary) | Syncs contact's mapped fields |
| --- | --- | --- | --- |
| - None | N/A | N/A | Yes |
| - Allow multiple organizations | N/A | N/A | Yes |
| - Primary account relationship | Yes | N/A | Yes |
| - Allow multiple organizations - Primary account relationship | No | Yes | Yes |
| - Allow multiple organizations - Primary account relationship - Secondary account relationships | No | Yes | Yes |

### Scenario 4

- Salesforce contact with a linked account is synced to Zendesk.
- The contact is matched to an existing user in Zendesk.
- The account is linked to an existing organization.
- The organization is not the matched user’s default organization.

| Settings enabled | Sets the user's organization in Zendesk (normal contact sync) | Creates organization memberships (primary/secondary) | Syncs contact's mapped fields |
| --- | --- | --- | --- |
| - None | No | N/A | Yes |
| - Allow multiple organizations | No | N/A | Yes |
| - Primary account relationship | Yes | N/A | Yes |
| - Allow multiple organizations - Primary account relationship | No | Yes | No (default org doesn't match) |
| - Allow multiple organizations - Primary account relationship - Secondary account relationships | No | Yes | No (default org doesn't match) |

### Scenario 5

- Salesforce contact with a linked account is synced to Zendesk.
- The contact is matched with an existing user in Zendesk.
- The account is not linked to any organization.

| Settings enabled | Sets the user's organization in Zendesk (normal contact sync) | Creates organization memberships (primary/secondary) | Syncs contact's mapped fields |
| --- | --- | --- | --- |
| - None | No | N/A | Yes |
| - Allow multiple organizations | No | No | Yes |
| - Primary account relationship | No | N/A | Yes |
| - Allow multiple organizations - Primary account relationship | No | No | Yes |
| - Allow multiple organizations - Primary account relationship - Secondary account relationships | No | No | Yes |

### Scenario 6

- Salesforce contact with a linked account is synced to Zendesk.
- The contact is not matched with any user.
- The account is linked to an existing organization in Zendesk.

| Settings enabled | Sets the user's organization in Zendesk (normal contact sync) | Creates organization memberships (primary/secondary) | Syncs contact's mapped fields |
| --- | --- | --- | --- |
| - None | No | N/A | Yes (new user created) |
| - Allow multiple organizations | No | No | Yes (new user created) |
| - Primary account relationship | Yes | N/A | Yes (new user created) |
| - Allow multiple organizations - Primary account relationship | Yes | No | Yes (new user created) |
| - Allow multiple organizations - Primary account relationship - Secondary account relationships | Yes | No | Yes (new user created) |

### Scenario 7

- Salesforce contact with a linked account is synced to Zendesk.
- The contact is not matched with any user in Zendesk.
- The account is not linked to any organization.

| Settings enabled | Sets the user's organization in Zendesk (normal contact sync) | Creates organization memberships (primary/secondary) | Syncs contact's mapped fields |
| --- | --- | --- | --- |
| - None | No | N/A | Yes (new user created) |
| - Allow multiple organizations | No | No | Yes (new user created) |
| - Primary account relationship | No | N/A | Yes (new user created) |
| - Allow multiple organizations - Primary account relationship | No | No | Yes (new user created) |
| - Allow multiple organizations - Primary account relationship - Secondary account relationships | No | No | Yes (new user created) |