# Manage your Amazon EC2 resources

Source: apps/user-manuals/aws/ec2-ug.pdf

---

# Manage your Amazon EC2 resources A resource is an entity that you can work with. Amazon EC2 creates resources as you use the features of the service. For example, Amazon EC2 resources include images, instances, fleets, key pairs, and security groups. All Amazon EC2 resource types include attributes that describe the resources. For example, names, descriptions, resource identifiers, and Amazon Resource Names (ARN).
Amazon EC2 resources are specific to the AWS Region or zone in which they reside. For example, an Amazon Machine Image (AMI) is specific to an AWS Region, but the instance that you launch from an AMI is specific to the zone in which you launch it. You can specify an Amazon EC2 resource in a permissions policy using its ARN.
Your AWS account has default quotas for Amazon EC2. These quotas define the maximum number of resources that you can create. For example, there are quotas for the maximum number of vCPUs across your running instances. If launching an instance or starting a stopped instance would cause you to exceed your quota, the operation fails.
You can search for specific resources in your AWS account by Region, using resource IDs or tags.
To search for specific resources or resource types across multiple Regions, use Amazon EC2 Global View.
Contents
- Select a Region for your Amazon EC2 resources
- Find your Amazon EC2 resources
- View resources across Regions using AWS Global View
- Tag your Amazon EC2 resources
- Amazon EC2 service quotas
## Select a Region for your Amazon EC2 resources Amazon EC2 resources are specific to the AWS Region or zone in which they reside. When you create an Amazon EC2 resource, you select the Region for the resource.

Considerations
- Some AWS resources might not be available in all Regions. Ensure that you can create all the AWS resources that you need in a Region before you start creating resources in a Region.
- Some Regions are disabled by default. You must enable these Regions before you can use them.
For more information , see AWS Regions.
To select a Region for a resource using the console
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. From the navigation bar, choose the Regions selector and then choose the Region.
3. The Regions selector includes all resources that are available for use in your AWS account.
Choose the underlined text near the bottom of the list to view the Regions that are not enabled for your account.
To select a Region for a resource using the AWS CLI You can configure the AWS CLI to use a default Region. If you don't specify a Region in the command, the default Region is used. To use a different Region for a specific command, add the following option.

--region us-east-1 To select a Region for a resource using the Tools for PowerShell You can configure the Tools for Windows PowerShell to use a default Region. If you don't specify a Region in a command, the default Region is used. To use a different Region for a specific command, add the following parameter.
-Region us-east-1
## Find your Amazon EC2 resources You can get a list of some types of resources using the Amazon EC2 console. You can get a list of each type of resource using its corresponding command or API action. If you have many resources, you can filter the results to include, or exclude, only the resources that match certain criteria.
Contents
- List and filter resources using the console
- List and filter using the command line
- View resources across Regions using Amazon EC2 Global View
### List and filter resources using the console Contents
- List resources using the console
- Filter resources using the console
- Supported filters
- Save filter sets using the console
- Key features
- Create a filter set
- Modify a filter set
- Delete a filter set

#### List resources using the console You can view the most common Amazon EC2 resource types using the console. To view additional resources, use the command line interface or the API actions.
To list EC2 resources using the console
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. Amazon EC2 resources are specific to an AWS Region. From the navigation bar, choose a Region from the Regions selector.
3. In the navigation pane, choose the option that corresponds to the resource type. For example, to list all your instances, choose Instances.
#### Filter resources using the console To filter a list of resources
1. In the navigation pane, select a resource type (for example, Instances).
2. Choose the search field.
3. Select the filter from the list.

4. Select an operator, for example, = (Equals). Some attributes have more available operators to select. Note that not all screens support selecting an operator.
5. Select a filter value.
6. To edit a selected filter, choose the filter token (blue box), make the required edits, and then choose Apply. Note that not all screens support editing the selected filter.
7. When you are finished, remove the filter.
##### Supported filters The Amazon EC2 console supports two types of filtering.
- API filtering happens on the server side. The filtering is applied on the API call, which reduces the number of resources returned by the server. It allows for quick filtering across large sets of resources, and it can reduce data transfer time and cost between the server and the browser. API filtering supports = (equals) and : (contains) operators, and is always case sensitive.
- Client filtering happens on the client side. It enables you to filter down on data that is already available in the browser (in other words, data that has already been returned by the API). Client filtering works well in conjunction with an API filter to filter down to smaller data sets in the browser. In addition to = (equals) and : (contains) operators, client filtering can also support range operators, such as >= (greater than or equal), and negation (inverse) operators, such as != (does not equal).
The Amazon EC2 console supports the following types of searches:

Search by keyword Searching by keyword is a free text search that lets you search for a value across all of your resources' attributes or tags, without specifying an attribute or tag key to search.
Note All keyword searches use client filtering.
To search by keyword, enter or paste what you're looking for in the search field, and then choose Enter. For example, searching for 123 matches all instances that have 123 in any of their attributes, such as an IP address, instance ID, VPC ID, or AMI ID, or in any of their tags, such as the Name. If your free text search returns unexpected matches, apply additional filters.
Search by attribute Searching by an attribute lets you search a specific attribute across all of your resources.
Note Attribute searches use either API filtering or client filtering, depending on the selected attribute. When performing an attribute search, the attributes are grouped accordingly.
For example, you can search the Instance state attribute for all of your instances to return only instances that are in the stopped state. To do this:
1. In the search field on the Instances screen, start entering Instance state. As you enter the characters, the two types of filters appear for Instance state: API filters and Client filters.
2. To search on the server side, choose Instance state under API filters. To search on the client side, choose Instance state (client) under Client filters.
A list of possible operators for the selected attribute appears.
3. Choose the = (Equals) operator.
A list of possible values for the selected attribute and operator appears.
4. Choose stopped from the list.

