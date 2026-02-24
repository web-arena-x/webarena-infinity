# Reauthorizing and confirming the Zendesk Support - Facebook pages connection

Source: https://support.zendesk.com/hc/en-us/articles/4634815441946-Reauthorizing-and-confirming-the-Zendesk-Support-Facebook-pages-connection

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

If you have configured your Zendesk and Facebook accounts to work together, at some point you may find you are unable to send or receive any public or private messages in Support (for example, from Facebook pages or via Facebook Messenger). If this happens, you can reauthorize Zendesk’s access to your Facebook account and check the connection between them.

This article includes the following topics:

- [Reauthorizing Zendesk’s connection to Facebook](#topic_ovs_qrm_q5b)
- [Confirming the Zendesk-Facebook connection](#topic_qfk_qrm_q5b)

Related articles:

- [How do I troubleshoot issues with my Facebook channel?](https://support.zendesk.com/hc/en-us/articles/4408887381914-How-do-I-troubleshoot-issues-with-my-Facebook-channel-)
- [My Facebook integration stopped working](https://support.zendesk.com/hc/en-us/articles/4408826833050-My-Facebook-integration-stopped-working)

You can also watch the following video:

How to reauthorize the connection between Zendesk Support and your Facebook pages (2:03)

## Reauthorizing Zendesk’s connection to Facebook

There are a [number of reasons](https://support.zendesk.com/hc/en-us/articles/4408826833050) why the connection between Facebook and Zendesk might be lost. If you determine that the Zendesk-Facebook connection is not working, you can reauthorize Zendesk’s access.

**To reauthorize Zendesk to access your Facebook pages**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_channels_icon.png)
   **Channels** in the sidebar, then select **Messaging and social > Facebook Pages**.
2. Move the cursor over the name of the Facebook page and then click **unlink** to completely remove the page.
3. Click **Add new page** to re-add the Facebook page you removed in the previous step.
4. Sign in to your Facebook account.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/fb_auth_previous_link.png)
5. Click **Edit settings**.
6. Select the pages you want to link to Zendesk, and then click **Next**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/fb_auth_pages.png)
7. Adjust your permissions, if needed, and then click **Done**.

   Note: If you have an account that enables you to use Facebook Messenger, and you want to use it, **Manage and access Page conversations on Messenger** must be enabled.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/fb_auth_permissions_2.png)
8. Go to [Facebook channel settings](https://support.zendesk.com/hc/en-us/articles/4408819897242#topic_ejk_hp3_zl) and enable **Include Wall posts** and **Include private messages**.

If these instructions do not reconnect your Zendesk and Facebook accounts, see [My Facebook integration stopped working](https://support.zendesk.com/hc/en-us/articles/4408826833050-My-Facebook-integration-stopped-working) for more suggestions.

## Confirming the Zendesk-Facebook connection

To determine that the reauthorization was successful, you can create a view to monitor the flow of Facebook tickets through Zendesk Support.

**To create the view for your Facebook tickets**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_workspaces_icon.png)
   **Workspaces** in the sidebar, then select **Agent tools > Views**.
2. Click **Add view**.
3. Enter a **Title** for the view, for example, "Facebook posts".
4. Under **Tickets must meet all of these conditions to appear in the view**, add:
   - **Status | Less than | Solved**
   - **Channel | Is | Facebook Post**
5. Create a post on your Facebook page.
6. In Support, open the view you just created.

   If you don't see the view on the list, [reorder your views](../../agent-guide/ticket-management/accessing-and-using-the-views-admin-page.md#topic_tmy_3hd_jjb) to move it up its position.
   Expect a [small delay](https://support.zendesk.com/hc/en-us/articles/4408831298714-Why-tickets-from-Facebook-don-t-show-immediately-in-Support-) between the time you created the post and the time Zendesk creates the ticket.

The following video also walks you through the confirmation process:

How to verify that the Facebook integration is working (2:03)