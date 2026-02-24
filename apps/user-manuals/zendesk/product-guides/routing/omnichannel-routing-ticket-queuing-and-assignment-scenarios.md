# Omnichannel routing ticket queuing and assignment scenarios

Source: https://support.zendesk.com/hc/en-us/articles/6083625616666-Omnichannel-routing-ticket-queuing-and-assignment-scenarios

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

Location:  Admin Center > Objects and rules > Omnichannel routing > Routing configuration

This article describes many common scenarios to help you understand how [omnichannel routing](https://support.zendesk.com/hc/en-us/articles/4409149119514) queues and assigns tickets.

#### Select a scenario to view it:

- [Agents are offline or at capacity](#01H7XJ4QW66QNZF5M76FXMNRY8)
- [Two agents are online](#01H7XJGV1WG1YP2BAGA449AGDK)
- [An agent marks an assigned ticket as solved](#01H7XJGV1WTDQ2END6XNZW3JTD)
- [A customer responds to a solved ticket](#01H7XJGV1WXH932AXW24CNT5W6)
- [An agent assigns an active conversation to another agent](#01H7XJGV1WKN6YV3R65N5S1DQH)
- [An agent is offered a message but doesn't accept it](#h_01H8YTBSDY0XHETWW9D1JJBYWJ)
- [A conversation becomes inactive while in the queue](#01H7XJGV1W8MQ077NFH8XF1472)
- [A conversation becomes inactive while assigned to an agent](#01H7XJGV1WRQYD42SZJ9KCJ34H)
- [An email with the auto-route tag is received, and two agents are online](#01H8MT1AKH8YVJXQTY6TBXW4C5)
- [A voice call is received, and two agents are online](#01H8MT236NWY8AV8DX0R3G2Q2F)
- [An agent declines a voice call](#01H8MT2WDXX77VG6Q4EB490TXR)

### Agents are offline or at capacity

|  |  |
| --- | --- |
| A new message is received and added to the top of the queue.  Another new message is received and added to the queue below the existing message because messages of the same priority are ordered by the time received (oldest at the top).  A new urgent priority message is received, which goes to the top of the queue as messages are ordered by priority in the queue (urgent at the top).  Routing based on priority is only available on Suite Professional and above. |  |

### Two agents are online

|  |  |
| --- | --- |
| The message at the top of the queue is offered to Agent 1 (the agent who has been inactive the longest.)  Agent 1 accepts the message.  The next message in the queue is offered to Agent 2 (the agent with the most free capacity.)  Agent 2 accepts the message.  The next message in the queue is offered to Agent 1 (both agents have the same free capacity, but Agent 1 has been inactive the longest.)  Agent 1 accepts the message. |  |

### An agent marks an assigned ticket as solved

|  |  |
| --- | --- |
| When an assigned ticket is marked as solved, it no longer counts toward an agent’s capacity.  The solved ticket is still be assigned to the agent  Marking a ticket as Pending, On-Hold, or a custom state based on those ticket status categories has the same effect. |  |

### A customer responds to a solved ticket

|  |  |
| --- | --- |
| If a customer believes their issue isn’t solved and responds, the agent currently assigned to the ticket receives a notification, and the ticket status changes to Open. This message will now count against their capacity.  If an agent reassigns the ticket back to the group, for example if they are going offline for an extended period, then when a response comes in, omnichannel routing routes the ticket to an alternative agent in the group. |  |

### An agent assigns an active conversation to another agent

|  |  |
| --- | --- |
| Agent 2 comes online and there are no messages in the queue.  Agent 1 decides to assign her lower priority conversation to Agent 2 who receives a notification that this has happened. |  |

### An agent is offered a message but doesn't accept it

|  |  |
| --- | --- |
| A new message arrives, is placed in the queue and offered to Agent 1.  Agent 1 doesn’t accept the message within the reassignment time, so the message is offered to Agent 2.  Agent 2 accepts the message. |  |

### A conversation becomes inactive while in the queue

|  |  |
| --- | --- |
| A conversation might become inactive during, for example, outside of business hours or during a spike in calls.  If a customer waits in the queue for over ten minutes, their conversation becomes inactive.  At this stage, the conversation remains in the queue because no agent has any free capacity.  When an agent comes online or frees up some capacity, they are assigned this conversation and receive a notification.  Depending on your [routing configuration](https://support.zendesk.com/hc/en-us/articles/4828787357210), all inactive messages could be assigned to the first available agent as they do not affect capacity. |  |

### A conversation becomes inactive while assigned to an agent

|  |  |
| --- | --- |
| If a customer is inactive for more than 10 minutes, the conversation becomes inactive  At this stage, the conversation remains assigned to Agent 1 but no longer counts toward their capacity  If the conversation becomes active again, Agent 1 receives a notification, and the conversation counts against their capacity again  If an inactive conversation assigned to an agent becomes active again when the agent is at capacity, they will go over their capacity threshold and not be served messages until they are within it again. |  |

### An email with the auto-route tag is received, and two agents are online

|  |  |
| --- | --- |
| An email is received, gets added to the top of the queue, and is automatically assigned to Agent 1 (the agent who has been inactive the longest).  Another email is received, gets added to the top of the queue, and is automatically assigned to Agent 2 (the agent with the most free capacity)  A third email is received, gets added to the top of the queue, and is automatically assigned to Agent 1 (both have the same free capacity; Agent 1 hasn’t received an email for the longest time). |  |

### A voice call is received, and two agents are online

|  |  |
| --- | --- |
| A call is received and is offered to Agent 1 (the agent who has been inactive the longest).  Agent 1 accepts it, and the ticket is assigned to them.  Another call is received and is offered to Agent 2 (the agent with the most free capacity).  Agent 2 accepts the call, and the ticket is assigned to them.  Another call is received. Since both agents are busy, the caller waits for the defined call wait time for an agent to become available. If no agent is available, the call goes to voicemail. |  |

### An agent declines a voice call

|  |  |
| --- | --- |
| A call is received and is offered to Agent 1 (the agent who has been inactive the longest.)  Agent 1 declines the call.  The call is then offered to Agent 2.  Agent 2 accepts the call, and the ticket is assigned to them. |  |

## Further reading

- [Omnichannel routing resources](https://support.zendesk.com/hc/en-us/articles/5061050408730)