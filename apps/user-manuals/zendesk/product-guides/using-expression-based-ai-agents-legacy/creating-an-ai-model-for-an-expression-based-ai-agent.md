# Creating an AI model for an expression-based AI agent

Source: https://support.zendesk.com/hc/en-us/articles/8357756681754-Creating-an-AI-model-for-an-expression-based-AI-agent

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **Add-on** | AI agents - Advanced |

AI model is the brain of your AI agent. The better an AI model is, the better your AI agent can understand customer queries.

A new AI model is created automatically every day at midnight if any changes have been made to the training data that day. However, an initial AI model has to be set up in order to kick off this process.

Follow the steps below to create the initial AI model for your AI agent:

- [Create the initial AI model](#1-create-the-initial-ai-model)
- [SNGP net](#2-sngp-net-)
- [Training Type Settings](#3-training-type-settings)

## Create the initial AI model

Now you have a basic intent structure, you want to create the initial AI model.

Go to **AI > Models > +New Model** **> Train AI agent**. 

When generating a model, there are a number of settings you can select or unselect:

## AI model Architecture

### SNGP net

The latest model type is faster, easier to use, and more confident than Intent net models that don't require tuning of hyperparameters - and thus you don't need to worry about the additional settings.

## Training Type Settings

### Run Cross-validation

This will generate an evaluated model which is automatically created once a week, whether training has taken place or not. A [Confusion Matrix](https://support.zendesk.com/hc/en-us/articles/8357756496922-Confusion-Matrix-explained) will help you identify at this early stage how clearly defined intents are and if there is overlap between intents.

### Use Model

This should be selected, but in the rare case you want to run a comparison and test hyperparameters before activating the model.

## Advanced Model Settings

Advanced Model Settings affect the way the AI model works.

### Training Loop

How long in seconds would you like to dedicate to the training and if it takes longer the training will be canceled?