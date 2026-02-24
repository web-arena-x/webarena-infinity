# Tracking visits in Zendesk Sell

Source: https://support.zendesk.com/hc/en-us/articles/4408829267354-Tracking-visits-in-Zendesk-Sell

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

![Available on all Sell plans](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/plan_available_sell_all.png)

You can set up and use visit tracking for in-person visits made to leads and contacts using your Zendesk Sell mobile app.

Whether you spend your day going door to door as an outside sales rep or only making occasional visits to your clients, you can track these in-person interactions using geolocation. Use the map to plan your route, log visit outcomes to indicate how things went, verify your team's visits using geoverification, and get insights on everything you need to know with visit reports.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sell_track_visit_ios.png) ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sell_track_visit_android.png)

This article covers the following topics:

- [Activating visits](#topic_srb_d4x_ztb)
- [Customizing visit outcomes](#topic_uj4_d4x_ztb)
- [Deactivating visits](#topic_cwz_d4x_ztb)
- [Activating geoverification](#topic_opm_24x_ztb)
- [Logging visits](#topic_b32_f4x_ztb)
- [Reporting for visits](#topic_xp5_f4x_ztb)

## Activating visits

As an admin you must log in to Sell using your Sell mobile app. Then on the web you can activate visits.

**To activate visits**

1. Click **Settings** (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/settings_icon.png)), then click ****[Customize > Visits](https://app.futuresimple.com/settings/visits)****.
2. Click **Enable Visits**.

   Visits is now available on mobile for all account users. You'll see the default visit outcomes defined for your team.

## Customizing visit outcomes

Create new visit outcomes or customize existing ones to indicate how the visit went. Choose a color for each different outcome, which corresponds to a map pin for each lead or contact you visit. This allows you to get a snapshot of visits made to your leads and contacts when viewing the map on your mobile app.

Visits must be customized from the web.

You need admin access to customize visit outcomes.

**To customize a visit outcome**

1. Click **Settings** (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/settings_icon.png)), then click ****[Customize > Visits](https://app.futuresimple.com/settings/visits)****.

   These are the default visit outcomes:
   - Interested
   - Not Interested
   - No Answer
   - Come Back Later
   - Customer Onsite
2. Click **Add Visit Outcome** to add a new visit outcome.
3. Add a name and choose a color for your visit outcome, and click to save.
4. You have a number of actions your can perform on default and new visit outcomes:
   - Edit: click the edit button change the color and name of a visit
   - Delete: click the trashcan icon to delete a visit
   - Up and down arrows: click to move the position of a visit outcome in the list

   Your settings are saved automatically and visit outcomes are updated on mobile for all account users.

## Deactivating visits

You must deactivate Visits on the web.

Note: If you deactivate Visits, users will no longer be able to log visits, view the history of visits, or access visit reports.

You need admin access to deactivate visits.

**To deactivate visits**

1. Click **Settings** (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/settings_icon.png)), then click ****[Customize > Visits](https://app.futuresimple.com/settings/visits)****.
2. Click **Disable Visits**, and click **Disable** to confirm.

   Any previously logged visits and associated data are removed, and users can no longer log visits

## Activating geoverification

Select whether you want to verify a user's location using geolocation on their device every time a visit is logged in Sell. Based on the address stored on the lead or contact, Sell verifies if the user's location matches. If the location of the user matches the address stored on the lead or contact, the visit is marked as verified (see [Using geolocation features from your mobile phone](https://support.zendesk.com/hc/en-us/articles/4408829254042)).

Geoverification must be enabled on the web, and visits must be enabled.

You need admin access to set geoverification.

**To set geoverification**

1. Click **Settings** (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/settings_icon.png)), then click ****[Customize > Visits](https://app.futuresimple.com/settings/visits)****.
2. When users log a visit, click **Yes** to verify the geolocation.

   Your settings are saved automatically and geolocation is activated on Sell mobile for all account users.

## Logging visits

You can log visits using either the Sell mobile app or via Sell in a web browser using the [Log Visit](https://www.zendesk.com/marketplace/apps/sell/269778/log-visit/) app (see [Installing and using the Log Visit app](https://support.zendesk.com/hc/en-us/articles/4408883405210)).

To log visits in the Sell mobile app, follow these instructions.

**To log a visit**

1. Log in to your mobile app.
2. Go to the lead or contact you want to visit, and click **Log a visit**.
3. Alternatively, in the map view, click the pin showing the lead or contact location, and click **Log a visit**.

   Note: Gray pins indicate leads or contacts that have not been visited.

## Reporting for visits

You can track insights around visits using smart lists and reports.

Smart lists are the solution for building custom reports that you can export from Sell. We recommend creating a new smart list to track everything you need to know about visits. If you're new to building smart lists, see [Creating and using smart lists](https://support.zendesk.com/hc/en-us/articles/4408827735066-How-to-Use-Smart-Lists).

The following Visit fields are useful to add to your smart list:

- Last Visit Date
- Last Visit Geoverified - if the location of the last visit was verified
- Last Visit Outcome
- Last Visit Owner - the last user to log a visit to the lead or contact
- Last Visit Summary - any notes logged with the last visit

The following reports give visit insights:

- [Activity Overview report](https://app.futuresimple.com/reports/activity_overview)

  Get insights into the volume of visits made by your team. Track how many visits are logged by each rep in a given timeframe. This report shows a visual snapshot of your activity breakdown in whatever time frame you're looking for (see [About activity reports](https://support.zendesk.com/hc/en-us/articles/4408842698906-Utilizing-Activity-Reports)).
- [Visit Outcomes report](https://app.futuresimple.com/reports/visit_outcomes)

  See how many visits you've made, broken down by outcome. Identify trends around visit outcomes to understand prime times to visit your leads in the future and make the most effective use of your time.