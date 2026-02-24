# Approve or Reject Project Connection Request

Source: https://v2.support.procore.com/product-manuals/connection-manager-project/tutorials/approve-or-reject-project-connection-requests

---

## Background

Procore Connect enables a connection between two separate Procore projects. The connection is one-way and copies published data from an upstream source project to a downstream connected project in an unpublished state.

Upstream company accounts can choose to automatically approve connections, or require review to manually accept or reject a downstream project's request to connect. See [Configure Connection Approval Settings](/product-manuals/admin-company/tutorials/configure-connection-approval-settings). Follow these steps if you chose to review and manually accept each connection.

## Things to Consider

- [Required User Permissions](/product-manuals/connection-manager-project/permissions)
- If you reject a request by mistake, the project can request a connection again that you can review and approve.
- An upstream project can support connections with multiple downstream projects. For example, multiple subcontractor companies (downstream) projects can connect to a single general contractor (upstream) project and receive data.
- For both upstream and downstream accounts, users on the Connection Manager tool email distribution list are notified of new connections, disconnections, and connection requests (if review is required). See [Connection Manager: Configure Advanced Settings](/product-manuals/connection-manager-project/tutorials/configure-advanced-settings-connection-manager).
- Projects can be disconnected by the upstream or downstream account at any time. See [Disconnect Connected Projects](/product-manuals/connection-manager-project/tutorials/disconnect-a-connected-project).

## Connect Projects for Downstream Companies

## Steps

1. Navigate to the project's **Connection Manager** tool.
2. Under 'Downstream Projects' click **Review Request**.
3. Do one of the following:

   1. Click **Approve** to approve the connection.
   2. Click **Reject** to decline the connection.