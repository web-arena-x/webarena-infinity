# EC2 Capacity Manager

Source: apps/user-manuals/aws/ec2-ug.pdf

---

# EC2 Capacity Manager Amazon EC2 Capacity Manager allows you to monitor, analyze, and manage your capacity usage across On-Demand Instances, Spot Instances, and Capacity Reservations from a single location.
Capacity Manager simplifies capacity tracking through a unified dashboard that aggregates your usage data with hourly refreshes and optimization opportunities.
Designed for large enterprises and multi-account organizations, Capacity Manager eliminates manual data collection from multiple sources. The tool provides deep insights across your AWS Regions. You can drill down into detailed capacity metrics and take immediate actions to optimize your cloud resources.
When you enable AWS Organizations integration, you can view and analyze capacity data across all member accounts in your organization from a single dashboard. Without Organizations integration, Capacity Manager only monitors resources within the individual AWS account where it's enabled.
Note
- You can only enable Capacity Manager in one AWS Region per account.
- All costs displayed in Capacity Manager are estimated costs based on published On- Demand pricing. These estimates don't include discounts such as Savings Plans or Reserved Instances. Your actual costs may differ from these estimates.
## Key Features
- Centralized dashboard: View capacity usage across all accounts and regions with new data points refreshed every hour
- Cross-account visibility: Organization-level view for admin accounts
- Data exports: Export capacity data to Amazon S3
- APIs: Programmatic access to capacity metrics and data
- Flexible analysis: Dynamic date selector for exploring capacity usage across different time periods from the past 90 days
- Comprehensive metrics and dimensions: Access to more than 30 metrics across multiple measurement units (vCPUs, instances, estimated costs) with extensive filtering capabilities

including Account ID, Region, Instance Family, Availability Zone, Instance Type, Platform, Tenancy, and reservation-specific dimensions
## Enabling EC2 Capacity Manager Capacity Manager can be enabled at two different levels depending on your requirements. You can enable it for a single AWS account to monitor resources within that account only, or integrate it with AWS Organizations for centralized visibility across all member accounts in your organization.
- Organization-level: View and analyze capacity data across all member accounts in your organization from a single dashboard.
- Account-level: Monitor capacity usage within a single AWS account.
Topics
- Enabling EC2 Capacity Manager with AWS Organizations
- Enabling EC2 Capacity Manager at the account-level
- Registering a delegated administrator
- Using service-linked roles for EC2 Capacity Manager
### Enabling EC2 Capacity Manager with AWS Organizations You can enable EC2 Capacity Manager with AWS Organizations for organization-level visibility and management of your capacity across all member accounts. This integration allows you to monitor, analyze, and manage capacity usage from a centralized location.
The management account is responsible for enabling organization-level access and managing capacity across the organization.
Enabling Capacity Manager with AWS Organizations provides the following benefits:
- Centralized capacity visibility — View capacity usage across all member accounts in your organization from a single dashboard with cross-account and cross-region aggregation.
- Organization-wide optimization — Identify unused Capacity Reservations and optimization opportunities across all accounts in your organization.
- Delegated administrator — Allow specific member accounts to manage Capacity Manager for an organization while maintaining proper access controls.

If you don't enable integration with AWS Organizations, you can only monitor resources in the individual AWS account where you enabled Capacity Manager.
#### Prerequisites
- You must have an AWS Organizations setup with a management account and one or more member accounts. For more information about account types, see Terminology and concepts in the AWS Organizations User Guide.
- The management account must have permissions for the following IAM actions:
- organizations:EnableAwsServiceAccess
- organizations:RegisterDelegatedAdministrator (if using delegated administration)
- iam:CreateServiceLinkedRole
- You must create a service-linked role with the AWSEC2CapacityManagerServiceRolePolicy use case to allow AWS Organization access. For more information, see Creating a service-linked role for Capacity Manager.
#### Enabling Capacity Manager with AWS Organizations Using the management account, enable organization access in Capacity Manager.
Console To enable organization access in Capacity Manager
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. In the navigation pane, choose Capacity Manager.
3. Choose the Settings tab.
4. In the Trusted access section, choose Manage trusted access.
5. In the prompt that appears, select Enable trusted access. Then, choose Save.
AWS CLI To enable organization access in Capacity Manager
1. Create a service-linked role

