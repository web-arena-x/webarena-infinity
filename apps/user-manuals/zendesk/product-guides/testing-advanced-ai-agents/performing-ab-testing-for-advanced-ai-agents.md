# Performing A/B testing for advanced AI agents

Source: https://support.zendesk.com/hc/en-us/articles/8357758896410-Performing-A-B-testing-for-advanced-AI-agents

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **Add-on** | AI agents - Advanced |

A/B testing is a mechanism that empowers a separation of visitors to differentiate the experience. A/B testing helps you understand the impact of changes to the AI agent experience on your most valuable CX KPIs before removing a previous version - thus making data-driven iterations.

There are a few ways to achieve A/B testing within the AI agents -Advanced add-on.

- [Label based separation](#h_01GR1DGBNGRE7J18WYKYT73C41)
- [AI agent/channel-based separation](#h_01GR1DGHKM9885RY037ZCA77C6)
- [Traffic\_split API](#h_01GR1DGQZ88RE2ZBC3KVSDSZ38)

## API/Label based separation

Based on a field coming from an API or setting a [label](https://support.zendesk.com/hc/en-us/articles/8357749583130) within the dialogue flow you can then use this within a [conditional block](https://support.zendesk.com/hc/en-us/articles/8357733406234) to take visitors down different paths.

Examples of separation criteria could be based on:

Whether someone triggers a default reply, after that point they get different replies.

If buttons are used after the welcome message rather than intent recognition, different messages are shown.

From the CRM you can use any field you want to divide the group. It could be a tailored choice like customer status or something more random such as location.

## AI agent/channel-based separation

Differentiating experiences based on channels is already a recommendation that we make. However, the communication style can be A/B tested across social channels either by having different AI agents or by separating by the messaging source, for example, Facebook or Whatsapp.

## Traffic\_split API

**Note -**If you would like to utilize this capability, reach out to your CSM to enable this feature.

This is run using an integration, which we are faking so no actual data is transferred as the logic is hosted in our dashboard, called trafficSplit to compile content-based A/B testing. The fake integration is required to support the randomization of control groups association.

### Setting up the division of groups

This fake integration uses a parameter called **split**.

The parameter **[split]** will dynamically distribute your user to the amount and share of control groups of your choosing - you don’t need to add the share up to 100 yourself, just ensure they are proportional. Below you can find some examples of split proportions. 
 
1 = 1 control group of 100% 1,1 = 2 control groups with an equal share of 50% each 1,1,1 = 3 control groups with an equal share of 33.333333333333% each 1,2,1 = 3 control groups, one of 50% share, the other 2 of 25% each - the control group and 1 variant will have the 25% split.
 
You can also set them up as percentages (i.e. 50,50), important is the relation to each other.

The groups will always be named in this fashion: First group is [control], second [variant\_1], third [variant\_2] ad infinitum.

The first group will always be the [control] group.

### Dialogue set-up

You can set this parameter latest upon the fake integration call; to ensure your user base is evenly distributed without bias it’s recommended though to add this to your Welcome Reply, if supported by the CRM, however, it can be set on the individual reply or replies you want to run tests on.

1. Set the split parameter as a string on the conversation data and a label to identify the conversations that make it to the splitting of visitors.
2. Add an API Integration block and select trafficSplit as the integration source
3. **Collect parameter split**: If you have not set this parameter already, latest you would select it in the Collect Parameters branch. Unless you need it, you can hide this branch by deleting the AI agent message and collapsing the collection. 
   **Scenario results**: Use however you please. This scenario does only one thing - assign your conversation to a control group. 
   **Scenario apiError**: This is super unlikely to trigger as it’s not a real API, however, just make sure to add a fallback so that the customer experience is seamless and the AI agent can continue to function even if the fake integration is inhibited. You can give out a Welcome Reply as any other, just make sure you set all required params that might be required to advance in dialogues later on.
4. Save your parameter to the conversation data by adding a label for value {{variant}}.

![Screenshot_2023-01-31_at_10.26.47.png](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/bots_9854672387730.png)

Within the scenario success path, is also recommended to add a **conversation document label** to identify the entire batch of conversations that were assigned to a control group during your A/B test.

### Use trafficSplit Variants

Technically you can branch off immediately after your fake integration results have been applied - but you don’t have to. Now that you have a parameter [split] with the individual [variant] outcomes of [control], [variant\_1], [variant\_2] etc. you can branch off this at any time you’d like via Conditional Blocks. 

![Screenshot_2023-01-31_at_10.18.13.png](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/bots_9854462209554.png)

In this trafficSplit, we give out three different solutions to the customer - two different self-service links, and one in-AI agent API. All users will be assigned to a conditional block based on their randomly assigned {{variant}} outcome. The Fallback is here to support an ApiError edge case - build it out in a way that is seamless to the customers, and tag it in conversation logs to easily locate and troubleshoot down the road. 
 
Now you will only have to define a success metric, i.e. CSAT or AI agent-Handled, and run your [variant] results against it using a label set on the variant paths. Alternatively, via Tableau.