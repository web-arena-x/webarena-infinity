# Oracle Primavera

Source: https://v2.support.procore.com/product-manuals/oracle-primavera/detailed-data-mapping

---

Table of Contents

## Detailed Data Mapping

##### Â Note

The below fields are supported in Procore. Additional or custom fields added in Primavera will not sync to Procore.

### Gantt View

In Procore, the Gantt chart reads directly from the native schedule file. The chart below shows how each field imports data from Primavera (Primavera Cloud, P6) to Procore. You can find the Gantt view in the Gantt section of the Project Schedule tool. See [View a Gantt Schedule](/product-manuals/schedule-project/tutorials/view-a-gantt-schedule).

| PROCORE Field Name | Imports data from Primavera (Primavera Cloud, P6) to Procore | Primavera (Primavera Cloud, P6) Field Name |
| --- | --- | --- |
| Activity ID |  | Activity ID |
| Task Name |  | Activity Name |
| Baseline Start |  | Baseline Start1 |
| Baseline Finish |  | Baseline Finish1 |
| Start |  | Start |
| Finish |  | Finish |
| Duration |  | At Completion Duration |
| % Complete |  | Duration, % Complete, Physical % Complete, Units % Complete2 |
| Predecessors |  | Predecessors |
| Successors |  | Successors |
| WBS3 |  | WBS |
| Resources |  | Resource Assignments4 |
| ID5 |  |  |

*Note*: Blank import fields on the chart indicate the fields do not map to Procore.

1 *Imports vary as described below:*

- *If the user has set the "Project Baseline" in Primavera to be "Current Project" (which is the default value) then we will populate the baseline fields appropriately when reading from XER and PMXML files. No special action required on the part of the user.  
   Note: Using 'Current Project' in Primavera will assume the 'Planned start' and 'Planned Finish' dates as the 'Baseline Start' and 'Baseline Finish' dates.*
- *If the user has selected a specific project under the "Project Baseline" setting in Primavera and an XER file is being used, we will not populate the baseline fields (the data won't be present in the XER file).*
- *Data will only be accurate when 'Budgeted values with planned dates' is selected for the "Earned Value Calculation" setting in P6.*
- *If the user has selected a specific project under the "Project Baseline" setting in Primavera and a PMXML file is being used, and the user has remembered to include the baseline project in the export, the baseline fields will be populated*.
- *Only one Baseline Start and Baseline Finish is supported in Procore.*

2 *Default settings in Primavera allows users to identify which % complete they want to used as the default. Whichever percent setting they choose will be the one pulled into Procore from Primavera.*

3 *Work Breakdown Structure (WBS). WBS tasks use 'Duration % Complete' in Procore.*

4 *Procore determines which resources are associated with a task by reading the resource assignment information from a Primavera schedule.*

5 *ID is originally pulled in for sequential numbering based scheduling software like Microsoft Project. This field does not integrate with Primavera.*

### Schedule TaskÂ Details

The task items details page is a list of all scheduled tasks, as well as their resource, WBS, start and finish date, and percentage complete. You can view the Task Items Details page in the List section of the Project level Schedule tool. See [View a Schedule Task](/product-manuals/schedule-project/tutorials/view-a-schedule-task).

| PROCORE Field Name | Imports data from Primavera (Primavera Cloud, P6) to Procore | Primavera (Primavera Cloud, P6) Field Name |
| --- | --- | --- |
| Activity ID |  | Activity ID |
| Activity Name |  | Activity Name |
| Baseline Start |  | Baseline Start1 |
| Baseline Finish |  | Baseline Finish1 |
| Start |  | Start |
| Finish |  | Finish |
| Duration |  | At Completion Duration |
| % Complete |  | Duration, % Complete, Physical % Complete, Units % Complete2 |
| Predecessors |  | Predecessors |
| Successors |  | Successors |
| Notes |  | Notes |
| WBS3 |  | WBS |
| Resource |  | Resource Assignments4 |
| Actual Start |  | Actual Start |
| Actual Finish |  | Actual Finish |
| Start Variance |  | Start Variance |
| Finish Variance |  | Finish Variance |

1 *If the user has set the "Project Baseline" in Primavera to be "Current Project" (which is the default value) then we will populate the baseline fields appropriately when reading from XER and PMXML files. No special action required on the part of the user.*

- *If the user has selected a specific project under the "Project Baseline" setting in Primavera and an XER file is being used, we will not populate the baseline fields (the data won't be present in the XER file).*
- *If the user has selected a specific project under the "Project Baseline" setting in Primavera and a PMXML file is being used, and the user has remembered to include the baseline project in the export, the baseline fields will be populated*.

2 *Default settings in Primavera allows users to identify which % complete they want to used as the default. Whichever percent setting they choose will be the one pulled into Procore from Primavera.*

3 *Work Breakdown Structure (WBS). WBS tasks use 'Duration % Complete' in Procore.*

4 *Procore determines which resources are associated with a task by reading the resource assignment information from a Primavera schedule.*

### Lookaheads

Lookaheads allows users to create schedule subtasks based off their native schedule file. Lookaheads operates separate from the native schedule and modifications to a Lookahead do NOT impact the native schedule. Lookaheads can be created to range from 1-6 weeks. See [Create a Lookahead Schedule](/product-manuals/schedule-project/tutorials/create-a-lookahead-schedule).

| PROCORE Field Name | Imports data from Primavera (Primavera Cloud, P6) to Procore | Primavera (Primavera Cloud, P6) Field Name |
| --- | --- | --- |
| Activity ID |  | Activity ID |
| WBS |  | WBS1 |
| Task Name |  | Activity Name |
| Start |  | Start |
| Finish |  | Finish |
| Resource |  | Resource Assignments |
| Notes |  | Notes2 |
| Company3 |  |  |
| Assignees3 |  |  |
| ID4 |  |  |

*Note*: Blank import fields on the chart indicate the fields do not map to Procore.

1 *Work Breakdown Structure (WBS)*

2 *The Notes column will map to the Gantt chart column not the Lookaheads note column.*

3 *Company and Assignee will pull from the Project Directory.*

4 *ID is originally pulled in for sequential numbering based scheduling software like Microsoft Project. This field does not integrate with Primavera.*