# Creating templates for Knowledge

Source: https://support.zendesk.com/hc/en-us/articles/4408828223898-Creating-templates-for-Knowledge

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Growth, Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support with** | Guide Professional or Enterprise |

Agents can use [Knowledge in the context panel](https://support.zendesk.com/hc/en-us/articles/4408835161114) to create new articles for your help center, directly from the Support ticket interface. To do so, you need to create one or more Knowledge templates for your agents to use to create new content.

Any article in your help center that contains the label `KCTemplate` is available as a template in Knowledge. You can create as many templates as you need. If you have multiple brands, you must create a Knowledge template in each help center.

Note: Knowledge templates are different from the page templates that you create in a Guide theme. See [Adding multiple article, section, and category templates to your theme](https://support.zendesk.com/hc/en-us/articles/4408828878106).

Here's how it works when an agent creates new content based on a Knowledge template:

- Any new article created using a template is a duplicate of the template and does not overwrite the template article.
- All of the template's fields are duplicated for the new article, with two exceptions:
 the `KCTemplate` label is removed and the author is set to the user creating the new article.
- All of the template's content is duplicated for the new article except for images or attachments, which are not included in any new article.
- The section where the template is published is retained for the new article. Agents can manually change the section, if they want, to any section where they have permission to publish. Knowledge uses ticket requester locale and ticket brand to identify what templates to show.

****To create a template for Knowledge****

1. In [help center](https://support.zendesk.com/hc/en-us/articles/9041943683354#topic_dzz_4wn_s2c) or [Knowledge admin](https://support.zendesk.com/hc/en-us/articles/9041943683354#topic_b5q_nwn_s2c), click **Add** in the top menu bar, then select **Article**.

   Alternatively, you can open an existing article that you want to make a template.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/hc_topmenu_add_options.png)
2. Enter a **Title** for your template.

   Think about the types of templates you plan to create and consider including the type in the title. For example, you might want to create a Q&A template and a How To template, and include that in the template title.
3. Enter the headings and content for your template in the body.

   You might want to include headings specific to the type of template you are creating. For example, a Problem/Solution template might include sections for the problem, the conditions, and the steps for the solution.

   Do not include images or attachments, as they will not be included in any new article created based on this template.
4. Set the **Managed by** and **Visible to** permissions.

   Agents will only be able to use templates where they have management permissions for editing.
5. In **Publish in section** select a section for the template.

   You might want to create a restricted help center section for agents to publish new content, depending on your workflow. Alternatively, you might want agents to create new content as a draft or work in progress.

   New articles based on this template will be created in the section you specify, unless an agent manually changes the section. Agents can create new articles in any section where they have permission. See [Allowing agents to add, edit, and delete articles](https://support.zendesk.com/hc/en-us/articles/4408834435738). The template does not restrict agents to publishing in a specific section.
6. Leave the **Author** as is.

   When an agent creates an article based on this template, the current agent will be set as the author automatically.
7. Add `KCTemplate` in **Label**.

   The label will not persist on any new articles created based on the template.

   Important: You must add this label for your article to be treated as a template in Knowledge.
8. Click **Save**.

   Now your template will be available to agents using Knowledge to create new articles. For information, see [Creating articles in Knowledge](https://support.zendesk.com/hc/en-us/articles/4408835161114).