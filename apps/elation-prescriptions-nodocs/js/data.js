/* Elation Prescriptions — Seed Data */
const SEED_DATA_VERSION = 1;

const CURRENT_USER_PROVIDER_ID = 'prov_001';

const PROVIDERS = [
    { id: 'prov_001', firstName: 'Sarah', lastName: 'Mitchell', title: 'MD', specialty: 'Internal Medicine', deaNumber: 'BM1234563', npi: '1234567890', epcsEnrolled: true, isCurrentUser: true },
    { id: 'prov_002', firstName: 'James', lastName: 'Okafor', title: 'DO', specialty: 'Family Medicine', deaNumber: 'AO9876541', npi: '2345678901', epcsEnrolled: true, isCurrentUser: false },
    { id: 'prov_003', firstName: 'Linda', lastName: 'Reyes', title: 'MD', specialty: 'Internal Medicine', deaNumber: 'BR5432167', npi: '3456789012', epcsEnrolled: false, isCurrentUser: false },
    { id: 'prov_004', firstName: 'Michael', lastName: 'Brandt', title: 'NP', specialty: 'Family Medicine', deaNumber: 'MB6781234', npi: '4567890123', epcsEnrolled: true, isCurrentUser: false },
    { id: 'prov_005', firstName: 'Priya', lastName: 'Sharma', title: 'PA-C', specialty: 'Internal Medicine', deaNumber: 'PS3219876', npi: '5678901234', epcsEnrolled: false, isCurrentUser: false },
    { id: 'prov_006', firstName: 'Robert', lastName: 'Tanaka', title: 'MD', specialty: 'Cardiology', deaNumber: 'RT4567891', npi: '6789012345', epcsEnrolled: true, isCurrentUser: false }
];

const PATIENTS = [
    {
        id: 'pat_001', firstName: 'Margaret', lastName: 'Chen', dob: '1958-03-14', gender: 'Female', mrn: 'MRN-20180423',
        allergies: [
            { id: 'alg_001', substance: 'Penicillin', reaction: 'Anaphylaxis', severity: 'severe' },
            { id: 'alg_002', substance: 'Sulfa drugs', reaction: 'Rash', severity: 'moderate' },
            { id: 'alg_003', substance: 'Codeine', reaction: 'Nausea/Vomiting', severity: 'mild' }
        ],
        preferredPharmacy: 'pharm_001',
        insurance: { plan: 'Medicare Part D', memberId: '1EG4-TE5-MK72', group: 'RX7834', bin: '610014', pcn: 'OHCP' }
    },
    {
        id: 'pat_002', firstName: 'David', lastName: 'Kowalski', dob: '1975-09-28', gender: 'Male', mrn: 'MRN-20190817',
        allergies: [
            { id: 'alg_004', substance: 'Aspirin', reaction: 'GI Bleeding', severity: 'severe' },
            { id: 'alg_005', substance: 'Ibuprofen', reaction: 'GI Bleeding', severity: 'severe' }
        ],
        preferredPharmacy: 'pharm_003',
        insurance: { plan: 'Blue Cross PPO', memberId: 'XKW928374', group: 'GRP-5521', bin: '004336', pcn: 'MEDDRUG' }
    },
    {
        id: 'pat_003', firstName: 'Aisha', lastName: 'Rahman', dob: '1992-01-05', gender: 'Female', mrn: 'MRN-20200312',
        allergies: [],
        preferredPharmacy: 'pharm_002',
        insurance: { plan: 'Aetna HMO', memberId: 'W924816735', group: 'AET-0092', bin: '610591', pcn: 'ASPROD1' }
    },
    {
        id: 'pat_004', firstName: 'William', lastName: 'Thornton', dob: '1944-11-22', gender: 'Male', mrn: 'MRN-20170605',
        allergies: [
            { id: 'alg_006', substance: 'Lisinopril', reaction: 'Angioedema', severity: 'severe' },
            { id: 'alg_007', substance: 'ACE Inhibitors', reaction: 'Angioedema', severity: 'severe' },
            { id: 'alg_008', substance: 'Latex', reaction: 'Contact dermatitis', severity: 'moderate' }
        ],
        preferredPharmacy: 'pharm_005',
        insurance: { plan: 'Medicare Part D', memberId: '7TH2-WN9-PL45', group: 'RX7834', bin: '610014', pcn: 'OHCP' }
    },
    {
        id: 'pat_005', firstName: 'Jessica', lastName: 'Morales', dob: '1988-06-17', gender: 'Female', mrn: 'MRN-20210901',
        allergies: [
            { id: 'alg_009', substance: 'Erythromycin', reaction: 'Rash', severity: 'mild' }
        ],
        preferredPharmacy: 'pharm_001',
        insurance: { plan: 'Cigna Open Access', memberId: 'CIG-7483920', group: 'EMP-334', bin: '600428', pcn: 'CICLAIM' }
    },
    {
        id: 'pat_006', firstName: 'Robert', lastName: 'Fitzgerald', dob: '1961-08-03', gender: 'Male', mrn: 'MRN-20160214',
        allergies: [
            { id: 'alg_010', substance: 'Metformin', reaction: 'Lactic acidosis', severity: 'severe' },
            { id: 'alg_011', substance: 'Shellfish', reaction: 'Hives', severity: 'moderate' }
        ],
        preferredPharmacy: 'pharm_004',
        insurance: { plan: 'UnitedHealth Choice Plus', memberId: 'UHC-5839201', group: 'UH-7782', bin: '610279', pcn: 'UHRX' }
    }
];

const CURRENT_PATIENT_ID = 'pat_001';

const PHARMACIES = [
    { id: 'pharm_001', name: 'CVS Pharmacy #4521', address: '1250 Market Street, San Francisco, CA 94103', phone: '(415) 555-0142', fax: '(415) 555-0143', type: 'retail', acceptsEPCS: true, hours: 'Mon-Sat 8am-9pm, Sun 9am-6pm', ncpdpId: '3498210' },
    { id: 'pharm_002', name: 'Walgreens #7893', address: '890 Van Ness Ave, San Francisco, CA 94109', phone: '(415) 555-0256', fax: '(415) 555-0257', type: 'retail', acceptsEPCS: true, hours: 'Mon-Fri 7am-10pm, Sat-Sun 8am-9pm', ncpdpId: '3501847' },
    { id: 'pharm_003', name: 'Rite Aid #5612', address: '2100 Geary Blvd, San Francisco, CA 94115', phone: '(415) 555-0378', fax: '(415) 555-0379', type: 'retail', acceptsEPCS: true, hours: 'Mon-Fri 8am-9pm, Sat 9am-7pm, Sun 10am-6pm', ncpdpId: '3487562' },
    { id: 'pharm_004', name: 'UCSF Medical Center Pharmacy', address: '505 Parnassus Ave, San Francisco, CA 94143', phone: '(415) 555-0491', fax: '(415) 555-0492', type: 'hospital', acceptsEPCS: true, hours: 'Mon-Fri 8am-6pm', ncpdpId: '3512098' },
    { id: 'pharm_005', name: 'Kaiser Permanente Pharmacy - Geary', address: '2425 Geary Blvd, San Francisco, CA 94115', phone: '(415) 555-0534', fax: '(415) 555-0535', type: 'retail', acceptsEPCS: true, hours: 'Mon-Fri 8:30am-6:30pm, Sat 9am-3pm', ncpdpId: '3498776' },
    { id: 'pharm_006', name: 'Costco Pharmacy #482', address: '450 10th Street, San Francisco, CA 94103', phone: '(415) 555-0612', fax: '(415) 555-0613', type: 'retail', acceptsEPCS: false, hours: 'Mon-Fri 10am-8:30pm, Sat 9:30am-6pm, Sun 10am-6pm', ncpdpId: '3503341' },
    { id: 'pharm_007', name: 'Alto Pharmacy', address: '800 Market Street, Ste 100, San Francisco, CA 94102', phone: '(415) 555-0745', fax: '(415) 555-0746', type: 'mail-order', acceptsEPCS: true, hours: 'Mon-Fri 9am-5pm (delivery)', ncpdpId: '3519823' },
    { id: 'pharm_008', name: 'Express Scripts Mail Pharmacy', address: 'PO Box 21141, Tempe, AZ 85285', phone: '(800) 555-0198', fax: '(800) 555-0199', type: 'mail-order', acceptsEPCS: false, hours: 'Mon-Fri 8am-8pm EST', ncpdpId: '3600142' },
    { id: 'pharm_009', name: 'Capsule Pharmacy SF', address: '560 Mission Street, Ste 300, San Francisco, CA 94105', phone: '(415) 555-0823', fax: '(415) 555-0824', type: 'mail-order', acceptsEPCS: true, hours: 'Mon-Fri 9am-9pm (same-day delivery)', ncpdpId: '3521908' },
    { id: 'pharm_010', name: 'BioPlus Specialty Pharmacy', address: '900 Sutter Street, Ste 200, San Francisco, CA 94109', phone: '(415) 555-0967', fax: '(415) 555-0968', type: 'specialty', acceptsEPCS: true, hours: 'Mon-Fri 8am-6pm', ncpdpId: '3534217' },
    { id: 'pharm_011', name: 'Accredo Specialty Pharmacy', address: '1640 Century Park East, Los Angeles, CA 90067', phone: '(800) 555-0234', fax: '(800) 555-0235', type: 'specialty', acceptsEPCS: true, hours: 'Mon-Fri 8am-7pm EST', ncpdpId: '3601987' },
    { id: 'pharm_012', name: 'Safeway Pharmacy #1234', address: '730 Taraval Street, San Francisco, CA 94116', phone: '(415) 555-1042', fax: '(415) 555-1043', type: 'retail', acceptsEPCS: true, hours: 'Mon-Fri 9am-8pm, Sat-Sun 9am-5pm', ncpdpId: '3478921' },
    { id: 'pharm_013', name: 'Amazon Pharmacy', address: 'PO Box 96130, Seattle, WA 98196', phone: '(855) 555-0301', fax: '(855) 555-0302', type: 'mail-order', acceptsEPCS: false, hours: '24/7 online ordering', ncpdpId: '3625401' },
    { id: 'pharm_014', name: 'Good Neighbor Pharmacy - Noe Valley', address: '1399 Church Street, San Francisco, CA 94114', phone: '(415) 555-1156', fax: '(415) 555-1157', type: 'retail', acceptsEPCS: false, hours: 'Mon-Fri 9am-7pm, Sat 10am-4pm', ncpdpId: '3456782' },
    { id: 'pharm_015', name: 'Optum Specialty Pharmacy', address: '2300 Main Street, Irvine, CA 92614', phone: '(800) 555-0478', fax: '(800) 555-0479', type: 'specialty', acceptsEPCS: true, hours: 'Mon-Fri 7am-7pm CST', ncpdpId: '3615293' }
];

