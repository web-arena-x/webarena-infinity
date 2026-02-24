# Clinical Profile Guide - Viewing growth charts for pediatric patients

Source: https://help.elationhealth.com/s/article/growth-charts-for-pediatric-patients

---

# **Contents**

- [Overview](#Overview)
 - [What are growth charts?](#description)
 - [How do growth charts work?](#how_does_it_work)
 - [Which growth charts are available?](#kinds_of_charts)
- [Workflow Instructions](#Workflows)
 - [Viewing growth charts](#viewing_growth_charts)
 - [Sharing growth charts](#share)
    - [Attaching growth charts to Letters or Referrals](#attach_growth_charts)
    - [Printing growth charts](#printing)
 - [Troubleshooting missing or unexpected percentiles](#troubleshooting)

# **Overview**

## **What are growth charts?**

Growth charts help you track a patient's height, weight, BMI, and head circumference distribution over time for patients 21 and younger. Elation's growth charts use the following guidelines:

- WHO guidelines for children from birth to 24 months.
- CDC guidelines for children between 2 and 20 years.

These growth chart standards are fixed and cannot be configured at the practice level. Elation automatically applies the appropriate standard based on the patient's age.

In addition to standard growth charts, you can also view growth charts for pre-term infants and patients with Down Syndrome.

## **How do growth charts work?**

Once you add a patient's height, weight, and/or head circumference in the Vitals section of a note, that data point will automatically plot on the corresponding growth chart. The percentiles for height, weight, and BMI will also appear on the charts.

Visit notes do not need to be signed in order for you to see vitals from that visit populated on the growth chart.

## **Which growth charts are available?**

There are five categories of growth charts available in Elation:

- 0-24 months (WHO)
 - Height
 - Weight
 - Age
 - Head Circumference
- 24-36 months (CDC)
 - Head Circumference
- 2-20 years (CDC)
 - Height
 - Age
 - BMI
- Pre-Term\*
 - Height
 - Weight
 - Head Circumference
- Down Syndrome (0-36 months)
 - Height
 - Weight
 - Head Circumference
- Down Syndrome (2-20 years)
 - Height
 - Weight
 - BMI
 - Head Circumference

ℹ️   **NOTE** To plot values on the **Pre-Term** Growth Chart, you first need to add a preterm infant diagnosis to the patient's Problem List. The diagnosis must specify the number of weeks of gestation (e.g., "Preterm infant, birth weight 500-749 grams, with 24 completed weeks of gestation"). Additionally, the vitals must be recorded on a visit note that is dated before the 40-week gestation period to appear on the chart.

# **Workflow Instructions**

## **Viewing growth charts**

You have four options for accessing growth charts in Elation:

| | | |
| --- | --- | --- |
| **Clinical Profile** | Click **Growth Charts** at the top of the Clinical Profile. | |
| Go to **Other Info** -> **Actions** -> **See Growth Charts** | |
| **Legacy Visit Note** (any 2-column format) | Go to **Vitals** -> **Growth Charts** | |
| **Elation Note** | Go to the **Vitals & Observations** block -> **Growth Charts** | |

Here's how to read a growth chart:

- The chart is color-coded to help you easily identify percentile trends.
- The patient’s vitals are marked by a dark blue dot. You can hover over any dot on the graph to see the exact value, percentile and record date.
- To view the patient's growth chart data in a table format, simply scroll down within the growth chart window.

## **Sharing growth charts**

### **Attaching growth charts to Letters or Referrals**

To attach a growth chart to a Patient Letter, Provider Letter or Referral:

1. Open a new **Patient Letter**, **Provider Letter** or **Referral** draft.
2. Click **Select Chart Items to Attach**.
3. Select **Growth Charts**.
4. Select the growth charts you want to attach.
5. Click **Attach Items**.

### **Printing growth charts**

Click the **Print Chart** button at the top of each growth chart to print a growth chart. Growth charts will print in black and white. The percentile lines and exact value will be printed but the exact percentile of each value will not be printed.+

**💡**  **USER TIP** If you would like to print a growth chart in color, we recommend taking a screenshot (or snippet) of the screen and printing out the screenshot/snippet.



## **Troubleshooting missing or unexpected percentiles**

If percentiles are not displaying on a growth chart or appear incorrect, verify the following:

| | |
| --- | --- |
| **1** | **Confirm the patient's age is within the supported range** - Growth charts are only available for patients 20 years and younger. - The patient must have a date of birth recorded in their demographics to calculate age-appropriate percentiles. |
| **2** | **Confirm the Sex field is correct** Open the patient's demographics and verify the **Sex at birth** field matches the patient's biological sex. Growth standards differ by sex, so an incorrect or missing value will affect percentile calculations. |
| **3** | **Confirm vitals are entered as structured data** - Height, weight, and head circumference must be entered in the **Vitals** section of a visit note or Elation Note. - Vitals documented in scanned PDFs, free-text notes, custom blocks, or imported documents will not populate growth charts. |
| **4** | **Verify measurement dates** Each vital must have a valid measurement date. Vitals without valid dates cannot be plotted on the chart. |
| **5** | **Check for special population requirements** - **Pre-term infants:** To use the Pre-Term Growth Chart, you must first add a preterm infant diagnosis to the patient's **Problem List**. The diagnosis must specify the number of weeks of gestation (e.g., "Preterm infant, birth weight 500-749 grams, with 24 completed weeks of gestation"). Vitals must also be recorded on a visit note dated before the 40-week gestation period. - **Down Syndrome:** Patients with Down Syndrome documented in their Problem list will have their percentiles displayed on the appropriate Down Syndrome growth chart. |
| **6** | **Confirm the correct chart type is displaying** Elation automatically selects the chart type based on the patient's age and any relevant diagnoses. If a patient appears on an unexpected chart, verify their date of birth and Problem List entries. |

If further assistance is required after following the above troubleshooting steps, click **I need help** -> **Contact Elation Support** to submit a request.

# **Related Articles**

- [Visit Note Documentation Guide- Visit Note Formats](Visit-Note-Documentation-Guide-Visit-Note-Formats.md)
- [Clinical Profile Guide- A snapshot of the patient's health status](clinical-profile-record-patient-medical-history.md)
- [Pediatric Features Guide](Pediatric-Features.md)