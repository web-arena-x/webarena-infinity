# Using Zendesk Support and Zendesk Knowledge together

Source: https://support.zendesk.com/hc/en-us/articles/4408882448922-Using-Zendesk-Support-and-Zendesk-Knowledge-together

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support with** | Guide Professional or Enterprise |

Zendesk Support and Zendesk Knowledge work in tandem to help you set up and manage your self-service customer experience and support workflow.

Zendesk Support is the powerful back-end of your support operations: defining your support workflow and helping you manage your users and ticket queue. Zendesk Knowledge is the help center you provide to your customers and it contains your knowledge base content and gives your customers easy access to request support from your staff.

As you’ll discover in this article, Support and Knowledge work closely together and some of the key elements of your customer experience, as it’s presented to your customers in your help center, are configured and enabled in Zendesk Support.

This article contains two main sections:

- [Enabling end users and agents to access and contribute to your self-service channel](#topic_jfy_5qj_nlb)
- [Enhancing and managing the self-service customer experience](zug_support_guide_together.html#topic_v1d_mrj_nlb)

The first explains the basics of setting up help center access for end users and agents and also how agents both promote and contribute to your self service efforts and goals. The other section provides information about how admins can use Support and Knowledge together to improve the customer support experience and how they can track, manage, and improve self service content.

If you’re just getting started with Zendesk Suite (and specifically setting up your help center and self service channel) and want to launch it quickly, the first section provides you with the essential information you need. The information in the second section is more advanced and may be steps that you want to take after launching your support solution.

Note: If you want to learn more about setting up a self service channel, see the series [Getting started with self-service](https://support.zendesk.com/hc/en-us/articles/4408885576346).

## Enabling end users and agents to access and contribute to your self-service channel

This section describes how you can enable end users and agents to access and contribute to your self service channel and contains the following topics:

- [Configuring end user access for submitting tickets and viewing your help center](#topic_v3b_zfd_v3)
- [Granting agents Knowledge admin privileges](#topic_r1f_4gd_v3)
- [Restricting view and edit access to specific content in your help center](#topic_uv2_331_53)
- [Directing customers to the self-service content in your help center](#topic_czm_dbn_ldb)
- [Providing feedback about and contributing new content to the knowledge base](#topic_5zm_cmt_ldb)

### Configuring end-user access for submitting tickets and viewing your help center

Because your customers are the key element in all that you do with Zendesk, the customer (or end user) records are shared across all products. This means that you need to configure user access and user roles in Support that will affect Knowledge.

Administrators in Zendesk Support can use the Customers and Security settings pages to define the type of access that you allow your customers. These access settings affect *both* Support and Knowledge access.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/customers-settings.jpeg)

Access to both Support and Knowledge is defined as being *open*, *closed*, or *restricted*.

- *Open* means that everyone can see your help center and submit support requests.
- *Closed* means your help center is visible to everyone but only the users that you add to your Zendesk account can sign in and submit support requests.
- *Restricted* means that your help center is visible to all users but only users with email addresses in domains that you approve are able to successfully submit support requests.

For Support, access determines if incoming support requests become tickets and user accounts are created. For Knowledge, access settings affect who can create tickets using your support request form.

Note: Access determines availability of your help center as a whole, but does not control visibility of individual articles (see [Restricting view and edit access to specific content in your help center](#topic_uv2_331_53)).

In Support, you can also configure what type of user authentication is used; how users register and sign-in to receive support and use your help center.

| Zendesk Support | Zendesk Knowledge |
| --- | --- |
| Define who can submit tickets, if customers are required to register, help center access, authentication methods. See:  - [Understanding options for end-user access and sign-in](https://support.zendesk.com/hc/en-us/articles/4408887573274) | Require users to sign-in to see and use your help center (this allows you to create a closed help center). See:  - [Restricting help center access to signed-in end users](https://support.zendesk.com/hc/en-us/articles/4408842656154) |

### Granting agents Knowledge admin privileges

An agent’s role in Knowledge is, by default, defined as *Knowledge Viewer*. This role allows them to participate in the knowledge base, but they don’t have any management privileges. Their permissions related to content are not role based, but are determined by user segments. (There’s another layer of access permission for content that is explained in [Restricting view and edit access to specific areas of content in your help center](#topic_uv2_331_53)).

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/managed_by_article_setting.png)

Administrators are defined as *Knowledge admins* and are granted all privileges in Knowledge, including all management privileges and access to all content, regardless of user segment. Administrators can also grant full Knowledge admin privileges to agents.

| Zendesk Support | Zendesk Knowledge |
| --- | --- |
| Grant an agent Knowledge admin privileges. See:  - [Changing an agent's role to grant Knowledge admin privileges](https://support.zendesk.com/hc/en-us/articles/4408845823386) | View a comparison of role permissions by role. See:  - [Understanding Knowledge roles and privileges](https://support.zendesk.com/hc/en-us/articles/4408827842458#topic_t44_db5_nv) |

### Restricting view and edit access to specific content in your help center

Note: This feature is not available on Suite Team.

After you’ve defined customer access and staff roles and access, you can further define which parts of the knowledge base in the help center can be seen and used by both end users and agents. You do this by creating *user segments*.

A user segment is a collection of end users and/or agents, defined by a specific set of attributes, used to determine access to help center content.

Each user segment contains either signed-in customers *or* agents. Additionally determine which signed-in users or agents are included, based on attributes in their user profiles in Support. For signed-in users, you can add the tags contained in their user profiles or the organization they’ve been added to (or both). For agents, it’s based on tags and the agent groups they belong to.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/user_seg_create.png)

User segments are the building blocks for user permissions. You apply user segments to a knowledge base article to define viewing access. And you use user segments to build management permissions that you apply to knowledge base articles to define editing and publishing permissions. You can apply only one user segment per article for visibility and one for management.

When you apply a user segment for visibility or management, only those users have permission to view or edit those knowledge base articles. User segments do not apply to Knowledge admins, who have access to all sections.

| Zendesk Support | Zendesk Knowledge |
| --- | --- |
| For customers, add tags to their user profile or add them to an organization and use these as criteria for user segments. For agents, use tags and the groups they belong to. Grant an agent Knowledge admin privileges.  See:  - [Adding tags to users and organizations](https://support.zendesk.com/hc/en-us/articles/4408881573658) - [Creating groups](https://support.zendesk.com/hc/en-us/articles/4408894175130) - [Creating organizations](https://support.zendesk.com/hc/en-us/articles/4408882246298) | Create user segments and apply them to articles in the knowledge base. See:   - [Creating user segments for Knowledge user permissions](https://support.zendesk.com/hc/en-us/articles/4408837707290) - [Creating management permissions to define agent editing and publishing rights](https://support.zendesk.com/hc/en-us/articles/4408827952538) - [Setting agent editing and publishing permissions on knowledge base articles](https://support.zendesk.com/hc/en-us/articles/4408834435738) - [Setting view permissions on articles with user segments](https://support.zendesk.com/hc/en-us/articles/4408824005914) |

### Directing customers to the self-service content in your help center

To help ensure that the self-service content you provide to your customers is discovered and used by your customers, it’s important to direct customers to it. You can help drive traffic to content in your help center using the agent interface in Zendesk Support.

You can add links to your help center articles in your global macros and agents manually add links to articles in their personal macros for replies to customers.

Agents can use Knowledge in the Context panel for easy access to help center articles. They can quickly search for and insert links to relevant articles in their replies without leaving the ticket.

Another option is to use autoreplies, which uses machine learning to automatically respond to support requests with a list of potentially relevant knowledge base articles.

Note: You can find other ideas for linking to and promoting your knowledge base content in [Best practices for driving traffic to your knowledge base and community](https://support.zendesk.com/hc/en-us/articles/4408828362522).

| Zendesk Support | Zendesk Knowledge |
| --- | --- |
| Agents can use Knowledge in the Context panel to insert links to help center articles in their ticket replies. Set up autoreplies to automatically respond to support requests with links to relevant help center articles.  See:  - [Searching for content in the knowledge section](https://support.zendesk.com/hc/en-us/articles/4408826700570) - [Linking, quoting, and pinning content to tickets](https://support.zendesk.com/hc/en-us/articles/5780128753946) - [Quickstart guide: Autoreplies with articles](https://support.zendesk.com/hc/en-us/articles/4408820349850) | Provide the knowledge base content in emails and web form. See:  - [Quickstart guide: Autoreplies with articles](https://support.zendesk.com/hc/en-us/articles/4408820349850) |

### Providing feedback about and contributing new content to the knowledge base

Note: This feature is not available on Suite Team.

Note: Your knowledge base is an invaluable resource for both your customers and your support staff. Ensuring that your content is accurate, up-to-date, and complete is essential.

Because your agents are constantly interacting with your knowledge base content and have firsthand experience with how effective it is, they should be active participants in its development and maintenance.

When you’re starting out to develop knowledge base content, you can analyze your support data to identify the areas that give your customers the most trouble or confusion and focus your efforts on documenting them.

On Enterprise plans, agents can use the Team Publishing features to collaborate on and manage content and you can also set up workflows for reviewing, approving, and publishing content.

| Zendesk Support | Zendesk Knowledge |
| --- | --- |
| Use the Reporting tools in Support to discover which customer issues need documentation. Use a ticket tagging process to flag issues that need documentation.  Use an About field on your ticket forms to capture and categorize issues that need attention and documentation.  Use the Knowledge Capture app to allow agents to contribute to the knowledge base from within the agent interface.  See:  - [Best practices for finding customer issues to start your knowledge base](https://support.zendesk.com/hc/en-us/articles/4408828230554) - [Zendesk on Zendesk: How we use the About field](https://support.zendesk.com/hc/en-us/community/posts/212671827) | Allow agents to directly manage and contribute content to the knowledge base. Allow agents to collaborate on creating and managing articles by setting up collaboration workflows with Team Publishing to review, approve, and publish content (Enterprise plans only).  See:  - [Allowing agents to add, edit, and delete articles in knowledge base sections](https://support.zendesk.com/hc/en-us/articles/4408834435738) - [About Team Publishing](https://support.zendesk.com/hc/en-us/articles/4408832609562) |

## Enhancing and managing the self-service customer experience

This section describes how you can enhance your self-service channel, monitor help center activity, and manage content and tickets created from help center comments. It contains the following topics:

- [Customizing and creating support request forms](#topic_p22_sw2_2db)
- [Setting up multiple branded versions of help center](#topic_wcm_dy2_2db)
- [Supporting multiple languages](#topic_5t2_k1n_ldb)
- [Embedding Zendesk Support features into your help center](#topic_hpx_51n_ldb)
- [Measuring user activity in your help center](#topic_ngh_xmt_ldb)
- [Moderating end-user content in your help center](#topic_brb_vnt_ldb)
- [Managing spam](#topic_swx_g4t_ldb)
- [Creating and managing tickets from help center comments](#topic_dlc_y4t_ldb)

### Customizing and creating support request forms

The support request form that’s available to customers in the help center is defined in Support. This form is displayed to customers in the help center when they click the **Submit a request** link in the upper-right corner of your help center. You don’t see this form in the help center when you’re signed-in as an admin or agent.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/hc_request_form.png)

The default version of the support request form contains the essential ticket data fields (email address, subject, and description) and enables customers to include an attachment. You can add custom fields and make other changes to this form as needed in Support.

On Enterprise plans, you can create multiple ticket forms for different types of support requests. For example, you can create a ticket form specifically for requesting a refund. These are created in Support and displayed to customers in the help center as support request options. You can also use ticket forms in business rules, including views, triggers, and automations.

| Zendesk Support | Zendesk Knowledge |
| --- | --- |
| Configure and customize the support request form. Note: On Enterprise plans, you can create multiple ticket forms for different types of support requests.  See:  - [Adding custom fields to your tickets and support request forms](https://support.zendesk.com/hc/en-us/articles/4408883152794) - [Creating ticket forms to support multiple request types](https://support.zendesk.com/hc/en-us/articles/4408846520858) | The support request form is displayed to customers in the help center. |

### Setting up multiple branded versions of a help center

On most plans, you can set up multiple help center versions for the different brands that you support (see [Creating a help center for one of your brands](https://support.zendesk.com/hc/en-us/articles/4408828794778)).

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/hc_brand_dropdown.png)

Brands are defined as customer facing identities can include their own visual branding elements, domain name, email support addresses, help center, and other customer contact channels.

Enabling multiple brands is done in Zendesk Support. This is where you define each brand’s settings (name, domain, logo, and so on) and also enable separate help centers for brands, if allowed on your plan. Once enabled, you separately manage each help center (for example, choosing the template, customizing the design, adding and managing content, restricting access to specific areas of content).

| Zendesk Support | Zendesk Knowledge |
| --- | --- |
| Add brands and enable separate help centers, as allowed. See:  - [Setting up multiple brands](https://support.zendesk.com/hc/en-us/articles/4408829476378) - [Creating a help center for one of your brands](https://support.zendesk.com/hc/en-us/articles/4408828794778) | Customize the look of and manage the content and users for each branded help center. See:  - [Viewing a help center for one of your brands](https://support.zendesk.com/hc/en-us/articles/4408832814362) |

### Supporting multiple languages

Note: Multi-language support requires Suite Growth or above *or* Support Professional or Enterprise with any Knowledge plan.

Enabling multiple language support is an independent process. You enable the languages you want to support for tickets in Support and enable the languages you want to support for your help center in Knowledge.

When you enable other supported languages, you’re responsible for providing translations of the content you add. For Support that means any content you add to your business rules and support ticket workflow (macros, automations, and triggers). For Knowledge that means any customized theme content, your help center name, category and section headings, and articles in your knowledge base. Only standard text in your help center, such as "Submit a request," is automatically translated for users.

| Zendesk Support | Zendesk Knowledge |
| --- | --- |
| Configure your account settings to support multiple languages. Manage the translations of content contained in your macros, automations, and triggers using a feature called dynamic content.  Set and detect a user’s language.  Include language as a condition in your business rules.  See:  - [Adding multiple languages to Zendesk Support](https://support.zendesk.com/hc/en-us/articles/4408888770714) - [Providing multiple language support with dynamic content](https://support.zendesk.com/hc/en-us/articles/4408882999066) - [Setting and detecting a user's language](https://support.zendesk.com/hc/en-us/articles/4408888770714#topic_tmu_gno_ze) - [Using a requester's language in your business rules](https://support.zendesk.com/hc/en-us/articles/4408888770714#topic_uqw_ufw_bf) | Specify a default language for your help center and enable any languages you want to support in it. Localize (translate), words used in your help center structure and any other text snippets you want to add to the help center user interface.  Create language versions of your knowledge base articles and select a provider and a process for translating and publishing your articles.  See:  - [Configuring your help center to support multiple languages](https://support.zendesk.com/hc/en-us/articles/4408827609882) - [Localizing help center content](https://support.zendesk.com/hc/en-us/articles/4408834328090) - [Creating and managing translated content for your knowledge base](https://support.zendesk.com/hc/en-us/articles/4408886903450) |

### Measuring user activity in your help center

User activity in your help center is tracked in Explore and is available in the Zendesk Knowledge dashboard. In the dashboard, you can track knowledge base, search, Knowledge, and bot statistics.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/explore_guide_db_tabs.png)

For the knowledge base, Support tracks the number of articles created, views, votes, subscriptions, and comments. Search reporting provides insight such as what your customers are searching for, if they find what they’re looking for, and the number of tickets created after a search.

And finally, you can optionally use Google Analytics to track website engagement metrics such as number of sessions and users, page views, average session duration, bounce rate and so on. You set up a Google Analytics account and then connect it to Knowledge.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ga_audience_overview_charts.png)

For more information about measuring help center activity and the success of your self-service channel, see [Getting started with self-service - Part 7: Tracking essential self-service metrics](https://support.zendesk.com/hc/en-us/articles/4408894139930).

| Zendesk Support | Zendesk Knowledge |
| --- | --- |
| Use the Zendesk Knowledge dashboard in Explore to track knowledge base, search, Knowledge, and bot activity. See:  - [Analyzing knowledge base activity](https://support.zendesk.com/hc/en-us/articles/4408830631962) - [Analyzing help center search results](https://support.zendesk.com/hc/en-us/articles/4408818465562) - [Analyzing your Knowledge activity](https://support.zendesk.com/hc/en-us/articles/4408887529370) - [Analyzing your autoreplies for article recommendations](https://support.zendesk.com/hc/en-us/articles/4409155069466) | Set up a Google Analytics account, add the tracking ID number to the Knowledge Admin settings page, and then track website engagement activity in Google Analytics. See:  - [Enabling Google Analytics for your help center](https://support.zendesk.com/hc/en-us/articles/4408828643098) |

### Moderating end-user content in your help center

Note: This feature is not available on Suite Team.

End user participation in your help center is vital for building community and also helps you scale your support because many customers are happy to help other customers successfully use your products and services. However, it can also make sense to control the end-user content contributions, especially if you’re trying to manage spam (see [Managing spam](#topic_swx_g4t_ldb)).

You can prevent all end-user contributed content or only end-user content that contain specific words from being published until you allow it to be. When you enable content moderation, content is sent to a queue, based on your moderation settings, to be reviewed and approved by a Knowledge admin before being published in your help center.

Moderating end-user content requires Knowledge admin privileges, as described in [Granting agents Knowledge admin privileges](#topic_r1f_4gd_v3).

| Zendesk Support | Zendesk Knowledge |
| --- | --- |
| Grant agents Knowledge admin privileges to agents so that they can moderate content in Knowledge. See:  - [Changing an agent's role to grant Knowledge admin privileges](https://support.zendesk.com/hc/en-us/articles/4408845823386) | For administrators and agents with Knowledge admin privileges, enable content moderation, manage end-user contributed content, and handle spam and spam user accounts. See:  - [Moderating end-user content](https://support.zendesk.com/hc/en-us/articles/4408894193562) |

### Managing spam

Both Support and Knowledge provide tools for preventing, managing, and removing spam and the user accounts associated with spam.

Support provides filtering for incoming support requests from the email channel, so that you don’t see and have to deal with it in your ticket queue. However, not all spam is caught in that filter and there are also reasons why some types of incoming support requests and emails may be flagged as suspicious. In these cases, Support suspends them and holds them in the Suspended Tickets view so that you can manually moderate them.

In Knowledge, spam comes in the form of knowledge base comments. To deal with spam in your help center, the spam filter is enabled by default to prevent new and edited end-user posts and comments that appear to be spam from being published to your help center.

You can manually flag and remove individual incidents of spam that might get through the filter. As you manage individual spam in Knowledge, you have the option of not only deleting the spam content but also of suspending the user who created it. When you suspend a user, that user can no longer submit tickets or post or comment in your help center.

For more information about all the spam prevention tools in place in the help center, see [About help center spam prevention](https://support.zendesk.com/hc/en-us/articles/4408883183770).

| Zendesk Support | Zendesk Knowledge |
| --- | --- |
| Zendesk Support filters and prevents spam from incoming support channels such as email. Incoming email that is considered suspicious but not clearly spam is suspended and placed in the Suspended Tickets view.  Users can be suspended when reviewing a suspended ticket and also in the user’s account profile.  See:  - [Understanding and managing suspended tickets and spam](https://support.zendesk.com/hc/en-us/articles/4408889141146) - [Suspending a user](https://support.zendesk.com/hc/en-us/articles/4408889293978) | Manually mark knowledge base comments as spam. Optionally also suspend an end user and delete all the content they created in your help center.  Enable content moderation to control end-user content that appears in your help center.  See:  - [Using the spam filter to prevent spam in help center](https://support.zendesk.com/hc/en-us/articles/4408888801690) - [Marking content as spam and removing it from your help center](https://support.zendesk.com/hc/en-us/articles/4408838281882) |

### Creating and managing tickets from help center comments

Your help center is your self-service channel and its purpose is to enable your customers to help themselves solve their problems without contacting you for support (in other words, prevent tickets from being created). However, you also need to monitor and be an active participant in your help center.

Most importantly, don’t let questions asked in your help center go unanswered. That’s why it’s a best practice to assign one or more agents to monitor your help center and answer their questions when other customers don’t.

Sometimes answering their questions requires help from other people in your support organization. When that happens, you can create tickets from help center comments, track down the answer, and then respond with a new comment or create a ticket on the commenter’s behalf and take the issue offline.

| Zendesk Support | Zendesk Knowledge |
| --- | --- |
| Manage and resolve tickets created from comments in your help center. | Create tickets from comments to follow up on a user question or take an issue offline. See:  - [Creating a ticket from a knowledge base comment](https://support.zendesk.com/hc/en-us/articles/4408834867610) |