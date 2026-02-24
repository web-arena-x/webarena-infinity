# Get updates from main files

Source: https://help.figma.com/hc/en-us/articles/5665728006423-Get-updates-from-main-files

---

Who can use this feature

Only people with a [paid seat](https://help.figma.com/hc/en-us/articles/360039960434#editor) in an organization or workspace can access the branching feature

Anyone with **can edit** access to a branch can receive and apply updates from the main file

This article covers one step in the branching process:

[Create](https://help.figma.com/hc/en-us/articles/360063144053) → [Share](https://help.figma.com/hc/en-us/articles/5665697002263) → [Update](https://help.figma.com/hc/en-us/articles/5665728006423) → [Request](https://help.figma.com/hc/en-us/articles/5691414603543) → [Review](https://help.figma.com/hc/en-us/articles/5693123873687) → [Merge](https://help.figma.com/hc/en-us/articles/5691189138839) → [Manage](https://help.figma.com/hc/en-us/articles/5668839659415)

If changes are made in the main file, Figma will notify any branches that updates are available. If you have edit access to the branch, you can review and apply those updates to your branch.

It's not possible to choose which changes from the main file you want to apply. You'll need to receive all updates from the main file.

If there are changes to layers you are editing in your branch, you may need to resolve conflicts. You can do this as soon as new changes are available, or when you merge the branch.

**Caution**: If you have an active memory limit banner in your file, you can't review and merge changes. Figma will disable the **Review and merge changes** setting. To get updates from the main file or merge a branch, you need to [reduce your memory usage](https://help.figma.com/hc/en-us/articles/360040528173).

## Review and apply changes

When you accept updates, Figma applies any changes to existing layers, components, or styles in your branch. If new assets were created in the main file, Figma will also add these to your branch. If you've created new assets in your branch, these changes won't have any affect on those assets.

1. Expand the  menu next to the file/branch name in the left sidebar.
2. Select **Update from main...** to preview any updates.
3. View a list of items that have been , , or . You can see a preview of the latest versions, but it's not a before and after of what's changed.
4. Select **Apply changes** to apply all updates to your branch.

## Resolve conflicts

If other collaborators have been continuing to make changes to the main file, you may have conflicting changes. This means one or more of the elements you've made changes to has been updated in the main file.

Figma will let you know if there are any conflicting changes from the **Update from main file** modal.

1. Click **Resolve conflicts** to view any conflicts.
2. View a list of conflicts in the left sidebar.
3. Select an option from the list to review the conflicting changes side-by-side. The version from the main file (source) is on the left and the branch on the right.
4. Select which version you would like to use. Figma will add a badge next to the conflict to show whether you selected the `main` or `branch`.
5. Repeat the process for the remaining conflicts. You'll need to choose a version for every conflict.
6. To quickly select the same option for every conflict, use the **Resolve all** menu. Choose from:
   - **Pick main file** to use the latest changes from the main file
   - **Pick branch** to keep the changes in your branch.
7. When you have a selection for every conflict, click **Next** to move to the next step.
8. You can now preview any other updates from the main file, if there are any. Click **Apply changes** to apply those updates.
9. Figma will apply updates from the main file return you to the branch. You can then continue to edit your branch. If you're receiving updates as part of a [branch merge](#), you can complete the rest of the process.

## Reverse or undo updates

If you want to undo or reverse a branch update, you can restore a previous version of the branch. If you notice something doesn’t look right after a merge or update, read our [Incomplete updates and merges](https://help.figma.com/hc/en-us/articles/5691750511383) article.

1. From the branch, click the  next to the file/branch name in the left sidebar.
2. Select **Show version history** to open version history in the right sidebar.
3. Select a version before the  update from the main file.
4. Right-click the version or click the  and select **Restore this version**.
5. Figma will add two autosave checkpoints to the file's version history. A checkpoint that saves the current version. This is an autosaved version with a timestamp that matches the current time. A checkpoint at the same timestamp for the version you just restored.
6. Click **Done** in the toolbar to exit version history.