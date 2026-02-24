# Understanding Contact Center components

Source: https://support.zendesk.com/hc/en-us/articles/9829206009242-Understanding-Contact-Center-components

---

Take a moment to understand the building blocks of Contact Center and how they interact.

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **Add-on** | Zendesk for Contact Center |

Verified AI summary ◀▼

Understand the key components of Contact Center: Amazon Connect for handling calls and chats, Amazon Cognito for user authentication, and Amazon CloudFormation for automating AWS resource setup. The Contact Center app enhances the Connect experience with features like an agent desktop and AI tools. Data stays in your AWS account, ensuring security. For updates, use a dual-stack process for safe rollbacks.

Take a moment to understand the building blocks of Contact Center and how they interact.

This article contains the following topics:

- [Amazon Connect](#amazon-connect)
- [Amazon Cognito](#amazon-cognito)
- [Amazon CloudFormation](#amazon-cf)
- [Contact Center app](#cc-app)
- [Dual-stack upgrade process](#dual-stack-upgrade)

## Amazon Connect

Amazon Connect (Connect) is a cloud-based contact center service provided by AWS that helps you set up and manage customer support calls and chats. Think of it as the telephony and contact routing engine for Contact Center. It handles phone calls, chat conversations, queues, contact flows, and more. Connect is the foundation of Contact Center; every customer who uses Contact Center must have their own Connect instance in their AWS account. Each Contact Center environment links one-to-one with a specific Connect instance. You can't link multiple Connect instances to one Contact Center account or vice versa.

## Amazon Cognito

Amazon Cognito is an AWS service for user authentication and authorization. It allows you to manage user sign-up, sign-in, and access control for web or mobile applications. Amazon Cognito provides a user pool where user accounts (agents, supervisors, admins) who will log into Contact Center are stored. Cognito securely handles passwords and login, so that users can sign into the Contact Center app (web application). Cognito is used to create and manage agent identities instead of using a custom system. During setup, a Cognito user pool is automatically created using CloudFormation to facilitate identity management.

## Amazon CloudFormation

AWS CloudFormation is a service that helps you automate the setup of AWS resources using templates. CloudFormation uses templates to deploy the necessary AWS components, services, and permissions for Contact Center, with minimal manual input.

The CloudFormation stack (a collection of AWS resources defined by a template)
creates and configures resources such as the Amazon Cognito user pool, Identity and Access Management (IAM) roles and permissions, AWS Lambda functions, streaming connections, and other components that allow Connect and Contact Center to work together. Using CloudFormation saves time and reduces errors in setting up the backend services that sustain Contact Center.

## Contact Center app

Zendesk for Contact Center is a built-by-Zendesk app that works with Connect. It provides an intuitive agent interface and additional features (like omnichannel inbox, AI-powered tools, and advanced dashboards) to enhance the Connect experience.
Agents log into the Contact Center web interface to receive calls or messages, handled through the customer’s Connect instance.

Contact Center is deployed in the client’s AWS environment. All customer and contact center data (call recordings, customer info, and so on) stays in the customer’s AWS account instead of Zendesk's servers. This helps to ensure security and privacy. To use Contact Center, you need to link the Connect instance to the Contact Center app and deploy the AWS components (using CloudFormation) that facilitate the integration. Once set up, Contact Center and Connect operate as a unified contact center solution.

For more information, see [Navigating the Contact Center app](https://support.zendesk.com/hc/en-us/articles/9696121449114).

## Dual-stack upgrade process

The required infrastructure for Contact Center is deployed to your AWS environment using CloudFormation. Once deployed, that stack is never updated using the CloudFormation update process. Instead, a new (dual) CloudFormation stack is created and, once ready, Contact Center is reconfigured to use the new infrastructure. Once tested and validated, the old stack can be deleted. This ensures you have a safe rollback point.

To perform an update, an updated template URL must be [requested from Zendesk](https://support.zendesk.com/hc/en-us/articles/4408843597850).