const DRUG_CATALOG = [
    { id: 'drug_001', brandName: 'Lipitor', genericName: 'Atorvastatin', drugClass: 'HMG-CoA Reductase Inhibitor (Statin)', schedule: null,
      forms: [{ form: 'Tablet', strengths: ['10mg', '20mg', '40mg', '80mg'] }], routes: ['Oral'],
      commonSigs: ['Take 1 tablet by mouth once daily', 'Take 1 tablet by mouth at bedtime'], allergenCrossReactivity: [] },
    { id: 'drug_002', brandName: 'Zocor', genericName: 'Simvastatin', drugClass: 'HMG-CoA Reductase Inhibitor (Statin)', schedule: null,
      forms: [{ form: 'Tablet', strengths: ['5mg', '10mg', '20mg', '40mg', '80mg'] }], routes: ['Oral'],
      commonSigs: ['Take 1 tablet by mouth once daily in the evening'], allergenCrossReactivity: [] },
    { id: 'drug_003', brandName: 'Crestor', genericName: 'Rosuvastatin', drugClass: 'HMG-CoA Reductase Inhibitor (Statin)', schedule: null,
      forms: [{ form: 'Tablet', strengths: ['5mg', '10mg', '20mg', '40mg'] }], routes: ['Oral'],
      commonSigs: ['Take 1 tablet by mouth once daily'], allergenCrossReactivity: [] },
    { id: 'drug_004', brandName: 'Prinivil', genericName: 'Lisinopril', drugClass: 'ACE Inhibitor', schedule: null,
      forms: [{ form: 'Tablet', strengths: ['2.5mg', '5mg', '10mg', '20mg', '40mg'] }], routes: ['Oral'],
      commonSigs: ['Take 1 tablet by mouth once daily', 'Take 1 tablet by mouth twice daily'], allergenCrossReactivity: ['ACE Inhibitors'] },
    { id: 'drug_005', brandName: 'Norvasc', genericName: 'Amlodipine', drugClass: 'Calcium Channel Blocker', schedule: null,
      forms: [{ form: 'Tablet', strengths: ['2.5mg', '5mg', '10mg'] }], routes: ['Oral'],
      commonSigs: ['Take 1 tablet by mouth once daily'], allergenCrossReactivity: [] },
    { id: 'drug_006', brandName: 'Lopressor', genericName: 'Metoprolol Tartrate', drugClass: 'Beta Blocker', schedule: null,
      forms: [{ form: 'Tablet', strengths: ['25mg', '50mg', '100mg'] }], routes: ['Oral'],
      commonSigs: ['Take 1 tablet by mouth twice daily', 'Take 1 tablet by mouth once daily'], allergenCrossReactivity: [] },
    { id: 'drug_007', brandName: 'Toprol-XL', genericName: 'Metoprolol Succinate ER', drugClass: 'Beta Blocker', schedule: null,
      forms: [{ form: 'Tablet, Extended Release', strengths: ['25mg', '50mg', '100mg', '200mg'] }], routes: ['Oral'],
      commonSigs: ['Take 1 tablet by mouth once daily'], allergenCrossReactivity: [] },
    { id: 'drug_008', brandName: 'Diovan', genericName: 'Valsartan', drugClass: 'Angiotensin II Receptor Blocker (ARB)', schedule: null,
      forms: [{ form: 'Tablet', strengths: ['40mg', '80mg', '160mg', '320mg'] }], routes: ['Oral'],
      commonSigs: ['Take 1 tablet by mouth once daily', 'Take 1 tablet by mouth twice daily'], allergenCrossReactivity: [] },
    { id: 'drug_009', brandName: 'Lasix', genericName: 'Furosemide', drugClass: 'Loop Diuretic', schedule: null,
      forms: [{ form: 'Tablet', strengths: ['20mg', '40mg', '80mg'] }, { form: 'Oral Solution', strengths: ['10mg/mL'] }], routes: ['Oral'],
      commonSigs: ['Take 1 tablet by mouth once daily in the morning', 'Take 1 tablet by mouth twice daily'], allergenCrossReactivity: ['Sulfa drugs'] },
    { id: 'drug_010', brandName: 'Hydrochlorothiazide', genericName: 'Hydrochlorothiazide', drugClass: 'Thiazide Diuretic', schedule: null,
      forms: [{ form: 'Tablet', strengths: ['12.5mg', '25mg', '50mg'] }, { form: 'Capsule', strengths: ['12.5mg'] }], routes: ['Oral'],
      commonSigs: ['Take 1 tablet by mouth once daily in the morning'], allergenCrossReactivity: ['Sulfa drugs'] },
    { id: 'drug_011', brandName: 'Coumadin', genericName: 'Warfarin', drugClass: 'Anticoagulant (Vitamin K Antagonist)', schedule: null,
      forms: [{ form: 'Tablet', strengths: ['1mg', '2mg', '2.5mg', '3mg', '4mg', '5mg', '6mg', '7.5mg', '10mg'] }], routes: ['Oral'],
      commonSigs: ['Take 1 tablet by mouth once daily', 'Take as directed by provider'], allergenCrossReactivity: [] },
    { id: 'drug_012', brandName: 'Eliquis', genericName: 'Apixaban', drugClass: 'Direct Oral Anticoagulant (DOAC)', schedule: null,
      forms: [{ form: 'Tablet', strengths: ['2.5mg', '5mg'] }], routes: ['Oral'],
      commonSigs: ['Take 1 tablet by mouth twice daily', 'Take 1 tablet by mouth twice daily with food'], allergenCrossReactivity: [] },
    { id: 'drug_013', brandName: 'Xarelto', genericName: 'Rivaroxaban', drugClass: 'Direct Oral Anticoagulant (DOAC)', schedule: null,
      forms: [{ form: 'Tablet', strengths: ['2.5mg', '10mg', '15mg', '20mg'] }], routes: ['Oral'],
      commonSigs: ['Take 1 tablet by mouth once daily with the evening meal'], allergenCrossReactivity: [] },
    { id: 'drug_014', brandName: 'Glucophage', genericName: 'Metformin', drugClass: 'Biguanide', schedule: null,
      forms: [{ form: 'Tablet', strengths: ['500mg', '850mg', '1000mg'] }, { form: 'Tablet, Extended Release', strengths: ['500mg', '750mg', '1000mg'] }], routes: ['Oral'],
      commonSigs: ['Take 1 tablet by mouth twice daily with meals', 'Take 1 tablet by mouth once daily with dinner'], allergenCrossReactivity: [] },
    { id: 'drug_015', brandName: 'Januvia', genericName: 'Sitagliptin', drugClass: 'DPP-4 Inhibitor', schedule: null,
      forms: [{ form: 'Tablet', strengths: ['25mg', '50mg', '100mg'] }], routes: ['Oral'],
      commonSigs: ['Take 1 tablet by mouth once daily'], allergenCrossReactivity: [] },
    { id: 'drug_016', brandName: 'Jardiance', genericName: 'Empagliflozin', drugClass: 'SGLT2 Inhibitor', schedule: null,
      forms: [{ form: 'Tablet', strengths: ['10mg', '25mg'] }], routes: ['Oral'],
      commonSigs: ['Take 1 tablet by mouth once daily in the morning'], allergenCrossReactivity: [] },
    { id: 'drug_017', brandName: 'Lantus', genericName: 'Insulin Glargine', drugClass: 'Long-Acting Insulin', schedule: null,
      forms: [{ form: 'Solution for Injection', strengths: ['100 units/mL (10mL vial)', '100 units/mL (3mL pen)'] }], routes: ['Subcutaneous'],
      commonSigs: ['Inject 20 units subcutaneously once daily at bedtime', 'Inject as directed subcutaneously once daily'], allergenCrossReactivity: [] },
    { id: 'drug_018', brandName: 'Synthroid', genericName: 'Levothyroxine', drugClass: 'Thyroid Hormone', schedule: null,
      forms: [{ form: 'Tablet', strengths: ['25mcg', '50mcg', '75mcg', '88mcg', '100mcg', '112mcg', '125mcg', '137mcg', '150mcg', '175mcg', '200mcg', '300mcg'] }], routes: ['Oral'],
      commonSigs: ['Take 1 tablet by mouth once daily on an empty stomach, 30 minutes before breakfast'], allergenCrossReactivity: [] },
    { id: 'drug_019', brandName: 'Protonix', genericName: 'Pantoprazole', drugClass: 'Proton Pump Inhibitor', schedule: null,
      forms: [{ form: 'Tablet, Delayed Release', strengths: ['20mg', '40mg'] }], routes: ['Oral'],
      commonSigs: ['Take 1 tablet by mouth once daily before breakfast', 'Take 1 tablet by mouth twice daily before meals'], allergenCrossReactivity: [] },
    { id: 'drug_020', brandName: 'Nexium', genericName: 'Esomeprazole', drugClass: 'Proton Pump Inhibitor', schedule: null,
      forms: [{ form: 'Capsule, Delayed Release', strengths: ['20mg', '40mg'] }], routes: ['Oral'],
      commonSigs: ['Take 1 capsule by mouth once daily before breakfast'], allergenCrossReactivity: [] },
    { id: 'drug_021', brandName: 'Prilosec', genericName: 'Omeprazole', drugClass: 'Proton Pump Inhibitor', schedule: null,
      forms: [{ form: 'Capsule, Delayed Release', strengths: ['10mg', '20mg', '40mg'] }], routes: ['Oral'],
      commonSigs: ['Take 1 capsule by mouth once daily before breakfast'], allergenCrossReactivity: [] },
    { id: 'drug_022', brandName: 'Ventolin HFA', genericName: 'Albuterol', drugClass: 'Short-Acting Beta Agonist (SABA)', schedule: null,
      forms: [{ form: 'Metered Dose Inhaler', strengths: ['90mcg/actuation (200 actuations)'] }, { form: 'Nebulizer Solution', strengths: ['0.63mg/3mL', '1.25mg/3mL', '2.5mg/3mL'] }], routes: ['Inhalation'],
      commonSigs: ['Inhale 1-2 puffs every 4-6 hours as needed for shortness of breath', 'Inhale 2 puffs 15 minutes before exercise'], allergenCrossReactivity: [] },
    { id: 'drug_023', brandName: 'Advair Diskus', genericName: 'Fluticasone/Salmeterol', drugClass: 'Inhaled Corticosteroid / Long-Acting Beta Agonist (ICS/LABA)', schedule: null,
      forms: [{ form: 'Dry Powder Inhaler', strengths: ['100/50mcg', '250/50mcg', '500/50mcg'] }], routes: ['Inhalation'],
      commonSigs: ['Inhale 1 puff twice daily, rinse mouth after use'], allergenCrossReactivity: [] },
    { id: 'drug_024', brandName: 'Spiriva', genericName: 'Tiotropium', drugClass: 'Long-Acting Muscarinic Antagonist (LAMA)', schedule: null,
      forms: [{ form: 'Dry Powder Inhaler', strengths: ['18mcg/capsule'] }, { form: 'Mist Inhaler', strengths: ['1.25mcg/actuation', '2.5mcg/actuation'] }], routes: ['Inhalation'],
      commonSigs: ['Inhale 1 capsule once daily using HandiHaler device', 'Inhale 2 puffs once daily'], allergenCrossReactivity: [] },
    { id: 'drug_025', brandName: 'Amoxil', genericName: 'Amoxicillin', drugClass: 'Aminopenicillin', schedule: null,
      forms: [{ form: 'Capsule', strengths: ['250mg', '500mg'] }, { form: 'Suspension', strengths: ['125mg/5mL', '250mg/5mL', '400mg/5mL'] }, { form: 'Chewable Tablet', strengths: ['125mg', '250mg'] }], routes: ['Oral'],
      commonSigs: ['Take 1 capsule by mouth three times daily', 'Take 1 capsule by mouth twice daily', 'Take 500mg by mouth three times daily for 10 days'], allergenCrossReactivity: ['Penicillin'] },
    { id: 'drug_026', brandName: 'Augmentin', genericName: 'Amoxicillin/Clavulanate', drugClass: 'Aminopenicillin/Beta-Lactamase Inhibitor', schedule: null,
      forms: [{ form: 'Tablet', strengths: ['250/125mg', '500/125mg', '875/125mg'] }, { form: 'Suspension', strengths: ['200/28.5mg per 5mL', '400/57mg per 5mL'] }], routes: ['Oral'],
      commonSigs: ['Take 1 tablet by mouth twice daily with food', 'Take 1 tablet by mouth three times daily with food'], allergenCrossReactivity: ['Penicillin'] },
    { id: 'drug_027', brandName: 'Keflex', genericName: 'Cephalexin', drugClass: 'First-Generation Cephalosporin', schedule: null,
      forms: [{ form: 'Capsule', strengths: ['250mg', '500mg', '750mg'] }, { form: 'Suspension', strengths: ['125mg/5mL', '250mg/5mL'] }], routes: ['Oral'],
      commonSigs: ['Take 1 capsule by mouth four times daily', 'Take 1 capsule by mouth twice daily for 7 days'], allergenCrossReactivity: [] },
    { id: 'drug_028', brandName: 'Zithromax', genericName: 'Azithromycin', drugClass: 'Macrolide Antibiotic', schedule: null,
      forms: [{ form: 'Tablet', strengths: ['250mg', '500mg', '600mg'] }, { form: 'Suspension', strengths: ['100mg/5mL', '200mg/5mL'] }], routes: ['Oral'],
      commonSigs: ['Take 500mg on day 1, then 250mg once daily for 4 days', 'Take 1 tablet by mouth once daily for 5 days'], allergenCrossReactivity: ['Erythromycin'] },
    { id: 'drug_029', brandName: 'Biaxin', genericName: 'Clarithromycin', drugClass: 'Macrolide Antibiotic', schedule: null,
      forms: [{ form: 'Tablet', strengths: ['250mg', '500mg'] }, { form: 'Tablet, Extended Release', strengths: ['500mg'] }], routes: ['Oral'],
      commonSigs: ['Take 1 tablet by mouth twice daily for 7-14 days'], allergenCrossReactivity: ['Erythromycin'] },
    { id: 'drug_030', brandName: 'Cipro', genericName: 'Ciprofloxacin', drugClass: 'Fluoroquinolone', schedule: null,
      forms: [{ form: 'Tablet', strengths: ['250mg', '500mg', '750mg'] }, { form: 'Suspension', strengths: ['250mg/5mL', '500mg/5mL'] }], routes: ['Oral'],
      commonSigs: ['Take 1 tablet by mouth twice daily for 7 days', 'Take 500mg by mouth twice daily'], allergenCrossReactivity: [] },
    { id: 'drug_031', brandName: 'Bactrim DS', genericName: 'Sulfamethoxazole/Trimethoprim', drugClass: 'Sulfonamide Antibiotic', schedule: null,
      forms: [{ form: 'Tablet', strengths: ['400/80mg', '800/160mg'] }, { form: 'Suspension', strengths: ['200/40mg per 5mL'] }], routes: ['Oral'],
      commonSigs: ['Take 1 tablet by mouth twice daily for 10 days', 'Take 1 DS tablet by mouth twice daily'], allergenCrossReactivity: ['Sulfa drugs'] },
    { id: 'drug_032', brandName: 'Diflucan', genericName: 'Fluconazole', drugClass: 'Azole Antifungal', schedule: null,
      forms: [{ form: 'Tablet', strengths: ['50mg', '100mg', '150mg', '200mg'] }, { form: 'Suspension', strengths: ['10mg/mL', '40mg/mL'] }], routes: ['Oral'],
      commonSigs: ['Take 150mg by mouth as a single dose', 'Take 1 tablet by mouth once daily'], allergenCrossReactivity: [] },
    { id: 'drug_033', brandName: 'Zoloft', genericName: 'Sertraline', drugClass: 'Selective Serotonin Reuptake Inhibitor (SSRI)', schedule: null,
      forms: [{ form: 'Tablet', strengths: ['25mg', '50mg', '100mg'] }, { form: 'Oral Concentrate', strengths: ['20mg/mL'] }], routes: ['Oral'],
      commonSigs: ['Take 1 tablet by mouth once daily', 'Take 1 tablet by mouth once daily in the morning'], allergenCrossReactivity: [] },
    { id: 'drug_034', brandName: 'Lexapro', genericName: 'Escitalopram', drugClass: 'Selective Serotonin Reuptake Inhibitor (SSRI)', schedule: null,
      forms: [{ form: 'Tablet', strengths: ['5mg', '10mg', '20mg'] }, { form: 'Oral Solution', strengths: ['1mg/mL'] }], routes: ['Oral'],
      commonSigs: ['Take 1 tablet by mouth once daily', 'Take 1 tablet by mouth once daily in the morning'], allergenCrossReactivity: [] },
    { id: 'drug_035', brandName: 'Cymbalta', genericName: 'Duloxetine', drugClass: 'Serotonin-Norepinephrine Reuptake Inhibitor (SNRI)', schedule: null,
      forms: [{ form: 'Capsule, Delayed Release', strengths: ['20mg', '30mg', '40mg', '60mg'] }], routes: ['Oral'],
      commonSigs: ['Take 1 capsule by mouth once daily', 'Take 1 capsule by mouth once daily with food'], allergenCrossReactivity: [] },
    { id: 'drug_036', brandName: 'Neurontin', genericName: 'Gabapentin', drugClass: 'Anticonvulsant / Neuropathic Pain Agent', schedule: null,
      forms: [{ form: 'Capsule', strengths: ['100mg', '300mg', '400mg'] }, { form: 'Tablet', strengths: ['600mg', '800mg'] }, { form: 'Oral Solution', strengths: ['250mg/5mL'] }], routes: ['Oral'],
      commonSigs: ['Take 1 capsule by mouth three times daily', 'Take 300mg by mouth at bedtime, increase as tolerated'], allergenCrossReactivity: [] },
    { id: 'drug_037', brandName: 'Lyrica', genericName: 'Pregabalin', drugClass: 'Anticonvulsant / Neuropathic Pain Agent', schedule: 'V',
      forms: [{ form: 'Capsule', strengths: ['25mg', '50mg', '75mg', '100mg', '150mg', '200mg', '225mg', '300mg'] }], routes: ['Oral'],
      commonSigs: ['Take 1 capsule by mouth twice daily', 'Take 75mg by mouth twice daily, may increase to 150mg twice daily'], allergenCrossReactivity: [] },
    { id: 'drug_038', brandName: 'Ambien', genericName: 'Zolpidem', drugClass: 'Sedative-Hypnotic', schedule: 'IV',
      forms: [{ form: 'Tablet', strengths: ['5mg', '10mg'] }, { form: 'Tablet, Extended Release', strengths: ['6.25mg', '12.5mg'] }], routes: ['Oral'],
      commonSigs: ['Take 1 tablet by mouth at bedtime as needed', 'Take 5mg by mouth at bedtime as needed for insomnia'], allergenCrossReactivity: [] },
    { id: 'drug_039', brandName: 'Xanax', genericName: 'Alprazolam', drugClass: 'Benzodiazepine', schedule: 'IV',
      forms: [{ form: 'Tablet', strengths: ['0.25mg', '0.5mg', '1mg', '2mg'] }], routes: ['Oral'],
      commonSigs: ['Take 1 tablet by mouth three times daily as needed for anxiety', 'Take 0.25mg by mouth twice daily as needed'], allergenCrossReactivity: [] },
    { id: 'drug_040', brandName: 'Ativan', genericName: 'Lorazepam', drugClass: 'Benzodiazepine', schedule: 'IV',
      forms: [{ form: 'Tablet', strengths: ['0.5mg', '1mg', '2mg'] }], routes: ['Oral'],
      commonSigs: ['Take 1 tablet by mouth twice daily as needed for anxiety', 'Take 0.5mg by mouth at bedtime as needed'], allergenCrossReactivity: [] },
    { id: 'drug_041', brandName: 'Percocet', genericName: 'Oxycodone/Acetaminophen', drugClass: 'Opioid Analgesic Combination', schedule: 'II',
      forms: [{ form: 'Tablet', strengths: ['2.5/325mg', '5/325mg', '7.5/325mg', '10/325mg'] }], routes: ['Oral'],
      commonSigs: ['Take 1 tablet by mouth every 4-6 hours as needed for pain', 'Take 1-2 tablets by mouth every 6 hours as needed for moderate to severe pain'], allergenCrossReactivity: [] },
    { id: 'drug_042', brandName: 'Tylenol #3', genericName: 'Codeine/Acetaminophen', drugClass: 'Opioid Analgesic Combination', schedule: 'III',
      forms: [{ form: 'Tablet', strengths: ['30/300mg'] }], routes: ['Oral'],
      commonSigs: ['Take 1-2 tablets by mouth every 4-6 hours as needed for pain'], allergenCrossReactivity: ['Codeine'] },
    { id: 'drug_043', brandName: 'Motrin', genericName: 'Ibuprofen', drugClass: 'Nonsteroidal Anti-Inflammatory Drug (NSAID)', schedule: null,
      forms: [{ form: 'Tablet', strengths: ['200mg', '400mg', '600mg', '800mg'] }, { form: 'Suspension', strengths: ['100mg/5mL'] }], routes: ['Oral'],
      commonSigs: ['Take 1 tablet by mouth every 6-8 hours as needed with food', 'Take 400mg by mouth three times daily with food'], allergenCrossReactivity: [] },
    { id: 'drug_044', brandName: 'Voltaren', genericName: 'Diclofenac', drugClass: 'Nonsteroidal Anti-Inflammatory Drug (NSAID)', schedule: null,
      forms: [{ form: 'Tablet, Delayed Release', strengths: ['25mg', '50mg', '75mg'] }, { form: 'Topical Gel', strengths: ['1%'] }], routes: ['Oral', 'Topical'],
      commonSigs: ['Take 1 tablet by mouth twice daily with food', 'Apply gel to affected area four times daily'], allergenCrossReactivity: [] },
    { id: 'drug_045', brandName: 'Prednisone', genericName: 'Prednisone', drugClass: 'Corticosteroid', schedule: null,
      forms: [{ form: 'Tablet', strengths: ['1mg', '2.5mg', '5mg', '10mg', '20mg', '50mg'] }, { form: 'Oral Solution', strengths: ['1mg/mL'] }], routes: ['Oral'],
      commonSigs: ['Take as directed per taper schedule', 'Take 40mg by mouth once daily for 5 days, then taper', 'Take 1 tablet by mouth once daily in the morning'], allergenCrossReactivity: [] },
    { id: 'drug_046', brandName: 'Medrol Dosepak', genericName: 'Methylprednisolone', drugClass: 'Corticosteroid', schedule: null,
      forms: [{ form: 'Tablet', strengths: ['4mg (21-tablet dose pack)'] }], routes: ['Oral'],
      commonSigs: ['Take as directed per dose pack instructions'], allergenCrossReactivity: [] },
    { id: 'drug_047', brandName: 'Flonase', genericName: 'Fluticasone Propionate Nasal', drugClass: 'Intranasal Corticosteroid', schedule: null,
      forms: [{ form: 'Nasal Spray', strengths: ['50mcg/spray (120 sprays)'] }], routes: ['Intranasal'],
      commonSigs: ['Spray 2 sprays in each nostril once daily', 'Spray 1-2 sprays in each nostril once daily'], allergenCrossReactivity: [] },
    { id: 'drug_048', brandName: 'Plavix', genericName: 'Clopidogrel', drugClass: 'P2Y12 Platelet Inhibitor', schedule: null,
      forms: [{ form: 'Tablet', strengths: ['75mg', '300mg'] }], routes: ['Oral'],
      commonSigs: ['Take 1 tablet by mouth once daily', 'Take 300mg loading dose, then 75mg once daily'], allergenCrossReactivity: [] },
    { id: 'drug_049', brandName: 'Ozempic', genericName: 'Semaglutide', drugClass: 'GLP-1 Receptor Agonist', schedule: null,
      forms: [{ form: 'Solution for Injection', strengths: ['0.25mg/0.5mL', '0.5mg/0.5mL', '1mg/0.5mL', '2mg/0.5mL'] }], routes: ['Subcutaneous'],
      commonSigs: ['Inject 0.25mg subcutaneously once weekly for 4 weeks, then increase to 0.5mg weekly', 'Inject 1mg subcutaneously once weekly'], allergenCrossReactivity: [] },
    { id: 'drug_050', brandName: 'Trulicity', genericName: 'Dulaglutide', drugClass: 'GLP-1 Receptor Agonist', schedule: null,
      forms: [{ form: 'Solution for Injection', strengths: ['0.75mg/0.5mL', '1.5mg/0.5mL', '3mg/0.5mL', '4.5mg/0.5mL'] }], routes: ['Subcutaneous'],
      commonSigs: ['Inject 0.75mg subcutaneously once weekly', 'Inject 1.5mg subcutaneously once weekly'], allergenCrossReactivity: [] },
    { id: 'drug_051', brandName: 'Singulair', genericName: 'Montelukast', drugClass: 'Leukotriene Receptor Antagonist', schedule: null,
      forms: [{ form: 'Tablet', strengths: ['4mg', '5mg', '10mg'] }, { form: 'Granules', strengths: ['4mg'] }], routes: ['Oral'],
      commonSigs: ['Take 1 tablet by mouth once daily in the evening'], allergenCrossReactivity: [] },
    { id: 'drug_052', brandName: 'Flexeril', genericName: 'Cyclobenzaprine', drugClass: 'Skeletal Muscle Relaxant', schedule: null,
      forms: [{ form: 'Tablet', strengths: ['5mg', '7.5mg', '10mg'] }], routes: ['Oral'],
      commonSigs: ['Take 1 tablet by mouth three times daily', 'Take 5mg by mouth three times daily as needed for muscle spasm'], allergenCrossReactivity: [] },
    { id: 'drug_053', brandName: 'Glucotrol', genericName: 'Glipizide', drugClass: 'Sulfonylurea', schedule: null,
      forms: [{ form: 'Tablet', strengths: ['5mg', '10mg'] }, { form: 'Tablet, Extended Release', strengths: ['2.5mg', '5mg', '10mg'] }], routes: ['Oral'],
      commonSigs: ['Take 1 tablet by mouth once daily 30 minutes before breakfast', 'Take 1 tablet by mouth twice daily before meals'], allergenCrossReactivity: ['Sulfa drugs'] },
    { id: 'drug_054', brandName: 'Aldactone', genericName: 'Spironolactone', drugClass: 'Potassium-Sparing Diuretic / Aldosterone Antagonist', schedule: null,
      forms: [{ form: 'Tablet', strengths: ['25mg', '50mg', '100mg'] }], routes: ['Oral'],
      commonSigs: ['Take 1 tablet by mouth once daily', 'Take 25mg by mouth once daily'], allergenCrossReactivity: [] },
    { id: 'drug_055', brandName: 'Cardizem', genericName: 'Diltiazem', drugClass: 'Calcium Channel Blocker', schedule: null,
      forms: [{ form: 'Tablet', strengths: ['30mg', '60mg', '90mg', '120mg'] }, { form: 'Capsule, Extended Release', strengths: ['120mg', '180mg', '240mg', '300mg', '360mg'] }], routes: ['Oral'],
      commonSigs: ['Take 1 capsule by mouth once daily', 'Take 1 tablet by mouth three times daily'], allergenCrossReactivity: [] },
    { id: 'drug_056', brandName: 'Prozac', genericName: 'Fluoxetine', drugClass: 'Selective Serotonin Reuptake Inhibitor (SSRI)', schedule: null,
      forms: [{ form: 'Capsule', strengths: ['10mg', '20mg', '40mg'] }, { form: 'Oral Solution', strengths: ['20mg/5mL'] }], routes: ['Oral'],
      commonSigs: ['Take 1 capsule by mouth once daily in the morning'], allergenCrossReactivity: [] },
    { id: 'drug_057', brandName: 'Coreg', genericName: 'Carvedilol', drugClass: 'Alpha/Beta Blocker', schedule: null,
      forms: [{ form: 'Tablet', strengths: ['3.125mg', '6.25mg', '12.5mg', '25mg'] }], routes: ['Oral'],
      commonSigs: ['Take 1 tablet by mouth twice daily with food'], allergenCrossReactivity: [] },
    { id: 'drug_058', brandName: 'Zestril', genericName: 'Lisinopril', drugClass: 'ACE Inhibitor', schedule: null,
      forms: [{ form: 'Tablet', strengths: ['2.5mg', '5mg', '10mg', '20mg', '30mg', '40mg'] }], routes: ['Oral'],
      commonSigs: ['Take 1 tablet by mouth once daily'], allergenCrossReactivity: ['ACE Inhibitors'] },
    { id: 'drug_059', brandName: 'Tamiflu', genericName: 'Oseltamivir', drugClass: 'Neuraminidase Inhibitor (Antiviral)', schedule: null,
      forms: [{ form: 'Capsule', strengths: ['30mg', '45mg', '75mg'] }, { form: 'Suspension', strengths: ['6mg/mL'] }], routes: ['Oral'],
      commonSigs: ['Take 1 capsule by mouth twice daily for 5 days'], allergenCrossReactivity: [] },
    { id: 'drug_060', brandName: 'Valtrex', genericName: 'Valacyclovir', drugClass: 'Antiviral', schedule: null,
      forms: [{ form: 'Tablet', strengths: ['500mg', '1000mg'] }], routes: ['Oral'],
      commonSigs: ['Take 1 tablet by mouth twice daily for 7-10 days', 'Take 500mg by mouth once daily for suppression'], allergenCrossReactivity: [] }
];

