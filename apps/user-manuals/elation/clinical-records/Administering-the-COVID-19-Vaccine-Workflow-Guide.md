# Administering the COVID-19 Vaccine Workflow Guide

Source: https://help.elationhealth.com/s/article/Administering-the-COVID-19-Vaccine-Workflow-Guide

---

If your practice has been approved to administer the COVID-19 vaccine, please use this step-by-step guide for recommendations of how to use Elation to recall patients, document vaccines, and report administration to your IIS.

If your practice has not been approved to administer the vaccine, but you have other questions about your COVIID-19 vaccination workflows, such as referring eligible patients or documenting vaccines administered elsewhere, please read our [COVID-19 Vaccination Recommendations](COVID-19-Vaccination-Recommendations.md) article.

### In the article we will cover:

1. ### [Configuring your settings to allow you to perform the COVID-19 vaccination workflows covered in this article](#one)
2. ### [Identifying patients who are eligible for the vaccine](#two)
3. ### [Scheduling patients who should be vaccinated](#three)
4. ### [Documenting the first dose of the vaccination](#four)
5. ### [Reporting the vaccines you have administered to the IIS](#five)
6. ### [Tracking and Recalling patients for the second dose of vaccine](#six)
7. ### [Documenting the second dose of the vaccination](#seven)

## 1.) Configuring your settings to allow you to perform the COVID-19 vaccination workflows covered in this article

### Calendar:

We recommend creating a [dedicated appointment type](calendar-and-booking-settings.md) in Elation to track your “COVID-19 Vaccine” visits. You can also consider making this appointment type available on your [Booking Site](Patient-Booking-Site.md) for patient self-scheduling.

### Patient Tags:

We recommend creating the following patient tags to allow you to track patients and their vaccination status for reporting and for recalling patients for second doses.

1. Create the following patient tag so that you can track vaccines that need to be reported to your IIS: **\*C-19 IIS Pending**
2. Create the following patient tags for the start of each upcoming week to allow you to easily track and recall patients who are due their second vaccine dose:**\*C-19 Due Wk *month/day* (ex. \*C-19 Due Wk 2/1, \*C-19 Due Wk 2/8, \*C-19 Due Wk 2/15)**

**User Tip:**Patient Tags appear in alphabetical order in the patient's chart. Any tag that begins with a punctuation mark will appear first, so adding the asterisks symbol will help draw attention to these COVID tags.

## 2.) Identifying patients who are eligible for the vaccine

Please remember to check and follow your local jurisdiction’s latest guidelines to determine which patients are eligible to receive the vaccine.

Use Elation’s [**Patient List**](find-patients-with-elations-patient-list.md) to identify who in your panel qualifies for their first dose of the vaccine.

1. Click “Reports >> Patient List” at the top of Elation.
2. On the left side, confirm which provider(s) you’re running the report for. Then apply the filters that you would like to use. For example:
   1. Check “Age” and specify patients older than 64.
   2. Check “Active Problems in Clinical Profile” and specify patients with certain high-risk diagnoses in their problem list.
   3. Check “Vaccinations in Clinical Profile” and exclude patients who already have a COVID-19 vaccine documented in their chart.
3. Click “Generate List” to generate the patient results. The patients will appear on the right side of the page.

##

## 3.) Scheduling patients who should be vaccinated

After drawing up your patient list, refer to the “Next Appointment” column to check if the patient has an upcoming appointment in the near future. If not, use the “Contact” column and call the patient to make an appointment.

You can also send a **[Bulk Letter](introduction-to-bulk-letters.md)**to these patients to share that they can make an appointment for their vaccine via Patient Passport or a mailer.

1. From the Patient List results, decide who you want to send the bulk letter to. To “select all”, click on the checkbox at the top of the page; to select specific patients, click the checkboxes next to each patient’s name.
2. Click “Send Bulk Letter”. Give the bulk letter a name and type in what you’d like the message to say.
3. Bulk letters will be delivered via Patient Passport to all patients who already have an account. If a patient doesn’t have an account yet but has their email and cell phone number recorded in Elation, you can choose to invite them to Patient Passport with the bulk letter. After they register, they’ll be able to see your message. For all other patients, you can choose to print a PDF along with their address cover page to mail the message.
4. After sending your Bulk Letter, you can check the Bulk Letter dashboard to check who has opened the message in their Patient Passport account.

