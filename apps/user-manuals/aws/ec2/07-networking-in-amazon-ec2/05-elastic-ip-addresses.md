# Elastic IP addresses

Source: apps/user-manuals/aws/ec2-ug.pdf

---

aws ec2 create-vpc --cidr-block 10.0.0.0/16 --ipv6-cidr-block ipv6-cidr --ipv6- pool pool-id --region us-east-1 To associate an IPv6 CIDR block from your IPv6 address pool with a VPC, use the following associate-vpc-cidr-block command. To let Amazon choose the IPv6 CIDR from your IPv6 address pool, omit the --ipv6-cidr-block option. aws ec2 associate-vpc-cidr-block --vpc-id vpc-123456789abc123ab --ipv6-cidr-block ipv6- cidr --ipv6-pool pool-id --region us-east-1 To view your VPCs and the associated IPv6 address pool information, use the describe-vpcs command. To view information about associated IPv6 CIDR blocks from a specific IPv6 address pool, use the following get-associated-ipv6-pool-cidrs command. aws ec2 get-associated-ipv6-pool-cidrs --pool-id pool-id --region us-east-1 If you disassociate the IPv6 CIDR block from your VPC, it's released back into your IPv6 address pool.
# Elastic IP addresses An Elastic IP address is a static IPv4 address designed for dynamic cloud computing. An Elastic IP address is allocated to your AWS account, and is yours until you release it. By using an Elastic IP address, you can mask the failure of an instance or software by rapidly remapping the address to another instance in your account. Alternatively, you can specify the Elastic IP address in a DNS record for your domain, so that your domain points to your instance. For more information, see the documentation for your domain registrar.
An Elastic IP address is a public IPv4 address, which is reachable from the internet. If you need to connect to an instance that does not have a public IPv4 address, you can associate an Elastic IP address with your instance to enable communication with the internet.
Contents
- Elastic IP address pricing
- Elastic IP address basics
- Elastic IP address quota
- Associate an Elastic IP address with an instance

- Transfer an Elastic IP address between AWS accounts
- Release an Elastic IP address
- Create a reverse DNS record for email on Amazon EC2
## Elastic IP address pricing There is a charge for all Elastic IP addresses whether they are in use (allocated to a resource, like an EC2 instance) or idle (created in your account but unallocated).
AWS charges for all public IPv4 addresses, including public IPv4 addresses associated with running instances and Elastic IP addresses. For more information, see the Public IPv4 Address tab on the Amazon VPC pricing page.
## Elastic IP address basics The following are the basic characteristics of an Elastic IP address:
- An Elastic IP address is static; it does not change over time.
- An Elastic IP address is for use in a specific Region only, and cannot be moved to a different Region.
- An Elastic IP address comes from Amazon's pool of IPv4 addresses, or from a custom IPv4 address pool that you have brought to your AWS account. We do not support Elastic IP addresses for IPv6.
- To use an Elastic IP address, you first allocate one to your account, and then associate it with your instance or a network interface.
- When you associate an Elastic IP address with an instance, it is also associated with the instance's primary network interface. When you associate an Elastic IP address with a network interface that is attached to an instance, it is also associated with the instance.
- When you associate an Elastic IP address with an instance or its primary network interface, if the instance already has a public IPv4 address associated with it, that public IPv4 address is released back into Amazon's pool of public IPv4 addresses and the Elastic IP address is associated with the instance instead. You cannot reuse the public IPv4 address previously associated with the instance and you cannot convert that public IPv4 address to an Elastic IP address. For more information, see Public IPv4 addresses.
- You can disassociate an Elastic IP address from a resource, and then associate it with a different resource. To avoid unexpected behavior, ensure that all active connections to the resource named