const DRUG_INTERACTIONS = [
    { id: 'int_001', drug1Id: 'drug_001', drug2Id: 'drug_029', drug1Name: 'Atorvastatin', drug2Name: 'Clarithromycin', severity: 'major',
      description: 'Clarithromycin inhibits CYP3A4, significantly increasing statin levels and risk of rhabdomyolysis.', recommendation: 'Avoid concurrent use. Consider azithromycin as an alternative. If concurrent use is necessary, limit atorvastatin dose to 20mg/day.' },
    { id: 'int_002', drug1Id: 'drug_011', drug2Id: 'drug_043', drug1Name: 'Warfarin', drug2Name: 'Ibuprofen', severity: 'major',
      description: 'NSAIDs increase the anticoagulant effect of warfarin and increase risk of GI bleeding.', recommendation: 'Avoid concurrent use if possible. If required, monitor INR more frequently and watch for signs of bleeding.' },
    { id: 'int_003', drug1Id: 'drug_011', drug2Id: 'drug_012', drug1Name: 'Warfarin', drug2Name: 'Apixaban', severity: 'major',
      description: 'Concurrent use of two anticoagulants dramatically increases bleeding risk.', recommendation: 'Do not use concurrently. Discontinue one agent before starting the other with appropriate washout period.' },
    { id: 'int_004', drug1Id: 'drug_012', drug2Id: 'drug_013', drug1Name: 'Apixaban', drug2Name: 'Rivaroxaban', severity: 'major',
      description: 'Concurrent use of two direct oral anticoagulants dramatically increases bleeding risk.', recommendation: 'Do not use concurrently. Choose one DOAC agent.' },
    { id: 'int_005', drug1Id: 'drug_033', drug2Id: 'drug_034', drug1Name: 'Sertraline', drug2Name: 'Escitalopram', severity: 'major',
      description: 'Concurrent use of two SSRIs increases serotonin syndrome risk significantly.', recommendation: 'Do not use concurrently. Cross-taper when switching between agents.' },
    { id: 'int_006', drug1Id: 'drug_033', drug2Id: 'drug_035', drug1Name: 'Sertraline', drug2Name: 'Duloxetine', severity: 'major',
      description: 'Combined serotonergic agents increase risk of serotonin syndrome.', recommendation: 'Avoid concurrent use. If switching, allow adequate washout period.' },
    { id: 'int_007', drug1Id: 'drug_011', drug2Id: 'drug_028', drug1Name: 'Warfarin', drug2Name: 'Azithromycin', severity: 'moderate',
      description: 'Macrolides may increase INR and potentiate anticoagulant effect.', recommendation: 'Monitor INR closely during and after antibiotic course. Adjust warfarin dose as needed.' },
    { id: 'int_008', drug1Id: 'drug_006', drug2Id: 'drug_055', drug1Name: 'Metoprolol Tartrate', drug2Name: 'Diltiazem', severity: 'major',
      description: 'Combined beta-blocker and non-dihydropyridine calcium channel blocker may cause severe bradycardia, heart block, or heart failure.', recommendation: 'Use with extreme caution. Monitor heart rate and ECG. Consider amlodipine as an alternative calcium channel blocker.' },
    { id: 'int_009', drug1Id: 'drug_014', drug2Id: 'drug_030', drug1Name: 'Metformin', drug2Name: 'Ciprofloxacin', severity: 'moderate',
      description: 'Fluoroquinolones may alter blood glucose levels and affect metformin efficacy.', recommendation: 'Monitor blood glucose more frequently during antibiotic therapy.' },
    { id: 'int_010', drug1Id: 'drug_004', drug2Id: 'drug_054', drug1Name: 'Lisinopril', drug2Name: 'Spironolactone', severity: 'moderate',
      description: 'Both agents increase potassium levels, risking hyperkalemia.', recommendation: 'Monitor serum potassium regularly. Consider dose adjustments.' },
    { id: 'int_011', drug1Id: 'drug_039', drug2Id: 'drug_040', drug1Name: 'Alprazolam', drug2Name: 'Lorazepam', severity: 'major',
      description: 'Concurrent use of two benzodiazepines increases risk of excessive sedation and respiratory depression.', recommendation: 'Do not prescribe concurrently. Consolidate to a single benzodiazepine.' },
    { id: 'int_012', drug1Id: 'drug_041', drug2Id: 'drug_039', drug1Name: 'Oxycodone/Acetaminophen', drug2Name: 'Alprazolam', severity: 'major',
      description: 'Concurrent opioid and benzodiazepine use significantly increases risk of respiratory depression, sedation, coma, and death.', recommendation: 'Avoid concurrent use. If medically necessary, limit dose and duration. FDA Black Box Warning.' },
    { id: 'int_013', drug1Id: 'drug_041', drug2Id: 'drug_040', drug1Name: 'Oxycodone/Acetaminophen', drug2Name: 'Lorazepam', severity: 'major',
      description: 'Concurrent opioid and benzodiazepine use significantly increases risk of respiratory depression, sedation, coma, and death.', recommendation: 'Avoid concurrent use. If medically necessary, limit dose and duration. FDA Black Box Warning.' },
    { id: 'int_014', drug1Id: 'drug_009', drug2Id: 'drug_004', drug1Name: 'Furosemide', drug2Name: 'Lisinopril', severity: 'moderate',
      description: 'Diuretic may enhance hypotensive effect of ACE inhibitor, risk of first-dose hypotension.', recommendation: 'Consider reducing diuretic dose before starting ACE inhibitor. Monitor blood pressure closely.' },
    { id: 'int_015', drug1Id: 'drug_018', drug2Id: 'drug_019', drug1Name: 'Levothyroxine', drug2Name: 'Pantoprazole', severity: 'moderate',
      description: 'PPIs may reduce levothyroxine absorption by increasing gastric pH.', recommendation: 'Separate administration by at least 4 hours. Monitor TSH levels and adjust thyroid dose if needed.' },
    { id: 'int_016', drug1Id: 'drug_011', drug2Id: 'drug_045', drug1Name: 'Warfarin', drug2Name: 'Prednisone', severity: 'moderate',
      description: 'Corticosteroids may enhance or reduce anticoagulant effect and increase GI bleeding risk.', recommendation: 'Monitor INR closely during corticosteroid therapy. Adjust warfarin dose as needed.' },
    { id: 'int_017', drug1Id: 'drug_048', drug2Id: 'drug_021', drug1Name: 'Clopidogrel', drug2Name: 'Omeprazole', severity: 'moderate',
      description: 'Omeprazole inhibits CYP2C19 and may reduce the antiplatelet effect of clopidogrel.', recommendation: 'Use pantoprazole instead of omeprazole. If PPI is necessary, choose one that does not inhibit CYP2C19.' },
    { id: 'int_018', drug1Id: 'drug_038', drug2Id: 'drug_033', drug1Name: 'Zolpidem', drug2Name: 'Sertraline', severity: 'moderate',
      description: 'SSRIs may increase sedative effect of zolpidem through serotonergic mechanism.', recommendation: 'Use lower dose of zolpidem. Monitor for excessive sedation.' },
    { id: 'int_019', drug1Id: 'drug_002', drug2Id: 'drug_005', drug1Name: 'Simvastatin', drug2Name: 'Amlodipine', severity: 'moderate',
      description: 'Amlodipine inhibits CYP3A4 and may increase simvastatin levels, increasing myopathy risk.', recommendation: 'Limit simvastatin dose to 20mg/day when used with amlodipine.' },
    { id: 'int_020', drug1Id: 'drug_036', drug2Id: 'drug_041', drug1Name: 'Gabapentin', drug2Name: 'Oxycodone/Acetaminophen', severity: 'major',
      description: 'Combined CNS depressants increase risk of severe sedation, respiratory depression, coma, and death.', recommendation: 'Use lowest effective doses if concurrent use is necessary. Monitor closely for respiratory depression.' },
    { id: 'int_021', drug1Id: 'drug_049', drug2Id: 'drug_017', drug1Name: 'Semaglutide', drug2Name: 'Insulin Glargine', severity: 'moderate',
      description: 'GLP-1 agonists with insulin increase risk of hypoglycemia.', recommendation: 'Consider reducing insulin dose by 20% when starting GLP-1 agonist. Monitor blood glucose frequently.' },
    { id: 'int_022', drug1Id: 'drug_043', drug2Id: 'drug_012', drug1Name: 'Ibuprofen', drug2Name: 'Apixaban', severity: 'major',
      description: 'NSAIDs increase anticoagulant effect and GI bleeding risk with DOACs.', recommendation: 'Avoid concurrent use. Use acetaminophen for pain management when possible.' },
    { id: 'int_023', drug1Id: 'drug_030', drug2Id: 'drug_018', drug1Name: 'Ciprofloxacin', drug2Name: 'Levothyroxine', severity: 'minor',
      description: 'Ciprofloxacin may slightly reduce levothyroxine absorption.', recommendation: 'Separate doses by at least 4 hours. No dose adjustment typically needed.' },
    { id: 'int_024', drug1Id: 'drug_033', drug2Id: 'drug_043', drug1Name: 'Sertraline', drug2Name: 'Ibuprofen', severity: 'moderate',
      description: 'SSRIs impair platelet function; combined with NSAID increases GI bleeding risk.', recommendation: 'Consider adding gastroprotective agent (PPI) if concurrent use is required. Monitor for signs of GI bleeding.' },
    { id: 'int_025', drug1Id: 'drug_004', drug2Id: 'drug_008', drug1Name: 'Lisinopril', drug2Name: 'Valsartan', severity: 'major',
      description: 'Dual RAAS blockade (ACE inhibitor + ARB) increases risk of hyperkalemia, renal impairment, and hypotension.', recommendation: 'Do not use concurrently. Choose either ACE inhibitor or ARB.' }
];

