# Customer Profiles Overview (Engage Legacy)

Source: https://support.zendesk.com/hc/en-us/articles/9731437839642-Customer-Profiles-Overview-Engage-Legacy

---

Engage classifies and displays customer details in specific panels on the Engage desktop. It searches for matching profiles for incoming contacts and either links or creates new ones. The contact display name in the UI relies on specific attributes with fallbacks if unavailable.

## Engage display

Engage only displays Customer Profile attributes in the customer details panel.

![](https://support.zendesk.com/hc/article_attachments/9731474683546)

On the other hand, Contact Attributes appear in the conversation metablock (middle panel), depending on display rules. Standard attributes like **Queue** may be present. To have other attributes display here prefix them with agt\_ .

## How Engage handles Profile Matching

When a contact is routed to an agent, Engage uses specific Contact Attributes to search for an existing profile. Engage will always search for profiles using all of the checked attributes and will not stop after a match is found. If there's a single match, the contact will be automatically associated with that profile, providing the agent with the profile's details and history.

In case of multiple matches, the agent will be asked to select the correct profile. If no profiles are found, Engage will either create a new profile automatically or prompt the agent to create one.

When creating a new profile, the agent can only update [standard profile attributes](https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_CreateProfile.html) and cannot add customer profile attributes. Once a profile is created, it cannot be edited.

Profile matching settings can be configured in General Settings > Customer Profiles > Matching Rules.

![](https://support.zendesk.com/hc/article_attachments/9731474712474)

Profile creation settings can be configured in General Settings > Workflows > Profile creation.

![](https://support.zendesk.com/hc/article_attachments/9731498710042)

## Engage's Approach to Profile Updates

As it stands, Engage doesn't update Profile Attributes for existing profiles. It simply associates the current ContactID to make the history accessible. Also, agents are not permitted to alter attributes.

Any updates need to be executed in Lambdas in contact flows, either before the agent receives the contact, or via a task (possibly with an approval step).

## Attribute Selection for Profile Creation

When creating profiles, any Contact Attributes with the same name will be mapped to the customer profile. Refer to [this document](https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_Profile.html) for a list of available Profile Attributes.

## How do I control the display name of a contact?

The customer name is displayed in various places throughout the Engage UI.

![](https://support.zendesk.com/hc/article_attachments/9731437903770)

Ultimately, Engage will use the FirstName and LastName attributes of the Customer from the matched profile. However there are a few fallbacks to try if that info isn't available. The current rules are as follows:

From Profile:

1. FirstName + LastName
2. EmailAddress
3. PhoneNumber
4. AccountNumber

If none of those are available Engage will use Contact Attributes:

1. FullName
2. EmailAddress
3. PhoneNumber
4. AccountNumber
5. Contacts Phone Number (for Calls only)

‍