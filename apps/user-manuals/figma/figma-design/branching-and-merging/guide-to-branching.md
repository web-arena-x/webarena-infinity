# Guide to branching

Source: https://help.figma.com/hc/en-us/articles/360063144053-Guide-to-branching

---

Who can use this feature

Available on the [Organization and Enterprise plans](https://help.figma.com/hc/en-us/articles/360040328273)

Requires a [Full seat](https://help.figma.com/hc/en-us/articles/360039960434#editor)

Branches are controlled environments that allow you to explore changes to designs, prototypes, and libraries, without editing the original file.

You can submit branches for review and, once approved, merge your changes to apply them to your files.

One popular use case is for maintaining and contributing to style and component libraries. But you can use branching outside of designs systems too!

- Share designs with collaborators and stakeholders
- Prepare designs for developer handoff
- Isolate experiments and usability tests

Explore use cases and best practices in our **[Branching in Figma guide →](https://www.figma.com/best-practices/branching-in-figma/)**

## How branches work

### Create branches

You and your team can create as many branches as you like. To create a branch, you need a Full seat and view or edit access to the main file.

Within the branch, you can safely explore changes and iterations, without disrupting anything or anyone in the main file. You can add, edit, or remove individual layers, components, or entire designs. Figma will keep track of all your changes.

**Caution:** The [**Allow viewers to copy, share, or export from the file** setting](https://help.figma.com/hc/en-us/articles/360040045574) must be enabled for viewers to create branches. If this is disabled, viewers will not see the option to create or edit branches.

1. From the main file, click the next to the file name in left sidebar.
2. Select **Create branch...** from the options.
3. Give the branch a name. Figma will use this to identify the branch in the editor, including in the main file's version history.
4. Figma will create a new branch that is an exact replica of the main file in its current state. In the left sidebar, you will see the `File name``Branch name`.
5. You can now make any changes to your branch without affecting the main file.

### Share branches

Branches are an extension of the main file. Anyone with access to the main file can access branches. Anyone you invite to a branch, gets access to the main file.

You can invite someone to a branch, or share the branch’s unique link.

[**Share branches →**](https://help.figma.com/hc/en-us/articles/5665697002263/)

Tip! You can tell if a file link is for a main file or a branch as all branches will include a `/branch/` variable and a unique string for that branch.

### Get updates from the main file

If you’re working with collaborators, it’s likely designs in the main file will change and evolve.

Figma will let you know if there are any updates available in the main file. You can then review any changes made in the main file and choose to apply them to your branch. This makes sure you're using the latest version of the designs.

It's not possible to pick and choose which changes you want to apply. You can choose to ignore these updates for now and resolve any conflicts when you merge instead.

**[Get updates from main files →](https://help.figma.com/hc/en-us/articles/5665728006423)**

### Request branch reviews

When you're finished making changes in your branch, you have the option to request a review. This allows other people to view your changes before they’re merged.

If you don’t have edit access to the main file, you need to request a review and allow someone who does to merge the branch.

If you have edit access and don’t require a review, you can skip straight to the merge process.

[**Request a branch review →**](https://help.figma.com/hc/en-us/articles/5691414603543/)

### Review and approve branches

Reviewers can preview the branch changes alongside the main file. View what’s been added, edited, or removed by page and compare changes side-by-side, or as an overlay.

Reviews can do any of the following:

- Approve changes
- Approve and merge branch (people with edit access to the main file)
- Suggest further changes

[**Review branch changes →**](https://help.figma.com/hc/en-us/articles/5693123873687/)

### Merge branch to main file

When you're satisfied with your changes, you can **review and merge** your branch with the main file. You'll have the option to resolve any conflicts before applying changes from your branch to the main file.

If someone else has already reviewed and approved the changes, the merge process is a few clicks to complete.

[**Merge branch into main file →**](https://help.figma.com/hc/en-us/articles/5691189138839/)

### View and manage branches

View all branches in the **Branches** modal. You'll see three tabs for **Active** and **Archived** branches, as well as branches you created (**Yours**). The Archived tab includes both merged and archived branches.

If you have can edit access to the main file, you can do the following from the **Branches** modal:

- Open the branch
- Copy a link to the branch
- Merge or archive a branch
- Rename the branch
- Restore an archived branch

[**View and manage branches →**](https://help.figma.com/hc/en-us/articles/5668839659415/)

**Note**: There are a few steps involved in receiving updates and merging changes. And while uncommon, it’s possible for something to go wrong at one of those steps.

There are a few things you can do if something doesn’t look right after a merge or update. [**Incomplete merges or updates →**](https://help.figma.com/hc/en-us/articles/5691750511383)

## Things to note

### Version history

View activity related to branching and merging in the file's version history. Figma will create checkpoints when you **create a branch** and **merge a branch**.

Figma will create an extra checkpoint in the file's version history before merging the file, this preserves a record of any other changes made to the main file before it was merged.

Everything that happened in the branch will be contained in that single checkpoint. You can view the detailed version history of a branch when viewing the branch itself.

- **Branch created**
- **Updated from main**
- **Branch merged**

![Version history panel showing recent branch creation and merge activities, highlighting collaboration and updates.](https://help.figma.com/hc/article_attachments/4410498342935)

### Comments

- Comments from the main file don't appear in any branches
- Comments do not count towards changes when checking for updates from the main file
- Comments from the branch don't end up in the main file when you merge

### Publish libraries

You can only publish to a library from the main file. If you've made changes in a branch that you want to share, you'll need to [merge the branch](#merge) before publishing.

### Publish to the Community

You can only publish to the Community from the main file. If you want to publish the branch, you can duplicate it to create a new file that's separate from the main file.

1. In the left sidebar, click the next to the file name.
2. Select **Duplicate as new file** from the options.
3. Figma will duplicate the branch and add it as a file to the existing location. The name of the file be `Main file name : branch name (Copy)`.

### More branching resources