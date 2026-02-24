# Request a branch review

Source: https://help.figma.com/hc/en-us/articles/5691414603543-Request-a-branch-review

---

Who can use this feature

Available on [Organization and Enterprise plans](https://help.figma.com/hc/en-us/articles/360040328273-Choose-a-Figma-Plan)

Anyone with a [paid seat](https://help.figma.com/hc/en-us/articles/360039960434#editor) in an organization or workspace can access the branching feature

Anyone with `can view` or `can edit` access to the main file can request a review

This article covers one step in the branching process:

[Create](https://help.figma.com/hc/en-us/articles/360063144053) → [Share](https://help.figma.com/hc/en-us/articles/5665697002263) → [Update](https://help.figma.com/hc/en-us/articles/5665728006423) → [Request](https://help.figma.com/hc/en-us/articles/5691414603543) → [Review](https://help.figma.com/hc/en-us/articles/5693123873687) → [Merge](https://help.figma.com/hc/en-us/articles/5691189138839) → [Manage](https://help.figma.com/hc/en-us/articles/5668839659415)

When you've finished making changes in your branch, you can request one or more people to review and approve the changes before merging the branch to the main file.

If you don’t have edit access to the main file, you must request a merge from someone who does have edit access. Reviewers can either **Approve** the branch or **Request changes**.

You can request a review from anyone who has access to the main file. This can include members of the team, as well as anyone who has access to the file or project.

A reviewer can then review the changes in your branch and choose whether to approve them or suggest changes.

## Request review

You can request one or more people to review and approve the changes before merging the branch to the main file. This process is not a requirement for merging to the main file.

1. Open the branch you want reviewed.
2. Expand the  menu next to the file/branch name in the toolbar.
3. Click **Review and merge changes...** to open the **Branch review** modal.
4. You can preview any changes you've made as well as select reviewers to approve the changes.  
   - Figma will suggest people with `can edit` access to the main file. Click **Add** next to the suggestion to add them as a reviewer.![Branch review window with options to add reviewers, showing edited color styles and components, ready to merge.](https://help.figma.com/hc/article_attachments/31497541664279)
   - To select another team member, or someone outside of your team, click  .
     - Browse **Other team members** in the list.
     - Use the  **Search** field to find a specific person.![Branch review panel showing color and component changes with reviewer selection for a Figma branch.](https://help.figma.com/hc/article_attachments/31497541668375)
5. Once you've added your reviewer(s), click **Request review**.
6. Use the description field to give reviewers more context for the changes you're making.  
   ![Request review dialog with context input field and "Send to 1 reviewer" button.](https://help.figma.com/hc/article_attachments/31497541671703)
7. Click **Send to reviewers** to submit the request.

Figma will notify reviewers by in-app notification and email. A label will also appear next to your branch name when viewing the Branch review window to show the branch is **In review**.

## View reviewer feedback

Reviewers can choose to approve your branch or suggest further changes. Figma will send you a notification and email (if enabled) to let you know the review outcome.

There are three possible outcomes from a review. Figma represents these outcomes as a status next to the branch name in the Branch review window:

- **In review:**A gray badge shows that a branch review has been requested from another user. No changes have been suggested or approved yet.
- **Changes suggested**: A yellow badge indicates that the reviewer needs you to make some changes before the branch is accepted. You can open the review modal to view the suggestions.  
  Reviewers may have added feedback to individual layers or designs using comments. If there are comments, you'll see a **View comments** banner.
- **Approved:** Your changes have been approved, but the branch has not yet been merged. This usually means the reviewer does not have edit access to the main file or is waiting for other reviewers to add their reviews too before merging.

![Review status indicators for Figma's branching process showing "In review," "Changes suggested," and "Approved" states.](https://help.figma.com/hc/article_attachments/31497570690455)

When ready, you can click **Merge branch** in the bottom right corner of the Branch review window, which will merge the branch into the main file. The branch will be archived and locked after it has been merged.

[Learn more about merging branches.](merge-branch-into-main-file.md)

## Resend request

Resend a review request to any reviewers. You can do this to remind a reviewer of an outstanding review or to submit another request after making changes.

1. Open the branch you want reviewed.
2. Expand the  menu next to the file/branch name in the toolbar.
3. Select **Review and merge changes** to open the **Branch review** modal.
4. Select **Request another review**.
5. Update the description of the review to account for any changes (optional).
6. Click **Send to reviewer**. Figma will notify any reviewers of the request via email and in-app notification.