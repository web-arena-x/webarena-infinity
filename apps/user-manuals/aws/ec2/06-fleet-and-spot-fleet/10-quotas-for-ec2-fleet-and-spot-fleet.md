# Quotas for EC2 Fleet and Spot Fleet

Source: apps/user-manuals/aws/ec2-ug.pdf

---

 "LaunchTemplateConfigs": [{ "LaunchTemplateSpecification": { "LaunchTemplateName": "my-launch-template", "Version": "1"
  }, "Overrides": [{ "InstanceRequirements": { "VCpuCount": { "Min": 2 }, "MemoryMiB": { "Min": 4 } } }]
 }]
}
# Quotas for EC2 Fleet and Spot Fleet Your AWS account has default quotas, formerly referred to as limits, for each AWS service. Unless otherwise noted, each quota is Region-specific.
The usual Amazon EC2 quotas apply to instances launched by an EC2 Fleet or a Spot Fleet, such as Spot Instance limits and volume limits.
In addition, your AWS account has the following quotas related to EC2 Fleet and Spot Fleet:
Quota description Quota The number of EC2 Fleets and Spot Fleets per Region of type maintain and request in the active, deleted_running , and cancelled_running  states 1,000 ¹ ² ³ The number of EC2 Fleets of type instant Unlimited The number of Spot capacity pools (unique combination of instance type and subnet) for 300 ¹

Quota description Quota EC2 Fleets and Spot Fleets of type maintain and request The number of Spot capacity pools (unique combination of instance type and subnet) for EC2 Fleets of type instant Unlimited The size of the user data in a launch specifica tion 16 KB ² The target capacity per EC2 Fleet or Spot Fleet 10,000 The target capacity across all EC2 Fleets and Spot Fleets in a Region 100,000 ¹ An EC2 Fleet request or a Spot Fleet request can't span Regions.

An EC2 Fleet request or a Spot Fleet request can't span different subnets from the same Availability Zone.

¹ These quotas apply to both your EC2 Fleets and your Spot Fleets.
² These are hard quotas. You can't request an increase for these quotas.
³ After you delete an EC2 Fleet or cancel a Spot Fleet request, and if you specified that the fleet should not terminate its Spot Instances when you deleted or canceled the request, the fleet request enters the deleted_running (EC2 Fleet) or cancelled_running (Spot Fleet) state and the instances continue to run until they are interrupted or you terminate them manually. If you terminate the instances, the fleet request enters the deleted_terminating (EC2 Fleet) or cancelled_terminating ( Spot Fleet) state and does not count towards this quota. For more information, see Delete an EC2 Fleet request and the instances in the fleet and Cancel (delete) a Spot Fleet request.

## Request a quota increase for target capacity If you need more than the default quota for target capacity, you can request a quota increase.
To request a quota increase for target capacity
1. Open the Support Center Create case form.
2. Choose Service limit increase.
3. For Limit type, choose EC2 Fleet.
4. For Region, choose the AWS Region in which to request the quota increase.
5. For Limit, choose Target Fleet Capacity per Fleet (in units) or Target Fleet Capacity per Region (in units), depending on which quota you want to increase.
6. For New limit value, enter the new quota value.
7. To request an increase for another quota, choose Add another request, and repeat Steps 4–6.
8. For Use case description, enter your reason for requesting a quota increase.
9. Under Contact options, specify your preferred contact language and contact method.
10. Choose Submit.