aws iam create-service-linked-role --aws-service-name ec2.capacitymanager.amazonaws.com

2. Enable AWS Organization access aws organizations enable-aws-service-access --service-principal ec2.capacitymanager.amazonaws.com

3. Enable Capacity Manager with AWS Organization aws ec2 enable-capacity-manager --organizations-access

To update organization access for an existing Capacity Manager, run the following command: aws ec2 update-capacity-manager-organizations-access --organizations-access

#### Verifying Capacity Manager is enabled with your organization Console To verify Capacity Manager is enabled with your organization
1. In the Capacity Manager console, choose Settings.
2. In the Trusted access section, verify that Organization access shows as Enabled.
3. Check that the Organization ID displays your organization's ID.
AWS CLI To verify Capacity Manager is enabled with your organization Run the following command:

aws ec2 get-capacity-manager-attributes

The output should display:
{ "CapacityManagerStatus": "enabled", "OrganizationsAccess": true, "IngestionStatus": "initial-ingestion-pending", "IngestionStatusMessage": "Capacity Manager is collecting historical data from 2025-10-01T00:00:00Z. Data collection is in progress and may take several hours to complete."
}

#### Considerations
- Service-linked role creation: When you enable organization access through the console, Capacity Manager automatically creates the AWSServiceRoleForEC2CapacityManager service- linked role in all m ember accounts. If you enable through the AWS CLI, you must call createServiceLinkedRole manually.
- Data aggregation: After enabling organization access, Capacity Manager will backfill 14 days of historical data from all member accounts. This process typically takes a few minutes to complete.
- Regional limitations: You can only enable Capacity Manager in one Region per organization, but it will aggregate data from all commercial regions.
- Permissions: Member accounts don't need to take any action. Capacity Manager uses the service- linked role to automatically discover resources across all accounts.
### Enabling EC2 Capacity Manager at the account-level Enable Capacity Manager at the account-level to monitor and analyze your EC2 capacity usage within a single AWS account. After you enable it, Capacity Manager collects data about your On- Demand Instances, Spot Instances, and Capacity Reservations to help you identify optimization opportunities and track usage patterns.

#### Enable Capacity Manager at the account-level Console To enable Capacity Manager for your account
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. In the navigation pane, choose Capacity Manager.
3. On the Capacity Manager page, choose Enable in Region.
AWS CLI To enable Capacity Manager for your account Run the following command: aws ec2 enable-capacity-manager

Note
- After you enable Capacity Manager, it collects and aggregates 14 days of historical data.
This process might take a few hours.
- While collecting your historical data, an initial-ingestion-in-progress state will be displayed. During this collection period you might observe gaps in your historical data.
Once data collection is complete, an ingestion-complete state will be displayed.
### Registering a delegated administrator You can register a delegated administrator for Capacity Manager. This allows a member account to manage Capacity Manager for your AWS Organization. Only the management account can register or remove a delegated administrator within your organization.

Note You can't disable Capacity Manager for your organization while there is a registered delegated administrator.
Topics
- Prerequisites
- Register a delegated administrator
- Remove a delegated administrator
#### Prerequisites Your management account must have enabled Capacity Manager with AWS Organizations. For more information, see Enabling EC2 Capacity Manager with AWS Organizations.
#### Register a delegated administrator You can register a delegated administrator using the Amazon EC2 console or the AWS CLI.
Console To register a delegated administrator
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. In the navigation pane, choose Capacity Manager.
3. Choose the Settings tab.
4. In the Delegated administrator section, choose Add.
5. In the prompt that appears, enter the account ID of the organization member you want to add as a delegated administrator.
6. Choose Add delegated administrator.
AWS CLI To register a delegated administrator Run the following command:

aws organizations register-delegated-administrator \ --account-id 123456789012 \ --service-principal ec2.capacitymanager.amazonaws.com

#### Remove a delegated administrator You can remove a delegated administrator using the Amazon EC2 console or the AWS CLI.
Console To remove a delegated administrator
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. In the navigation pane, choose Capacity Manager.
3. Choose the Settings tab.
4. In the Delegated administrator section, choose Manage.
5. In the prompt that appears, choose Remove delegated administrator.
AWS CLI To remove a delegated administrator Run the following command: aws organizations deregister-delegated-administrator \ --account-id 123456789012 \ --service-principal ec2.capacitymanager.amazonaws.com

