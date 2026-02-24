# Create custom integrations and apps with Xero

Source: https://central.xero.com/s/article/Create-custom-integrations-and-apps-with-Xero

---

## Overview

- Use Xero’s open application programming interface (API) to create custom integrations for your organisation.

How it works

Third party app developers can use Xero’s open application programming interface (API) to create custom integrations between a Xero organisation and other products or programs.

Xero’s API uses [OAuth 2.0](https://developer.xero.com/documentation/oauth2/overview) (Xero Developer Centre), which is the industry-standard protocol for authorisation. OAuth 2.0 allows third party developers secure access to Xero data without sharing a Xero password. Apps that connect using OAuth 2.0 request access to essential data only.

The Xero API supports several variations of OAuth 2.0 to suit different types of integration.

All third party app integrations require a user to authorise the connection. If the user who authorised the connection is deleted from the organisation, another user will need to reconnect the integration.

Types of integrations available

### Choosing the right type of integration

The three variations of OAuth 2.0 we support use different authorisation flows, allow different numbers of connections and have different use cases. We recommend you work with your developer to choose the option that works best with your technology and user needs.

| | Web app | Mobile or desktop app | Custom connection |
| --- | --- | --- | --- |
| **Cost** | Free | Free | Monthly Xero user fee |
| **Authorisation flow** | The [standard authorisation code flow](https://developer.xero.com/documentation/oauth2/auth-flow) (Xero Developer Centre). | The authorisation code flow with [PKCE extension](https://developer.xero.com/documentation/guides/oauth2/pkce-flow) (Xero Developer Centre). | The [client credentials grant type](https://developer.xero.com/documentation/guides/oauth2/custom-connections/) (Xero Developer Centre). |
| **Use case** | Best for web server apps that can securely store a client secret. | For mobile and desktop apps that can't securely store a client secret (Single Page Apps not currently supported). | For custom, machine-to-machine integrations. |
| **Total connections** | Connect with up to 25 Xero organisations. | Connect with up to 25 Xero organisations. | Connect to a single Xero organisation. |
| **Regional availability** | Global | Global | UK, AU, NZ and US Xero organisations only. |

### Web app and mobile or desktop apps

Web app and mobile or desktop integrations offer more flexibility than a custom connection but also require more technical knowledge. To set up this type of integration, your developer needs to be comfortable with writing code to build the authorisation flow.

These integrations are generally used by developers who want to build apps for Xero App Store, but they can also be used for custom integrations if they suit your requirements.

If you want to connect with more than one Xero organisation, you’ll need to use either the web app or mobile or desktop connection. You can connect these integrations to Xero organisations on any plan and in any region.

### Xero custom connections

#### How they work

Xero custom connections are designed to make it easier for developers or app owners to customise their Xero experience with bespoke integrations. Custom connections require less technical knowledge to build because Xero provides the authorisation flow. This means they’re also quicker to integrate and are easier to manage over time.

Custom connections can only be used to integrate with Xero organisations. They can’t be used to integrate with other Xero products, such as Xero HQ or Xero Practice Manager.

#### Price and availability

Custom connections are available to Xero organisations in Australia, New Zealand, United Kingdom and the United States. They incur a [monthly fee](http://connect.xero.com/custom) (Xero) for as long as the connection is in place.

You'll need a standard or advisor user role to purchase a custom connection subscription.

This fee applies to each custom connection you purchase. The billing cycle starts on the day you purchase the connection.

You’ll receive an invoice each month. You can view your invoice and manage your subscription in Xero in the same way as any other connected app.

View and manage your connected apps

1. Click the organisation name, then select **Settings**.
2. Under **General**, select **Connected Apps** to see the apps you've already connected.
3. (Optional) To update your payment method or billing details, click **Update**.
4. (Optional) To view your invoices, change your plan or cancel your subscription, click the app name under the **App Store subscriptions** heading.

Set up a custom integration

### Set up web app and mobile or desktop app connections

Everything your developer needs to know about setting up a web, mobile or desktop app is in our [Xero Developer Centre](https://developer.xero.com/). From here, they can learn more about the technical requirements and access Xero's [AI toolkit](https://developer.xero.com/ai) to help code custom integrations using AI. This is also where they can contact our developer platform team for additional support.

### Buy a custom connection for your Xero organisation

You can buy custom connections for Xero organisations in Australia, New Zealand, the United Kingdom and the United States. You need the standard or advisor Xero user role in the relevant organisation to buy a custom connection.

Practice administrators and staff can only purchase a custom connection for their own practice's Xero organisation. We recommend clients purchase their organisation's custom connection themselves.

Custom connections are only available for Xero organisations in Australia, New Zealand and the United Kingdom.

1. Purchase a [custom connection subscription](https://connect.xero.com/custom) (Xero) for your organisation.
2. Ask your developer to initiate a custom connection from developer.xero.com.
3. In your email inbox, authorise the custom connection request.

Your developer will receive a notification confirming that the custom connection has been authorised and activated. They can now start the [setup process](https://developer.xero.com/documentation/guides/oauth2/custom-connections/) (Xero Developer Centre).

## What's next?

For more information and support, check out the [Xero Developer Centre](https://developer.xero.com/).