in the existing association are closed before you make the change. After you have associated your Elastic IP address to a different resource, you can reopen your connections to the newly associated resource.
- A disassociated Elastic IP address remains allocated to your account until you explicitly release it. You are charged for all Elastic IP addresses in your account, regardless of whether they are associated or disassociated with an instance. For more information, see the Public IPv4 Address tab on the Amazon VPC pricing page.
- When you associate an Elastic IP address with an instance that previously had a public IPv4 address, the public DNS host name of the instance changes to match the Elastic IP address.
- We resolve a public DNS host name to the public IPv4 address or the Elastic IP address of the instance outside the network of the instance, and to the private IPv4 address of the instance from within the network of the instance.
- When you allocate an Elastic IP address from an IP address pool that you have brought to your AWS account, it does not count toward your Elastic IP address limits. For more information, see Elastic IP address quota.
- When you allocate the Elastic IP addresses, you can associate the Elastic IP addresses with a network border group. This is the location from which we advertise the CIDR block. Setting the network border group limits the CIDR block to this group. If you do not specify the network border group, we set the border group containing all of the Availability Zones in the Region (for example, us-west-2).
- An Elastic IP address is for use in a specific network border group only.
## Elastic IP address quota By default, all AWS accounts have a quota of five (5) Elastic IP addresses per Region, because public (IPv4) internet addresses are a scarce public resource. We strongly recommend that you use Elastic IP addresses primarily for their ability to remap the address to another instance in the case of instance failure, and to use DNS hostnames for all other inter-node communication.
If you think your architecture warrants additional Elastic IP addresses, you can request a quota increase directly from the Service Quotas console. To request a quota increase, choose Request increase at account-level. For more information, see Amazon EC2 service quotas.

## Associate an Elastic IP address with an instance After you allocate an Elastic IP address, you can associate it with an AWS resource, such as an EC2 instance, NAT gateway, or Network Load Balancer. To associate an Elastic IP address with a different AWS resource later on, you can disassociate it from its current resource and then associated it with the new resource.
Tasks
- Allocate an Elastic IP address
- Associate an Elastic IP address
- Disassociate an Elastic IP address
### Allocate an Elastic IP address You can allocate an Elastic IP address for use in a Region. There is a charge for all Elastic IP addresses whether they are in use (associated with a resource, like an EC2 instance) or idle (created in your account but unassociated).
Console To allocate an Elastic IP address
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. In the navigation pane, choose Network & Security, Elastic IPs.
3. Choose Allocate Elastic IP address.
4. (Optional) When you allocate an Elastic IP address (EIP), you choose the Network border group in which to allocate the EIP. A network border group is a collection of Availability Zones (AZs), Local Zones, or Wavelength Zones from which AWS advertises a public IP address. Local Zones and Wavelength Zones may have different network border groups than the AZs in a Region to ensure minimum latency or physical distance between the AWS network and the customers accessing the resources in these Zones.
Important You must allocate an EIP in the same network border group as the AWS resource that will be associated with the EIP. An EIP in one network border group can only

be advertised in zones in that network border group and not in any other zones represented by other network border groups.
If you have Local Zones or Wavelength Zones enabled (for more information, see Enable a Local Zone or Enable Wavelength Zones), you can choose a network border group for AZs, Local Zones, or Wavelength Zones. Choose the network border group carefully as the EIP and the AWS resource it is associated with must reside in the same network border group.
You can use the EC2 console to view the network border group that your Availability Zones, Local Zones, or Wavelength Zones are in. Typically, all Availability Zones in a Region belong to the same network border group, whereas Local Zones or Wavelength Zones belong to their own separate network border groups.
If you don't have Local Zones or Wavelength Zones enabled, when you allocate an EIP, the network border group that represents all of the AZs for the Region (such as us-west-2) is predefined for you and you cannot change it. This means that the EIP that you allocate to this network border group will be advertised in all AZs in the Region you're in.
5. For Public IPv4 address pool, choose one of the following:
- Amazon's pool of IPv4 addresses—If you want an IPv4 address to be allocated from Amazon's pool of IPv4 addresses.
- Public IPv4 address that you bring to your AWS account—If you want to allocate a non- contiguous (non-sequential) public IPv4 address from an IP address pool that you have brought to your AWS account. This option is disabled if you do not have any IP address pools. For more information about bringing your own IP address range to your AWS account, see Bring your own IP addresses (BYOIP) to Amazon EC2.
- Customer owned pool of IPv4 addresses—If you want to allocate an IPv4 address from a pool created from your on-premises network for use with an AWS Outpost. This option is disabled if you do not have an AWS Outpost.
- Allocate using an IPAM IPv4 pool: If you want to allocate sequential Elastic IP addresses from a contiguous public IPv4 block in an IPAM pool. Allocating sequential Elastic IP addresses can significantly reduce management overhead for security access control lists and simplify IP address allocation and tracking for enterprises scaling on AWS. For more information, see Allocate sequential Elastic IP addresses from an IPAM pool in the Amazon VPC IPAM User Guide.
6. (Optional) To add a tag, choose Add new tag and enter a tag key and a tag value.