Search by tag Searching by a tag lets you filter the resources in the currently displayed table by a tag key or a tag value.
Tag searches use either API filtering or client filtering, depending on the settings in the Preferences window.
To ensure API filtering for tags
1. Open the Preferences window.
2. Clear the Use regular expression matching checkbox. If this checkbox is selected, client filtering is performed.
3. Select the Use case sensitive matching checkbox. If this checkbox is cleared, client filtering is performed.
4. Choose Confirm.
When searching by tag, you can use the following values:
- (empty) – Find all resources with the specified tag key, but there must be no tag value.
- All values – Find all resources with the specified tag key and any tag value.
- Not tagged – Find all resources that do not have the specified tag key.
- The displayed value – Find all resources with the specified tag key and the specified tag value.
You can use the following techniques to enhance or refine your searches:
Inverse search Inverse searches let you search for resources that do not match a specified value. In the Instances and AMIs screens, inverse searches are performed by selecting the != (Does not equal) or !: (Does not contain) operator and then selecting a value. In other screens, inverse searches are performed by prefixing the search keyword with the exclamation mark (!) character.
Note Inverse search is supported with keyword searches and attribute searches on client filters only. It is not supported with attribute searches on API filters.

For example, you can search the Instance state attribute for all of your instances to exclude all instances that are in the terminated state. To do this:
1. In the search field on the Instances screen, start entering Instance state. As you enter the characters, the two types of filters appear for Instance state: API filters and Client filters.
2. Under Client filters, choose Instance state (client). Inverse search is only supported on client filters.
A list of possible operators for the selected attribute appears.
3. Choose != (Does not equal), and then choose terminated.
To filter instances based on an instance state attribute, you can also use the search icons ( ) in the Instance state column. The search icon with a plus sign ( + ) displays all the instances that match that attribute. The search icon with a minus sign ( - ) excludes all instances that match that attribute.
Here is another example of using the inverse search: To list all instances that are not assigned the security group named launch-wizard-1, under Client filters, search by the Security group name attribute, choose !=, and in the search bar, enter launch-wizard-1.
Partial search With partial searches, you can search for partial string values. To perform a partial search, enter only a part of the keyword that you want to search for. On the Instances and AMIs screens, partial searches can only be performed with the : (Contains) operator. On other screens, you can select the client filter attribute and immediately enter only a part of the keyword that you want to search for. For example, on the Instance type screen, to search for all t2.micro, t2.small, and t2.medium instances, search by the Instance Type attribute, and for the keyword, enter t2.
Regular expression search To use regular expression searches, you must select the Use regular expression matching checkbox in the Preferences window.
Regular expressions are useful when you need to match the values in a field with a specific pattern. For example, to search for a value that starts with s, search for ^s. To search for a value that ends with xyz, search for xyz$. Or to search for a value that starts with a number that is followed by one or more characters, search for [0-9]+.*.

Note Regular expression search is supported with keyword searches and attribute searches on client filters only. It is not supported with attribute searches on API filters.
Case-sensitive search To use case-sensitive searches, you must select the Use case sensitive matching checkbox in the Preferences window. The case-sensitive preference only applies to client and tag filters.
Note API filters are always case-sensitive.
Wildcard search Use the * wildcard to match zero or more characters. Use the ? wildcard to match zero or one character. For example, if you have a data set with the values prod, prods, and production, a search of prod* matches all values, whereas prod? matches only prod and prods. To use the literal values, escape them with a backslash (\). For example, "prod\*" would match prod*.
Note Wildcard search is supported with attribute and tag searches on API filters only. It is not supported with keyword searches, and with attribute and tag searches on client filters.
Combining searches In general, multiple filters with the same attribute are automatically joined with OR. For example, searching for Instance State : Running and Instance State : Stopped returns all instances that are either running OR stopped. To join search with AND, search across different attributes. For example, searching for Instance State : Running and Instance Type : c4.large returns only instances that are of type c4.large AND that are in the running state.

#### Save filter sets using the console A saved filter set is a customized group of filters that you can create and reuse to efficiently view your Amazon EC2 resources. This feature helps streamline your workflow, enabling quick access to specific resource views.
Saved filter sets are only supported in the Amazon EC2 console and are currently only available for the Volumes page.
##### Key features
- Customization: Create filter sets tailored to your needs. For example, you can create a filter set to display only your gp3 volumes that were created after a specified date.
- Default filter: Set a default filter set for a page, and the default filters are automatically applied when you navigate to the page. If no default is set, no filters are applied.
- Easy application: Select a saved filter set to apply it instantly. Amazon EC2 then displays the relevant resources, with the active filters indicated by blue tokens.
- Flexibility: Create, modify, and delete filter sets as needed.
##### Create a filter set To create a new filter set
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. In the navigation pane, choose Volumes.
Note Saved filter sets are currently only available for Volumes.
3. In the search field, select filters for your filter set.
4. Choose the arrow next to the Clear filters button, and choose Save new filter set.
5. In the Save filter set window, do the following: a.
For Filter set name, enter a name for the filter set. b.
(Optional) For Filter set description, enter a description for the filter set. c.
(Optional) To set the filter set as the default filter, select the Set as default checkbox.

Note The default filter is automatically applied every time you open the console page. d.
Choose Save.
##### Modify a filter set To modify a filter set
1. From the Saved filter sets list, select the filter to modify.
2. To add a filter, in the search field, select a filter to add to your filter set. To delete a filter in the set, choose the X on the filter token.
3. Choose the arrow next to the Clear filters button, and choose Modify filter set.
4. In the Modify filter set window, do the following: a.
(Optional) To set the filter set as the default filter, select the Set as default checkbox.
Note The default filter is automatically applied every time you open the console page. b.
Choose Modify.
##### Delete a filter set To delete a filter set
1. From the Saved filter sets list, select the filter to delete.
2. Choose the arrow next to the Clear filters button, and choose Delete filter set.
3. In the Delete filter set window, review the filter to confirm this is the filter you want to delete, and then choose Delete.

