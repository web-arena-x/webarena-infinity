# Exporting Chat Conversion Tracking data

Source: https://support.zendesk.com/hc/en-us/articles/4408821637786-Exporting-Chat-Conversion-Tracking-data

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support with** | Live chat and messaging Professional or Enterprise |

If you want to export the raw past conversion data being recorded from enabled Goals, you have a couple options. For general information about setting up conversion tracking, see [Measuring business goals with conversion tracking](https://support.zendesk.com/hc/en-us/articles/4408886086042).

## Exporting all conversion data from Goals page

If you want to export all conversion data (unattributed and attributed) for a certain time period (max 90 day range), follow these steps:

1. Go to the Goals list page and click on the 'Export CSV' button on the upper right 
   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/chat_exporting_conversion_tracking_1.png)
2. In the dialog, select the date range you want to export and to which agents you want to send the export.
3. Click **Send**.
4. You'll receive an email with a link to download the CSV file with the conversion data.  
   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/chat_exporting_conversion_tracking_2.png)
5. You will see the following columns in the CSV file: Conversion Create Time (UTC+0), Goal Name, Attributed Chat ID, Attributed Chat Timestamp (UTC+0), Attributed Agent Name, Attributed Agent ID, Department Name, Department ID

## Exporting attributed conversion data from History page

If you are only interested in chats with an attributed conversion, you can use the chat details CSV export in the History tab. You can learn how to export chat details [here](https://support.zendesk.com/hc/en-us/articles/4408893866778-Browsing-past-chats-in-History).

In the chat details export CSV file, you should see the following columns: last\_conversion\_goal\_name, last\_conversion\_goal\_id, last\_conversion\_date (UTC +0), last\_conversion\_attribution (Agent Name)

## Using REST APIs

If you are comfortable using the Chat REST APIs, you can get the last 20 conversions attributed to a chat using the [Chat API](https://developer.zendesk.com/rest_api/docs/chat/chats).