const PRESCRIPTIONS = [
    {
        id: 'rx_001', patientId: 'pat_001', drugId: 'drug_001', drugName: 'Atorvastatin', brandName: 'Lipitor',
        formStrength: '20mg Tablet', dosage: '20mg', frequency: 'Once daily', route: 'Oral', quantity: 90, daysSupply: 90,
        refillsTotal: 3, refillsRemaining: 2, sig: 'Take 1 tablet by mouth once daily at bedtime',
        daw: false, pharmacyId: 'pharm_001', prescriberId: 'prov_001', status: 'active',
        startDate: '2025-06-15', endDate: null, priorAuth: false, priorAuthNumber: null,
        discontinuedReason: null, discontinuedDate: null,
        fillHistory: [
            { fillDate: '2025-06-15', pharmacy: 'CVS Pharmacy #4521', quantity: 90, daysSupply: 90, fillNumber: 1 },
            { fillDate: '2025-09-13', pharmacy: 'CVS Pharmacy #4521', quantity: 90, daysSupply: 90, fillNumber: 2 }
        ],
        history: [
            { action: 'prescribed', date: '2025-06-15', provider: 'Dr. Sarah Mitchell', note: 'Initiated for hyperlipidemia, LDL 168' },
            { action: 'filled', date: '2025-06-15', pharmacy: 'CVS Pharmacy #4521' },
            { action: 'filled', date: '2025-09-13', pharmacy: 'CVS Pharmacy #4521' },
            { action: 'renewed', date: '2025-12-10', provider: 'Dr. Sarah Mitchell', note: 'LDL improved to 112, continue therapy' }
        ]
    },
    {
        id: 'rx_002', patientId: 'pat_001', drugId: 'drug_005', drugName: 'Amlodipine', brandName: 'Norvasc',
        formStrength: '5mg Tablet', dosage: '5mg', frequency: 'Once daily', route: 'Oral', quantity: 30, daysSupply: 30,
        refillsTotal: 5, refillsRemaining: 4, sig: 'Take 1 tablet by mouth once daily',
        daw: false, pharmacyId: 'pharm_001', prescriberId: 'prov_001', status: 'active',
        startDate: '2025-08-20', endDate: null, priorAuth: false, priorAuthNumber: null,
        discontinuedReason: null, discontinuedDate: null,
        fillHistory: [
            { fillDate: '2025-08-20', pharmacy: 'CVS Pharmacy #4521', quantity: 30, daysSupply: 30, fillNumber: 1 },
            { fillDate: '2025-09-19', pharmacy: 'CVS Pharmacy #4521', quantity: 30, daysSupply: 30, fillNumber: 2 },
            { fillDate: '2025-10-18', pharmacy: 'CVS Pharmacy #4521', quantity: 30, daysSupply: 30, fillNumber: 3 }
        ],
        history: [
            { action: 'prescribed', date: '2025-08-20', provider: 'Dr. Sarah Mitchell', note: 'BP 152/94, adding CCB' },
            { action: 'filled', date: '2025-08-20', pharmacy: 'CVS Pharmacy #4521' },
            { action: 'filled', date: '2025-09-19', pharmacy: 'CVS Pharmacy #4521' },
            { action: 'filled', date: '2025-10-18', pharmacy: 'CVS Pharmacy #4521' }
        ]
    },
    {
        id: 'rx_003', patientId: 'pat_001', drugId: 'drug_014', drugName: 'Metformin', brandName: 'Glucophage',
        formStrength: '1000mg Tablet', dosage: '1000mg', frequency: 'Twice daily', route: 'Oral', quantity: 60, daysSupply: 30,
        refillsTotal: 5, refillsRemaining: 3, sig: 'Take 1 tablet by mouth twice daily with meals',
        daw: false, pharmacyId: 'pharm_001', prescriberId: 'prov_001', status: 'active',
        startDate: '2025-03-10', endDate: null, priorAuth: false, priorAuthNumber: null,
        discontinuedReason: null, discontinuedDate: null,
        fillHistory: [
            { fillDate: '2025-03-10', pharmacy: 'CVS Pharmacy #4521', quantity: 60, daysSupply: 30, fillNumber: 1 },
            { fillDate: '2025-04-09', pharmacy: 'CVS Pharmacy #4521', quantity: 60, daysSupply: 30, fillNumber: 2 },
            { fillDate: '2025-05-09', pharmacy: 'CVS Pharmacy #4521', quantity: 60, daysSupply: 30, fillNumber: 3 },
            { fillDate: '2025-06-08', pharmacy: 'CVS Pharmacy #4521', quantity: 60, daysSupply: 30, fillNumber: 4 }
        ],
        history: [
            { action: 'prescribed', date: '2025-03-10', provider: 'Dr. Sarah Mitchell', note: 'A1C 7.8%, starting metformin' },
            { action: 'modified', date: '2025-04-20', provider: 'Dr. Sarah Mitchell', note: 'Increased from 500mg BID to 1000mg BID, tolerated well' }
        ]
    },
    {
        id: 'rx_004', patientId: 'pat_001', drugId: 'drug_018', drugName: 'Levothyroxine', brandName: 'Synthroid',
        formStrength: '75mcg Tablet', dosage: '75mcg', frequency: 'Once daily', route: 'Oral', quantity: 30, daysSupply: 30,
        refillsTotal: 11, refillsRemaining: 8, sig: 'Take 1 tablet by mouth once daily on an empty stomach, 30 minutes before breakfast',
        daw: true, pharmacyId: 'pharm_001', prescriberId: 'prov_002', status: 'active',
        startDate: '2024-09-05', endDate: null, priorAuth: false, priorAuthNumber: null,
        discontinuedReason: null, discontinuedDate: null,
        fillHistory: [
            { fillDate: '2024-09-05', pharmacy: 'CVS Pharmacy #4521', quantity: 30, daysSupply: 30, fillNumber: 1 },
            { fillDate: '2024-10-05', pharmacy: 'CVS Pharmacy #4521', quantity: 30, daysSupply: 30, fillNumber: 2 },
            { fillDate: '2024-11-04', pharmacy: 'CVS Pharmacy #4521', quantity: 30, daysSupply: 30, fillNumber: 3 }
        ],
        history: [
            { action: 'prescribed', date: '2024-09-05', provider: 'Dr. James Okafor', note: 'TSH 8.2, hypothyroidism, DAW for brand consistency' },
            { action: 'filled', date: '2024-09-05', pharmacy: 'CVS Pharmacy #4521' }
        ]
    },
    {
        id: 'rx_005', patientId: 'pat_001', drugId: 'drug_019', drugName: 'Pantoprazole', brandName: 'Protonix',
        formStrength: '40mg Tablet, Delayed Release', dosage: '40mg', frequency: 'Once daily', route: 'Oral', quantity: 30, daysSupply: 30,
        refillsTotal: 2, refillsRemaining: 1, sig: 'Take 1 tablet by mouth once daily before breakfast',
        daw: false, pharmacyId: 'pharm_001', prescriberId: 'prov_001', status: 'active',
        startDate: '2025-11-01', endDate: null, priorAuth: false, priorAuthNumber: null,
        discontinuedReason: null, discontinuedDate: null,
        fillHistory: [
            { fillDate: '2025-11-01', pharmacy: 'CVS Pharmacy #4521', quantity: 30, daysSupply: 30, fillNumber: 1 },
            { fillDate: '2025-12-01', pharmacy: 'CVS Pharmacy #4521', quantity: 30, daysSupply: 30, fillNumber: 2 }
        ],
        history: [
            { action: 'prescribed', date: '2025-11-01', provider: 'Dr. Sarah Mitchell', note: 'GERD symptoms, empiric PPI trial' },
            { action: 'filled', date: '2025-11-01', pharmacy: 'CVS Pharmacy #4521' }
        ]
    },
    {
        id: 'rx_006', patientId: 'pat_001', drugId: 'drug_022', drugName: 'Albuterol', brandName: 'Ventolin HFA',
        formStrength: '90mcg/actuation Metered Dose Inhaler', dosage: '90mcg', frequency: 'Every 4-6 hours as needed', route: 'Inhalation', quantity: 1, daysSupply: 30,
        refillsTotal: 3, refillsRemaining: 2, sig: 'Inhale 1-2 puffs every 4-6 hours as needed for shortness of breath',
        daw: false, pharmacyId: 'pharm_001', prescriberId: 'prov_001', status: 'active',
        startDate: '2025-10-15', endDate: null, priorAuth: false, priorAuthNumber: null,
        discontinuedReason: null, discontinuedDate: null,
        fillHistory: [
            { fillDate: '2025-10-15', pharmacy: 'CVS Pharmacy #4521', quantity: 1, daysSupply: 30, fillNumber: 1 }
        ],
        history: [
            { action: 'prescribed', date: '2025-10-15', provider: 'Dr. Sarah Mitchell', note: 'Intermittent wheezing with URI' }
        ]
    },
    {
        id: 'rx_007', patientId: 'pat_001', drugId: 'drug_036', drugName: 'Gabapentin', brandName: 'Neurontin',
        formStrength: '300mg Capsule', dosage: '300mg', frequency: 'Three times daily', route: 'Oral', quantity: 90, daysSupply: 30,
        refillsTotal: 5, refillsRemaining: 4, sig: 'Take 1 capsule by mouth three times daily',
        daw: false, pharmacyId: 'pharm_001', prescriberId: 'prov_003', status: 'active',
        startDate: '2025-12-01', endDate: null, priorAuth: false, priorAuthNumber: null,
        discontinuedReason: null, discontinuedDate: null,
        fillHistory: [
            { fillDate: '2025-12-01', pharmacy: 'CVS Pharmacy #4521', quantity: 90, daysSupply: 30, fillNumber: 1 }
        ],
        history: [
            { action: 'prescribed', date: '2025-12-01', provider: 'Dr. Linda Reyes', note: 'Peripheral neuropathy, bilateral feet' }
        ]
    },
    {
        id: 'rx_008', patientId: 'pat_001', drugId: 'drug_047', drugName: 'Fluticasone Propionate Nasal', brandName: 'Flonase',
        formStrength: '50mcg/spray Nasal Spray', dosage: '50mcg', frequency: 'Once daily', route: 'Intranasal', quantity: 1, daysSupply: 30,
        refillsTotal: 2, refillsRemaining: 2, sig: 'Spray 2 sprays in each nostril once daily',
        daw: false, pharmacyId: 'pharm_001', prescriberId: 'prov_001', status: 'active',
        startDate: '2026-01-10', endDate: null, priorAuth: false, priorAuthNumber: null,
        discontinuedReason: null, discontinuedDate: null,
        fillHistory: [
            { fillDate: '2026-01-10', pharmacy: 'CVS Pharmacy #4521', quantity: 1, daysSupply: 30, fillNumber: 1 }
        ],
        history: [
            { action: 'prescribed', date: '2026-01-10', provider: 'Dr. Sarah Mitchell', note: 'Allergic rhinitis, seasonal' }
        ]
    },
    {
        id: 'rx_009', patientId: 'pat_001', drugId: 'drug_004', drugName: 'Lisinopril', brandName: 'Prinivil',
        formStrength: '10mg Tablet', dosage: '10mg', frequency: 'Once daily', route: 'Oral', quantity: 30, daysSupply: 30,
        refillsTotal: 5, refillsRemaining: 0, sig: 'Take 1 tablet by mouth once daily',
        daw: false, pharmacyId: 'pharm_001', prescriberId: 'prov_001', status: 'discontinued',
        startDate: '2025-01-15', endDate: '2025-08-20', priorAuth: false, priorAuthNumber: null,
        discontinuedReason: 'Persistent dry cough, switched to amlodipine', discontinuedDate: '2025-08-20',
        fillHistory: [
            { fillDate: '2025-01-15', pharmacy: 'CVS Pharmacy #4521', quantity: 30, daysSupply: 30, fillNumber: 1 },
            { fillDate: '2025-02-14', pharmacy: 'CVS Pharmacy #4521', quantity: 30, daysSupply: 30, fillNumber: 2 },
            { fillDate: '2025-03-16', pharmacy: 'CVS Pharmacy #4521', quantity: 30, daysSupply: 30, fillNumber: 3 }
        ],
        history: [
            { action: 'prescribed', date: '2025-01-15', provider: 'Dr. Sarah Mitchell', note: 'Hypertension, initial therapy' },
            { action: 'filled', date: '2025-01-15', pharmacy: 'CVS Pharmacy #4521' },
            { action: 'discontinued', date: '2025-08-20', provider: 'Dr. Sarah Mitchell', note: 'Persistent dry cough, switching to CCB' }
        ]
    },
    {
        id: 'rx_010', patientId: 'pat_001', drugId: 'drug_025', drugName: 'Amoxicillin', brandName: 'Amoxil',
        formStrength: '500mg Capsule', dosage: '500mg', frequency: 'Three times daily', route: 'Oral', quantity: 30, daysSupply: 10,
        refillsTotal: 0, refillsRemaining: 0, sig: 'Take 1 capsule by mouth three times daily for 10 days',
        daw: false, pharmacyId: 'pharm_001', prescriberId: 'prov_001', status: 'discontinued',
        startDate: '2024-11-05', endDate: '2024-11-15', priorAuth: false, priorAuthNumber: null,
        discontinuedReason: 'Allergic reaction - developed rash on day 3', discontinuedDate: '2024-11-08',
        fillHistory: [
            { fillDate: '2024-11-05', pharmacy: 'CVS Pharmacy #4521', quantity: 30, daysSupply: 10, fillNumber: 1 }
        ],
        history: [
            { action: 'prescribed', date: '2024-11-05', provider: 'Dr. Sarah Mitchell', note: 'Sinusitis' },
            { action: 'filled', date: '2024-11-05', pharmacy: 'CVS Pharmacy #4521' },
            { action: 'discontinued', date: '2024-11-08', provider: 'Dr. Sarah Mitchell', note: 'Allergic reaction - maculopapular rash. Allergy added to chart.' }
        ]
    },
    {
        id: 'rx_011', patientId: 'pat_001', drugId: 'drug_045', drugName: 'Prednisone', brandName: 'Prednisone',
        formStrength: '10mg Tablet', dosage: '10mg', frequency: 'Once daily', route: 'Oral', quantity: 21, daysSupply: 7,
        refillsTotal: 0, refillsRemaining: 0, sig: 'Take 4 tablets day 1-2, 3 tablets day 3-4, 2 tablets day 5, 1 tablet day 6-7',
        daw: false, pharmacyId: 'pharm_001', prescriberId: 'prov_001', status: 'completed',
        startDate: '2025-09-22', endDate: '2025-09-28', priorAuth: false, priorAuthNumber: null,
        discontinuedReason: null, discontinuedDate: null,
        fillHistory: [
            { fillDate: '2025-09-22', pharmacy: 'CVS Pharmacy #4521', quantity: 21, daysSupply: 7, fillNumber: 1 }
        ],
        history: [
            { action: 'prescribed', date: '2025-09-22', provider: 'Dr. Sarah Mitchell', note: 'Acute asthma exacerbation, 7-day taper' },
            { action: 'filled', date: '2025-09-22', pharmacy: 'CVS Pharmacy #4521' },
            { action: 'completed', date: '2025-09-28', provider: 'Dr. Sarah Mitchell', note: 'Taper completed' }
        ]
    },
    {
        id: 'rx_012', patientId: 'pat_001', drugId: 'drug_010', drugName: 'Hydrochlorothiazide', brandName: 'Hydrochlorothiazide',
        formStrength: '25mg Tablet', dosage: '25mg', frequency: 'Once daily', route: 'Oral', quantity: 30, daysSupply: 30,
        refillsTotal: 5, refillsRemaining: 5, sig: 'Take 1 tablet by mouth once daily in the morning',
        daw: false, pharmacyId: 'pharm_001', prescriberId: 'prov_001', status: 'on-hold',
        startDate: '2026-02-01', endDate: null, priorAuth: false, priorAuthNumber: null,
        discontinuedReason: null, discontinuedDate: null,
        fillHistory: [],
        history: [
            { action: 'prescribed', date: '2026-02-01', provider: 'Dr. Sarah Mitchell', note: 'Additional BP control needed. On hold pending lab results (electrolytes).' },
            { action: 'on-hold', date: '2026-02-01', provider: 'Dr. Sarah Mitchell', note: 'Awaiting BMP results before starting, sulfa allergy noted - monitoring closely' }
        ]
    },
    {
        id: 'rx_013', patientId: 'pat_001', drugId: 'drug_033', drugName: 'Sertraline', brandName: 'Zoloft',
        formStrength: '50mg Tablet', dosage: '50mg', frequency: 'Once daily', route: 'Oral', quantity: 30, daysSupply: 30,
        refillsTotal: 5, refillsRemaining: 3, sig: 'Take 1 tablet by mouth once daily in the morning',
        daw: false, pharmacyId: 'pharm_001', prescriberId: 'prov_001', status: 'active',
        startDate: '2025-07-10', endDate: null, priorAuth: false, priorAuthNumber: null,
        discontinuedReason: null, discontinuedDate: null,
        fillHistory: [
            { fillDate: '2025-07-10', pharmacy: 'CVS Pharmacy #4521', quantity: 30, daysSupply: 30, fillNumber: 1 },
            { fillDate: '2025-08-09', pharmacy: 'CVS Pharmacy #4521', quantity: 30, daysSupply: 30, fillNumber: 2 },
            { fillDate: '2025-09-08', pharmacy: 'CVS Pharmacy #4521', quantity: 30, daysSupply: 30, fillNumber: 3 }
        ],
        history: [
            { action: 'prescribed', date: '2025-07-10', provider: 'Dr. Sarah Mitchell', note: 'GAD, PHQ-9 score 14' },
            { action: 'filled', date: '2025-07-10', pharmacy: 'CVS Pharmacy #4521' }
        ]
    },
    {
        id: 'rx_014', patientId: 'pat_001', drugId: 'drug_012', drugName: 'Apixaban', brandName: 'Eliquis',
        formStrength: '5mg Tablet', dosage: '5mg', frequency: 'Twice daily', route: 'Oral', quantity: 60, daysSupply: 30,
        refillsTotal: 5, refillsRemaining: 4, sig: 'Take 1 tablet by mouth twice daily',
        daw: false, pharmacyId: 'pharm_001', prescriberId: 'prov_006', status: 'active',
        startDate: '2025-11-20', endDate: null, priorAuth: true, priorAuthNumber: 'PA-2025-88432',
        discontinuedReason: null, discontinuedDate: null,
        fillHistory: [
            { fillDate: '2025-11-20', pharmacy: 'CVS Pharmacy #4521', quantity: 60, daysSupply: 30, fillNumber: 1 },
            { fillDate: '2025-12-20', pharmacy: 'CVS Pharmacy #4521', quantity: 60, daysSupply: 30, fillNumber: 2 }
        ],
        history: [
            { action: 'prescribed', date: '2025-11-20', provider: 'Dr. Robert Tanaka', note: 'Atrial fibrillation, CHA2DS2-VASc 4' },
            { action: 'prior-auth-approved', date: '2025-11-22', note: 'PA approved by Medicare Part D' },
            { action: 'filled', date: '2025-11-20', pharmacy: 'CVS Pharmacy #4521' }
        ]
    },
    {
        id: 'rx_015', patientId: 'pat_001', drugId: 'drug_011', drugName: 'Warfarin', brandName: 'Coumadin',
        formStrength: '5mg Tablet', dosage: '5mg', frequency: 'Once daily', route: 'Oral', quantity: 30, daysSupply: 30,
        refillsTotal: 0, refillsRemaining: 0, sig: 'Take 1 tablet by mouth once daily',
        daw: false, pharmacyId: 'pharm_001', prescriberId: 'prov_006', status: 'discontinued',
        startDate: '2024-06-10', endDate: '2025-11-20', priorAuth: false, priorAuthNumber: null,
        discontinuedReason: 'Switched to Eliquis for better INR control', discontinuedDate: '2025-11-20',
        fillHistory: [
            { fillDate: '2024-06-10', pharmacy: 'CVS Pharmacy #4521', quantity: 30, daysSupply: 30, fillNumber: 1 },
            { fillDate: '2024-07-10', pharmacy: 'CVS Pharmacy #4521', quantity: 30, daysSupply: 30, fillNumber: 2 }
        ],
        history: [
            { action: 'prescribed', date: '2024-06-10', provider: 'Dr. Robert Tanaka', note: 'New AFib diagnosis' },
            { action: 'modified', date: '2024-08-15', provider: 'Dr. Robert Tanaka', note: 'Dose adjusted from 5mg to 7.5mg based on INR 1.6' },
            { action: 'discontinued', date: '2025-11-20', provider: 'Dr. Robert Tanaka', note: 'Switching to apixaban, labile INR despite dose adjustments' }
        ]
    },
    {
        id: 'rx_016', patientId: 'pat_002', drugId: 'drug_007', drugName: 'Metoprolol Succinate ER', brandName: 'Toprol-XL',
        formStrength: '50mg Tablet, Extended Release', dosage: '50mg', frequency: 'Once daily', route: 'Oral', quantity: 30, daysSupply: 30,
        refillsTotal: 5, refillsRemaining: 3, sig: 'Take 1 tablet by mouth once daily',
        daw: false, pharmacyId: 'pharm_003', prescriberId: 'prov_001', status: 'active',
        startDate: '2025-04-22', endDate: null, priorAuth: false, priorAuthNumber: null,
        discontinuedReason: null, discontinuedDate: null,
        fillHistory: [
            { fillDate: '2025-04-22', pharmacy: 'Rite Aid #5612', quantity: 30, daysSupply: 30, fillNumber: 1 },
            { fillDate: '2025-05-22', pharmacy: 'Rite Aid #5612', quantity: 30, daysSupply: 30, fillNumber: 2 }
        ],
        history: [
            { action: 'prescribed', date: '2025-04-22', provider: 'Dr. Sarah Mitchell', note: 'Hypertension, resting HR 92' }
        ]
    },
    {
        id: 'rx_017', patientId: 'pat_002', drugId: 'drug_001', drugName: 'Atorvastatin', brandName: 'Lipitor',
        formStrength: '40mg Tablet', dosage: '40mg', frequency: 'Once daily', route: 'Oral', quantity: 30, daysSupply: 30,
        refillsTotal: 5, refillsRemaining: 4, sig: 'Take 1 tablet by mouth once daily at bedtime',
        daw: false, pharmacyId: 'pharm_003', prescriberId: 'prov_001', status: 'active',
        startDate: '2025-05-10', endDate: null, priorAuth: false, priorAuthNumber: null,
        discontinuedReason: null, discontinuedDate: null,
        fillHistory: [
            { fillDate: '2025-05-10', pharmacy: 'Rite Aid #5612', quantity: 30, daysSupply: 30, fillNumber: 1 }
        ],
        history: [
            { action: 'prescribed', date: '2025-05-10', provider: 'Dr. Sarah Mitchell', note: 'LDL 192, high risk' }
        ]
    },
    {
        id: 'rx_018', patientId: 'pat_002', drugId: 'drug_034', drugName: 'Escitalopram', brandName: 'Lexapro',
        formStrength: '10mg Tablet', dosage: '10mg', frequency: 'Once daily', route: 'Oral', quantity: 30, daysSupply: 30,
        refillsTotal: 5, refillsRemaining: 2, sig: 'Take 1 tablet by mouth once daily in the morning',
        daw: false, pharmacyId: 'pharm_003', prescriberId: 'prov_002', status: 'active',
        startDate: '2025-02-14', endDate: null, priorAuth: false, priorAuthNumber: null,
        discontinuedReason: null, discontinuedDate: null,
        fillHistory: [
            { fillDate: '2025-02-14', pharmacy: 'Rite Aid #5612', quantity: 30, daysSupply: 30, fillNumber: 1 },
            { fillDate: '2025-03-16', pharmacy: 'Rite Aid #5612', quantity: 30, daysSupply: 30, fillNumber: 2 },
            { fillDate: '2025-04-15', pharmacy: 'Rite Aid #5612', quantity: 30, daysSupply: 30, fillNumber: 3 }
        ],
        history: [
            { action: 'prescribed', date: '2025-02-14', provider: 'Dr. James Okafor', note: 'MDD, PHQ-9 score 18' }
        ]
    },
    {
        id: 'rx_019', patientId: 'pat_002', drugId: 'drug_014', drugName: 'Metformin', brandName: 'Glucophage',
        formStrength: '500mg Tablet, Extended Release', dosage: '500mg', frequency: 'Once daily', route: 'Oral', quantity: 30, daysSupply: 30,
        refillsTotal: 5, refillsRemaining: 5, sig: 'Take 1 tablet by mouth once daily with dinner',
        daw: false, pharmacyId: 'pharm_003', prescriberId: 'prov_001', status: 'active',
        startDate: '2026-01-20', endDate: null, priorAuth: false, priorAuthNumber: null,
        discontinuedReason: null, discontinuedDate: null,
        fillHistory: [
            { fillDate: '2026-01-20', pharmacy: 'Rite Aid #5612', quantity: 30, daysSupply: 30, fillNumber: 1 }
        ],
        history: [
            { action: 'prescribed', date: '2026-01-20', provider: 'Dr. Sarah Mitchell', note: 'Prediabetes, A1C 6.3%' }
        ]
    },
    {
        id: 'rx_020', patientId: 'pat_003', drugId: 'drug_028', drugName: 'Azithromycin', brandName: 'Zithromax',
        formStrength: '250mg Tablet', dosage: '250mg', frequency: 'Once daily', route: 'Oral', quantity: 6, daysSupply: 5,
        refillsTotal: 0, refillsRemaining: 0, sig: 'Take 2 tablets on day 1, then 1 tablet once daily for 4 days',
        daw: false, pharmacyId: 'pharm_002', prescriberId: 'prov_004', status: 'completed',
        startDate: '2026-02-28', endDate: '2026-03-04', priorAuth: false, priorAuthNumber: null,
        discontinuedReason: null, discontinuedDate: null,
        fillHistory: [
            { fillDate: '2026-02-28', pharmacy: 'Walgreens #7893', quantity: 6, daysSupply: 5, fillNumber: 1 }
        ],
        history: [
            { action: 'prescribed', date: '2026-02-28', provider: 'Michael Brandt, NP', note: 'Community-acquired pneumonia' },
            { action: 'filled', date: '2026-02-28', pharmacy: 'Walgreens #7893' },
            { action: 'completed', date: '2026-03-04', note: 'Course completed' }
        ]
    },
    {
        id: 'rx_021', patientId: 'pat_003', drugId: 'drug_034', drugName: 'Escitalopram', brandName: 'Lexapro',
        formStrength: '5mg Tablet', dosage: '5mg', frequency: 'Once daily', route: 'Oral', quantity: 30, daysSupply: 30,
        refillsTotal: 5, refillsRemaining: 5, sig: 'Take 1 tablet by mouth once daily',
        daw: false, pharmacyId: 'pharm_002', prescriberId: 'prov_002', status: 'active',
        startDate: '2026-03-01', endDate: null, priorAuth: false, priorAuthNumber: null,
        discontinuedReason: null, discontinuedDate: null,
        fillHistory: [
            { fillDate: '2026-03-01', pharmacy: 'Walgreens #7893', quantity: 30, daysSupply: 30, fillNumber: 1 }
        ],
        history: [
            { action: 'prescribed', date: '2026-03-01', provider: 'Dr. James Okafor', note: 'Anxiety disorder, starting low dose' }
        ]
    },
    {
        id: 'rx_022', patientId: 'pat_004', drugId: 'drug_008', drugName: 'Valsartan', brandName: 'Diovan',
        formStrength: '160mg Tablet', dosage: '160mg', frequency: 'Once daily', route: 'Oral', quantity: 30, daysSupply: 30,
        refillsTotal: 5, refillsRemaining: 2, sig: 'Take 1 tablet by mouth once daily',
        daw: false, pharmacyId: 'pharm_005', prescriberId: 'prov_001', status: 'active',
        startDate: '2025-03-15', endDate: null, priorAuth: false, priorAuthNumber: null,
        discontinuedReason: null, discontinuedDate: null,
        fillHistory: [
            { fillDate: '2025-03-15', pharmacy: 'Kaiser Permanente Pharmacy - Geary', quantity: 30, daysSupply: 30, fillNumber: 1 },
            { fillDate: '2025-04-14', pharmacy: 'Kaiser Permanente Pharmacy - Geary', quantity: 30, daysSupply: 30, fillNumber: 2 },
            { fillDate: '2025-05-14', pharmacy: 'Kaiser Permanente Pharmacy - Geary', quantity: 30, daysSupply: 30, fillNumber: 3 }
        ],
        history: [
            { action: 'prescribed', date: '2025-03-15', provider: 'Dr. Sarah Mitchell', note: 'Hypertension, ACE inhibitor contraindicated due to angioedema history' }
        ]
    },
    {
        id: 'rx_023', patientId: 'pat_004', drugId: 'drug_017', drugName: 'Insulin Glargine', brandName: 'Lantus',
        formStrength: '100 units/mL (3mL pen) Solution for Injection', dosage: '24 units', frequency: 'Once daily', route: 'Subcutaneous', quantity: 5, daysSupply: 30,
        refillsTotal: 5, refillsRemaining: 3, sig: 'Inject 24 units subcutaneously once daily at bedtime',
        daw: false, pharmacyId: 'pharm_005', prescriberId: 'prov_001', status: 'active',
        startDate: '2025-01-08', endDate: null, priorAuth: true, priorAuthNumber: 'PA-2025-33210',
        discontinuedReason: null, discontinuedDate: null,
        fillHistory: [
            { fillDate: '2025-01-08', pharmacy: 'Kaiser Permanente Pharmacy - Geary', quantity: 5, daysSupply: 30, fillNumber: 1 },
            { fillDate: '2025-02-07', pharmacy: 'Kaiser Permanente Pharmacy - Geary', quantity: 5, daysSupply: 30, fillNumber: 2 }
        ],
        history: [
            { action: 'prescribed', date: '2025-01-08', provider: 'Dr. Sarah Mitchell', note: 'T2DM uncontrolled on oral agents, A1C 9.4%' },
            { action: 'prior-auth-approved', date: '2025-01-10', note: 'PA approved' },
            { action: 'modified', date: '2025-03-01', provider: 'Dr. Sarah Mitchell', note: 'Increased from 18 to 24 units based on fasting glucose logs' }
        ]
    },
    {
        id: 'rx_024', patientId: 'pat_004', drugId: 'drug_009', drugName: 'Furosemide', brandName: 'Lasix',
        formStrength: '40mg Tablet', dosage: '40mg', frequency: 'Once daily', route: 'Oral', quantity: 30, daysSupply: 30,
        refillsTotal: 5, refillsRemaining: 4, sig: 'Take 1 tablet by mouth once daily in the morning',
        daw: false, pharmacyId: 'pharm_005', prescriberId: 'prov_006', status: 'active',
        startDate: '2025-06-20', endDate: null, priorAuth: false, priorAuthNumber: null,
        discontinuedReason: null, discontinuedDate: null,
        fillHistory: [
            { fillDate: '2025-06-20', pharmacy: 'Kaiser Permanente Pharmacy - Geary', quantity: 30, daysSupply: 30, fillNumber: 1 }
        ],
        history: [
            { action: 'prescribed', date: '2025-06-20', provider: 'Dr. Robert Tanaka', note: 'CHF with peripheral edema, NYHA class II' }
        ]
    },
    {
        id: 'rx_025', patientId: 'pat_005', drugId: 'drug_027', drugName: 'Cephalexin', brandName: 'Keflex',
        formStrength: '500mg Capsule', dosage: '500mg', frequency: 'Four times daily', route: 'Oral', quantity: 28, daysSupply: 7,
        refillsTotal: 0, refillsRemaining: 0, sig: 'Take 1 capsule by mouth four times daily for 7 days',
        daw: false, pharmacyId: 'pharm_001', prescriberId: 'prov_004', status: 'active',
        startDate: '2026-03-14', endDate: null, priorAuth: false, priorAuthNumber: null,
        discontinuedReason: null, discontinuedDate: null,
        fillHistory: [
            { fillDate: '2026-03-14', pharmacy: 'CVS Pharmacy #4521', quantity: 28, daysSupply: 7, fillNumber: 1 }
        ],
        history: [
            { action: 'prescribed', date: '2026-03-14', provider: 'Michael Brandt, NP', note: 'Cellulitis, right lower extremity' }
        ]
    },
    {
        id: 'rx_026', patientId: 'pat_005', drugId: 'drug_056', drugName: 'Fluoxetine', brandName: 'Prozac',
        formStrength: '20mg Capsule', dosage: '20mg', frequency: 'Once daily', route: 'Oral', quantity: 30, daysSupply: 30,
        refillsTotal: 5, refillsRemaining: 1, sig: 'Take 1 capsule by mouth once daily in the morning',
        daw: false, pharmacyId: 'pharm_001', prescriberId: 'prov_002', status: 'active',
        startDate: '2025-09-01', endDate: null, priorAuth: false, priorAuthNumber: null,
        discontinuedReason: null, discontinuedDate: null,
        fillHistory: [
            { fillDate: '2025-09-01', pharmacy: 'CVS Pharmacy #4521', quantity: 30, daysSupply: 30, fillNumber: 1 },
            { fillDate: '2025-10-01', pharmacy: 'CVS Pharmacy #4521', quantity: 30, daysSupply: 30, fillNumber: 2 },
            { fillDate: '2025-11-01', pharmacy: 'CVS Pharmacy #4521', quantity: 30, daysSupply: 30, fillNumber: 3 },
            { fillDate: '2025-12-01', pharmacy: 'CVS Pharmacy #4521', quantity: 30, daysSupply: 30, fillNumber: 4 }
        ],
        history: [
            { action: 'prescribed', date: '2025-09-01', provider: 'Dr. James Okafor', note: 'Depression, starting SSRI' }
        ]
    },
    {
        id: 'rx_027', patientId: 'pat_006', drugId: 'drug_016', drugName: 'Empagliflozin', brandName: 'Jardiance',
        formStrength: '10mg Tablet', dosage: '10mg', frequency: 'Once daily', route: 'Oral', quantity: 30, daysSupply: 30,
        refillsTotal: 5, refillsRemaining: 3, sig: 'Take 1 tablet by mouth once daily in the morning',
        daw: false, pharmacyId: 'pharm_004', prescriberId: 'prov_001', status: 'active',
        startDate: '2025-08-15', endDate: null, priorAuth: true, priorAuthNumber: 'PA-2025-67891',
        discontinuedReason: null, discontinuedDate: null,
        fillHistory: [
            { fillDate: '2025-08-15', pharmacy: 'UCSF Medical Center Pharmacy', quantity: 30, daysSupply: 30, fillNumber: 1 },
            { fillDate: '2025-09-14', pharmacy: 'UCSF Medical Center Pharmacy', quantity: 30, daysSupply: 30, fillNumber: 2 }
        ],
        history: [
            { action: 'prescribed', date: '2025-08-15', provider: 'Dr. Sarah Mitchell', note: 'T2DM, metformin intolerant, also benefits for CHF' },
            { action: 'prior-auth-approved', date: '2025-08-18', note: 'PA approved by UnitedHealth' }
        ]
    },
    {
        id: 'rx_028', patientId: 'pat_006', drugId: 'drug_057', drugName: 'Carvedilol', brandName: 'Coreg',
        formStrength: '12.5mg Tablet', dosage: '12.5mg', frequency: 'Twice daily', route: 'Oral', quantity: 60, daysSupply: 30,
        refillsTotal: 5, refillsRemaining: 4, sig: 'Take 1 tablet by mouth twice daily with food',
        daw: false, pharmacyId: 'pharm_004', prescriberId: 'prov_006', status: 'active',
        startDate: '2025-07-01', endDate: null, priorAuth: false, priorAuthNumber: null,
        discontinuedReason: null, discontinuedDate: null,
        fillHistory: [
            { fillDate: '2025-07-01', pharmacy: 'UCSF Medical Center Pharmacy', quantity: 60, daysSupply: 30, fillNumber: 1 }
        ],
        history: [
            { action: 'prescribed', date: '2025-07-01', provider: 'Dr. Robert Tanaka', note: 'CHF with reduced EF, titrate up as tolerated' }
        ]
    },
    {
        id: 'rx_029', patientId: 'pat_006', drugId: 'drug_054', drugName: 'Spironolactone', brandName: 'Aldactone',
        formStrength: '25mg Tablet', dosage: '25mg', frequency: 'Once daily', route: 'Oral', quantity: 30, daysSupply: 30,
        refillsTotal: 5, refillsRemaining: 5, sig: 'Take 1 tablet by mouth once daily',
        daw: false, pharmacyId: 'pharm_004', prescriberId: 'prov_006', status: 'active',
        startDate: '2026-02-15', endDate: null, priorAuth: false, priorAuthNumber: null,
        discontinuedReason: null, discontinuedDate: null,
        fillHistory: [
            { fillDate: '2026-02-15', pharmacy: 'UCSF Medical Center Pharmacy', quantity: 30, daysSupply: 30, fillNumber: 1 }
        ],
        history: [
            { action: 'prescribed', date: '2026-02-15', provider: 'Dr. Robert Tanaka', note: 'HFrEF, adding aldosterone antagonist' }
        ]
    },
    {
        id: 'rx_030', patientId: 'pat_001', drugId: 'drug_049', drugName: 'Semaglutide', brandName: 'Ozempic',
        formStrength: '1mg/0.5mL Solution for Injection', dosage: '1mg', frequency: 'Once weekly', route: 'Subcutaneous', quantity: 1, daysSupply: 28,
        refillsTotal: 5, refillsRemaining: 4, sig: 'Inject 1mg subcutaneously once weekly',
        daw: false, pharmacyId: 'pharm_010', prescriberId: 'prov_001', status: 'active',
        startDate: '2026-01-15', endDate: null, priorAuth: true, priorAuthNumber: 'PA-2026-10234',
        discontinuedReason: null, discontinuedDate: null,
        fillHistory: [
            { fillDate: '2026-01-15', pharmacy: 'BioPlus Specialty Pharmacy', quantity: 1, daysSupply: 28, fillNumber: 1 },
            { fillDate: '2026-02-12', pharmacy: 'BioPlus Specialty Pharmacy', quantity: 1, daysSupply: 28, fillNumber: 2 }
        ],
        history: [
            { action: 'prescribed', date: '2026-01-15', provider: 'Dr. Sarah Mitchell', note: 'T2DM inadequately controlled on metformin, adding GLP-1 RA' },
            { action: 'prior-auth-approved', date: '2026-01-18', note: 'PA approved by Medicare Part D, step therapy met' }
        ]
    }
];

