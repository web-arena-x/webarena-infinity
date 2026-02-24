# Managing and strengthening the AI model for an advanced AI agent

Source: https://support.zendesk.com/hc/en-us/articles/8357756708378-Managing-and-strengthening-the-AI-model-for-an-advanced-AI-agent

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **Add-on** | AI agents - Advanced |

As additional intents and expressions are added and the AI model becomes more advanced, it is essential to monitor how the AI model is performing and identify where improvements can be made.

We offer a number of tools you can use to strengthen the AI model. 

Optimized training

Here’s a step-by-step guide to optimizing your training by using our AI-based tools. This is an iterative process that can be done both pre- and post-launch.

# Step 1: Generate a new evaluated model

- Go to AI > Models > + New Model > Tick ‘Run Cross-validation’ > Train AI agent.
- This can take several hours. The status will move from Queued > Started > Finished, so you’ll know when it’s done.
- Tip: run the night before if you want to train the following morning.

# Step 2: Consult Confusion Matrix

Go to Training Center > Confusion Matrix. Use ‘Confusion Matrix’ and ‘List of Issues’ to evaluate which intents are "confused" or overlapping with other intents.

For the Medium & High intents, go to Manage Expressions to deep dive into which expressions are causing confusion. These will be highlighted in yellow.

Ask yourself: 

- Are both intents well defined? Is the scope of each intent clear? Tip: use the Intent Description to clearly outline scope of an intent
- Does the topic of this intent or its expression overlap with another intent? If there is overlap, does it make sense to merge the intents?
- Does the intent have enough expressions to live on its own? Note: the more expressions an intent has the more weight it has in the model, so if an intent isn’t being recognized when it should be, it can be due to a lack of sufficient training data.

# Step 3: Train from Impact Report

- Generate a new Impact Report:

- Go to AI > Impact Report > + New Report
- Select “From Existing Messages” if you wish to use data already imported, or “From CRM” if you wish to import additional data
- Specify a timeframe: depending on the timeframe selected and the volume of messages, this can take anywhere from 10 mins to an hour
- Set ‘Benchmark Model’ as ‘Current Model’ > Create.

- Use the new impact report to train. Use the filters to target your training.

After Step 3, you could re-run an evaluated model and check whether the Confusion Matrix has improved.