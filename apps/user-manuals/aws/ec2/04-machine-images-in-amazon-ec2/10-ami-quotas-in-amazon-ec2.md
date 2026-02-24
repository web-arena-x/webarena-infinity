# AMI quotas in Amazon EC2

Source: apps/user-manuals/aws/ec2-ug.pdf

---

To verify the billing information, find the instance ID in your CUR and check the corresponding value in the lineitem/Operation column. That value should match the value for Usage operation that's associated with the AMI.
For example, the AMI ami-0123456789EXAMPLE has the following billing information:
- Platform details = Red Hat Enterprise Linux
- Usage operation = RunInstances:0010 If you launched an instance using this AMI, you can find the instance ID in your CUR, and check the corresponding value in the lineitem/Operation column. In this example, the value should be RunInstances:0010.
# AMI quotas in Amazon EC2 The following quotas apply to creating and sharing AMIs. The quotas apply per AWS Region.
Quota name Description Default quota per Region AMIs The maximum number of public and private AMIs allowed per Region. These include  available, pending, and disabled AMIs, and AMIs in the Recycle Bin.
50,000 Public AMIs The maximum number of public AMIs, including public AMIs in the Recycle  Bin, allowed per Region.
5 AMI sharing The maximum number of entities (organizations, organizational units (OUs), and accounts) that an AMI can be shared with in a Region.
Note that if you share an AMI 1,000

Quota name Description Default quota per Region with an organization or OU, the number of accounts in the organization or OU does not count towards the quota.
If you exceed your quotas and you want to create or share more AMIs, you can do the following:
- If you exceed your total AMIs or public AMIs quota, consider deregistering unused images.
- If you exceed your public AMIs quota, consider making one or more public AMIs private.
- If you exceed your AMI sharing quota, consider sharing your AMIs with an organization or OU instead of separate accounts.
- Request a quota increase for AMIs.
## Request a quota increase for AMIs If you need more than the default quota for AMIs, you can request a quota increase.
To request a quota increase for AMIs
1. Open the Service Quotas console at https://console.aws.amazon.com/servicequotas/.
2. In the navigation pane, choose AWS services.
3. Choose Amazon Elastic Compute Cloud (Amazon EC2) from the list, or type the name of the service in the search box.
4. Choose the AMI quota to request an increase. The AMI quotas you can select are:
- AMIs
- Public AMIs
- AMI sharing
5. Choose Request quota increase.
6. For Change quota value, enter the new quota value, and then choose Request.
To view any pending or recently resolved requests, choose Dashboard from the navigation pane.
For pending requests, choose the status of the request to open the request receipt. The initial

status of a request is Pending. After the status changes to Quota requested, you'll see the case number under Support Center case number. Choose the case number to open the ticket for your request.
After the request is resolved, the Applied quota value for the quota is set to the new value.
For more information, see the Service Quotas User Guide.
