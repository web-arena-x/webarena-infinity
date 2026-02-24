# Using customer profiles in Contact Center

Source: https://support.zendesk.com/hc/en-us/articles/9790965061658-Using-customer-profiles-in-Contact-Center

---

Add-on | Zendesk for Contact Center

Customer profiles appear in the Customer details panel in Contact Center. Incoming contacts are matched to an existing profile, if one exists, or a new contact is created. The contact name is based on specific attributes, and there are fallback values if the attributes are unavailable.

Contact attributes appear in the conversation block (middle panel), depending on display rules. Standard attributes, such as queue, might be present. If you want other attributes to appear, attach the prefix "agt\_ " to the attribute.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/cc_extra_12.png)

This article contains the following topics:

- [Matching incoming contacts to customer profiles](#topic_trv_ktj_xgc)
- [Configuring customer profile creation](#topic_nts_xtj_xgc)
- [About the display name for contacts](#topic_tyv_kxj_xgc)
- [Preventing duplicate customer profiles](#topic_rzd_ckg_wgc)

## Matching incoming contacts to customer profiles

When a contact is routed to an agent, specific contact attributes are used to try to match the contact to an existing profile. All profiles are searched for matches, using all of the checked attributes.

- If a single match is found, the contact is automatically associated with that profile.
- If multiple matches are found, the agent can select the correct profile.
- If no profile matches are found, a new profile is automatically created or the agent is prompted to create one.

**To configure profile matching settings**

- Select **General Settings > Customer Profiles > Matching Rules**.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/cc_extra_13.png)

## Configuring customer profile creation

When creating a new customer profile, agents can update [standard profile attributes](https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_CreateProfile.html) only, they cannot add customer profile attributes. After a profile is created, it cannot be edited. When creating profiles, any contact attributes with the same name are mapped to the customer profile. See the list of [available profile attributes](https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_Profile.html).

Contact Center doesn't update profile attributes for existing profiles, rather it associates the current ContactID to make the history accessible. Agents cannot alter attributes. Any updates should be made in Lambdas in contact flows, either before the agent receives the contact or as a task (possibly with an approval step).

**To configure customer profile creation**

- Select **General Settings > Workflows > Profile creation**.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/cc_extra_14.png)

## Preventing duplicate customer profiles

You can prevent duplicate customer profiles by using the CTR-NoInferred template for profile creation. See [Contact record templates in Amazon Connect Customer Profiles](https://docs.aws.amazon.com/connect/latest/adminguide/ctr-contact-record-template.html) in the AWS documentation.

**To set the template for profile creation and auto association**

- In Profile creation and auto association, select **Create limited profiles and auto-associate profiles**.

 ![](../../../../Desktop/aaaaaaa/cc_extra_16.png)

 Click **Save**.

In the case of duplicate profiles, Amazon Connect provides tools to consolidate profiles automatically. See[Use Identity Resolution to consolidate similar profiles in Amazon Connect](https://docs.aws.amazon.com/connect/latest/adminguide/use-identity-resolution.html) in the AWS documentation.

‍

## About the display name for contacts

The customer name is displayed in several places in Contact Center.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/cc_extra_15.png)

The display name uses the FirstName and LastName attributes in the customer profile. If that the first name and last name are not available, other attributes are used.

The following profile attributes are used as the display name, in this order:

1. FirstName + LastName
2. EmailAddress
3. PhoneNumber
4. AccountNumber

If none of the profile attributes are available, contact attributes are used, in this order:

1. FullName
2. EmailAddress
3. PhoneNumber
4. AccountNumber
5. Contacts Phone Number (for calls only)