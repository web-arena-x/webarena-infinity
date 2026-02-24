# About Utilities (Engage Legacy)

Source: https://support.zendesk.com/hc/en-us/articles/9731500537498-About-Utilities-Engage-Legacy

---

# What are Utilities in Engage?

- Utilities are a concept in Engage, designed to bring greater flexibility to the platform
- Utilities enable Admins to configure functionality and determine where and when it is available to Agents (via Workflows)
- Utilities can be configured to appear in either the Main or Side Panel in Engage, and can be made visible to Agents during a contact, in after call work, or both
- Over time, a range of Utility Types will be made available
- The first set of Utility Types will be iFrames and Tasks
- Utilities are contact driven, meaning they are available to Agents whilst on a contact or in after call work (ACW)

**tldr:** Think of a Utility as a flexible and customizable UI component that can be configured (by an Admin) to contain various functionality. It can be positioned in different locations across the Engage platform and activated in multiple ways depending on an Agent’s actions.

## Why are Utilities important?

Agents often need to use multiple applications to resolve a customer query. Switching between the applications is an inefficient process, leading to longer call times and lower customer satisfaction.

Utilities in Engage make it easier for Agents to get the information they need to assist a customer quicker and within the Engage application. This results in a better experience for both the Agent and the customer.

Utilities also ensure that when an Agent needs to perform additional tasks/actions (such as create a follow up task during a call), they can do it quickly and easily whilst remaining on the contact screen.

## Utility Types

### iFrame Embed

- Display 3rd party applications within Engage, based on the configuration of the Utility and the relevant Workflow
- Enables an agent to read, write, or update data within the 3rd party application (based on their permission within the 3rd party application)
- Reduces the need for Agents to switch between multiple applications
- Ensures focus on the ongoing contact

#### Example

The example below shows an Agent using two Utilities:

- Side Panel: An iFrame Embed Utility displaying a 3rd party booking application, enabling the Agent to book an appointment for the customer without navigating away from the contact
- Main Panel: An iFrame Embed Utility using a custom Google Map to display points of interest to the Agent, enabling the Agent to provide information (in this case a list of stations) to the customer without navigating away from the contact

![](https://support.zendesk.com/hc/article_attachments/9731464089882)

### Tasks

- Display Tasks within Engage, based on the configuration of the Utility and the relevant Workflow
- Enables the Agent to efficiently create follow-up Tasks whilst on a contact
- If you have previously utilised Tasks within Engage, you will notice that the functionality within Tasks has not changed with the introduction of Utilities
- Tasks within Utilities ensures Admins have greater control as to when and where Tasks appear to Agents

#### Example

The example below shows an Agent using a Task Utility:

- The Task Utility is configured by the Admin and displays a form for the Agent to complete
- This example enables the Agent to quickly schedule a callback at the time specific by the customer

![](https://support.zendesk.com/hc/article_attachments/9731464104346)

To an Agent, all Utilities behave and appear in a similar fashion. They can all be configured to appear in either the Main or Side Panel within Engage, and can be made visible during a contact, in after call work, or both.  
Once an Agent opens a Utility, the functionality within the Utility will be dependant on what the Admins have configured

## Other things to consider.

Utilities are contact driven - they are only available to Agents whilst on a contact or in after call work (ACW). Utilities are designed to only display information to Agents if it is relevant to their ongoing contact or ACW.

As an example, a dashboard displaying metrics to an Agent is is not a recommended use case for a Utility.

‍