AWS CLI To allocate an Elastic IP address Use the allocate-address AWS CLI command.
In the following example, Amazon EC2 selects an address from Amazon's address pool. aws ec2 allocate-address In the following example, Amazon EC2 selects an address from the specified pool that you brought to AWS using BYOIP. aws ec2 allocate-address \ --public-ipv4-pool ipv4pool-ec2-012345abcdef67890 The following example specifies an address from the specified IPv4 IPAM pool. aws ec2 allocate-address \ --ipam-pool-id ipam-pool-1234567890abcdef0 \ --address 192.0.2.0 PowerShell To allocate an Elastic IP address Use the New-EC2Address cmdlet.
In the following example, Amazon EC2 selects an address from Amazon's address pool.
New-EC2Address In the following example, Amazon EC2 selects an address from the specified pool that you brought to AWS using BYOIP.
New-EC2Address \ --PublicIpv4Pool ipv4pool-ec2-012345abcdef67890 The following example specifies an address from the specified IPv4 IPAM pool.

New-EC2Address \ --IpamPoolId ipam-pool-1234567890abcdef0 \ --Address 192.0.2.0
### Associate an Elastic IP address If you're associating an Elastic IP address with your instance to enable communication with the internet, you must also ensure that your instance is in a public subnet. For more information, see Enable internet access using an internet gateway in the Amazon VPC User Guide.
Console To associate an Elastic IP address with an instance
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. In the navigation pane, choose Elastic IPs.
3. Select the Elastic IP address to associate and choose Actions, Associate Elastic IP address.
4. For Resource type, choose Instance.
5. For instance, choose the instance with which to associate the Elastic IP address. You can also enter text to search for a specific instance.
6. (Optional) For Private IP address, specify a private IP address with which to associate the Elastic IP address.
7. Choose Associate.
To associate an Elastic IP address with a network interface
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. In the navigation pane, choose Elastic IPs.
3. Select the Elastic IP address to associate and choose Actions, Associate Elastic IP address.
4. For Resource type, choose Network interface.
5. For Network interface, choose the network interface with which to associate the Elastic IP address. You can also enter text to search for a specific network interface.
6. (Optional) For Private IP address, specify a private IP address with which to associate the Elastic IP address.
7. Choose Associate.

AWS CLI To associate an Elastic IP address Use the associate-address AWS CLI command. aws ec2 associate-address \ --instance-id i-0b263919b6498b123 \ --allocation-id eipalloc-64d5890a PowerShell To associate an Elastic IP address Use the Register-EC2Address cmdlet.
Register-EC2Address `
    -InstanceId i-0b263919b6498b123 `
    -AllocationId eipalloc-64d5890a
### Disassociate an Elastic IP address You can disassociate an Elastic IP address from an instance or network interface at any time. After you disassociate the Elastic IP address, you can associate it with another resource.
Console To disassociate and reassociate an Elastic IP address
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. In the navigation pane, choose Elastic IPs.
3. Select the Elastic IP address to disassociate, choose Actions, Disassociate Elastic IP address.
4. Choose Disassociate.
AWS CLI To disassociate an Elastic IP address Use the disassociate-address AWS CLI command.

aws ec2 disassociate-address --association-id eipassoc-12345678 PowerShell To disassociate an Elastic IP address Use the Unregister-EC2Address cmdlet.
Unregister-EC2Address -AssociationId eipassoc-12345678
## Transfer an Elastic IP address between AWS accounts You can transfer an Elastic IP address from one AWS account to another. This can be helpful in the following situations:
- Disaster recovery – Quickly remap the IP addresses for public-facing internet workloads during emergency events.
- Organizational restructuring – Quickly move a workload from one AWS account to another.
An address transfer avoids the need to wait for new Elastic IP addresses to be allowed by your security groups and network ACLs.
- Centralized security administration – Use a centralized AWS security account to track and transfer Elastic IP addresses that have been vetted for security compliance.
Pricing There is no charge for transferring Elastic IP addresses.
Tasks
- Enable Elastic IP address transfer
- Accept a transferred Elastic IP address
- Disable Elastic IP address transfer
### Enable Elastic IP address transfer This section describes how to accept a transferred Elastic IP address. Note the following limitations related to enabling Elastic IP addresses for transfer:

- You can transfer Elastic IP addresses from any AWS account (source account) to any other AWS account in the same AWS Region (transfer account). You cannot transfer Elastic IP addresses to a different Region.
- When you transfer an Elastic IP address, there is a two-step handshake between the AWS accounts. When the source account starts the transfer, the transfer accounts have seven days to accept the Elastic IP address transfer. During those seven days, the source account can view the pending transfer (for example in the AWS console or by using the describe-address-transfers command). After seven days, the transfer expires and ownership of the Elastic IP address returns to the source account.
- Accepted transfers are visible to the source account (for example in the AWS console or by using the describe-address-transfers command) for 14 days after the transfers have been accepted.
- AWS does not notify transfer accounts about pending Elastic IP address transfer requests. The owner of the source account must notify the owner of the transfer account that there is an Elastic IP address transfer request that they must accept.
- Any tags that are associated with an Elastic IP address being transferred are reset when the transfer is complete.
- You cannot transfer Elastic IP addresses allocated from public IPv4 address pools that you bring to your AWS account – commonly referred to as Bring Your Own IP (BYOIP) address pools.
- You cannot transfer Elastic IP addresses allocated from an Amazon-provided contiguous public IPv4 Amazon VPC IP Address Manager (IPAM) pool. Instead, IPAM allows you to share IPAM pools across AWS accounts by integrating IPAM with AWS Organizations and using AWS RAM. For more information, see Allocate sequential Elastic IP addresses from an IPAM pool in the Amazon VPC IPAM User Guide.
- If you attempt to transfer an Elastic IP address that has a reverse DNS record associated with it, you can begin the transfer process, but the transfer account will not be able to accept the transfer until the associated DNS record is removed.
- If you have enabled and configured AWS Outposts, you might have allocated Elastic IP addresses from a customer-owned IP address pool (CoIP). You cannot transfer Elastic IP addresses allocated from a CoIP. However, you can use AWS RAM to share a CoIP with another account. For more information, see Customer-owned IP addresses in the AWS Outposts User Guide.
- You can use Amazon VPC IPAM to track the transfer of Elastic IP addresses to accounts in an organization from AWS Organizations. For more information, see View IP address history. If an Elastic IP address is transferred to an AWS account outside of the organization, the IPAM audit history of the Elastic IP address is lost.

These steps must be completed by the source account.
Console To enable Elastic IP address transfer
1. Ensure that you're using the source AWS account.
2. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
3. In the navigation pane, choose Elastic IPs.
4. Select one or more Elastic IP address to enable for transfer and choose Actions, Enable transfer.
5. If you are transferring multiple Elastic IP addresses, you'll see the Transfer type option.
Choose one of the following options:
- Choose Single account if you are transferring the Elastic IP addresses to a single AWS account.
- Choose Multiple accounts if you are transferring the Elastic IP addresses to multiple AWS accounts.
6. Under Transfer account ID, enter the IDs of the AWS accounts that you want to transfer the Elastic IP addresses to.
7. Confirm the transfer by entering enable in the text box.
8. Choose Submit.
9. To accept the transfer, see Accept a transferred Elastic IP address. To disable the transfer, see Disable Elastic IP address transfer.
AWS CLI To enable Elastic IP address transfer Use the enable-address-transfer command. aws ec2 enable-address-transfer \ --allocation-id eipalloc-09ad461b0d03f6aaf \ --transfer-account-id 123456789012 PowerShell To enable Elastic IP address transfer

Use the Enable-EC2AddressTransfer cmdlet.
Enable-EC2AddressTransfer `
    -AllocationId eipalloc-09ad461b0d03f6aaf `
    -TransferAccountId 123456789012