### List and filter using the command line Each resource type has a corresponding API actions that you use to describe, list, or get resources of that type. The resulting lists of resources can be long, so it can be faster and more useful to filter the results to include only the resources that match specific criteria.
Filtering considerations
- You can specify up to 50 filters and up to 200 values per filter in a single request.
- Filter strings can be up to 255 characters in length.
- You can use wildcards with the filter values. An asterisk (*) matches zero or more characters, and a question mark (?) matches zero or one character.
- Filter values are case sensitive.
- Your search can include the literal values of the wildcard characters; you just need to escape them with a backslash before the character. For example, a value of \*amazon\?\\ searches for the literal string *amazon?\.
- You can't specify a filter value of null. Instead, use client-side filtering. For example, the following command uses the --query option and returns the IDs of the instances that were launched without a key pair. aws ec2 describe-instances \ --query 'Reservations[*].Instances[?!not_null(KeyName)].InstanceId' \ --output text AWS CLI Example: Specify a single filter You can list your Amazon EC2 instances using describe-instances. Without filters, the response contains information for all of your resources. You can use the following option to include only the running instances in the output.
--filters Name=instance-state-name,Values=running To list only the instance IDs for your running instances, add the --query option as follows.
--query "Reservations[*].Instances[*].InstanceId"

Example: Specify multiple filters or filter values If you specify multiple filters or multiple filter values, the resource must match all filters to be included in the output.
You can use the following option to list all instances whose type is either m5.large or m5d.large.
--filters Name=instance-type,Values=m5.large,m5d.large You can use the following option to list all stopped instances whose type is t2.micro.
--filters Name=instance-state-name,Values=stopped Name=instance-type,Values=t2.micro Example: Use wildcards in a filter value You can use the following option with describe-snapshots to return only the snapshots whose description is "database".
--filters Name=description,Values=database The * wildcard matches zero or more characters. You can use the following option to return only the snapshots whose description includes the word database.
--filters Name=description,Values=*database* The ? wildcard matches exactly 1 character. You can use the following option to return only the snapshots whose description is "database" or "database" followed by one character.
--filters Name=description,Values=database?
You can use the following option to return only the snapshots whose description is "database" followed by up to four characters. This excludes descriptions with "database" followed by five or more characters.
--filters Name=description,Values=database????

Example: Filter based on date With the AWS CLI, you can use JMESPath to filter results using expressions. For example, the following describe-snapshots command displays the IDs of all snapshots created by the specified AWS account before the specified date. If you do not specify the owner, the results include all public snapshots. aws ec2 describe-snapshots \ --filters Name=owner-id,Values=123456789012 \ --query "Snapshots[?(StartTime<='2024-03-31')].[SnapshotId]" \ --output text The following example displays the IDs of all snapshots created in the specified date range. aws ec2 describe-snapshots \ --filters Name=owner-id,Values=123456789012 \ --query "Snapshots[?(StartTime>='2024-01-01') && (StartTime<='2024-12-31')].
[SnapshotId]" \ --output text Example: Filter based on tags For examples of how to filter a list of resources according to their tags, see Filter Amazon EC2 resources by tag.
PowerShell Example: Specify a single filter You can list your Amazon EC2 instances using Get-EC2Instance. Without filters, the response contains information for all of your resources. You can use the following parameter to include only the running instances in the output.
-Filter @{Name="instance-state-name"; Values="running"} The following example lists only the instance IDs for your running instances.
(Get-EC2Instance -Filter @{Name="instance-state-name"; Values="stopped"}).Instances
 | Select InstanceId

Example: Specify multiple filters or filter values If you specify multiple filters or multiple filter values, the resource must match all filters to be included in the results.
You can use the following option to list all instances whose type is either m5.large or m5d.large.
-Filter @{Name="instance-type"; Values="m5.large", "m5d.large"} You can use the following option to list all stopped instances whose type is t2.micro.
-Filter @{Name="instance-state-name"; Values="stopped"}, @{Name="instance-type"; Values="t2.micro"}
### View resources across Regions using Amazon EC2 Global View Amazon EC2 Global View enables you to view and search for Amazon EC2 and Amazon VPC resources in a single AWS Region, or across multiple Regions simultaneously in a single console. For more information, see View resources across Regions using AWS Global View.
## View resources across Regions using AWS Global View AWS Global View enables you to view some of your Amazon EC2 and Amazon VPC resources across a single AWS Region, or across multiple Regions in a single console. AWS Global View also provides global search functionality that lets you search for specific resources or specific resource types across multiple Regions simultaneously.
AWS Global View does not let you modify resources in any way.
Supported resources Using AWS Global View, you can view a global summary of the following resources across all of the Regions for which your AWS account is enabled.
- Auto Scaling groups
- Availability Zones
- Capacity Reservations and Capacity Blocks
- DB clusters

- DB instances
- DHCP option set
- Egress-only internet gateways
- Elastic IPs
- Endpoint services
- Instances
- Internet gateways
- Managed prefix lists
- NAT gateways
- Network ACLs
- Network interfaces
- Outposts
- Route tables
- S3 buckets
- Security groups
- Subnets
- Volumes
- VPCs
- VPC endpoints
- VPC peering connections Required permissions A user must have the following permissions to use AWS Global View.
JSON { "Version":"2012-10-17", "Statement": [ { "Effect": "Allow", "Action": [ "autoscaling:DescribeAutoScalingGroups",

      "ec2:DescribeRegions", "ec2:DescribeCapacityReservations", "ec2:DescribeDhcpOptions", "ec2:DescribeEgressOnlyInternetGateways", "ec2:DescribeAddresses", "ec2:DescribeVpcEndpointServices", "ec2:DescribeInstances", "ec2:DescribeInternetGateways", "ec2:DescribePrefixLists", "ec2:DescribeNatGateways", "ec2:DescribeNetworkAcls", "ec2:DescribeNetworkInterfaces", "ec2:DescribeRouteTables", "ec2:DescribeSecurityGroups", "ec2:DescribeSubnets", "ec2:DescribeVolumes", "ec2:DescribeVpcs", "ec2:DescribeVpcEndpoints", "ec2:DescribeVpcPeeringConnections", "ec2:DescribeAvailabilityZones", "ec2:DescribeVpcEndpointServiceConfigurations", "ec2:DescribeManagedPrefixLists", "outposts:ListOutposts", "rds:DescribeDBInstances", "rds:DescribeDBClusters", "s3:ListAllMyBuckets"
  ], "Resource": "*"
  }]
} To use AWS Global View Sign in to the AWS Global View console.
Important You cannot use a private window in Firefox to access AWS Global View.
The console consists of the following:

