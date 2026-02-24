# Ensuring dark mode compatibility for your Zendesk Support apps

Source: https://support.zendesk.com/hc/en-us/articles/9257152764570-Ensuring-dark-mode-compatibility-for-your-Zendesk-Support-apps

---

**Audience:** This article is for Zendesk customers using Support apps.

As Zendesk supports dark mode, it's important that the apps you use also support it to maintain a consistent and visually comfortable workspace. If an app doesn’t support dark mode, it may appear with bright or mismatched visuals that can be distracting or harder to use.

This article will help you understand what steps to take based on how your app was created or acquired.   
  
This article includes these sections:

- [Scenario 1: App installed from the Zendesk Marketplace](#h_01JV8EXH7Y7PHNW3CBPFGACJQJ)
- [Scenario 2: App developed internally by your team](#h_01JV8EXH81B8NJ6T79GCA2S7WB)
- [Scenario 3: App built by Zendesk Professional Services](#h_01JV8EXH845QGQ5RAVKXG5E84Z)
- [Additional tips](#h_01JV8EXH87RJFW50N7K2CKJ65A)

## Scenario 1: App installed from the Zendesk Marketplace

**What to do**  
If you installed the app from the Zendesk App Marketplace, the responsibility for dark mode support lies with the app developer.

**Steps to take**

1. Visit the app’s page in the marketplace.
2. Scroll to find the **“Contact Us”** link.
3. Reach out to the developer to request dark mode support or inquire about planned updates.

Tip: When contacting the developer, mention
your current Zendesk theme setting (light or dark) and share screenshots
if possible. This helps them prioritize and troubleshoot effectively.

## Scenario 2: App developed internally by your team

**What to do**  
Your internal development team will need to update the app to support dark
mode using Zendesk’s development guidelines.

**Steps to take**

1. Direct your developers to
   [Supporting dark mode](https://developer.zendesk.com/documentation/apps/app-developer-guide/dark-mode/)
   in the Zendesk developer documentation.
2. Ensure the app uses the latest version of the
   [Zendesk Garden design system](https://garden.zendesk.com/),
   which includes built-in support for dark mode.

If your app doesn't use the Garden component, you can import
`@zendeskgarden/react-theming` from Garden to access the full
color theme.

Tip: Ask your developers to test the app
in both light and dark modes to ensure proper behavior before deploying
changes.

## Scenario 3: App built by Zendesk Professional Services

**What to do**  
Zendesk Professional Services builds custom apps for customers. If they
created your app, they can help update it for dark mode.

**Steps to take**

1. Reach out to your Zendesk account representative or customer success
   manager.
2. Mention that you’re using dark mode and would like assistance with
   updating your custom app.

Tip: If you’re unsure whether Zendesk
built the app, check your project documentation or reach out to Zendesk
support for clarification.

## Additional tips

- **How do I know if an app supports dark mode?** Switch
  the profile menu of your Zendesk instance to dark mode and
  observe the app's appearance. If the app looks out of place
  (for example, overly bright or unreadable), it likely doesn't
  support dark mode.
- **Can I force dark mode in an unsupported app?** Not
  reliably. If an app isn’t designed for dark mode, forcing
  dark styles may cause functionality or visibility issues.
- **Still not sure who built the app?** Visit
  the
  **Admin Center > Apps and Integrations > Apps** page.
  The app name and configuration details can help identify
  whether it's installed from the Marketplace, built internally,
  or built by Zendesk.