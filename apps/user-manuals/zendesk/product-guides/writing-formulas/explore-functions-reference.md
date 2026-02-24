# Explore functions reference

Source: https://support.zendesk.com/hc/en-us/articles/4408834558746-Explore-functions-reference

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support with** | Explore Professional or Enterprise |

When you start to create your own custom metrics and attributes, you'll use functions a lot to help you perform comparisons, calculations, and manipulations to your business information.

Explore offers many functions to help you work with, for example, dates, text strings, calculations and more. Use this article as a reference to help you discover the available functions and how to use them.

Tip: If any table columns are not visible on your screen, you can scroll sideways to see them.

This article contains the following topics:

- [Getting started](#topic_y5p_f2n_dhb)
- [Basic mathematical operators](#topic_mfs_nqf_dhb)
- [Logical functions](#topic_alh_4lf_dhb)
- [Attribute functions](#topic_ihb_zkf_dhb)
- [Tag functions](#topic_gz1_dz4_plb)
- [Text functions](#topic_l1t_plf_dhb)
- [Regex functions](#topic_i1d_vlf_dhb)
- [Date functions](#topic_rpl_mlf_dhb)
- [Numeric functions](#topic_dmy_4lf_dhb)
- [Trigonometric functions](#topic_pxj_rlf_dhb)
- [Comment functions](#topic_kmv_2yd_y2c)

## Getting started

You can browse for, and select functions when you create a standard calculated metric or attribute. In the formula editing window, you can either begin to type the name of a function or click **Add** under **Functions** and choose your function from the list.

When the function is added to a formula, it will appear with standard values. You must replace these with the values you want to use in your formula. In this example, you want to return only your tickets with subject lines beginning with "[Flagged]".

1. In the calculations menu (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_calculations.png)), click **Standard calculated attribute**.
2. Name your calculated attribute. This example uses **Subject begins with [Flagged]**.
3. Under **Functions**, click **Add**.
4. In the formula window, type IF .
5. Under **Functions**, click **Add**.
6. Search for **LEFTPART**. Either use the search box, click **Filter** to scope the values down to the **Text** category, or scroll through the list until you find the function you want.
7. Next to **LEFTPART**, click **+**.
8. You'll now see the formula **IF LEFTPART(\_text,\_number)**. Change the *\_text* parameter to the Ticket Subject attribute. Either highlight **\_text** and then choose **Ticket subject** from the **Fields** menu, or amend the formula manually to add the attribute.

   The formula will now read **IF LEFTPART([Ticket subject],\_number)**
9. Change the text \_number to the number of characters you want to compare.
   [Flagged] has nine characters, so enter **9**.

   The formula will now read **IF LEFTPART([Ticket subject],9)**
10. Finally, add the condition we are searching for; in this case, the text "[Flagged]". The final formula will read:

    **IF LEFTPART([Ticket subject],9)="[Flagged]" THEN [TicketID] ENDIF**

    ![Explore sample function](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_sample_function.png)

Now, when you use this attribute in your report, it will only return tickets with a subject line beginning "[Flagged]".

For more help and examples, see [Writing Explore formulas](https://support.zendesk.com/hc/en-us/articles/4408836190362-Navigating-the-Formula-window).

## Basic mathematical operators

In addition to the above functions, you can also use the following basic mathematical operators to perform calculations and connect text:

| Operator | Description |
| + | Add two numeric values, or join two text strings. |
| - | Subtract one value from another. |
| \* | Multiply two values |
| / | Divide one value by another |
| = | Test if one value is equal to another value |
| != | Test if one value is not equal to another value |
| > | Test if the first value is greater than the following value (x>y) |
| < | Test if the first value is less than the following value (x<y) |
| >= | Test if the first value is greater than or equal to the following value (x>=y) |
| <= | Test if the first value is less than or equal to the following value (x<=y) |
| % | Computes the modulo (or remainder) after dividing one value by another. Example: 5%2 returns 1, 20%3 returns 2 |

## Logical functions

These functions give you great flexibility in analyzing and presenting your information just how you want.

| Function | Description |
| IF THEN ELSE Conditional expression | Enables you to evaluate logical values. Format: IF (*condition*) THEN (*value if true*) ELSE (*value if false*) ENDIF For in-depth information about this function, see [Using the IF THEN ELSE function](using-the-if-then-else-function.md). |
| AND | Returns TRUE if the two supplied expressions are TRUE. Example: IF ([Ticket channel]="Email") AND ([Submitter email]="fred@fredco.com") THEN [Ticket ID] ENDIF Returns all tickets that were received via. email from fred@freedco.com. |
| OR | Returns TRUE if at least one of the supplied expressions is TRUE. Example: IF ([Ticket channel]="Email") OR ([Ticket channel]="Voice") THEN [Ticket ID] ENDIF Returns all tickets that were received through either the email or voice channels. |
| NOT | Reverses the logical value of the supplied expression. Example: IF NOT([Ticket channel]="Email") THEN [Ticket ID] ENDIF Returns all tickets that were not received through the email channel. |
| TRUE | Returns the logical value "TRUE". |
| FALSE | Returns the logical value "FALSE" |
| IN*(\_param,\_array)* | Returns TRUE if the first entered parameter is in the array specified in the second parameter. Examples: IN(200,ARRAY(100,200,300,400)) returns TRUE IN(250,ARRAY(20,40,60,80)) returns FALSE |
| SWITCH Conditional expression | SWITCH provides an easier-to-understand alternative to IF THEN ELSE statements that have multiple branches. SWITCH (*\_tested\_element*) { CASE \_value1: *\_return\_value* CASE \_value2: *\_return\_value* DEFAULT: *\_default\_return\_value* } For in-depth information about this function, see [Adding multiple conditional expressions with SWITCH](adding-multiple-conditional-expressions-with-switch.md). |

## Attribute functions

These functions let you perform basic operations to quantify the number of attributes returned by your report. You can also perform more advanced operations to "lock in" or extend the aggregation level of your calculations.

| Function | Description |
| COUNT\_VALUES*(\_attribute)* | Counts the number of values of the attribute you supply. Repeat values are included. Can be used as a condition in calculated attributes and metrics, but cannot be used in the THEN clause of a calculated metric. Example: IF COUNT\_VALUES([Ticket ID])>30 THEN 1 ELSE 0 ENDIF The example above returns 1 when there are more than 30 tickets, and 0 when there are fewer than 30. Tip: If you want to create a metric that counts the number of the values of an attribute, the metric formula should be simply [Attribute]. You can then [apply the COUNT aggregator](../building-reports/choosing-metric-aggregators.md#topic_ycz_vxv_ngb) as normal. |
| DCOUNT\_VALUES(*\_attribute*) | Counts the distinct number of different values of the attribute you supply. Can be used as a condition in calculated attributes and metrics, but cannot be used in the THEN clause of a calculated metric. Example: IF COUNT\_VALUES([Organization name])>100 THEN 1 ELSE 0 ENDIF The example above returns 1 when there are more than 100 distinct organizations, and 0 when there are fewer than 100. Tip: If you want to create a metric that counts the number of distinct values of an attribute, the metric formula should be simply [Attribute]. You can then [apply the D\_COUNT aggregator](../building-reports/choosing-metric-aggregators.md#topic_ycz_vxv_ngb) as normal. |
| ATTRIBUTE\_FIX(*aggregator*(*metric name*), *attribute1*, *attribute2*) | Returns the value of *aggregator*(*metric name*) aggregated by the attributes you specify (in this example *attribute1* and *attribute2*). No other attributes can affect the results from this metric. [Calculated attributes](https://support.zendesk.com/hc/en-us/articles/4408831146266#topic_m4c_hc2_zsb) can’t be used inside of the ATTRIBUTE\_FIX function. Example: ATTRIBUTE\_FIX(MED(First Reply Time (min), [Ticket created - Year], [Ticket created - Month]) For more help and examples, see [Working with aggregation level functions](https://support.zendesk.com/hc/en-us/articles/4408845551258). |
| ATTRIBUTE\_ADD(*aggregator*(*metric name*), *attribute1*, *attribute2*) | Returns the value of *aggregator*(*metric name*) aggregated to all attributes in the report in addition to *attribute1* and *attribute2*. [Calculated attributes](https://support.zendesk.com/hc/en-us/articles/4408831146266-Calculation-types-reference#topic_m4c_hc2_zsb) can’t be used inside of the ATTRIBUTE\_ADD function. Example: ATTRIBUTE\_ADD(MED(First Reply Time (min), [Ticket created - Year], [Ticket created - Month]) For more help and examples, see [Working with aggregation level functions](https://support.zendesk.com/hc/en-us/articles/4408845551258). |

## Tag functions

These functions help you search for the presence or absence of tags. This can include ticket tags, call tags, or anything else that uses tags.

Important: Only the functions in this section can be used to report on tags. Reports might not work or return inaccurate results if you use functions not detailed below.

| Function | Description |
| INCLUDES\_ALL([*tag attribute*], "*tag1*", "*tag2*") | Returns TRUE if all of the specified tags are included in the tag attribute. Examples: INCLUDES\_ALL([Ticket tags], "London", "Milan") returns TRUE if a ticket contains the tags "London" and "Milan". NOT INCLUDES\_ALL ([Ticket tags], "London", "Milan") returns TRUE if a ticket does not contain both of the tags "London" and "Milan". For more examples of how to use this function, see [Reporting with tags](https://support.zendesk.com/hc/en-us/articles/4408838151450). |
| INCLUDES\_ANY([*tag attribute*], "*tag1*", "*tag2*") | Returns TRUE if any of the specified tags are included in the tag attribute. Examples: INCLUDES\_ANY([Ticket tags], "London", "Milan") returns TRUE if a ticket contains the tags "London" or "Milan". NOT INCLUDES\_ANY ([Ticket tags], "London", "Milan") returns TRUE if a ticket does not contain either of the tags "London" or "Milan". For more examples of how to use this function, see [Reporting with tags](https://support.zendesk.com/hc/en-us/articles/4408838151450). |

## Text functions

These functions enable you to perform operations that search and evaluate text. You can also modify text using formulas and patterns you create.

For examples of how to use some of these text functions (like CONTAINS, LEFTPART, SUBSTR, FIND, and LENGTH) see [Explore recipe: Reporting on nested drop-down fields](https://support.zendesk.com/hc/en-us/articles/4408846701082).

| Function | Description |
| CONTAINS*(\_text,\_text\_to\_search)* | Returns TRUE if the first entered parameter contains the second one as a substring. Example: CONTAINS([Submitter name],"Sally") - Returns TRUE if the submitter name is "Sally Jones" - Returns FALSE if the submitter name is "Rachel Jones" |
| ENDSWITH*(\_text,\_text\_to\_search)* | Returns TRUE if the first supplied text ends with the second supplied text. Example: ENDSWITH([US State],"ippi") returns TRUE for Mississippi, but FALSE for Delaware. |
| FIND*(\_text,\_text\_to\_find,\_number\_start\_index)* | Returns the index, in the first entered text, of the first instance of the second entered text, from the entered start index. Returns -1 if the second entered text is not found. The index of the first character of a string is 0. Examples: If [Ship Mode]="Urgent" then FIND([ShipMode","Norm",0) returns -1 If [Ship Mode]="Normal" then FIND([ShipMode","ma",0) returns 3 If [Ship Mode]="Urgent" then FIND([ShipMode","ge",2) returns 0 |
| LEFTPART*(\_text,\_number)* | Returns the leftmost *\_number* of characters in the supplied text. Example: If [Department]="Technical documentation" then LEFTPART([Department],9) returns "Technical" |
| LENGTH*(\_text)* | Returns the length (number of characters) of the supplied text. Example: LENGTH([Product category]) returns the length of each value of the Product category attribute. |
| LOWERCASE*(\_text)* | Converts and returns the supplied text in lower case. |
| LTRIM*(\_text)* | Returns the supplied attribute value with any whitespace to the left removed. Example: LTRIM([Name]) would return "Peter " if [Name] is " Peter " |
| REPLACE*(\_text,\_text\_to\_replace,\_text\_to\_replace\_with)* | Returns a copy of *\_text* in which all instances of *\_text\_to\_replace* have been replaced with *\_text\_to\_replace\_with*. Example: IF [US State]="new York" then REPLACE([US State],"n","N") returns "New York" |
| RIGHTPART*(\_text,\_number)* | Returns the rightmost *\_number* of characters in the supplied text. Example: If [Department]="Technical documentation" then RIGHTPART([Department],13) returns "documentation" |
| RTRIM*(\_text)* | Returns the supplied attribute value with any whitespace to the right removed. Example: TRIM([Name]) would return " Peter" if [Name] is " Peter " |
| STARTSWITH*(\_text,\_text\_to\_search)* | Returns TRUE if the first supplied text starts with the second supplied text. Example: STARTSWITH([US State],"Miss") returns TRUE for Mississippi, but FALSE for Delaware. |
| IS\_POSITIVE*(\_text)* | Returns TRUE for positive and FALSE for negative based on analysis of the text. |
| SUBSTR*(\_text,\_number\_start\_index,\_number\_end\_index)* | Returns part of *\_text* consisting of the character specified by start index (the first entered integer) and all characters up to end index-1 (the second entered integer). Example: SUBSTR("Web marketing",0,3) returns "Web" |
| TRIM*(\_text)* | Returns the supplied attribute value with any whitespace to the left or right removed. Example: TRIM([Name]) would return "Peter" if [Name] is " Peter ": |
| UPPERCASE*(\_text)* | Converts and returns the supplied text in upper case. |
| STRING*(\_number)* | Converts the supplied number into a string. |
| LPAD*(\_text,\_length,\_pad)* | Pads text to the left of *\_text* with *\_pad* until the string is at *\_length*. Example: LPAD("1",7,"?") returns "??????1" |
| RPAD*(\_text,\_length,\_pad)* | Pads text to the right of *\_text* with *\_pad* until the string is at *\_length*. Example: RPAD("1",7,"?") returns "1??????" |
| LINK*(\_url,\_label)* | Returns a HTML link pointing to the supplied URL. For an example, see [Explore recipe: Configuring clickable links to tickets](https://support.zendesk.com/hc/en-us/articles/4408839123226-Explore-recipe-Configuring-clickable-links-to-tickets). |

## Regex functions

A regular expression (sometimes known as a regex or regexp) is a sequence of characters that define a search pattern. Explore contains support for using regular expressions to accomplish the following calculations in your formulas:

| Function | Description |
| REGEXP\_MATCH*(\_text,\_regexp)* | Returns true if the text matches the regular expression. |
| REGEXP\_EXTRACT*(\_text,\_regexp)* | Returns the portion of text that matches the capturing group in the regular expression. For an example of how to use this function, see [Can I report on user email domain in Explore?](https://support.zendesk.com/hc/en-us/articles/4408845536794) |
| REGEXP\_REPLACE*(\_text,\_regexp,\_replace\_text)* | Returns a string where any substring of text that matches the regular expression is replaced by *replace\_text*. Example: REGEXP\_REPLACE("Hello","lo","p") returns "Help" |

For more information about regular expressions, see [this Wikipedia page](https://en.wikipedia.org/wiki/Regular_expression).

## Date functions

Explore lets you create, compare, and perform calculations on dates and times. These functions are particularly useful because you'll likely spend a lot of time examining your company information over a chosen date range.

| Function | Description |
| DATE*(\_text)* | Converts the supplied text into a date with a UTC timestamp. The entered text can be in a variety of formats, but must at least include the month, day, and year. Examples:   - "2020-07-24T06:23:00+0200" - "2020-07-24T06:23" - "2020-07-24" - "07/24/2020" - "2020-Jul-24" - "July-24-2020" |
| DATE\_EQUAL*(\_date,\_date)* | Returns TRUE if the two entered dates are equal. Example: IF DATE\_EQUAL([Ticket Created - Month],[Ticket Solved - Month]) THEN [Ticket ID] ENDIF Returns all tickets that were solved in the same month they were created. The year isn't included in this example so a ticket that was created in June 2018 and solved in June 2020 would be returned by this example. |
| DATE\_NOT\_EQUAL*(\_date,\_date)* | Returns TRUE if the two entered dates are not equal. Example: IF DATE\_EQUAL([Ticket Created - Month],[Ticket Solved - Month]) THEN [Ticket ID] ENDIF Returns all tickets that were not solved in the same month they were created. |
| DATE\_LESS*(\_date,\_date)* | Returns TRUE if the first date is earlier than the second date. Example: IF DATE\_LESS([Ticket Assigned - Date],[Ticket Due - Date - Date]) THEN [Ticket ID] ENDIF Returns all tickets that were assigned before their due date. |
| DATE\_LESS\_OR\_EQUAL*(\_date,\_date)* | Returns TRUE if the first date is earlier or the same as the second date. Example: IF DATE\_LESS\_OR\_EQUAL([Ticket Assigned - Date],[Ticket Due - Date - Date]) THEN [Ticket ID] ENDIF Returns all tickets that were assigned before or on their due date. |
| DATE\_GREATER*(\_date,\_date)* | Returns TRUE if the first date is later than the second date. Example: IF DATE\_GREATER([Ticket Assigned - Date],[Ticket Due - Date - Date]) THEN [Ticket ID] ENDIF Returns all tickets that were assigned after their due date. |
| DATE\_GREATER\_OR\_EQUAL*(\_date,\_date)* | Returns TRUE if the first date is later or the same as the second date. Example: IF DATE\_GREATER\_OR\_EQUAL([Ticket Assigned - Date],[Ticket Due - Date - Date]) THEN [Ticket ID] ENDIF Returns all tickets that were assigned on or after their due date. |
| DATE\_ADD*(\_date,\_date\_part,\_increment)* | Returns the given date in the user's time zone, updated by the entered increment. The *\_date\_part* parameter could be for example, 'year', 'quarter', 'month', 'day', 'hour', etc. The entered increment must be an integer value, but it can be negative. |
| DATE\_DIFF*(\_date,\_date,\_date\_part)* | Returns the relative or exact difference between two dates in the format you choose. In the function, *\_date\_part* can be one of the following: For relative differences (whole numbers):   - "year" - "half\_year" - "quarter" - "month" - "day" - "hour" - "minute" - "second"   For exact values:   - "nb\_of\_years" - "nb\_of\_half\_years" - "nb\_of\_quarters" - "nb\_of\_months" - "nb\_of\_days" - "nb\_of\_hours" - "nb\_of\_minutes" - "nb\_of\_seconds"   Examples: DATE\_DIFF("2011/10/22","2008/01/06","year") returns 3 (2011-2008) DATE\_DIFF("2011/10/22","2008/01/06","nb\_of\_years") returns 4 (actual count of years) DATE\_DIFF("2019/03/06","2017/03/05","day") returns 1 DATE\_DIFF("2019/03/06","2017/03/05","nb\_of\_days") returns 731 Use only one custom timestamp. If you attempt to use two, no results are returned. |
| DATE\_FORMAT*(\_date,\_format)* | Returns the entered date in the user's time zone in the supplied format. For a list of the formats you can use, see [Formatting dates](#topic_esm_5qg_dhb). |
| TODAY*()* | Returns the current date in the user's time zone. |
| NOW*()* | Returns the current date and time in the user's time zone (in hours, minutes, and seconds). |
| CURRENT\_YEAR*()* | Returns the current year. |
| CURRENT\_HALFYEAR*()* | Returns the current semester as "H1" or "H2" |
| CURRENT\_QUARTER*()* | Returns the current quarter as "Q1", "Q2", "Q3", or "Q4" |
| CURRENT\_MONTH*()* | Returns the current month, for example "January", "February". |
| CURRENT\_MONTH\_NUMERIC*()* | Returns the current month as a number, for example "1" for January, "2" for February. |
| CURRENT\_DAY*()* | Returns the current day as a number. |
| CURRENT\_WEEKDAY*()* | Returns the current day of the week as text, for example "Monday", "Tuesday". |
| CURRENT\_WEEKDAY\_NUMERIC*()* | Returns the current day of the week as a number, for example "0" for Sunday, "1" for Monday. |
| CURRENT\_HOUR*()* | Returns the current hour in the user's time zone as a number. |
| CURRENT\_MINUTE*()* | Returns the current minute in the user's time zone as a number. |
| CURRENT\_SECOND*()* | Returns the current second in the user's time zone as a number. |
| YEAR*(\_date)* | Returns the year of the supplied date. |
| MONTH*(\_date)* | Returns the month of the supplied date as text, for example "January", "February" |
| MONTH\_NUMERIC*(\_date)* | Returns the month of the supplied date as a number, for example "1" for January, "2" for February. |
| DAY*(\_date)* | Returns the day of the supplied date. |
| WEEKDAY*(\_date)* | Returns the day of the supplied date as a string, for example "Monday", "Tuesday". |
| WEEKDAY\_NUMERIC*(\_date)* | Returns the day of the supplied date as a number, for example "1" for Sunday, "2" for Monday. |
| HOURS*(\_date)* | Returns the hour of the supplied date. |
| MINUTES*(\_date)* | Returns the minute of the supplied date. |
| SECONDS*(\_date)* | Returns the second of the supplied date. |
| WEEK\_NUMBER*(\_date)* | Returns the week number associated with the supplied date. See [Understanding how the start of the week affects week numbers](https://support.zendesk.com/hc/en-us/articles/4418307079322#topic_ibw_tym_htb). |
| WEEK\_NUMBER\_MONDAY*(\_date)* | Returns the week number associated with the supplied date starting on Monday. |
| WEEK\_NUMBER\_FRIDAY*(\_date)* | Returns the week number associated with the supplied date starting on Friday. |
| WEEK\_NUMBER\_SATURDAY*(\_date)* | Returns the week number associated with the supplied date starting on Saturday. |
| WEEK\_NUMBER\_SUNDAY*(\_date)* | Returns the week number associated with the supplied date starting on Sunday. |
| START\_OF\_QUARTER*(\_date)* | Returns the start of the quarter for the supplied date. |
| END\_OF\_QUARTER*(\_date)* | Returns the end of the quarter for the supplied date. |
| START\_OF\_MONTH*(\_date)* | Returns the start of the month for the supplied date. |
| END\_OF\_MONTH*(\_date)* | Returns the end of the month for the supplied date. |
| START\_OF\_WEEK*(\_date)* | Returns the start of the week for the supplied date. See [Setting the start of the week for reports and filters](https://support.zendesk.com/hc/en-us/articles/4418307079322). |
| END\_OF\_WEEK*(\_date)* | Returns the end of the week for the supplied date. See [Setting the start of the week for reports and filters](https://support.zendesk.com/hc/en-us/articles/4418307079322). |
| START\_OF\_WEEK\_MONDAY*(\_date)* | Returns the start of the week that matches the supplied date with the week starting on Monday. |
| END\_OF\_WEEK\_MONDAY*(\_date)* | Returns the end of the week that matches the supplied date with the week starting on Monday. |
| START\_OF\_WEEK\_FRIDAY*(\_date)* | Returns the start of the week that matches the supplied date with the week starting on Friday. |
| END\_OF\_WEEK\_FRIDAY*(\_date)* | Returns the end of the week that matches the supplied date with the week starting on Friday. |
| START\_OF\_WEEK\_SATURDAY*(\_date)* | Returns the start of the week that matches the supplied date with the week starting on Saturday. |
| END\_OF\_WEEK\_SATURDAY*(\_date)* | Returns the end of the week that matches the supplied date with the week starting on Saturday. |
| START\_OF\_WEEK\_SUNDAY*(\_date)* | Returns the start of the week that matches the supplied date with the week starting on Sunday. |
| END\_OF\_WEEK\_SUNDAY*(\_date)* | Returns the end of the week that matches the supplied date with the week starting on Sunday. |
| DATE\_FROM\_ISO | Returns a timestamp if the parameter is an ISO standard timestamp string. Assumes that the timestamp has a timezone, but timestamps without timezone information can be parsed by setting the optional skip-timezone parameter to TRUE. Examples: DATE\_FROM\_ISO("2020-07-24T13:42:00Z") DATE\_FROM\_ISO("2020-07-24T13:42EST") DATE\_FROM\_ISO("2020-07-24T13:42+05") DATE\_FROM\_ISO("2020-07-24T13:42," TRUE) |
| DATE\_FROM\_TIMESTAMP*(\_timestamp)* | Returns a date from a supplied [UNIX timestamp](https://www.unixtimestamp.com/) in seconds. |
| DATE\_FROM\_MILLI\_TIMESTAMP*(\_timestamp)* | Returns a date from a supplied [UNIX timestamp](https://www.unixtimestamp.com/) in milliseconds. |
| DATE\_TO\_TIMESTAMP*(\_date)* | Returns a [UNIX timestamp](https://www.unixtimestamp.com/) in the user's time zone from a supplied date. |
| DATE\_TO\_MILLI\_TIMESTAMP*(\_date)* | Returns a [UNIX timestamp](https://www.unixtimestamp.com/) in milliseconds from a supplied date. |
| SECONDS\_TO\_TIME*(\_time)* | Converts seconds to HH:MM:SS format. |
| FISCAL\_YEAR*(\_date,\_start\_month)* | Returns the fiscal year based on the supplied date and start month. The *month* parameter must be the full name of the month (e.g., "February", not "Feb"). |
| FISCAL\_QUARTER*(\_date,\_start\_month)* | Returns the fiscal quarter based on the supplied date and start month. The *month* parameter must be the full name of the month (e.g., "February", not "Feb"). |
| FISCAL\_WEEK\_NUMBER*(\_date,\_start\_month)* | Returns the fiscal week number based on the supplied date and start month. The *month* parameter must be the full name of the month (e.g., "February", not "Feb"). |
| WEEKYEAR*(\_date)* | Returns the year of the week number associated with the supplied date. |
| DATE\_FIRST(*time attribute*) | Returns the earliest date or timestamp according to attributes added to the report and is affected by all applied filters. Example: DATE\_FIRST([Update - Timestamp]) Returns the earliest update timestamp taking into account all attributes you added to the report. For more help and examples, see [Working with earliest and latest date functions](https://support.zendesk.com/hc/en-us/articles/4408833381402). |
| DATE\_LAST(*time attribute*) | Returns the latest date or timestamp according to attributes added to the report and is affected by all applied filters. Example: DATE\_LAST([Update - Timestamp]) Returns the latest update timestamp taking into account all attributes you added to the report. For more help and examples, see [Working with earliest and latest date functions](https://support.zendesk.com/hc/en-us/articles/4408833381402). |
| DATE\_FIRST\_FIX(*time attribute, attribute1, attribute2, ...*) | Returns the earliest date or timestamp according to the attributes specified in the function. Attributes added to the report will not affect the calculation but any filters applied will be taken into account. Example: DATE\_FIRST\_FIX([Update - Timestamp], [Update ticket ID]) Returns the earliest update timestamp per ticket, regardless of the attributes from the report. For more help and examples, see [Working with earliest and latest date functions](https://support.zendesk.com/hc/en-us/articles/4408833381402). |
| DATE\_LAST\_FIX(*time attribute, attribute1, attribute2, ...*) | Returns the latest date or timestamp according to the attributes specified in the function. Attributes added to the report will not affect the calculation but any filters applied will be taken into account. Example: DATE\_LAST\_FIX([Update - Timestamp], [Update ticket ID]) Returns the latest update timestamp per ticket, regardless of the attributes from the report. For more help and examples, see [Working with earliest and latest date functions](https://support.zendesk.com/hc/en-us/articles/4408833381402). |

### Formatting dates

The DATE\_FORMAT function render full timestamps as different types of dates. Each format is represented by a different letter. You enter the associated letter in the format part of the **DATE\_FORMAT** function. Letters must be entered in double quotes. You can combine the date or time components to display more information about a date.

For example, to change the default format (2015-01-27T13:21:10) of the **Ticket created - Timestamp** attribute to a US-style format (Jan 27, 2015 01:21 PM), use this formula:

```
DATE_FORMAT([Ticket created - Timestamp],"Mon DD, YYYY hh:MI AM")
```

The table shows formats you can use. The examples use the timestamp 2017-11-03T15:18:25.

| | | |
| --- | --- | --- |
| Date or time component | Letter | Example using 2017-11-03T15:18:25 |
| Year | YYYY | 2017 |
| Year | YY | 17 |
| Quarter | Q | Q4 |
| Month number | MM | 11 |
| Month name | Mon | Nov |
| Month name | Month | November |
| Week of year (1–53) | WW | 44 |
| Week of month (1-5) | W | 1 |
| Day number of year (01-366) | DDD | 307 |
| Day number of month (01-31) | DD | 3 |
| Day name of week | Day | Friday |
| Day name of week | Dy | Fri |
| Hour in day (01-12) | hh | 3 |
| Hour in day (1-23) | HH | 15 |
| Minutes | MI | 18 |
| Seconds | SS | 25 |
| Millisecond (000-999) | MS | 0 |
| Meridiem indicator (AM or PM) | AM | PM |

## Numeric functions

These functions enable you to perform a wide range of mathematical calculations on the information in your reports.

| Function | Description |
| ABS*(\_number)* | Returns the absolute value of the supplied number. Examples: The absolute value of **1** is **1** The absolute value of **-7.3** is **7.3** |
| BETWEEN*(\_number,\_number,\_number)* | Returns TRUE if the first supplied number is between the two other numbers. Example: BETWEEN(SUM(Profit),500,1500) returns TRUE if SUM(Profit) is equal to, or between 500 and 1500. |
| CEIL*(\_number)* | Returns the ceiling of the supplied number. The ceiling of a number is its highest closest or equal integer. Examples: The ceiling of 125.4 is 126 The ceiling of -63.2 is -63 CEILING(SUM(First resolution time (min))) returns the highest closest integer to each first resolution time stored in the attribute. |
| EXP*(\_number)* | Returns the value of the base of the natural logarithm (e) to the power of the supplied exponent. Example: EXP(SUM(Unit price)) returns the natural logarithm of each value of the SUM (Unit price) metric. |
| FLOOR*(\_number)* | Returns the floor of the supplied number. The floor of a number is its lowest closest or equal integer. Examples: The floor of 125.4 is 125 The floor of -63.2 is -64 FLOOR(SUM(First resolution time (min))) returns the lowest closest integer to each first resolution time stored in the attribute. |
| INTEGER*(\_param)* | Returns the integer of the supplied non-integer number. Example: INTEGER(1.56) returns 1 |
| IS\_NUMBER*(\_param)* | Returns TRUE if the given parameter is a number (integer or decimal) and FALSE if it isn’t. Examples:   - IS\_NUMBER(“-1234.987”) returns TRUE - IS\_NUMBER(“West”) returns FALSE |
| MAXIMUM*(\_number,\_number)* | Returns the largest of the two supplied parameters. MAXIMUM(SUM(Revenues),SUM(Expenses)) returns the larger of Revenues and Expenses. |
| MINIMUM*(\_number,\_number)* | Returns the smallest of the two supplied parameters. MINIMUM(SUM(Revenues),SUM(Expenses)) returns the smaller of Revenues and Expenses. |
| NUMBER*(\_param)* | Returns the number representation of the given parameter, or returns NaN when it cannot be displayed as a number. Examples: NUMBER("3.14116") returns 3.14116 NUMBER ([Box category]) returns the number of the current value of the Box category attribute. |
| PI*()* | Returns the mathematical constant for the ratio of the circumference of a circle to its diameter, expressed as PI. The value is 3.141592653589793. |
| POWER*(\_number,\_number)* | Computes and returns the first supplied number to the power of the second supplied number. Example: IF SUM(Unit Price)=2 then POWER(SUM(Unit Price),3) returns 8 |
| RANDOM*()* | Returns a pseudo-random number 'n' where 0<=n<1. If you need a random integer, use the formula Round(Random()\*100). |
| ROUND*(\_number)* | Rounds the value of supplied number up or down to the nearest integer. If equidistant, the value is rounded up. |
| SIGN*(\_number)* | Returns -1 if the number is negative, 0 if zero, and 1 if positive. |
| SQRT*(\_number)* | Computes and returns the square root of the supplied number. |
| SQUARE*(\_number)* | Computes and returns the square of the supplied number. |
| LN*(\_number)* | Returns the natural logarithm of the supplied number. |
| LOG10*(\_number)* | Returns the Base-10 logarithm of the supplied number. |
| LOG2*(\_number)* | Returns the Base-2 logarithm of the supplied number. |
| LOG*(\_base,\_number)* | Returns the logarithm of the supplied number to the supplied base. |

## Trigonometric functions

These functions help you to create advanced formulas for measuring angles and distances.

| Function | Description |
| ACOS*(\_number)* | Computes the arc cosine of the entered number, in radians. |
| ASIN*(\_number)* | Computes the arc sine of the entered number, in radians. |
| ATAN*(\_number)* | Returns the value in radians of the angle with the tangent entered in the parameter. The value returned is between negative PI/2 and positive PI/2. |
| ATAN2*(\_number,\_number)* | Returns the angle of the point Y/X in radians when measured counterclockwise from a circle's X axis (0,0 represents the center of the circle). The return value is between positive PI and negative PI. Enter the Y coordinate as the first parameter. |
| COS*(\_number)* | Computes the cosine of the entered number, in radians. |
| DEGREES*(\_number)* | Converts the given number from radians to degrees. |
| RADIANS*(\_number)* | Converts the given number from degrees to radians. |
| SIN*(\_number)* | Computes the sine of the entered number, in radians. |
| TAN*(\_number)* | Returns the tangent of the entered angle. |

## Comment functions

Use these operators to add comments to your formulas to explain how it works. This is helpful if you want to collaborate on formulas with other users, or if you want to make notes for yourself on why you built the formula the way you did.

| Operator | Description |
| /\* | Marks the start of a comment. |
| \*/ | Marks the end of a comment. |

Example: `/* this is a comment in a formula */`