# API and Webhooks

Linear's GraphQL API and webhooks lets you extend Linear's functionality beyond what we provide out of the box. 

![Linear logo and a logo representing the API](https://webassets.linear.app/images/ornj730p/production/c944abb65e6b46b14d2666d88f8d390699ffd265-2880x1620.png?q=95&auto=format&dpr=2)

## Overview

Linear's public API is built using GraphQL. It's the same API we use internally for developing our applications.

Linear's webhooks allow you to receive HTTP(S) push notifications whenever data is created or updated. This allows you to build integrations on top of Linear. 

## Basics

### API

You own your data in Linear and our GraphQL API lets you query that data. In addition to querying, Linear has full support for mutating all entities. Any mutations you make via the API are observed in real-time by all clients.

Go to the API section under Account > Security & Access[ settings](https://linear.app/settings/account/security) and read the linked [API documentation](https://developers.linear.app/docs/graphql/working-with-the-graphql-api) for more information. Our GraphQL schema is available [here](https://studio.apollographql.com/public/Linear-API/variant/current/schema/reference).

> [!NOTE]
> For more in depth documentation visit [developers.linear.app](https://developers.linear.app/docs/). If you have a question the docs don't answer, post it in the #api channel in our [Slack community](https://linear.app/join-slack).

### API Keys

Admins can choose whether or not Members can create their own API keys from _Settings > Administration > API > Member API keys._ This setting will not apply to Admins who can always create API keys.

![Member API Key permission toggle](https://webassets.linear.app/images/ornj730p/production/91976e7722c04bf16f048765228587c090b0bd96-974x303.png?q=95&auto=format&dpr=2)

Existing API keys for your workspace can be viewed from the same menu and revoked if needed. 

Admins and permitted Members can create personal API keys from _Settings > Account > Security & Access._ For each key you create, you can choose to give it full access to the data your user can access, or restrict it to certain permissions (_Read, Write, Admin, Create issues, Create comments)._ You can also limit an API key's access to specific teams in your workspace.

### Webhooks

Our webhooks support data change events for Issues, Comments, Issue attachments, Documents, Emoji reactions, Projects, Project updates, Cycles, Labels, Users and Issue SLAs.

Consider using webhooks to trigger CI builds, perform calculations on issue data or send messages on specific conditions. Creating and managing webhooks requires admin permissions. Read more in our [webhook documentation](https://linear.app/developers/webhooks).

The configured URL will be called whenever any issue or comment in that team is created or updated. You'll receive the entire data object as the payload. We'll also let you know what the previous values for all changed properties were.

### Create a webhook

Create and manage webhooks and OAuth applications in _Settings > Administration > API._ Admin permissions in your workspace are necessary to view this page.

### Third-party apps

Third-party integrations created for Linear can be found on our [integrations directory.](https://linear.app/integrations)
