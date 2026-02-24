# Issue templates

Templates speed up issue creation, ensure properties are applied when necessary, and facilitate reporting.

![Form template exposed in the issue composer with fields title, repro steps, component](https://webassets.linear.app/images/ornj730p/production/5e1cb2f12b568848b2fabf98420b2a0639854858-1310x1092.png?q=95&auto=format&dpr=2)

## Overview

Templates help you file issues more quickly, and ensure desired issue properties are applied without having to add each one manually. When a template is set as default for a team, each new issue in that team will be created from that template unless manually changed.

## Create standard issue templates

![The settings page for Templates showing a button on how to create a template](https://webassets.linear.app/images/ornj730p/production/7a91829a12a45a33528236cb58a98221b2737795-2414x817.png?q=95&auto=format&dpr=2)

Create new templates by navigating to either [_Workspace settings > Templates_](https://linear.app/settings/templates) or _Team settings > Templates_. Standard templates allow you set the properties of the issue, and provide some context in the description if desired.

Standard templates have the same formatting options of regular issues, with the addition of placeholder text. If you want to prompt the creator to input information in the issue's description, consider using this formatting in your template. 

To format text as a placeholder, select text while editing your template and click the `Aa` icon on the formatting bar. This formatting type is only available when creating or editing templates.

### Workspace Templates

You can create issues with a workspace template on any team in your workspace. Team specific properties like team labels or issue statuses cannot be preset in a workspace level template.

Use workspace templates for issue types that are likely to appear across different teams.

### Team Templates

When a template is scoped to a particular team, it's available only when creating issues in that team. This template type has full access to team properties like team labels and issue statuses.

Team templates are commonly used in our Asks integration, or for types of issues should always be filed to only one team in your Linear workspace.

## Create form templates

Form templates are more structured than standard issue templates and can be used when it's important that certain information is provided at issue creation. They support a set of generic form fields that the submitting user can fill out, as well as fillable fields that correspond to the issue's properties directly. Form templates can be triggered in the Slack integration and in Asks, and also directly in Linear by selecting the template. Any field can be required in a form template. 

### Generic form fields

Field | Function --- | --- Text | Single-line text input Long text | Multi-line text input Dropdown | One value can be selected among options you provide Checkboxes | One or more values can be selected among options you provide Date | Date picker, not tied to any issue property Instructions | Static text that you can use to provide context for how to fill the form, or a particular field in it. Instructions text will be included in the description of the created issue.

### Property form fields

You can also elect to include **customer, a label group, priority, title, and due date**. These fields are treated like generic fields as the user fills the form, but they correspond directly to an issue property rather than being a value input into the created issue's description.

### Default properties

Like standard templates, some properties can be applied by default. These appear to the user when the form template is triggered in Linear, but not elsewhere. These fields are **team, status, priority, assignee, project, label,** and **sub-issue.**

## Use issue templates

Create an issue from a template with the keyboard shortcut `Option/Alt` `C`. Alternatively, access templates directly from the issue creation modal by clicking on _Template_ next to the team name.

If you don't see the template, check that you're creating the issue from the right team. In a sub-issue, only templates that do not themselves contain sub-issues are available.

## Default templates

Default templates are templates that are automatically applied when creating a new issue, given the conditions are met. Configure default templates from a team's template settings page. You can configure defaults differently for members of your team or people who are not part of your team. Form templates are only available as default templates for non-team members.

![Default templates in Linear settings](https://webassets.linear.app/images/ornj730p/production/d6eebc35f66823df066e862e923953b55def74c7-1520x506.png?q=95&auto=format&dpr=2)



## Templates in integrations

Templates created in Linear can also be used in integrations to help save time and keep properties applied consistently where needed. 

Integration | Use-case | Supports form templates --- | --- | --- Intercom & Zendesk | Support agents can select a template for the type of issue being reported, speeding up filing and prefilling needed properties like status Triage and label Bug Slack | When creating issues from a Slack message, select a template from the dropdown menu | ✔ Asks in Slack | Asks is designed to be primarily template driven; users outside your Linear workspace but in your Slack workspace create issues via template enabled in Asks, so their issues end up with the necessary data in Linear | ✔ Asks in Email | Internal request intake via email through Asks Zapier | Consider creating issues via template in the Create Issue step for Linear in Zapier for more complex, multi-application workflows Email | Templates can have unique email addresses; sending an email to that address will create an issue with the properties of the template

Add a template to a supported integration in that integration's settings page in Linear.

## Template based Insights

Issues created by template are filterable by their template, regardless of where they were created. For example, for a template Bug Report, filtering for that template will return issues created with that template in created in Slack with our Slack or Asks integrations, Intercom/Zendesk, and Linear's interface. Questions like "What's our breakdown of bug reports vs. feature requests look like, and how many of them are solved" can be explored with [Insights](https://linear.app/docs/insights):

![Insights showing bugs/feature requests/quick wins/mobile feas, broken down by status](https://webassets.linear.app/images/ornj730p/production/590af179a56bf8e74f60838cbb9ff4a42cb759c9-1242x862.png?q=95&auto=format&dpr=2)

Or, investigate the breakdown of template use by intake source:

![Insights sliced by source and segmented by template](https://webassets.linear.app/images/ornj730p/production/af3a7409ca32ae87de8a695ea54f2f3cfc687295-1247x925.png?q=95&auto=format&dpr=2)

### FAQ

<details>
<summary>Some of my standard templates are now form templates. How do I change them back?</summary>
All templates that used Asks fields have been migrated to form templates, as this feature replaces the former Asks fields functionality.

You can use this option to run a best effort conversion back from a form template to a standard issue template. 

![Convert to standard template option in template overflow menu](https://webassets.linear.app/images/ornj730p/production/4dcf403e825728cfee0cedf0065fff6bee013bb9-1478x284.png?q=95&auto=format&dpr=2)
</details>
