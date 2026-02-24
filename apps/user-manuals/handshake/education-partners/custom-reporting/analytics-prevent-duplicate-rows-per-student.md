# Analytics: Prevent Duplicate Rows Per Student

Source: https://support.joinhandshake.com/hc/en-us/articles/360000868168-Analytics-Prevent-Duplicate-Rows-Per-Student

---

When reporting on student data, you may notice duplicate rows for one student, when you want each student condensed into one row. Here's a quick highlight of the filters you'll want to use as defaults.

## Primary Education = (yes)

You'll want to be sure to add this filter - it will make sure that it is only scoping to the student's education at your institution.

Navigate to the Educations field picker, on the left side of the report. Locate the the *Primary? (Yes/No)* dimension and click **Filter**:

![Screen_Shot_2018-03-27_at_11.08.02_AM.png](https://support.joinhandshake.com/hc/article_attachments/26001341983127)

This will auto-add to your list of filters at the top of the page:

![Screen_Shot_2018-03-27_at_11.08.08_AM.png](https://support.joinhandshake.com/hc/article_attachments/26001341982359)

## Name vs Name List

Using a Name List will identify the full list associated with each student, and add that information in one row, instead of separate rows for each unique name. The most common example for this is in pulling the Major Name, as students will often have double majors.

Instead of adding "Name" (highlighted in the screenshot below), you'll need to click "Name List" in the Measures subsection.

![Screen_Shot_2018-03-27_at_11.15.05_AM.png](https://support.joinhandshake.com/hc/article_attachments/26001302434455)

That will consolidate them on the right side of your report:

![Screen_Shot_2018-03-27_at_11.17.50_AM.png](https://support.joinhandshake.com/hc/article_attachments/26001302436119)

Name Lists are available for a variety of features in the Student template, such as:

- Career Interests
- Educations - Colleges
- Institution Labels
- Majors
- Minors
- Organizations
- School Year