# How to Configure and Customize Screen Pops (Engage Legacy)

Source: https://support.zendesk.com/hc/en-us/articles/9731466408346-How-to-Configure-and-Customize-Screen-Pops-Engage-Legacy

---

Screen pop is a valuable feature within Salesforce CTI as it instantly displays relevant customer profile information from Engage on an agent's screen during a call, enabling quicker issue resolution, personalised interactions, reduced call handling time, and an enhanced customer experience.  
EngageCTI will support screen pop to any Salesforce Record such as Contacts, Cases, Accounts and Leads.

## Default Behaviour

Without any additional configuration the Engage CTI will attempt to Screen Pop based on the Phone Number, Email Address, or Name of the contact (in that order).

The specific behaviour will depend on the [Softphone layout](https://support.zendesk.com/hc/en-us/articles/9731439448986) for the given Salesforce User.

## Using Customer Profiles

If a Customer Profile is linked to a Salesforce Contact (either [manually](https://support.zendesk.com/hc/en-us/articles/9731439448986) or via [an Integration](https://docs.aws.amazon.com/connect/latest/adminguide/steps-integrate-cp-salesforce-servicenow.html)), then the Engage CTI will pop straight to that Contact Record.

**Further Reading:** Understand some [Best Practices for Profile Matching for Salesforce](https://support.zendesk.com/articles/best-practices-for-profile-matching-for-cti)

## Using Contact Attributes

Often you will want to Screen Pop different information for a specific call or chat (eg: a specific Case or a related Account). To achieve this Engage CTI provides 2 attributes you can add to Contact. If one of these attributes are Engage will use these rules instead of the Profile or Default behaviour.

1. **\_cti\_screenpop\_id:** Set this attribute using an Object ID for any Salesforce Object. This is most useful if you are doing a lookup in Contact Flow before the Contact gets to the Agent.
2. \_**cti\_screenpop\_search:** Set this attribute to any value you want to search for in Salesforce (eg. Phone Number, Website, Case Reference Number). Use this option when you don't know the exact Salesforce Object Id but want more control of the search term.

**Further Reading:** Deepdive into [Contact Attributes in the Connect Admin Guide](https://docs.aws.amazon.com/connect/latest/adminguide/how-to-reference-attributes.html)

### Referencing Dynamic Values

These to attributes also support [Personalisation Tokens](https://support.zendesk.com/hc/en-us/articles/9731499735706) as values, allowing you to reference other attributes on the Contact or Profile.

A scenario where this is useful is when you don't know the Profile during a contact flow, and want to rely on Engage Profile Matching or manual matching by the Agent:

1. Set the **\_cti\_screenpop\_search** to {{Customer.AccountId}}
2. Once the Profile is matched (either automatically or manually by an agent)
3. Engage CTI will search for the matched Profile's AccountID in Salesforce and Pop to that record.