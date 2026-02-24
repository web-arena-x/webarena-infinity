# Zapier

This integration lets you build custom automations to create or update Linear issues when actions are taken on other apps or using any of Zapier's triggers.

![Linear and Zapier logos](https://webassets.linear.app/images/ornj730p/production/2b0624304661a01aeb711c514ac6d55496dc30d3-2880x1620.png?q=95&auto=format&dpr=2)

## Overview

Zapier is a good solution for building no-code automations with Linear.

### Keyboard

`G` then `S` to go to _Settings > Workspace > Integrations > Zapier_

### Mouse

* Click the Avatar to go to to go to _Settings > Workspace > Integrations > Zapier_

### Command menu

`settings` to go to _Settings > Workspace > Integrations > Zapier_

## Getting Started

Create a Zapier account and then create workflows using our [Zapier integration](https://linear.app/settings/integrations/zapier). This integration is open source and you're welcome to [contribute](https://github.com/linear/linear-zapier/pulls?q=is%3Apr+is%3Aclosed) to it. Zapier has a free trial after which you're charged based on usage.

You can create workflows with apps such as Typeform, Gmail, Intercom, Google Forms, Discord, Airtable, Todoist, Productboard and more.

## Basics

### Build workflows

Our Zapier trigger can be combined with other app triggers or with Zapier's default triggers to build workflows and automations. For instance, you can set up a Zapier workflow that creates a Linear issue whenever a specific Typeform is filled out. 



### Actions

You can take the following actions in Linear in response to a trigger you configure in Zapier:

* Create a new issue
* Update an issue
* Create an issue attachment
* Create a new comment
* Create a new project

### Triggers

If Linear is the start of your Zap, the following actions can be used as triggers for downstream actions in Linear or other applications:

* New issue
* New issue comment
* New document comment
* New project
* New project update
* New project update comment
* Updated issue
* Updated project update

Issues created through Zapier appear as created by “Zapier” and not the user who authorized the application.

### Example workflows

* Create an issue with a bug label when you receive an email message with specific keywords.
* Create a new issue when a tag has been added to an Intercom conversation.
* Let team members or clients outside of Linear create bug reports and feature requests via an online form.
* Create an issue whenever a custom database query returns a new row.
* Create a dealflow pipeline: use a form integration such as Typeform or Google Forms to create a new Linear issue with a custom description.

### Update to latest version

If you're not seeing full functionality, you may be running an old version of the Zapier integration. Update the version you're using in a Zap from the status pane:

![status pane in zapier showing an available update for Linear](https://webassets.linear.app/images/ornj730p/production/875f39f2b76b594ea8e188cfe11e08ebce581df7-1508x942.png?q=95&auto=format&dpr=2)

## FAQ

<details>
<summary>How do I @mention a Linear user in a Zap?</summary>
We support the syntax `@[displayName](userId)` to mention Linear user accounts from Zapier. For example `@[alantest](68bc9696-35d5-442d-ab56-214c8cfefbec)`
</details>
