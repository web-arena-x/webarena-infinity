# Disconnect a Connected Project

Source: https://v2.support.procore.com/product-manuals/connection-manager-project/tutorials/disconnect-a-connected-project

---

## Background

Procore Connect enables a connection between two separate Procore projects. The connection is one-way and copies published data from an upstream source project to a downstream connected project in an unpublished state.

Projects can be disconnected by either the upstream or downstream account at any time. Once disconnected, projects cannot reconnect.

## Things to Consider

- [Required User Permissions](/product-manuals/connection-manager-project/permissions)
- Admins' of the Connection Manager tool at either the upstream or downstream project can disconnect projects at any time.
- Once a downstream project disconnects from an upstream project, it is not able to reconnect to that same upstream project or establish new connections with any other upstream projects. This is a one-to-one termination that doesn't affect other downstream accounts connected to the project.
- When projects are disconnected, existing data remains available in the downstream account but no new information is copied from the upstream account.

## Disconnect Projects

## Steps

1. Navigate to the project's **Connection Manager** tool.
2. Next to the connection, click **Disconnect**.
3. Mark the checkbox to accept the terms.
4. Enter the reason you are disconnecting projects.
5. Click **Disconnect** to confirm.