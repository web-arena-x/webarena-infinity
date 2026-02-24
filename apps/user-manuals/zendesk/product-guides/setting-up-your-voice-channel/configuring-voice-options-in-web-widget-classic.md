# Configuring voice options in Web Widget (Classic)

Source: https://support.zendesk.com/hc/en-us/articles/4408824310426-Configuring-voice-options-in-Web-Widget-Classic

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support with** | Talk Professional or Enterprise |

To offer voice support in Web Widget (Classic), you need to create a configuration that defines
how to handle voice requests that originate from Web Widget (Classic). For example, you
can route a voice request to a certain group of agents, and you can assign a priority
level for voice requests.

The configuration that you create also defines the appearance of call components and values
in Web Widget (Classic). The available components differ based on the type of
configuration you are using:

- **Request a callback** allows customers to submit a request for a phone call
  from an agent.
- **Call us** (Professional and Enterprise) uses [a digital
  line](https://support.zendesk.com/hc/en-us/articles/1260805715389) to embed a call button customers can click to initiate a call to
  an agent.

Keep in mind that the first configuration you create becomes the default and is used by
all instances of Web Widget (Classic), unless you override it with another configuration
using the nickname API (see [Advanced configuration of Talk in Web Widget
(Classic)](https://support.zendesk.com/hc/en-us/articles/4408832257562#topic_ffj_xsy_hdb) and [the developer docs](https://developer.zendesk.com/api-reference/widget/settings/#nickname)).

Important: If you configure more than one Web Widget (Classic), you must set
which is your default widget (the widget that will appear in your help center).
After you set a new default widget, it might take a few minutes before you see your
changes. This behavior doesn't apply if you're using the Javascript snippet to
configure your widgets.

Allow 10 minutes for the changes to propagate and appear in Web Widget (Classic).

This article contains the following sections:

- [Configuring a callback request
  widget](#topic_ckg_kzj_g4b)
- [Configuring a call button
  widget](#topic_x4m_kzj_g4b)
- [Modifying call options in an existing widget configuration](#topic_mvc_3wm_h4b)

Related articles:

- [Configuring the components in your Web
  Widget](https://support.zendesk.com/hc/en-us/articles/4408838063258)
- [Web Widget resources](https://support.zendesk.com/hc/en-us/articles/4408833907354)

## Configuring a callback request widget

Use the steps below to offer your customers the option to request a
callback from an agent.

**To create a callback widget configuration** 

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_channels_icon.png)
   **Channels** in the sidebar, then select **Talk and email > Talk**.
2. From the **Widget** tab, click **Add widget configuration**, then
   select **Request a callback**.
3. At the top of the configuration settings, click to **Enable the
   configuration on Web Widget**.
4. Update the settings shown [in the table below](#topic_ckg_kzj_g4b__table_tph_w2t_fdb).
5. Click **Save**.

| Setting | Description |
| --- | --- |
| Enable configuration on Web Widget | Turn the toggle on to be able to use the configuration in Web Widget (Classic). If you don’t want to use the configuration, but don’t want to delete it, turn the toggle off (for example, if you think you might want to use it again in the future). Keep in mind that you need to turn the toggle on for each configuration that you want to use. |
| Group routing | Select the group that will receive calls and callback requests from Web Widget (Classic). When agents from the selected group are available, the configuration contact option displays. If all agents in the group haven't answered or made a call for an extended period of time (there is no maximum time limit for this), Web Widget (Classic) treats them as if they are all still online.  Tip: If for some reason the call option doesn't appear in Web Widget (Classic), try toggling your agents offline and then back online. |
| Nickname | Enter the configuration name. If you create multiple configurations of the widget, you need to use the configuration nickname in the Web Widget API to select which configurations to show on the current page. See [Advanced configuration of Talk in Web Widget (Classic)](https://support.zendesk.com/hc/en-us/articles/4408832257562#topic_ffj_xsy_hdb). |
| Brand | Select the brand you want to associate with the configuration. |
| Priority | Select the call priority routed to the configuration. You can choose from these options:  - **Normal**: Callback requests are routed to the call   queue. - **High**: Callback requests will be pushed to the   front of the queue. |
| Contact options | Select the ways you want user to be able to contact you. You can choose from these options:  - **Request a callback:** Allows customers to enter a phone   number to receive a callback. Appears only when agents are   online. - **Call us:** Displays a phone number customers can call.   Appears only when agents are online. For a more interactive   experience, try [Configuring a call button   widget](#topic_x4m_kzj_g4b). - **Request a callback and call us:** Allows customers to   enter a phone number to receive a callback, and also   displays a phone number customers can call. Appears only   when agents are online.   The Web Widget (Classic) title reflects the option you select.  Note: Request a callback is not available for Support Team or Suite Growth. |
| Outbound calling number | When **Request a callback** is selected, the phone number in the drop-down list is called **Outbound calling number**. Select the phone number agents use to return callback requests. This number does not appear in the Web Widget (Classic).  Note: It’s possible to select a toll-free number from this drop-down list, but we strongly recommend that you don’t because toll-free numbers are designed to be used for domestic inbound calls and don’t support outbound calls. |
| Phone number | When **Call us (display phone number)** is selected, the phone number drop-down list is called **Phone number to be displayed**. Select a phone number that you want customers to use to make inbound calls to your business. The number displays in Web Widget (Classic). You may or may not want to use a toll-free number. If you want to display multiple configurations' phone numbers, you need to customize Web Widget (Classic) (see [Advanced configuration of Talk in Web Widget (Classic)](https://support.zendesk.com/hc/en-us/articles/4408832257562#topic_ffj_xsy_hdb)). |
| Phone number to be displayed | When **Request a callback and call us** is selected, the phone number drop-down list is called **Phone number**. Select a phone number that you want customers to use to make inbound calls to your business. The number displays in Web Widget (Classic) when agents are online and the Call us button is displayed. The number is also used to make outbound calls to your customers when agents are offline and the Request a callback appears button is displayed.  Note: It’s possible to select a toll-free number from this drop-down list, but we strongly recommend that you don’t because toll-free numbers are designed to be used for domestic inbound calls and don’t support outbound calls. If you want to display multiple configurations' phone numbers, you need to customize Web Widget (Classic) (see [Advanced configuration of Talk in Web Widget (Classic)](https://support.zendesk.com/hc/en-us/articles/4408832257562#topic_ffj_xsy_hdb)). |
| Display average wait time? | Display the average time until an agent is available. The wait time is the Average Wait Time metric (see [Analyzing call activity with the Talk Team dashboard](https://support.zendesk.com/hc/en-us/articles/4408821396762)). |
| Set min and max limits for your wait times? | Enter custom wait times to display in Web Widget (Classic). These numbers do not impact call requests and are not related to your actual average wait time. For example, they can be almost any number you set and function the same as display text.  Note: If you set the minimum and maximum wait time to the same integer, then the wait time always reflects that integer. |
| Minimum average wait time | Enter a custom average minimum wait time to display in Web Widget (Classic). This number does not impact call requests and functions the same as display text. For example, if you set your minimum average wait time to five minutes, Web Widget (Classic) never shows a wait time of less than five minutes.  Note: You cannot set your minimum average wait time to less than two minutes. |
| Maximum average wait time | Enter a custom average maximum wait time to display in Web Widget (Classic). This number does not impact on call requests and functions the same as display text. For example, if you set your maximum average wait time to 15 minutes, then your widget will never show a wait time of more than 15 minutes.  Note: If you leave the maximum average wait time blank, then the number displays the **Average Wait Time** metric. |

## Configuring a call button widget

If you are using [Embedded voice](https://support.zendesk.com/hc/en-us/articles/4408830696090), you can add a call button to Web Widget
(Classic).

If you're looking for information about how to add a call button to a mobile app, see
[Adding a call button to your mobile
app](https://support.zendesk.com/hc/en-us/articles/4408830559258).

Before you start, you must have created a digital line to associate with the call
button. For more information, see [Adding a digital line](https://support.zendesk.com/hc/en-us/articles/1260805715389).

**To add a call button to Web Widget (Classic)**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_channels_icon.png)
   **Channels** in the sidebar, then select **Talk and email > Talk**.
2. From the **Widget** tab, click **Add widget configuration**.
3. From the list of configurations, choose **Call us (via digital
   line)**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Talk_widget_digital_line_1.png)
4. On the Web Widget configuration page, select **Enable configuration on the
   Web Widget** to ensure this configuration is displayed in the
   widget.
5. Update the settings shown [in the table below](#topic_x4m_kzj_g4b__table_utp_wcn_h4b):

   Table 1.

   | Setting | Description |
   | --- | --- |
   | Nickname | Enter the configuration name. If you create multiple configurations of the widget, you need to use the configuration nickname in the Web Widget API to select which configurations to show on the current page. See [Advanced configuration of Talk in Web Widget (Classic)](https://support.zendesk.com/hc/en-us/articles/4408832257562#topic_ffj_xsy_hdb). |
   | Brand | Select the brand you want to associate with the configuration. |
   | Digital line | Use the drop-down list to choose the name of the digital line you want to associate with the call button. For help with digital lines, see [Understanding Embedded voice](https://support.zendesk.com/hc/en-us/articles/4408830696090). |

   ![](http://zen-marketing-documentation.s3.amazonaws.com/docs/en/Talk_widget_digital_line_2.png)
6. When you are finished, click **Save**.

## Modifying call options in an existing widget configuration

**To modify an existing widget configuration**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_channels_icon.png)
   **Channels** in the sidebar, then select **Talk and email > Talk**.
2. From the **Widget** tab, click to expand the widget configuration you
   want to edit.

   If you have multiple configurations, you can filter them by
   brand using the **All widget configurations** drop-down list in the
   upper-left portion of the screen.
3. Edit the settings and then click **Save**.