### Using service-linked roles for EC2 Capacity Manager EC2 Capacity Manager uses AWS Identity and Access Management (IAM) service-linked roles. A service-linked role is a unique type of IAM role that is linked directly to Capacity Manager. Service- linked roles are predefined by Capacity Manager and include all the permissions that the service requires to call other AWS services on your behalf.

A service-linked role makes setting up Capacity Manager easier because you don't have to manually add the necessary permissions. Capacity Manager defines the permissions of its service-linked roles, and unless defined otherwise, only Capacity Manager can assume its roles. The defined permissions include the trust policy and the permissions policy, and that permissions policy cannot be attached to any other IAM entity.
You can delete a service-linked role only after first deleting their related resources. This protects your Capacity Manager resources because you can't inadvertently remove permission to access the resources.
For information about other services that support service-linked roles, see AWS services that work with IAM and look for the services that have Yes in the Service-linked roles column. Choose a Yes with a link to view the service-linked role documentation for that service.
Service-linked role permissions for Capacity Manager Capacity Manager uses the service-linked role named AWSServiceRoleForEC2CapacityManager to allow you to manage capacity resources and integrate with AWS Organizations on your behalf.
The AWSServiceRoleForEC2CapacityManager service-linked role trusts the following services to assume the role:
- ec2.capacitymanager.amazonaws.com The role permissions policy named AWSEC2CapacityManagerServiceRolePolicy allows Capacity Manager to complete the following actions:
- organizations:DescribeOrganization
- organizations:ListAccounts
- organizations:ListChildren
- organizations:ListAWSServiceAccessForOrganization
- organizations:ListDelegatedAdministrators You must configure permissions to allow your users, groups, or roles to create, edit, or delete a service-linked role. For more information, see Service-linked role permissions in the IAM User Guide.

Creating a service-linked role for Capacity Manager You can use the IAM console to create a service-linked role with the AWSEC2CapacityManagerServiceRolePolicy use case. In the AWS CLI or the AWS API, create a service-linked role with the ec2.capacitymanager.amazonaws.com service name. For more information, see Creating a service-linked role in the IAM User Guide. If you delete this service- linked role, you can use this same process to create the role again.
Editing a service-linked role for Capacity Manager Capacity Manager does not allow you to edit the AWSServiceRoleForEC2CapacityManager service- linked role. After you create a service-linked role, you cannot change the name of the role because various entities might reference the role. However, you can edit the description of the role using IAM. For more information, see Editing a service-linked role in the IAM User Guide.
Deleting a service-linked role for Capacity Manager If you no longer need to use a feature or service that requires a service-linked role, we recommend that you delete that role. That way you don't have an unused entity that is not actively monitored or maintained. However, you must clean up the resources for your service-linked role before you can manually delete it.
Note If the Capacity Manager service is using the role when you try to delete the resources, then the deletion might fail. If that happens, wait for a few minutes and try the operation again.
To remove Capacity Manager resources used by the AWSServiceRoleForEC2CapacityManager
1. All delegated administrators must have disabled their Capacity Manager before removing organizations access.
2. You must delete any active data exports before disabling a capacity manager.
To manually delete the service-linked role using IAM Use the IAM console, the AWS CLI, or the AWS API to delete the AWSServiceRoleForEC2CapacityManager service-linked role. For more information, see Deleting a service-linked role in the IAM User Guide.

Supported Regions for Capacity Manager service-linked roles Capacity Manager supports using service-linked roles in all of the Regions where the service is available. For more information, see AWS Regions and endpoints.
Capacity Manager does not support using service-linked roles in every Region where the service is available. You can use the AWSServiceRoleForEC2CapacityManager role in the following Regions.
Region name Region identity Support in Capacity Manager US East (N. Virginia) us-east-1 Yes US East (Ohio) us-east-2 Yes US West (N. California) us-west-1 Yes US West (Oregon) us-west-2 Yes Africa (Cape Town) af-south-1 No Asia Pacific (Hong Kong) ap-east-1 No Asia Pacific (Jakarta) ap-southeast-3 No Asia Pacific (Mumbai) ap-south-1 Yes Asia Pacific (Osaka) ap-northeast-3 Yes Asia Pacific (Seoul) ap-northeast-2 Yes Asia Pacific (Singapore) ap-southeast-1 Yes Asia Pacific (Sydney) ap-southeast-2 Yes Asia Pacific (Tokyo) ap-northeast-1 Yes Canada (Central) ca-central-1 Yes Europe (Frankfurt) eu-central-1 Yes Europe (Ireland) eu-west-1 Yes

