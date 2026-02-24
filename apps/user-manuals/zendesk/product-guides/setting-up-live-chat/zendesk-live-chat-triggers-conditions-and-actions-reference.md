# Zendesk live chat triggers conditions and actions reference

Source: https://support.zendesk.com/hc/en-us/articles/4408842880282-Zendesk-live-chat-triggers-conditions-and-actions-reference

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **Support with** | Live chat and messaging Team, Professional, or Enterprise |

Zendesk live chat triggers allow you to add information about your customers, improve workflow routing, and handle spam requests.

For more information about live chat triggers, see [Zendesk chat triggers resources](https://support.zendesk.com/hc/en-us/articles/4408842880282).

For information on messaging triggers, see [Messaging triggers conditions and actions reference](https://support.zendesk.com/hc/en-us/articles/8015292388378).

This article contains the following tables:

- [Selecting run events for live chat triggers](#topic_pgr_rsj_d4b)
- [Building live chat trigger condition statements](#topic_d3p_q5f_rhb)
 - [Trigger operators](#topic_abf_q5f_rhb)
- [Building live chat trigger action statements](#topic_hxz_q5f_rhb)
 - [Using placeholders in live chat trigger action statements](#topic_n5j_r5f_rhb)

## Selecting run events for live chat triggers

When you create a trigger, you must select a *run event*. These events determine whether that trigger will run, check its conditions, and perform its defined actions. Run events are selected when creating a trigger using the **Run trigger**drop-down.

Table 1. Trigger run events

| Firing event | Description |
| --- | --- |
| When a visitor has loaded the chat widget | Runs the trigger when the chat widget appears on the page but the visitor hasn't interacted with it. Note: Selecting this firing event overrides pre-chat forms. To continue using your pre-chat form, use other firing events. |
| When a visitor requests a chat | Runs the trigger when the visitor requests a chat. |
| When a chat message is sent | Runs the trigger when the visitor has sent text in the chat widget. |

## Building live chat trigger condition statements

Condition statements consist of conditions, field operators, and condition values (these vary depending on the condition selected). Condition statements are essentially ‘if’ statements that return 'true' values that meet the specified criteria. When '**Check All of the Following Conditions**' is selected, the first condition statement that evaluates to false terminates the trigger. When '**Check Any of the Following Conditions' is selected**', only one condition needs to be true for the actions to fire.

You cannot use a combination of **Check all of the following conditions** and **Check any of the following conditions** when creating a live chat trigger.
You can only select one option or the other. This is also not possible in Developer view.

Note: Zendesk has introduced limits to some trigger conditions. Existing triggers exceeding these limits will be disabled. When you re-enable them, you will receive an error. Condition limits are included in the table below.

Table 2. Trigger conditions

| Condition | Description |
| --- | --- |
| **Time/Date** | |
| Hour of day | Hour of the Day (Universal Time Clock): **0** = Midnight **23** = 11 p.m. Note that the Hour of day condition uses the hour only, and **does not** include minutes. |
| Day of week | Day of the Week: **0** = Monday **6** = Sunday |
| Still on site | A condition check of whether the user is still on the domain after X seconds since the scenario chosen has elapsed. Max 3600 seconds |
| Still on page | A condition check of whether the user is still on the same page after X seconds since the scenario chosen has elapsed. Max 3600 seconds |
| **Location of visitor** | |
| Visitor IP | IP address of visitor |
| Visitor host name | Host name (domain) associated with the visitor's IP address |
| Visitor city | City name associated with the visitor's IP address |
| Visitor region | Region the visitor is from, according to [GeoIP](https://www.maxmind.com/en/geolocation_landing). For the US and Canada, we use the ISO-3166-2 regions. These are the different states (e.g. Vermont). For everywhere else, we use the FIPS 10-4 standard. The GeoIP website has a CSV file which lists all the different regions: http://www.maxmind.com/download/geoip/misc/region\_codes.csv |
| Visitor country code | Two-letter country code of the visitor's IP address. Codes are case-sensitive and should be upper-case. |
| Visitor country name | Country name associated with the visitor's IP address |
| **Previous visit information** | |
| Visitor previous visits | Number of previous independent visits: **0** = First time visit Max value 2.1 million |
| Visitor previous chats | Number of previous independent chats initiated with an agent: **0** = First time chatter |
| **Page information** | |
| Visitor page URL | Current URL of visitor (Widget must be installed on this page) |
| Visitor page title | Current title of page visitor is on (Widget must be installed on this page) |
| Visitor page count | Number of pages visitor has viewed. First page = **1** |
| Previous page | URL of the previous page the user was on. |
| **Visitor information** | |
| Visitor name | Name of visitor |
| Visitor email | Email of visitor |
| Visitor referrer | Referrer URL of visitor, if applicable, determined from content headers |
| Visitor search engine | Referring search engine, if applicable. Note that these values are case-sensitive and should be lowercase: **google** **yahoo** **bing** **yandex** |
| Visitor search terms | Referring search terms, if applicable |
| Visitor tag | Tag (Applied via *Add tag* action) |
| Visitor triggered | Triggered visitor (activated by Set Triggered action). Select either of the following from the drop-down menu: **True** **False** |
| Visitor department | Visitor's department, set by the action *Set visitor department* or Javascript API. |
| **Software/Computer of visitor** | |
| Visitor user agent | Visitor's user agent string |
| Visitor browser | Browser used by visitor |
| Visitor platform | Platform used by visitor |
| **Online statuses** | |
| Account status | Status of your Zendesk Chat account which works as a hierarchy system. **Online** **Away** **Offline**   - If one agent is online (and the rest are away or   offline) then the account status is online and the   **Online** Trigger will fire. - If one agent is away (and the rest are offline) then the   account status is away and the **Away** trigger will   fire - If all agents are offline then the account status is   offline and the **Offline** trigger will fire. |
| Department status | Status of the selected Zendesk department. **Online** **Away** **Offline** |
| Visitor status | Status of Visitor: **Online** **Idle** (no mouse or keyboard movement in the chat window for 10 minutes) |
| **Chat-related information** | |
| Visitor is chatting | 'true' if the visitor is currently in an active chat session. |
| Visitor requesting chat | 'true' if the visitor is requesting a chat by hitting *Send* in their chat message. 'false' if the visitor is not requesting a chat. |
| Visitor served | 'true' if the visitor is currently being served by an agent (for instance, an agent has opted to serve the customer and has sent their first message in the chat). 'false' if an agent has not sent a response to the visitor. |
| Sender | Name of sender of the chat message |
| Sender type | Type of sender. Note that these values are case-sensitive and should be lowercase: **visitor** **agent** |
| Message | The message being sent |
| Department | Department (name) that visitor chooses from the pre-chat form |
| **Visitor queue** | |
| Queue size (account) | Total number of incoming chat requests for the account. Note that the condition targets the total account queue, and does not measure the department queue. |

### Operators for trigger condition statements

Use the following operators to build trigger condition statements.

Table 3. Trigger operators

| Operator | Description |
| --- | --- |
| Equals | Exact match ``` = 5 returns true only when 5 ``` |
| Less than | Less than the number entered, but not including ``` < 10 returns true from 0-9 ``` |
| Greater than | More than the number entered ``` > 120 returns true from 121 to 1,000,000,000,000,000,000 ``` |
| Less than or equal to | An exact match or less than the number entered ``` <= 3 returns true on a 3, 2, 1, or 0 ``` |
| Greater than or equal to | An exact match or more than the number entered ``` >= 600 returns true from 600 to 1,000,000,000,000,000 ``` |
| Is not equal | Anything but the value entered ``` != 0 returns true for any number but 0 ``` |
| Contains | String includes the following text ``` "help" matches true with "help, i need somebody" ``` |
| Does not contain | String does not include the following text ``` "help" matches true with "not just anybody" ``` |
| Reg Ex | Matches for regular expression values using the [Python RegEx framework](https://docs.python.org/2/library/re.html). This field looks for a *full* match, not a partial. For assistance, you can use [Pythex](https://pythex.org/) as a quick-reference and validation tool. ``` (?P<year>(?:19|20)\d\d)(?P<delimiter>[- /.])(?P<month>0[1-9]|1[012])\2(?P<day>0[1-9]|[12][0-9]|3[01]) Test String: 2014-07-28 String match: 2014-07-28 ``` |

## Building live chat trigger action statements

Action statements define what occurs if all the condition statements are true and the trigger fires. You can think of action statements as ‘then’ statements: if all of your conditions are true, then perform these actions to update the user and optionally send notifications.

Table 4. Trigger actions

| Action | Description |
| --- | --- |
| Send Message to visitor | Sends the given message to the visitor Note: If the account is offline, this action will not work. |
| Set triggered | Set Triggered can be one of two values and applies a flag which can be used in conjunction with the 'Visitor Triggered?' condition. Select one of the following from the drop-down menu: - **True** - **False**   Note: If the account is offline, this action will not work. |
| Wait | Delay (in seconds) before the next action fires Note: If you have multiple triggers that must be executed in a certain order, you need to add at least one second of wait time between each trigger. This is required due to the fact that triggers do not run in a particular order and are evaluated and executed simultaneously. |
| Add tag | Adds a tag to the ticket |
| Remove tag | Removes a tag from the ticket |
| Set name of visitor | Sets the visitor's name |
| Set visitor department | Adds a department to the visitor profile. When this action is selected, a drop-down menu appears, allowing you to select an available department. **Only works when Run trigger is set to When a visitor has loaded the chat widget**. |
| Replace note | Replaces the note of the visitor's profile |
| Append note | Adds to the note of the visitor's profile |
| Block visitor | Bans the visitor from accessing your chat service. See [Banning visitors from accessing Chat](https://support.zendesk.com/hc/en-us/articles/4408824467098) for more information on blocking visitors. |
| Request email (continuous conversations) | Sends automated message to visitor requesting an email for continuous conversation re-engagement. See [Allowing customers to continue their conversation over email](https://support.zendesk.com/hc/en-us/articles/4408829095706) for more information. |

Note: For the trigger actions, **Send Message to Visitor**, **Replace Note**, **Set Name of Visitor**, and **Append Note**, to use the @ symbol, you must include an extra @ symbol. For example, user@domain.com should be entered as user@@domain.com.

### Using placeholders in live chat trigger action statements

Placeholders are references to visitor details you can use in trigger action statements. When the trigger is fired, the placeholder pulls in the current visitor and session information.

Table 5. Trigger placeholders

| Placeholder | Type | Description |
| --- | --- | --- |
| @hour\_of\_day | Integer | Current hour of the day (UTC timezone). 0 - 23 |
| @day\_of\_week | Integer | Current day of the week (0 = Monday, 6 = Sunday) |
| @visitor\_ip | String | City the visitor is from (based on IP address) |
| @visitor\_hostname | String | Host name of the visitor's IP address |
| @visitor\_city | String | Visitor's city |
| @visitor\_region | String | Region the visitor is from (based on IP address) |
| @visitor\_country\_code | String | Two-letter country code of where the visitor is from (based on IP address). Codes are case-sensitive and should be upper-case. |
| @visitor\_country\_name | String | Country the visitor is from (based on IP address) |
| @visitor\_page\_url | String | URL of the page the visitor is currently on |
| @visitor\_page\_title | String | Title of the page the visitor is currently on |
| @visitor\_referrer | String | Visitor's referral URL |
| @visitor\_search\_engine | String | Search engine the visitor used to find your website (can be blank) |
| @visitor\_search\_terms | String | Search terms the visitor used to find your website (can be blank) |
| @visitor\_user\_agent | String | Visitor's browser User-Agent string |
| @visitor\_browser | String | Visitor's browser |
| @visitor\_platform | String | Adds to the note of the visitor's profile |
| @account\_status | String | Status of your account (*online*, *away*, or *offline*) |
| @visitor\_previous\_visits | String | Number of previous independent visits |
| @visitor\_previous\_chats | String | Number of previous independent chats inititated with agent |
| @visitor\_name | String | Name of visitor |
| @visitor\_status | String | Visitor status (*online*, *idle*, or *offline*) |
| @visitor\_time\_on\_page | String | Visitor's time spent on current page |
| @visitor\_time\_on\_site | String | Visitor's time spent on site during current log in |
| @visitor\_page\_count | String | Number of pages viewed by visitor |
| @visitor\_requesting\_chat | String | *True* if visitor requested chat |
| @visitor\_served | String | *True* if visitor is currently being served by an agent |
| @visitor\_tags | String | Tags applied to visitor |
| @visitor\_triggered | String | Triggered visitor (*true* or *false*) |
| @referrer | String | The URL where the visitor's current session originated |