# How to Provide Legal Notices and Obtain Consent in Zendesk

Source: https://support.zendesk.com/hc/en-us/articles/9536020725658-How-to-Provide-Legal-Notices-and-Obtain-Consent-in-Zendesk

---

**Note:** For guides on how Zendesk features can assist with your other obligations under privacy laws, see [Complying with Privacy and Data Protection Law in Zendesk products.](complying-with-privacy-and-data-protection-law-in-zendesk-products.md)

Various laws, including the General Data Protection Regulation (GDPR), California Consumer Privacy Act (CCPA), artificial intelligence-related laws, and call recording consent rules, may require you to provide legal notices to and/or obtain consent from your end-users.

Zendesk offers a variety of tools and features that empower you to meet these obligations effectively. Below is an overview of how you can use Zendesk products to provide the necessary notices and obtain consent from your end-users:

### 1. Call Recording Permissions: Opt-In and Opt-Out Notices

If your business records calls, you may be required to inform callers or obtain their consent depending on applicable laws. Zendesk provides options for call recordings, allowing you to comply with opt-in or opt-out requirements.

*Learn more:*[Understanding call recording permissions (opt-in and opt-out)](../managing-your-voice-channel/understanding-call-recording-permissions-opt-in-and-opt-out.md).

### 2. Legal Notices in Web-Based Widgets and Pre-Chat Form

**Web-based Widgets:** When engaging with customers via Zendesk’s web-based messaging widgets, you can link to your privacy notice directly within the widget interface. You can also configure other notice options, such as configuring default greeting messages or providing notice through the use of a cookie banner.

**Pre-chat Form Using Web Tools in Zendesk Chat:** You can create a custom pre-chat form using web tools in Zendesk Chat. This pre-chat form can include a checkbox for end-users. You can use the SDK to rebuild the entire widget, add additional disclaimers, and leverage the translations available in multiple languages. When the user submits the form, the account can initiate chat using the zChat.init API. You can add tags to store the consent along with the chat. These tags are available with the chats and can be downloaded by the account in CSV format. Admins can identify the chats and delete the chats where end-users do not wish to have their details stored with the account. Tags can help identify such chats. You can also create a similar notice for your offline forms. Please note that this feature is specific to Zendesk Chat and does not apply to Zendesk Messaging.

*Learn more:* [Notifying end users of legal terms in Zendesk’s web-based widgets,](../web-widget-documentation/notifying-end-users-of-legal-terms-in-zendesks-web-based-widgets.md)[zChat.init API (options)](https://api.zopim.com/web-sdk/#zchat-init-options) and [Setting up Zendesk Chat](https://support.zendesk.com/hc/en-us/sections/4405298916890-Setting-up-Zendesk-Chat).

### 3. Legal Notices in Ticket Forms

You can add disclaimers or links to your legal or privacy notices, directly within your ticket submission forms. Using the “End-user description” field, you can provide clear information about data handling practices before customers submit their requests.

*Learn more*: [Managing your ticket forms](../ticket-customization/managing-your-ticket-forms.md).

### 4. Cookie Consent Implementation in Your Help Center

If your Help Center uses cookies, you may need to implement cookie consent banners to comply with privacy laws. Zendesk supports adding cookie consent notices and obtaining user consent through customizable banners on your Help Center pages.

*Learn more:* [Implementing cookie consent in your help center](../setting-up-your-help-center/implementing-cookie-consent-in-your-help-center.md).

---

By leveraging these Zendesk features, you can efficiently provide legally required notices to help maintain compliance and build trust with your customers.

### Disclaimer

This article is for informational purposes only and does not constitute legal advice. Readers should always seek legal advice before taking any action with respect to the matters discussed herein.