### Accept a transferred Elastic IP address This section describes how to accept a transferred Elastic IP address.
When you transfer an Elastic IP address, there is a two-step handshake between the AWS accounts.
When the source account starts the transfer, the transfer accounts have seven days to accept the Elastic IP address transfer. During those seven days, the source account can view the pending transfer (for example in the AWS console or by using the describe-address-transfers command).
After seven days, the transfer expires and ownership of the Elastic IP address returns to the source account.
When accepting transfers, note the following exceptions that might occur and how to resolve them:
- AddressLimitExceeded: If your transfer account has exceeded the Elastic IP address quota, the source account can enable Elastic IP address transfer, but this exception occurs when the transfer account tries to accept the transfer. By default, all AWS accounts are limited to 5 Elastic IP addresses per Region. See Elastic IP address quota for instructions on increasing the limit.
- InvalidTransfer.AddressCustomPtrSet: If you or someone in your organization has configured the Elastic IP address that you are attempting to transfer to use reverse DNS lookup, the source account can enable transfer for the Elastic IP address, but this exception occurs when the transfer account tries to accept the transfer. To resolve this issue, the source account must remove the DNS record for the Elastic IP address. For more information, see Create a reverse DNS record for email on Amazon EC2.
- InvalidTransfer.AddressAssociated: If an Elastic IP address is associated with an ENI or EC2 instance, the source account can enable transfer for the Elastic IP address, but this exception occurs when the transfer account tries to accept the transfer. To resolve this issue, the source account must disassociate the Elastic IP address. For more information, see Disassociate an Elastic IP address.
For any other exceptions, contact Support.

These steps must be completed by the transfer account.
Console To accept an Elastic IP address transfer
1. Ensure that you're using the transfer account.
2. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
3. In the navigation pane, choose Elastic IPs.
4. Choose Actions, Accept transfer.
5. No tags that are associated with the Elastic IP address being transferred are transferred with the Elastic IP address when you accept the transfer. If you want to define a Name tag for the Elastic IP address that you are accepting, select Create a tag with a key of 'Name' and a value that you specify.
6. Enter the Elastic IP address that you want to transfer.
7. If you are accepting multiple transferred Elastic IP addresses, choose Add address to enter an additional Elastic IP address.
8. Choose Submit.
AWS CLI To accept an Elastic IP address transfer Use the accept-address-transfer command. aws ec2 accept-address-transfer --address 100.21.184.216 PowerShell To accept an Elastic IP address transfer Use the Approve-EC2AddressTransfer cmdlet.
Approve-EC2AddressTransfer -Address 100.21.184.216
### Disable Elastic IP address transfer This section describes how to disable an Elastic IP transfer after the transfer has been enabled.

These steps must be completed by the source account that enabled the transfer.
Console To disable an Elastic IP address transfer
1. Ensure that you're using the source AWS account.
2. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
3. In the navigation pane, choose Elastic IPs.
4. In the resource list of Elastic IPs, ensure that you have the property enabled that shows the column Transfer status.
5. Select one or more Elastic IP address that have a Transfer status of Pending, and choose Actions, Disable transfer.
6. Confirm by entering disable in the text box.
7. Choose Submit.
AWS CLI To disable Elastic IP address transfer Use the disable-address-transfer command. aws ec2 disable-address-transfer --allocation-id eipalloc-09ad461b0d03f6aaf PowerShell To disable Elastic IP address transfer Use the Disable-EC2AddressTransfer cmdlet.
Disable-EC2AddressTransfer -AllocationId eipalloc-09ad461b0d03f6aaf
## Release an Elastic IP address If you no longer need an Elastic IP address, we recommend that you release it. The Elastic IP address to release must not be currently associated with an AWS resource.

Console To release an Elastic IP address
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. In the navigation pane, choose Elastic IPs.
3. Select the Elastic IP address to release and choose Actions, Release Elastic IP addresses.
4. Choose Release.
AWS CLI To release an Elastic IP address Use the release-address AWS CLI command. aws ec2 release-address --allocation-id eipalloc-64d5890a PowerShell To release an Elastic IP address Use the Remove-EC2Address cmdlet.
Remove-EC2Address -AllocationId eipalloc-64d5890a After you release your Elastic IP address, you might be able to recover. The following rules apply:
- You can't recover an Elastic IP address if it has been allocated to another AWS account, or if it will result in your exceeding your Elastic IP address limit.
- You can't recover tags associated with an Elastic IP address.
AWS CLI To recover an Elastic IP address Use the allocate-address command. aws ec2 allocate-address \ --domain vpc \

    --address 203.0.113.3 PowerShell To recover an Elastic IP address Use the New-EC2Address cmdlet.
