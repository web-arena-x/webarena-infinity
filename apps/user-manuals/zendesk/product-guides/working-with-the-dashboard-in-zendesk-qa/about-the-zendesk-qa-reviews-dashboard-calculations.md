# About the Zendesk QA Reviews dashboard calculations

Source: https://support.zendesk.com/hc/en-us/articles/7043701093786-About-the-Zendesk-QA-Reviews-dashboard-calculations

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **Add-on** | Quality Assurance (QA) or Workforce Engagement Management (WEM) |

Verified AI summary ◀▼

Learn how to interpret the QA Reviews dashboard to evaluate agent performance and identify improvement areas. Understand calculations for the internal quality score (IQS), category scores, and individual review scores. Discover how marking categories as N/A affects QA score calculations, ensuring accurate performance assessments. This helps you make informed decisions to enhance customer support interactions.

Location:  Zendesk QA > Dashboard > Reviews

This article helps you understand how to interpret and use the different [Reviews dashboard cards](https://support.zendesk.com/hc/en-us/articles/7043724913690) in Zendesk QA to evaluate agent performance
and identify areas for improvement.

This article contains the following topics:

- [Understanding how the IQS is
  calculated](#topic_sws_4ww_42c)
- [Understanding how category scores
  are calculated](#category_scores)
- [Understanding
  how individual review scores are calculated](#understanding_individual_review_scores)
- [Understanding how N/A affects QA
  score calculations](#topic_y5g_2cj_4fc)

Related articles:

- [Understanding the Reviews dashboard in Zendesk
  QA](https://support.zendesk.com/hc/en-us/articles/7043724913690)
- [Filtering the Reviews dashboard](https://support.zendesk.com/hc/en-us/articles/7043701144858)

## Understanding how the IQS is calculated

Your [internal quality score (IQS)](https://support.zendesk.com/hc/en-us/articles/7043724913690#topic_g5y_dw1_cbc) is based on your
conversation reviews. It represents the average of all [review scores](#understanding_individual_review_scores) received
over a [specified period](https://support.zendesk.com/hc/en-us/articles/7043701144858#topic_km1_vzq_tcc), expressed as a percentage.

The IQS is calculated using the following formula:

`IQS = (review_score1 + review_score2 + ...) / (number of reviews) * 100`

For example, considering the following review scores scenario:

|  |  |
| --- | --- |
| **Review** | **Review Score** |
| 1 | 100.00% |
| 2 | 9.91% |
| 3 | 63.96% |
| 4 | 90.99% |
| 5 | 0% |
| **IQS** | 52.97% |

The IQS is calculated as follows:

`(100% + 9.91% + 63.96% + 90.99% + 0%) / 5 = 52.97%`

## Understanding how category scores are calculated

When you [set up your QA scorecard](https://support.zendesk.com/hc/en-us/articles/7043760215194) and define your categories,
you also decide the rating scale for each category. This scale is used to determine the
category score for an interaction.

It’s calculated using the following formula:

```
 Category score = (score_selected - scale_minimum) / (scale_max - scale_minimum) * 100
```

And uses the following scores:

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| **Score** | **1** | **2** | **3** | **4** | **5** |
| Binary scale | 0 | 100% |  |  |  |
| 3-point scale | 0% | 50% | 100% |  |  |
| 4-point scale | 0% | 33.3% | 66.6% | 100% |  |
| 5-point scale | 0% | 25% | 50% | 75% | 100% |

## Understanding how individual review scores are calculated

Each category on your [scorecard](https://support.zendesk.com/hc/en-us/articles/7043760215194) has a weight value, represented as an integer from 0 to
100. To calculate the [review score for an interaction](https://support.zendesk.com/hc/en-us/articles/7043724913690#topic_smr_t3r_tcc), multiply each
category's score by its weight, then divide the total by the sum of the weights.

If a critical
category rating is below 50%, the score is automatically set to zero.

It’s calculated using the following formula:

```
Review score = (category1_score * category1_weight + category2_score * category2_weight...) / (category1_weight + category2_weight...) >> critical category < 50%, then 0%
```

For example, consider the following scenario with five grouped categories with different
weights, where the agent received the following ratings. Critical categories are marked with an asterisk (\*).

| Review | Request\*(1) | Clarification (3) | Explanation (3) | Writing( 2) | Internal Data (1) | Review Score |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | 100% | 100% | 100% | 100% | 100% | 100% |
| 2 | 100% | 0% | 0% | 100% | 0% | 30% |
| 3 | 100% | 0% | 100% | 100% | 100% | 70% |
| 4 | 100% | 100% | 100% | 0% | 100% | 80% |
| 5 | 0% | 100% | 100% | 100% | 100% | 0% |

## Understanding how N/A affects QA score calculations

When evaluating support interactions, you may encounter situations where one or
more categories are marked as [N/A (Not Applicable)](https://support.zendesk.com/hc/en-us/articles/8875998154906#topic_ufd_t3n_zfc).

N/A selections affect the calculation of the final QA score.

When a category is marked as N/A:

- It’s excluded from the final score calculation.
- The final score becomes a weighted average of the remaining rated
  categories.
- The weights of the rated categories are not adjusted; instead, the score is
  based only on the weights of the non-N/A categories.

For example, consider a scenario with the following four categories with
different weights, where the tone category received an N/A rating:

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| **Category** | **Weight** | **Max rating** | **Value** | **Normalized score** | **N/A?** |
| Clarity | 30 | 4 | 3 | 0.75 | No |
| Tone | 30 | 4 | N/A | - | Yes |
| Accuracy | 30 | 4 | 2 | 0.5 | No |
| Structure | 10 | 4 | 4 | 1.0 | No |

In this scenario, only three categories—Clarity, Accuracy, and Structure—are used
in the calculation. Their contributions are as follows:

- Clarity: 0.75 × 30 × 100 = **2250**
- Accuracy: 0.5 × 30 × 100 = **1500**
- Structure: 1.0 × 10 × 100 = **1000**

```
Total Score = 4750 / 70 = 67.8571%
```

If all categories are marked as N/A, no final score is calculated. The review
will display as “No Score” or remain unscored.

If only one category is rated and all others are marked as N/A, that single
category fully determines the final score. Its contribution is calculated normally, and its
weight becomes the total weight used in the score calculation.

The same logic applies within groups. If a group contains multiple categories and
some are marked as N/A, only the valid categories contribute to the group score. If all
categories within a group are marked as N/A, the group score is excluded from the final
calculation.