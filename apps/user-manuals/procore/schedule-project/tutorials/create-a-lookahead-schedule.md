# Create a Lookahead Schedule

Source: https://v2.support.procore.com/product-manuals/schedule-project/tutorials/create-a-lookahead-schedule

---

## Things to Consider

- **Required User Permissions**:

  - *To create a lookahead schedule, you need one of the following:*

    - 'Admin' permissions on the project's Schedule tool.
    - 'Read Only' or 'Standard' level permissions on the Schedule tool with the ['Create Lookaheads' granular permission](/product-manuals/permissions-company/tutorials/grant-granular-permissions-in-a-project-permissions-template) enabled on your permissions template.
- **Additional Information**:

  - When you create a Lookahead in Procore, it will *not* show up on an integrated schedule in Procore (e.g. Microsoft Project, Primavera).
  - Lookaheads populate directly from the master schedule. To see changes made to the master schedule reflected on the lookahead you will need to re-upload the master schedule and create a new Lookahead schedule.
  - You can create multiple lookahead schedules within the same project.   
    See Create Follow-up Lookahead.
- **Prerequisites:**

  - In order to create a Lookahead, you must have Admin permissions and already have a master schedule uploaded in Procore.   
    See [Upload a Project Schedule File](/product-manuals/schedule-project/tutorials/upload-a-project-schedule-file-to-procores-web-application).

## Steps

### Create Your First Lookahead

1. Navigate to the project's Schedule tool.
2. Click the **Lookaheads** tab.
3. Click **+Create Lookahead**.
4. Fill out the following fields:

   - **Start date:** The date you want your lookahead to start.
   - **Duration:** Time frame you want the lookahead to show. You can select a minimum of one week and a maximum of six weeks.  
     *Note:* If a task on your lookahead lasts longer than the duration of the lookahead, it will still be reflected.
5. Click **Create**.

### Create Follow-up Lookahead

1. Navigate to the project's Schedule tool.
2. Click the **Lookaheads** tab.
3. Click **+Create Lookahead**.
4. Do one of the following:

   - To create your follow-up lookahead from a previous lookahead, select **Create from Previous Lookahead.***Note*: Your new lookahead will persist changes to tasks from the previous lookahead, then pull in new tasks from the latest master schedule.
   - To create your follow-up lookahead from a master schedule, select **Create From Master Schedule**.  
     *Note*: Your new lookahead will only pull in any tasks from your master schedule that fall within your defined start date and duration. All changes from the previous lookahead will be ignored.
5. Fill out the following fields:

   - **Start date:** The date you want your lookahead to start.
   - **Duration:** Time frame you want the lookahead to show. You can select a minimum of one week and a maximum of six weeks.  
     *Note:* If the date ranges of your new Lookahead overlaps with the most previous Lookahead, the tasks and subtasks from the most previous Lookahead will carry over to the new Lookahead.
6. Click **Create**.