New-EC2Address `
    -Address 203.0.113.3 `
    -Domain vpc `
    -Region us-east-1
## Create a reverse DNS record for email on Amazon EC2 If you intend to send email to third parties from an EC2 instance, we recommend that you provision one or more Elastic IP addresses and assign static reverse DNS records to the Elastic IP addresses that you use to send email. This can help you avoid having your email flagged as spam by some anti-spam organizations. AWS works with ISPs and internet anti-spam organizations to reduce the chance that your email sent from these addresses will be flagged as spam.
Considerations
- Before you create a reverse DNS record, you must set a corresponding forward DNS record (record type A) that points to your Elastic IP address.
- If a reverse DNS record is associated with an Elastic IP address, the Elastic IP address is locked to your account and cannot be released from your account until the record is removed.
- If you contacted Support to set up reverse DNS for an Elastic IP address, you can remove the reverse DNS, but you can't release the Elastic IP address because it is locked by Support. To unlock the Elastic IP address, contact AWS Support. After the Elastic IP address is unlocked, you can release it.
- [AWS GovCloud (US) Region] You can't create a reverse DNS record. AWS must assign the static reverse DNS records for you. Open a support case to remove reverse DNS and email sending limitations. You must provide your Elastic IP addresses and reverse DNS records.
### Create a reverse DNS record You can create a reverse DNS record for your Elastic IP address as follows.

Console To create a reverse DNS record
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. In the navigation pane, choose Elastic IPs.
3. Select the Elastic IP address and choose Actions, Update reverse DNS.
4. For Reverse DNS domain name, enter the domain name.
5. Enter update to confirm.
6. Choose Update.
AWS CLI To create a reverse DNS record Use the modify-address-attribute command. aws ec2 modify-address-attribute \ --allocation-id eipalloc-abcdef01234567890 \ --domain-name example.com The following is example output.
{ "Addresses": [ { "PublicIp": "192.0.2.0", "AllocationId": "eipalloc-abcdef01234567890", "PtrRecord": "example.net.", "PtrRecordUpdate": { "Value": "example.com.", "Status": "PENDING"
            } } ]
} PowerShell To create a reverse DNS record

Use the Edit-EC2AddressAttribute cmdlet.
Edit-EC2AddressAttribute `
    -AllocationId 'eipalloc-abcdef01234567890' `
    -DomainName 'example.com' | Format-List `
    AllocationId, PtrRecord, PublicIp, @{Name='PtrRecordUpdate';Expression={$_.PtrRecordUpdate | Format-List | Out- String}} The following is example output.
AllocationId    : eipalloc-abcdef01234567890 PtrRecord       : example.net.
PublicIp        : 192.0.2.0 PtrRecordUpdate :
                  Reason :
                  Status : PENDING Value  : example.com.
### Remove a reverse DNS record You can remove a reverse DNS record from your Elastic IP address as follows.
If you receive the following error, you can submit a Request to remove email sending restrictions to Support for assistance.
The address cannot be released because it is locked to your account.
Console To remove a reverse DNS record
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. In the navigation pane, choose Elastic IPs.
3. Select the Elastic IP address and choose Actions, Update reverse DNS.
4. For Reverse DNS domain name, clear the domain name.
5. Enter update to confirm.

6. Choose Update.
AWS CLI To remove a reverse DNS record Use the reset-address-attribute command. aws ec2 reset-address-attribute \ --allocation-id eipalloc-abcdef01234567890 \ --attribute domain-name The following is example output.
{ "Addresses": [ { "PublicIp": "192.0.2.0", "AllocationId": "eipalloc-abcdef01234567890", "PtrRecord": "example.com.", "PtrRecordUpdate": { "Value": "example.net.", "Status": "PENDING"
            } } ]
} PowerShell To remove a reverse DNS record Use the Reset-EC2AddressAttribute cmdlet.
Reset-EC2AddressAttribute `
    -AllocationId 'eipalloc-abcdef01234567890' `
    -Attribute domain-name | Format-List `
    AllocationId, PtrRecord, PublicIp, @{Name='PtrRecordUpdate';Expression={$_.PtrRecordUpdate | Format-List | Out- String}}
