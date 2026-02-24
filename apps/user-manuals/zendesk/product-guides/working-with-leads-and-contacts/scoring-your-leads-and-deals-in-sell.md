# Scoring your leads and deals in Sell

Source: https://support.zendesk.com/hc/en-us/articles/4408824510490-Scoring-your-leads-and-deals-in-Sell

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

![Available on Sell Professional plans and above](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/plan_available_sell_ee.png)

You can use lead and deal scoring to help you focus on your most important opportunities. For example, a scoring model can help determine if your leads are good, or not.

Note: For a better understanding of lead scoring and its uses, we recommend that you first read this Zendesk Blog article: [Make more sales faster with lead scoring](https://www.zendesk.com/blog/make-sales-faster-lead-scoring/).

To score a lead or deal, you assign numerical values to important and revealing data points. For example, the source or status of a lead can be a good predictor of the lead’s likelihood of becoming a qualified lead. You combine these variables into a formula that produces a score that you can then track.

scoring formulas can be defined by an Admin user.

**To define lead and deal scoring**

1. Click **Settings** (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/settings_icon.png)), then select [**Business Rules > Scoring**](https://app.futuresimple.com/settings/scores).
2. There are separate tabs for leads and deals scoring. Choose which type of score you want to define.
3. Add variables for the scoring formula that you want to create by clicking **Add Variable**.
4. Choose a symbol for your new variable (A, B, C, etc.).
5. Select the field you want to use for the variable. There are predefined fields, but you can also create and use custom fields for leads and deals.
6. When you’ve defined your variables, you need to enter your lead scoring formula then click **Save**.

To better understand how scoring formulas work, here’s an example. The caveat here is that this is an advanced subject and we’re using a very simple formula to illustrate how this works. If you don’t already understand lead scoring, we recommend that you do additional research to make the most of this Sell feature.

A formula consists of variables to which you assign values. What you choose as your variables depends on what you consider to be valuable lead characteristics that are more likely to predict a successful outcome (conversion and won deals).

In this example, we consider industry and lead source to be valuable indicators for a strong lead. Therefore, we create variables for each and assign values to each variable’s options.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sell-lead-scoring-formula.png)

We’ve added the Industry custom field as a variable and assigned a value between 1 and 10 to each industry type.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sell-lead-scoring-formula2.png)

We create a second variable for the deal source and then add values to the source types we’ve defined.

With both variables defined and saved, we can now enter a formula.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sell-lead-scoring-formula-color.png)

This very simple formula adds the value of industry with the value of the deal source. Therefore, if a lead is in an industry that you’ve assigned a high value and it also comes from a deal source that you consider a good predictor of success and has a high value, your lead will have a high score.

With a scoring formula defined, you can then see how each of your leads rate against your scoring model. You can indicate that by choosing a color scale. Either red to green or cold to hot.

The lead score is shown on lead cards, just below the lead status.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sell-lead-scoring-lead-card.png)

The color of the score number is relative to the color scale you chose and their score is based on the values you defined. The score number can also be added to your working and smart lists as a filter.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sell-lead-scoring-filter2.png)

In this example, the Score filter is added to a smart list and the score range is set from 10 to 30, a range that should be our warm to hot leads.