- Region explorer – This page includes the following sections:
- Summary – Provides a high-level overview of your resources across all Regions.
Expand Show all resource summary indicates the number of Regions for which your AWS account is enabled. The remaining fields indicate the number of resources that you currently have in those Regions. Choose any of the links to view the resources of that type across all Regions. For example, if the link below the Instances label is 29 in 10 Regions, it indicates that you currently have 29 instances across 10 Regions. Choose the link to view a list of all 29 instances.
- Region explorer – Lists all of the AWS Regions (including those for which your account is not enabled) and provides totals for each resource type for each Region.
Choose a Region name to view all resources of all types for that specific Region. For example, choose Africa (Cape Town) af-south-1 to view all VPCs, subnets, instances, security groups, volumes, and Auto Scaling groups in that Region. Alternatively, select a Region and choose View resources for selected Region.
Choose the value for a specific resource type in a specific Region to view only resources of that type in that Region. For example, choose the value for Instances for Africa (Cape Town) af- south-1 to view only the instances in that Region.
- Global search – This page enables you to search for specific resources or specific resource types across a single Region or across multiple Regions. It also enables you to view details for a specific resource.
To search for resources, enter the search criteria in the field preceding the grid. You can search by Region, by resource type, and by the tags assigned to resources.
To view the details for a specific resource, select it in the grid. You can also choose the resource ID of a resource to open it in its respective console. For example, choose an instance ID to open the instance in the Amazon EC2 console, or choose a subnet ID to open the subnet in the Amazon VPC console.
- Regions and Zones – This page allows you to view and manage all available Regions, Availability Zones, Local Zones, and Wavelength Zones.
From the Regions tab, you can view all the AWS Regions. The Status column shows the Regions that are enabled for your AWS account. From this page, you can select a Region to:

- View details of the Region such as the Region code, Geography, and number of each type of Zone.
You can also view the list of Availability Zones, Local Zones, and Wavelength Zones and the list of your resources in the Region.
- Enable or disable the Region.
From each zone tab, you can view the list of that zone type. From the Local Zones tab, you can opt-in to a Local Zone.
Tip If you only use specific Regions or resource types, you can customize AWS Global View to display only those Regions and resource types. To customize the displayed Regions and resource types, in the navigation panel, choose Settings, and then on the Resources and Regions tabs, select the Regions and resource types that you do not want to be displayed in AWS Global View.
## Tag your Amazon EC2 resources To help you manage your instances, images, and other Amazon EC2 resources, you can assign your own metadata to each resource in the form of tags. Tags enable you to categorize your AWS resources in different ways, for example, by purpose, owner, or environment. This is useful when you have many resources of the same type—you can quickly identify a specific resource based on the tags that you've assigned to it. This topic describes tags and shows you how to create them.
Warning Tag keys and their values are returned by many different API calls. Denying access to DescribeTags doesn't automatically deny access to tags returned by other APIs. As a best practice, we recommend that you do not include sensitive data in your tags.
Contents
- Tag basics
- Tag your resources

- Tag restrictions
- Tags and access management
- Tag your resources for billing
- Grant permission to tag Amazon EC2 resources during creation
- Add and remove tags for Amazon EC2 resources
- Filter Amazon EC2 resources by tag
- View tags for your EC2 instances using instance metadata
### Tag basics A tag is a label that you assign to an AWS resource. Each tag consists of a key and an optional value, both of which you define.
Tags enable you to categorize your AWS resources in different ways, for example, by purpose, owner, or environment. For example, you could define a set of tags for your account's Amazon EC2 instances that helps you track each instance's owner and stack level.
The following diagram illustrates how tagging works. In this example, you've assigned two tags to each of your instances—one tag with the key Owner and another with the key Stack. Each tag also has an associated value.
We recommend that you devise a set of tag keys that meets your needs for each resource type.
Using a consistent set of tag keys makes it easier for you to manage your resources. You can search

and filter the resources based on the tags you add. For more information about how to implement an effective resource tagging strategy, see the Tagging Best Practices AWS Whitepaper.
Tags don't have any semantic meaning to Amazon EC2 and are interpreted strictly as a string of characters. Also, tags are not automatically assigned to your resources. You can edit tag keys and values, and you can remove tags from a resource at any time. You can set the value of a tag to an empty string, but you can't set the value of a tag to null. If you add a tag that has the same key as an existing tag on that resource, the new value overwrites the old value. If you delete a resource, any tags for the resource are also deleted.
Note After you delete a resource, its tags might remain visible in the console, API, and CLI output for a short period. These tags will be gradually disassociated from the resource and be permanently deleted.
### Tag your resources When you use the Amazon EC2 console, you can apply tags to resources by using the Tags tab on the relevant resource screen, or you can use the Tags Editor in the AWS Resource Groups console.
Some resource screens enable you to specify tags for a resource when you create the resource; for example, a tag with a key of Name and a value that you specify. In most cases, the console applies the tags immediately after the resource is created (rather than during resource creation). The console might organize resources according to the Name tag, but this tag doesn't have any semantic meaning to the Amazon EC2 service.
If you're using the Amazon EC2 API, the AWS CLI, or an AWS SDK, you can use the CreateTags EC2 API action to apply tags to existing resources. Additionally, some resource-creating actions enable you to specify tags for a resource when the resource is created. If tags cannot be applied during resource creation, we roll back the resource creation process. This ensures that resources are either created with tags or not created at all, and that no resources are left untagged at any time.
By tagging resources at the time of creation, you can eliminate the need to run custom tagging scripts after resource creation. For more information about enabling users to tag resources on creation, see Grant permission to tag Amazon EC2 resources during creation.
You can apply tag-based resource-level permissions in your IAM policies to the Amazon EC2 API actions that support tagging on creation to implement granular control over the users and

