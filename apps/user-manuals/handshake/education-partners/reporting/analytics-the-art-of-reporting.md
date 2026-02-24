# Analytics: The Art of Reporting

Source: https://support.joinhandshake.com/hc/en-us/articles/360003892314-Analytics-The-Art-of-Reporting

---

Handshake Analytics provides a way for you to explore, gain insight, then [save](analytics-using-saved-reports.md) and [share](https://support.joinhandshake.com/hc/en-us/articles/360036418494) your data. It's very important to understand how information is collected, and its relationship, to get the report that you are looking for. 

Reports in Handshake provide accurate data based on the selected filters and results, so the key to telling the desired story is ensuring that your report pulls back the intended data. Insights will only pull in data that exists in Handshake.

*Note: you'll need both* Analytics: Access*and*Manage *permissions in order to view and/or create reports. If you don't have these permissions, please reach out to your team's Handshake administrator to request access.*

**Reporting Basics**

Understanding items on the reporting page will help you better identify what you need. This section provides an overview, and there are more details in the dedicated sections for each item.

In the main portion of the page is the Data Table. This is where the data you've chosen to report on will be displayed.

On the left of the page is the Field Picker. This is where you choose what to display in the data table and how to find that data. Each report template has category names listed in the Field Picker –– click the category name to select “dimensions” and “measures” for your report. 

- **Dimensions**- What data do I want? Dimensions are the column descriptors of the data table.
- **Measures****-** What do I want to do with my data? Measures are the counts and/or math of data.

**Note**: Within Field Picker categories, dimensions will always be listed first in black text, and measures will be listed last in orange text. Within the data table, dimensions will default to the left of the table in blue text, and measures will display to the right in orange text.

Within each dimension and measure, there are "results", “filters”, and “pivots”:

- **Results**- What story do I want to tell? Results are the fields chosen to display in the data table. 
  - Click directly on the name of a dimension or measure to add that item as a result to your data table.
- **Filters** - How do I get the right data? Choosing the data that you are interested in.
  - Hover your mouse pointer over the dimension or measure, then slide it to the right and click Filter to add that item as a filter.
- **Pivots** - What if I have 2 questions? Pivoting enables dimensions to be displayed horizontally with counts. 
  - Hover your mouse pointer over the dimension, then slide it to the right and click Pivot to add the pivot to your data table.
  - **Note**: you can only pivot on dimensions by including a measure (count) in your data table.

In the upper-right corner of the page is the **Run** button to process your report. To the right of Run is a gear icon –– to download a report, click the gear icon, then click **Download**., select from the options that appear (including file format, name, etc.), then click the **Download** button in the lower-right corner.

Directly above the Run button are the options for duplicating, saving, or updating the report, which vary depending on how you accessed the reporting page (e.g. a Handshake pre-built report, a report you or a colleague saved, or a new custom report). 

![navigating_reporting_page.png](https://support.joinhandshake.com/hc/article_attachments/25995122540311)

**Reporting Page (additional details)**

Topics include: 

- [Data Table](#h_01ESKKX8SHGXAVZYS8X48GPRV9)
- [Results](#h_01ESKKXF2S6VHGKHPCE316FVCM)
- [Dimensions](#h_01ESKKXP9KDYFB3RNW01D0FTGC)
- [Measures](#h_01ESKKXWMKT635B1Y0CBK79BNJ)
- [Filters](#h_01ESKKY3VCXM67NPMXTBFQCGA9)

### Data table

Click on the word Data at the top of the data table to expand or collapse the table. 

![data_table_header.png](https://support.joinhandshake.com/hc/article_attachments/25995103960727)

- **Results**: displays selected data in formatted columns
- **Calculations**: allows you to manually configure calculations for results. For more information, refer to [Looker: Using Table Calculations](https://looker.com/docs/exploring-data/using-table-calculations).
- **Row Limit**: The default row limit is 50, and the maximum possible to display in Handshake is 5,000. For results beyond 5,000, you'll need to download the report and select **Download All Results** in the download confirmation. 
  - *If this option isn't available to you, you can request access to all rows by contacting our Support Team.*
- **Column Limit**: We do not have a limit on columns that you can add to a report, however, the more columns you add, the larger the report will be, which can potentially cause issues with the report running or data scoping properly.
- **Totals**: Check the Totals box to display column totals at the bottom of the data table. If you've already run the report, you'll need to click **Run** again after checking the totals box.
- **Row Totals**: Check the Row Totals box to display totals per row to the far right of the data table. If you've already run the report, you'll need to click **Run** again after checking the totals box.

**Note**: Totals only count unique values, so if a student is listed in two sections it'll only count them once. For example, if you are counting the number of students in multiple majors, and a student has both Economics and Business Admin, it'll only count them once in the row total, but both of the lines for Economics and Business Admin would include that student in their count, so this wouldn't represent a unique student count overall. 

**Tip***:* if you receive an error that states "Refusing to run query with no limit that Looker......" when including row totals on a report, select the “Results in Table” option instead of "Download All Results" AND ensure you've added a row limit to the report.

### Results

- **Sort results**: Within the data table, you can sort results alphabetically or numerically by clicking the column header name once or twice (to switch between descending/ascending).
- **Results with "0" values**: If your report has “0” values, you’re most likely not using the correct template, so it depends on what you are trying to report on. If you encounter this issue, try looking at another template that is based on the 'root' of the data.  
  - For example, if you are trying to run a list of employers that have never posted a job, you will want to use the Employer template instead of the Jobs template. Since the Jobs template is pulling from Jobs first, if that employer hasn't posted a job at your school, they would not be included. However, if you go to the Employers template, you can filter to employers who have a posting\_count (measure) less than 1.
- **Results with Null values:** Depending on the report, null values can appear for different reasons. 
  - **Education records:** If you're creating a report for a student's education records and did not filter for primary education only, the report may bring up their secondary education records. If the student has a high school listed as their secondary education, that will populate as a null value in the report.
  - **Employer approval date:** If the employer wasn't approved through traditional means (i.e. sent an Employer Approval URL), the value will appear as null. The system cannot recognize the date that the URL was sent, so it cannot make a correct "assumption" about the date, thus claims it to be null.
  - **Document Reviewer ID:** The system may not provide an ID for specific reviewers, so it is recommended to use **Document Review Staff** fields instead.
- **Combine results from different databases**: In general, data in Handshake is saved under the particular feature area where it was created –– for example, job types are saved in the Jobs template, so if you wanted to report on job types per on-campus interviews, you'd have to run two reports (one in Jobs and one in Interview Schedules), then merge the two reports using a vlookup in Excel. In this example, you would need to include the job\_id in both reports and then you can use a vlookup to merge the two data sets.

### Dimensions

- **Profile Completion**: Profile completion counts and percentages are included in the Student Engagement Dashboard. If you'd prefer to add profile completion information to a custom report, use the Students template, and refer to the Field Picker category Profile Completion for dimensions and measures.
- **'Registered' vs 'Checked in'**: Registered indicates the student registered for the fair or event, and Checked In = Yes indicates the student checked in to the fair or event. If the date has passed, and some students are registered but not checked in, this indicates they didn't attend the fair or event.

### Measures

- **Name lists**: this measure is particularly helpful if you would like to ensure each unique student (or item) has one row only. For example, if a student has a double major, and you include Major Name in the data table results, that student would be listed twice. Using Major Name List instead will list the student once, with both majors in one cell to the far right in the table.

### Filters

- Every dimension and measure within a template can be used as a filter.
- **Filter options**: when filtering using "is equal to" or "is not equal to", click once in the text field to populate a dropdown list of all available options.
- **Filtering using labels**: if your school uses labels, you can use the dimension insititution\_labels\_name, then select "is equal to" or "is not equal to" to include or exclude the label name(s).
- **Filter logic**: 
  - Within a single filter: the logic is "OR" –– for example: 
    - Major Name is equal to Business Administration OR Business Analytics OR Economics
    - School Year Name is equal to Sophomore OR Junior
  - Across 2 or more filters: the logic is "AND" –– for example: 
    - in order to be included in the results, the student must have one of the selected Major Names AND selected School Years
  - This is the default setting for reporting, however, the ability to select AND vs OR is possible via a custom filter. The following link provides more information on this process: [Looker Expressions: Functions and Operators](https://docs.looker.com/exploring-data/creating-looker-expressions/looker-functions-and-operators?version=5.10)
    - **Note**: when writing a custom filter, you are still limited to the dimensions and measures within the selected template's field picker. To bring in data from another template, you'd have to download the reports and combine the data in Excel.
    - The custom filter does work on customizable institution labels. It treats the values the same way as a major.
  - Filtering using "NOT" logic: if you are looking at a field for which there can be no more than one entry for a student (School Year Name, for example, assuming you have filtered on Educations), you can use the "does not equal to" filter as you would expect.   
    - If you are filtering on a field where a student may have more than one entry attached to their profile (Institution Label Name, Majors Name, etc.), you need to filter results differently -- for example:   
      - With labels, a student has a unique entry in our database for every label attached to their profile. If you use the "does not equal" filter for a specific label, it'll only filter out that one entry for the student. If the student has another label attached to their profile, they'll show up in your results.
      - To get around this, we want to add all of the labels attached to the student profile into one line within our data set by adding the "Label Name List" field. Then, you'd use the "doesn't contain" filter and enter the text for the label you'd like to exclude — This will filter out the entries as desired.
- **Filter value limits**: if you choose to copy results from one report and paste it into a filter on another report, there is no limit to how many results can be pasted at a time, however, the more values you paste, the longer the page will take to load. 
  - If you are pasting in hundreds of values, your browser may ask you if you want to close the page or wait (you may have to click "wait" a few times with a large number of values). In this case, we recommend breaking up the original report into smaller subsets to paste less filter values at a time.

**Tip**: once you've selected your filters, we recommend collapsing the **Filters** section to review the data and results more easily! Click the upside-down triangle symbol to the left of F**ilters** to collapse.

**Advanced Reporting Examples**

**I need to report on students with a particular label to see the events they attended this semester. The report needs to list each student and the names and dates of attended events. Some of the students will have been 'checked in' by the import process.**

- First, filter the student label with the Student Attendee Institution Label Name Field. With this filter you can select which label you'd like to report on.
- Next, select the following dimensions: Name from the Events field, Name from the Event Types field, Start Date from the Events field, and Checked In? under the Attendees field.
- Here's an example of this report: <https://app.joinhandshake.com/analytics/explore_embed?insights_page=ZXhwbG9yZS9nZW5lcmF0ZWRfaGFuZHNoYWtlX3Byb2R1Y3Rpb24vZXZlbnRzP3FpZD1aRHlsWmJUaDZTMkE1UWFiYXAxMG9CJmVtYmVkX2RvbWFpbj1odHRwczolMkYlMkZhcHAuam9pbmhhbmRzaGFrZS5jb20mdG9nZ2xlPWZpbA==>

**I need a report that calculates a percent of columns.**

- After building your report, click the Calculations button.

![Screenshot__6_.png](https://support.joinhandshake.com/hc/article_attachments/25995122537751)

- A box will appear where you can enter the formula - you can choose which fields you want to use for the formula. You can add a title for this new field and format the percentage too. Click Save Table Calculations to add it to the results.

![Screenshot__7_.png](https://support.joinhandshake.com/hc/article_attachments/25995122539671)

- Once the calculation is saved, a new column will load to the far right (with a green header) with percentages.
  - Here's an example of a report with the calculation: <https://app.joinhandshake.com/analytics/explore_embed?insights_page=ZXhwbG9yZS9nZW5lcmF0ZWRfaGFuZHNoYWtlX3Byb2R1Y3Rpb24vaW50ZXJ2aWV3X3NjaGVkdWxlcz9xaWQ9eUdXQ3k1TnNVdVlMZEREOUd1VjMwNSZlbWJlZF9kb21haW49aHR0cHM6JTJGJTJGYXBwLmpvaW5oYW5kc2hha2UuY29tJnRvZ2dsZT1maWw=>

**Best Practices and Reminders**

Analytics data is updated on a nightly basis –– this means any changes you've made in Handshake *today* (manually or via Importer) will be reflected in Analytics *tomorrow*. The update starts around midnight Pacific.

- Run only one report at a time for the most efficiency
- Start small and simple and work your way up to more complicated explores
- The best explores are those that return within a few seconds, if it takes longer than that you should try removing fields and starting simpler  
  - Also, more filters = less data
- All data can be downloaded to excel –– if you can’t do something in Analytics, you can always download the results and transform there
- Location searches - Filter on Lat\_long and use syntax of: "100 miles from 41.8781136, -87.6297982"
- Institution Labels are the labels created/applied to that item by your school.

### Additional Resources

- **Saved and Pre-Built Reports**
  - [Analytics: Using Saved Reports](analytics-using-saved-reports.md)
  - Pre-built reports are available in Handshake on the Analytics overview page. For more information, refer to the articles that start with "Pre-built Reports", in the Reporting section of our Help Center: [The Reporting Section](https://support.joinhandshake.com/hc/en-us/sections/204202028-Reporting).
- **Recorded Webinars**
  - For recorded webinars on Reporting, check out <https://learn.joinhandshake.com/hub/career-centers/webinars/>.
- **Support Options**
  - If you are having trouble pulling a report, you can always reach out [here](https://support.joinhandshake.com/hc/en-us/requests/new) with the link to the report and our Support Team can assist you!
- **External Resources**
  - [Looker Documentation](https://docs.looker.com/)
  - [Looker Help Center](https://help.looker.com/hc/en-us)