Region name Region identity Support in Capacity Manager Europe (London) eu-west-2 Yes Europe (Milan) eu-south-1 No Europe (Paris) eu-west-3 Yes Europe (Stockholm) eu-north-1 Yes Middle East (Bahrain) me-south-1 No Middle East (UAE) me-central-1 No South America (São Paulo) sa-east-1 Yes AWS GovCloud (US-East) us-gov-east-1 No AWS GovCloud (US-West) us-gov-west-1 No
## Organizing your data in Capacity Manager Capacity Manager uses a combination of metrics, data points, dimensions, date ranges, and periods to organize your capacity data. This can help you analyze usage patterns and make informed decisions about your resources.
Metrics and data points A metric is a time-ordered set of data points. For example, if you want to monitor your Spot usage in vCPUs, you would use the SpotTotalUsageHrsVcpu metric.
Every hour, the metric generates a timestamped data point with the Spot usage in vCPU hours. For example, if you used 100 vCPUs during the 10:00 AM hour, Capacity Manager creates a data point with a 10:00 AM timestamp and a value of 100.
For the full list of metrics that Capacity Manager analyzes, see EC2 Capacity Manager metrics.
Dimensions

Dimensions are name-value pairs that help you categorize and identify different aspects of a metric. For example, the name of one dimension in Capacity Manager is AccountID, where the value is the actual account ID. Capacity Manager provides dimensions to segment and group your data such as Instance Family, Reservation ARN, Reservation type, and Tenancy.
For the full list of dimensions, see EC2 Capacity Manager metrics.
Date range and period The date range specifies how much time you want to analyze, from one hour to 90 days. The period determines how Capacity Manager aggregates your data across time and how many data points to return. For example, if your date range is one week and your period is 1 day, Capacity Manager returns 7 data points. Each data point represents one day of aggregated data. The period must be an interval of one hour and divide evenly into the date range.
Topics
- EC2 Capacity Manager metrics
- Grouping and filtering data
### EC2 Capacity Manager metrics Capacity Manager offers a comprehensive selection of metrics for tracking your capacity across different resource types. Metrics can be measured using different units depending on your analysis needs.
The metric names in Capacity Manager use four different prefixes to categorize the type of capacity being measured:
- Reservation — Capacity Reservations themselves, including total reserved capacity, utilization rates, unused capacity, and reservation counts.
- Reserved — On-Demand Instance usage that is covered by your Capacity Reservations.
- Unreserved — On-Demand Instance usage that runs outside of any Capacity Reservations.
- Spot — Specifically for Spot Instance usage, including runtime and estimated costs. These metrics are separate from reservation-based capacity.
The following table also provides the Dimensions available for each metric. The dimension categories are broken down as follows:

- General capacity dimensions — Account ID, Region, Instance Family, Availability Zone, Instance Type, Platform, and Tenancy
- Capacity Reservation dimensions — Reservation ID (Capacity Reservation ID), Reservation ARN, Unused Financial Owner, Reservation Type (ODCR/Capacity Block), Create timestamp, Start timestamp, End timestamp, State, and Instance match criteria.
- Reserved usage dimensions — Reservation ID (CRID), Reservation ARN, Reservation type Metric Description Dimensions available Units available Reservati onAvgComm ittedSize The average total amount of capacity in an active or scheduled state with a commitment. The size is summed across dimensions and averaged over time.
General capacity and Capacity Reservation dimensions vCPU, Instance Reservati onAvgFutu reSize The average amount of Capacity Reservations that are scheduled to start in the future but have not yet become active during the selected period.
The size is summed across dimensions and averaged over time.
General capacity and Capacity Reservation dimensions vCPU, Instance Reservati onAvgUtil ization The average percentage of your reserved capacity that was used during the selected period.
General capacity and Capacity Reservation dimensions vCPU, Instance Reservati onMaxComm ittedSize The maximum total capacity in an active or scheduled state with a commitment. The size is summed across dimensions and General capacity and Capacity Reservation dimensions vCPU, Instance