groups that can tag resources on creation. Your resources are properly secured from creation— tags are applied immediately to your resources, therefore any tag-based resource-level permissions controlling the use of resources are immediately effective. Your resources can be tracked and reported on more accurately. You can enforce the use of tagging on new resources, and control which tag keys and values are set on your resources.
You can also apply resource-level permissions to the CreateTags and DeleteTags Amazon EC2 API actions in your IAM policies to control which tag keys and values are set on your existing resources. For more information, see Example: Tag resources.
For more information about tagging your resources for billing, see Using cost allocation tags in the AWS Billing User Guide.
### Tag restrictions The following basic restrictions apply to tags:
- Maximum number of tags per resource – 50
- For each resource, each tag key must be unique, and each tag key can have only one value.
- Maximum key length – 128 Unicode characters in UTF-8
- Maximum value length – 256 Unicode characters in UTF-8
- Allowed characters
- Although EC2 allows for any character in its tags, other AWS services are more restrictive. The allowed characters across all AWS services are: letters (a-z, A-Z), numbers (0-9), and spaces representable in UTF-8, and the following characters: + - = . _ : / @.
- If you enable instance tags in instance metadata, instance tag keys can only use letters (a-z, A-Z), numbers (0-9), and the following characters: + - = . , _ : @. Instance tag keys can't contain spaces or /, and can't comprise only . (one period), .. (two periods), or _index. For more information, see View tags for your EC2 instances using instance metadata.
- Tag keys and values are case-sensitive.
- The aws: prefix is reserved for AWS use. If a tag has a tag key with this prefix, then you can't edit or delete the tag's key or value. Tags with the aws: prefix do not count against your tags per resource limit.
You can't terminate, stop, or delete a resource based solely on its tags; you must specify the resource identifier. For example, to delete snapshots that you tagged with a tag key called

DeleteMe, you must use the DeleteSnapshots action with the resource identifiers of the snapshots, such as snap-1234567890abcdef0.
When you tag public or shared resources, the tags you assign are available only to your AWS account; no other AWS account will have access to those tags. For tag-based access control to shared resources, each AWS account must assign its own set of tags to control access to the resource.
### Tags and access management If you're using AWS Identity and Access Management (IAM), you can control which users in your AWS account have permission to create, edit, or delete tags. For more information, see Grant permission to tag Amazon EC2 resources during creation.
You can also use resource tags to implement attribute-based control (ABAC). You can create IAM policies that allow operations based on the tags for the resource. For more information, see Control access using attribute-based access.
### Tag your resources for billing You can use tags to organize your AWS bill to reflect your own cost structure. To do this, sign up to get your AWS account bill with tag key values included. For more information about setting up a cost allocation report with tags, see Monthly cost allocation report in the AWS Billing User Guide.
To see the cost of your combined resources, you can organize your billing information based on resources that have the same tag key values. For example, you can tag several resources with a specific application name, and then organize your billing information to see the total cost of that application across several services. For more information, see Using cost allocation tags in the AWS Billing User Guide.
Note If you've just enabled reporting, data for the current month is available for viewing after 24 hours.
Cost allocation tags can indicate which resources are contributing to costs, but deleting or deactivating resources doesn't always reduce costs. For example, snapshot data that is referenced by another snapshot is preserved, even if the snapshot that contains the original data is deleted.

For more information, see Amazon Elastic Block Store volumes and snapshots in the AWS Billing User Guide.
Note Elastic IP addresses that are tagged do not appear on your cost allocation report.
### Grant permission to tag Amazon EC2 resources during creation Some resource-creating Amazon EC2 API actions enable you to specify tags when you create the resource. You can use resource tags to implement attribute-based control (ABAC). For more information, see Tag your resources and Control access using attribute-based access.
To enable users to tag resources on creation, they must have permissions to use the action that creates the resource, such as ec2:RunInstances or ec2:CreateVolume. If tags are specified in the resource-creating action, Amazon performs additional authorization on the ec2:CreateTags action to verify if users have permissions to create tags. Therefore, users must also have explicit permissions to use the ec2:CreateTags action.
In the IAM policy definition for the ec2:CreateTags action, use the Condition element with the ec2:CreateAction condition key to give tagging permissions to the action that creates the resource.
The following example demonstrates a policy that allows users to launch instances and apply any tags to instances and volumes during launch. Users are not permitted to tag any existing resources (they cannot call the ec2:CreateTags action directly).
{ "Statement": [ { "Effect": "Allow", "Action": [ "ec2:RunInstances"
      ], "Resource": "*"
    }, { "Effect": "Allow", "Action": [ "ec2:CreateTags"

      ], "Resource": "arn:aws:ec2:us-east-1:111122223333:*/*", "Condition": { "StringEquals": { "ec2:CreateAction" : "RunInstances"
          } } } ]
} Similarly, the following policy allows users to create volumes and apply any tags to the volumes during volume creation. Users are not permitted to tag any existing resources (they cannot call the ec2:CreateTags action directly).
{ "Statement": [ { "Effect": "Allow", "Action": [ "ec2:CreateVolume"
      ], "Resource": "*"
    }, { "Effect": "Allow", "Action": [ "ec2:CreateTags"
      ], "Resource": "arn:aws:ec2:us-east-1:111122223333:*/*", "Condition": { "StringEquals": { "ec2:CreateAction" : "CreateVolume"
          } } } ]
} The ec2:CreateTags action is only evaluated if tags are applied during the resource-creating action. Therefore, a user that has permissions to create a resource (assuming there are no tagging conditions) does not require permissions to use the ec2:CreateTags action if no tags are

