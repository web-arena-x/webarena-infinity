# Updating the Local Measure Engage CloudFormation Stack (Engage Legacy)

Source: https://support.zendesk.com/hc/en-us/articles/9731451023386-Updating-the-Local-Measure-Engage-CloudFormation-Stack-Engage-Legacy

---

**NB:** This article is outdated, please see the Guide with the updated instructions on how to upgrade the Engage CloudFormation stack (resources.localmeasure.com/guides/updating-the-engage-cloudformation-stack)

‍

## Overview

Local Measure recommends creating a new, parallel CloudFormation stack for upgrades, rather than updating an existing stack. The new stack can safely be deployed without any impact on the existing stack. When ready, the Engage Account configuration can be changed to point to the new CloudFormation stack and the solution can be tested. Once everything is confirmed to be working, the old CloudFormation stack can safely be deleted. If any challenges are encountered during testing, the Engage Account configuration can again be changed to point to the old CloudFormation stack. This ensures that an operational environment can be maintained while any potential issues are investigated on the new CloudFormation stack.

‍

**NB:** Local Measure does not recommend that environments using email routing be upgraded without assistance from Local Measure. Please reach out to Local Measure for assistance with this.

## Instructions

To perform such a "dual stack" upgrade, log into the AWS account and navigate to the CloudFormation service.

Select 'Create Stack' -> 'With new resources (standard)'

Paste the Local Measure stack template url (<https://localmeasure-connect.s3.amazonaws.com/localmeasure-connect.yaml>) in the Amazon S3 URL field as shown below and click 'Next'.

![](https://support.zendesk.com/hc/article_attachments/9731467595290)

Under 'Stack name' fill in a descriptive name such as "LM-Engage-V2". **NB:** Very long stack names can result in a failure upon stack creation. The reason for this is that the stack name is included in the names of the resources, which could result in the eventual resource path exceeding the character limit for that service.

The template should be filled in with exactly the same values as for the original stack, with the following **important exceptions**:

| Parameter | Mandatory | Description |
| --- | --- | --- |
| Authentication with Cognito | | |
| EnableCognito | y | Select Existing |
| UserPoolId | y | Navigate to the userpool which was created by the original CloudFormation stack. AWS Console -> Coginto. Select and open the userpool and copy the ‘User pool ID’ from the ‘User pool overview’ section. Paste the value in this field. |
| AppClientId | y | After copying the UserPoolId, select the ‘App Integration’ tab and scroll to the bottom. Copy the ‘Client ID’. Paste the value in this field. |
| DomainPrefix | y | Enter the exact same value as when the initial stack was created. |
| Email channel for Amazon Connect, using Simple Email Service (SES) | | |
| EnableEmail | n | Same as original stack |
| SESRegion | n | Same as original stack |
| SESBucketName | n | If email was enabled in the original stack, the bucket will already exist. Fill in the same bucket name. |
| SESBucketRegion | n | Same as original stack |
| SESBucketExist | n | If email was enabled in the original stack, the bucket will already exist. Therefore select ‘Yes’. |
| CreateSESBucketPolicy | n | If email was enabled in the original stack, the bucket will already exist and the policy would already have been applied to the bucket… Therefore select ‘No’. |
| SESReceiveEmail | n | Same as original stack |

Once you have filled in the CloudFormation template, check all fields to ensure that no additional whitespace (including tabs) have been added while copying and pasting the required values.

Once everything has been checked:

1. Click Next.
2. On the next page, leave everything as-is and click Next (Tags are optional).
3. On the next page, leave everything as-is and select “I acknowledge” at the bottom. Click Create Stack.
4. The CloudFormation Stack will take about 10 minutes to run. Refresh the status (right-side button) to watch for errors. Once it’s complete, the main Stack you created will show CREATE\_COMPLETE.

Upon completion, when all resources have been created, switch to the 'Outputs' tab. Local Measure will require these values in order to finalize the account setup. It is recommended to copy these values into an excel spreadsheet and to share this with the Local Measure Architect assisting you.

There is no need to reconfigure the Cognito user pool after an upgrade as the existing configuration has been retained.

‍

‍