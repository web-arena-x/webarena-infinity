# Troubleshooting: Student Data Discrepancies

Source: https://support.joinhandshake.com/hc/en-us/articles/360009221914-Troubleshooting-Student-Data-Discrepancies

---

This article will help you navigate issues related to inaccurate student data counts. We'll outline the reasoning, and highlight next steps to reconcile what you're seeing in Handshake with the data you find in your student information system.

### 

### Why is my data inaccurate?

If your data looks incorrect, this is most likely result of:

- Out-of-date student data - you should be regularly refreshing your student data, especially at the end of each semester
- Inaccurate data coming from your student information system - it's important that you're importing records that are the "source of truth" at your school
- Duplicate student accounts - we do not recommend approving "pending" student accounts for students that have an existing, imported account. For more information refer to [Managing and Merging Duplicate Student Accounts](https://support.joinhandshake.com/hc/en-us/articles/115002657968).

### 

### Things to keep in mind:

This information is coming from your student information system (SIS) so your **IT team, Registrar, or data team** are best equipped to assist. The Handshake Support team can outline the processes, confirm the required formatting, and help you update the data in Handshake - we just can't reconcile the data from the source of truth.

**A (throwback!) metaphor to help clarify:**

You can think of the process like a VCR - where the Importer is the VCR, Handshake is the TV that displays what the VCR processes, and your data files are the VHS tapes that you feed into the VCR.

The TV (Handshake) will display whatever the VCR (Importer) processes. The VCR will only process the right kind of tapes (student data) to confirm everything is formatted correctly. That said, there's no way for the VCR or the TV to know what exact film should be displayed - it relies on whoever is feeding the tape (student data) into the VCR to make the accurate "film" choice!

### 

### How to check if your student list is accurate in Handshake:

1. **Generate an Insights report** of your [full student list](https://app.joinhandshake.com/analytics/explore_embed?insights_page=ZXhwbG9yZS9nZW5lcmF0ZWRfaGFuZHNoYWtlX3Byb2R1Y3Rpb24vc3R1ZGVudHM_cWlkPW9lWUxTNXZmakZIRVhhS1NBdFV6V3cmZW1iZWRfZG9tYWluPWh0dHBzOiUyRiUyRmFwcC5qb2luaGFuZHNoYWtlLmNvbQ==) - including school year name
2. **Download the full report** (using little gear icon in upper right hand corner) to an Excel file. **Note**: If the download exceeds 5,000 rows, you will need to contact our Support team to request access to download more than 5,000 rows.
3. **Obtain a correct list of current students** from your Registrar office (if the data going through the importer is correct, you may want to just download that importer file)
4. **Compare the lists** from your Registrar and from the Insights report to ensure they match up. You may want to use student email as the unique identifier or anchor point. You could also use the username or auth identifier.
5. **Identify any gaps.** If there are students that exist in the Handshake list and NOT in the registrar list they are likely either…

- Alumni
- Students who transferred / dropped out

### 

### Next steps to adjust:

**For alumni,** you will likely just want update their "school year" field to alumni. This article outlines the specific instructions for [Importer: Updating Graduating Students to Alumni](https://support.joinhandshake.com/hc/en-us/articles/227482608)

**For students who transferred or who did not complete their degree,** you can archive their accounts by following the steps in [Importer: Bulk Archiving Students](https://support.joinhandshake.com/hc/en-us/articles/115001497067) and learn more about archiving student accounts in [What Happens When I Archive a Student?](https://support.joinhandshake.com/hc/en-us/articles/37658603402519)

**Note:** Students will still be able to access Handshake if they are archived, they just won't be connected to your institution after they attempt to log in. In some cases, you may want to block students from using Handshake while remaining connected to your institution. Refer to this article for more information: [How to Block a Student](https://support.joinhandshake.com/hc/en-us/articles/219133287)

**For any additional student groups,** you might also consider [Importing Labels](https://support.joinhandshake.com/hc/en-us/articles/229507687). You can then use this labels to filter on your analytics moving forward.

**For data discrepancies**, use the attachment below to help identify and resolve data discrepancies.

### 

### If you're still running into issues:

Additionally, you can connect with our Support team to confirm that you have followed the process outlined above and to provide specific details, such as:

- Student lists/reports you're exploring (Insights URLs or Handshake URLS are especially important)
- Specific discrepancies you've identified (Exact counts and examples are best)
- Any additional context, concerns, and details