specified in the request. However, if the user attempts to create a resource with tags, the request fails if the user does not have permissions to use the ec2:CreateTags action.
The ec2:CreateTags action is also evaluated if tags are provided in a launch template. For an example policy, see Tags in a launch template.
#### Control access to specific tags You can use additional conditions in the Condition element of your IAM policies to control the tag keys and values that can be applied to resources.
The following condition keys can be used with the examples in the preceding section:
- aws:RequestTag: To indicate that a particular tag key or tag key and value must be present in a request. Other tags can also be specified in the request.
- Use with the StringEquals condition operator to enforce a specific tag key and value combination, for example, to enforce the tag cost-center=cc123:
"StringEquals": { "aws:RequestTag/cost-center": "cc123" }
- Use with the StringLike condition operator to enforce a specific tag key in the request; for example, to enforce the tag key purpose:
"StringLike": { "aws:RequestTag/purpose": "*" }
- aws:TagKeys: To enforce the tag keys that are used in the request.
- Use with the ForAllValues modifier to enforce specific tag keys if they are provided in the request (if tags are specified in the request, only specific tag keys are allowed; no other tags are allowed). For example, the tag keys environment or cost-center are allowed:
"ForAllValues:StringEquals": { "aws:TagKeys": ["environment","cost-center"] }
- Use with the ForAnyValue modifier to enforce the presence of at least one of the specified tag keys in the request. For example, at least one of the tag keys environment or webserver must be present in the request:
"ForAnyValue:StringEquals": { "aws:TagKeys": ["environment","webserver"] }

These condition keys can be applied to resource-creating actions that support tagging, as well as the ec2:CreateTags and ec2:DeleteTags actions. To learn whether an Amazon EC2 API action supports tagging, see Actions, resources, and condition keys for Amazon EC2.
To force users to specify tags when they create a resource, you must use the aws:RequestTag condition key or the aws:TagKeys condition key with the ForAnyValue modifier on the resource- creating action. The ec2:CreateTags action is not evaluated if a user does not specify tags for the resource-creating action.
For conditions, the condition key is not case-sensitive and the condition value is case-sensitive.
Therefore, to enforce the case-sensitivity of a tag key, use the aws:TagKeys condition key, where the tag key is specified as a value in the condition.
For example IAM policies, see Example policies to control access the Amazon EC2 API. For more information, see Conditions with multiple context keys or values in the IAM User Guide.
### Add and remove tags for Amazon EC2 resources When you create an Amazon EC2 resource, such as an Amazon EC2 instance, you can specify the tags to add to the resource. You can also use the Amazon EC2 console to display the tags for a specific Amazon EC2 resource. You can also add or remove tags from an existing Amazon EC2 resource.
You can use the Tag Editor in the AWS Resource Groups console to view, add, or remove tags across of all of your AWS resources across all Regions. You can apply or remove tags from multiple types of resources at the same time. For more information, see the Tagging AWS Resources User Guide.
Tasks
- Add tags using the console
- Add tags using the AWS CLI
- Add tags using PowerShell
- Add tags using CloudFormation
#### Add tags using the console You can add tags to an existing resource directly from the page for a resource.

To add tags to an existing resource
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. From the navigation bar, select the Region where the resource is located.
3. In the navigation pane, select a resource type (for example, Instances).
4. Select the resource from the list.
5. From the Tags tab, choose Manage tags.
6. Choose Add new tag and enter a key and a value for the tag.
7. Choose Save.
#### Add tags using the AWS CLI You can add tags when you create a resource or to an existing resource.
To add a tag on resource creation Use the -tag-specifications option to tag a resource on creation. A tag specification requires the type of resource to be tagged, the tag key, and the tag value. The following example creates a tag and adds it to a tag specification.
--tag-specifications 'ResourceType=instance,Tags=[{Key=stack,Value=production}]'
To add a tag to an existing resource The following examples demonstrate how to add tags to existing resources using the create-tags command.
Example: Add a tag to a resource The following command adds the tag Stack=production to the specified image, or overwrites an existing tag for the AMI where the tag key is stack. If the command succeeds, no output is returned. aws ec2 create-tags \ --resources ami-0abcdef1234567890 \ --tags Key=stack,Value=production

