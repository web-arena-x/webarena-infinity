# View App Management Metrics

Source: https://v2.support.procore.com/product-manuals/admin-company/tutorials/admin-view-app-management-metrics

---

## Background

As a Procore company administrator, you have the ability to view App Management Metrics for a given App across all projects and users in a company.

## Things to Consider

- **Required User Permissions:**

 - 'Admin' level permissions on the company's Directory tool.
- **Data Availability:**

 - Data connection and embedded App usage metrics will not be immediately available in App Management Metrics, and could take up to 24 hours to appear.
- **Applications Not Supported:**

 - App Management Metrics for the [Zoom](https://support.procore.com/integrations/zoom), [Meetings with Microsoft Teams](https://support.procore.com/integrations/meetings-with-microsoft-teams), and [Meetings with GoToMeeting](https://support.procore.com/integrations/go-to-meeting) integrations are currently not supported.

## Steps

1. Navigate to the company's **Admin** tool.
2. Under 'Company Settings', click **App Management**.

       

   Each installed App is shown with information for 'Name', 'Publisher', 'Installed By', and 'Installed On'. 'Installed By' shows the last user that installed or reinstalled the App. 'Installed On' shows the last date the App was installed or reinstalled.
3. Locate the App you want to view App Management Metrics for and click its **View** button.

       

   General information about the App is presented on the App Info tab. You can also view the list of projects the App is being used in, as well as the date the App was last used in a project. See [View Information about an Installed App](/product-manuals/admin-company/tutorials/view-information-about-installed-app) for additional information.
4. Click the 'Usage' tab. Daily API request totals for the past two-week period are plotted on a graph. [Note: For embedded Apps, these data represent instances of project users launching the App in the Embedded Experience from the Procore user interface.] Also shown is a list of all App users. Each user entry can be expanded to show which projects they use the App in, and the last date they used them. Items denoted as '--' indicate App usage at the company level.

##### Â Note

- At least two days' worth of data must exist in order for plotted data points to be visible in the graph.
- If no calls to the Procore API have been made by an App (or embedded use) in more than a two-week period, the graph will be empty.

##### Â Tip

Use the Projects drop-down to filter the data for one or more individual projects.