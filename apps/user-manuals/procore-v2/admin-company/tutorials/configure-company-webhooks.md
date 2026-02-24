# Configure Company Webhooks

Source: https://v2.support.procore.com/product-manuals/admin-company/tutorials/configure-company-webhooks

---

## Background

A webhook is an automated message, or an HTTP request, sent from one application to another in real-time when a specific event occurs, allowing for real-time data updates without the need for constant polling or manual requests. Webhooks automate the process of transferring data between applications, eliminating the need for one application to constantly check for updates from another.

In the context of Procore, the Webhooks feature allows company and project administrators to enable third-party developers and integrators to subscribe to event notifications for one or more Procore API resources when Create, Update, or Delete actions occur. For example, a third-party RFI integration may want to be notified whenever a new RFI is created in Procore.

The benefits of the Webhooks feature include:

- Enabling instant communication between Procore and third-party applications and services. Instead of waiting for an application to request information, webhooks push data from Procore as soon as an event occurs. This ensures that systems are always up-to-date.
- Enabling the automation of workflows by triggering actions in third-party applications whenever specific events take place.
- By eliminating the need for constant polling, webhooks reduce the load on servers and conserve bandwidth. This results in more efficient use of resources.
- Reducing the number of API requests through polling can lead to significant cost savings, especially for applications that handle large volumes of data.

## Things to Consider

- **Administrator Information:**

 - 'Admin' level permissions on the Company level Admin tool.
- **Developer Information:**

 - Refer to the [Introduction to Webhooks](https://developers.procore.com/documentation/webhooks) and [Using the Webhooks API](https://developers.procore.com/documentation/webhooks-api) guides on the Developer Portal for information on developing your application or integration to properly support Webhooks.

## Creating a New Hook

1. Navigate to the Company level Admin tool.
2. Under 'Company Settings', click **Webhooks**.
3. On the Webhooks page, click **Create Hook.** This opens a new hook configuration page that includes a number of fields and controls for configuring a hook.
4. Endpoint Configuration:

       
   1. **Endpoint URL** - Enter the URL for the endpoint on the third-party web server that will handle the POST requests coming from Procore when a webhook is triggered.
   2. **Authorization Header (Optional)** - Enter the authorization token that you want to have placed in the header for the POST request sent from Procore. Though this field can be used to define any authorization header information you wish, it is most commonly used to specify authorization credentials for the third-party server. For example, a valid entry for this field might be âBasic c3a24b8208ac5199d083d54a1234e94b8864â.
   3. **Payload Format** - Select the REST API payload version you'd like to send to the third-party service. You will need to work with the third-party developer to understand which payload format is preferred. Note that once the hook is created, the payload version cannot be changed. You will need to delete and re-create the hook if you need to change the payload version.
5. Select the Events to Send:
6. View Selected Events:

You can review the notification events you have selected and remove some if you need to.

## Viewing Webhooks Events

Once a hook is created and configured, you can view the status of the events that Procore has sent to the third-party service.The Overview section provides a high-level summary of the hook including the hook status and other relevant information.

The Events section displays the event history for the selected hook. The event history is maintained for a rolling 28-day period.

Each event is identified by its Resource Name, Resource ID, Event Type, Event Status, and Timestamp in UTC.

Possible values for Event Status are as follows:

- Delivered - the event has been successfully delivered to the third-party service.
- Discarded - the event has been discarded. No further delivery attempts will be made.
- Failed - the event delivery has failed.
- Queued - the event has been queued for delivery to the third-party service.
- Retrying - delivery of the event is being attempted again.

You can perform a variety of actions with the Events list:

- Search for events on a specific resource by resource ID.
- Use the Resource Name dropdown to show only the events for the selected resource.
- Use the Event Status dropdown to show only the events with the selected event status.
- Use the Filter button to create a custom filter on the events list.
- Click on an individual event in the list to view details.