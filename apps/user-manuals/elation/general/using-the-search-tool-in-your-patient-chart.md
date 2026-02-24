# Chronological Record Guide - Searching for records in the patient's chart

Source: https://help.elationhealth.com/s/article/using-the-search-tool-in-your-patient-chart

---

# **Contents**

- [Overview](#Overview)
 - [How do I search for information in my patient’s chart?](#description)
 - [What are Clinical Insights?](#Clinical_Insights_overview)
 - [What are the benefits of Clinical Insights?](#benefits)
- [Setup](#setup)
 - [Configuring Clinical Insight display settings](#display_settings)
 - [Configuring custom instructions for Clinical Insights](#custom_instructions)
 - [Configuring the Clinical Insights Search Bar Quick Action](#configure_quick_action)
- [Workflow Instructions](#Workflows)
 - [Searching for documents using keywords](#keywords)
    - [Viewing Clinical Insights](#view_insights)
      - [Using Clinical Insights Search Bar Quick Action](#use_quick_action)
 - [Using search filters](#DocumentFilters)
 - [Using special search terms](#special_search_terms)
    - [Vitals](#vitals)
    - [Lab Results](#labs)
- [Glossary](#glossary)
 - [Example Clinical Insight searches](#search_examples)
    - [Example Clinical Insight searches for Pediatrics](#search_examples_for_pediatrics)

# **Overview**

## **How do I search for information in my patient’s chart?**

Quickly find what you're looking for in a patient's chart using the search box or filters at the top of the Chronological Record. You can also use AI-powered Clinical Insights to get a summarized view of relevant information, or enter special search terms to pull up corresponding data tables. Combine the search tool with [Document Tags](tag-reports-and-notes-with-document-tags.md) to build stronger searches.

Documents in **Requiring Action** or **Outstanding Items** are excluded.

## **What are Clinical Insights?**

The AI-powered Clinical Insights feature lets you search a patient’s chart, then surfaces and summarizes relevant information, displaying the results with citations at the top of the chart. The Clinical Insights feature is optimized for searching for the following:

- Clinical Reminders - searches for [preventive care follow up history](https://help.elationemr.com/s/article/clinical-reminders-for-clinical-quality-measures).
- Conditions - searches for a known diagnosis/condition.
- Health Maintenance - searches for [health maintenance history](https://help.elationemr.com/s/article/health-maintenance).
- Medication - searches for the drug name (generic or brand).
- Symptom - searches for a clinical sign/symptom.
- Preventive screening - searches for information about a preventive procedure or test.
- Vaccination history - searches for vaccination records in the chart.

You can view multiple Clinical Insights searches at once to keep each clinical question distinct to compare findings, preserve your search history, and share results.

ℹ️   **NOTE** Clinical Insights is an informational tool only and is not intended to replace professional medical judgment or serve as a clinical decision-making tool. Always verify information and make clinical decisions based on your own expertise and the patient’s complete medical record.

## **What are the benefits of Clinical Insights?**

Clinical Insights summarizes key information for you, so you don't have to spend time searching for it yourself. This helps you quickly find the information you need in reports and notes, so you don't have to spend time searching or requesting data that's already available.

# **Setup**

## **Configuring Clinical Insight display settings**

By default, Clinical Insights can only be accessed on demand when you search the Chronological Record. You can enable a setting to generate insights automatically when you search by following these steps:

| | |
| --- | --- |
| **1** | Click on your **email address** in the upper right corner of Elation. |
| **2** | Click **Settings**. |
| **3** | In the left-hand menu, click **AI Personalizations**. |
| **4** | Under the **Clinical Insights** section, go to **Display Settings** and select **Automatic (recommended)**. |

## **Configuring the Clinical Insights Search Bar Quick Action**

You can launch preset Clinical Insights searches from the search bar at the top of the patient's chart. The default search is *"Summarize the patient's most recent visits, highlighting any care plan items that need follow up."*

To define define and edit preset searches:

| | |
| --- | --- |
| **1** | Access your AI Personalizations Settings using one of these two workflows:   1. Click on your **email address** in the upper right corner of Elation -> **Settings** -> **AI Personalizations**. 2. In any patient's chart, click on the **Quick Action dropdown** and click **Personalize Quick Actions**. |
| **2** | Under the **Clinical Insights** section, go to **Search Bar Quick Action** and click **+ Add Quick Action**. |
| **3** | Update the following data for the preset search:   - **Search Title** - The name of the button in the chronological record search bar and title of the search that will appear at the top of the search results. - **Search Query** - The query that will automatically be triggered when you click the Button Label. |
| **4** | Data entered will be automatically saved. |
| **5** | Use the grid menu button to drag and drop the quick action into the desired order as needed. We will fit as many quick action buttons below the Chronological Record Search bar as the screen allows. Quick action buttons that don't fit will be available under the **More** button. |

## **Configuring custom instructions for Clinical Insights**

While using Clinical Insights doesn’t require personalization, you have the option to tailor the responses to better match your preferences. Each user must set their own custom instructions.

| | |
| --- | --- |
| **1** | Click on your **email address** in the upper right corner of Elation. |
| **2** | Click **Settings**. |
| **3** | In the left-hand menu, click **AI Personalizations**. |
| **4** | Under the **Clinical Insights** section, go to **Custom Instructions** and click **+ Add New Instruction** to type a custom rule (e.g. “List lab results as a bulleted list”) or select one of our **sample instructions** from the provided list.   1. Click the **trash can** icon if you’d like to delete a rule. |
| **5** | Changes are automatically saved. |

# **Workflow Instructions**

## **Searching for documents using keywords**

To look for all documents related to a specific topic, type a related search word or phrase into the search box (e.g. **diabetes** or **accident**). After you search, the chart will display related information and documents at the top of the chart. You'll see any matching text in the documents highlighted in yellow. To search for multiple topics, type the additional search term in the search box after the results for the first search term is generated.

To return to the full chart view, simply clear your search by clicking the **X** next to the search term(s).

### **Viewing Clinical Insights**

Search for conditions, medications, symptoms or preventative screening information using Clinical Insights.

- You will see one of two behaviors depending on which [display setting](#display_settings) you have enabled for Clinical Insights:
 1. **Automatic**: After you type a search term, AI automatically finds relevant insights and displays them in the Clinical Insights section.
 2. **Manual**: After you type a search term, click **Generate Clinical Insights for…** to surface clinical insights related to your search.
- All insights include citations, so you can easily see where it came from. Click on the citation numbers to open the referenced chart record.
- If you'd like to ask follow up questions for any of the insights, simply type your follow up question into the **Dive deeper into the data with a follow-up question box**.

#### **Using Clinical Insights Search Bar Quick Action**

The Clinical Insights Search Bar Quick Action buttons are located right below the chronological record search bar at the top of the chart. We will fit as many quick action buttons below the Chronological Record Search bar as the screen allows. Quick action buttons that don't fit will be available under the **More** button. Click any of the buttons to run a preset search as specified in your [AI Personalization Settings](#configure_quick_action).

## **Using search filters**

The following built-in filters let you quickly search for specific types of documents:

- **Note Type** - Surface all visit notes with a specific [visit note category](visit-note-categories.md).
- **Document Type** - Surface all documents that match one of the following document types:
 - **Letters & Referrals**
 - **Medications**
 - **Messages**
 - **Non-Visit Notes**
 - **Order**
 - **Pt Summaries (CCD/CCDA)**
 - **Reports**
 - **Visit Notes**

## **Using quick view buttons**

The following quick view buttons under the chronological record search lets you pull up the following data with the click of a button.

- **My Last Visit Note** - Jump to the last signed visit note.
- **Vitals** - Opens the vitals trend table.
- **Labs** - Opens a table that shows all of the patient's structured lab results.

## **Using special search terms**

### **Vitals**

To see a patient’s vitals trend table and visualizations, click the **Vitals** filter under the chronological record search box.

- To search for a specific vital, type in the vital name (e.g. **BMI** or **BP**).
- To adjust the time window, click the **Time Window** dropdown and select the desired timeframe.

### **Lab Results**

To see a table of all of the patient's structured lab results, click the **Labs** quick view button.

To see tables and visualizations related to [electronic lab results](https://help.elationemr.com/s/article/Viewing-results-from-lab-interfaces), [manually entered lab values](record-structured-data-from-in-house-or-faxed-lab-reports.md) or lab results recorded using the [Point-of-Care Labs feature](point-of-care-labs.md), type in related search terms.

- Lab values in blue = within normal reference range
- Lab values in red = outside of normal reference range

Reference the table below for search terms you can use and the results they will yield:

# **Glossary**

## **Example Clinical Insight searches**

| |
| --- |
| Provide a checklist of care protocols to review with the patient today. |
| Summarize relevant lab trends, monitoring recommendations, and protocol-driven actions for today. |
| Summarize *[insert chronic condition]* management plan, including medications, labs, and monitoring protocols. |

### **Example Clinical Insight searches for Pediatrics**

| |
| --- |
| Summarize key trends from the last 3 well-child visits: growth trajectory, developmental milestones achieved, outstanding screening gaps and parental concerns that were deferred or remain unresolved. |
| Show me what vaccines this patient is due for based on their age. Highlight any they are overdue for based on AAP guidelines. |
| Draft a parent-friendly handout about any medications prescribed, discussing expected course, worrisome signs or symptoms to contact me about and when to contact me. |
| Draft a parent-friendly after-visit summary of *[insert diagnosis]*, reading level 6th grade, emphasizing which red flags are reasons for returning to see me. |

**Next Step**

**Explore the Chronological Record Search today to narrow your search for specific records!**

# **Related Articles**

- [Chronological Record Introduction- A timeline of your patient's records](store-everything-in-chronological-record.md)
- [Chronological Record Guide- Sort Settings](chronological-record-sort-settings.md)
- [Document Tags for Visit Notes & Reports Guide](tag-reports-and-notes-with-document-tags.md)
- [Lab Orders & Results - Managing electronic lab results](https://help.elationemr.com/s/article/Viewing-results-from-lab-interfaces)
- [Lab Result Documentation Guide- Point-of-Care Labs](point-of-care-labs.md)