Example: Add tags to multiple resources This example adds (or overwrites) two tags for an AMI and an instance. One of the tags contains just a key (webserver), with no value (we set the value to an empty string). The other tag consists of a key (stack) and value (Production). If the command succeeds, no output is returned. aws ec2 create-tags \ --resources ami-0abcdef1234567890 i-1234567890abcdef0 \ --tags Key=webserver,Value=  Key=stack,Value=Production Example: Add tags with special characters This example adds the tag [Group]=test to an instance. The square brackets ([ and ]) are special characters, which must be escaped.
If you are using Linux or OS X, to escape the special characters, enclose the element with the special character with double quotes ("), and then enclose the entire key and value structure with single quotes ('). aws ec2 create-tags \ --resources i-1234567890abcdef0 \ --tags 'Key="[Group]",Value=test'
If you are using Windows, to escape the special characters, enclose the element that has special characters with double quotes ("), and then precede each double quote character with a backslash (\) as follows: aws ec2 create-tags ^ --resources i-1234567890abcdef0 ^ --tags Key=\"[Group]\",Value=test If you are using Windows PowerShell, to escape the special characters, enclose the value that has special characters with double quotes ("), precede each double quote character with a backslash (\), and then enclose the entire key and value structure with single quotes (') as follows: aws ec2 create-tags `
    --resources i-1234567890abcdef0 `
    --tags 'Key=\"[Group]\",Value=test'

#### Add tags using PowerShell You can add tags when you create a resource or to an existing resource.
To add a tag on resource creation Use the -TagSpecification parameter to tag a resource on creation. A tag specification requires the type of resource to be tagged, the tag key, and the tag value. The following example creates a tag and adds it to a tag specification.
$tag = @{Key="stack"; Value="production"} $tagspec = new-object Amazon.EC2.Model.TagSpecification $tagspec.ResourceType = "instance"
$tagspec.Tags.Add($tag)
The following example specifies this tag in the -TagSpecification parameter.
-TagSpecification $tagspec To add a tag to an existing resource Use the New-EC2Tag cmdlet. You must specify the resource, the tag key, and the tag value.
New-EC2Tag `
    -Resource i-1234567890abcdef0 `
    -Tag @{Key="purpose"; Value="production"}
#### Add tags using CloudFormation With Amazon EC2 resource types, you specify tags using either a Tags or TagSpecifications property.
The following examples add the tag Stack=Production to AWS::EC2::Instance using its Tags property.
Example: Tags in YAML Tags:
  - Key: "Stack"

    Value: "Production"
Example: Tags in JSON "Tags": [ { "Key": "Stack", "Value": "Production"
    } ]
The following examples add the tag Stack=Production to AWS::EC2::LaunchTemplate LaunchTemplateData using its TagSpecifications property.
Example: TagSpecifications in YAML TagSpecifications:
  - ResourceType: "instance"
    Tags:
    - Key: "Stack"
      Value: "Production"
Example: TagSpecifications in JSON "TagSpecifications": [ { "ResourceType": "instance", "Tags": [ { "Key": "Stack", "Value": "Production"
            } ]
    } ]
### Filter Amazon EC2 resources by tag After you add tags, you can filter your Amazon EC2 resources based tag keys and tag values.

Console To filter resources by tag
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. In the navigation pane, select a resource type (for example, Instances).
3. Choose the search field.
4. In the list, under Tags, choose the tag key.
5. Choose the corresponding tag value from the list.
6. When you are finished, remove the filter.
For more information about using filters in the Amazon EC2 console, see Find your Amazon EC2 resources.
AWS CLI To describe resources of a single type with the specified tag key Add the following filter to a describe command to describe the resources of that type with a Stack tag, regardless of the value of the tag.
--filters Name=tag-key,Values=Stack To describe resources of a single type with the specified tag Add the following filter to a describe command to describe the resources of that type with the tag Stack=production.
--filters Name=tag:Stack,Values=production To describe resources of a single type with the specified tag value Add the following filter to a describe command to describe the resources of that type with a tag with the value production, regardless of the tag key.
--filters Name=tag-value,Values=production To describe all EC2 resources with the specified tag

Add the following filter to the describe-tags command to describe all EC2 resources with the tag Stack=test.
--filters Name=key,Values=Stack Name=value,Values=test PowerShell To filter resources of a single type by tag key Add the following filter to a Get cmdlet to describe the resources of that type with a Stack tag, regardless of the value of the tag.
-Filter @{Name="tag-key"; Values="Stack"} To filter resources of a single type by tag Add the following filter to a Get cmdlet to describe the resources of that type with the tag Stack=production.
-Filter @{Name="tag:Stack"; Values="production"} To filter resources of a single type by tag value Add the following filter to a Get cmdlet to describe the resources of that type with a tag with the value production, regardless of the value of the tag key.
-Filter @{Name="tag-value"; Values="production"} To filter all EC2 resources by tag Add the following filter to the Get-EC2Tag cmdlet to describe all EC2 resources with the tag Stack=test.
-Filter @{Name="tag:Stack"; Values="test"}
### View tags for your EC2 instances using instance metadata You can access an instance's tags from the instance metadata. By accessing tags from the instance metadata, you no longer need to use the DescribeInstances or DescribeTags API calls

to retrieve tag information, which reduces your API transactions per second, and lets your tag retrievals scale with the number of instances that you control. Furthermore, local processes that are running on an instance can view the instance's tag information directly from the instance metadata.
By default, tags are not available from the instance metadata; you must explicitly allow access. You can allow access at instance launch, or after launch on a running or stopped instance. You can also allow access to tags by specifying this in a launch template. Instances that are launched by using the template allow access to tags in the instance metadata.
If you add or remove an instance tag, the instance metadata is updated while the instance is running, without needing to stop and then start the instance.
Tasks
- Enable access to tags in instance metadata
- Retrieve tags from instance metadata
- Disable access to tags in instance metadata
#### Enable access to tags in instance metadata By default, there is no access to instance tags in the instance metadata. For each instance, you must explicitly enable access.
Note If you allow access to tags in instance metadata, instance tag keys are subject to specific restrictions. Non-compliance will result in failed launches for new instances or an error for existing instances. The restrictions are:
- Can only include letters (a-z, A-Z), numbers (0-9), and the following characters: + - = . , _ : @.
- Can't contain spaces or /.
- Can't consist only of . (one period), .. (two periods), or _index.
For more information, see Tag restrictions.

Console To enable access to tags in instance metadata during instance launch
1. Follow the procedure to launch an instance.
2. Expand Advanced details, and for Allow tags in metadata, choose Enable.
3. In the Summary panel, review your instance configuration, and then choose Launch instance. For more information, see Launch an EC2 instance using the launch instance wizard in the console.
To enable access to tags in instance metadata after instance launch
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. In the navigation pane, choose Instances.
3. Select your instance, and then choose Actions, Instance settings, Allow tags in instance metadata.
4. To allow access to tags in instance metadata, select the Allow checkbox.
5. Choose Save.
AWS CLI To enable access to tags in instance metadata during instance launch Use the run-instances command and add the following --metadata-options option.
--metadata-options "InstanceMetadataTags=enabled"
To enable access to tags in instance metadata after instance launch Use the following modify-instance-metadata-options command. aws ec2 modify-instance-metadata-options \ --instance-id i-1234567890abcdef0 \ --instance-metadata-tags enabled To verify that access to tags in instance metadata is enabled Use the describe-instances command and check the value of InstanceMetadataTags.

aws ec2 describe-instances \ --instance-ids i-1234567890abcdef0 \ --query "Reservations[*].Instances[].MetadataOptions[].InstanceMetadataTags"

The following is example output. The value is either enabled or disabled.
[ "enabled"
]
PowerShell To enable access to tags in instance metadata during instance launch Use the New-EC2Instance cmdlet and add the following - MetadataOptions_InstanceMetadataTags parameter.
-MetadataOptions_InstanceMetadataTags enabled To enable access to tags in instance metadata after instance launch Use the Edit-EC2InstanceMetadataOption cmdlet.
Edit-EC2InstanceMetadataOption `
    -InstanceId i-1234567890abcdef0 `
    -InstanceMetadataTags enabled To verify that access to tags in instance metadata is enabled Use the Get-EC2Instance cmdlet and check the value of InstanceMetadataTags.
(Get-EC2Instance `
    - InstanceId i-1234567890abcdef0).Instances.MetadataOptions.InstanceMetadataTags.Value The following is example output. The value is either enabled or disabled. enabled

#### Retrieve tags from instance metadata After you allow access to instance tags in the instance metadata, you can access the tags/ instance category from the instance metadata. For more information, see Access instance metadata for an EC2 instance.
IMDSv2 Linux Run the following command from your Linux instance to list all the tag keys for the instance.
TOKEN=`curl -X PUT "http://169.254.169.254/latest/api/token" -H "X-aws-ec2-metadata- token-ttl-seconds: 21600"` \ && curl -H "X-aws-ec2-metadata-token: $TOKEN" http://169.254.169.254/latest/ meta-data/tags/instance This example gets the value of a key obtained in the previous example. The IMDSv2 request uses the stored token that was created using the command in the previous example. The token must not be expired. curl -H "X-aws-ec2-metadata-token: $TOKEN" http://169.254.169.254/latest/meta-data/ tags/instance/tag-key Windows Run the following cmdlet from your Windows instance to list all the tag keys for the instance.
$token = Invoke-RestMethod `
    -Headers @{"X-aws-ec2-metadata-token-ttl-seconds" = "21600"} `
    -Method PUT -Uri http://169.254.169.254/latest/api/token Invoke-RestMethod `
    -Headers @{"X-aws-ec2-metadata-token" = $token} `
    -Method GET -Uri http://169.254.169.254/latest/meta-data/tags/instance This example gets the value of a key obtained in the previous example. The IMDSv2 request uses the stored token that was created using the command in the previous example. The token must not be expired.

Invoke-RestMethod `
    -Headers @{"X-aws-ec2-metadata-token" = $token} `
    -Method GET -Uri http://169.254.169.254/latest/meta-data/tags/instance/tag-key IMDSv1 Linux Run the following command from your Linux instance to list all the tag keys for the instance. curl http://169.254.169.254/latest/meta-data/tags/instance This example gets the value of a key obtained in the previous example. curl http://169.254.169.254/latest/meta-data/tags/instance/tag-key Windows Run the following cmdlet from your Windows instance to list all the tag keys for the instance.
Invoke-RestMethod -Uri http://169.254.169.254/latest/meta-data/tags/instance This example gets the value of a key obtained in the previous example.
Invoke-RestMethod -Uri http://169.254.169.254/latest/meta-data/tags/instance/tag-key
#### Disable access to tags in instance metadata You can disable access to instance tags in the instance metadata. You don't need to disable access to instance tags on instance metadata at launch because it's turned off by default.
Console To disable access to tags in instance metadata
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. In the navigation pane, choose Instances.

3. Select an instance, and then choose Actions, Instance settings, Allow tags in instance metadata.
4. To turn off access to tags in instance metadata, clear the Allow checkbox.
5. Choose Save.
AWS CLI To disable access to tags in instance metadata Use the following modify-instance-metadata-options command. aws ec2 modify-instance-metadata-options \ --instance-id i-1234567890abcdef0 \ --instance-metadata-tags disabled PowerShell To disable access to tags in instance metadata Use the Edit-EC2InstanceMetadataOption cmdlet.
Edit-EC2InstanceMetadataOption `
    -InstanceId i-1234567890abcdef0 `
    -InstanceMetadataTag disabled
## Amazon EC2 service quotas When you create your AWS account, we set default quotas (also referred to as limits) on your AWS resources on a per-Region basis. If you attempt to exceed the quota for a resource, the request fails. For example, there is a maximum number of Amazon EC2 vCPUs that you can provision for On-Demand Instances in a Region. If you attempt to launch an instance in a Region and this request would cause your usage to exceed this quota, the request fails. If this happens, you can reduce your resource usage or request a quota increase.
The Service Quotas console is a central location where you can view and manage your quotas for AWS services, and request a quota increase for many of the resources that you use. Use the quota information that we provide to manage your AWS infrastructure. Plan to request any quota increases in advance of the time that you'll need them.

Related quota documentation
- Amazon EC2 endpoints and quotas
- Amazon EC2 instance type quotas
- Quotas for Amazon EBS
- Amazon VPC quotas
### View your current quotas You can view your quotas for each Region using the Service Quotas console.
To view your current quotas using the Service Quotas console
1. Open the Service Quotas console at https://console.aws.amazon.com/servicequotas/home/ services/ec2/quotas/.
2. From the navigation bar (at the top of the screen), select a Region.
3. On the Manage quotas pane, select a service; for example, Amazon Elastic Compute Cloud (Amazon EC2). Choose View quotas.
4. Use the filter field to filter the list by resource name. For example, enter On-Demand to locate the quotas for On-Demand Instances.
5. To view more information, choose the quota name to open the details page for the quota.
### Request an increase You can request a quota increase for each Region.
To request an increase using the Service Quotas console
1. Open the Service Quotas console at https://console.aws.amazon.com/servicequotas/home/ services/ec2/quotas/.
2. From the navigation bar (at the top of the screen), select a Region.
3. Use the filter field to filter the list by resource name. For example, enter On-Demand to locate the quotas for On-Demand Instances.
4. If the quota is adjustable, choose the quota and then choose Request quota increase.
5. For Change quota value, enter the new quota value.

6. Choose Request.
7. To view any pending or recently resolved requests in the console, choose Dashboard from the navigation pane. For pending requests, choose the status of the request to open the request receipt. The initial status of a request is Pending. After the status changes to Quota requested, you'll see the case number with Support. Choose the case number to open the ticket for your request.
For more information, including how to use the AWS CLI or SDKs to request a quota increase, see Requesting a quota increase in the Service Quotas User Guide.
### Restriction on email sent using port 25 By default, Amazon EC2 allows outbound traffic over port 25 only to private IPv4 addresses. Traffic over port 25 is blocked to public IPv4 addresses and IPv6 addresses.
You can request that this restriction be removed. For more information, see How do I remove the restriction on port 25 from my Amazon EC2 instance or Lambda function?
This restriction does not apply to outbound traffic over port 25 destined for:
- IP addresses in the primary CIDR block of the VPC in which the originating network interface exists.
- IP addresses in the CIDRs defined in RFC 1918, RFC 6598, and  RFC 4193.