Metric Description Dimensions available Units available the maximum value is taken for the period.
Reservati onMaxFutu reSize The maximum amount of Capacity Reservations that are scheduled to start in the future but have not yet become active during the selected period.
The size is summed across dimensions and the maximum value is taken for the period.
General capacity and Capacity Reservation dimensions vCPU, Instance Reservati onMaxSize The maximum size your Capacity Reservation reached at any point during the selected period. Reservation ID Required.
General capacity and Capacity Reservation dimensions vCPU, Instance Reservati onMaxUnus edSize The maximum amount of unused capacity in your Capacity Reservation at any point during the selected period. Reservation ID Required.
General capacity and Capacity Reservation dimensions vCPU, Instance Reservati onMaxUtil ization The maximum utilization percentage your Capacity Reservation achieved at any point during the selected period. Reservation ID Required.
General capacity and Capacity Reservation dimensions


Metric Description Dimensions available Units available Reservati onMinComm ittedSize The minimum total amount of capacity in an active or scheduled state with a commitment. The size is summed across dimensions and minimum value is taken for the period.
General capacity and Capacity Reservation dimensions vCPU, Instance Reservati onMinFutu reSize The minimum amount of Capacity Reservations that are scheduled to start in the future but have not yet become active at any point during the selected period. The size is summed across dimensions and minimum value is taken for the period.
General capacity and Capacity Reservation dimensions vCPU, Instance Reservati onMinSize The minimum size your Capacity Reservation reached at any point during the selected period. Reservation ID Required.
General capacity and Capacity Reservation dimensions vCPU, Instance Reservati onMinUnus edSize The minimum amount of unused capacity in your Capacity Reservation at any point during the selected period. Reservation ID Required.
General capacity and Capacity Reservation dimensions vCPU, Instance

Metric Description Dimensions available Units available Reservati onMinUtil ization The minimum utilization percentage your Capacity Reservation achieved at any point during the selected period. Reservation ID Required.
General capacity and Capacity Reservation dimensions

Reservati onTotalCa pacityHrs Total amount of capacity you have reserved through Capacity Reservations during the selected period.
General capacity and Capacity Reservation dimensions vCPU, Instance Reservati onTotalCount The total number of different Capacity Reservations you had during the selected period.
General capacity and Capacity Reservation dimensions

Reservati onTotalEs timatedCost Estimated cost of the total capacity hours reserved during the selected period.
General capacity and Capacity Reservation dimensions

Reservati onUnusedT otalCapac ityHrs Total amount of reserved capacity that you had but didn't use during the selected period.
General capacity and Capacity Reservation dimensions vCPU, Instance Reservati onUnusedT otalEstim atedCost Estimated cost of the reserved capacity you had but didn't use during the selected period (calculated using On-Demand rates).
General capacity and Capacity Reservation dimensions


Metric Description Dimensions available Units available ReservedT otalEstim atedCost Estimated cost of On-Demand Instance usage that was covered by a Capacity Reservati on during the selected period.
This excludes Spot usage.
General capacity and Reserved usage dimension s

ReservedT otalUsageHrs Total hours of On-Demand Instance usage that were covered by a Capacity Reservati on during the selected period.
This excludes Spot usage.
General capacity and Reserved usage dimension s vCPU, Instance SpotAvgRu nTimeBefo reInterruption Average runtime in hours for instances interrupted in the selected period.
Region, AZ, and Account ID dimensions only Instance SpotInter ruptionRate Percentage of running Spot Instances that were interrupted in the selected period.
Region, AZ, and Account ID dimensions only vCPU, Instance SpotMaxRu nTimeBefo reInterruption Maximum runtime in hours for instances interrupted in the selected period.
Region, AZ, and Account ID dimensions only Instance SpotMinRu nTimeBefo reInterruption Minimum runtime in hours for instances interrupted in the selected period.
Region, AZ, and Account ID dimensions only Instance SpotTotalCount Number of Spot Instances or vCPUs that ran during the selected period.
Region, AZ, and Account ID dimensions only vCPU, Instance

Metric Description Dimensions available Units available SpotTotal EstimatedCost Estimated cost of Spot Instance usage during the selected period (calculated using published Spot rates).
General capacity dimensions

