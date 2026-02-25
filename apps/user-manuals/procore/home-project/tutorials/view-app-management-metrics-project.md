# View App Management Metrics in a Project

Source: https://v2.support.procore.com/product-manuals/home-project/tutorials/view-app-management-metrics-project

---

## Background

As a project user, you can view App Management Metrics for a given App within a project. The data presented are scoped to the current project.

## Things to Consider

- **Required User Permissions**:

 - 'Read-only' or higher on the Portfolio tool.
- **Data Availability:**

 - Data connection and embedded App usage metrics will not be immediately available in App Management Metrics, and could take up to 24 hours to appear.
- **Applications Not Supported:**

 - App Management Metrics for the [Zoom](https://support.procore.com/integrations/zoom), [Meetings with Microsoft Teams](https://support.procore.com/integrations/meetings-with-microsoft-teams), and [Meetings with GoToMeeting](https://support.procore.com/integrations/go-to-meeting) integrations are currently not supported.

## Steps

1. Navigate to the project you want to view App Management Metrics in.
2. In the top navigation bar, open the **Apps** dropdown menu and click **App Management**.

1. Locate the App you want to view App Management Metrics for and click its **View** button.

1. Click the 'App Info' tab. General information about the App is presented on the App Info tab. See [View Information about an Installed App](/product-manuals/admin-company/tutorials/view-information-about-installed-app) for more information.

1. Click the 'Usage' tab.

1. Daily API request totals for the past two-week period for the selected project are plotted on a graph. [Note: For embedded Apps, these data represent instances of project users launching the App in the Embedded Experience from the Procore user interface.]

##### Â Note

- At least two days' worth of data must exist in order for plotted data points to be visible in the graph.
- If no calls to the Procore API have been made by an App (or embedded use) in more than a two-week period, the graph will be empty.