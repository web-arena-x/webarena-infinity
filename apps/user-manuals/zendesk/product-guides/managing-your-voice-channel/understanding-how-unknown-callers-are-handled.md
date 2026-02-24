# Understanding how unknown callers are handled

Source: https://support.zendesk.com/hc/en-us/articles/4408845588250-Understanding-how-unknown-callers-are-handled

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support with** | Talk Team, Professional, or Enterprise |

When a call is received, the phone number of the incoming call is automatically associated with an end user in Zendesk, then a ticket is created with that user as the requester. If the user doesn't exist, a new user is created and named with the phone number of the incoming call. See [Understanding how calls become tickets](https://support.zendesk.com/hc/en-us/articles/4408821302810).

Sometimes, incoming calls will come from a blocked number or from a number where the caller ID is hidden. These calls and tickets are handled just the same as calls that come in from unrecognized numbers by creating a new user.

This article contains the following sections:

- [How unknown callers are handled](#topic_n3s_wmg_mmb)
- [Best practices for managing unknown callers](#topic_hmz_wmg_mmb)

## How unknown callers are handled

When a call comes in from an unknown number, the agent follows the same process as for any other call (see [Receiving incoming calls](https://support.zendesk.com/hc/en-us/articles/4408821359002)).

Note: When calls come in from a digital line, the requester is currently always added as Caller Unknown. For more information about digital lines, see [Understanding Embedded voice](https://support.zendesk.com/hc/en-us/articles/4408830696090).

When a call from an unknown number is received, the following happens:

1. A new, unique user is created in Zendesk.
2. A ticket is created with the new user as the requester.

For help managing these new users, see [Best practices for managing unknown callers](https://support.zendesk.com/hc/en-us/articles/4408845588250#topic_hmz_wmg_mmb).

## Best practices for managing unknown callers

If you get a lot of calls from unknown numbers, you might end up with a large number of unknown end users being created in Zendesk. Here are some best practices that can help you manage these users:

- As your agents work on tickets from unknown callers, try to identify the caller, then change the ticket requester to the identified user (if that user already exists) or update the unknown user’s attributes with the caller’s details.
- End users will become ‘orphaned’ if they have no attributes or tickets associated with the user. This will happen if your agents reassign the ticket from the caller to an existing user profile. It’s good practice to have your agents delete these end users at the point where they assign the ticket to the correct end user.
- Occasionally, work through your list of unknown users and delete ones that you know you don't need. This will help prevent the list from becoming too unmanageable.