If your staff are calling to schedule the patient’s initial appointment, consider also booking the follow-up appointment for Dose 2 before ending the call to increase the likelihood of recall.

## 4.) Documenting the first dose of the vaccination

When you administer the vaccine, document all fields [required by the CDC](https://www.cdc.gov/coronavirus/2019-ncov/lab/reporting-lab-data.html#what-to-report) to meet reporting requirements. These include:

| | |
| --- | --- |
| Patient Demographics | Vaccine Details |
| - Recipient name - Recipient ID - Recipient date of birth - Recipient sex - Recipient address | - Administration date - CVX (product) - Dose number - Lot number - MVX (manufacturer) - Vaccine administration site (on the body) - Vaccine expiration date - Vaccine route of administration - Vaccine administering provider’s name and suffix |
| The following practice-level Information also needs to be reported, but doesn’t need to be documented in each patient’s chart:   - Administration address (including Company) - Administering provider’s address, if different than the administration address |

1. Update patient demographics by clicking the patient’s name in their chart.
2. Document the vaccine by scrolling to the Immunization section of the Clinical Profile. Click “+ Add Vaccination Details”
3. Start typing the name of the vaccine and select the vaccine from the dropdown results. This will ensure that the CVX number is documented and pulls in any pre-saved vaccine details (for your convenience, Elation pre-fills the dose, lot number, manufacturer, and expiration date after the first time you document them).
4. Enter the required vaccine details in the corresponding fields.
5. Click “Save”.

![]()

Apply the following patient tags (by clicking on "+ Tags" to the right of the patient's name) to the patient’s chart.

1. **\*C-19 IIS Pending** (to identify that this vaccination needs to be reported to the IIS)
2. **\*C-19 Due Wk *month/day*** (use the tag that corresponds with the week the patient should return for Dose 2)

Check the appointment summary in the Clinical Profile to see if the patient has an upcoming appointment for Dose 2 by the recommended deadline. If they do not, make sure that someone in the practice schedules the patient before they leave.

## 5.) Reporting the vaccines you have administered to the IIS

Reporting deadlines vary by state, but it needs to be completed within 72 hours at the latest. Please follow the steps below at the end of each day, or every 2-3 days depending on your state’s requirements.

1. Use the patient list to identify vaccines that have been administered.
   1. Click “Reports >> Patient List” at the top of Elation.
   2. On the left side, confirm which provider(s) you’re running the report for. Click the checkbox for the “Patient Tag” filter. Search for the **\*C-19 Pending IIS** tag and select it.
   3. Click “Generate Report”. At the top of the results, click “Download >> Download CSV” to save a copy of the results. Open the CSV spreadsheet and also keep the Elation patient list results open.
2. Log into your state IIS and report the vaccination details according to their requirements.
   1. For patient demographics: Open the spreadsheet that you downloaded from the Patient list results. Each patient’s name, ID, date of birth, sex, and address will be documented here. Transfer this information to your IIS using the workflows advised by the IIS entity.
   2. For vaccine details: Click the patient’s name from the Patient List results to open their chart. Scroll to the Immunization section of the Clinical Profile. Click the vaccine name to view the administration details. Transfer this information to your IIS using the workflows advised by the entity. Once the information has been transferred, click on the **\*C-19 Pending IIS** tag. Click “x” to remove it from the patient’s chart to indicate that the reporting is complete.

## 6.) Tracking and Recalling patients for the second dose of vaccine

1. Click “Reports >> Patient List” at the top of Elation.
2. On the left side, confirm which provider(s) you’re running the report for. Click the checkbox for the “Patient Tag” filter. Type in the **\*C-19 Due Wk *month/day*** tag that you want to filter for.
   1. Pick the tag that matches the current week if you want to find patients who are due this week.
   2. Pick tags in the future if you want to find patients who are due back soon.
   3. Pick tags from the past if you want to find patients who are past due for Dose 2.
3. Click “Generate Report”. Check to see if patients have upcoming appointment dates in the report results and reach out to schedule any patients who do not.

## 7.) Documenting the second dose of the vaccination

Use the [documentation instructions for Dose 1](#four) to document the second dose of the vaccine for the patient.

Update the Patient tags:

- Click on the **\*C-19 Due Wk *month/day*** tag, and click the “x” button to remove it from the chart because the second dose is complete.
- Add the tag for **\*C-19 IIS Pending**