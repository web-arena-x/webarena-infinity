# Restricting access to messaging channels by IP address

Source: https://support.zendesk.com/hc/en-us/articles/9418691150106-Restricting-access-to-messaging-channels-by-IP-address

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support with** | Live chat and messaging Team, Professional, or Enterprise |

Note: The feature described in this article is similar to [banning visitors by IP address in live chat](https://support.zendesk.com/hc/en-us/articles/4408824467098).

Admins can block all end users from a specified IP address from conducting messaging conversations with your AI or human agents. Messaging channel bans can be applied to IP addresses in Admin Center, or from messaging conversations in Agent Workspace.

This article includes the following topics:

- [Understanding what happens when an IP address is banned from messaging channels](#topic_q2k_1mh_dgc)
- [Banning IP addresses in Admin Center](#topic_hw4_1mh_dgc)
- [Banning IP addresses in a messaging conversation in Agent Workspace](#topic_wft_1mh_dgc)

Related articles:

- [About banning IP addresses from messaging channels](https://support.zendesk.com/hc/en-us/articles/9418700382618)
- [Managing IP addresses banned from messaging channels](https://support.zendesk.com/hc/en-us/articles/9535836802074)
- [Accessing and using the Banned IP addresses page in Admin Center](https://support.zendesk.com/hc/en-us/articles/9435777614874)

## Understanding what happens when an IP address is banned from messaging channels

Banning an IP address from accessing your messaging channels:

- Prevents any users with the banned IP address from connecting with your Web Widget, iOS SDK, and Android SDK channels.
- Adds it to the [Banned IP addresses page](https://support.zendesk.com/hc/en-us/articles/9435777614874-Viewing-and-managing-IP-addresses-banned-from-messaging-channels).
- Adds the action to the [audit log](https://support.zendesk.com/hc/en-us/articles/4408828001434).

Banning an IP address does not notify the end user that their IP address has been banned. End users, however, do experience a change in behavior in the Web Widget or Mobile SDK channels. See [About banning IP addresses from messaging channels](about-banning-ip-addresses-from-messaging-channels.md#topic_ztg_z2h_dgc).

## Banning IP addresses in Admin Center

Admins and agents with the right permissions can ban IP addresses from the Banned IP addresses page.

**To ban an IP address from the Banned IP addresses page**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_people_icon.png)
   **People** in the sidebar, then select **Restrictions > Banned IP addresses**.
2. Click **Ban IP address**.
3. On the **Add a banned IP page**, add the following information:
   - **IP address (required)**: Enter the IP address or range you want to ban. Use valid IPv4 formatting for individual IP addresses. See [Specifying a range of IP addresses](#topic_igr_bmh_dgc) for adding a multiple addresses.
   - **Reason (required)**: Use the drop-down to select a reason for banning the address.
   - **Additional comments**: Enter a comment (up to 500 characters) with relevant information about the IP address or the ban.
4. Click **Ban**. The IP address is added to the banned IP list.

### Specifying a range of IP addresses

You can specify ranges of IP addresses. Use valid IPv4 addresses, along with the methods below, to specify a range:

- **Use asterisk (\*) wildcards**. An IP address consists of four numbers separated by periods, such as 192.168.0.1. You can substitute a single asterisk character (\*) for any number group to let Zendesk know that it should accept any value in that space. For example, 192.\*.\*.\* allows any IP address whose first number is 192.
- **Use IP subnet mask syntax**. For example, 192.168.1.0/25 specifies all the IP addresses between 192.168.1.0 and 192.168.1.127.

## Banning IP addresses in a messaging conversation in Agent Workspace

If device metadata is displayed in Agent Workspace, you can ban IP addresses from the ticket interface. The option to ban an IP address appears in the Device information section of the Customer context panel.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ip_ban_messaging-ban_button.png)

Note: [End-user device information](https://support.zendesk.com/hc/en-us/articles/7041910642074) must be displayed in the Customer context panel to view and ban IP addresses in Agent Workspace. If device information isn’t displayed, IP addresses can only be banned from the [Banned IP addresses page](https://support.zendesk.com/hc/en-us/articles/9435777614874-Viewing-and-managing-IP-addresses-banned-from-messaging-channels) in Admin Center.

**To ban an IP address in Agent Workspace**

1. In Agent Workspace, click the **User** icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/icon_omnipanel_user.png) ) on the side of the ticket. This opens customer context in the context panel.
2. Expand the **Device information** section.
3. Click **Ban IP**.