const REFILL_REQUESTS = [
    {
        id: 'rr_001', prescriptionId: 'rx_001', patientId: 'pat_001', drugName: 'Atorvastatin 20mg Tablet',
        patientName: 'Margaret Chen', pharmacyId: 'pharm_001', pharmacyName: 'CVS Pharmacy #4521',
        requestDate: '2026-03-15T10:23:00Z', status: 'pending', urgency: 'routine',
        originalPrescriber: 'Dr. Sarah Mitchell', refillsRemaining: 2,
        notes: 'Patient requesting routine refill. Last fill 2025-09-13.',
        denyReason: null, responseDate: null, respondedBy: null
    },
    {
        id: 'rr_002', prescriptionId: 'rx_003', patientId: 'pat_001', drugName: 'Metformin 1000mg Tablet',
        patientName: 'Margaret Chen', pharmacyId: 'pharm_001', pharmacyName: 'CVS Pharmacy #4521',
        requestDate: '2026-03-14T14:45:00Z', status: 'pending', urgency: 'routine',
        originalPrescriber: 'Dr. Sarah Mitchell', refillsRemaining: 3,
        notes: 'Routine refill request.',
        denyReason: null, responseDate: null, respondedBy: null
    },
    {
        id: 'rr_003', prescriptionId: 'rx_005', patientId: 'pat_001', drugName: 'Pantoprazole 40mg Tablet',
        patientName: 'Margaret Chen', pharmacyId: 'pharm_001', pharmacyName: 'CVS Pharmacy #4521',
        requestDate: '2026-03-16T09:10:00Z', status: 'pending', urgency: 'urgent',
        originalPrescriber: 'Dr. Sarah Mitchell', refillsRemaining: 1,
        notes: 'Patient ran out of medication 2 days ago. Requesting urgent refill.',
        denyReason: null, responseDate: null, respondedBy: null
    },
    {
        id: 'rr_004', prescriptionId: 'rx_007', patientId: 'pat_001', drugName: 'Gabapentin 300mg Capsule',
        patientName: 'Margaret Chen', pharmacyId: 'pharm_001', pharmacyName: 'CVS Pharmacy #4521',
        requestDate: '2026-03-12T16:30:00Z', status: 'approved', urgency: 'routine',
        originalPrescriber: 'Dr. Linda Reyes', refillsRemaining: 4,
        notes: 'Standard refill.',
        denyReason: null, responseDate: '2026-03-12T17:15:00Z', respondedBy: 'prov_001'
    },
    {
        id: 'rr_005', prescriptionId: 'rx_016', patientId: 'pat_002', drugName: 'Metoprolol Succinate ER 50mg Tablet',
        patientName: 'David Kowalski', pharmacyId: 'pharm_003', pharmacyName: 'Rite Aid #5612',
        requestDate: '2026-03-15T11:00:00Z', status: 'pending', urgency: 'routine',
        originalPrescriber: 'Dr. Sarah Mitchell', refillsRemaining: 3,
        notes: 'Refill request from pharmacy.',
        denyReason: null, responseDate: null, respondedBy: null
    },
    {
        id: 'rr_006', prescriptionId: 'rx_026', patientId: 'pat_005', drugName: 'Fluoxetine 20mg Capsule',
        patientName: 'Jessica Morales', pharmacyId: 'pharm_001', pharmacyName: 'CVS Pharmacy #4521',
        requestDate: '2026-03-13T08:45:00Z', status: 'denied', urgency: 'routine',
        originalPrescriber: 'Dr. James Okafor', refillsRemaining: 1,
        notes: 'Refill request.',
        denyReason: 'Need appointment - overdue for follow-up', responseDate: '2026-03-13T14:20:00Z', respondedBy: 'prov_002'
    },
    {
        id: 'rr_007', prescriptionId: 'rx_022', patientId: 'pat_004', drugName: 'Valsartan 160mg Tablet',
        patientName: 'William Thornton', pharmacyId: 'pharm_005', pharmacyName: 'Kaiser Permanente Pharmacy - Geary',
        requestDate: '2026-03-16T13:20:00Z', status: 'pending', urgency: 'routine',
        originalPrescriber: 'Dr. Sarah Mitchell', refillsRemaining: 2,
        notes: 'Routine refill.',
        denyReason: null, responseDate: null, respondedBy: null
    },
    {
        id: 'rr_008', prescriptionId: 'rx_014', patientId: 'pat_001', drugName: 'Apixaban 5mg Tablet',
        patientName: 'Margaret Chen', pharmacyId: 'pharm_001', pharmacyName: 'CVS Pharmacy #4521',
        requestDate: '2026-03-10T10:00:00Z', status: 'approved', urgency: 'urgent',
        originalPrescriber: 'Dr. Robert Tanaka', refillsRemaining: 4,
        notes: 'Urgent - anticoagulant, do not miss doses.',
        denyReason: null, responseDate: '2026-03-10T10:30:00Z', respondedBy: 'prov_001'
    },
    {
        id: 'rr_009', prescriptionId: 'rx_018', patientId: 'pat_002', drugName: 'Escitalopram 10mg Tablet',
        patientName: 'David Kowalski', pharmacyId: 'pharm_003', pharmacyName: 'Rite Aid #5612',
        requestDate: '2026-03-11T09:15:00Z', status: 'modified', urgency: 'routine',
        originalPrescriber: 'Dr. James Okafor', refillsRemaining: 2,
        notes: 'Patient requested dose increase to 20mg per last visit notes.',
        denyReason: null, responseDate: '2026-03-11T11:00:00Z', respondedBy: 'prov_002',
        modifiedDetails: 'Increased from 10mg to 20mg per patient request and clinical assessment'
    },
    {
        id: 'rr_010', prescriptionId: 'rx_024', patientId: 'pat_004', drugName: 'Furosemide 40mg Tablet',
        patientName: 'William Thornton', pharmacyId: 'pharm_005', pharmacyName: 'Kaiser Permanente Pharmacy - Geary',
        requestDate: '2026-03-17T07:30:00Z', status: 'pending', urgency: 'urgent',
        originalPrescriber: 'Dr. Robert Tanaka', refillsRemaining: 4,
        notes: 'Patient reporting increased edema. Pharmacy recommending urgent refill.',
        denyReason: null, responseDate: null, respondedBy: null
    },
    {
        id: 'rr_011', prescriptionId: 'rx_013', patientId: 'pat_001', drugName: 'Sertraline 50mg Tablet',
        patientName: 'Margaret Chen', pharmacyId: 'pharm_001', pharmacyName: 'CVS Pharmacy #4521',
        requestDate: '2026-03-17T15:45:00Z', status: 'pending', urgency: 'routine',
        originalPrescriber: 'Dr. Sarah Mitchell', refillsRemaining: 3,
        notes: 'Routine refill request.',
        denyReason: null, responseDate: null, respondedBy: null
    },
    {
        id: 'rr_012', prescriptionId: 'rx_028', patientId: 'pat_006', drugName: 'Carvedilol 12.5mg Tablet',
        patientName: 'Robert Fitzgerald', pharmacyId: 'pharm_004', pharmacyName: 'UCSF Medical Center Pharmacy',
        requestDate: '2026-03-09T12:00:00Z', status: 'approved', urgency: 'routine',
        originalPrescriber: 'Dr. Robert Tanaka', refillsRemaining: 4,
        notes: 'Standard refill for heart failure management.',
        denyReason: null, responseDate: '2026-03-09T13:45:00Z', respondedBy: 'prov_006'
    }
];

