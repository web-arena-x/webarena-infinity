# Blocking unwanted callers

Source: https://support.zendesk.com/hc/en-us/articles/4408834961050-Blocking-unwanted-callers

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support with** | Talk Professional or Enterprise |

When you run a call center, you might need to block unwanted or spam calls. You can block incoming calls from a single number, or use conditions to block multiple numbers simultaneously. Additionally, you cannot make calls to blocked numbers.

You must be a [Talk admin or team lead](https://support.zendesk.com/hc/en-us/articles/4408832171034#topic_a54_zlt_qmb) to manage blocked numbers.

This article contains the following topics:

- [Viewing your blocked numbers](#topic_crv_rqn_bhb)
- [Blocking numbers](#topic_tgh_kpn_bhb)
- [Editing blocked numbers](#topic_rqh_jrn_bhb)
- [Calling blocked numbers](#topic_pct_gby_xkb)
- [Unblocking numbers](#topic_dtz_kpn_bhb)

## Viewing your blocked numbers

You can view blocked numbers and conditions.

**To view your blocked numbers**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_channels_icon.png)
   **Channels** in the sidebar, then select **Talk and email > Talk**.
2. Click the **Blocked numbers** tab.

A list of your blocked numbers is displayed.

![Blocked number list](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Talk_block_1.png)

## Blocking numbers

You can block a single number or block all numbers that match a condition you enter.

Note: You can't block numbers when using a [SIP-IN line](https://support.zendesk.com/hc/en-us/articles/8397091234586).

**To block a single number**

1. On the **Blocked numbers** tab, click **Add number**.
2. On the add number page, choose **Equal to** from the **Condition** drop-down list.
3. In the **Phone number** field, enter the number you want to block.

   Important: The number must be in the e.164 format including +1 before the number.

   ![Block a new number](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Talk_block_3.png)
4. When you are finished, click **Save changes**.

The phone number you entered is added to the list of blocked numbers and is immediately blocked.

**To block all numbers that match a condition**

1. On the **Blocked numbers** tab, click **Add number**.
2. From the **Condition** drop-down list choose **Starts with** if you want to block all numbers that start with the pattern you enter or **Ends with** to block all numbers that end in the pattern you enter.
3. In the **Phone number** field, enter the pattern you want to match. For example, you could block all numbers that start with **+1206**.
4. When you are finished, click **Save changes**.

## Editing blocked numbers

You can make changes to a blocked number or condition. Any changes you make will take effect immediately.

**To edit a blocked number**

1. On the **Blocked numbers** tab, click the icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/manage_icon.png)) next to the number or condition want to edit.
2. From the drop-down list, choose **Edit**.

   ![Edit blocked number](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Talk_block_2.png)
3. Make the required changes to the condition and number, then click **Save changes**.

## Calling blocked numbers

When you try to call a blocked number, you'll see a message indicating the number is blocked and the call won't connect.

![Calling a blocked number](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Talk_block_call.png)

## Unblocking numbers

When you delete a number from the list it is immediately unblocked.

**To unblock a number**

1. On the **Blocked numbers** tab, click the icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/manage_icon.png)) next to the number or condition you want to unblock.
2. From the drop-down list, choose **Unblock**.

If you deleted a single number, it is unblocked. If you deleted a condition, then all numbers that match that condition are unblocked.