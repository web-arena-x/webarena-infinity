# Resolve issues with time entry in Practice Manager

Source: https://central.xero.com/s/article/Troubleshooting-time-sheets

---

## Overview

- Understand why you’re having trouble entering time in Practice Manager or why a job or task isn’t displaying.

Unable to enter time

If you're unable to enter time in Practice Manager, check:

- You're [assigned to the job and task](View-staff-allocation.md)
- The [staff task allocation](Set-up-your-practice-settings.md) in your practice settings is set to **Inherit from Job**
- You have the right [user privileges](About-staff-privileges-in-Practice-Manager.md)
- The [timesheet is unlocked](Submit-time-sheets.md) and a timesheet hasn't already been submitted for the period
- There's no [WIP lock date](Set-up-and-work-with-lock-dates.md) set
- The task hasn't been [marked as completed](View-scheduled-tasks-mark-them-as-complete.md)

Job or task isn't listed

If a job isn’t listed, it might be because:

- You're not assigned to the job
- The job start date is in the future

If you're trying to add time but no tasks are shown, it might be because:

- There are no tasks assigned to the job
- The tasks are marked as completed
- The [staff task allocation](Set-up-your-practice-settings.md) is set to **Explicit**and you're not assigned to the task

You can [view or assign staff to jobs and tasks](View-staff-allocation.md) in the Job Manager or in the individual job.

Time entry descriptions are combined

Switching between daily and weekly [time entry modes](Select-time-recording-mode.md) can merge the descriptions of two or more time entries.

To recreate the issue:

1. In daily mode, make two or more time entries for the same task on the same day.
2. Switch to weekly mode and add more time for the same task on a different day.
3. Switch back to daily mode.

Descriptions from the previous daily entries for the day are combined and shown in the first entry, and the description for any other entry on that day is blank. The combined descriptions are only cosmetic and have no effect on time tracking or invoicing.

To fix the problem, you can edit the entries and re-enter the description.

To keep the problem from recurring, choose one of the time entry modes and use it consistently.

Time entry error messages

| Error message | Possible causes |
| --- | --- |
| Oops! No job access | - The job has locked time sheets - You don't have the job manager security privilege, or the job is an adhoc job and you don't have the adhoc time privilege - You're not assigned to the job |
| Oops! No task access | - You have no job access - The task is completed - You're not assigned to the task |
| Oops! No client access | - You have no job access - You don't have the client view security privilege - The client is deleted or archived |
| Hold on! Entry is invoiced and can't change | - The time entry has been invoiced |
| The time record cannot be entered as there is already a submitted timesheet for this period | - The timesheet for this period has been submitted, so it's locked and can't be edited |
| Oops! Time sheet already submitted. Refresh | - You'll only see this error if you're using the timer in quick time entry. The timesheet for this period has been submitted, so it's locked and can't be edited |

Incorrect time due to daylight savings

If your region observes daylight savings, ensure your computer, browser and [practice settings](Set-up-your-practice-settings.md) are updated to reflect the correct time.

Once you’ve updated the time settings, log out of Practice Manager then back in, for the changes to take effect. If your practice still isn’t reflecting the correct time, please [contact our support team](Get-help-while-you-re-using-Practice-Manager.md).

## What's next?

If you're still having trouble, [contact Xero support](Get-help-while-you-re-using-Practice-Manager.md).