# Routing incoming calls with IVR

Source: https://support.zendesk.com/hc/en-us/articles/4408885628698-Routing-incoming-calls-with-IVR

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support with** | Talk Professional or Enterprise |

Using multi-level interactive voice response (IVR), or phone trees, you can route customers to the right agent or department, provide recorded responses for frequently asked questions, and deflect calls by allowing callers to switch from a live call to a text message.

This article contains the following topics:

- [Understanding IVR](#topic_mwh_24k_bzb)
- [Recording an IVR greeting](#topic_vq2_1sf_yt)
- [Creating an IVR menu](#topic_sms_bsf_yt)
- [Assigning an IVR menu to a number](#topic_ztr_5sf_yt)

Related articles

- [Interactive Voice Response definition, benefits + steps](https://www.zendesk.com/blog/what-is-ivr/).

## Understanding IVR

Implementing IVR involves the creation of an IVR menu or tree that callers navigate through key presses. You can build a simple phone tree with one level or, if you have a complex support team structure, you can layer multiple menu levels together.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/zug_voice_ivr_overview.png)

Consider the following functionality and limitations before implementing IVR for your account:

- You can't use IVR for incoming calls from a digital line. For more information about digital lines, see [Understanding Embedded voice](https://support.zendesk.com/hc/en-us/articles/4408830696090).
- If [call recording is on](https://support.zendesk.com/hc/en-us/articles/4408831738266), recording continues after you transfer a call internally (to another agent or group) or externally (to an end-user or external number).
- If your plan doesn't support IVR, you can route calls using group routing. See [Routing incoming calls to groups of agents](https://support.zendesk.com/hc/en-us/articles/4408885952922).

### Using IVR with omnichannel routing

- IVR is automatically supported by omnichannel routing. No configuration is required to activate omnichannel routing to assign IVR calls to agents. When using omnichannel routing, a ticket is created for incoming calls as soon as they enter the queue. That means you can run ticket triggers on incoming calls before they are answered.

 When you use IVR to add ticket tags based on keypresses, those tags can then be used in [queue](https://support.zendesk.com/hc/en-us/articles/6712096584090) and [trigger](https://support.zendesk.com/hc/en-us/articles/4408886797466) conditions to influence how the call is routed, such as changing the ticket's group assignment, priority, or skills and determining the ticket's omnichannel routing queue. You can also [generate Explore reports on IVR keypresses based on ticket tags](https://support.zendesk.com/hc/en-us/articles/6257973320090). See [About omnichannel routing](https://support.zendesk.com/hc/en-us/articles/4409149119514).
- If you've turned on [omnichannel routing](https://support.zendesk.com/hc/en-us/articles/4409149119514), you can define [custom queues](https://support.zendesk.com/hc/en-us/articles/6712096584090) if you need to route tickets to more than one group on a keypress.
- If you have already configured IVR and want to turn on omnichannel routing, remove all non-primary groups from your IVR menu before activating omnichannel routing.

### Using IVR with SIP lines

- [SIP-IN lines](https://support.zendesk.com/hc/en-us/articles/8397091234586) automatically support IVR. If you're using a SIP-IN line, the following applies:
 - For the textback and external number IVR actions, if no new number has been entered by the caller, the caller number for IVR actions is extracted from the username contained in the "from" SIP URI.
 - For the transfer to external number IVR action, the call is dialled from the phone number selected as the outbound ID for over flow/forwarding and IVR transfers in the SIP line settings.

    Note: IVR menus that require transferring to an external number will be unavailable if the customer does not have an associated outbound number configured in the settings tab of the SIP-IN line.

## Recording an IVR greeting

Each IVR menu requires at least one IVR greeting listing the options and corresponding key presses. If your IVR menu will be complex with multiple levels and options, you might want to come back to this step after you've built out your menu (see [Creating an IVR menu](#topic_sms_bsf_yt)).

Only Support administrators can modify or delete greetings.

**To record a personalized IVR greeting and prompts**

- Follow the steps to create a custom greeting in [Managing outgoing greetings](https://support.zendesk.com/hc/en-us/articles/4408821594650). Select **IVR** as the greeting type.

 When you create your greeting, keep in mind that when an IVR greeting message is played to a caller, they must listen to the whole message before they can press a key to interact with the IVR.

## Creating an IVR menu

The way you structure your IVR menu determines how callers are routed and what options they hear.

**To create a new menu**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_channels_icon.png)
   **Channels** in the sidebar, then select **Talk and email > Talk**.
2. Click the **IVR** tab.
3. Click **Add menu**.
4. In the menu that's added, click the **Settings** tab and enter a name for the menu.
5. Click the **Menu levels** tab.
6. The first menu level, Main menu, is already created for you. If you want additional, secondary menu levels that callers can reach from the main menu, click **Add menu level**.
7. Click the **Name** field of a menu level to edit the menu level name.
8. Choose an IVR greeting from the **Greeting** menu. You can only choose greetings of the type IVR.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/voice_ivr_selectgreeting.png)
9. Click **Add Route** to add a new menu option.

   ![IVR Add route](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Talk_ivr_route_2.png)
10. For **Keypress**, select an available key or select **Default**.

    If the caller hasn't pressed a key after the greeting plays three times, or if the caller presses the wrong key four times during the greeting, the default route will be used. If you haven't set a default route, the caller will be disconnected.
11. (Omnichannel routing only) In the **Tags** field, enter one or more tags you want applied to the tickets when users press this key in the IVR menu.
    These tags can be used in triggers, omnichannel routing, and Explore reports. You can add multiple tags, but cumulatively they can't exceed 100 characters in length.

    Note: Tags don't persist if a call is routed to a different phone line.
12. For **Greeting**, select an optional greeting which will be played to the caller before they take action on the call. This greeting must be of the type IVR.
13. Select one of the following actions:

    Note: The available actions will differ depending on the type of greeting you select.

    - **Voicemail**: Routes the call to the number's voicemail.
      Keep in mind that if you haven't selected a greeting in the field above, no greeting will play (just the beep and straight to recording). When you select a voicemail action, you'll also be prompted to enter a group that voicemail tickets will be associated with.
    - **Group**: Choose one or more groups of agents to route the call to. Unless a greeting is assigned to this group, the caller will be placed in the queue and hear the Wait greeting set for the number. The Available agents greeting will not be played.
      For more information about managing groups, see [Creating groups](https://support.zendesk.com/hc/en-us/articles/4408894175130).
    - **Number**: Routes the call directly to the specified number.
      When you select this action type, you'll also be prompted to enter the number to route calls to. When routing to an external number in an IVR, that call is not recorded, and a ticket is not created for the call. Additionally, the number you enter cannot use an extension number.

      Important: When you route a call from your IVR to another number, you will incur an extra charge for the call forwarding.
    - **IVR Menu**: Routes the call to another menu level within the same IVR menu. For example, you might want callers to press 1 for VIP support from the main menu, then be directed to another menu with options for VIP billing, VIP sales, etc. When you select the IVR menu action type, you'll also be prompted to select an IVR menu that calls will be routed to.
    - **Text back**: Switches the interaction over to text by confirming the customer's number, then disconnecting the call and sending a text message. An SMS ticket will be created for this interaction with the customer so the conversation can continue by text. When you select a text back action, you'll be prompted to select a language to use when asking the caller to enter the phone number for text back, to select the phone number to send the message from, and to enter the first message of the switch to text.
14. Select a **Group** to route the call to. From the list of groups, turn on the ones you want, then, in the **Primary group** menu, choose the group that calls will be routed to first. If agents in the primary group are not available, the call will be routed to one of the other selected groups.
    If no agents are available and the caller leaves a voicemail, it will be assigned to the primary group.
15. Click **Save**.
16. Repeat steps 9-15 to add additional routes.
17. Click **Save** to save the IVR menu.

## Assigning an IVR menu to a number

Once you've built your IVR menu, assign it to a number.

**To assign an IVR to a number**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_channels_icon.png)
   **Channels** in the sidebar, then select **Talk and email > Talk**.
2. Click the number you want to edit.
3. Select the **Routing** tab.
4. Toggle the **Enable IVR?** field to on.
5. Select the menu you want to use from the **IVR menu**.
6. Click **Save changes**.