# Merge branch into main file

Source: https://help.figma.com/hc/en-us/articles/5691189138839-Merge-branch-into-main-file

---

Who can use this feature

Only people with an [Full seat](https://help.figma.com/hc/en-us/articles/360039960434#editor) in an organization or workspace can access the branching feature

Anyone with can edit access to the main file can merge branches

This article covers one step in the branching process:

[Create](https://help.figma.com/hc/en-us/articles/360063144053) → [Share](https://help.figma.com/hc/en-us/articles/5665697002263) → [Update](https://help.figma.com/hc/en-us/articles/5665728006423) → [Request](https://help.figma.com/hc/en-us/articles/5691414603543) → [Review](https://help.figma.com/hc/en-us/articles/5693123873687) → [Merge](https://help.figma.com/hc/en-us/articles/5691189138839) → [Manage](https://help.figma.com/hc/en-us/articles/5668839659415)

When you want to apply your branch changes to the main file, you can merge the branch. If you have multiple branches and contributors, we recommend coordinating merges to reduce errors or disruption.

If you have view only access to the main file, you will need to [request a branch review](https://help.figma.com/hc/en-us/articles/5691414603543) from someone with edit access.

If you have edit access to the main file, you can go ahead and merge the branch. You can still choose to [request a review](https://help.figma.com/hc/en-us/articles/5691414603543) from a collaborator.

**Caution**: If you have an active memory limit banner in your file, you can't review and merge changes. Figma will disable the **Review and merge changes** setting. To get updates from the main file or merge a branch, you need to [reduce your memory usage](https://help.figma.com/hc/en-us/articles/360040528173).

## Open branch review

1. Open the branch you want to merge.
2. Expand the menu next to the file/branch name.
3. Select **Review and merge changes** to open the branch review modal.
4. You may need to [review updates from the main file](https://help.figma.com/hc/en-us/articles/5665728006423) and **resolve any conflicts**. Click **Resolve conflicts** to start the process.

## Review changes

At the moment, you need to merge all updates from the branch into the main file. There isn't a way to select or merge specific changes.

1. View a list of components, instances, or layers that have been , , or . Figma groups changes by page.
2. Select an object or page to view changes. You can choose to view these **side by side** or as an **overlay**.
3. View the layer, frame, or component name at the top of the modal.
4. Use the buttons to:
   - Zoom out
   - Zoom in
   - `FIT` Zoom to fit
5. Use and arrows at the bottom to move between changes if there is more than one change.
6. Click in the top left to go back to the summary.

### Side by side

**Side by side** view allows you to see both designs at the same time. This is the default display option.

- The left side shows what your object looks like **before** your changes (the main file).
- The right side shows what that object look will look like **after** the merge (the branch).

![Review branch merging](https://help.figma.com/hc/article_attachments/31413613979671)

### Overlay

**Overlay** allows you to compare the before and after by placing them on top of one another.

- The layer underneath is the element **before** the branch is merged (the main file).
- The top on top is the element **after** the merge (the branch).

You can drag the toggle left or right to **adjust the opacity** of the **after** object.

![branch review modal - asset changes overlay view](https://help.figma.com/hc/article_attachments/16988877911831)

## Merge branch

Click **Merge** to apply changes from the branch to the main file. This will also archive the branch.

Figma will show a notification at the bottom of the screen to confirm the merge. There is an option to add a name and description for the merge in the file's version history.

1. Click **Edit merge description**.
2. Add a **Name** for the merge.
3. Give the merge a **Description**.
4. Click **Save** to apply.

You can also come back and add or edit this description in the file's version history.

It’s possible to undo merges and updates by restoring a previous version of the branch or main file. This also applies if you notice something doesn’t look right after a merge or update. **[Incomplete updates and merges →](https://help.figma.com/hc/en-us/articles/5691750511383)**