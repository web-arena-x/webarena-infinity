# History chat details CSV glossary

Source: https://support.zendesk.com/hc/en-us/articles/4408886507802-History-chat-details-CSV-glossary

---

![](https://support.zendesk.com/hc/article_attachments/360033063874/mceclip0.png)

This article contains a glossary of the metrics included when exporting chat details from the History tab.

The CSV export file will show 45 columns, containing all the information of each chat session during the time session selected on the dashboard.

For more information on the History feature, see [Browsing past chats in History](https://support.zendesk.com/hc/en-us/articles/4408893866778-Browsing-past-chats-in-History).

**Glossary**

| | |
| --- | --- |
| Metric | Description |
| chat\_id | Unique chat session identifier |
| visitor\_id | Unique visitor identifier; unique for every visit even when the visitor email address has already been used previously |
| timestamp (GMT+0) | Date and time the visitor sent their first message. |
| type | The classification of a session on whether the message was received when the account was online (chat) or offline (offline message). |
| duration (seconds) | The time between the first and last message sent, regardless of the sender. |
| started\_by | The party who initiated the chat Parties include:    • Agent    • Visitor    • Trigger    • None (applies to offline messages only) |
| visitor\_name | The name provided by the visitor in the pre-chat form; the last/final name indicated/updated by the visitor before the chat ends |
| visitor\_email | The email address provided by the visitor in the pre-chat form; the last/final email indicated/updated by the visitor before the chat ends |
| visitor\_phone | The phone number provided by the visitor in the pre-chat form or during chat |
| visitor\_notes | Additional information about the customer; may only be added by agents in the account |
| session\_city | City of the visitor in the chat session |
| session\_start\_date (GMT+0) | Date when the chat session started. The chat session starts when a visitor first lands on a website that activates the chat, not when the visitor sends their first message. |
| session\_end\_date (GMT+0) | Date when the chat session ended. A session ends when the visitor clicks "end chat" within an ongoing chat or when the visitor leaves the website. |
| session\_ip | IP address of the visitor |
| session\_region | Region of the visitor where the chat session happened |
| session\_id | Unique ID for the specific chat session |
| session\_platform | The operating system used by the visitor |
| session\_user\_agent | Information of the web browser and operating system used by the customer |
| session\_country\_code | Code of the country where the chat was initiated |
| session\_country\_name | Name of the country where the chat was initiated |
| session\_browser | Browser used by the visitor during chat |
| visitor\_message\_count | The total number of messages sent by the visitor |
| agent\_message\_count | The total number of messages sent by the agent(s) who handled the chat. |
| total\_message\_count | The total number of messages sent by all the parties who joined the chat. |
| is\_triggered | Shows "true" when the chat was triggered (a trigger ran in the session) and "false" when no trigger ran in the session. This is in conjunction with the "Visitor Triggered?" condition. |
| is\_missed | Shows "true" when the chat was missed and "false" when the chat was accepted |
| is\_unread | Applies offline messages and missed chats that haven't been read/clicked yet |
| landing\_page | This is the section accessed by the visitor when they clicked a hyperlink on a certain web page, typically the website's home page |
| referral | Any domain that originates and redirects traffic to your domain where the visitor sees the widget |
| tags | All the tags added to the chat. Tags are separated by commas |
| department\_name | The department to where the chat was routed |
| agent\_names | The names of the agents who served in the chat session |
| agent\_ids | The agent IDs of all the agents who served the chat |
| rating\_score | The satisfaction rating of the entire chat session Ratings include the following:    • good    • bad    • none (chats without ratings) |
| rating\_comment | The comment when the chat was rated, either good or bad |
| max\_response\_time (seconds) | The longest time it took the agent to respond to a message in the chat |
| avg\_response\_time (seconds) | The average time it takes for an agent to respond to messages in the chat |
| first\_response\_time (seconds) | The time in seconds, taken by the agent to pick the chat and send the initial message |
| zendesk\_ticket\_id | Zendesk Support ticket ID associated with the chat session. Appears blank when there's no ID (usually when ticket creation is set to manual) |
| skills | All the agent skills that matched the visitor's information |
| skill\_match | The agent skill that matched the information set by the visitor and to where the chat was routed |
| last\_conversion\_goal\_name | Name of the goal conversion |
| last\_conversion\_goal\_id | A unique conversion identifier |
| last\_conversion\_date | The date when the goal was considered a conversion |
| last\_conversion\_attribution | The name of the agent to which the goal converted was attributed |