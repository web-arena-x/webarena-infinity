# Best practices for creating use cases for advanced AI agents

Source: https://support.zendesk.com/hc/en-us/articles/8357733365402-Best-practices-for-creating-use-cases-for-advanced-AI-agents

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **Add-on** | AI agents - Advanced |

Use cases are the mechanism by which [zero-training AI agents](https://support.zendesk.com/hc/en-us/articles/8357749447194) and [AI agents that use agentic AI](https://support.zendesk.com/hc/en-us/articles/8966284087066) understand what a customer is
asking about and connect them with the right [dialogue](https://support.zendesk.com/hc/en-us/articles/8357749494810) or [procedure](https://support.zendesk.com/hc/en-us/articles/8979864563610).

A use case’s name and description provide the necessary context for an AI agent to
understand the customer’s messages and connect them with the right dialogues to help
them. As such, it’s important to write clear and specific use case names and
descriptions in order to get the best performance possible from your AI agent.

This article contains the following topics:

- [Best practices for use case descriptions](#topic_t1g_sd4_s2c)
- [Best practices for use case names](#topic_bvf_k2r_mdc)
- [Use case examples for different industries](#topic_hhc_n2r_mdc)

Related articles:

- [Creating use cases for advanced AI agents to
  identify what customers are asking about](https://support.zendesk.com/hc/en-us/articles/9041901679130)
- [Managing use cases for advanced AI
  agents](https://support.zendesk.com/hc/en-us/articles/9041911005850)

## Best practices for use case descriptions

When creating use case descriptions, keep the following best practices in mind:

- Write use case descriptions in English.
- Start all of your use cases in a consistent way (for example, “Customer wants
  to…”).
- Avoid including keywords in the description.
  - **Do this:** Customer wants to schedule a collection for their return
  - **Don’t do this:** Customer wants to schedule a collection for their
    return. Keywords: pick-up, collection
- Write descriptions that are concise (around 120 characters, including spaces)
  yet detailed enough to connect the customer to the right dialogue.
- Avoid acronyms, or write the acronyms to provide additional context.
  - **Do this:** Customer requests do it yourself instructions
  - **Don’t do this:** Customer requests DIY instructions
- Create distinct use cases and ensure they don’t overlap. Overlapping use cases
  cause confusion and worse results in the AI model.
- Don’t create use cases for small talk or for recognizing a specific
  language.

## **Best practices for use case names**

When creating use case names, keep the following best practices in mind:

- Write use case names in English.
- Keep names short, ideally 3-5 words.
  - **Do this:** Username or password change
  - **Don’t do this:** How do I change my username or password?
- Choose names that are as clear as possible.
- Avoid any punctuation except commas.
  - **Do this:** Issues with Klarna
  - **Don’t do this:** Issues - Klarna

## **Use case examples for different industries**

The tables below collect well-performing use case names and descriptions for various
industries. Feel free to use these in your own AI agent.

|  |  |  |
| --- | --- | --- |
| **Use case name** | **Description** | **Insights and tips** |
| **General industry** | | |
| Refund status | Customer asks for an update on the status of their refund |  |
| Login issues | Customer can’t log in due to incorrect password or username | In this use case, “login issues” and “password reset” have been merged together due to semantic similarities with customers having trouble logging in. |
| Update account information | Customer asks how to update personal or account information | Most often, customers want to update either their personal details (name, phone) or account information (delivery, billing address). Due to semantic similarities, these topics have been merged. |
| Payment methods | Customer wants to know what payment methods are supported |  |
| Email confirmation | Customer didn’t receive an email confirmation for their order | This use case can be adjusted according to your use case (for example, order, booking, etc.). |
| **E-commerce industry** | | |
| Order status | Customer wants to know the status of their order |  |
| Lost order | Customer hasn’t received their order despite delivery |  |
| Sizing enquiries | Customer asks about product sizing | This can be further iterated to be more product-category-specific, like shoe or clothing sizing. |
| Incorrect item received | Customer claims they received an item they did not order |  |
| Return request | Customer wants to return their order, or part of their order |  |
| **Travel industry** | | |
| Cancel booking | Customer requests to cancel their booking | The use case name and description are unified and not overly lengthy. It clearly expresses the user's desire to cancel their booking. |
| Changes to booking | Customer wants to change the date, destination or departure for their booking. | This use case covers three different changes: arrival, departure, and date for travel. Customers can change these details themselves depending on their ticket type, whereas a name change would require agent attention, which is why that’s covered in a different use case (below). |
| Change the name on booking | Customer needs to change the name on their booking | As mentioned above, this use case has been excluded from the more general “Changes to booking” use case as they’re semantically different enough, and we were able to write clear names and descriptions without strong confusion. |
| Recommendations for activities | Customer wants to know what activities are available at their location |  |
| **Financial services industry** | | |
| Status of transfer | Customer needs information on the status of their money transfer | Customer has concerns about whether the recipient has received a money transfer, and wants to check the status of it. This use case doesn't cover lost or unsuccessful transfers, as these are covered in a separate use case (below). |
| Unsuccessful transfer | Customer is concerned about a money transfer that didn’t reach the recipient | As mentioned above, this use case covers instances where a money transfer has been made but never arrived at the recipient account. |
| Card activation issues | Customer expresses issues with credit card activation |  |
| Failed payment | Customer wants to understand why their card payment failed |  |