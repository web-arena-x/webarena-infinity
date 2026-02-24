# Understanding different types of tags in Chat

Source: https://support.zendesk.com/hc/en-us/articles/4408888643866-Understanding-different-types-of-tags-in-Chat

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support with** | Live chat and messaging Team, Professional, or Enterprise |

Zendesk Chat offers two different types of tags to categorize your visitors and chat sessions:

- **Chat tags** contain information about the specific content of a chat session.
- **Javascript API and trigger tags** contain more general information about the visitor.

You can use either or both types of tags to better understand your chat traffic. There are important differences in how these types of tags are added, stored, and displayed.

Table 1.

| | Chat tags | Javascript API and trigger tags |
| --- | --- | --- |
| How they're added and removed | - Directly in the chat panel. For details, see [Managing individual tags in the chat panel](../live-chat-agent-guide/adding-tags-to-chat-sessions.md#topic_vvx_lnm_nt). - Using a shortcut with an associated chat tag. For details, see [Adding tags with shortcuts](../live-chat-agent-guide/adding-tags-to-chat-sessions.md#topic_wdz_jtm_nt). - In History for past chats and offline messages. | - Through the API using the API calls addTags and removeTags. For details, see the [Javascript API documentation](https://api.zopim.com/files/meshim/widget/controllers/LiveChatAPI-js.html). - With a trigger using the actions Add tag and Remove tag. For details, see [Chat trigger conditions and actions reference](https://support.zendesk.com/hc/en-us/articles/4408842880282). - In History for past chats and offline messages. |
| What they're used for | Categorize chat sessions based on actual content of conversation. For example, you might add a reporting\_issue tag to customers who are having issues with your reporting feature. Chat tags apply to individual conversations; they are not intended for overall user management. | Add details about a visitor based on information other than chat content. For example, you could add a returning\_customer tag to visitors who have previously purchased something on your website. |
| How available tags are determined | Admins add new tags to the Predefined List and, depending on settings, can create tags on the fly in shortcuts and the chat panel. Agents can only select from existing tags, not create new ones. For details, see [Setting up chat tags](setting-up-chat-tags.md). | Can enter existing tags or any new tag when setting up triggers and API code. Tags do not appear on the Predefined List. |
| How to search for them | Use advanced search Tags field in History. | Use advanced search Tags field in History. |
| How to format | 140 character maximum with no blank spaces or special characters allowed. | Tags can have blank spaces and special characters. |