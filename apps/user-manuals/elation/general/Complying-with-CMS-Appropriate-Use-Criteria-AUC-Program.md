# Complying with CMS' Appropriate Use Criteria (AUC) Program

Source: https://help.elationhealth.com/s/article/Complying-with-CMS-Appropriate-Use-Criteria-AUC-Program

---

In this article, you will learn more about CMS' Appropriate Use Criteria (AUC) requirements and how to create advanced imaging orders that adhere to the AUC.

## Contents

1. [Background on PAMA and AUC](#background)
2. [Choosing a Clinical Decision Support Mechanism (CDSM)](#CDSM)
3. [How to create an advanced imaging order in Elation to meet requirements](#creating-order)
4. [Advanced imaging CPT® codes requiring CDSM consultation](#CPT-codes)
5. [Reporting requirements for CDSM consultations](#consulting-cdsm)

## Background

The Protecting Access to Medicare Act (PAMA) of 2014, Section 218(b), established the appropriate use criteria (AUC) program to ensure advanced imaging orders (CT, PET, nuclear medicine, and MRI) for Medicare patients that will be reimbursed by CMS are appropriate.

**What does this mean for your practice?** Starting on January 1st, 2021, providers will need to consult an AUC program for all advanced imaging orders for Medicare patients and provide furnishing provider information or the claim will not be reimbursed by CMS. Many imaging centers will not accept imaging orders for tests impacted by this program unless the proper AUC consultation information is provided.

The AUC consultation must occur when the advanced imaging is ordered and can be delegated to clinical staff. Please note that providers whose ordering patterns are considered by CMS to be outliers could be subject to prior authorization before future orders.

**Who does this impact?**This program impacts all physicians and practitioners (1861(r) or 1842(b)(18)(C)) “that order advanced diagnostic imaging services and physicians, practitioners and facilities that furnish advanced diagnostic imaging services in a physician’s office, hospital outpatient department (including the emergency department), an ambulatory surgical center or an independent diagnostic testing facility (IDTF) and whose claims are paid under the physician fee schedule, hospital outpatient prospective payment system, or ambulatory surgical center payment system.” ([From CMS AUC Program page](https://www.cms.gov/Medicare/Quality-Initiatives-Patient-Assessment-Instruments/Appropriate-Use-Criteria-Program).)

**Are there any exceptions?**Yes - AUC does not need to be consulted before ordering advanced imaging in the following situations:

- Emergency services
- Inpatients and Medicare part A payments
- Providers with significant hardship

### Choosing a Clinical Decision Support Mechanism (CDSM)

CMS has approved many clinical decision support mechanisms (CDSMs) to consult AUC, which can be reviewed [here](https://www.cms.gov/Medicare/Quality-Initiatives-Patient-Assessment-Instruments/Appropriate-Use-Criteria-Program/CDSM). Your practice may consult any of these CDSMs in order to retrieve the information necessary to include on imaging orders to meet CMS program requirements. Free CDSMs are marked with an asterisk on this list.

### How to create an advanced imaging order in Elation to meet requirements

To easily meet CMS AUC requirements for imaging orders placed in Elation, please follow the steps below. Note that this process only needs to be followed for advanced imaging tests (see the set of relevant test codes in the section below).

1. Create an imaging order by clicking on the Orders>Imaging Orders button in the grep action bar within a patient's chart
    ![]()
2. Fill out the required fields in the Imaging Requisition Form, including: Test, Reason, Imaging Center
    ![]()
3. Consult your clinical decision support mechanism (CDSM).
   - Have the following information readily available:
     - Patient age and gender
     - Requested advanced imaging service (e.g. MRI spectroscopy head/brain w/o contrast), and
     - Indication (e.g. headache, infection suspected).
   - The CDSM will report an appropriateness score (1-9) for the selected imaging service and will suggest other imaging services based on the patient demographics and indication. Select an imaging service.
   - The CDSM will then generate a Decision Support Number, with a summary of the appropriateness score, adherence results (e.g. adheres to AUC), G-code (e.g. CDSM CareSelect’s is G1004), and modifier (e.g. ME).
4. Back in the Elation Imaging Requisition Form, click “more…” and copy and paste the AUC information into Instr/Notes of the imaging order.
    ![]()
5. Click Print & Close and send the Imaging Order to the imaging center. [Read more about faxing an imaging order or referral.](efaxing-lab-and-radiology-orders.md)
    ![]()

### Advanced imaging CPT codes requiring CDSM consultationper the [January 2020 CMS AUC imaging bulletin](https://www.cms.gov/Outreach-and-Education/Medicare-Learning-Network-MLN/MLNMattersArticles/Downloads/MM11268.pdf), the advanced imaging CPT codes requiring AUC review include:

| Advanced Imaging test | CPT Codes |
| --- | --- |
| CT | 70450, 70460, 70470, 70480, 70481, 70482, 70486, 70487, 70488, 70490, 70491, 70492, 70496, 70498, 71250, 71260, 71270, 71275, 72125, 72126, 72127, 72128, 72129, 72130, 72131, 72132, 72133, 72191, 72192, 72193, 72194, 73200, 73201, 73202, 73206, 73700, 73701, 73702, 73706, 74150, 74160, 74170, 74174, 74175, 74176, 74177, 74178, 74261, 74262, 74712, 74713, 75571, 75572, 75573, 75574, 75635, 76380, 76497 |
| MRI | 70336, 70540, 70542, 70543, 70544, 70545, 70546, 70547, 70548, 70549, 70551, 70552, 70553, 70554, 70555, 71550, 71551, 71552, 71555, 72141, 72142, 72146, 72147, 72148, 72149, 72156, 72157, 72158, 72159, 72195, 72196, 72197, 72198, 73218, 73219, 73220, 73221, 73222, 73223, 73225, 73718, 73719, 73720, 73721, 73722, 73723, 73725, 74181, 74182, 74183, 74185, 75557, 75559, 75561, 75563, 75565, 76498, 77046, 77047, 77048, 77049 |
| **Nuclear Medicine** | 78012, 78013, 78014, 78015, 78016, 78018, 78020, 78070, 78071, 78072, 78075, 78099, 78102, 78103, 78104, 78110, 78111, 78120, 78121, 78122, 78130, 78135, 78140, 78185, 78191, 78195, 78199, 78201, 78202, 78215, 78216, 78226, 78227, 78230, 78231, 78232, 78258, 78261, 78262, 78264, 78265, 78266, 78267, 78268, 78278, 78282, 78290, 78291, 78299, 78300, 78305, 78306, 78315, 78350, 78351, 78399, 78414, 78428, 78429, 78430, 78431, 78432, 78433, 78434, 78445, 78451, 78452, 78453, 78454, 78456, 78457, 78458, 78459, 78466, 78468, 78469, 78472, 78473, 78481, 78483, 78491, 78492, 78494, 78496, 78499, 78579, 78580, 78582, 78597, 78598, 78599, 78600, 78601, 78605, 78606, 78608, 78609, 78610, 78630, 78635, 78645, 78650, 78660, 78699, 78700, 78701, 78707, 78708, 78709, 78725, 78730, 78740, 78761, 78799, 78800, 78801, 78802, 78803, 78804, 78811, 78812, 78813, 78814, 78815, 78816, 78830, 78831, 78832, 78835, 78999 |
| **SPECT** | 76390 |

### Reporting requirements for CDSM consultations

All Medicare claims for advanced imaging orders (CT, MRI, Nuclear Medicine, and SPECT, see CPT codes below) must report:

1. HCPCS code (G-code): Code for the CDSM consulted.
2. Decision Support Number (DSN): unique number for AUC consultation.
3. HCPCS modifier (M-code): Code for CDSM AUC determination.

   - MA: Ordering professional is not required to consult a clinical decision support mechanism due to service being rendered to a patient with a suspected or confirmed emergency medical condition
   - MB: Ordering professional is not required to consult a clinical decision support mechanism due to the significant hardship exception of insufficient internet access
   - MC: Ordering professional is not required to consult a clinical decision support mechanism due to the significant hardship exception of electronic health record or clinical decision support mechanism vendor issues
   - MD: Ordering professional is not required to consult a clinical decision support mechanism due to the significant hardship exception of extreme and uncontrollable circumstances
   - ME: The imaging service ordered would adhere to specified applicable AUC
   - MF: The imaging service ordered would not adhere to specified applicable AUC
   - MG: The order for this service does not have appropriate use criteria in the clinical decision support mechanism consulted by the ordering professional
   - QQ: Ordering professional consulted a qualified clinical decision support mechanism for this service and the related data was provided to the furnishing professional

The name and NPI of the ordering provider who consulted the AUC if different from furnishing provider.

*CPT copyright 2019 American Medical Association. All rights reserved.*