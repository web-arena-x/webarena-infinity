# How to Configure Cases (Engage Legacy)

Source: https://support.zendesk.com/hc/en-us/articles/9731462374170-How-to-Configure-Cases-Engage-Legacy

---

Cases are configured in Amazon Connect and enabled in Engage.

## Prerequisites

Before delving into the configuration within Engage, there are certain requirements you need to have in place:

1. CF Template Update: Ensure your CF template is updated to version v20221013 or newer.
2. Cases Domain Configuration: This must be set up within Amazon Connect.
3. Case Fields & Templates: These should also be pre-configured in Amazon Connect.
4. Enable Cases Feature: This needs to be activated within the Connect settings.

Please see the [official AWS documentation](https://aws.amazon.com/blogs/contact-center/simplify-case-management-in-your-contact-center-using-amazon-connect-cases/) for more detailed information on configuration of Cases domain, fields and templates.

## Enable Cases in Engage

Once the above steps are completed, Cases can be enabled in Engage. Navigate to Engage Admin settings and under General Settings select Local Measure Features > Edit settings. Toggle the button under Connect Cases to enable the feature and select Save.

![](https://support.zendesk.com/hc/article_attachments/9731449919002)

‍