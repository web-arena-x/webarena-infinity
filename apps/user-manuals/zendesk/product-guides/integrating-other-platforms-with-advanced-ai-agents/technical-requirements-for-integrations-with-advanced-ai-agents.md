# Technical requirements for integrations with advanced AI agents

Source: https://support.zendesk.com/hc/en-us/articles/8357749781274-Technical-requirements-for-integrations-with-advanced-AI-agents

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **Add-on** | AI agents - Advanced |

AI agents - Advanced make server-to-server HTTP requests to your backend system. The requests are initiated when a user path triggers an integration node in their dialogue, and the mapped returned data is stored and available for the duration of the AI agents - Advanced session.

## Technical Requirements of your backend API

### API Types

Your API must be one of the following architectures:

- REST
- GraphQL

### Response

Your API response must follow the general requirements:

- Provide an API response within 30 seconds
- Preferably return JSON format

### Authentication

From AI agents - Advanced side, we can authenticate using any of the following:

- API key
- Bearer token
- Expiration token
- Basic auth
- OAuth 2.0
- IP safelists / allowlist

## Self Checklist

The self-checklist below contains questions and information that will help you build a robust API:

- Is the API "searchable" with data that a typical user would know, or with data passed through from your CRM?
- Does the data in the API response contain information that satisfies your use case?
- If your use case requires data from multiple systems, can you consolidate them into a middle layer?
- Is it known when the API throws a 200, a 400, and a 404 HTTP status code?
- What does the API return if the input is invalid or incorrect?
- Does your system set an API rate limit?
- How long does your system take to send a response?

#### Please be ready to provide: • Documentation: Auth, API request query / body and response schema • (Optionally a Postman collection.) • Test data for the most common outcomes.

Read more about the onboarding plan in the previous article, [Custom integration - preparation](https://support.zendesk.com/hc/en-us/articles/8357756827674).