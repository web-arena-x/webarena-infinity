# Request Self-Serve Workflows Transition

Source: https://v2.support.procore.com/product-manuals/workflows-company/tutorials/request-self-serve-workflows-transition

---

## Things to Consider

- **Required User Permissions:**

  - 'Admin' level permissions on the Company level Workflows tool.

##### Â Important

- **Impact on Workflow History:**

  - **Finished Items** (Approved, Void, or Terminated Status):\* The item's legacy workflow history will be saved.
  - **In-Progress Items** (Not in a finished state):\* Legacy workflow history for in-progress items is NOT saved.\* In-progress items will revert to a **Draft** status, and the legacy workflow will be replaced with the new default workflow.  
     *Note:* If a project does not have a workflow configured or set as the default, the legacy workflow will be stopped where it is at and the item will not have a new workflow applied. The workflow history for these items will be preserved. However, it is important to note that a new workflow cannot be applied to items in this category. To avoid issues caused by this, it is highly recommend that a new default workflow has been configured and set in the tool configuration settings on projects with in-progress legacy workflows.
- Updating Workflows introduces granular permissions, providing enhanced flexibility and control compared to Legacy Workflows. These permissions allow for more precise management of user access and roles. It's important to note that tool admins are automatically granted all granular permissions, including those for Workflows. If this level of default access poses a challenge for your team, we recommend carefully evaluating the upgrade before proceeding.

## Steps

1. Navigate to the Company **Workflows** tool.
2. Click **Configure Settings**  .
3. Click **Submit Request** in the banner at the top of the page.
4. Review the list of projects to which no default workflows have been applied.
5. Read the statement in Procore and if you are ready to proceed, check the box and click **Upgrade**.