# Initiate a Project Connection

Source: https://v2.support.procore.com/product-manuals/connection-manager-project/tutorials/initiate-a-project-connection

---

## Background

Procore Connect enables a connection between two separate Procore projects. The connection is one-way and copies published data from an upstream source project to a downstream connected project in an unpublished state.

Only the users at the downstream company account can initiate a connection. Upstream company accounts can choose to automatically approve connections, or require review to manually accept or reject a downstream project's request to connect. See [Configure Connection Approval Settings](/product-manuals/admin-company/tutorials/configure-connection-approval-settings). Projects can be disconnected by the upstream or downstream account at any time.

## Things to Consider

- [Required User Permissions](../permissions.md#:~:text=Initiate%20a%20Request%20to%20Connect%20Projects%0AWeb)
- Only the downstream company account can initiate a connection with an upstream account's project.
- A downstream project can only connect to one upstream project.
- For both upstream and downstream accounts, users on the Connection Manager tool email distribution list are notified of new connections and connection requests (if review is required). See [Connection Manager: Configure Advanced Settings](/product-manuals/connection-manager-project/tutorials/configure-advanced-settings-connection-manager).
- GovCloud accounts will not be able to participate in a project connection.

## Steps

1. Navigate to the project's **Connection Manager** tool.
2. Click **Connect**.
3. Select the upstream company and project. 
   *Note:* If you are connecting to a project within the *same* company, look for the 'Current Company' section in the 'Upstream Company' dropdown to select your company's name.
4. Click **Next**.
5. Select at least one feature for this connection, then click **Next**.
6. Review the Considerations, then click **Connect Projects** to initiate the project connection.

If the upstream company chose to automatically approve connections, your projects automatically connect. If the upstream company's settings require manual review for accepting or rejecting connections, Procore sends a request to the upstream company for review.