SpotTotal Interruptions Number of interrupted Spot Instances or vCPUs during the selected period.
Region, AZ, and Account ID dimensions only vCPU, Instance SpotTotal UsageHrs Total hours of Spot Instance usage during the selected period.
General capacity dimensions vCPU, Instance Unreserve dTotalEst imatedCost Estimated cost of On-Demand Instance usage that was not covered by a Capacity Reservati on during the selected period.
This excludes Spot usage.
General capacity dimensions

Unreserve dTotalUsageHrs Total hours of On-Demand Instance usage that were not covered by a Capacity Reservati on during the selected period.
This excludes Spot usage.
General capacity dimensions vCPU, Instance Note If you include instances in your units, we recommend including the instance type in your dimensions.

### Grouping and filtering data Capacity Manager aggregates your metrics based on the dimensions and date period you choose. If no dimensions are chosen, Capacity Manager will aggregate the data and return one data point per period in the date range. You can group your data into smaller aggregations by adding dimensions.
- Grouping — Break down your capacity data by dimensions such as Region, Instance Family, or Account ID. You can group your metrics by multiple dimensions to break down your data further.
For example, if you group by Region and Availability Zone, you get a data point for each Region and AZ combination where you have usage.
- Filtering — Show only specific subsets of the dimensions you selected. For example, if you group by instance family, you will get data points for all families where you have usage. However, if you also filter by p5, you see only data points for the p5 instance family.
- Metric units — View results by different units like vCPUs, instances, or estimated costs. For example, after grouping by Region and filtering by a specific instance family, you can view the data in different ways. Switch between total vCPUs used, number of instances running, or estimated costs.
#### How to group and filter data in the console To group and filter data in Capacity Manager
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. In the navigation pane, choose Capacity Manager.
3. Choose the tab for the resource type you want to analyze: Usage, Reservations, or Spot.
4. In the Date filter section, choose a Date range, Time zone, and Interval.
5. In the Dimension filter section, choose a dimension from the Select a dimension dropdown.
6. Select the dimensions you want to group by from the dropdown. Note that the dimension options differ for each resource type. For more information, see EC2 Capacity Manager metrics.
You can add multiple dimensions to create more granular groupings.
7. To filter by the dimension(s) you selected, choose a filter option from the Filter by dimension dropdown.
8. In the Aggregations section, choose a unit to view your results by vCPUs, Instances, or Estimated costs.

## Navigating Capacity Manager in the AWS console The Capacity Manager console is organized into tabs that provide different views of your capacity data:
- Dashboard — Provides a high-level overview of all On-Demand Capacity Reservations, On- Demand and Spot usage, including key metrics and top alerts to help improve your capacity posture.
- Usage — Provides an overview of your instance usage patterns for On-Demand and Spot instances. Analyze coverage by Capacity Reservations and identify optimization opportunities through flexible grouping and filtering.
- Reservations — Provides analysis of Capacity Reservation utilization, management capabilities, and detailed reservation metrics across accounts and Regions.
- Spot — Monitors Spot usage patterns and provides cost analysis for Spot instances across accounts and Regions.
- Data exports — Manages data export configuration to Amazon S3, including scheduling, formatting, and template selection.
- Settings — Provides service configuration options including organization access and regional settings.
Within the Usage and Reservations tabs, Capacity Manager provides a hierarchical navigation structure that allows you to drill down from high-level overviews to detailed resource information.
Understanding this navigation pattern helps you analyze your capacity data efficiently and identify optimization opportunities.
Topics
- Navigation hierarchy
- View breakdown and details for Usage and Reservations
### Navigation hierarchy Capacity Manager uses a three-level navigation structure for Usage and Reservations:
1. Overview page — High-level summary with aggregated metrics.
2. Breakdown page — Detailed analysis with filtering and grouping options

