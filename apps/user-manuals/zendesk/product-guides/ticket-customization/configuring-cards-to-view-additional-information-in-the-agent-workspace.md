# Configuring cards to view additional information in the Agent Workspace

Source: https://support.zendesk.com/hc/en-us/articles/5768595554714-Configuring-cards-to-view-additional-information-in-the-Agent-Workspace

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support** | Professional or Enterprise |

Location: Admin Center > Workspaces > Agent tools > Cards

Cards provide agents on all plans with a preview of user, custom object, and organization records from the context panel in the Zendesk Agent Workspace. On Professional plans and above, admins can configure these cards to display certain fields so that only the most relevant information is displayed.

Configuring cards can improve your agents’ efficiency because it reduces the need to navigate away from the ticket they’re working on.

Note: Agent Workspace must be activated to configure the essentials card. See [Activating the Agent Workspace](https://support.zendesk.com/hc/en-us/articles/4581758611866).

This article includes the following sections:

- [Accessing your cards](#topic_kyt_k42_wxb)
- [Considerations for the user essentials card](#topic_up3_fp2_wxb)
- [Considerations for custom object cards](#topic_zv1_pyd_mcc)
- [Considerations for organization cards](#topic_un5_p53_5fc)
- [Configuring a card](#topic_hw5_yyd_mcc)

Related articles

- [Viewing customer context in a ticket](https://support.zendesk.com/hc/en-us/articles/4408829170458)
- [Interacting with related object records in tickets](https://support.zendesk.com/hc/en-us/articles/6097369527322)

## Accessing your cards

The **Cards** page in Zendesk Admin Center provides a list of your [custom objects cards](#topic_zv1_pyd_mcc), the [user essentials cards](#topic_up3_fp2_wxb), and the [organization card](#topic_un5_p53_5fc). From this page, admins on Professional plans and above can configure which fields are included in the cards.

**To open the Cards page**

- In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_workspaces_icon.png)
 **Workspaces** in the sidebar, then select **Agent tools > Cards**.![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/cards_select_card_type.png)

## Considerations for the user essentials card

The user essentials card appears in the [context panel](https://support.zendesk.com/hc/en-us/articles/4408836526362) in the Agent Workspace and displays information about the ticket requester.

Admins can add, remove, and reorder standard and [custom user fields](https://support.zendesk.com/hc/en-us/articles/4408822051866), including [user contact information](https://support.zendesk.com/hc/en-us/articles/4408822763546#topic_zb2_22c_ppb) and organization memberships, so that agents can access the most relevant information.

In the customer’s card in the context panel, agents will see the fields you configured that have a value. Configured fields without a value aren’t visible.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/essentials_compare_cards.png)

## Considerations for custom object cards

A [custom object](https://support.zendesk.com/hc/en-us/articles/5914453843994) is a user-defined object with unique fields and permissions. Custom objects can be almost anything, including a product, contract, delivery driver, asset, or event. When a custom object record is related to a ticket, agents can use the record preview panel in the Agent Workspace to see details about the custom object record. See [Interacting with related object records in tickets](https://support.zendesk.com/hc/en-us/articles/6097369527322).

You must have [created at least one custom object](https://support.zendesk.com/hc/en-us/articles/5392409465370) and defined its custom fields to select a custom object card.

Admins can configure custom object cards so that only certain fields display in the record preview panel. By default, the record preview displays the custom object’s first 20 fields. You may want to configure custom object cards so that agents have access to the most relevant information without navigating away from the ticket.

## Considerations for organization cards

[Organizations](https://support.zendesk.com/hc/en-us/articles/4408886146842) are collections of users that can help you define workflows and organize users based on shared criteria. All Zendesk accounts come with a default organization that includes all of your users, and you can create additional organizations as needed to keep track of user subsets.
When an organization record is related to a ticket, agents can use the record preview panel in the Agent Workspace to see useful details about that organization.

Admins can [configure organization cards](#topic_hw5_yyd_mcc) to display up to 20 standard or custom organization fields in the record preview panel.

## Configuring a card

Whether you're configuring the user essentials card, a custom object card, or an organization card, the process is the same.

**To configure a card**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_workspaces_icon.png)
   **Workspaces** in the sidebar, then select **Agent tools > Cards**.
2. Select the **User essentials card**, a custom object card, or an organization card by clicking its name.

   Note: To configure a custom object card, you must have created at least one custom object and defined its custom fields. See [Creating custom objects to integrate with custom data](https://support.zendesk.com/hc/en-us/articles/5392409465370).

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/cards_select_card_type.png)
3. Modify the card’s configuration as needed.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_essentials_card_edit.png)

   1. To add fields, click **+Add field**, then select a field from the list of available fields or search for the field you want to add.

      ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_essentials_card_add.png)
   2. To remove a field from the card, click the **X** icon next to its name.
   3. To reorder fields, click the grabber icon at the end of a field, then drag it to another position within the card.

      ![](https://zen-marketing-documentation.s3.us-west-1.amazonaws.com/docs/en/ac_essentials_card_reorder.png)

      The preview of the card updates as you make changes.
4. Click **Save**.