const DENY_REASONS = [
    'No longer needed',
    'Changed therapy',
    'Need appointment - overdue for follow-up',
    'Need lab work before renewal',
    'Need to verify diagnosis',
    'Patient non-compliant',
    'Insurance issue - need prior authorization',
    'Duplicate therapy',
    'Adverse reaction reported',
    'Other - see notes'
];

const FREQUENCIES = [
    'Once daily',
    'Twice daily',
    'Three times daily',
    'Four times daily',
    'Every 4 hours',
    'Every 4-6 hours',
    'Every 6 hours',
    'Every 6-8 hours',
    'Every 8 hours',
    'Every 12 hours',
    'Once weekly',
    'Twice weekly',
    'Every other day',
    'Once monthly',
    'As needed',
    'At bedtime',
    'Before meals',
    'After meals',
    'With meals'
];

const ROUTES = [
    'Oral',
    'Sublingual',
    'Topical',
    'Inhalation',
    'Intranasal',
    'Ophthalmic',
    'Otic',
    'Rectal',
    'Vaginal',
    'Subcutaneous',
    'Intramuscular',
    'Intravenous',
    'Transdermal'
];

const PRESCRIPTION_PRINT_FORMATS = ['standard', 'detailed', 'compact'];

const DEFAULT_SETTINGS = {
    defaultPharmacy: 'pharm_001',
    prescriptionFormat: 'standard',
    defaultDaysSupply: 30,
    defaultRefills: 0,
    showGenericFirst: true,
    autoCheckInteractions: true,
    requireAllergyReview: true,
    eRxEnabled: true,
    printFormat: 'standard',
    signatureRequired: true,
    favoritesDrugIds: ['drug_001', 'drug_005', 'drug_014', 'drug_018', 'drug_019', 'drug_033', 'drug_025', 'drug_028', 'drug_043', 'drug_045']
};
