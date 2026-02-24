# Banning visitors from accessing Chat

Source: https://support.zendesk.com/hc/en-us/articles/4408824467098-Banning-visitors-from-accessing-Chat

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support with** | Live chat and messaging Team, Professional, or Enterprise |

You can ban visitors so that they can't access the Chat widget or Web Widget
(Classic) and chat with agents. Visitors can be added to the banned visitor list
directly from a chat, or from the Chat dashboard. You can view, search, and add
users to the Banned Visitors list through the Banned settings page.

This article contains the following topics:

- [Banning
  visitors](#topic_m2b_4c3_flb)
- [Viewing and managing
  banned visitors](#topic_zh3_4c3_flb)
- [The end user
  experience](#topic_m5d_tkr_rpb)

## Banning visitors

You can ban unlimited visitors, and up to 5,000 IP addresses. If the number of banned
IP addresses exceeds 5,000, the oldest banned IP address is removed from the list
and is no longer banned.

There are two ways to ban a visitor:

- Directly from a chat: With this option, the system places a cookie on the
  visitor's browser to identify them. This method prevents visitors from avoiding
  the ban with proxies or VPNs, but they might still be able to get through it on
  another browser.

  After selecting **Ban Visitor** from the chat, you also
  have the choice of banning the visitor's IP address at the same time, as
  described in the steps below.
- Adding the IP address to the Banned Visitors list: This option stops banned
  visitors from gaining access just through another browser, but it also
  doesn't prevent them from using a proxy or VPN. You can find a visitor's IP
  address by [opening the chat history](https://support.zendesk.com/hc/en-us/articles/4408893866778#topic_sbw_bqq_3rb) and
  clicking the **User info** tab.

Note: Banning a visitor in Chat does not suspend that user in Support. See [Suspending a user](https://support.zendesk.com/hc/en-us/articles/4408889293978) for information on blocking users in
Support.

**To ban a visitor directly from a chat**

1. From the chat window, select **Ban Visitor** from the **Actions**drop-down menu.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/zopim_transfer_to_dept.png)
2. Optional**:** Enter a reason in the **Reason** field.
3. Optional: If you want to also ban the visitor's IP address, select the **Also
   ban visitor's IP address** check box.
4. Click **Ban User**.

**To ban a visitor by IP address**

1. From the dashboard, select **Settings** > **Banned**.
2. To add a visitor's IP to the list, click **Add Visitor**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/banned_visitors_search_chat.png)
3. Enter an IP address and a reason.
4. Click **Create Ban**.

## Viewing and managing banned visitors

Banned visitors are listed on the Banned settings page.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/banned_visitors_page_chat.png)

On the Banned settings page you can:

- View all banned visitors
- Search the banned visitors list
- Add visitors to the banned list by IP address (described in the previous
  section)
- Remove visitors from the banned list

By default, the banned visitors list displays 10,000 entries (5,000 each for visitors
and IP addresses). Using the Chat API, you can extend this to display up to 5,000
banned IP addresses and unlimited banned visitors. See [Bans](https://developer.zendesk.com/rest_api/docs/chat/bans) in our developer documentation.

**To access the Banned settings page and view banned visitors**

- From the dashboard, select **Settings** > **Banned**.

  A list of
  all banned visitors is displayed. The list includes the following
  columns:

  - **Visitor/IP address**, the name of the banned user or banned
    IP address
  - **Reason**, the description given for banning the user/IP
    address
  - **Date created**, the date the user/IP address was
    banned

  You can display only banned IP addresses, or only banned individual
  visitors, by using the **Filter** drop-down menu at the top of the
  page.

**To search the banned visitors list**

1. Go to the **Banned settings** page.
2. In the Search box, enter one or more keywords to search for.
3. As you type, the list displays only banned IP addresses or visitors
   with the search terms in their name, IP address, or reason for
   banning.

**To remove a visitor from the ban list**

1. From the **Banned settings** page, select the check box next to the
   visitor's name or IP address.
2. Click the **Delete Selected** button that appears at the top of the
   list.
3. Click **Delete** on the window that appears.

## The end user experience

When an individual visitor is banned in Chat, or if a visitor is from a blocked
country, they do not receive a notification, but they will not be able to access
chat functionality.

- If you have an **embedded Chat standalone widget**, the widget will
  not load for that visitor on your website.
- If you are using a **messaging Web Widget or Mobile SDK**, a chat
  connection will not be established.
- If you are using **Chat in the Web Widget (Classic)**, the Web Widget
  (Classic) will still appear to the visitor, but the chat option will not
  appear in the contact options menu.