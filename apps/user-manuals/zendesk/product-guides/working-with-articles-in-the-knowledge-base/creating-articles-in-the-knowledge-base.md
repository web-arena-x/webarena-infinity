# Creating articles in the knowledge base

Source: https://support.zendesk.com/hc/en-us/articles/4408839258778-Creating-articles-in-the-knowledge-base

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support with** | Guide Professional or Enterprise |

Knowledge admins can create new articles in the knowledge base. Agents who are not Knowledge admins can create articles if they have [management permissions](https://support.zendesk.com/hc/en-us/articles/4408827952538). End users can't contribute articles to the knowledge base.

You must have at least one section in the knowledge base before you can start adding articles. When you create an article, you must assign it to a section. For more information, see [Anatomy of the help center](https://support.zendesk.com/hc/en-us/articles/4408846795674#topic_ol5_3fd_43).

Note: This article describes creating articles with the new article editor. For more information about transitioning from the legacy editor to the new article editor, see [Transitioning to the new article editor: Phase overview](https://support.zendesk.com/hc/en-us/community/posts/9228848607002).

Topics covered in this article:

- [Creating articles and adding content](#topic_fwm_vkx_cfc)
- [Configure article settings](#topic_bpt_tdq_cy)
- [Save and publish articles](#topic_ngr_25x_cfc)

Related article:

- [Migrating existing content to help center](https://support.zendesk.com/hc/en-us/articles/4408828053146)
- [Editing articles in the knowledge base](https://support.zendesk.com/hc/en-us/articles/9185667124506)

## Creating articles and adding content

You can create a maximum of 40,000 total articles, excluding translations. This limit includes articles in all states, except archived.

**To create an article and add content**

1. In your [help center](https://support.zendesk.com/hc/en-us/articles/9041943683354#topic_dzz_4wn_s2c) or [Knowledge admin](https://support.zendesk.com/hc/en-us/articles/9041943683354#topic_b5q_nwn_s2c), click **Add** in the top menu bar, then select **Article**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/guide-add-contentblock.png)
2. Enter your content.
   - Use the article editor's toolbar for formatting options or to add links, images, or tables.

     ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/guide-new-art-editor-toolbar-ga.png)

     For information, see:
     - [Help center article editor toolbar reference](https://support.zendesk.com/hc/en-us/articles/4408839186586)
     - [Inserting and editing links in articles](https://support.zendesk.com/hc/en-us/articles/4408822378266)
     - [Inserting images in articles and content blocks](https://support.zendesk.com/hc/en-us/articles/4408824620698)
     - [Inserting videos and embedded files in articles and content blocks](https://support.zendesk.com/hc/en-us/articles/4408829384986)
     - [Adding and formatting tables in help center articles](https://support.zendesk.com/hc/en-us/articles/4408829307418)
     - [Adding article summaries to knowledge base articles](https://support.zendesk.com/hc/en-us/articles/9195508027034)
   - [Edit the HTML source](https://support.zendesk.com/hc/en-us/articles/4408824584602) by clicking the **HTML** button at the end of the editor's toolbar.

     Note: To keep your help center secure and provide the best experience for your end users, Zendesk limits the HTML you can use in articles.
     For information, see [Allowing unsafe HTML in articles](https://support.zendesk.com/hc/en-us/articles/4408824584602#topic_ihw_rcy_kxb).
   - Format article and content block text using markdown. See [Formatting text with Markdown](https://support.zendesk.com/hc/en-us/articles/4408846544922) for a list of supported Markdown commands.
3. Continue to [Configure the article settings](#topic_bpt_tdq_cy) to define management permissions and placement prior to saving and publishing.

## Configure article settings

Before you can save and publish, you must configure basic management permissions and article placement. You can also configure other settings that add labels, content tags, or comment fields to your article.

**To configure article settings**

1. In the article settings panel, review and configure the **Management permissions**:
   - Under **Management permissions**, click the drop-down arrow, then select management permissions to determine which agents have editing and publishing rights for this article.

     - **Administrators** enables only Knowledge admins to edit and publish the article. This option is selected by default on new articles.
     - **Agents and admins** enables all agents and admins to edit and publish the article.
     - **Editors and Publishers** (Enterprise plans only), enables all agents and admins to edit this article, but only admins can publish the article. This option appears only if it's been activated.
     - **Custom management permission** enables specific user segments to edit and publish the article.

     Depending on your account, you might also see an agents and managers option.

     Knowledge admins can apply any management permissions. Agents with management permissions can apply only the management permissions they belong to. Agents who do not have management permissions on any article will not see this option, and the management permissions will default to admins.
   - Under **Owner**, verify or select a new owner for the article.
2. Review and configure the **Placement settings**:
   - You can place the article in up to 10 different sections across all brands in your help center. See [Creating article placements](https://support.zendesk.com/hc/en-us/articles/9354869473178#topic_yng_kdm_pcc).
   - Under **Author**, verify or select a new author for the article.
   - Under **Viewing permissions**, select one of the following options to determine which users can view this article:
     - **Visible to everyone** includes anyone who visits your help center and does not require sign in.
     - **Only visible to selected user segments** includes up to 10 user selected segments from any of the following:
       - **Signed-in users** includes internal and external users who create an account and sign in to your help center.
       - **Agents and admins** includes team members only, so that you can create content that is internal-only.

         Note: Light agents are included in this segment. For a list of light agent permissions, see [Understanding and setting light agent permissions](https://support.zendesk.com/hc/en-us/articles/4408846501402-Understanding-and-setting-light-agent-permissions-).
       - **Custom user segment** enables you to restrict viewing access to specific users based on tags, organizations, or groups by applying user segments. See [Creating user segments to restrict access](https://support.zendesk.com/hc/en-us/articles/4408837707290).
   - (Not available on Suite Team) Under **Content tags**, start typing the content tag you want to add, then select **Add as new tag** or select the matching content tag, if it exists. See [Adding content tags to articles.](https://support.zendesk.com/hc/en-us/articles/5003635888410)
   - (Not available on Suite Team) Under **Labels**, add any labels you want.

     As you start typing, a list of existing labels appears for you to choose from, or you can add a new keyword by selecting **Add as a new label** or by typing a word and pressing **Enter**.

     ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/add_new_label.png)

     For more information about using labels and best practices, see [Using labels on help center articles](https://support.zendesk.com/hc/en-us/articles/4408835056154).

     You can add labels to the default language article only and not to translations of the article.
     You can add labels in multiple languages to the default article.
   - Choose any of the following options:
     - To close the article for comments, deselect **Turn on comments**.
     - To [promote the article in its section](https://support.zendesk.com/hc/en-us/articles/4408822265754), select **Promote article**.
     - To add an attachment, click **Manage attachment** in the Attachments section at the bottom of the pane. See [Attaching media to articles](https://support.zendesk.com/hc/en-us/articles/6037983662234).

       The file size limit is 20 MB. You can remove an attachment by clicking the **x** next to it.
   - (Enterprise plans only) Under **Template**, if you have [multiple article templates](https://support.zendesk.com/hc/en-us/articles/4408828878106) in your live theme, click the drop-down, then select a template.

     You might have to scroll down to see this option.
     If you do not select an alternate template, the default article template will be applied.

     ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/article_select_template.png)
   - Under **Attached media**, click **Manage attached media** to attach a downloadable file to the article. See [Attaching media to articles](https://support.zendesk.com/hc/en-us/articles/6037983662234).
3. Continue to [save and publish your article](#topic_ngr_25x_cfc).

## Save and publish articles

When you are finished working on your article, you can save, preview, or publish your article to add it to your help center.

**To save and publish articles**

Do one of the following:

- Click **Save** to save your new article as a draft or work in progress to publish later.
- Click **Preview** to [view the article in your help center](https://support.zendesk.com/hc/en-us/articles/8290688602906).
- When you're ready to publish your article, click the drop-down arrow on the **Save** button, then select **Publish**.