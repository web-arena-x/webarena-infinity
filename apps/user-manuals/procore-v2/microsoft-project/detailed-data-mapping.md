# Microsoft Project

Source: https://v2.support.procore.com/product-manuals/microsoft-project/detailed-data-mapping

---

Table of Contents

## Detailed Data Mapping

##### Â Note

The below fields are supported in Procore. Additional or custom fields added in Microsoft Project will not sync to Procore.

### Gantt View

In Procore, the Gantt chart reads directly from the Microsoft Project schedule file. The chart below shows how each field maps from Microsoft Project to Procore. You can find the Gantt view in the Gantt section of the Project Schedule tool. See [View a Gantt Schedule](/product-manuals/schedule-project/tutorials/view-a-gantt-schedule).

| **PROCORE Field Name** | **Imports data from Microsoft Project to Procore** | **Microsoft Project Field Name** |
| --- | --- | --- |
| ID |  | ID |
| Task Name |  | Task Name |
| Baseline Start1 |  | Baseline Start1 |
| Baseline Finish1 |  | Baseline Finish1 |
| Start2 |  | Start |
| Finish2 |  | Finish |
| Duration |  | Duration |
| % Complete |  | % Complete, Physical % Complete, Work % Complete 3,4 |
| Predecessors |  | Predecessors |
| Successors |  | Successors |
| Notes |  | Notes |
| WBS (Work Breakdown Structure) |  | WBS (Work Breakdown Structure) |
| Resources |  | Resource Names |

1 *Only one Baseline Start and Baseline Finish is supported in Procore.*

2 *If the Start and Finish dates are blank on the schedule file, the Procore fields will inherit the dates referenced in the Microsoft Project file in the Project Information Section.*

3 *The schedule tool will show the highest values of the three based on these percent complete readings: % complete, physical % percent, or work % complete.*

*4 The schedule tool only displays the change history for % complete and does not display a change history for physical % complete or work % complete.*

### Schedule Task Details

The Schedule Task Details page gives a detailed look at an individual schedule task and provides details such as start and finish variance, as well as requesting a schedule change. See [Request a Schedule Change](/product-manuals/schedule-project/tutorials/request-a-schedule-change) and [View a Schedule Task](/product-manuals/schedule-project/tutorials/view-a-schedule-task).

| **PROCORE Field Name** | **Imports data from Microsoft Project to Procore** | **Microsoft Project Field Name** |
| --- | --- | --- |
| Task ID |  | ID |
| Task Name |  | Task Name |
| Baseline Start1 |  | Baseline Start1 |
| Baseline Finish1 |  | Baseline Finish1 |
| Start |  | Start |
| Finish |  | Finish |
| Duration |  | Duration |
| % Complete |  | % Complete, Physical % Complete, Work % Complete 2,3 |
| WBS (Work Breakdown Structure) |  | WBS (Work Breakdown Structure) |
| Resource |  | Resource Names |
| Actual Start |  | Actual Start |
| Actual Finish |  | Actual Finish |
| Start Variance |  | Start Variance |
| Finish Variance |  | Finish Variance |
| Critical Path3 |  | Critical Path4 |

1 *Only one Baseline Start and Baseline Finish is supported in Procore.*

2 *The schedule tool displays % complete, but does not display physical % complete or work % complete.*

3 *The schedule tool only displays the change history for % complete and does not display a change history for physical % complete or work % complete.*

4 *The critical path fields reads as Yes or No.*

### Lookaheads

Lookaheads allows users to create schedule subtasks based off their integrated Microsoft Project schedule file. Lookaheads operates separate from the integrated schedule file and modifications to a Lookahead do NOT impact the integrated schedule. Lookaheads can be created to range from 1-6 weeks. See [Create a Lookahead Schedule](/product-manuals/schedule-project/tutorials/create-a-lookahead-schedule).

| **PROCORE Field Name** | **Imports data from Microsoft Project to Procore** | **Microsoft Project Field Name** |
| --- | --- | --- |
| ID |  | ID |
| Start |  | Start |
| Finish |  | Finish |
| Notes |  | Notes |
| Resource |  | Resource Names |
| Company |  | Company |
| Assignee |  | Assignee |
| Task Name |  | Task Name |
| Activity ID |  | N/A |

*Note*: Blank import fields indicate the the field does not map to Procore.