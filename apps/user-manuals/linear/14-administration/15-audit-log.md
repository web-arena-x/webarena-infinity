# Audit log

Audit logs show you a record of workspace events over the last 90 days.

> [!NOTE]
> Available to workspaces on our [Enterprise](https://linear.app/pricing) plan

![Audit log page in Linear](https://webassets.linear.app/images/ornj730p/production/9d0afc74a9a0ed53d8370f87cb109ea4eb297125-2160x1327.png?q=95&auto=format&dpr=2)

## Overview

Linear automatically tracks events related to account access, subscriptions, and settings changes including the IP and country of the actor. All audit logs are retained for 90 days. You can browse recent events and filter them by event type. For more complex queries, we recommend you access the audit log through the API.

## Configure

Only workspace owners can access audit logs given the sensitive nature of the information. You can find them under [**Workspace Settings > Administration > Audit Log**](https://linear.app/settings/audit-log) 

## Access via API

To perform complex queries based on type, actor, and other metadata, we recommend that you access the audit log through [Linear's GraphQL API](https://developers.linear.app/docs/graphql/working-with-the-graphql-api). Visit our [API documentation](https://linear.app/docs/api-and-webhooks) to read more about making GraphQL API requests.

```text
# Simple query to get last 250 events
query {
 auditEntries(first: 250) {
    nodes {
      id
      type
      createdAt
      actor {
        id
        name
      }
      metadata
    }
 }
}
```

You can utilize the advanced filtering capabilities of our API to narrow down your query.

```text
# Get login events for an user
query {
	auditEntries(filter: {type: {eq: "login"}, actor: {email: {eq: "user@company.app"}}}) {
	 nodes {
	    id
	    type
	    createdAt
	    actor {
	      email
	    }
			ip
	    metadata
	 }
	 pageInfo {
	    endCursor
	    hasNextPage
	 }
	}
}
```

You can also get the list of all the available log entry types from our API.

```text
query {
 auditEntryTypes {
    type
    description
 }
}
```

### Webhook and SIEM support

Audit logs can be streamed to a webhook and configured for SIEM data ingestion. To enable the audit log webhook, visit the [Audit Log](https://linear.app/settings/audit-log) under workspace settings and enable **Stream logs.** To learn more about securing your webhook using a signing secret, visit our [API documentation](https://developers.linear.app/docs/graphql/webhooks#securing-webhooks).

#### Sample responses

User joins a team:

```json
{
 "action": "create",
 "actor":
    {
      "id": "8e03f2cf-e644-4d68-a7cc-f834ad2f43b4",
      "name": "Miha Rebernik",
      "email": "miha@linear.app",
      "avatarUrl": "https://public.linear.dev/8e03f2cf-e644-4d68-a7cc-f834ad2f43b4/d3c0a4bf-51a7-41cc-ade7-0f61f9d4f886",
      "type": "user",
    },
 "createdAt": "2025-03-28T19:46:01.382Z",
 "data":
    {
      "id": "4b0186dc-a464-4330-9d4b-f4fc8f01db5b",
      "createdAt": "2025-03-28T19:46:01.382Z",
      "type": "userJoinedTeam",
      "organizationId": "5a3b982d-8f04-4971-956c-fbcb2c68642a",
      "actorId": "8e03f2cf-e644-4d68-a7cc-f834ad2f43b4",
      "metadata":
        {
          "teamName": "New team",
          "teamKey": "NEW",
          "teamId": "7586c601-2c9f-4764-bbc5-6132791c68c9",
          "owner": false,
        },
      "requestInformation": {},
    },
 "type": "AuditEntry",
 "organizationId": "5a3b982d-8f04-4971-956c-fbcb2c68642a",
 "webhookTimestamp": 1743191166416,
 "webhookId": "f1d0caa0-a974-4604-a300-a4edbba66803",
}
```

A webhook is created:

```json
{
 "action": "create",
 "actor": {
    "id": "8e03f2cf-e644-4d68-a7cc-f834ad2f43b4",
    "name": "Miha Rebernik",
    "email": "miha@linear.app",
    "avatarUrl": "https://public.linear.dev/8e03f2cf-e644-4d68-a7cc-f834ad2f43b4/d3c0a4bf-51a7-41cc-ade7-0f61f9d4f886",
    "type": "user"
 },
 "createdAt": "2025-03-28T19:46:18.441Z",
 "data": {
    "id": "e78bfecd-53a6-4197-8a71-f614b187553a",
    "createdAt": "2025-03-28T19:46:18.441Z",
    "type": "webhookCreated",
    "organizationId": "5a3b982d-8f04-4971-956c-fbcb2c68642a",
    "actorId": "8e03f2cf-e644-4d68-a7cc-f834ad2f43b4",
    "ip": "::ffff:127.0.0.1",
    "metadata": {
      "id": "53188995-5f3b-44a9-993b-9bb0d37136a5",
      "url": "https://webhook.site/399c1880-02e6-4a2b-8b62-6f2ea5c8cc7e/123",
      "label": "A new webhook",
      "enabled": true,
      "resourceTypes": ["Issue"],
      "allPublicTeams": true
    },
    "requestInformation": {
      "userAgent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36",
      "authMethod": "jwt",
      "authService": "google"
    }
 },
 "type": "AuditEntry",
 "organizationId": "5a3b982d-8f04-4971-956c-fbcb2c68642a",
 "webhookTimestamp": 1743191178476,
 "webhookId": "f1d0caa0-a974-4604-a300-a4edbba66803"
}
```
