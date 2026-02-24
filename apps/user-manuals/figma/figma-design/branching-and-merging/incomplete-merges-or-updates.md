# Incomplete merges or updates

Source: https://help.figma.com/hc/en-us/articles/5691750511383-Incomplete-merges-or-updates

---

Before you Start

Who can use this feature

Available on the [Organization and Enterprise plans](https://help.figma.com/hc/en-us/articles/360040328273).

Anyone with `can edit` access to the main file can merge branches.

This is one step in the branching process. For more information on branching, check out our [Guide to branching](https://help.figma.com/hc/en-us/articles/360063144053).

There are a few steps involved in receiving updates and merging changes. And while uncommon, it’s possible for something to go wrong at one of those steps.

If it does, you may find yourself in a situation where a merge or update didn't complete. We’re working on improvements that will reduce the chances of this happening.

In the meantime, there are a few things you can do if something doesn’t look right after a merge or update.

## Issues

|  |  |
| --- | --- |
| **Problem** | **Solution** |
| Updates from a previous merge show up as conflicts you still need to resolve. This means a previous update from main didn’t complete. | You have two options available:   - Repeat the process by [resolving the conflicts](https://help.figma.com/hc/en-us/articles/5691750511383). - [**Restore the branch ↓**](#restore-branch) to a version before the failed update. You can restore from the **Before update** checkpoint in the branch’s version history. |
| Changes from the branch have been applied to the main file, but the branch hasn’t been closed. | If all your changes have been successfully applied, you can [archive the branch](https://help.figma.com/hc/en-us/articles/5668839659415#archive). |
| Not all changes from the branch are applied to the main file. | [**Restore the main file ↓**](#restore-main) to a version before the failed merge. Then repeat the merge process. |
| You accidentally merged changes from a branch, or want to undo your changes. | You can [**restore a previous version of the main file ↓**](#restore-main). |

### Restore an earlier version of a branch

**Tip!** You can identify a branch by looking out for this structure next to the file name:

`File name`  `Branch name`

1. Open the branch.
2. Click on an empty spot in the canvas to deselect any layers.
3. Click the dropdown next to the file name in the left sidebar.
4. Select **Show version history**.
5. In the right sidebar, select a previous version checkpoint.

   ![Version History panel showing "Before update" checkpoint, indicated by an arrow for selecting a previous file version.](https://help.figma.com/hc/article_attachments/5984991832215)
6. Click  next to the version name and select **Restore this version**.
7. Click **Done** in the toolbar to exit version history.

### Restore an earlier version of the main file

**Caution:** Restoring a previous version applies to everyone with access to the main file. This won’t preserve any other changes made to the main file, including other branch merges.

**Note:** Reversing or undoing a merge won’t restore an archived branch. You’ll need to **restore the branch** before trying to merge the branch again.

1. From the main file, click next to the file name in the left sidebar.
2. Select **Show version history** to open version history in the right sidebar.
3. You can identify a merged branch with the  **Branch merge** icon.
4. Select a version before the merged branch. This could be the “Before merge” checkpoint or any other checkpoint.
5. Click  next to the version and select **Restore this version**.
6. Click **Done** in the toolbar to exit version history.

**[View a file's version history →](https://help.figma.com/hc/en-us/articles/360038006754)**

### Restore an archived branch

1. Click the file/branch name  in the left sidebar.
2. Select **See all branches** to open the branches modal.
3. Select the **Archived** tab to view any archived branches.
4. Click  next to the branch you want to restore and select **Restore**.
5. You can then switch to the **Active** tab, hover over the branch and click **Open**.