3. Detail pages:
- Usage details — Information about your selected dimension combination, which provides statistics and time-series data to help you understand usage patterns.
- Reservation details — Information about a specific Capacity Reservation including utilization statistics, usage patterns over time, and configuration details.
Note Spot follows a simplified structure with only the overview page.
### View breakdown and details for Usage and Reservations Both Usage and Reservations tabs follow the same three-level navigation structure, allowing you to progress from overview to breakdown to details pages. The processes for accessing breakdown and details pages are similar, with only minor differences in where the navigation links are located within each tab.
To access the resource breakdown pages
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. In the navigation pane, choose Capacity Manager.
3. Choose the tab for the resource type you want to analyze: Usage or Reservations.
4. In the Aggregations section, locate the breakdown link:
- Usage: In the Actions column, choose View breakdown.
Note Depending on your screen size or the number of dimensions you've applied, you might need to scroll horizontally across the page to find the View breakdown link.
- Reservations: In the Reservations column, choose the number (the number is a link) of the reservation you want to view.

To access the details pages
1. On the breakdown page, navigate to the relevant section:
- Usage: The Unique dimension combinations section.
- Reservations: The Reservations section.
2. In the relevant section of your chosen resources, access the details page.
- Usage: In the Actions column, choose View details.
Note Depending on your screen size or the number of dimensions you've applied, you might need to scroll horizontally across the page to find the View details link.
- Reservations: In the Reservation ID column, choose the reservation you want to view.
## Exporting your Capacity Manager data You can export capacity data from EC2 Capacity Manager to Amazon S3 to enable further analysis, create custom reports, or integrate with other AWS services. You can export your data in CSV or Parquet format. In the following sections, you'll find information on how to export your Capacity Manager data.
Note Capacity Manager only allows one data export per AWS account.
Topics
- Setting up an Amazon S3 bucket for Capacity Manager data exports
- Creating a data export for your Capacity Manager data
### Setting up an Amazon S3 bucket for Capacity Manager data exports To receive Capacity Manager data exports, you must have an Amazon S3 bucket in your AWS account to receive and store your export files. When creating a data export in the Capacity Manager console, you can select an existing Amazon S3 bucket that you own or create a new bucket.

In either case, you must apply the required bucket policy to allow Capacity Manager to deliver export files. Editing this policy in the Amazon S3 console or changing the bucket owner after you've created a data export will prevent Capacity Manager from delivering your exports.
To create an Amazon S3 bucket, see Creating an S3 bucket in the Amazon Simple Storage Service User Guide.
The following policy must be applied to your S3 bucket to allow Capacity Manager to deliver data exports:
{ "Version": "2012-10-17", "Statement": [ { "Effect": "Allow", "Principal": { "Service": "ec2.capacitymanager.amazonaws.com"
            }, "Action": [ "s3:PutObject", "s3:GetObject", "s3:ListBucket"
            ], "Resource": [ "arn:aws:s3:::amzn-s3-demo-bucket", "arn:aws:s3:::amzn-s3-demo-bucket/*"
            ], "Condition": { "StringEquals": { "aws:SourceAccount": "111122223333"
                }, "ArnLike": { "aws:SourceArn": "arn:aws:ec2:us-east-1:111122223333:capacity- manager-data-export/*"
                } } } ]
}

This bucket policy helps ensure that Capacity Manager data export files can be delivered securely to your bucket. Specifically:

- Every time a Capacity Manager data export is delivered, AWS first confirms whether the bucket is still owned by the account that set up the export. If the bucket ownership has changed, the export will not be delivered. This helps to ensure the security of Capacity Manager data. This bucket policy allows AWS ("Effect": "Allow") to check which account owns the bucket ("Action": ["s3:ListBucket"]).
- The policy grants the Capacity Manager service ("Service":
"ec2.capacitymanager.amazonaws.com") permission to write export files ("Action":
"s3:PutObject") and read objects ("Action": "s3:GetObject") to copy data to your bucket.
### Creating a data export for your Capacity Manager data To create a data export, you can use the Data Exports page in the Capacity Manager console or the AWS CLI.
#### Prerequisites You must create an Amazon Simple Storage Service (Amazon S3) bucket. You must make sure of the following:
- Your S3 bucket must be in the same AWS Region where you enabled Capacity Manager.
- Your S3 bucket has the required permissions policy for the Capacity Manager service to deliver files.
For more information, see Setting up an Amazon S3 bucket for Capacity Manager data exports.
#### Procedure You can export your Capacity Manager data using the AWS Console or the AWS CLI.
Console To create a data export
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. In the navigation pane, choose Capacity Manager.
3. Choose the Data exports tab.
4. Choose Create data export.
