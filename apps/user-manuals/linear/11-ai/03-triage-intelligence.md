# Triage Intelligence

Route issues by using LLMs to infer issue properties and relationships.

> [!NOTE]
> Available to workspaces on [Business](https://linear.app/pricing) and [Enterprise](https://linear.app/pricing) plans

![Hero image showing the product intelligence pane underneath issue title](https://webassets.linear.app/images/ornj730p/production/02067ce6f9065399e26861ebb5db223bdc0c897e-1494x584.png?q=95&auto=format&dpr=2)

## Overview

Triage Intelligence automates the time consuming assessment and routing steps required when triaging issues. 

When enabled, issues in your workspace are analyzed by agentic models. Every future issue that enters triage is assessed against the rest of your data. This allows Triage Intelligence to proactively surface suggested issue properties and relationships. Accept, decline, or view more information about why a suggestion was made before making a decision. Issue properties suggested include teams, projects, assignees, and labels, and can be configured to auto-apply when suggested.

## Configure

Enable Triage Intelligence by navigating to Settings > AI and toggling the feature on; this will enable the feature for every team. Taking this action requires admin permissions.

In teams where the functionality won't be useful, turn it off in that team's individual triage suggestions settings. Or, if the scope of suggestions should be limited to that team and its sub-teams (don't suggest related issues in other teams, for example), set that behavior in the "Include suggestions from" menu. 

### Issue property suggestions

![Assignee suggestion detail explaining why the suggestion was made](https://webassets.linear.app/images/ornj730p/production/048e6fa94fdd12e50f05a37a4772354b73c5295d-1596x1034.png?q=95&auto=format&dpr=2)

As organizations scale, questions like "who should work on this" or "what labels are usually applied in these scenarios" become harder to answer. Triage Intelligence uses historical trends evaluated against the current issue's content to proactively surface these suggestions. These suggestions appear alongside suggested duplicates and when issues are in Triage.

### Issue property suggestion automation

![Image displays show, auto-apply, and hide options in team settings for product intelligence](https://webassets.linear.app/images/ornj730p/production/e073228328f5928cafd819cfddc2ec4a61674a85-1206x610.png?q=95&auto=format&dpr=2)

In each team where Triage Intelligence is on, customize whether issue property suggestions appear, are hidden, or are auto-applied for different property types. Optionally, filter to specific values to suggest or auto-apply. Sub-team rules are inherited from the parent team by default, but can be overridden in sub-team settings.

### Duplicate and relationship detection

![suggested related issue](https://webassets.linear.app/images/ornj730p/production/ec52900779f7dd8bdaceb6eb19c5564333dce947-1618x1146.png?q=95&auto=format&dpr=2)

When Triage Intelligence determines there is a strong semantic similarity between an issue in Triage and an existing issue, a suggestion appears to accept the relation. Hover over the suggestion to see why it's appearing, and optionally accept it, dismiss it, or follow the reference to the secondary issue to analyze further.

### Refine suggestion behavior

In Triage Intelligence settings at any level (sub-team, parent team, or workspace) you can provide additional guidance to refine suggestion behavior. This is best used reactively (for example, if you're seeing persistent suggestion themes that are incorrect) rather than as part of initial configuration for Triage Intelligence. When additional guidance is set at multiple levels like team and workspace, all are considered but the most local guidance is considered first and weighted most heavily.

### Triggering on issues outside Triage

Triage Intelligence can still be run on issues in other statuses (if you're looking at a backlog issue for instance, and would like to double-check for duplicates).

To do so, use the `Cmd` / `Ctrl` + `K` menu to search for _Find Suggestions._ This will run in the background and enrich the issue with suggestions when available.

### FAQ

<details>
<summary>AI Privacy</summary>
Linear does not utilize your data to train its own AI models. Any data processed to enable Linear’s AI features is shared with our trusted partners (AI subprocessors, see our DPA) exclusively to deliver those AI functionalities to you without permission to train on provided data.

To provide features powered by AI and large language models (LLMs), Linear utilizes voluntary data provided by the user in terms of labeling feature outputs (thumbs up/down) or in other opt-in ways. If you have any questions or concerns, please let us know at security@linear.app.

For further information, please see AI Security FAQ in our [Trust Center](https://trustcenter.linear.app/).
</details>

<details>
<summary>Can I see reasoning about why suggestions are made?</summary>
Yes! Click on the Triage Intelligence window in an issue in Triage while it's processing, or on the suggestion overflow menu once suggestions have been made. 

![Expanded reasoning for Product Intelligence suggestion](https://webassets.linear.app/images/ornj730p/production/1ebe7390a9bb84355abb0e761696b5712df3bcde-1600x1718.png?q=95&auto=format&dpr=2)
</details>

<details>
<summary>I'm on another plan and I still see suggestions. How do these work?</summary>
Quick suggestions in the issue composer and property menus are available in all plans in Linear. These leverage search, so they're faster but much less thorough than Triage Intelligence's suggestions.
</details>

<details>
<summary>How long does it take to generate suggestions?</summary>
Processing new issues in Triage is expected to take 1-4 minutes to generate high-quality suggestions. Because most issues aren’t triaged this quickly, we make a tradeoff here with spending more time to yield better results. We do expect speed improvements over time as models improve.
</details>
