# Exporting data from Zendesk QA

Source: https://support.zendesk.com/hc/en-us/articles/7043724806810-Exporting-data-from-Zendesk-QA

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **Add-on** | Quality Assurance (QA) or Workforce Engagement Management (WEM) |

This article describes how to export data from Zendesk QA using the API. Exporting data allows you to analyze and review customer interactions outside of the Zendesk QA platform.

Admins and Account Managers can set up an API connection in Zendesk QA.

This article contains the following sections:

- [Setting up an API connection](#setting-up-api-connection)
- [Exporting data with API](#exporting-data-with-api)
- [Response structure](#response-structure)

## Setting up an API connection

To export data, you first need to set up an [API connection](https://support.zendesk.com/hc/en-us/articles/7043669282714) in your Zendesk QA account. You will need the API token, account ID, and workspace ID from that step to continue.

## Exporting data with API

The [Zendesk QA (formerly Klaus) Public Export API reference guide](https://pub.klausapp.com/?urls.primaryName=Public%20Export%20API#/PublicExportApi/PublicExportApi_AccountReviewsV2API) lists the available exportable data. Data related to reviews can be exported, excluding [voice transcripts](https://support.zendesk.com/hc/en-us/articles/8536308081178), [AutoQA data](https://support.zendesk.com/hc/en-us/articles/7043747123354), and [data from dashboards](https://support.zendesk.com/hc/en-us/articles/7043701144858).

**To export data using the API**

1. Acquire the API token, account ID, and workspace ID from your API connection setup.
2. Make a GET request to `/qa/api/export/workspace/11759/reviews` by setting the token as a Bearer token in the **Authorization** header.

An example request with `curl` would look like this:

```
curl 'https://yoursubdomain.zendesk.com/qa/api/export/workspace/reviews?fromDate=2020-01-01T00%3A00%3A00%2B00%3A00&toDate=2020-03-31T00%3A00%3A00' \
  -H 'accept: application/json' \
  -H 'Authorization: Bearer YOUR_API_TOKEN'
```

- For an account-wide export, you can use our `/qa/api/export/reviews` endpoint.
- Both endpoints also accept `page` and `pageSize` parameters for pagination.

## Response structure

## The structure of the response:

```
{
  "conversations": [
    {
      "externalId": "string",
      "url": "string",
      "externalUrl": "string",
      "lastUpdated": "string",
      "reviews": [
        {
          "id": "string",
          "reviewer": {
            "email": "string",
            "name": "string",
            "avatar": "string"
          },
          "reviewee": {
            "email": "string",
            "name": "string",
            "avatar": "string"
          },
          "score": 0,
          "ratings": [
            {
              "categoryId": "string",
              "categoryName": "string",
              "score": 0,
              "weight": 0,
              "critical": true,
              "cause": "string"
            }
          ],
          "comment": "string",
          "thread": [
            {
              "id": "string",
              "owner": {
                "email": "string",
                "name": "string",
                "avatar": "string"
              },
              "comment": "string",
              "created": "string",
              "updated": "string",
              "thread": [
                "string"
              ],
              "tags": [
                {
                  "tag": "string",
                  "user": {
                    "email": "string",
                    "name": "string",
                    "avatar": "string"
                  }
                }
              ]
            }
          ],
          "tags": [
            {
              "tag": "string",
              "user": {
                "email": "string",
                "name": "string",
                "avatar": "string"
              }
            }
          ],
          "created": "string",
          "updated": "string",
          "received": true,
          "reviewTime": "string",
          "scorecard": {
            "id": "string",
            "name": "string"
          }
        }
      ],
      "comments": [
        {
          "id": "string",
          "owner": {
            "email": "string",
            "name": "string",
            "avatar": "string"
          },
          "comment": "string",
          "created": "string",
          "updated": "string",
          "thread": [
            "string"
          ],
          "tags": [
            {
              "tag": "string",
              "user": {
                "email": "string",
                "name": "string",
                "avatar": "string"
              }
            }
          ]
        }
      ],
      "workspaceId": "string"
    }
  ],
  "pagination": {
    "page": 0,
    "pageSize": 0,
    "total": 0
  }
}
```

Note: `externalId` in [Zendesk QA's Public Export API reference guide](https://pub.klausapp.com/?urls.primaryName=Public%20Export%20API) corresponds to the `ticket_id` ID in [Zendesk Support](https://developer.zendesk.com/api-reference/ticketing/tickets/tickets/#parameters-1).