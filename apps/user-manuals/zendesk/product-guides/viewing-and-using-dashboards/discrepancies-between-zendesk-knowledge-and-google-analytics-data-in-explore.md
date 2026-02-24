# Discrepancies between Zendesk Knowledge and Google Analytics data in Explore 

Source: https://support.zendesk.com/hc/en-us/articles/4408830705178-Discrepancies-between-Zendesk-Knowledge-and-Google-Analytics-data-in-Explore

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support with** | Guide Professional or Enterprise |

You can report on Zendesk Knowledge data within Knowledge, by using Google Analytics, or with Explore. This article answers frequently asked questions about discrepancies in reporting data between these three tools.

This article contains the following topics:

- [Why doesn't the Guide data in Explore match the data I see in Google Analytics?](#topic_mqq_5yy_qpb)
- [Why do deleted or unpublished articles still get views?](#topic_w4w_wyy_qpb)
- [Why don't I see Knowledge Base data in Explore from before January 18, 2021?](#topic_j2x_bzy_qpb)
- [Why is there a discrepancy between "native" reporting and the Explore dashboard?](#topic_e3x_g3z_qpb)

## Why doesn’t the Knowledge data in Explore match the data I see in Google Analytics?

Google Analytics is a general-purpose tool for tracking user activity on any website. As a result, it offers a much broader set of features than the Knowledge integration with Explore.

At the same time, Google Analytics provides less contextual information than the integration between Knowledge and Explore. For instance, Google Analytics does not automatically differentiate between page views from agents and end users.

Because the two tools were designed with different goals in mind, they are implemented differently. Furthermore, Google Analytics is user-configurable, meaning that its behavior varies widely between individual installations.

### Can we fix discrepancies between the two tools?

Generally speaking, no. We have no insight into how Google Analytics is implemented. We can only speculate about how its tracking and aggregation features behave relative to analogous mechanisms that power the Knowledge integration with Explore.

## Why do deleted or unpublished articles still get views?

There are a number of reasons an article may appear as having been viewed after it was deleted or unpublished.

- Most commonly, deleted or unpublished articles receive views if they have multiple translations and only one of the translations has been deleted or unpublished. For example, if you publish both French and English translations of an article, but you delete only the English translation, the French translation might still receive views. To exclude deleted or unpublished translations, you can filter by language in Explore.

- It’s also possible for Explore to register a view for an archived article because Explore relies on the user's web browser in order to register the activity. Under normal circumstances, the sequence of events that leads Explore to track a view proceeds as follows:

 1. A user visits an article URL in their browser.
 2. The help center server responds with the contents of the article as well as some code asking the user's browser to register the view with our activity tracking system.
 3. The user's browser sends a request to our activity tracking system with the information the help center provided (like which article it was or which user viewed the article).
 4. Our activity tracking system receives the request from the user's browser and registers the view.

 In most cases, step 3 happens almost immediately after step 2—it takes only milliseconds for the user's browser to make the request. However, because the browser's behavior is not something we control, we cannot say for sure how long it will take for step 3 to happen.

 For example, if the user's internet connection cuts out between steps 2 and 3, and they later reconnect, we may register the activity only when they reconnect. It might also be that the user's browser crashes and step 3 can happen only when they restart the browser.

 When we finally receive the tracking event, we can be confident that the user did, in fact, view the article. However, we cannot make guarantees about when the view actually occurred on the basis of when the tracking event was received.

## Why don’t I see Knowledge Base data in Explore from before January 18, 2021?

The Knowledge Base dataset in Explore launched on January 18, 2021. Data from before that date is not available in Explore.

## Why is there a discrepancy between “native” reporting and the Explore dashboard?

We are replacing “native” reporting dashboards in the Zendesk agent interface with Explore datasets. For example, the Knowledge Base dataset replaces the Knowledge Base tab in the reporting section of the agent interface. While we aim to provide feature parity between the two reporting tools, they are implemented differently. As a result, discrepancies might exist. Once a dataset is available in Explore, it should be considered the source of truth.

## Why isn't Explore reporting all of my article views?

There are multiple reasons why the number of article views in Explore might differ from the number of views you see in Google Analytics:

- Ad blockers might prevent Explore from recording article views.
- Article views for draft, archived, and deleted articles are not recorded by Explore.