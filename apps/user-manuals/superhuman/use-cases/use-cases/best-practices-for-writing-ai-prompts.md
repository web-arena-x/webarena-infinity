# Best Practices for Writing AI Prompts

Source: https://help.superhuman.com/hc/en-us/articles/39785596906387-Best-Practices-for-Writing-AI-Prompts

---

Here are some helpful tips for creating effective Auto Label prompts to ensure your emails are categorized correctly every time:

## **Structure your Prompts**

**Capitalization** — Superhuman AI will understand that capitalized words are emphasized.

- Example: *NEVER apply this to emails from my team, ONLY to external emails. Do not under any circumstances skip any of these steps/criteria. DO NOT include promotional emails.*

**Simple hierarchy** — Keep your prompts short and sweet.

- Example: *Everything from Google (docs, sheets, meet recordings, drive).*

**Add headers** — Structure your prompts with # large, ## medium, or ### small headers.

- Example:

*## This label should be applied to emails that meet the following criteria:*

*\* From nico@superhuman.com OR lorilyn.mccue@superhuman.com.*

*\* Subject must contain the string “Update”.*

*\* Email should have originally been sent on a Friday.*

*## Examples:*

**Use formatting** — Include hyphens, bullet points, or numbered lists.

- Example:

*a. From: Lorilyn Mccue <lorilyn.mccue@superhuman.com> Date: Friday, December 13 2024 at 10:02 AM PST Subject: Update - Week of 12/16 To: Weekly Updates <updates@superhuman.com> Hey Everyone! Here's the link to the project tracker - feel free to ping me or the team with any questions.*

*b. From: Nico Siciliano <nico@superhuman.com> Date: Friday, March 7 2023 at 11:50 AM PST Subject: GA Update To: Superhuman Mail Team <hello@superhuman.com> Happy Friday, Just an update that AI Compose is now released to all users.*

**Name what to include** — Consider using structured keywords when designing your prompt.

- **Must include** – Specify essential keywords or phrases.
- **May include** – Define optional but relevant terms.

## **Use Precise Language**

**Be explicit** — Ensure the criteria for labeling emails are clearly defined, whether they are concise or more detailed.

- Concise Example: *All emails from nytimes.com*
- Detailed Example: *Emails from the New York Times that mention the Golden Gate Warriors. Do not analyze the content of the email; you are looking for an exact full string match of "Golden Gate Warriors". Do not include related emails that do not contain this complete string. Never include emails that are not sent from nytimes.com*

**Use examples** — Provide an example email that fits the category to refine the logic, and to help constrain what’s included.

- Example: *Emails that contain the exact string "bug". Do not analyze the content of the email; you are looking for an exact string match with these three characters only.* *### Example that should receive this label* *From: Joe Schmoe schmoey@joe.com Date: Monday, March 3 2025 at 1:08 AM PST Subject: Feedback To: Superhuman Mail hello@superhuman.com There seems to be a bug where images can't be copied.* *### Example that should NOT receive this label* *From: Joe Schmoe schmoey@joe.com Date: Monday, March 3 2025 at 1:08 AM PST Subject: Feedback To: Superhuman Mail hello@superhuman.com There seems to be an issue where images can't be copied.*

## **Other Tips for Writing an Effective Prompt:**

**Metadata** — Make sure the prompt can access the data it references.

Here is what the prompt cannot access:

- Attachments (this includes inline images and .ics files).
- Unread, read, starred, and flagged messages.
- Formatting such as bold, italicized, hyperlinks, and quoting.
- Sharing or Reminder status.
- Comments.

**Consider variations** — Think about alternative phrasings that may be clearer.

- Bad example: *Updates from founders I invest with and my co-investors*
- Good example: *Messages from Superhuman Mail or Acme Co. These could come from a variety of senders, such as members of those companies or my fellow investors, but they will always include updates about these companies. My co-investors always use the domain @superinvest.org, and members of these companies use the domain @superhuman.com or acme.co. This should only apply to emails with specific updates about things like revenue, user activity, growth, and not simple promotional emails or requests for introductions.*

**Leverage boolean logic** — Use conditional rules to improve specificity.

- Example: *This label should be applied to all newsletter and promotional emails that contain film-related events in Seattle, WA. Do NOT include events based in Seattle that aren't primarily cinematic events. For example, an email that primarily highlights a movie in Seattle should receive this label, but an email that only features events like live comedy performances, lectures, dance parties, or live musical performances should NOT receive this label.* *If an email features both film and non-film events in Seattle, it's correct to give it this label. Do NOT apply this label to emails that are not also newsletters or promotional in nature.*

**Iterate and refine** — Test your prompt and make adjustments based on misclassifications.

When a label is created, it will be applied to emails from the last 14 days that are in your inbox. When a label is edited, those changes will reflect moving forward, and will *not* backfill. You can always create a new label to see if it’s more effective since emails can receive multiple Auto Labels.