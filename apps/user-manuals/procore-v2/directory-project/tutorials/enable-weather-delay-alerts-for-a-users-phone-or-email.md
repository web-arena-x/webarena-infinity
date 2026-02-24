# Enable Weather Delay Alerts for a User's Phone or Email

Source: https://v2.support.procore.com/product-manuals/directory-project/tutorials/enable-weather-delay-alerts-for-a-users-phone-or-email

---

##### Â In Beta

A redesigned version of the Project Directory is currently in beta and can be enabled with [Procore Explore](/product-manuals/admin-company/tutorials/manage-features-with-procore-explore).

## Background

When a user triggers a weather delay alert in Daily Log tool, the system sends alert messages.

- **Phone**: When the system sends a weather delay alert by phone, it dials the user's number. If the user answers, a robotic voice alerts them of the delay and identifies the project by name. If the user declines or misses the call, the system will leave a voicemail with the weather delay alert.
- **Email**: The system sends an email message to the address on the user's record.

When a weather delay is removed or canceled in the Daily Log too, no alerts are sent.

## Things to Consider

- [Required User Permissions](/product-manuals/directory-project/permissions)

## Prerequisites

- **For alerts settings to take effect:**

 - The Project level Daily Log tool must be enabled.   
    See [Add and Remove Tools on a Project](/product-manuals/admin-project/tutorials/add-and-remove-project-tools).
 - The Weather Log must be enabled in the Daily Log tool.
- **For a user to receive alerts:**

 - They must have a valid email address recorded in the Project Directory.
 - They must have a valid cellular telephone number recorded in the Project Directory.
- **To trigger a weather delay alert:** A weather delay must be added to the Weather Log in the Project level Daily Log tool.   
 See [Create Observed Weather Log Entries](/product-manuals/daily-log-project/tutorials/create-observed-weather-entries).

## Steps

1. Navigate to the Project level **Directory** tool.
2. Click the **Users** tab.
3. Locate the person, then click **Edit**. 
   ORClick the **person's name.**
4. Under 'General Information, ensure the relevant field has a valid entry for the user to receive alerts:

   - **Email Address**
   - **Cell Phone**
5. Mark the following checkboxes under 'Default Email Notifications' to enable the alert:

   - **Weather Delay (via email)**
   - **Weather Delay (via phone)**
6. Click **Save**.