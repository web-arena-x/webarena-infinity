# Setting business hours for WFM forecasts

Source: https://support.zendesk.com/hc/en-us/articles/6443363799066-Setting-business-hours-for-WFM-forecasts

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **Add-on** | Workforce Management (WFM) or Workforce Engagement Management (WEM) |

In Zendesk Workforce management (WFM), you can specify the business hours you want to forecast for.

**To specify business hours**

1. Open the [Forecast](https://support.tymeshift.com/hc/en-us/articles/10680257719443) in Zendesk WFM.
2. (Optional) Choose the **Day** view.   
   You can apply business hours in any view. It's recommended to use the day view because the week and month views might not show the impact of applying business hours.
3. Choose the [workstream](https://support.tymeshift.com/hc/en-us/articles/10679984897043) you want to apply business hours to.
4. Under Staffing Parameters, check **Availability**.
5. Select your business hours and click **Save**. 
   The forecast recalculates the newly configured business hours.
6. To turn off business hours, uncheck the box and save.   
   The forecast is automatically recalculated.

**Note**: For chat and voice channels, the volume outside of these business hours isn't counted. This means that the volume outside of the availability hours will not be considered when calculating staffing requirements within the availability window. However, the email channel sums up the volume outside of the availability hours and considers as if it came in the first second of the availability hours and its SLA started at that point.

## Related articles

- [WFM forecast overview](https://support.tymeshift.com/hc/en-us/articles/10680257719443)