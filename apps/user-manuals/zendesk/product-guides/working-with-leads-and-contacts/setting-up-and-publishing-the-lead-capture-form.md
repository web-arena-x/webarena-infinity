# Setting up and publishing the lead capture form

Source: https://support.zendesk.com/hc/en-us/articles/4408832077338-Setting-up-and-publishing-the-lead-capture-form

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

![Available on Sell Growth plans and above](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/plan_available_sell_pee.png)

You can capture leads directly into your sales funnel using a customizable embedded or hosted form. The data that is captured using this form is added as a new lead in your Zendesk Sell account.

There are two steps required to create a lead capture form. The first is to set up what you want on the form. The second is to publish the form.

This article covers the following topics:

- [Setting up a lead capture form](#topic_pyt_z23_ptb)
- [Publishing a lead capture form](#topic_h52_1f3_ptb)
- [Troubleshooting forms not rendering](#topic_gf1_njf_jvb)

## Setting up a lead capture form

You must be an admin to set up and publish the lead capture form.

**To create a lead capture form**

1. On the Sell sidebar, click **Settings** (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/settings_icon.png)).
2. Click [**Data > Lead capture > Lead capture form**](https://app.futuresimple.com/settings/lead_capture_form).

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sell_lead_capture.png)
3. On the **Fields** tab, define the data fields that you want to include on the form.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sell_leads_capture_fields_tab.png)
4. By default, the form contains the essential data fields you need to collect your lead data. Delete the fields that you're not going to use (Full name is the only required and non-deletable field). You can also rename fields, mark fields as required.
5. (Optional) To add custom fields, click **+Add Field**, enter the details for the field, and click **Add**.

   You can also change the order of the data fields by dragging and dropping the fields into the order you prefer.
6. Click **Preview** to see your changes, then click**Save**.
7. On the **Settings** tab, click the **Leads owner** dropdown menu to specify who you want the leads assigned to.
8. Click the **Form language** dropdown menu to specify which language the form is displayed in.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sell_leads_capture_settings_tab.png)

Note: If you’ve already set up and published a lead capture form, you can make updates to it here. There is only one version of the form. When it is changed, it is updated wherever it has been published.

## Publishing a lead capture form

You can publish your lead capture form, in two ways:

- You can generate embed code that you can add to any website.
- You can publish the lead capture form to a site that's hosted by Zendesk.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sell_leads_capture_publish_options_tab.png)

Note: You cannot change the design (colors and style) of the lead capture form. If you need more customization options to match your brand (for example), use the Zapier integration (see [Using Zapier with Zendesk Sell](https://support.zendesk.com/hc/en-us/articles/4408837805210)).

## Troubleshooting forms not rendering

If the embedded form does not render on your website it might be blocked by Content Security Policies (CSP) that were set up by your company. Ask your website administrator if you have a CSP in place, if yes, ask them to update it to allow the Capture form,

`script-src and iframe using frame-src for
<your-zendesk-subdomain>.zendesk.com`