# Importer: Date Formatting

Source: https://support.joinhandshake.com/hc/en-us/articles/231942648-Importer-Date-Formatting

---

*Please note: if your location participates in Daylight Savings Time, double-check the dates for historical imports: if it's during standard time, proceed as normal, and if the date is during Daylight Savings Time, you'll need to account for the difference. For example, this historical appointment was (2016-11-01T12:00:00-04:00), but due to DST, it should have actually been (2016-11-01T12:00:00-05:00).*

*Formatting dates may be a little confusing because the system assumes UTC time, unless another timezone is specified.*

**When using dates or date/times for any field included in a CSV file uploaded either through AWS or the Importer, please provide them in one of the following formats:**

- yyyy-mm-dd

- **Example:** *2016-11-01*

- yyyy-mm-dd**T**hh:mm:ss
 - Remember that this assumes UTC time, so if you're in an eastern time zone, you would see this as 8am. (There's a -4:00 offset)

- **Example:** *2016-11-01T12:00:00*

- yyyy-mm-dd**T**hh:mm:ss offset (where timezone offset is either + or -, and hh:mm)
 - This would show as 12:00pm in the system (if in Eastern)

- **Example:** *2016-11-01T12:00:00-04:00*

**Notes**

- For most imports, you will only need to use the date format
- For imports such as appointments, you may use the date-only format **BUT**:
 - Example: 2016-11-01
 - This will show as: 2016-10-31 at 8:00PM (if in Eastern)

- The time defaults to 00:00
- When translated from UTC, the appointment will appear to have happened the day before

**We formatted dates with the time for appointments (or notes)! Why is it not working?**

The date/time formatting must be formatted precisely in order for it to successfully upload. If only the date is formatted correctly, it won't process any data after that.

- ***2016-11-01T12:00:00-04:00** -* Works
- ***2016-11-01 12:00 -400*** - Will not work

-------------------------------------------------------------------

**\*\*Please Note: Dates can now be included with the following formatting (as of 6/11/2018):**

**MM/DD/YYYY**

**However, if you do include dates with this formatting, the following option *must* be selected when uploading your file:**

**![](https://support.joinhandshake.com/hc/article_attachments/25997328591255)**