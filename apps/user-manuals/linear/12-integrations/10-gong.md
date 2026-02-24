# Gong

Automatically create issues from Gong call recordings. 

> [!NOTE]
> Available to workspaces on our [Enterprise](https://linear.app/pricing) plan

![Linear X Gong](https://webassets.linear.app/images/ornj730p/production/940ff2d3f160aeeb393baafb09b22edd78250cb3-2880x1620.png?q=95&auto=format&dpr=2)

## Overview

The Gong integration automatically creates Linear issues from customer call recordings. Each issue includes a drafted title and description, speaker-attributed excerpts pulled directly from the transcript, and a link to the exact moment in the recording where the request or problem was raised.

Once enabled, Linear reviews new customer-facing calls and identifies meaningful product feedback without requiring anyone to listen to the recording. The integration captures what customers are asking for, adds the relevant context from the conversation, and sends the issue into your team’s [Triage](https://linear.app/docs/triage) view for review. This keeps your workflow organized in Linear while leaving calls and transcripts in Gong.

## How it works⁠

Linear periodically checks for new Gong recordings and processes new calls that meet specific criteria for analysis. Only customer-facing conversations are included, so internal or private calls and shorter recordings under 10 minutes are automatically skipped.

The system filters out items that aren’t actionable, like sales-related questions, beta access requests, general inquiries, or internal commentary.

Actionable findings that pass these filters are created as issues in Linear. Each issue includes a concise summary, customer motivation for the request, transcript excerpts with speaker attribution and a link directly to the timestamp in the recording for posterity.

Issues are added to your team’s Triage view, where they can be quickly reviewed, categorized, and moved into your existing backlog.

## Configure

To set up the integration, navigate into your workspace-level _Settings_ > _Integrations_ and search for _Gong_. After enabling the Gong integration, navigate to your Gong settings, enable the recording intake and select the team that should receive Gong-generated issues:  


![Recording intake settings section on, with a destination team chosen](https://webassets.linear.app/images/ornj730p/production/bc401ef7f3a78e59da4ba456851349d01d9834c4-1444x532.heif?q=95&auto=format&dpr=2)

  
Optionally, you can also provide additional guidance to help route issues to the correct teams or templates. This guidance can include examples, team mentions, or internal rules the Linear Agent should follow when interpreting feedback.

## Customer requests

When customer requests are enabled in your workspace, Gong is capable of creating customers just-in-time as their first request is added. If a customer already exists in Linear that matches the customer on the call, that customer will be re-used for association with the new customer request.

## FAQ

<details>
<summary>Do users in Gong need Linear seats?</summary>
No, once an admin configures this integration it will run on all external calls without a seat for itself or other call participants.
</details>
