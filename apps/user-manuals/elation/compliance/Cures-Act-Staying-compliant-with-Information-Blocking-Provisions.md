# 21st Century Cures Act Guide- Staying compliant with Information Blocking Provisions

Source: https://help.elationhealth.com/s/article/Cures-Act-Staying-compliant-with-Information-Blocking-Provisions

---

## **Contents**

- [21st Century Cures Act- Information Blocking Provisions Overview](#overview)
- [How your practice can stay compliant](#practice_compliance)
- [Information Blocking Exceptions](#exceptions)
- [Additional Resources](#additional_resources)

## **21st Century Cures Act- Information Blocking Provisions Overview**

Information Blocking is a practice that

1. is likely to interfere with access, exchange, or use of electronic health information (unless required by law or covered by an [exception](#exceptions)) and
2. if conducted by a health IT developer of certified health IT, health information network or health information exchange, such developer, network or exchange knows, or should know, that such practice is likely to interfere with access, exchange, or use of electronic health information; or
3. if conducted by a health care provider, such provider knows that such practice is unreasonable and is likely to interfere with access, exchange, or use of electronic health information.

The [21st Century Cures Act](21st-Century-Cures-Act-and-Elation-EHR.md) (“Cures Act”) Information Blocking provision took effect April 5th, 2021. The Information Blocking provision states that healthcare providers are required by law to make a core set of clinical data available to patients in a timely fashion to encourage interoperability and portability of Electronic Health Information (EHI).

- Electronic Health Information is defined as “the electronic protected health information (ePHI) in a designated record set (as defined in the Health Insurance Portability and Accountability Act (HIPAA) regulations) regardless of whether the records are used or maintained by or for a covered entity” ([§170.401](https://www.healthit.gov/condition-ccg/information-blocking)).
- **From April 5, 2021 to October 6, 2022**, EHI is limited to the data classes represented in the US Core Data for Interoperability (USCDI) v1 standard. ([Read more about the USCDI v1 dataset here.](Cures-Act-Patient-Data-and-USCDI.md))
- **From October 6, 2022 onward**, EHI includes all ePHI in the designated record set that is transmitted in any electronic media or maintained in any electronic media.

## **How your practice can stay compliant**

1. Establish practice policies to provide Patient access to their health information in a timely manner upon patient request. You can use Elation’s Patient Passport feature to easily meet this requirement. [Read more about Patient Passport here](https://help.elationemr.com/s/article/elation-patient-passport-an-introduction).
   - Once Patients have activated their Patient Passport account, they will have access to their EHI via a combination of individually attached records AND a CCDA file.
     - **Important Note**: Due to the expanded definition of EHI **after October 6, 2022**, Elation’s CCDA files with USCDI v1 data elements will NOT include all ePHI as defined in the 21st Century Cures Act. Data elements not included in USCDI v1 will need to be [shared as attachments via Patient Letters](https://help.elationemr.com/s/article/how-to-send-a-letter-on-elation#Patient).
       1. Examples of data elements not included in USCDI v1 are test orders & referral letters.
       2. Elation CCDAs will not include non-visit notes or visit notes with dates of service **prior to April 5, 2021**. Non-visit notes and visit notes **prior to April 5, 2021** can be shared with patients via a Patient Letter.
2. Ensure patient information is shared with the authorized individuals according to your state guidelines.
3. Establish practice policies to exercise information blocking only when certain exceptions have been met.
   - [Read more about the 8 exceptions](#exceptions)
   - [Instructions on how to use the confidential section to store exceptions](https://help.elationemr.com/s/article/confidential-items-in-your-patient-chart)




## **Information Blocking Exceptions**

The Cures Act established 8 exceptions that may be applied to Information Blocking provisions. There are specific conditions that must be met for the Exception to apply. We encourage you to [read more about the Exceptions here](https://www.healthit.gov/cures/sites/default/files/cures/2020-03/InformationBlockingExceptions.pdf) and to consult with a legal resource regarding how the Cures Act may impact your practice and whether the Information Blocking Exceptions may be applicable.

Exceptions that involve not fulfilling requests to access, exchanges, or use electronic health information (EHI):

- **Preventing Harm Exception**: It is necessary and reasonable to prevent harm to a patient or another patient.
- **Privacy Exception**: It is necessary to protect an individual’s privacy.
- **Security Exception**: It is necessary to protect the security of EHI.
- **Infeasibility Exception**: It is not possible due to infeasibility of the EHI request.
- **Health IT Performance Exception**: If it is not possible due to health IT temporarily being unavailable or if the request would degrade health IT’s performance.

Exceptions that involve procedures for fulfilling requests to access, exchange, or use EHI:

- **Content and Manner Exception**: The content of the request may be limited as long as the required EHI elements are present and the actor may use an alternative method to fulfill the request if the manner requested is not technically possible or not possible in agreeable terms.
- **Fees Exception**: Charging fees is acceptable within a reasonable profit margin.
- **Licensing Exception**: Interoperability elements to access, exchange, and use EHI may be licensed

To block patient data from being shared with patients, in accordance with the exception scenarios above, use the Confidential section of the Clinical Profile. [Instructions on how to use the confidential section to store exceptions](https://help.elationemr.com/s/article/confidential-items-in-your-patient-chart).

## **Additional Resources**

- [21st Century Cures Act: Interoperability, Information Blocking, and the ONC Health IT Certification Program Final Rule in the Federal Register](https://www.federalregister.gov/documents/2020/05/01/2020-07419/21st-century-cures-act-interoperability-information-blocking-and-the-onc-health-it-certification)
- [ONC Information Blocking FAQs](https://www.healthit.gov/curesrule/resources/information-blocking-faqs)
- [Information Blocking Exceptions Information Sheet](https://www.healthit.gov/cures/sites/default/files/cures/2020-03/InformationBlockingExceptions.pdf)

## **Related Articles**

- [21st Century Cures Act Introduction](21st-Century-Cures-Act-and-Elation-EHR.md)
- [21st Century Cures Act Guide- Patient CCDAs and U.S. Core Data for Interoperability (USCDI)](Cures-Act-Patient-Data-and-USCDI.md)
- [Elation Patient Passport Guide](elation-patient-passport-an-introduction.md)
- [Letters & Referrals Guide- Sending messages to patients & corresponding with third party professionals](how-to-send-a-fax.md)
- [Patient Chart Guide- Managing confidential records](confidential-items-in-your-patient-chart.md)