# Product Updates - October 2025

Source: https://help.elationhealth.com/s/article/Product-Updates-October-2025

---

# What’s New?

Elation Health is excited to announce our latest updates designed to enhance your experience with our EHR, Billing and Developer Platform services. All of our releases focus on reducing documentation burden, streamlining workflows, and improving efficiency. Here's what's new:

- [Elation EHR updates](#EHR)
 - [A central place for product updates](#updates)
 - [Simplify patient insights in one click](#clinical_insights)
 - [Schedule ongoing care efficiently](#recurring_appointments)
 - [Calculate exact dosing every time](#dosage_calculator)
 - [Improve interoperability instantly](#Carequality)
 - [New bidirectional lab integration](#bidi_labs)
- [Elation Billing updates](#Elation_Billing)
 - [Elation Billing now supports multi-TIN practices!](#multi_tin)
 - [Spot downcoded claims immediately](#downcoded_claims)
- [Developer Platform updates](#Developer_Platform)
 - [Enhanced security and compliance](#security)
 - [Added new endpoints](#new_endpoints)
 - [Analyze clinical data with new hosted database tables](#new_tables)
 - [Stay updated](https://docs.google.com/document/d/17hm3lWV8FzDJcOwQARJ-FO9lv_vW5Vyd1ZfTu02m8l8/edit?tab=t.0#heading=h.fpb0i41kz3w4)

#

# **Elation EHR** updates

## **A central place for product updates**

You can find all the latest Elation product updates in one easy-to-access location—right inside your workflow. We know in-app messages and pop-ups don’t always come at the right time. That’s why we’ve added a permanent **Resource Center**, where you can catch up on new features and enhancements whenever it works for you. This means fewer interruptions and more control—so you can stay informed, adopt new tools at your own pace, and get the most out of Elation.

## **Simplify patient insights in one click**

The **Quick Action Buttons** makes extracting key patient insights easier and faster with just one click. These customizable buttons are located just beneath the Chronological Record search bar within a dropdown bar at the top of the patient chart. By default their behavior summarizes the last three visits, but you can tailor it to surface specific information so you can simply click a button instead of typing the same search prompt throughout the day. Learn how to customize your **Quick Action Button** to match your specific workflow in our [Chronological Records Guide](https://help.elationemr.com/s/article/using-the-search-tool-in-your-patient-chart#use_quick_action).

## **Schedule ongoing care efficiently**

**Recurring appointments** simplify ongoing care by allowing your front-office teams to schedule weekly, biweekly, or monthly visits in a single, streamlined workflow, saving them up to 15 minutes per patient. The system automatically carries forward key details and flags scheduling conflicts before saving, reducing errors and helping your staff be more efficient. Check out the [Calendar Guide](recurring-patient-appointments.md) for more information.

## **Calculate exact dosing every time**

Our new **weight-based pediatric calculator** assists you in calculating the appropriate sig and quantity for a pediatric prescription. The calculator automatically appears when you're prescribing and will surface the patient's weight, ensuring every dose is accurate for a child's size. By minimizing manual calculation errors, the calculator directly contributes to improved medication safety for children and offers major relief for clinicians when dosing varies. Check out our [Prescribing Guide](https://help.elationemr.com/s/article/Prescriptions-Forms-Guide-ePrescribing-and-ordering-meds) for more information  on using the calculator and integrating it into your practice.

## **Improve interoperability instantly**

Admins can now enable seamless data sharing through enhanced interoperability with a new self-serve opt-in into **Carequality**. This update lets your practice securely query and share patient data with other networks and EHRs via the Outside Care workflow—no manual setup required. Admins can enable it instantly in **Settings** → **Security & Privacy** → **Patient Data Sharing with Outside Care**, then accept the compliance checkbox. Remember to record patient consent before sharing. This streamlined process reduces admin work and improves care continuity. For more information on Carequailty, check out our [Carequality Integration Introduction](https://help.elationemr.com/s/article/Carequality-Integration-Introduction).

## **New bidirectional lab integration**

The following bidirectional lab integration is now available:

- [American Health Associates](https://americanhealthassociates.com/) - U.S.-wide diagnostics company delivering rapid, tech-enabled lab and mobile specimen services to healthcare providers and patients ― especially in long-term care and home settings.

Bidirectional lab interfaces enable eOrdering in addition to eResults, ensuring efficiency and accuracy when placing lab orders and reducing administrative burden and paperwork for your practice. Elation is thrilled to offer these integrations at no additional cost to its valued customers. Refer to our [Bidirectional Lab Interface Guide](Bidirectional-Lab-Interface-Guide.md) for more information.

# **Elation Billing** updates

## **Elation Billing now supports multi-TIN practices!**

The first iteration of multi-TIN claim submission in Elation Billing is here, allowing billers to specify the correct TIN, Taxonomy, and NPI at the claim level using the **More Fields** dialog on the Superbill. Look for our fully automated solution arriving by the end of the year! Check out our [Help Center](https://help.billing.elationemr.com/en/articles/7884140-how-elation-billing-corresponds-to-the-hcfa-1500) for more information.

## **Spot downcoded claims immediately**

In response to recent payer policy changes, we released changes to help you identify claims that have been downcoded. Elation will automatically identify and tag downcoded charges, adding the relevant claims to your Worklist for immediate review. Alerts will also display on the Superbill and Payment pages, giving you additional visibility into the downcoding events and allowing you to review the claim history and take action as needed. Look for additional updates in-app or review our [Help Center](https://help.billing.elationemr.com/en/articles/12453286-monitoring-for-downcoded-claims) for more information.

# **Developer Platform** updates

## **Enhanced security and compliance**

Elation is upgrading to SMART on FHIR V2, a secure, standards-based framework that enables approved apps to connect seamlessly to your EHR with stronger privacy controls, improved interoperability, and full compliance—without disrupting existing integrations.

## **Added new endpoints**

We’ve added new USCDI v3-aligned data elements to our FHIR and CCDA exports to improve completeness and ensure closer alignment with the Hosted Database model. This update reduces data gaps and makes downstream integrations and analytics more consistent.

## **Analyze clinical data with new hosted database tables**

Elation's Hosted Database (HDB) now includes beta Elation Note (VN2) tables that surface structured documentation data for deeper analysis in Snowflake. These new tables include key information such as custom blocks and signatures. Messaging threads also remain available through existing HDB messaging tables, enabling your teams to combine both documentation and communication insights in your analytics programs. This enhanced data access is crucial for sophisticated clinical analysis and quality improvement efforts. Check out our [Hosted Database Guide](https://help.elationemr.com/s/article/Elation-Analyst) for more details on integrating these new HDB tables into your analytics program.

## **Stay updated**

To stay informed of all the latest updates to our Developer Platform services, we recommend bookmarking the individual changelogs and monitoring them regularly.

- [API V2 changelog](https://docs.elationhealth.com/reference/changelog#2025-02-16)
- [Hosted Database changelog](https://elationhdb.readme.io/reference/hdb-snowflake)