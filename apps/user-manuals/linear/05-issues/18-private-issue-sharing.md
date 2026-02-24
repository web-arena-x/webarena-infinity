# Beta: Private issue sharing

### Beta: Private issue sharing

# Overview

Access to Linear issues is managed at the team level by default—a user in a private team has access to all issues in that team, and a user who is not a member of that team has no visibility.

This works well for the vast majority of cases but there are some workflows that require access to a very limited set of issues. Consider a private Security team sharing a vulnerability with specific developers—or an HR team that needs a manager to fulfill a sensitive task.

To address these and similar scenarios, we've added support for sharing individual issues directly.

### Sharing an issue

Share an issue on a private team through the ⌘/Ctrl + K menu, or by selecting the _Share_ action in an issue's overflow menu. 

When an issue is shared, a banner at the top of the issue indicates whom it's shared with. Any team members can share or stop sharing an issue in that team. 

### Interacting with shared issues

When an issue is shared with you, it appears in _My issues_ under the _Shared_ tab. You can view and update the issue and any of its sub-issues on the same team, but cannot view projects or cycles associated with that issue or share the issue with others.

Users in the private team can filter for all shared issues, or issues shared with a particular user.

### Sub-issues

When you share a parent issue, you’re also sharing its sub-issue tree (the issue’s sub-issues, sub-issues of those sub-issues, etc.) Because of this:

* If a sub-issue is not in the same team as the parent, that parent issue is not sharable.
* You’ll be warned if you attempt to mark another issue as sub-issue to shared issue, to prevent accidentally oversharing data.
