const SEED_DATA_VERSION = 1;

const CURRENT_USER = {
    id: 'user_1',
    name: 'Sarah Chen',
    email: 'sarah.chen@meridianlaw.com',
    role: 'administrator',
    hourlyRate: 350,
    avatarColor: '#4A90D9'
};

const USERS = [
    { id: 'user_1', name: 'Sarah Chen', email: 'sarah.chen@meridianlaw.com', role: 'administrator', hourlyRate: 350, avatarColor: '#4A90D9' },
    { id: 'user_2', name: 'Marcus Williams', email: 'marcus.williams@meridianlaw.com', role: 'attorney', hourlyRate: 425, avatarColor: '#E67E22' },
    { id: 'user_3', name: 'Diana Reyes', email: 'diana.reyes@meridianlaw.com', role: 'attorney', hourlyRate: 475, avatarColor: '#9B59B6' },
    { id: 'user_4', name: 'Thomas O\'Brien', email: 'thomas.obrien@meridianlaw.com', role: 'of_counsel', hourlyRate: 550, avatarColor: '#2ECC71' },
    { id: 'user_5', name: 'Priya Sharma', email: 'priya.sharma@meridianlaw.com', role: 'associate', hourlyRate: 275, avatarColor: '#E74C3C' },
    { id: 'user_6', name: 'Kevin Nakamura', email: 'kevin.nakamura@meridianlaw.com', role: 'associate', hourlyRate: 250, avatarColor: '#3498DB' },
    { id: 'user_7', name: 'Lisa Tran', email: 'lisa.tran@meridianlaw.com', role: 'paralegal', hourlyRate: 150, avatarColor: '#1ABC9C' },
    { id: 'user_8', name: 'Robert Jackson', email: 'robert.jackson@meridianlaw.com', role: 'attorney', hourlyRate: 400, avatarColor: '#F39C12' },
    { id: 'user_9', name: 'Angela Martinez', email: 'angela.martinez@meridianlaw.com', role: 'paralegal', hourlyRate: 145, avatarColor: '#8E44AD' },
    { id: 'user_10', name: 'David Kim', email: 'david.kim@meridianlaw.com', role: 'associate', hourlyRate: 285, avatarColor: '#2C3E50' },
    { id: 'user_11', name: 'Jennifer Walsh', email: 'jennifer.walsh@meridianlaw.com', role: 'legal_assistant', hourlyRate: 125, avatarColor: '#D35400' },
    { id: 'user_12', name: 'Michael Foster', email: 'michael.foster@meridianlaw.com', role: 'attorney', hourlyRate: 450, avatarColor: '#27AE60' },
    { id: 'user_13', name: 'Rachel Goldstein', email: 'rachel.goldstein@meridianlaw.com', role: 'of_counsel', hourlyRate: 525, avatarColor: '#C0392B' },
    { id: 'user_14', name: 'James Cooper', email: 'james.cooper@meridianlaw.com', role: 'associate', hourlyRate: 260, avatarColor: '#7F8C8D' },
    { id: 'user_15', name: 'Maria Santos', email: 'maria.santos@meridianlaw.com', role: 'legal_assistant', hourlyRate: 130, avatarColor: '#16A085' },
    { id: 'user_16', name: 'William Park', email: 'william.park@meridianlaw.com', role: 'attorney', hourlyRate: 410, avatarColor: '#8E44AD' }
];

const GROUPS = [
    { id: 'group_1', name: 'Litigation Team', userIds: ['user_1', 'user_2', 'user_5', 'user_8', 'user_10'] },
    { id: 'group_2', name: 'Family Law Division', userIds: ['user_3', 'user_6', 'user_9', 'user_11'] },
    { id: 'group_3', name: 'Corporate & Business', userIds: ['user_4', 'user_12', 'user_14'] },
    { id: 'group_4', name: 'Criminal Defense Unit', userIds: ['user_8', 'user_5', 'user_15'] },
    { id: 'group_5', name: 'Real Estate Practice', userIds: ['user_13', 'user_6', 'user_7'] },
    { id: 'group_6', name: 'Administrative Staff', userIds: ['user_7', 'user_9', 'user_11', 'user_15'] }
];

const CONTACTS = [
    { id: 'contact_1', type: 'person', firstName: 'James', lastName: 'Patterson', companyName: null, displayName: 'James Patterson', email: 'james.patterson@email.com', phone: '(555) 234-5678', address: '123 Oak Street, San Francisco, CA 94102', tags: ['personal-injury', 'referral'], createdAt: '2024-03-15T10:00:00Z' },
    { id: 'contact_2', type: 'person', firstName: 'Maria', lastName: 'Gonzalez', companyName: null, displayName: 'Maria Gonzalez', email: 'maria.gonzalez@gmail.com', phone: '(555) 345-6789', address: '456 Mission Blvd, San Jose, CA 95112', tags: ['family-law'], createdAt: '2024-01-10T08:30:00Z' },
    { id: 'contact_3', type: 'person', firstName: 'William', lastName: 'Chen-Ramirez', companyName: null, displayName: 'William Chen-Ramirez', email: 'wchenramirez@outlook.com', phone: '(555) 456-7890', address: '789 Broadway Ave, Oakland, CA 94612', tags: ['criminal-defense'], createdAt: '2024-02-20T11:15:00Z' },
    { id: 'contact_4', type: 'company', firstName: null, lastName: null, companyName: 'Vertex Technologies Inc.', displayName: 'Vertex Technologies Inc.', email: 'legal@vertextech.com', phone: '(555) 567-8901', address: '1200 Market Street, Suite 400, San Francisco, CA 94103', tags: ['corporate', 'technology'], createdAt: '2024-04-01T09:00:00Z' },
    { id: 'contact_5', type: 'person', firstName: 'Aisha', lastName: 'Johnson', companyName: null, displayName: 'Aisha Johnson', email: 'aisha.j@yahoo.com', phone: '(555) 678-9012', address: '321 Pine Street, Berkeley, CA 94704', tags: ['personal-injury', 'slip-and-fall'], createdAt: '2024-05-12T14:20:00Z' },
    { id: 'contact_6', type: 'person', firstName: 'Robert', lastName: 'O\'Malley', companyName: null, displayName: "Robert O'Malley", email: 'romalley@comcast.net', phone: '(555) 789-0123', address: '654 Sunset Drive, Daly City, CA 94015', tags: ['real-estate'], createdAt: '2024-03-28T16:45:00Z' },
    { id: 'contact_7', type: 'company', firstName: null, lastName: null, companyName: 'Bay Area Construction LLC', displayName: 'Bay Area Construction LLC', email: 'info@bayareaconst.com', phone: '(555) 890-1234', address: '2100 Industrial Blvd, South San Francisco, CA 94080', tags: ['construction', 'business'], createdAt: '2024-06-05T10:30:00Z' },
    { id: 'contact_8', type: 'person', firstName: 'Diane', lastName: 'Kowalski', companyName: null, displayName: 'Diane Kowalski', email: 'diane.kowalski@email.com', phone: '(555) 901-2345', address: '987 Elm Court, Palo Alto, CA 94301', tags: ['estate-planning'], createdAt: '2024-07-14T08:00:00Z' },
    { id: 'contact_9', type: 'person', firstName: 'Marcus', lastName: 'Thompson', companyName: null, displayName: 'Marcus Thompson', email: 'mthompson99@gmail.com', phone: '(555) 012-3456', address: '543 MLK Jr Way, Oakland, CA 94607', tags: ['criminal-defense', 'dui'], createdAt: '2024-08-22T13:10:00Z' },
    { id: 'contact_10', type: 'company', firstName: null, lastName: null, companyName: 'Pacific Rim Imports & Exports', displayName: 'Pacific Rim Imports & Exports', email: 'legal@pacificrim-ie.com', phone: '(555) 123-4567', address: '500 Embarcadero, Suite 200, San Francisco, CA 94105', tags: ['international', 'trade'], createdAt: '2024-01-25T09:45:00Z' },
    { id: 'contact_11', type: 'person', firstName: 'Stephanie', lastName: 'Nguyen', companyName: null, displayName: 'Stephanie Nguyen', email: 'steph.nguyen@email.com', phone: '(555) 234-5679', address: '876 Geary Blvd, San Francisco, CA 94109', tags: ['family-law', 'custody'], createdAt: '2024-09-03T11:20:00Z' },
    { id: 'contact_12', type: 'person', firstName: 'David', lastName: 'Washington', companyName: null, displayName: 'David Washington', email: 'dwashington@email.com', phone: '(555) 345-6780', address: '234 Central Ave, Alameda, CA 94501', tags: ['personal-injury', 'workplace'], createdAt: '2024-04-18T15:30:00Z' },
    { id: 'contact_13', type: 'company', firstName: null, lastName: null, companyName: 'Golden Gate Properties', displayName: 'Golden Gate Properties', email: 'contact@ggproperties.com', phone: '(555) 456-7891', address: '1 Ferry Building, Suite 300, San Francisco, CA 94111', tags: ['real-estate', 'commercial'], createdAt: '2024-02-14T10:00:00Z' },
    { id: 'contact_14', type: 'person', firstName: 'Jennifer', lastName: 'Li', companyName: null, displayName: 'Jennifer Li', email: 'jennifer.li@protonmail.com', phone: '(555) 567-8902', address: '432 Castro Street, Mountain View, CA 94041', tags: ['employment', 'discrimination'], createdAt: '2024-10-07T09:15:00Z' },
    { id: 'contact_15', type: 'person', firstName: 'Anthony', lastName: 'Russo', companyName: null, displayName: 'Anthony Russo', email: 'arusso@email.com', phone: '(555) 678-9013', address: '765 Columbus Ave, San Francisco, CA 94133', tags: ['personal-injury', 'auto-accident'], createdAt: '2024-05-30T12:40:00Z' },
    { id: 'contact_16', type: 'person', firstName: 'Karen', lastName: 'Blackwell', companyName: null, displayName: 'Karen Blackwell', email: 'kblackwell@yahoo.com', phone: '(555) 789-0124', address: '198 Haight Street, San Francisco, CA 94117', tags: ['family-law', 'divorce'], createdAt: '2024-06-19T14:00:00Z' },
    { id: 'contact_17', type: 'company', firstName: null, lastName: null, companyName: 'NovaBio Pharmaceuticals', displayName: 'NovaBio Pharmaceuticals', email: 'legal@novabio.com', phone: '(555) 890-1235', address: '3400 Hillview Ave, Palo Alto, CA 94304', tags: ['corporate', 'pharmaceutical'], createdAt: '2024-03-05T08:20:00Z' },
    { id: 'contact_18', type: 'person', firstName: 'Timothy', lastName: 'O\'Connor', companyName: null, displayName: "Timothy O'Connor", email: 'tim.oconnor@gmail.com', phone: '(555) 901-2346', address: '523 Divisadero St, San Francisco, CA 94117', tags: ['criminal-defense'], createdAt: '2024-07-28T16:55:00Z' },
    { id: 'contact_19', type: 'person', firstName: 'Patricia', lastName: 'Yamamoto', companyName: null, displayName: 'Patricia Yamamoto', email: 'pyamamoto@email.com', phone: '(555) 012-3457', address: '890 Japan Center, San Francisco, CA 94115', tags: ['estate-planning', 'trust'], createdAt: '2024-08-15T10:10:00Z' },
    { id: 'contact_20', type: 'company', firstName: null, lastName: null, companyName: 'Sierra Nevada Brewing Co.', displayName: 'Sierra Nevada Brewing Co.', email: 'legal@sierranevadabrew.com', phone: '(555) 123-4568', address: '1075 E 20th St, Chico, CA 95928', tags: ['business', 'food-beverage'], createdAt: '2024-11-02T09:00:00Z' },
    { id: 'contact_21', type: 'person', firstName: 'Charles', lastName: 'Mbeki', companyName: null, displayName: 'Charles Mbeki', email: 'cmbeki@outlook.com', phone: '(555) 234-5680', address: '345 University Ave, Sacramento, CA 95825', tags: ['immigration'], createdAt: '2024-04-22T11:30:00Z' },
    { id: 'contact_22', type: 'person', firstName: 'Laura', lastName: 'Fitzgerald', companyName: null, displayName: 'Laura Fitzgerald', email: 'lfitzgerald@email.com', phone: '(555) 345-6781', address: '678 Broadway, Redwood City, CA 94063', tags: ['personal-injury', 'medical-malpractice'], createdAt: '2024-09-18T13:25:00Z' },
    { id: 'contact_23', type: 'person', firstName: 'Mohammed', lastName: 'Al-Rashid', companyName: null, displayName: 'Mohammed Al-Rashid', email: 'malrashid@gmail.com', phone: '(555) 456-7892', address: '901 Fremont Blvd, Fremont, CA 94538', tags: ['business', 'partnership'], createdAt: '2024-02-08T09:50:00Z' },
    { id: 'contact_24', type: 'company', firstName: null, lastName: null, companyName: 'Coastal Realty Group', displayName: 'Coastal Realty Group', email: 'office@coastalrealtygrp.com', phone: '(555) 567-8903', address: '250 Pacific Ave, Santa Cruz, CA 95060', tags: ['real-estate'], createdAt: '2024-12-01T08:00:00Z' },
    { id: 'contact_25', type: 'person', firstName: 'Emily', lastName: 'Sato', companyName: null, displayName: 'Emily Sato', email: 'emily.sato@email.com', phone: '(555) 678-9014', address: '412 Clement Street, San Francisco, CA 94118', tags: ['family-law', 'adoption'], createdAt: '2024-05-05T10:40:00Z' },
    { id: 'contact_26', type: 'person', firstName: 'Brian', lastName: 'Doyle', companyName: null, displayName: 'Brian Doyle', email: 'bdoyle@comcast.net', phone: '(555) 789-0125', address: '567 Grand Ave, South San Francisco, CA 94080', tags: ['personal-injury', 'construction'], createdAt: '2024-10-25T15:15:00Z' },
    { id: 'contact_27', type: 'person', firstName: 'Sandra', lastName: 'Petrovic', companyName: null, displayName: 'Sandra Petrovic', email: 'spetrovic@email.com', phone: '(555) 890-1236', address: '134 Lakeshore Drive, Oakland, CA 94610', tags: ['employment'], createdAt: '2024-06-30T12:00:00Z' },
    { id: 'contact_28', type: 'company', firstName: null, lastName: null, companyName: 'TechVenture Capital Partners', displayName: 'TechVenture Capital Partners', email: 'legal@tvcp.com', phone: '(555) 901-2347', address: '2200 Sand Hill Road, Suite 100, Menlo Park, CA 94025', tags: ['corporate', 'venture-capital'], createdAt: '2024-01-15T14:30:00Z' },
    { id: 'contact_29', type: 'person', firstName: 'Richard', lastName: 'Hernandez', companyName: null, displayName: 'Richard Hernandez', email: 'rhernandez@yahoo.com', phone: '(555) 012-3458', address: '823 Mission Street, San Francisco, CA 94103', tags: ['criminal-defense', 'felony'], createdAt: '2024-07-04T08:45:00Z' },
    { id: 'contact_30', type: 'company', firstName: null, lastName: null, companyName: 'ABC Insurance Co.', displayName: 'ABC Insurance Co.', email: 'claims@abcinsurance.com', phone: '(555) 100-2000', address: '4000 Insurance Plaza, Los Angeles, CA 90017', tags: ['insurance'], createdAt: '2024-01-05T09:00:00Z' },
    { id: 'contact_31', type: 'person', firstName: 'Natasha', lastName: 'Volkov', companyName: null, displayName: 'Natasha Volkov', email: 'nvolkov@protonmail.com', phone: '(555) 234-5681', address: '290 Divisadero St, San Francisco, CA 94117', tags: ['immigration', 'asylum'], createdAt: '2024-08-09T10:20:00Z' },
    { id: 'contact_32', type: 'person', firstName: 'Gregory', lastName: 'Simmons', companyName: null, displayName: 'Gregory Simmons', email: 'gsimmons@email.com', phone: '(555) 345-6782', address: '145 Noe Street, San Francisco, CA 94114', tags: ['personal-injury'], createdAt: '2024-11-14T13:50:00Z' },
    { id: 'contact_33', type: 'person', firstName: 'Catherine', lastName: 'Park-Anderson', companyName: null, displayName: 'Catherine Park-Anderson', email: 'cparkanderson@gmail.com', phone: '(555) 456-7893', address: '678 El Camino Real, Millbrae, CA 94030', tags: ['family-law', 'prenuptial'], createdAt: '2024-03-22T09:30:00Z' },
    { id: 'contact_34', type: 'company', firstName: null, lastName: null, companyName: 'Bay Logistics International', displayName: 'Bay Logistics International', email: 'legal@baylogistics.com', phone: '(555) 567-8904', address: '800 Port of Oakland, Oakland, CA 94607', tags: ['business', 'logistics'], createdAt: '2024-04-10T11:00:00Z' },
    { id: 'contact_35', type: 'person', firstName: 'Derek', lastName: 'Franklin', companyName: null, displayName: 'Derek Franklin', email: 'dfranklin@email.com', phone: '(555) 678-9015', address: '901 Van Ness Ave, San Francisco, CA 94109', tags: ['criminal-defense', 'white-collar'], createdAt: '2024-12-18T15:40:00Z' },
    { id: 'contact_36', type: 'person', firstName: 'Hannah', lastName: 'McCarthy', companyName: null, displayName: 'Hannah McCarthy', email: 'hmccarthy@outlook.com', phone: '(555) 789-0126', address: '345 Hayes Street, San Francisco, CA 94102', tags: ['personal-injury', 'pedestrian'], createdAt: '2024-09-27T08:15:00Z' },
    { id: 'contact_37', type: 'person', firstName: 'Oscar', lastName: 'Gutierrez', companyName: null, displayName: 'Oscar Gutierrez', email: 'ogutierrez@gmail.com', phone: '(555) 890-1237', address: '567 24th Street, Oakland, CA 94612', tags: ['employment', 'wage-theft'], createdAt: '2024-06-12T14:10:00Z' },
    { id: 'contact_38', type: 'company', firstName: null, lastName: null, companyName: 'Redwood Financial Services', displayName: 'Redwood Financial Services', email: 'compliance@redwoodfs.com', phone: '(555) 901-2348', address: '1800 Financial Blvd, Suite 500, San Mateo, CA 94402', tags: ['corporate', 'financial'], createdAt: '2024-02-28T10:30:00Z' },
    { id: 'contact_39', type: 'person', firstName: 'Janet', lastName: 'Crawford', companyName: null, displayName: 'Janet Crawford', email: 'jcrawford@email.com', phone: '(555) 012-3459', address: '432 Scott Street, San Francisco, CA 94117', tags: ['estate-planning'], createdAt: '2024-10-03T09:00:00Z' },
    { id: 'contact_40', type: 'person', firstName: 'Victor', lastName: 'Okafor', companyName: null, displayName: 'Victor Okafor', email: 'vokafor@yahoo.com', phone: '(555) 234-5682', address: '789 Shattuck Ave, Berkeley, CA 94707', tags: ['personal-injury', 'product-liability'], createdAt: '2024-07-19T11:45:00Z' },
    { id: 'contact_41', type: 'person', firstName: 'Elizabeth', lastName: 'Morrison', companyName: null, displayName: 'Elizabeth Morrison', email: 'emorrison@email.com', phone: '(555) 345-6783', address: '234 Pacific Heights, San Francisco, CA 94115', tags: ['real-estate', 'residential'], createdAt: '2024-05-21T16:20:00Z' },
    { id: 'contact_42', type: 'company', firstName: null, lastName: null, companyName: 'CalComp Workers Compensation', displayName: 'CalComp Workers Compensation', email: 'liens@calcomp-wc.com', phone: '(555) 456-7894', address: '3200 Wilshire Blvd, Los Angeles, CA 90010', tags: ['insurance', 'workers-comp'], createdAt: '2024-01-20T08:00:00Z' },
    { id: 'contact_43', type: 'person', firstName: 'Andrew', lastName: 'Kim', companyName: null, displayName: 'Andrew Kim', email: 'akim@gmail.com', phone: '(555) 567-8905', address: '876 Taraval Street, San Francisco, CA 94116', tags: ['business', 'startup'], createdAt: '2024-11-30T10:50:00Z' },
    { id: 'contact_44', type: 'person', firstName: 'Rebecca', lastName: 'Stone', companyName: null, displayName: 'Rebecca Stone', email: 'rstone@protonmail.com', phone: '(555) 678-9016', address: '145 Guerrero Street, San Francisco, CA 94103', tags: ['family-law', 'domestic-violence'], createdAt: '2024-08-04T13:00:00Z' },
    { id: 'contact_45', type: 'person', firstName: 'Linda', lastName: 'Patterson', companyName: null, displayName: 'Linda Patterson', email: 'linda.patterson@email.com', phone: '(555) 789-0127', address: '123 Oak Street, San Francisco, CA 94102', tags: ['family'], createdAt: '2024-03-15T10:05:00Z' },
    { id: 'contact_46', type: 'person', firstName: 'Frank', lastName: 'DeLuca', companyName: null, displayName: 'Frank DeLuca', email: 'fdeluca@email.com', phone: '(555) 890-1238', address: '654 North Beach, San Francisco, CA 94133', tags: ['criminal-defense'], createdAt: '2024-12-05T14:30:00Z' },
    { id: 'contact_47', type: 'person', firstName: 'Christina', lastName: 'Ababio', companyName: null, displayName: 'Christina Ababio', email: 'cababio@outlook.com', phone: '(555) 901-2349', address: '567 MLK Jr Blvd, Oakland, CA 94607', tags: ['personal-injury'], createdAt: '2024-04-28T09:30:00Z' },
    { id: 'contact_48', type: 'company', firstName: null, lastName: null, companyName: 'Mission District Restaurant Group', displayName: 'Mission District Restaurant Group', email: 'legal@missionrestaurants.com', phone: '(555) 012-3460', address: '2400 Mission Street, San Francisco, CA 94110', tags: ['business', 'food-beverage'], createdAt: '2024-06-25T08:15:00Z' },
    { id: 'contact_49', type: 'person', firstName: 'Terrence', lastName: 'Mills', companyName: null, displayName: 'Terrence Mills', email: 'tmills@gmail.com', phone: '(555) 234-5683', address: '321 Potrero Ave, San Francisco, CA 94110', tags: ['personal-injury', 'motorcycle'], createdAt: '2024-09-11T11:00:00Z' },
    { id: 'contact_50', type: 'person', firstName: 'Susan', lastName: 'Chang', companyName: null, displayName: 'Susan Chang', email: 'schang@email.com', phone: '(555) 345-6784', address: '890 Irving Street, San Francisco, CA 94122', tags: ['employment', 'wrongful-termination'], createdAt: '2024-10-16T15:45:00Z' },
    { id: 'contact_51', type: 'company', firstName: null, lastName: null, companyName: 'Pinnacle Software Solutions', displayName: 'Pinnacle Software Solutions', email: 'legal@pinnaclesoft.com', phone: '(555) 456-7895', address: '1500 Page Mill Rd, Palo Alto, CA 94304', tags: ['technology', 'corporate'], createdAt: '2024-02-18T10:00:00Z' },
    { id: 'contact_52', type: 'person', firstName: 'Douglas', lastName: 'Reed', companyName: null, displayName: 'Douglas Reed', email: 'dreed@comcast.net', phone: '(555) 567-8906', address: '234 Marina Blvd, San Francisco, CA 94123', tags: ['estate-planning', 'probate'], createdAt: '2024-07-09T09:20:00Z' },
    { id: 'contact_53', type: 'person', firstName: 'Angela', lastName: 'Dimitriou', companyName: null, displayName: 'Angela Dimitriou', email: 'adimitriou@email.com', phone: '(555) 678-9017', address: '678 Balboa Street, San Francisco, CA 94118', tags: ['personal-injury', 'dog-bite'], createdAt: '2024-11-21T13:40:00Z' },
    { id: 'contact_54', type: 'person', firstName: 'Raymond', lastName: 'Torres', companyName: null, displayName: 'Raymond Torres', email: 'rtorres@yahoo.com', phone: '(555) 789-0128', address: '432 Valencia Street, San Francisco, CA 94103', tags: ['criminal-defense', 'misdemeanor'], createdAt: '2024-08-27T08:50:00Z' },
    { id: 'contact_55', type: 'company', firstName: null, lastName: null, companyName: 'SF General Hospital - Records Dept', displayName: 'SF General Hospital - Records Dept', email: 'medrecords@sfgeneral.org', phone: '(555) 890-1239', address: '1001 Potrero Ave, San Francisco, CA 94110', tags: ['medical-provider'], createdAt: '2024-01-02T08:00:00Z' },
    { id: 'contact_56', type: 'company', firstName: null, lastName: null, companyName: 'Bay Area Orthopedic Associates', displayName: 'Bay Area Orthopedic Associates', email: 'records@bayortho.com', phone: '(555) 901-2350', address: '3000 California Street, Suite 200, San Francisco, CA 94115', tags: ['medical-provider'], createdAt: '2024-01-02T08:05:00Z' },
    { id: 'contact_57', type: 'company', firstName: null, lastName: null, companyName: 'Pacific Physical Therapy Center', displayName: 'Pacific Physical Therapy Center', email: 'billing@pacificpt.com', phone: '(555) 012-3461', address: '1200 Divisadero Street, San Francisco, CA 94115', tags: ['medical-provider'], createdAt: '2024-01-02T08:10:00Z' },
    { id: 'contact_58', type: 'company', firstName: null, lastName: null, companyName: 'State Farm Insurance - Liens', displayName: 'State Farm Insurance - Liens', email: 'liens@statefarm.com', phone: '(555) 200-3000', address: '1 State Farm Plaza, Bloomington, IL 61710', tags: ['insurance', 'lien-holder'], createdAt: '2024-01-03T09:00:00Z' },
    { id: 'contact_59', type: 'company', firstName: null, lastName: null, companyName: 'UCSF Medical Center - Billing', displayName: 'UCSF Medical Center - Billing', email: 'billing@ucsf.edu', phone: '(555) 234-5684', address: '505 Parnassus Ave, San Francisco, CA 94143', tags: ['medical-provider'], createdAt: '2024-01-02T08:15:00Z' },
    { id: 'contact_60', type: 'company', firstName: null, lastName: null, companyName: 'Dr. Michael Reeves Chiropractic', displayName: 'Dr. Michael Reeves Chiropractic', email: 'office@reeveschiro.com', phone: '(555) 345-6785', address: '789 Polk Street, San Francisco, CA 94109', tags: ['medical-provider'], createdAt: '2024-01-02T08:20:00Z' },
    { id: 'contact_61', type: 'person', firstName: 'Nancy', lastName: 'Whitfield', companyName: null, displayName: 'Nancy Whitfield', email: 'nwhitfield@email.com', phone: '(555) 456-7896', address: '1023 Stockton Street, San Francisco, CA 94108', tags: ['personal-injury'], createdAt: '2024-12-10T10:30:00Z' },
    { id: 'contact_62', type: 'person', firstName: 'Jerome', lastName: 'Baptiste', companyName: null, displayName: 'Jerome Baptiste', email: 'jbaptiste@gmail.com', phone: '(555) 567-8907', address: '456 Fillmore Street, San Francisco, CA 94117', tags: ['family-law'], createdAt: '2025-01-05T14:00:00Z' },
    { id: 'contact_63', type: 'company', firstName: null, lastName: null, companyName: 'Alliance Property Management', displayName: 'Alliance Property Management', email: 'legal@allianceprop.com', phone: '(555) 678-9018', address: '600 Montgomery Street, Suite 800, San Francisco, CA 94111', tags: ['real-estate', 'property-management'], createdAt: '2024-05-15T09:00:00Z' },
    { id: 'contact_64', type: 'person', firstName: 'Yuki', lastName: 'Tanaka', companyName: null, displayName: 'Yuki Tanaka', email: 'ytanaka@outlook.com', phone: '(555) 789-0129', address: '234 Japantown, San Francisco, CA 94115', tags: ['immigration', 'visa'], createdAt: '2025-01-20T08:30:00Z' },
    { id: 'contact_65', type: 'person', firstName: 'Paul', lastName: 'Brennan', companyName: null, displayName: 'Paul Brennan', email: 'pbrennan@email.com', phone: '(555) 890-1240', address: '567 Dolores Street, San Francisco, CA 94110', tags: ['personal-injury', 'slip-and-fall'], createdAt: '2025-02-03T11:15:00Z' },
    { id: 'contact_66', type: 'company', firstName: null, lastName: null, companyName: 'Meridian Radiology Associates', displayName: 'Meridian Radiology Associates', email: 'records@meridianrad.com', phone: '(555) 901-2351', address: '2300 Sutter Street, San Francisco, CA 94115', tags: ['medical-provider'], createdAt: '2024-01-02T08:25:00Z' },
    { id: 'contact_67', type: 'person', firstName: 'Christina', lastName: 'Vasquez', companyName: null, displayName: 'Christina Vasquez', email: 'cvasquez@gmail.com', phone: '(555) 012-3462', address: '890 Cesar Chavez, San Francisco, CA 94124', tags: ['family-law', 'child-support'], createdAt: '2024-04-14T13:20:00Z' },
    { id: 'contact_68', type: 'company', firstName: null, lastName: null, companyName: 'Horizon Healthcare Partners', displayName: 'Horizon Healthcare Partners', email: 'admin@horizonhcp.com', phone: '(555) 234-5685', address: '1400 California Street, San Francisco, CA 94109', tags: ['medical-provider'], createdAt: '2024-01-02T08:30:00Z' },
    { id: 'contact_69', type: 'person', firstName: 'Keith', lastName: 'Andersen', companyName: null, displayName: 'Keith Andersen', email: 'kandersen@email.com', phone: '(555) 345-6786', address: '321 Lombard Street, San Francisco, CA 94133', tags: ['real-estate'], createdAt: '2025-02-18T09:45:00Z' },
    { id: 'contact_70', type: 'person', firstName: 'Megan', lastName: 'Sullivan-Wright', companyName: null, displayName: 'Megan Sullivan-Wright', email: 'msullivanwright@protonmail.com', phone: '(555) 456-7897', address: '654 Nob Hill, San Francisco, CA 94108', tags: ['personal-injury', 'medical-malpractice'], createdAt: '2024-09-05T10:00:00Z' }
];

const PRACTICE_AREAS = [
    {
        id: 'pa_1',
        name: 'Personal Injury',
        stages: [
            { id: 'stage_1_1', name: 'Intake', order: 0 },
            { id: 'stage_1_2', name: 'Investigation', order: 1 },
            { id: 'stage_1_3', name: 'Demand', order: 2 },
            { id: 'stage_1_4', name: 'Litigation', order: 3 },
            { id: 'stage_1_5', name: 'Settlement/Trial', order: 4 }
        ]
    },
    {
        id: 'pa_2',
        name: 'Family Law',
        stages: [
            { id: 'stage_2_1', name: 'Consultation', order: 0 },
            { id: 'stage_2_2', name: 'Filing', order: 1 },
            { id: 'stage_2_3', name: 'Discovery', order: 2 },
            { id: 'stage_2_4', name: 'Mediation', order: 3 },
            { id: 'stage_2_5', name: 'Trial/Resolution', order: 4 }
        ]
    },
    {
        id: 'pa_3',
        name: 'Criminal Defense',
        stages: [
            { id: 'stage_3_1', name: 'Arraignment', order: 0 },
            { id: 'stage_3_2', name: 'Pre-Trial', order: 1 },
            { id: 'stage_3_3', name: 'Plea Negotiation', order: 2 },
            { id: 'stage_3_4', name: 'Trial', order: 3 },
            { id: 'stage_3_5', name: 'Sentencing/Appeal', order: 4 }
        ]
    },
    {
        id: 'pa_4',
        name: 'Real Estate',
        stages: [
            { id: 'stage_4_1', name: 'Due Diligence', order: 0 },
            { id: 'stage_4_2', name: 'Contract Review', order: 1 },
            { id: 'stage_4_3', name: 'Closing', order: 2 }
        ]
    },
    {
        id: 'pa_5',
        name: 'Corporate/Business',
        stages: [
            { id: 'stage_5_1', name: 'Engagement', order: 0 },
            { id: 'stage_5_2', name: 'Drafting', order: 1 },
            { id: 'stage_5_3', name: 'Review', order: 2 },
            { id: 'stage_5_4', name: 'Execution', order: 3 }
        ]
    },
    {
        id: 'pa_6',
        name: 'Employment Law',
        stages: [
            { id: 'stage_6_1', name: 'Intake', order: 0 },
            { id: 'stage_6_2', name: 'EEOC/Admin Filing', order: 1 },
            { id: 'stage_6_3', name: 'Negotiation', order: 2 },
            { id: 'stage_6_4', name: 'Litigation', order: 3 },
            { id: 'stage_6_5', name: 'Resolution', order: 4 }
        ]
    },
    {
        id: 'pa_7',
        name: 'Estate Planning',
        stages: [
            { id: 'stage_7_1', name: 'Initial Consultation', order: 0 },
            { id: 'stage_7_2', name: 'Document Preparation', order: 1 },
            { id: 'stage_7_3', name: 'Execution', order: 2 }
        ]
    },
    {
        id: 'pa_8',
        name: 'Immigration',
        stages: [
            { id: 'stage_8_1', name: 'Case Assessment', order: 0 },
            { id: 'stage_8_2', name: 'Application Preparation', order: 1 },
            { id: 'stage_8_3', name: 'Filing', order: 2 },
            { id: 'stage_8_4', name: 'Adjudication', order: 3 }
        ]
    },
    {
        id: 'pa_9',
        name: 'Intellectual Property',
        stages: [
            { id: 'stage_9_1', name: 'Search/Analysis', order: 0 },
            { id: 'stage_9_2', name: 'Application/Registration', order: 1 },
            { id: 'stage_9_3', name: 'Prosecution', order: 2 },
            { id: 'stage_9_4', name: 'Maintenance', order: 3 }
        ]
    },
    {
        id: 'pa_10',
        name: 'Bankruptcy',
        stages: [
            { id: 'stage_10_1', name: 'Pre-Filing Counseling', order: 0 },
            { id: 'stage_10_2', name: 'Petition Filing', order: 1 },
            { id: 'stage_10_3', name: 'Creditor Meeting', order: 2 },
            { id: 'stage_10_4', name: 'Plan Confirmation', order: 3 },
            { id: 'stage_10_5', name: 'Discharge', order: 4 }
        ]
    },
    {
        id: 'pa_11',
        name: 'Tax Law',
        stages: [
            { id: 'stage_11_1', name: 'Assessment', order: 0 },
            { id: 'stage_11_2', name: 'Planning/Filing', order: 1 },
            { id: 'stage_11_3', name: 'Audit Defense', order: 2 },
            { id: 'stage_11_4', name: 'Resolution', order: 3 }
        ]
    },
    {
        id: 'pa_12',
        name: 'Medical Malpractice',
        stages: [
            { id: 'stage_12_1', name: 'Case Review', order: 0 },
            { id: 'stage_12_2', name: 'Expert Consultation', order: 1 },
            { id: 'stage_12_3', name: 'Filing', order: 2 },
            { id: 'stage_12_4', name: 'Discovery', order: 3 },
            { id: 'stage_12_5', name: 'Trial/Settlement', order: 4 }
        ]
    },
    {
        id: 'pa_13',
        name: 'Environmental Law',
        stages: [
            { id: 'stage_13_1', name: 'Assessment', order: 0 },
            { id: 'stage_13_2', name: 'Regulatory Compliance', order: 1 },
            { id: 'stage_13_3', name: 'Enforcement/Litigation', order: 2 }
        ]
    }
];

const CUSTOM_FIELD_DEFINITIONS = [
    { id: 'cf_1', name: 'Court Case Number', type: 'text', required: false },
    { id: 'cf_2', name: 'Opposing Counsel', type: 'text', required: false },
    { id: 'cf_3', name: 'Statute of Limitations', type: 'date', required: false },
    { id: 'cf_4', name: 'Insurance Company', type: 'text', required: false },
    { id: 'cf_5', name: 'Policy Limit', type: 'currency', required: false },
    { id: 'cf_6', name: 'Jurisdiction', type: 'text', required: false },
    { id: 'cf_7', name: 'Judge Assigned', type: 'text', required: false },
    { id: 'cf_8', name: 'Next Court Date', type: 'date', required: false },
    { id: 'cf_9', name: 'Referral Source', type: 'text', required: false },
    { id: 'cf_10', name: 'Priority Level', type: 'text', required: false },
    { id: 'cf_11', name: 'Case Value Estimate', type: 'currency', required: false },
    { id: 'cf_12', name: 'Accident Date', type: 'date', required: false }
];

const MATTER_TEMPLATES = [
    {
        id: 'template_1',
        name: 'Personal Injury - Auto Accident',
        isDefault: true,
        description: 'Standard template for automobile accident personal injury cases',
        practiceAreaId: 'pa_1',
        billable: true,
        billingMethod: 'contingency',
        deductionOrder: 'fees_first',
        customFields: { cf_4: '', cf_5: '', cf_12: '' },
        documentFolders: [
            { name: 'Medical Records', category: 'Medical' },
            { name: 'Police Reports', category: 'Evidence' },
            { name: 'Insurance Correspondence', category: 'Correspondence' },
            { name: 'Photos/Videos', category: 'Evidence' }
        ]
    },
    {
        id: 'template_2',
        name: 'Family Law - Divorce',
        isDefault: false,
        description: 'Template for divorce and dissolution proceedings',
        practiceAreaId: 'pa_2',
        billable: true,
        billingMethod: 'hourly',
        deductionOrder: null,
        customFields: { cf_1: '', cf_6: '', cf_7: '' },
        documentFolders: [
            { name: 'Financial Disclosures', category: 'Financial' },
            { name: 'Custody Documents', category: 'Custody' },
            { name: 'Court Filings', category: 'Court' }
        ]
    },
    {
        id: 'template_3',
        name: 'Criminal Defense - Misdemeanor',
        isDefault: false,
        description: 'Template for misdemeanor criminal defense cases',
        practiceAreaId: 'pa_3',
        billable: true,
        billingMethod: 'flat_rate',
        deductionOrder: null,
        customFields: { cf_1: '', cf_7: '', cf_8: '' },
        documentFolders: [
            { name: 'Police Reports', category: 'Evidence' },
            { name: 'Court Documents', category: 'Court' },
            { name: 'Witness Statements', category: 'Evidence' }
        ]
    },
    {
        id: 'template_4',
        name: 'Corporate - General Business',
        isDefault: false,
        description: 'Template for general corporate and business matters',
        practiceAreaId: 'pa_5',
        billable: true,
        billingMethod: 'hourly',
        deductionOrder: null,
        customFields: { cf_6: '' },
        documentFolders: [
            { name: 'Contracts', category: 'Contracts' },
            { name: 'Corporate Documents', category: 'Corporate' },
            { name: 'Correspondence', category: 'Correspondence' }
        ]
    },
    {
        id: 'template_5',
        name: 'Real Estate - Residential Transaction',
        isDefault: false,
        description: 'Template for residential real estate purchase and sale transactions',
        practiceAreaId: 'pa_4',
        billable: true,
        billingMethod: 'flat_rate',
        deductionOrder: null,
        customFields: { cf_6: '' },
        documentFolders: [
            { name: 'Title Documents', category: 'Title' },
            { name: 'Inspection Reports', category: 'Inspection' },
            { name: 'Closing Documents', category: 'Closing' }
        ]
    },
    {
        id: 'template_6',
        name: 'Estate Planning - Comprehensive',
        isDefault: false,
        description: 'Template for comprehensive estate planning including trusts and wills',
        practiceAreaId: 'pa_7',
        billable: true,
        billingMethod: 'flat_rate',
        deductionOrder: null,
        customFields: {},
        documentFolders: [
            { name: 'Wills', category: 'Estate' },
            { name: 'Trust Documents', category: 'Estate' },
            { name: 'Powers of Attorney', category: 'Estate' },
            { name: 'Asset Inventory', category: 'Financial' }
        ]
    },
    {
        id: 'template_7',
        name: 'Personal Injury - Slip and Fall',
        isDefault: false,
        description: 'Template for premises liability and slip-and-fall injury cases',
        practiceAreaId: 'pa_1',
        billable: true,
        billingMethod: 'contingency',
        deductionOrder: 'fees_first',
        customFields: { cf_4: '', cf_5: '', cf_12: '' },
        documentFolders: [
            { name: 'Incident Reports', category: 'Evidence' },
            { name: 'Medical Records', category: 'Medical' },
            { name: 'Surveillance Footage', category: 'Evidence' },
            { name: 'Insurance Correspondence', category: 'Correspondence' }
        ]
    }
];

const NUMBERING_SCHEME = {
    format: 'auto',
    template: '[number]-[client]',
    components: ['number', 'client'],
    separator: '-',
    startingNumber: 1,
    nextNumber: 121,
    updateExisting: true,
    yearDigits: 4,
    numberPadding: 5
};

const MATTERS = [
    // === PERSONAL INJURY MATTERS (25+) ===
    {
        id: 'matter_1', number: '00001', displayNumber: '00001-Patterson', description: 'Patterson v. Metro Transit Authority - Bus accident resulting in back injury', status: 'open', billingMethod: 'contingency', clientId: 'contact_1', responsibleAttorneyId: 'user_2', originatingAttorneyId: 'user_1', responsibleStaffId: 'user_7', clientReferenceNumber: 'PI-2024-0234', location: 'San Francisco County Superior Court', practiceAreaId: 'pa_1', stageId: 'stage_1_3', openDate: '2024-03-20', pendingDate: null, closedDate: null, createdDate: '2024-03-18T14:30:00Z', templateId: 'template_1',
        permissions: { type: 'everyone', userIds: [], groupIds: [] }, blockedUsers: [],
        relationships: [{ contactId: 'contact_45', relationship: 'Spouse', billRecipient: false }],
        customFields: { cf_1: 'SF-2024-CV-08821', cf_2: 'Robert Hayes, Hayes & Associates', cf_3: '2026-03-20', cf_4: 'State Farm Insurance', cf_5: '250000', cf_12: '2024-03-15' },
        billing: { billable: true, method: 'contingency', currency: 'USD', rates: [], budget: 50000, budgetUsed: 23450, trustBalance: 5000, minimumTrust: 2000, contingencyFee: { userId: 'user_2', percentage: 33.33 }, flatRate: null },
        personalInjury: { deductionOrder: 'fees_first' },
        notifications: [{ userId: 'user_1', types: ['matter_updates', 'budget_threshold'] }],
        documentFolders: [{ id: 'folder_1_1', name: 'Medical Records', category: 'Medical' }, { id: 'folder_1_2', name: 'Police Reports', category: 'Evidence' }, { id: 'folder_1_3', name: 'Insurance Correspondence', category: 'Correspondence' }],
        reports: { useFirmSettings: true, originatingPct: 50, responsiblePct: 50 }, deleted: false, deletedAt: null
    },
    {
        id: 'matter_2', number: '00002', displayNumber: '00002-Johnson', description: 'Johnson v. Whole Foods Market - Slip and fall on wet floor causing hip fracture', status: 'open', billingMethod: 'contingency', clientId: 'contact_5', responsibleAttorneyId: 'user_2', originatingAttorneyId: 'user_2', responsibleStaffId: 'user_7', clientReferenceNumber: 'PI-2024-0312', location: 'Alameda County Superior Court', practiceAreaId: 'pa_1', stageId: 'stage_1_2', openDate: '2024-05-15', pendingDate: null, closedDate: null, createdDate: '2024-05-14T09:00:00Z', templateId: 'template_7',
        permissions: { type: 'everyone', userIds: [], groupIds: [] }, blockedUsers: [],
        relationships: [],
        customFields: { cf_1: 'AC-2024-CV-12445', cf_2: 'Lisa Morgan, Morgan Law', cf_3: '2026-05-12', cf_4: 'Hartford Insurance', cf_5: '500000', cf_12: '2024-05-12' },
        billing: { billable: true, method: 'contingency', currency: 'USD', rates: [], budget: 30000, budgetUsed: 8750, trustBalance: 0, minimumTrust: 0, contingencyFee: { userId: 'user_2', percentage: 33.33 }, flatRate: null },
        personalInjury: { deductionOrder: 'fees_first' },
        notifications: [], documentFolders: [{ id: 'folder_2_1', name: 'Incident Reports', category: 'Evidence' }, { id: 'folder_2_2', name: 'Medical Records', category: 'Medical' }],
        reports: { useFirmSettings: true, originatingPct: 100, responsiblePct: 0 }, deleted: false, deletedAt: null
    },
    {
        id: 'matter_3', number: '00003', displayNumber: '00003-Russo', description: 'Russo v. Lyft Inc. - Rideshare accident on Highway 101, multiple fractures', status: 'closed', billingMethod: 'contingency', clientId: 'contact_15', responsibleAttorneyId: 'user_2', originatingAttorneyId: 'user_1', responsibleStaffId: 'user_9', clientReferenceNumber: 'PI-2024-0198', location: 'San Mateo County Superior Court', practiceAreaId: 'pa_1', stageId: 'stage_1_5', openDate: '2024-06-01', pendingDate: '2025-04-10', closedDate: '2025-06-15', createdDate: '2024-05-30T11:20:00Z', templateId: 'template_1',
        permissions: { type: 'everyone', userIds: [], groupIds: [] }, blockedUsers: [],
        relationships: [{ contactId: 'contact_30', relationship: 'Insurance Adjuster', billRecipient: false }],
        customFields: { cf_1: 'SM-2024-CV-05567', cf_2: 'Daniel Park, Park & Reed LLP', cf_3: '2026-06-01', cf_4: 'ABC Insurance Co.', cf_5: '300000', cf_12: '2024-05-28' },
        billing: { billable: true, method: 'contingency', currency: 'USD', rates: [], budget: 40000, budgetUsed: 38200, trustBalance: 0, minimumTrust: 0, contingencyFee: { userId: 'user_2', percentage: 33.33 }, flatRate: null },
        personalInjury: { deductionOrder: 'fees_first' },
        notifications: [], documentFolders: [{ id: 'folder_3_1', name: 'Medical Records', category: 'Medical' }, { id: 'folder_3_2', name: 'Settlement Documents', category: 'Settlement' }],
        reports: { useFirmSettings: false, originatingPct: 40, responsiblePct: 60 }, deleted: false, deletedAt: null
    },
    {
        id: 'matter_4', number: '00004', displayNumber: '00004-Washington', description: 'Washington v. Pacific Steel Works - Workplace crush injury to left hand', status: 'open', billingMethod: 'contingency', clientId: 'contact_12', responsibleAttorneyId: 'user_8', originatingAttorneyId: 'user_2', responsibleStaffId: 'user_7', clientReferenceNumber: 'PI-2024-0401', location: 'San Francisco County Superior Court', practiceAreaId: 'pa_1', stageId: 'stage_1_4', openDate: '2024-04-20', pendingDate: null, closedDate: null, createdDate: '2024-04-19T10:15:00Z', templateId: 'template_1',
        permissions: { type: 'everyone', userIds: [], groupIds: [] }, blockedUsers: [],
        relationships: [{ contactId: 'contact_42', relationship: 'Insurance Adjuster', billRecipient: false }],
        customFields: { cf_1: 'SF-2024-CV-11023', cf_2: 'James Thornton, Thornton & Associates', cf_3: '2026-04-18', cf_4: 'CalComp Workers Compensation', cf_5: '150000', cf_12: '2024-04-18' },
        billing: { billable: true, method: 'contingency', currency: 'USD', rates: [], budget: 35000, budgetUsed: 27800, trustBalance: 0, minimumTrust: 0, contingencyFee: { userId: 'user_8', percentage: 40 }, flatRate: null },
        personalInjury: { deductionOrder: 'expenses_first' },
        notifications: [{ userId: 'user_2', types: ['matter_updates'] }], documentFolders: [{ id: 'folder_4_1', name: 'Medical Records', category: 'Medical' }, { id: 'folder_4_2', name: 'OSHA Reports', category: 'Evidence' }],
        reports: { useFirmSettings: true, originatingPct: 50, responsiblePct: 50 }, deleted: false, deletedAt: null
    },
    {
        id: 'matter_5', number: '00005', displayNumber: '00005-Doyle', description: 'Doyle v. Summit Construction - Fall from scaffolding at construction site', status: 'open', billingMethod: 'contingency', clientId: 'contact_26', responsibleAttorneyId: 'user_2', originatingAttorneyId: 'user_8', responsibleStaffId: 'user_9', clientReferenceNumber: 'PI-2024-0556', location: 'San Mateo County Superior Court', practiceAreaId: 'pa_1', stageId: 'stage_1_2', openDate: '2024-10-28', pendingDate: null, closedDate: null, createdDate: '2024-10-27T08:45:00Z', templateId: 'template_1',
        permissions: { type: 'everyone', userIds: [], groupIds: [] }, blockedUsers: [],
        relationships: [],
        customFields: { cf_1: '', cf_2: '', cf_3: '2026-10-25', cf_4: 'Travelers Insurance', cf_5: '1000000', cf_12: '2024-10-25' },
        billing: { billable: true, method: 'contingency', currency: 'USD', rates: [], budget: 75000, budgetUsed: 12300, trustBalance: 0, minimumTrust: 0, contingencyFee: { userId: 'user_2', percentage: 33.33 }, flatRate: null },
        personalInjury: { deductionOrder: 'fees_first' },
        notifications: [], documentFolders: [{ id: 'folder_5_1', name: 'Medical Records', category: 'Medical' }, { id: 'folder_5_2', name: 'OSHA Reports', category: 'Evidence' }, { id: 'folder_5_3', name: 'Photos/Videos', category: 'Evidence' }],
        reports: { useFirmSettings: true, originatingPct: 50, responsiblePct: 50 }, deleted: false, deletedAt: null
    },
    {
        id: 'matter_6', number: '00006', displayNumber: '00006-McCarthy', description: 'McCarthy v. City of San Francisco - Pedestrian struck in crosswalk by city vehicle', status: 'open', billingMethod: 'contingency', clientId: 'contact_36', responsibleAttorneyId: 'user_8', originatingAttorneyId: 'user_1', responsibleStaffId: 'user_7', clientReferenceNumber: 'PI-2024-0489', location: 'San Francisco County Superior Court', practiceAreaId: 'pa_1', stageId: 'stage_1_3', openDate: '2024-09-30', pendingDate: null, closedDate: null, createdDate: '2024-09-29T13:00:00Z', templateId: 'template_1',
        permissions: { type: 'everyone', userIds: [], groupIds: [] }, blockedUsers: [],
        relationships: [],
        customFields: { cf_1: 'SF-2024-CV-18902', cf_2: 'City Attorney Office', cf_3: '2025-03-27', cf_4: 'CSAC EIA (self-insured)', cf_5: '0', cf_12: '2024-09-27' },
        billing: { billable: true, method: 'contingency', currency: 'USD', rates: [], budget: 60000, budgetUsed: 18500, trustBalance: 0, minimumTrust: 0, contingencyFee: { userId: 'user_8', percentage: 33.33 }, flatRate: null },
        personalInjury: { deductionOrder: 'fees_first' },
        notifications: [], documentFolders: [{ id: 'folder_6_1', name: 'Medical Records', category: 'Medical' }, { id: 'folder_6_2', name: 'Accident Report', category: 'Evidence' }],
        reports: { useFirmSettings: true, originatingPct: 50, responsiblePct: 50 }, deleted: false, deletedAt: null
    },
    {
        id: 'matter_7', number: '00007', displayNumber: '00007-Okafor', description: 'Okafor v. HomeComfort Appliances - Defective space heater causing severe burns', status: 'open', billingMethod: 'contingency', clientId: 'contact_40', responsibleAttorneyId: 'user_2', originatingAttorneyId: 'user_2', responsibleStaffId: 'user_7', clientReferenceNumber: 'PI-2024-0422', location: 'Northern District of California', practiceAreaId: 'pa_1', stageId: 'stage_1_4', openDate: '2024-07-22', pendingDate: null, closedDate: null, createdDate: '2024-07-21T15:30:00Z', templateId: 'template_1',
        permissions: { type: 'specific', userIds: ['user_1', 'user_2', 'user_7'], groupIds: ['group_1'] }, blockedUsers: ['user_14'],
        relationships: [{ contactId: 'contact_30', relationship: 'Insurance Adjuster', billRecipient: false }],
        customFields: { cf_1: 'NDCA-2024-CV-04521', cf_2: 'Wilson & Kraft LLP', cf_3: '2026-07-19', cf_4: 'Nationwide Insurance', cf_5: '500000', cf_12: '2024-07-19' },
        billing: { billable: true, method: 'contingency', currency: 'USD', rates: [], budget: 100000, budgetUsed: 45600, trustBalance: 0, minimumTrust: 0, contingencyFee: { userId: 'user_2', percentage: 40 }, flatRate: null },
        personalInjury: { deductionOrder: 'fees_first' },
        notifications: [{ userId: 'user_1', types: ['matter_updates', 'budget_threshold'] }], documentFolders: [{ id: 'folder_7_1', name: 'Medical Records', category: 'Medical' }, { id: 'folder_7_2', name: 'Product Analysis', category: 'Evidence' }],
        reports: { useFirmSettings: true, originatingPct: 100, responsiblePct: 0 }, deleted: false, deletedAt: null
    },
    {
        id: 'matter_8', number: '00008', displayNumber: '00008-Mills', description: 'Mills v. Rodriguez - Motorcycle collision at intersection, traumatic brain injury', status: 'open', billingMethod: 'contingency', clientId: 'contact_49', responsibleAttorneyId: 'user_8', originatingAttorneyId: 'user_2', responsibleStaffId: 'user_9', clientReferenceNumber: 'PI-2024-0501', location: 'San Francisco County Superior Court', practiceAreaId: 'pa_1', stageId: 'stage_1_2', openDate: '2024-09-15', pendingDate: null, closedDate: null, createdDate: '2024-09-14T10:00:00Z', templateId: 'template_1',
        permissions: { type: 'everyone', userIds: [], groupIds: [] }, blockedUsers: [],
        relationships: [],
        customFields: { cf_1: '', cf_2: '', cf_3: '2026-09-11', cf_4: 'Progressive Insurance', cf_5: '100000', cf_12: '2024-09-11' },
        billing: { billable: true, method: 'contingency', currency: 'USD', rates: [], budget: 45000, budgetUsed: 9200, trustBalance: 0, minimumTrust: 0, contingencyFee: { userId: 'user_8', percentage: 33.33 }, flatRate: null },
        personalInjury: { deductionOrder: 'fees_first' },
        notifications: [], documentFolders: [{ id: 'folder_8_1', name: 'Medical Records', category: 'Medical' }, { id: 'folder_8_2', name: 'Police Report', category: 'Evidence' }],
        reports: { useFirmSettings: true, originatingPct: 50, responsiblePct: 50 }, deleted: false, deletedAt: null
    },
    {
        id: 'matter_9', number: '00009', displayNumber: '00009-Ababio', description: 'Ababio v. SafeMart Grocery - Falling merchandise causing shoulder injury', status: 'pending', billingMethod: 'contingency', clientId: 'contact_47', responsibleAttorneyId: 'user_2', originatingAttorneyId: 'user_1', responsibleStaffId: 'user_7', clientReferenceNumber: 'PI-2024-0278', location: 'Contra Costa County Superior Court', practiceAreaId: 'pa_1', stageId: 'stage_1_5', openDate: '2024-04-30', pendingDate: '2025-09-01', closedDate: null, createdDate: '2024-04-29T11:45:00Z', templateId: 'template_7',
        permissions: { type: 'everyone', userIds: [], groupIds: [] }, blockedUsers: [],
        relationships: [],
        customFields: { cf_1: 'CC-2024-CV-09012', cf_2: 'Baker & Wells', cf_3: '2026-04-28', cf_4: 'Liberty Mutual', cf_5: '200000', cf_12: '2024-04-28' },
        billing: { billable: true, method: 'contingency', currency: 'USD', rates: [], budget: 25000, budgetUsed: 22100, trustBalance: 0, minimumTrust: 0, contingencyFee: { userId: 'user_2', percentage: 33.33 }, flatRate: null },
        personalInjury: { deductionOrder: 'fees_first' },
        notifications: [], documentFolders: [{ id: 'folder_9_1', name: 'Medical Records', category: 'Medical' }],
        reports: { useFirmSettings: true, originatingPct: 50, responsiblePct: 50 }, deleted: false, deletedAt: null
    },
    {
        id: 'matter_10', number: '00010', displayNumber: '00010-Dimitriou', description: 'Dimitriou v. Lawson - Severe dog bite requiring reconstructive surgery', status: 'open', billingMethod: 'contingency', clientId: 'contact_53', responsibleAttorneyId: 'user_5', originatingAttorneyId: 'user_2', responsibleStaffId: 'user_7', clientReferenceNumber: 'PI-2024-0601', location: 'San Francisco County Superior Court', practiceAreaId: 'pa_1', stageId: 'stage_1_1', openDate: '2024-11-25', pendingDate: null, closedDate: null, createdDate: '2024-11-24T09:30:00Z', templateId: 'template_1',
        permissions: { type: 'everyone', userIds: [], groupIds: [] }, blockedUsers: [],
        relationships: [],
        customFields: { cf_1: '', cf_2: '', cf_3: '2026-11-22', cf_4: 'Allstate Insurance', cf_5: '300000', cf_12: '2024-11-22' },
        billing: { billable: true, method: 'contingency', currency: 'USD', rates: [], budget: 0, budgetUsed: 3200, trustBalance: 0, minimumTrust: 0, contingencyFee: { userId: 'user_5', percentage: 33.33 }, flatRate: null },
        personalInjury: { deductionOrder: 'fees_first' },
        notifications: [], documentFolders: [{ id: 'folder_10_1', name: 'Medical Records', category: 'Medical' }, { id: 'folder_10_2', name: 'Animal Control Report', category: 'Evidence' }],
        reports: { useFirmSettings: true, originatingPct: 50, responsiblePct: 50 }, deleted: false, deletedAt: null
    },
    {
        id: 'matter_11', number: '00011', displayNumber: '00011-Whitfield', description: 'Whitfield v. Bay Area Rapid Transit - Escalator malfunction causing knee injury', status: 'open', billingMethod: 'contingency', clientId: 'contact_61', responsibleAttorneyId: 'user_2', originatingAttorneyId: 'user_8', responsibleStaffId: 'user_7', clientReferenceNumber: 'PI-2024-0645', location: 'San Francisco County Superior Court', practiceAreaId: 'pa_1', stageId: 'stage_1_1', openDate: '2024-12-12', pendingDate: null, closedDate: null, createdDate: '2024-12-11T14:00:00Z', templateId: 'template_1',
        permissions: { type: 'everyone', userIds: [], groupIds: [] }, blockedUsers: [],
        relationships: [],
        customFields: { cf_3: '2026-12-10', cf_4: 'BART Self-Insured', cf_5: '0', cf_12: '2024-12-10' },
        billing: { billable: true, method: 'contingency', currency: 'USD', rates: [], budget: 0, budgetUsed: 1800, trustBalance: 0, minimumTrust: 0, contingencyFee: { userId: 'user_2', percentage: 33.33 }, flatRate: null },
        personalInjury: { deductionOrder: 'fees_first' },
        notifications: [], documentFolders: [{ id: 'folder_11_1', name: 'Medical Records', category: 'Medical' }],
        reports: { useFirmSettings: true, originatingPct: 50, responsiblePct: 50 }, deleted: false, deletedAt: null
    },
    {
        id: 'matter_12', number: '00012', displayNumber: '00012-Brennan', description: 'Brennan v. Oceanview Hotel - Slip on unmarked wet lobby floor, broken wrist and concussion', status: 'open', billingMethod: 'contingency', clientId: 'contact_65', responsibleAttorneyId: 'user_5', originatingAttorneyId: 'user_1', responsibleStaffId: 'user_9', clientReferenceNumber: 'PI-2025-0012', location: 'San Francisco County Superior Court', practiceAreaId: 'pa_1', stageId: 'stage_1_1', openDate: '2025-02-05', pendingDate: null, closedDate: null, createdDate: '2025-02-04T10:30:00Z', templateId: 'template_7',
        permissions: { type: 'everyone', userIds: [], groupIds: [] }, blockedUsers: [],
        relationships: [],
        customFields: { cf_3: '2027-02-01', cf_4: 'Zurich Insurance', cf_5: '500000', cf_12: '2025-02-01' },
        billing: { billable: true, method: 'contingency', currency: 'USD', rates: [], budget: 0, budgetUsed: 750, trustBalance: 0, minimumTrust: 0, contingencyFee: { userId: 'user_5', percentage: 33.33 }, flatRate: null },
        personalInjury: { deductionOrder: 'fees_first' },
        notifications: [], documentFolders: [{ id: 'folder_12_1', name: 'Medical Records', category: 'Medical' }, { id: 'folder_12_2', name: 'Incident Report', category: 'Evidence' }],
        reports: { useFirmSettings: true, originatingPct: 50, responsiblePct: 50 }, deleted: false, deletedAt: null
    },
    {
        id: 'matter_13', number: '00013', displayNumber: '00013-Simmons', description: 'Simmons v. Uber Technologies - Rear-end collision by Uber driver, cervical spine injury', status: 'open', billingMethod: 'contingency', clientId: 'contact_32', responsibleAttorneyId: 'user_2', originatingAttorneyId: 'user_2', responsibleStaffId: 'user_7', clientReferenceNumber: 'PI-2024-0578', location: 'San Francisco County Superior Court', practiceAreaId: 'pa_1', stageId: 'stage_1_3', openDate: '2024-11-18', pendingDate: null, closedDate: null, createdDate: '2024-11-17T16:00:00Z', templateId: 'template_1',
        permissions: { type: 'everyone', userIds: [], groupIds: [] }, blockedUsers: [],
        relationships: [],
        customFields: { cf_1: 'SF-2024-CV-22109', cf_2: 'Chen & Associates', cf_3: '2026-11-14', cf_4: 'James River Insurance', cf_5: '1000000', cf_12: '2024-11-14' },
        billing: { billable: true, method: 'contingency', currency: 'USD', rates: [], budget: 55000, budgetUsed: 14300, trustBalance: 0, minimumTrust: 0, contingencyFee: { userId: 'user_2', percentage: 33.33 }, flatRate: null },
        personalInjury: { deductionOrder: 'fees_first' },
        notifications: [], documentFolders: [{ id: 'folder_13_1', name: 'Medical Records', category: 'Medical' }],
        reports: { useFirmSettings: true, originatingPct: 100, responsiblePct: 0 }, deleted: false, deletedAt: null
    },
    {
        id: 'matter_14', number: '00014', displayNumber: '00014-Sullivan-Wright', description: 'Sullivan-Wright v. Kaiser Permanente - Surgical error during appendectomy causing internal bleeding', status: 'open', billingMethod: 'contingency', clientId: 'contact_70', responsibleAttorneyId: 'user_8', originatingAttorneyId: 'user_1', responsibleStaffId: 'user_7', clientReferenceNumber: 'MM-2024-0089', location: 'San Francisco County Superior Court', practiceAreaId: 'pa_12', stageId: 'stage_12_3', openDate: '2024-09-08', pendingDate: null, closedDate: null, createdDate: '2024-09-07T11:15:00Z', templateId: 'template_1',
        permissions: { type: 'specific', userIds: ['user_1', 'user_8', 'user_7', 'user_5'], groupIds: [] }, blockedUsers: [],
        relationships: [],
        customFields: { cf_1: 'SF-2024-CV-17890', cf_2: 'Kaiser Legal Department', cf_3: '2025-09-05', cf_4: 'Kaiser Self-Insured', cf_5: '0', cf_12: '2024-09-05' },
        billing: { billable: true, method: 'contingency', currency: 'USD', rates: [], budget: 150000, budgetUsed: 67800, trustBalance: 0, minimumTrust: 0, contingencyFee: { userId: 'user_8', percentage: 40 }, flatRate: null },
        personalInjury: { deductionOrder: 'fees_first' },
        notifications: [{ userId: 'user_1', types: ['matter_updates'] }], documentFolders: [{ id: 'folder_14_1', name: 'Medical Records', category: 'Medical' }, { id: 'folder_14_2', name: 'Expert Reports', category: 'Expert' }],
        reports: { useFirmSettings: false, originatingPct: 30, responsiblePct: 70 }, deleted: false, deletedAt: null
    },
    {
        id: 'matter_15', number: '00015', displayNumber: '00015-Fitzgerald', description: 'Fitzgerald v. St. Mary Medical Center - Misdiagnosis of breast cancer leading to delayed treatment', status: 'pending', billingMethod: 'contingency', clientId: 'contact_22', responsibleAttorneyId: 'user_8', originatingAttorneyId: 'user_2', responsibleStaffId: 'user_9', clientReferenceNumber: 'MM-2024-0112', location: 'San Mateo County Superior Court', practiceAreaId: 'pa_12', stageId: 'stage_12_5', openDate: '2024-09-20', pendingDate: '2025-11-01', closedDate: null, createdDate: '2024-09-19T14:30:00Z', templateId: 'template_1',
        permissions: { type: 'everyone', userIds: [], groupIds: [] }, blockedUsers: [],
        relationships: [],
        customFields: { cf_1: 'SM-2024-CV-08934', cf_2: 'Medical Defense Associates', cf_3: '2025-09-18', cf_4: 'The Doctors Company', cf_5: '2000000', cf_12: '2023-09-18' },
        billing: { billable: true, method: 'contingency', currency: 'USD', rates: [], budget: 200000, budgetUsed: 156000, trustBalance: 0, minimumTrust: 0, contingencyFee: { userId: 'user_8', percentage: 40 }, flatRate: null },
        personalInjury: { deductionOrder: 'fees_first' },
        notifications: [], documentFolders: [{ id: 'folder_15_1', name: 'Medical Records', category: 'Medical' }, { id: 'folder_15_2', name: 'Expert Reports', category: 'Expert' }],
        reports: { useFirmSettings: true, originatingPct: 50, responsiblePct: 50 }, deleted: false, deletedAt: null
    },
    {
        id: 'matter_16', number: '00016', displayNumber: '00016-Patterson-WC', description: 'Patterson Workers Comp Claim - Repetitive stress injury from warehouse work', status: 'open', billingMethod: 'contingency', clientId: 'contact_1', responsibleAttorneyId: 'user_5', originatingAttorneyId: 'user_2', responsibleStaffId: 'user_7', clientReferenceNumber: 'WC-2025-0034', location: 'California Workers Compensation Appeals Board', practiceAreaId: 'pa_1', stageId: 'stage_1_2', openDate: '2025-01-15', pendingDate: null, closedDate: null, createdDate: '2025-01-14T09:00:00Z', templateId: 'template_1',
        permissions: { type: 'everyone', userIds: [], groupIds: [] }, blockedUsers: [],
        relationships: [{ contactId: 'contact_45', relationship: 'Spouse', billRecipient: false }],
        customFields: { cf_4: 'CalComp Workers Compensation', cf_5: '75000', cf_12: '2024-12-20' },
        billing: { billable: true, method: 'contingency', currency: 'USD', rates: [], budget: 15000, budgetUsed: 4500, trustBalance: 0, minimumTrust: 0, contingencyFee: { userId: 'user_5', percentage: 15 }, flatRate: null },
        personalInjury: { deductionOrder: 'fees_first' },
        notifications: [], documentFolders: [{ id: 'folder_16_1', name: 'Medical Records', category: 'Medical' }],
        reports: { useFirmSettings: true, originatingPct: 50, responsiblePct: 50 }, deleted: false, deletedAt: null
    },
    {
        id: 'matter_17', number: '00017', displayNumber: '00017-Gonzalez-PI', description: 'Gonzalez v. DoorDash - Delivery vehicle struck client while jogging', status: 'closed', billingMethod: 'contingency', clientId: 'contact_2', responsibleAttorneyId: 'user_2', originatingAttorneyId: 'user_1', responsibleStaffId: 'user_7', clientReferenceNumber: 'PI-2024-0145', location: 'Santa Clara County Superior Court', practiceAreaId: 'pa_1', stageId: 'stage_1_5', openDate: '2024-01-15', pendingDate: '2024-10-01', closedDate: '2024-12-20', createdDate: '2024-01-14T11:00:00Z', templateId: 'template_1',
        permissions: { type: 'everyone', userIds: [], groupIds: [] }, blockedUsers: [],
        relationships: [],
        customFields: { cf_1: 'SC-2024-CV-02345', cf_2: 'Roberts & Klein', cf_3: '2026-01-10', cf_4: 'GEICO', cf_5: '250000', cf_12: '2024-01-10' },
        billing: { billable: true, method: 'contingency', currency: 'USD', rates: [], budget: 30000, budgetUsed: 28900, trustBalance: 0, minimumTrust: 0, contingencyFee: { userId: 'user_2', percentage: 33.33 }, flatRate: null },
        personalInjury: { deductionOrder: 'fees_first' },
        notifications: [], documentFolders: [{ id: 'folder_17_1', name: 'Medical Records', category: 'Medical' }, { id: 'folder_17_2', name: 'Settlement', category: 'Settlement' }],
        reports: { useFirmSettings: true, originatingPct: 50, responsiblePct: 50 }, deleted: false, deletedAt: null
    },
    {
        id: 'matter_18', number: '00018', displayNumber: '00018-ChenRamirez-PI', description: 'Chen-Ramirez v. Amazon Delivery - Package delivery truck backed into client in driveway', status: 'open', billingMethod: 'contingency', clientId: 'contact_3', responsibleAttorneyId: 'user_5', originatingAttorneyId: 'user_8', responsibleStaffId: 'user_9', clientReferenceNumber: 'PI-2025-0067', location: 'Alameda County Superior Court', practiceAreaId: 'pa_1', stageId: 'stage_1_1', openDate: '2025-02-22', pendingDate: null, closedDate: null, createdDate: '2025-02-21T15:45:00Z', templateId: 'template_1',
        permissions: { type: 'everyone', userIds: [], groupIds: [] }, blockedUsers: [],
        relationships: [],
        customFields: { cf_3: '2027-02-18', cf_4: 'Amazon Corporate Insurance', cf_5: '500000', cf_12: '2025-02-18' },
        billing: { billable: true, method: 'contingency', currency: 'USD', rates: [], budget: 0, budgetUsed: 450, trustBalance: 0, minimumTrust: 0, contingencyFee: { userId: 'user_5', percentage: 33.33 }, flatRate: null },
        personalInjury: { deductionOrder: 'fees_first' },
        notifications: [], documentFolders: [{ id: 'folder_18_1', name: 'Medical Records', category: 'Medical' }],
        reports: { useFirmSettings: true, originatingPct: 50, responsiblePct: 50 }, deleted: false, deletedAt: null
    },
    {
        id: 'matter_19', number: '00019', displayNumber: '00019-Simmons-2', description: 'Simmons v. PetSmart - Dog grooming burn injury from overheated dryer', status: 'pending', billingMethod: 'contingency', clientId: 'contact_32', responsibleAttorneyId: 'user_2', originatingAttorneyId: 'user_5', responsibleStaffId: 'user_7', clientReferenceNumber: 'PI-2024-0390', location: 'San Francisco County Superior Court', practiceAreaId: 'pa_1', stageId: 'stage_1_5', openDate: '2024-08-10', pendingDate: '2025-08-20', closedDate: null, createdDate: '2024-08-09T10:00:00Z', templateId: 'template_1',
        permissions: { type: 'everyone', userIds: [], groupIds: [] }, blockedUsers: [],
        relationships: [],
        customFields: { cf_1: 'SF-2024-CV-15678', cf_2: 'Anderson & Price', cf_3: '2026-08-07', cf_4: 'CNA Insurance', cf_5: '100000', cf_12: '2024-08-07' },
        billing: { billable: true, method: 'contingency', currency: 'USD', rates: [], budget: 20000, budgetUsed: 19500, trustBalance: 0, minimumTrust: 0, contingencyFee: { userId: 'user_2', percentage: 33.33 }, flatRate: null },
        personalInjury: { deductionOrder: 'fees_first' },
        notifications: [], documentFolders: [{ id: 'folder_19_1', name: 'Medical Records', category: 'Medical' }],
        reports: { useFirmSettings: true, originatingPct: 50, responsiblePct: 50 }, deleted: false, deletedAt: null
    },
    {
        id: 'matter_20', number: '00020', displayNumber: '00020-Johnson-2', description: 'Johnson v. Target Corp - Chemical burn from defective cleaning product', status: 'open', billingMethod: 'contingency', clientId: 'contact_5', responsibleAttorneyId: 'user_8', originatingAttorneyId: 'user_1', responsibleStaffId: 'user_9', clientReferenceNumber: 'PI-2025-0023', location: 'Contra Costa County Superior Court', practiceAreaId: 'pa_1', stageId: 'stage_1_2', openDate: '2025-01-20', pendingDate: null, closedDate: null, createdDate: '2025-01-19T08:30:00Z', templateId: 'template_1',
        permissions: { type: 'everyone', userIds: [], groupIds: [] }, blockedUsers: [],
        relationships: [],
        customFields: { cf_3: '2027-01-15', cf_4: 'Target Risk Management', cf_5: '250000', cf_12: '2025-01-15' },
        billing: { billable: true, method: 'contingency', currency: 'USD', rates: [], budget: 0, budgetUsed: 2100, trustBalance: 0, minimumTrust: 0, contingencyFee: { userId: 'user_8', percentage: 33.33 }, flatRate: null },
        personalInjury: { deductionOrder: 'fees_first' },
        notifications: [], documentFolders: [{ id: 'folder_20_1', name: 'Medical Records', category: 'Medical' }],
        reports: { useFirmSettings: true, originatingPct: 50, responsiblePct: 50 }, deleted: false, deletedAt: null
    },
    // PI matters 21-27
    {
        id: 'matter_21', number: '00021', displayNumber: '00021-Okafor-2', description: 'Okafor v. SF Municipal Railway - Sudden stop on Muni bus causing neck whiplash', status: 'closed', billingMethod: 'contingency', clientId: 'contact_40', responsibleAttorneyId: 'user_2', originatingAttorneyId: 'user_2', responsibleStaffId: 'user_7', clientReferenceNumber: 'PI-2024-0088', location: 'San Francisco County Superior Court', practiceAreaId: 'pa_1', stageId: 'stage_1_5', openDate: '2024-02-01', pendingDate: '2024-08-15', closedDate: '2024-11-30', createdDate: '2024-01-31T09:00:00Z', templateId: 'template_1',
        permissions: { type: 'everyone', userIds: [], groupIds: [] }, blockedUsers: [],
        relationships: [], customFields: { cf_1: 'SF-2024-CV-01234', cf_2: 'City Attorney Office', cf_3: '2025-08-01', cf_4: 'SFMTA Self-Insured', cf_5: '0', cf_12: '2024-01-28' },
        billing: { billable: true, method: 'contingency', currency: 'USD', rates: [], budget: 20000, budgetUsed: 18900, trustBalance: 0, minimumTrust: 0, contingencyFee: { userId: 'user_2', percentage: 33.33 }, flatRate: null },
        personalInjury: { deductionOrder: 'fees_first' },
        notifications: [], documentFolders: [{ id: 'folder_21_1', name: 'Medical Records', category: 'Medical' }],
        reports: { useFirmSettings: true, originatingPct: 100, responsiblePct: 0 }, deleted: false, deletedAt: null
    },
    {
        id: 'matter_22', number: '00022', displayNumber: '00022-Doyle-2', description: 'Doyle v. Home Depot - Forklift accident in warehouse causing leg fracture', status: 'open', billingMethod: 'contingency', clientId: 'contact_26', responsibleAttorneyId: 'user_5', originatingAttorneyId: 'user_2', responsibleStaffId: 'user_7', clientReferenceNumber: 'PI-2025-0045', location: 'San Mateo County Superior Court', practiceAreaId: 'pa_1', stageId: 'stage_1_1', openDate: '2025-02-10', pendingDate: null, closedDate: null, createdDate: '2025-02-09T14:20:00Z', templateId: 'template_1',
        permissions: { type: 'everyone', userIds: [], groupIds: [] }, blockedUsers: [],
        relationships: [], customFields: { cf_3: '2027-02-05', cf_4: 'Home Depot Insurance', cf_5: '500000', cf_12: '2025-02-05' },
        billing: { billable: true, method: 'contingency', currency: 'USD', rates: [], budget: 0, budgetUsed: 600, trustBalance: 0, minimumTrust: 0, contingencyFee: { userId: 'user_5', percentage: 33.33 }, flatRate: null },
        personalInjury: { deductionOrder: 'fees_first' },
        notifications: [], documentFolders: [{ id: 'folder_22_1', name: 'Medical Records', category: 'Medical' }],
        reports: { useFirmSettings: true, originatingPct: 50, responsiblePct: 50 }, deleted: false, deletedAt: null
    },
    {
        id: 'matter_23', number: '00023', displayNumber: '00023-McCarthy-2', description: 'McCarthy v. Whole Foods - Allergic reaction from undisclosed allergen in deli food', status: 'open', billingMethod: 'contingency', clientId: 'contact_36', responsibleAttorneyId: 'user_2', originatingAttorneyId: 'user_5', responsibleStaffId: 'user_9', clientReferenceNumber: 'PI-2025-0078', location: 'San Francisco County Superior Court', practiceAreaId: 'pa_1', stageId: 'stage_1_1', openDate: '2025-02-28', pendingDate: null, closedDate: null, createdDate: '2025-02-27T11:00:00Z', templateId: 'template_1',
        permissions: { type: 'everyone', userIds: [], groupIds: [] }, blockedUsers: [],
        relationships: [], customFields: { cf_3: '2027-02-25', cf_12: '2025-02-25' },
        billing: { billable: true, method: 'contingency', currency: 'USD', rates: [], budget: 0, budgetUsed: 200, trustBalance: 0, minimumTrust: 0, contingencyFee: { userId: 'user_2', percentage: 33.33 }, flatRate: null },
        personalInjury: { deductionOrder: 'fees_first' },
        notifications: [], documentFolders: [{ id: 'folder_23_1', name: 'Medical Records', category: 'Medical' }],
        reports: { useFirmSettings: true, originatingPct: 50, responsiblePct: 50 }, deleted: false, deletedAt: null
    },
    {
        id: 'matter_24', number: '00024', displayNumber: '00024-Ababio-2', description: 'Ababio v. Pacific Gas & Electric - Electrical shock from exposed wiring in apartment', status: 'open', billingMethod: 'contingency', clientId: 'contact_47', responsibleAttorneyId: 'user_8', originatingAttorneyId: 'user_1', responsibleStaffId: 'user_7', clientReferenceNumber: 'PI-2024-0534', location: 'Alameda County Superior Court', practiceAreaId: 'pa_1', stageId: 'stage_1_3', openDate: '2024-10-15', pendingDate: null, closedDate: null, createdDate: '2024-10-14T09:15:00Z', templateId: 'template_1',
        permissions: { type: 'everyone', userIds: [], groupIds: [] }, blockedUsers: [],
        relationships: [], customFields: { cf_1: 'AC-2024-CV-19087', cf_2: 'PG&E Legal Dept', cf_3: '2025-10-12', cf_4: 'PG&E Self-Insured', cf_5: '0', cf_12: '2024-10-12' },
        billing: { billable: true, method: 'contingency', currency: 'USD', rates: [], budget: 80000, budgetUsed: 31200, trustBalance: 0, minimumTrust: 0, contingencyFee: { userId: 'user_8', percentage: 40 }, flatRate: null },
        personalInjury: { deductionOrder: 'expenses_first' },
        notifications: [], documentFolders: [{ id: 'folder_24_1', name: 'Medical Records', category: 'Medical' }, { id: 'folder_24_2', name: 'Utility Records', category: 'Evidence' }],
        reports: { useFirmSettings: true, originatingPct: 50, responsiblePct: 50 }, deleted: false, deletedAt: null
    },
    {
        id: 'matter_25', number: '00025', displayNumber: '00025-Whitfield-2', description: 'Whitfield v. Costco Wholesale - Shopping cart collision in parking lot causing ankle fracture', status: 'pending', billingMethod: 'contingency', clientId: 'contact_61', responsibleAttorneyId: 'user_5', originatingAttorneyId: 'user_2', responsibleStaffId: 'user_9', clientReferenceNumber: 'PI-2024-0367', location: 'San Francisco County Superior Court', practiceAreaId: 'pa_1', stageId: 'stage_1_5', openDate: '2024-07-10', pendingDate: '2025-07-15', closedDate: null, createdDate: '2024-07-09T13:45:00Z', templateId: 'template_7',
        permissions: { type: 'everyone', userIds: [], groupIds: [] }, blockedUsers: [],
        relationships: [], customFields: { cf_1: 'SF-2024-CV-13456', cf_2: 'Martinez & Stone', cf_3: '2026-07-08', cf_4: 'Costco Self-Insured', cf_5: '0', cf_12: '2024-07-08' },
        billing: { billable: true, method: 'contingency', currency: 'USD', rates: [], budget: 15000, budgetUsed: 14200, trustBalance: 0, minimumTrust: 0, contingencyFee: { userId: 'user_5', percentage: 33.33 }, flatRate: null },
        personalInjury: { deductionOrder: 'fees_first' },
        notifications: [], documentFolders: [{ id: 'folder_25_1', name: 'Medical Records', category: 'Medical' }],
        reports: { useFirmSettings: true, originatingPct: 50, responsiblePct: 50 }, deleted: false, deletedAt: null
    },
    {
        id: 'matter_26', number: '00026', displayNumber: '00026-Mills-2', description: 'Mills v. State of California - Highway guardrail failure causing additional crash injuries', status: 'open', billingMethod: 'contingency', clientId: 'contact_49', responsibleAttorneyId: 'user_2', originatingAttorneyId: 'user_8', responsibleStaffId: 'user_7', clientReferenceNumber: 'PI-2024-0612', location: 'Marin County Superior Court', practiceAreaId: 'pa_1', stageId: 'stage_1_2', openDate: '2024-12-01', pendingDate: null, closedDate: null, createdDate: '2024-11-30T10:30:00Z', templateId: 'template_1',
        permissions: { type: 'everyone', userIds: [], groupIds: [] }, blockedUsers: [],
        relationships: [], customFields: { cf_3: '2025-05-28', cf_4: 'CalTrans Self-Insured', cf_5: '0', cf_12: '2024-11-28' },
        billing: { billable: true, method: 'contingency', currency: 'USD', rates: [], budget: 0, budgetUsed: 5400, trustBalance: 0, minimumTrust: 0, contingencyFee: { userId: 'user_2', percentage: 33.33 }, flatRate: null },
        personalInjury: { deductionOrder: 'fees_first' },
        notifications: [], documentFolders: [{ id: 'folder_26_1', name: 'Medical Records', category: 'Medical' }],
        reports: { useFirmSettings: true, originatingPct: 50, responsiblePct: 50 }, deleted: false, deletedAt: null
    },
    {
        id: 'matter_27', number: '00027', displayNumber: '00027-Dimitriou-2', description: 'Dimitriou v. SF Unified School District - Child injured on playground due to defective equipment', status: 'open', billingMethod: 'contingency', clientId: 'contact_53', responsibleAttorneyId: 'user_8', originatingAttorneyId: 'user_2', responsibleStaffId: 'user_7', clientReferenceNumber: 'PI-2025-0089', location: 'San Francisco County Superior Court', practiceAreaId: 'pa_1', stageId: 'stage_1_1', openDate: '2025-03-01', pendingDate: null, closedDate: null, createdDate: '2025-02-28T16:00:00Z', templateId: 'template_1',
        permissions: { type: 'everyone', userIds: [], groupIds: [] }, blockedUsers: [],
        relationships: [], customFields: { cf_3: '2026-02-25', cf_12: '2025-02-25' },
        billing: { billable: true, method: 'contingency', currency: 'USD', rates: [], budget: 0, budgetUsed: 0, trustBalance: 0, minimumTrust: 0, contingencyFee: { userId: 'user_8', percentage: 33.33 }, flatRate: null },
        personalInjury: { deductionOrder: 'fees_first' },
        notifications: [], documentFolders: [{ id: 'folder_27_1', name: 'Medical Records', category: 'Medical' }],
        reports: { useFirmSettings: true, originatingPct: 50, responsiblePct: 50 }, deleted: false, deletedAt: null
    },
    // === FAMILY LAW MATTERS (15+) ===
    {
        id: 'matter_28', number: '00028', displayNumber: '00028-Gonzalez', description: 'Gonzalez Divorce - Contested dissolution with complex property division and child custody', status: 'open', billingMethod: 'hourly', clientId: 'contact_2', responsibleAttorneyId: 'user_3', originatingAttorneyId: 'user_1', responsibleStaffId: 'user_11', clientReferenceNumber: 'FL-2024-0034', location: 'Santa Clara County Family Court', practiceAreaId: 'pa_2', stageId: 'stage_2_3', openDate: '2024-01-12', pendingDate: null, closedDate: null, createdDate: '2024-01-11T10:00:00Z', templateId: 'template_2',
        permissions: { type: 'everyone', userIds: [], groupIds: [] }, blockedUsers: [],
        relationships: [{ contactId: 'contact_62', relationship: 'Opposing Party', billRecipient: false }],
        customFields: { cf_1: 'SC-2024-FL-00456', cf_6: 'Santa Clara County', cf_7: 'Hon. Patricia Kim' },
        billing: { billable: true, method: 'hourly', currency: 'USD', rates: [], budget: 25000, budgetUsed: 18750, trustBalance: 3000, minimumTrust: 2500, contingencyFee: null, flatRate: null },
        personalInjury: null,
        notifications: [{ userId: 'user_3', types: ['matter_updates', 'trust_balance'] }], documentFolders: [{ id: 'folder_28_1', name: 'Financial Disclosures', category: 'Financial' }, { id: 'folder_28_2', name: 'Custody Documents', category: 'Custody' }],
        reports: { useFirmSettings: true, originatingPct: 50, responsiblePct: 50 }, deleted: false, deletedAt: null
    },
    {
        id: 'matter_29', number: '00029', displayNumber: '00029-Nguyen', description: 'Nguyen v. Nguyen - Child custody modification and relocation request', status: 'open', billingMethod: 'hourly', clientId: 'contact_11', responsibleAttorneyId: 'user_3', originatingAttorneyId: 'user_3', responsibleStaffId: 'user_9', clientReferenceNumber: 'FL-2024-0089', location: 'San Francisco County Family Court', practiceAreaId: 'pa_2', stageId: 'stage_2_4', openDate: '2024-09-05', pendingDate: null, closedDate: null, createdDate: '2024-09-04T14:15:00Z', templateId: 'template_2',
        permissions: { type: 'everyone', userIds: [], groupIds: [] }, blockedUsers: [],
        relationships: [],
        customFields: { cf_1: 'SF-2024-FL-03421', cf_6: 'San Francisco County', cf_7: 'Hon. Robert Chen' },
        billing: { billable: true, method: 'hourly', currency: 'USD', rates: [], budget: 15000, budgetUsed: 11200, trustBalance: 1500, minimumTrust: 1000, contingencyFee: null, flatRate: null },
        personalInjury: null,
        notifications: [], documentFolders: [{ id: 'folder_29_1', name: 'Custody Documents', category: 'Custody' }],
        reports: { useFirmSettings: true, originatingPct: 100, responsiblePct: 0 }, deleted: false, deletedAt: null
    },
    {
        id: 'matter_30', number: '00030', displayNumber: '00030-Blackwell', description: 'Blackwell Divorce - High-asset dissolution with multiple properties and retirement accounts', status: 'open', billingMethod: 'hourly', clientId: 'contact_16', responsibleAttorneyId: 'user_3', originatingAttorneyId: 'user_1', responsibleStaffId: 'user_11', clientReferenceNumber: 'FL-2024-0067', location: 'San Francisco County Family Court', practiceAreaId: 'pa_2', stageId: 'stage_2_2', openDate: '2024-06-22', pendingDate: null, closedDate: null, createdDate: '2024-06-21T09:30:00Z', templateId: 'template_2',
        permissions: { type: 'specific', userIds: ['user_1', 'user_3', 'user_11'], groupIds: ['group_2'] }, blockedUsers: ['user_10'],
        relationships: [],
        customFields: { cf_1: 'SF-2024-FL-02789', cf_6: 'San Francisco County', cf_7: 'Hon. Maria Santos', cf_11: '4500000' },
        billing: { billable: true, method: 'hourly', currency: 'USD', rates: [{ userId: 'user_3', rate: 500 }], budget: 50000, budgetUsed: 32100, trustBalance: 10000, minimumTrust: 5000, contingencyFee: null, flatRate: null },
        personalInjury: null,
        notifications: [{ userId: 'user_1', types: ['budget_threshold'] }], documentFolders: [{ id: 'folder_30_1', name: 'Financial Disclosures', category: 'Financial' }, { id: 'folder_30_2', name: 'Property Appraisals', category: 'Financial' }],
        reports: { useFirmSettings: true, originatingPct: 50, responsiblePct: 50 }, deleted: false, deletedAt: null
    },
    {
        id: 'matter_31', number: '00031', displayNumber: '00031-Park-Anderson', description: 'Park-Anderson Prenuptial Agreement - Comprehensive prenuptial with business interests', status: 'closed', billingMethod: 'flat_rate', clientId: 'contact_33', responsibleAttorneyId: 'user_6', originatingAttorneyId: 'user_3', responsibleStaffId: 'user_11', clientReferenceNumber: 'FL-2024-0102', location: 'San Mateo County', practiceAreaId: 'pa_2', stageId: 'stage_2_2', openDate: '2024-03-25', pendingDate: '2024-10-01', closedDate: '2024-11-15', createdDate: '2024-03-24T11:00:00Z', templateId: 'template_2',
        permissions: { type: 'everyone', userIds: [], groupIds: [] }, blockedUsers: [],
        relationships: [], customFields: { cf_6: 'San Mateo County' },
        billing: { billable: true, method: 'flat_rate', currency: 'USD', rates: [], budget: 0, budgetUsed: 0, trustBalance: 5000, minimumTrust: 2500, contingencyFee: null, flatRate: { amount: 7500, recipientId: 'user_6' } },
        personalInjury: null,
        notifications: [], documentFolders: [{ id: 'folder_31_1', name: 'Financial Disclosures', category: 'Financial' }],
        reports: { useFirmSettings: true, originatingPct: 50, responsiblePct: 50 }, deleted: false, deletedAt: null
    },
    {
        id: 'matter_32', number: '00032', displayNumber: '00032-Sato', description: 'Sato Adoption - International adoption from Japan, complex immigration requirements', status: 'pending', billingMethod: 'hourly', clientId: 'contact_25', responsibleAttorneyId: 'user_3', originatingAttorneyId: 'user_3', responsibleStaffId: 'user_9', clientReferenceNumber: 'FL-2024-0078', location: 'San Francisco County Family Court', practiceAreaId: 'pa_2', stageId: 'stage_2_4', openDate: '2024-05-08', pendingDate: '2025-10-01', closedDate: null, createdDate: '2024-05-07T08:45:00Z', templateId: 'template_2',
        permissions: { type: 'everyone', userIds: [], groupIds: [] }, blockedUsers: [],
        relationships: [], customFields: { cf_1: 'SF-2024-FL-02100', cf_6: 'San Francisco County' },
        billing: { billable: true, method: 'hourly', currency: 'USD', rates: [], budget: 20000, budgetUsed: 17800, trustBalance: 500, minimumTrust: 1000, contingencyFee: null, flatRate: null },
        personalInjury: null,
        notifications: [{ userId: 'user_3', types: ['trust_balance'] }], documentFolders: [{ id: 'folder_32_1', name: 'Adoption Documents', category: 'Adoption' }, { id: 'folder_32_2', name: 'Immigration Forms', category: 'Immigration' }],
        reports: { useFirmSettings: true, originatingPct: 100, responsiblePct: 0 }, deleted: false, deletedAt: null
    },
    {
        id: 'matter_33', number: '00033', displayNumber: '00033-Stone', description: 'Stone v. Stone - Domestic violence restraining order and emergency custody', status: 'open', billingMethod: 'hourly', clientId: 'contact_44', responsibleAttorneyId: 'user_3', originatingAttorneyId: 'user_1', responsibleStaffId: 'user_11', clientReferenceNumber: 'FL-2024-0098', location: 'San Francisco County Family Court', practiceAreaId: 'pa_2', stageId: 'stage_2_1', openDate: '2024-08-06', pendingDate: null, closedDate: null, createdDate: '2024-08-05T16:30:00Z', templateId: 'template_2',
        permissions: { type: 'specific', userIds: ['user_1', 'user_3', 'user_11'], groupIds: [] }, blockedUsers: ['user_6', 'user_14'],
        relationships: [], customFields: { cf_1: 'SF-2024-FL-03100', cf_6: 'San Francisco County', cf_7: 'Hon. David Park' },
        billing: { billable: true, method: 'hourly', currency: 'USD', rates: [{ userId: 'user_3', rate: 400 }], budget: 10000, budgetUsed: 8500, trustBalance: 500, minimumTrust: 500, contingencyFee: null, flatRate: null },
        personalInjury: null,
        notifications: [{ userId: 'user_1', types: ['matter_updates'] }], documentFolders: [{ id: 'folder_33_1', name: 'Court Orders', category: 'Court' }],
        reports: { useFirmSettings: true, originatingPct: 50, responsiblePct: 50 }, deleted: false, deletedAt: null
    },
    {
        id: 'matter_34', number: '00034', displayNumber: '00034-Vasquez', description: 'Vasquez v. Vasquez - Child support modification due to income change', status: 'open', billingMethod: 'hourly', clientId: 'contact_67', responsibleAttorneyId: 'user_6', originatingAttorneyId: 'user_3', responsibleStaffId: 'user_9', clientReferenceNumber: 'FL-2024-0115', location: 'San Francisco County Family Court', practiceAreaId: 'pa_2', stageId: 'stage_2_3', openDate: '2024-04-16', pendingDate: null, closedDate: null, createdDate: '2024-04-15T10:20:00Z', templateId: 'template_2',
        permissions: { type: 'everyone', userIds: [], groupIds: [] }, blockedUsers: [],
        relationships: [], customFields: { cf_1: 'SF-2024-FL-01890', cf_6: 'San Francisco County' },
        billing: { billable: true, method: 'hourly', currency: 'USD', rates: [], budget: 8000, budgetUsed: 5600, trustBalance: 1200, minimumTrust: 1000, contingencyFee: null, flatRate: null },
        personalInjury: null,
        notifications: [], documentFolders: [{ id: 'folder_34_1', name: 'Financial Documents', category: 'Financial' }],
        reports: { useFirmSettings: true, originatingPct: 50, responsiblePct: 50 }, deleted: false, deletedAt: null
    },
    {
        id: 'matter_35', number: '00035', displayNumber: '00035-Baptiste', description: 'Baptiste v. Baptiste - Contested divorce with business valuation dispute', status: 'open', billingMethod: 'hourly', clientId: 'contact_62', responsibleAttorneyId: 'user_3', originatingAttorneyId: 'user_3', responsibleStaffId: 'user_11', clientReferenceNumber: 'FL-2025-0005', location: 'San Francisco County Family Court', practiceAreaId: 'pa_2', stageId: 'stage_2_1', openDate: '2025-01-08', pendingDate: null, closedDate: null, createdDate: '2025-01-07T14:00:00Z', templateId: 'template_2',
        permissions: { type: 'everyone', userIds: [], groupIds: [] }, blockedUsers: [],
        relationships: [], customFields: { cf_6: 'San Francisco County' },
        billing: { billable: true, method: 'hourly', currency: 'USD', rates: [], budget: 30000, budgetUsed: 4200, trustBalance: 5000, minimumTrust: 3000, contingencyFee: null, flatRate: null },
        personalInjury: null,
        notifications: [], documentFolders: [{ id: 'folder_35_1', name: 'Financial Disclosures', category: 'Financial' }],
        reports: { useFirmSettings: true, originatingPct: 100, responsiblePct: 0 }, deleted: false, deletedAt: null
    },
    {
        id: 'matter_36', number: '00036', displayNumber: '00036-Kowalski-Custody', description: 'Kowalski v. Kowalski - Grandparent visitation rights petition', status: 'closed', billingMethod: 'hourly', clientId: 'contact_8', responsibleAttorneyId: 'user_6', originatingAttorneyId: 'user_3', responsibleStaffId: 'user_9', clientReferenceNumber: 'FL-2024-0045', location: 'San Mateo County Family Court', practiceAreaId: 'pa_2', stageId: 'stage_2_5', openDate: '2024-07-16', pendingDate: '2025-02-01', closedDate: '2025-04-15', createdDate: '2024-07-15T09:15:00Z', templateId: 'template_2',
        permissions: { type: 'everyone', userIds: [], groupIds: [] }, blockedUsers: [],
        relationships: [], customFields: { cf_1: 'SM-2024-FL-00890', cf_6: 'San Mateo County', cf_7: 'Hon. Lisa Wong' },
        billing: { billable: true, method: 'hourly', currency: 'USD', rates: [], budget: 12000, budgetUsed: 11200, trustBalance: 0, minimumTrust: 0, contingencyFee: null, flatRate: null },
        personalInjury: null,
        notifications: [], documentFolders: [{ id: 'folder_36_1', name: 'Court Documents', category: 'Court' }],
        reports: { useFirmSettings: true, originatingPct: 50, responsiblePct: 50 }, deleted: false, deletedAt: null
    },
    {
        id: 'matter_37', number: '00037', displayNumber: '00037-Nguyen-2', description: 'Nguyen Guardianship - Establishing legal guardianship for elderly parent', status: 'open', billingMethod: 'hourly', clientId: 'contact_11', responsibleAttorneyId: 'user_6', originatingAttorneyId: 'user_3', responsibleStaffId: 'user_11', clientReferenceNumber: 'FL-2025-0018', location: 'San Francisco Probate Court', practiceAreaId: 'pa_2', stageId: 'stage_2_2', openDate: '2025-02-14', pendingDate: null, closedDate: null, createdDate: '2025-02-13T11:30:00Z', templateId: 'template_2',
        permissions: { type: 'everyone', userIds: [], groupIds: [] }, blockedUsers: [],
        relationships: [], customFields: { cf_6: 'San Francisco County' },
        billing: { billable: true, method: 'hourly', currency: 'USD', rates: [], budget: 10000, budgetUsed: 1800, trustBalance: 3000, minimumTrust: 2000, contingencyFee: null, flatRate: null },
        personalInjury: null,
        notifications: [], documentFolders: [{ id: 'folder_37_1', name: 'Court Documents', category: 'Court' }, { id: 'folder_37_2', name: 'Medical Evaluations', category: 'Medical' }],
        reports: { useFirmSettings: true, originatingPct: 50, responsiblePct: 50 }, deleted: false, deletedAt: null
    },
    {
        id: 'matter_38', number: '00038', displayNumber: '00038-Gonzalez-2', description: 'Gonzalez Paternity - Paternity establishment and parenting plan', status: 'closed', billingMethod: 'hourly', clientId: 'contact_2', responsibleAttorneyId: 'user_3', originatingAttorneyId: 'user_1', responsibleStaffId: 'user_9', clientReferenceNumber: 'FL-2024-0023', location: 'Santa Clara County Family Court', practiceAreaId: 'pa_2', stageId: 'stage_2_5', openDate: '2024-02-05', pendingDate: '2024-06-01', closedDate: '2024-08-30', createdDate: '2024-02-04T10:45:00Z', templateId: 'template_2',
        permissions: { type: 'everyone', userIds: [], groupIds: [] }, blockedUsers: [],
        relationships: [], customFields: { cf_1: 'SC-2024-FL-00123', cf_6: 'Santa Clara County' },
        billing: { billable: true, method: 'hourly', currency: 'USD', rates: [], budget: 8000, budgetUsed: 7500, trustBalance: 0, minimumTrust: 0, contingencyFee: null, flatRate: null },
        personalInjury: null,
        notifications: [], documentFolders: [{ id: 'folder_38_1', name: 'Court Documents', category: 'Court' }],
        reports: { useFirmSettings: true, originatingPct: 50, responsiblePct: 50 }, deleted: false, deletedAt: null
    },
    {
        id: 'matter_39', number: '00039', displayNumber: '00039-Blackwell-2', description: 'Blackwell Post-Judgment - Enforcement of spousal support order', status: 'open', billingMethod: 'hourly', clientId: 'contact_16', responsibleAttorneyId: 'user_3', originatingAttorneyId: 'user_3', responsibleStaffId: 'user_11', clientReferenceNumber: 'FL-2025-0029', location: 'San Francisco County Family Court', practiceAreaId: 'pa_2', stageId: 'stage_2_2', openDate: '2025-02-20', pendingDate: null, closedDate: null, createdDate: '2025-02-19T15:00:00Z', templateId: 'template_2',
        permissions: { type: 'specific', userIds: ['user_1', 'user_3', 'user_11'], groupIds: ['group_2'] }, blockedUsers: ['user_10'],
        relationships: [], customFields: { cf_1: 'SF-2025-FL-00456', cf_6: 'San Francisco County', cf_7: 'Hon. Maria Santos' },
        billing: { billable: true, method: 'hourly', currency: 'USD', rates: [{ userId: 'user_3', rate: 500 }], budget: 15000, budgetUsed: 2100, trustBalance: 5000, minimumTrust: 3000, contingencyFee: null, flatRate: null },
        personalInjury: null,
        notifications: [], documentFolders: [{ id: 'folder_39_1', name: 'Enforcement Documents', category: 'Court' }],
        reports: { useFirmSettings: true, originatingPct: 100, responsiblePct: 0 }, deleted: false, deletedAt: null
    },
    {
        id: 'matter_40', number: '00040', displayNumber: '00040-Stone-2', description: 'Stone v. Stone - Divorce filing following domestic violence restraining order', status: 'open', billingMethod: 'hourly', clientId: 'contact_44', responsibleAttorneyId: 'user_3', originatingAttorneyId: 'user_1', responsibleStaffId: 'user_11', clientReferenceNumber: 'FL-2024-0134', location: 'San Francisco County Family Court', practiceAreaId: 'pa_2', stageId: 'stage_2_3', openDate: '2024-10-01', pendingDate: null, closedDate: null, createdDate: '2024-09-30T09:00:00Z', templateId: 'template_2',
        permissions: { type: 'specific', userIds: ['user_1', 'user_3', 'user_11'], groupIds: [] }, blockedUsers: ['user_6', 'user_14'],
        relationships: [], customFields: { cf_1: 'SF-2024-FL-03890', cf_6: 'San Francisco County', cf_7: 'Hon. David Park' },
        billing: { billable: true, method: 'hourly', currency: 'USD', rates: [{ userId: 'user_3', rate: 400 }], budget: 20000, budgetUsed: 12400, trustBalance: 2000, minimumTrust: 1500, contingencyFee: null, flatRate: null },
        personalInjury: null,
        notifications: [{ userId: 'user_1', types: ['matter_updates'] }], documentFolders: [{ id: 'folder_40_1', name: 'Court Documents', category: 'Court' }, { id: 'folder_40_2', name: 'Financial Disclosures', category: 'Financial' }],
        reports: { useFirmSettings: true, originatingPct: 50, responsiblePct: 50 }, deleted: false, deletedAt: null
    },
    {
        id: 'matter_41', number: '00041', displayNumber: '00041-Petrovic-FL', description: 'Petrovic Annulment - Fraud-based marriage annulment petition', status: 'pending', billingMethod: 'hourly', clientId: 'contact_27', responsibleAttorneyId: 'user_6', originatingAttorneyId: 'user_3', responsibleStaffId: 'user_9', clientReferenceNumber: 'FL-2024-0056', location: 'Alameda County Family Court', practiceAreaId: 'pa_2', stageId: 'stage_2_5', openDate: '2024-07-01', pendingDate: '2025-06-15', closedDate: null, createdDate: '2024-06-30T13:00:00Z', templateId: 'template_2',
        permissions: { type: 'everyone', userIds: [], groupIds: [] }, blockedUsers: [],
        relationships: [], customFields: { cf_1: 'AC-2024-FL-01234', cf_6: 'Alameda County' },
        billing: { billable: true, method: 'hourly', currency: 'USD', rates: [], budget: 12000, budgetUsed: 10800, trustBalance: 0, minimumTrust: 0, contingencyFee: null, flatRate: null },
        personalInjury: null,
        notifications: [], documentFolders: [{ id: 'folder_41_1', name: 'Court Documents', category: 'Court' }],
        reports: { useFirmSettings: true, originatingPct: 50, responsiblePct: 50 }, deleted: false, deletedAt: null
    },
    {
        id: 'matter_42', number: '00042', displayNumber: '00042-Sato-2', description: 'Sato Postnuptial Agreement - Asset protection postnuptial agreement', status: 'open', billingMethod: 'flat_rate', clientId: 'contact_25', responsibleAttorneyId: 'user_6', originatingAttorneyId: 'user_6', responsibleStaffId: 'user_11', clientReferenceNumber: 'FL-2025-0032', location: 'San Francisco County', practiceAreaId: 'pa_2', stageId: 'stage_2_1', openDate: '2025-02-25', pendingDate: null, closedDate: null, createdDate: '2025-02-24T09:00:00Z', templateId: 'template_2',
        permissions: { type: 'everyone', userIds: [], groupIds: [] }, blockedUsers: [],
        relationships: [], customFields: { cf_6: 'San Francisco County' },
        billing: { billable: true, method: 'flat_rate', currency: 'USD', rates: [], budget: 0, budgetUsed: 0, trustBalance: 4000, minimumTrust: 2000, contingencyFee: null, flatRate: { amount: 6000, recipientId: 'user_6' } },
        personalInjury: null,
        notifications: [], documentFolders: [{ id: 'folder_42_1', name: 'Financial Disclosures', category: 'Financial' }],
        reports: { useFirmSettings: true, originatingPct: 100, responsiblePct: 0 }, deleted: false, deletedAt: null
    },
    // === CRIMINAL DEFENSE MATTERS (12+) ===
    {
        id: 'matter_43', number: '00043', displayNumber: '00043-ChenRamirez', description: 'People v. Chen-Ramirez - DUI defense, first offense, BAC 0.12', status: 'pending', billingMethod: 'flat_rate', clientId: 'contact_3', responsibleAttorneyId: 'user_8', originatingAttorneyId: 'user_8', responsibleStaffId: 'user_15', clientReferenceNumber: 'CD-2024-0045', location: 'Alameda County Criminal Court', practiceAreaId: 'pa_3', stageId: 'stage_3_2', openDate: '2024-02-22', pendingDate: '2025-05-01', closedDate: null, createdDate: '2024-02-21T16:00:00Z', templateId: 'template_3',
        permissions: { type: 'everyone', userIds: [], groupIds: [] }, blockedUsers: [],
        relationships: [], customFields: { cf_1: 'AC-2024-CR-04567', cf_7: 'Hon. Sandra Lee', cf_8: '2025-06-15' },
        billing: { billable: true, method: 'flat_rate', currency: 'USD', rates: [], budget: 0, budgetUsed: 0, trustBalance: 5000, minimumTrust: 2500, contingencyFee: null, flatRate: { amount: 7500, recipientId: 'user_8' } },
        personalInjury: null,
        notifications: [], documentFolders: [{ id: 'folder_43_1', name: 'Police Reports', category: 'Evidence' }, { id: 'folder_43_2', name: 'Court Documents', category: 'Court' }],
        reports: { useFirmSettings: true, originatingPct: 100, responsiblePct: 0 }, deleted: false, deletedAt: null
    },
    {
        id: 'matter_44', number: '00044', displayNumber: '00044-Thompson', description: 'People v. Thompson - Felony assault charge, bar altercation', status: 'open', billingMethod: 'hourly', clientId: 'contact_9', responsibleAttorneyId: 'user_8', originatingAttorneyId: 'user_1', responsibleStaffId: 'user_15', clientReferenceNumber: 'CD-2024-0078', location: 'Alameda County Criminal Court', practiceAreaId: 'pa_3', stageId: 'stage_3_3', openDate: '2024-08-25', pendingDate: null, closedDate: null, createdDate: '2024-08-24T14:30:00Z', templateId: 'template_3',
        permissions: { type: 'everyone', userIds: [], groupIds: [] }, blockedUsers: [],
        relationships: [], customFields: { cf_1: 'AC-2024-CR-09876', cf_7: 'Hon. James Wright', cf_8: '2025-04-22' },
        billing: { billable: true, method: 'hourly', currency: 'USD', rates: [], budget: 25000, budgetUsed: 16800, trustBalance: 3000, minimumTrust: 2000, contingencyFee: null, flatRate: null },
        personalInjury: null,
        notifications: [{ userId: 'user_1', types: ['matter_updates'] }], documentFolders: [{ id: 'folder_44_1', name: 'Police Reports', category: 'Evidence' }, { id: 'folder_44_2', name: 'Witness Statements', category: 'Evidence' }],
        reports: { useFirmSettings: true, originatingPct: 50, responsiblePct: 50 }, deleted: false, deletedAt: null
    },
    {
        id: 'matter_45', number: '00045', displayNumber: '00045-OConnor', description: "People v. O'Connor - Drug possession charge, diversion program eligibility", status: 'open', billingMethod: 'flat_rate', clientId: 'contact_18', responsibleAttorneyId: 'user_8', originatingAttorneyId: 'user_8', responsibleStaffId: 'user_5', clientReferenceNumber: 'CD-2024-0091', location: 'San Francisco County Criminal Court', practiceAreaId: 'pa_3', stageId: 'stage_3_2', openDate: '2024-07-30', pendingDate: null, closedDate: null, createdDate: '2024-07-29T09:00:00Z', templateId: 'template_3',
        permissions: { type: 'everyone', userIds: [], groupIds: [] }, blockedUsers: [],
        relationships: [], customFields: { cf_1: 'SF-2024-CR-05678', cf_7: 'Hon. Michael Torres', cf_8: '2025-03-15' },
        billing: { billable: true, method: 'flat_rate', currency: 'USD', rates: [], budget: 0, budgetUsed: 0, trustBalance: 3500, minimumTrust: 2000, contingencyFee: null, flatRate: { amount: 5000, recipientId: 'user_8' } },
        personalInjury: null,
        notifications: [], documentFolders: [{ id: 'folder_45_1', name: 'Police Reports', category: 'Evidence' }],
        reports: { useFirmSettings: true, originatingPct: 100, responsiblePct: 0 }, deleted: false, deletedAt: null
    },
    {
        id: 'matter_46', number: '00046', displayNumber: '00046-Hernandez', description: 'People v. Hernandez - Armed robbery charge, alibi defense', status: 'open', billingMethod: 'hourly', clientId: 'contact_29', responsibleAttorneyId: 'user_8', originatingAttorneyId: 'user_1', responsibleStaffId: 'user_15', clientReferenceNumber: 'CD-2024-0034', location: 'San Francisco County Superior Court', practiceAreaId: 'pa_3', stageId: 'stage_3_4', openDate: '2024-07-06', pendingDate: null, closedDate: null, createdDate: '2024-07-05T11:00:00Z', templateId: 'template_3',
        permissions: { type: 'specific', userIds: ['user_1', 'user_8', 'user_5', 'user_15'], groupIds: ['group_4'] }, blockedUsers: [],
        relationships: [], customFields: { cf_1: 'SF-2024-CR-07890', cf_7: 'Hon. Patricia Kim', cf_8: '2025-05-01' },
        billing: { billable: true, method: 'hourly', currency: 'USD', rates: [], budget: 50000, budgetUsed: 38900, trustBalance: 5000, minimumTrust: 5000, contingencyFee: null, flatRate: null },
        personalInjury: null,
        notifications: [{ userId: 'user_1', types: ['matter_updates', 'budget_threshold'] }], documentFolders: [{ id: 'folder_46_1', name: 'Police Reports', category: 'Evidence' }, { id: 'folder_46_2', name: 'Witness Statements', category: 'Evidence' }, { id: 'folder_46_3', name: 'Surveillance Footage', category: 'Evidence' }],
        reports: { useFirmSettings: false, originatingPct: 40, responsiblePct: 60 }, deleted: false, deletedAt: null
    },
    {
        id: 'matter_47', number: '00047', displayNumber: '00047-Franklin', description: 'People v. Franklin - Securities fraud and embezzlement, white-collar defense', status: 'open', billingMethod: 'hourly', clientId: 'contact_35', responsibleAttorneyId: 'user_8', originatingAttorneyId: 'user_4', responsibleStaffId: 'user_15', clientReferenceNumber: 'CD-2024-0112', location: 'Northern District of California', practiceAreaId: 'pa_3', stageId: 'stage_3_2', openDate: '2024-12-20', pendingDate: null, closedDate: null, createdDate: '2024-12-19T15:00:00Z', templateId: 'template_3',
        permissions: { type: 'specific', userIds: ['user_1', 'user_4', 'user_8', 'user_15'], groupIds: [] }, blockedUsers: [],
        relationships: [], customFields: { cf_1: 'NDCA-2024-CR-01234', cf_7: 'Hon. Elizabeth Chen', cf_8: '2025-07-15' },
        billing: { billable: true, method: 'hourly', currency: 'USD', rates: [{ userId: 'user_8', rate: 450 }, { userId: 'user_4', rate: 600 }], budget: 200000, budgetUsed: 42300, trustBalance: 25000, minimumTrust: 10000, contingencyFee: null, flatRate: null },
        personalInjury: null,
        notifications: [{ userId: 'user_4', types: ['matter_updates', 'budget_threshold'] }], documentFolders: [{ id: 'folder_47_1', name: 'Financial Records', category: 'Financial' }, { id: 'folder_47_2', name: 'SEC Filings', category: 'Regulatory' }],
        reports: { useFirmSettings: false, originatingPct: 30, responsiblePct: 70 }, deleted: false, deletedAt: null
    },
    {
        id: 'matter_48', number: '00048', displayNumber: '00048-DeLuca', description: 'People v. DeLuca - Felony DUI with injury, third offense', status: 'open', billingMethod: 'hourly', clientId: 'contact_46', responsibleAttorneyId: 'user_5', originatingAttorneyId: 'user_8', responsibleStaffId: 'user_15', clientReferenceNumber: 'CD-2024-0123', location: 'San Francisco County Criminal Court', practiceAreaId: 'pa_3', stageId: 'stage_3_1', openDate: '2024-12-08', pendingDate: null, closedDate: null, createdDate: '2024-12-07T08:30:00Z', templateId: 'template_3',
        permissions: { type: 'everyone', userIds: [], groupIds: [] }, blockedUsers: [],
        relationships: [], customFields: { cf_1: 'SF-2024-CR-11234', cf_7: 'Hon. Michael Torres', cf_8: '2025-04-10' },
        billing: { billable: true, method: 'hourly', currency: 'USD', rates: [], budget: 30000, budgetUsed: 5600, trustBalance: 7500, minimumTrust: 5000, contingencyFee: null, flatRate: null },
        personalInjury: null,
        notifications: [], documentFolders: [{ id: 'folder_48_1', name: 'Police Reports', category: 'Evidence' }, { id: 'folder_48_2', name: 'BAC Records', category: 'Evidence' }],
        reports: { useFirmSettings: true, originatingPct: 50, responsiblePct: 50 }, deleted: false, deletedAt: null
    },
    {
        id: 'matter_49', number: '00049', displayNumber: '00049-Torres', description: 'People v. Torres - Misdemeanor shoplifting, first offense with mental health considerations', status: 'closed', billingMethod: 'flat_rate', clientId: 'contact_54', responsibleAttorneyId: 'user_5', originatingAttorneyId: 'user_8', responsibleStaffId: 'user_15', clientReferenceNumber: 'CD-2024-0098', location: 'San Francisco County Criminal Court', practiceAreaId: 'pa_3', stageId: 'stage_3_5', openDate: '2024-08-29', pendingDate: '2024-12-01', closedDate: '2025-01-15', createdDate: '2024-08-28T10:00:00Z', templateId: 'template_3',
        permissions: { type: 'everyone', userIds: [], groupIds: [] }, blockedUsers: [],
        relationships: [], customFields: { cf_1: 'SF-2024-CR-08901', cf_7: 'Hon. Sandra Lee' },
        billing: { billable: true, method: 'flat_rate', currency: 'USD', rates: [], budget: 0, budgetUsed: 0, trustBalance: 0, minimumTrust: 0, contingencyFee: null, flatRate: { amount: 3500, recipientId: 'user_5' } },
        personalInjury: null,
        notifications: [], documentFolders: [{ id: 'folder_49_1', name: 'Court Documents', category: 'Court' }],
        reports: { useFirmSettings: true, originatingPct: 50, responsiblePct: 50 }, deleted: false, deletedAt: null
    },
    {
        id: 'matter_50', number: '00050', displayNumber: '00050-Thompson-2', description: 'People v. Thompson - Domestic violence charge, anger management defense', status: 'pending', billingMethod: 'hourly', clientId: 'contact_9', responsibleAttorneyId: 'user_8', originatingAttorneyId: 'user_8', responsibleStaffId: 'user_5', clientReferenceNumber: 'CD-2025-0012', location: 'Alameda County Criminal Court', practiceAreaId: 'pa_3', stageId: 'stage_3_3', openDate: '2025-01-10', pendingDate: '2025-12-01', closedDate: null, createdDate: '2025-01-09T14:00:00Z', templateId: 'template_3',
        permissions: { type: 'everyone', userIds: [], groupIds: [] }, blockedUsers: [],
        relationships: [], customFields: { cf_1: 'AC-2025-CR-00456', cf_7: 'Hon. James Wright', cf_8: '2025-06-20' },
        billing: { billable: true, method: 'hourly', currency: 'USD', rates: [], budget: 15000, budgetUsed: 8900, trustBalance: 2000, minimumTrust: 1500, contingencyFee: null, flatRate: null },
        personalInjury: null,
        notifications: [], documentFolders: [{ id: 'folder_50_1', name: 'Court Documents', category: 'Court' }],
        reports: { useFirmSettings: true, originatingPct: 100, responsiblePct: 0 }, deleted: false, deletedAt: null
    },
    {
        id: 'matter_51', number: '00051', displayNumber: '00051-ChenRamirez-2', description: 'People v. Chen-Ramirez - Reckless driving charge from separate incident', status: 'open', billingMethod: 'flat_rate', clientId: 'contact_3', responsibleAttorneyId: 'user_5', originatingAttorneyId: 'user_8', responsibleStaffId: 'user_15', clientReferenceNumber: 'CD-2025-0034', location: 'Alameda County Criminal Court', practiceAreaId: 'pa_3', stageId: 'stage_3_1', openDate: '2025-02-15', pendingDate: null, closedDate: null, createdDate: '2025-02-14T11:45:00Z', templateId: 'template_3',
        permissions: { type: 'everyone', userIds: [], groupIds: [] }, blockedUsers: [],
        relationships: [], customFields: { cf_1: 'AC-2025-CR-01234', cf_7: 'Hon. Sandra Lee', cf_8: '2025-05-20' },
        billing: { billable: true, method: 'flat_rate', currency: 'USD', rates: [], budget: 0, budgetUsed: 0, trustBalance: 4000, minimumTrust: 2000, contingencyFee: null, flatRate: { amount: 5000, recipientId: 'user_5' } },
        personalInjury: null,
        notifications: [], documentFolders: [{ id: 'folder_51_1', name: 'Police Reports', category: 'Evidence' }],
        reports: { useFirmSettings: true, originatingPct: 50, responsiblePct: 50 }, deleted: false, deletedAt: null
    },
    {
        id: 'matter_52', number: '00052', displayNumber: '00052-Hernandez-2', description: 'People v. Hernandez - Probation violation hearing from prior conviction', status: 'open', billingMethod: 'hourly', clientId: 'contact_29', responsibleAttorneyId: 'user_8', originatingAttorneyId: 'user_8', responsibleStaffId: 'user_15', clientReferenceNumber: 'CD-2025-0023', location: 'San Francisco County Superior Court', practiceAreaId: 'pa_3', stageId: 'stage_3_2', openDate: '2025-01-25', pendingDate: null, closedDate: null, createdDate: '2025-01-24T09:30:00Z', templateId: 'template_3',
        permissions: { type: 'specific', userIds: ['user_1', 'user_8', 'user_5', 'user_15'], groupIds: ['group_4'] }, blockedUsers: [],
        relationships: [], customFields: { cf_1: 'SF-2025-CR-00234', cf_7: 'Hon. Patricia Kim', cf_8: '2025-04-15' },
        billing: { billable: true, method: 'hourly', currency: 'USD', rates: [], budget: 10000, budgetUsed: 3200, trustBalance: 2000, minimumTrust: 1500, contingencyFee: null, flatRate: null },
        personalInjury: null,
        notifications: [], documentFolders: [{ id: 'folder_52_1', name: 'Court Documents', category: 'Court' }],
        reports: { useFirmSettings: true, originatingPct: 100, responsiblePct: 0 }, deleted: false, deletedAt: null
    },
    {
        id: 'matter_53', number: '00053', displayNumber: '00053-OConnor-2', description: "People v. O'Connor - Trespassing and public intoxication charges", status: 'closed', billingMethod: 'flat_rate', clientId: 'contact_18', responsibleAttorneyId: 'user_5', originatingAttorneyId: 'user_8', responsibleStaffId: 'user_15', clientReferenceNumber: 'CD-2024-0056', location: 'San Francisco County Criminal Court', practiceAreaId: 'pa_3', stageId: 'stage_3_5', openDate: '2024-04-10', pendingDate: '2024-09-01', closedDate: '2024-11-15', createdDate: '2024-04-09T13:00:00Z', templateId: 'template_3',
        permissions: { type: 'everyone', userIds: [], groupIds: [] }, blockedUsers: [],
        relationships: [], customFields: { cf_1: 'SF-2024-CR-03456', cf_7: 'Hon. Michael Torres' },
        billing: { billable: true, method: 'flat_rate', currency: 'USD', rates: [], budget: 0, budgetUsed: 0, trustBalance: 0, minimumTrust: 0, contingencyFee: null, flatRate: { amount: 2500, recipientId: 'user_5' } },
        personalInjury: null,
        notifications: [], documentFolders: [{ id: 'folder_53_1', name: 'Court Documents', category: 'Court' }],
        reports: { useFirmSettings: true, originatingPct: 50, responsiblePct: 50 }, deleted: false, deletedAt: null
    },
    {
        id: 'matter_54', number: '00054', displayNumber: '00054-DeLuca-2', description: 'People v. DeLuca - Hit and run, leaving the scene of accident', status: 'pending', billingMethod: 'hourly', clientId: 'contact_46', responsibleAttorneyId: 'user_8', originatingAttorneyId: 'user_5', responsibleStaffId: 'user_15', clientReferenceNumber: 'CD-2024-0145', location: 'San Francisco County Criminal Court', practiceAreaId: 'pa_3', stageId: 'stage_3_3', openDate: '2024-11-10', pendingDate: '2025-10-01', closedDate: null, createdDate: '2024-11-09T10:00:00Z', templateId: 'template_3',
        permissions: { type: 'everyone', userIds: [], groupIds: [] }, blockedUsers: [],
        relationships: [], customFields: { cf_1: 'SF-2024-CR-10567', cf_7: 'Hon. Sandra Lee', cf_8: '2025-04-05' },
        billing: { billable: true, method: 'hourly', currency: 'USD', rates: [], budget: 20000, budgetUsed: 14500, trustBalance: 1000, minimumTrust: 1000, contingencyFee: null, flatRate: null },
        personalInjury: null,
        notifications: [], documentFolders: [{ id: 'folder_54_1', name: 'Police Reports', category: 'Evidence' }],
        reports: { useFirmSettings: true, originatingPct: 50, responsiblePct: 50 }, deleted: false, deletedAt: null
    },
    // === REAL ESTATE MATTERS (8) ===
    {
        id: 'matter_55', number: '00055', displayNumber: '00055-OMalley', description: "O'Malley Residential Purchase - Single family home acquisition in Daly City", status: 'closed', billingMethod: 'flat_rate', clientId: 'contact_6', responsibleAttorneyId: 'user_13', originatingAttorneyId: 'user_1', responsibleStaffId: 'user_7', clientReferenceNumber: 'RE-2024-0012', location: 'San Mateo County', practiceAreaId: 'pa_4', stageId: 'stage_4_2', openDate: '2024-03-30', pendingDate: '2024-09-15', closedDate: '2024-10-30', createdDate: '2024-03-29T10:00:00Z', templateId: 'template_5',
        permissions: { type: 'everyone', userIds: [], groupIds: [] }, blockedUsers: [],
        relationships: [{ contactId: 'contact_24', relationship: 'Other', billRecipient: false }],
        customFields: { cf_6: 'San Mateo County' },
        billing: { billable: true, method: 'flat_rate', currency: 'USD', rates: [], budget: 0, budgetUsed: 0, trustBalance: 3500, minimumTrust: 1500, contingencyFee: null, flatRate: { amount: 4500, recipientId: 'user_13' } },
        personalInjury: null,
        notifications: [], documentFolders: [{ id: 'folder_55_1', name: 'Title Documents', category: 'Title' }, { id: 'folder_55_2', name: 'Inspection Reports', category: 'Inspection' }],
        reports: { useFirmSettings: true, originatingPct: 50, responsiblePct: 50 }, deleted: false, deletedAt: null
    },
    {
        id: 'matter_56', number: '00056', displayNumber: '00056-GoldenGateProperties', description: 'Golden Gate Properties - Commercial lease negotiation for 3-story office building', status: 'pending', billingMethod: 'hourly', clientId: 'contact_13', responsibleAttorneyId: 'user_13', originatingAttorneyId: 'user_4', responsibleStaffId: 'user_6', clientReferenceNumber: 'RE-2024-0034', location: 'San Francisco County', practiceAreaId: 'pa_4', stageId: 'stage_4_1', openDate: '2024-02-16', pendingDate: '2025-10-01', closedDate: null, createdDate: '2024-02-15T14:00:00Z', templateId: 'template_5',
        permissions: { type: 'everyone', userIds: [], groupIds: [] }, blockedUsers: [],
        relationships: [{ contactId: 'contact_63', relationship: 'Other', billRecipient: false }],
        customFields: { cf_6: 'San Francisco County' },
        billing: { billable: true, method: 'hourly', currency: 'USD', rates: [], budget: 35000, budgetUsed: 28400, trustBalance: 5000, minimumTrust: 3000, contingencyFee: null, flatRate: null },
        personalInjury: null,
        notifications: [{ userId: 'user_4', types: ['budget_threshold'] }], documentFolders: [{ id: 'folder_56_1', name: 'Lease Documents', category: 'Contracts' }, { id: 'folder_56_2', name: 'Property Reports', category: 'Inspection' }],
        reports: { useFirmSettings: true, originatingPct: 50, responsiblePct: 50 }, deleted: false, deletedAt: null
    },
    {
        id: 'matter_57', number: '00057', displayNumber: '00057-Morrison', description: 'Morrison Property Sale - Luxury condo sale in Pacific Heights with HOA complications', status: 'closed', billingMethod: 'flat_rate', clientId: 'contact_41', responsibleAttorneyId: 'user_6', originatingAttorneyId: 'user_13', responsibleStaffId: 'user_7', clientReferenceNumber: 'RE-2024-0023', location: 'San Francisco County', practiceAreaId: 'pa_4', stageId: 'stage_4_3', openDate: '2024-05-23', pendingDate: '2024-10-01', closedDate: '2024-11-15', createdDate: '2024-05-22T09:30:00Z', templateId: 'template_5',
        permissions: { type: 'everyone', userIds: [], groupIds: [] }, blockedUsers: [],
        relationships: [], customFields: { cf_6: 'San Francisco County' },
        billing: { billable: true, method: 'flat_rate', currency: 'USD', rates: [], budget: 0, budgetUsed: 0, trustBalance: 0, minimumTrust: 0, contingencyFee: null, flatRate: { amount: 6000, recipientId: 'user_6' } },
        personalInjury: null,
        notifications: [], documentFolders: [{ id: 'folder_57_1', name: 'Closing Documents', category: 'Closing' }],
        reports: { useFirmSettings: true, originatingPct: 50, responsiblePct: 50 }, deleted: false, deletedAt: null
    },
    {
        id: 'matter_58', number: '00058', displayNumber: '00058-CoastalRealty', description: 'Coastal Realty v. Pacific Heights HOA - Dispute over commercial zoning restrictions', status: 'open', billingMethod: 'hourly', clientId: 'contact_24', responsibleAttorneyId: 'user_13', originatingAttorneyId: 'user_13', responsibleStaffId: 'user_6', clientReferenceNumber: 'RE-2024-0056', location: 'Santa Cruz County Superior Court', practiceAreaId: 'pa_4', stageId: 'stage_4_1', openDate: '2024-12-05', pendingDate: null, closedDate: null, createdDate: '2024-12-04T11:00:00Z', templateId: 'template_5',
        permissions: { type: 'everyone', userIds: [], groupIds: [] }, blockedUsers: [],
        relationships: [], customFields: { cf_1: 'SCR-2024-CV-04567', cf_6: 'Santa Cruz County' },
        billing: { billable: true, method: 'hourly', currency: 'USD', rates: [], budget: 40000, budgetUsed: 8900, trustBalance: 8000, minimumTrust: 5000, contingencyFee: null, flatRate: null },
        personalInjury: null,
        notifications: [], documentFolders: [{ id: 'folder_58_1', name: 'Zoning Documents', category: 'Regulatory' }],
        reports: { useFirmSettings: true, originatingPct: 100, responsiblePct: 0 }, deleted: false, deletedAt: null
    },
    {
        id: 'matter_59', number: '00059', displayNumber: '00059-Andersen', description: 'Andersen Property Purchase - Multi-unit investment property in Nob Hill', status: 'open', billingMethod: 'flat_rate', clientId: 'contact_69', responsibleAttorneyId: 'user_6', originatingAttorneyId: 'user_13', responsibleStaffId: 'user_7', clientReferenceNumber: 'RE-2025-0008', location: 'San Francisco County', practiceAreaId: 'pa_4', stageId: 'stage_4_1', openDate: '2025-02-20', pendingDate: null, closedDate: null, createdDate: '2025-02-19T10:15:00Z', templateId: 'template_5',
        permissions: { type: 'everyone', userIds: [], groupIds: [] }, blockedUsers: [],
        relationships: [], customFields: { cf_6: 'San Francisco County' },
        billing: { billable: true, method: 'flat_rate', currency: 'USD', rates: [], budget: 0, budgetUsed: 0, trustBalance: 5500, minimumTrust: 2500, contingencyFee: null, flatRate: { amount: 8000, recipientId: 'user_6' } },
        personalInjury: null,
        notifications: [], documentFolders: [{ id: 'folder_59_1', name: 'Title Documents', category: 'Title' }],
        reports: { useFirmSettings: true, originatingPct: 50, responsiblePct: 50 }, deleted: false, deletedAt: null
    },
    {
        id: 'matter_60', number: '00060', displayNumber: '00060-AllianceProperty', description: 'Alliance Property v. Tenants Assoc. - Eviction dispute for commercial tenants', status: 'pending', billingMethod: 'hourly', clientId: 'contact_63', responsibleAttorneyId: 'user_13', originatingAttorneyId: 'user_4', responsibleStaffId: 'user_6', clientReferenceNumber: 'RE-2024-0078', location: 'San Francisco County Superior Court', practiceAreaId: 'pa_4', stageId: 'stage_4_2', openDate: '2024-05-18', pendingDate: '2025-07-01', closedDate: null, createdDate: '2024-05-17T13:30:00Z', templateId: null,
        permissions: { type: 'everyone', userIds: [], groupIds: [] }, blockedUsers: [],
        relationships: [], customFields: { cf_1: 'SF-2024-CV-10234', cf_6: 'San Francisco County', cf_7: 'Hon. Robert Chen' },
        billing: { billable: true, method: 'hourly', currency: 'USD', rates: [], budget: 25000, budgetUsed: 19800, trustBalance: 3000, minimumTrust: 2000, contingencyFee: null, flatRate: null },
        personalInjury: null,
        notifications: [], documentFolders: [{ id: 'folder_60_1', name: 'Lease Agreements', category: 'Contracts' }, { id: 'folder_60_2', name: 'Court Documents', category: 'Court' }],
        reports: { useFirmSettings: true, originatingPct: 50, responsiblePct: 50 }, deleted: false, deletedAt: null
    },
    {
        id: 'matter_61', number: '00061', displayNumber: '00061-OMalley-2', description: "O'Malley Property Boundary - Neighbor boundary dispute and fence line litigation", status: 'pending', billingMethod: 'hourly', clientId: 'contact_6', responsibleAttorneyId: 'user_6', originatingAttorneyId: 'user_13', responsibleStaffId: 'user_7', clientReferenceNumber: 'RE-2024-0045', location: 'San Mateo County Superior Court', practiceAreaId: 'pa_4', stageId: 'stage_4_2', openDate: '2024-08-12', pendingDate: '2025-09-01', closedDate: null, createdDate: '2024-08-11T09:00:00Z', templateId: null,
        permissions: { type: 'everyone', userIds: [], groupIds: [] }, blockedUsers: [],
        relationships: [], customFields: { cf_1: 'SM-2024-CV-06789', cf_6: 'San Mateo County' },
        billing: { billable: true, method: 'hourly', currency: 'USD', rates: [], budget: 15000, budgetUsed: 12300, trustBalance: 500, minimumTrust: 500, contingencyFee: null, flatRate: null },
        personalInjury: null,
        notifications: [], documentFolders: [{ id: 'folder_61_1', name: 'Survey Reports', category: 'Evidence' }],
        reports: { useFirmSettings: true, originatingPct: 50, responsiblePct: 50 }, deleted: false, deletedAt: null
    },
    {
        id: 'matter_62', number: '00062', displayNumber: '00062-GoldenGateProperties-2', description: 'Golden Gate Properties - Construction defect claim for newly built condos', status: 'open', billingMethod: 'hourly', clientId: 'contact_13', responsibleAttorneyId: 'user_13', originatingAttorneyId: 'user_13', responsibleStaffId: 'user_6', clientReferenceNumber: 'RE-2025-0015', location: 'San Francisco County Superior Court', practiceAreaId: 'pa_4', stageId: 'stage_4_1', openDate: '2025-01-28', pendingDate: null, closedDate: null, createdDate: '2025-01-27T14:45:00Z', templateId: null,
        permissions: { type: 'everyone', userIds: [], groupIds: [] }, blockedUsers: [],
        relationships: [{ contactId: 'contact_7', relationship: 'Opposing Party', billRecipient: false }],
        customFields: { cf_6: 'San Francisco County' },
        billing: { billable: true, method: 'hourly', currency: 'USD', rates: [], budget: 60000, budgetUsed: 5600, trustBalance: 10000, minimumTrust: 5000, contingencyFee: null, flatRate: null },
        personalInjury: null,
        notifications: [{ userId: 'user_13', types: ['matter_updates'] }], documentFolders: [{ id: 'folder_62_1', name: 'Inspection Reports', category: 'Inspection' }, { id: 'folder_62_2', name: 'Construction Documents', category: 'Evidence' }],
        reports: { useFirmSettings: true, originatingPct: 100, responsiblePct: 0 }, deleted: false, deletedAt: null
    },
    // === CORPORATE/BUSINESS MATTERS (10) ===
    {
        id: 'matter_63', number: '00063', displayNumber: '00063-VertexTech', description: 'Vertex Technologies - Series B financing and investor agreements', status: 'open', billingMethod: 'hourly', clientId: 'contact_4', responsibleAttorneyId: 'user_4', originatingAttorneyId: 'user_1', responsibleStaffId: 'user_14', clientReferenceNumber: 'CORP-2024-0012', location: 'Delaware', practiceAreaId: 'pa_5', stageId: 'stage_5_2', openDate: '2024-04-05', pendingDate: null, closedDate: null, createdDate: '2024-04-04T09:00:00Z', templateId: 'template_4',
        permissions: { type: 'everyone', userIds: [], groupIds: [] }, blockedUsers: [],
        relationships: [{ contactId: 'contact_28', relationship: 'Other', billRecipient: false }],
        customFields: { cf_6: 'Delaware' },
        billing: { billable: true, method: 'hourly', currency: 'USD', rates: [{ userId: 'user_4', rate: 600 }], budget: 75000, budgetUsed: 42300, trustBalance: 15000, minimumTrust: 10000, contingencyFee: null, flatRate: null },
        personalInjury: null,
        notifications: [{ userId: 'user_4', types: ['matter_updates', 'budget_threshold'] }], documentFolders: [{ id: 'folder_63_1', name: 'Term Sheets', category: 'Contracts' }, { id: 'folder_63_2', name: 'Investor Agreements', category: 'Contracts' }],
        reports: { useFirmSettings: true, originatingPct: 50, responsiblePct: 50 }, deleted: false, deletedAt: null
    },
    {
        id: 'matter_64', number: '00064', displayNumber: '00064-PacificRim', description: 'Pacific Rim Imports - Import/export compliance review and trade agreement', status: 'pending', billingMethod: 'hourly', clientId: 'contact_10', responsibleAttorneyId: 'user_12', originatingAttorneyId: 'user_4', responsibleStaffId: 'user_14', clientReferenceNumber: 'CORP-2024-0023', location: 'Northern District of California', practiceAreaId: 'pa_5', stageId: 'stage_5_3', openDate: '2024-01-28', pendingDate: '2025-09-01', closedDate: null, createdDate: '2024-01-27T11:30:00Z', templateId: 'template_4',
        permissions: { type: 'everyone', userIds: [], groupIds: [] }, blockedUsers: [],
        relationships: [], customFields: { cf_6: 'California / International' },
        billing: { billable: true, method: 'hourly', currency: 'USD', rates: [], budget: 45000, budgetUsed: 38700, trustBalance: 2000, minimumTrust: 2000, contingencyFee: null, flatRate: null },
        personalInjury: null,
        notifications: [], documentFolders: [{ id: 'folder_64_1', name: 'Trade Agreements', category: 'Contracts' }, { id: 'folder_64_2', name: 'Compliance Documents', category: 'Regulatory' }],
        reports: { useFirmSettings: true, originatingPct: 50, responsiblePct: 50 }, deleted: false, deletedAt: null
    },
    {
        id: 'matter_65', number: '00065', displayNumber: '00065-NovaBio', description: 'NovaBio Pharmaceuticals - FDA regulatory compliance and product approval', status: 'open', billingMethod: 'hourly', clientId: 'contact_17', responsibleAttorneyId: 'user_4', originatingAttorneyId: 'user_4', responsibleStaffId: 'user_14', clientReferenceNumber: 'CORP-2024-0034', location: 'FDA / California', practiceAreaId: 'pa_5', stageId: 'stage_5_2', openDate: '2024-03-08', pendingDate: null, closedDate: null, createdDate: '2024-03-07T10:00:00Z', templateId: 'template_4',
        permissions: { type: 'specific', userIds: ['user_1', 'user_4', 'user_14'], groupIds: ['group_3'] }, blockedUsers: [],
        relationships: [], customFields: { cf_6: 'Federal / California' },
        billing: { billable: true, method: 'hourly', currency: 'USD', rates: [{ userId: 'user_4', rate: 600 }], budget: 120000, budgetUsed: 89500, trustBalance: 10000, minimumTrust: 5000, contingencyFee: null, flatRate: null },
        personalInjury: null,
        notifications: [{ userId: 'user_4', types: ['budget_threshold'] }], documentFolders: [{ id: 'folder_65_1', name: 'FDA Submissions', category: 'Regulatory' }, { id: 'folder_65_2', name: 'Clinical Data', category: 'Evidence' }],
        reports: { useFirmSettings: true, originatingPct: 100, responsiblePct: 0 }, deleted: false, deletedAt: null
    },
    {
        id: 'matter_66', number: '00066', displayNumber: '00066-SierraNevada', description: 'Sierra Nevada Brewing - Distribution agreement and franchise licensing', status: 'closed', billingMethod: 'hourly', clientId: 'contact_20', responsibleAttorneyId: 'user_12', originatingAttorneyId: 'user_4', responsibleStaffId: 'user_14', clientReferenceNumber: 'CORP-2024-0045', location: 'California', practiceAreaId: 'pa_5', stageId: 'stage_5_4', openDate: '2024-11-05', pendingDate: '2025-06-01', closedDate: '2025-08-15', createdDate: '2024-11-04T09:45:00Z', templateId: 'template_4',
        permissions: { type: 'everyone', userIds: [], groupIds: [] }, blockedUsers: [],
        relationships: [], customFields: { cf_6: 'California' },
        billing: { billable: true, method: 'hourly', currency: 'USD', rates: [], budget: 30000, budgetUsed: 27800, trustBalance: 0, minimumTrust: 0, contingencyFee: null, flatRate: null },
        personalInjury: null,
        notifications: [], documentFolders: [{ id: 'folder_66_1', name: 'Distribution Agreements', category: 'Contracts' }],
        reports: { useFirmSettings: true, originatingPct: 50, responsiblePct: 50 }, deleted: false, deletedAt: null
    },
    {
        id: 'matter_67', number: '00067', displayNumber: '00067-TechVenture', description: 'TechVenture Capital - Fund formation and limited partnership agreements', status: 'open', billingMethod: 'hourly', clientId: 'contact_28', responsibleAttorneyId: 'user_4', originatingAttorneyId: 'user_12', responsibleStaffId: 'user_14', clientReferenceNumber: 'CORP-2024-0056', location: 'Delaware / California', practiceAreaId: 'pa_5', stageId: 'stage_5_3', openDate: '2024-01-18', pendingDate: null, closedDate: null, createdDate: '2024-01-17T14:00:00Z', templateId: 'template_4',
        permissions: { type: 'everyone', userIds: [], groupIds: [] }, blockedUsers: [],
        relationships: [], customFields: { cf_6: 'Delaware / California' },
        billing: { billable: true, method: 'hourly', currency: 'USD', rates: [{ userId: 'user_4', rate: 600 }], budget: 100000, budgetUsed: 78500, trustBalance: 8000, minimumTrust: 5000, contingencyFee: null, flatRate: null },
        personalInjury: null,
        notifications: [{ userId: 'user_4', types: ['budget_threshold'] }], documentFolders: [{ id: 'folder_67_1', name: 'Fund Documents', category: 'Corporate' }, { id: 'folder_67_2', name: 'LP Agreements', category: 'Contracts' }],
        reports: { useFirmSettings: false, originatingPct: 40, responsiblePct: 60 }, deleted: false, deletedAt: null
    },
    {
        id: 'matter_68', number: '00068', displayNumber: '00068-BayAreaConst', description: 'Bay Area Construction - Contractor licensing dispute and bond claim', status: 'pending', billingMethod: 'hourly', clientId: 'contact_7', responsibleAttorneyId: 'user_12', originatingAttorneyId: 'user_12', responsibleStaffId: 'user_14', clientReferenceNumber: 'CORP-2024-0067', location: 'CSLB / San Francisco County', practiceAreaId: 'pa_5', stageId: 'stage_5_3', openDate: '2024-06-08', pendingDate: '2025-08-01', closedDate: null, createdDate: '2024-06-07T10:30:00Z', templateId: 'template_4',
        permissions: { type: 'everyone', userIds: [], groupIds: [] }, blockedUsers: [],
        relationships: [], customFields: { cf_1: 'CSLB-2024-00567', cf_6: 'California' },
        billing: { billable: true, method: 'hourly', currency: 'USD', rates: [], budget: 20000, budgetUsed: 17800, trustBalance: 0, minimumTrust: 0, contingencyFee: null, flatRate: null },
        personalInjury: null,
        notifications: [], documentFolders: [{ id: 'folder_68_1', name: 'Licensing Documents', category: 'Regulatory' }],
        reports: { useFirmSettings: true, originatingPct: 100, responsiblePct: 0 }, deleted: false, deletedAt: null
    },
    {
        id: 'matter_69', number: '00069', displayNumber: '00069-MissionRestaurant', description: 'Mission District Restaurant Group - Multi-location franchise setup and employment compliance', status: 'open', billingMethod: 'hourly', clientId: 'contact_48', responsibleAttorneyId: 'user_12', originatingAttorneyId: 'user_1', responsibleStaffId: 'user_14', clientReferenceNumber: 'CORP-2024-0078', location: 'California', practiceAreaId: 'pa_5', stageId: 'stage_5_1', openDate: '2024-06-28', pendingDate: null, closedDate: null, createdDate: '2024-06-27T09:00:00Z', templateId: 'template_4',
        permissions: { type: 'everyone', userIds: [], groupIds: [] }, blockedUsers: [],
        relationships: [], customFields: { cf_6: 'California' },
        billing: { billable: true, method: 'hourly', currency: 'USD', rates: [], budget: 25000, budgetUsed: 15600, trustBalance: 4000, minimumTrust: 2500, contingencyFee: null, flatRate: null },
        personalInjury: null,
        notifications: [], documentFolders: [{ id: 'folder_69_1', name: 'Franchise Documents', category: 'Contracts' }, { id: 'folder_69_2', name: 'Employment Policies', category: 'Compliance' }],
        reports: { useFirmSettings: true, originatingPct: 50, responsiblePct: 50 }, deleted: false, deletedAt: null
    },
    {
        id: 'matter_70', number: '00070', displayNumber: '00070-RedwoodFinancial', description: 'Redwood Financial Services - SEC compliance audit and advisory opinions', status: 'open', billingMethod: 'hourly', clientId: 'contact_38', responsibleAttorneyId: 'user_4', originatingAttorneyId: 'user_4', responsibleStaffId: 'user_14', clientReferenceNumber: 'CORP-2024-0089', location: 'SEC / California', practiceAreaId: 'pa_5', stageId: 'stage_5_2', openDate: '2024-03-01', pendingDate: null, closedDate: null, createdDate: '2024-02-29T15:00:00Z', templateId: 'template_4',
        permissions: { type: 'specific', userIds: ['user_1', 'user_4', 'user_14'], groupIds: ['group_3'] }, blockedUsers: [],
        relationships: [], customFields: { cf_6: 'Federal / California' },
        billing: { billable: true, method: 'hourly', currency: 'USD', rates: [{ userId: 'user_4', rate: 600 }], budget: 80000, budgetUsed: 56700, trustBalance: 12000, minimumTrust: 8000, contingencyFee: null, flatRate: null },
        personalInjury: null,
        notifications: [{ userId: 'user_4', types: ['budget_threshold'] }], documentFolders: [{ id: 'folder_70_1', name: 'SEC Filings', category: 'Regulatory' }, { id: 'folder_70_2', name: 'Compliance Reports', category: 'Compliance' }],
        reports: { useFirmSettings: true, originatingPct: 100, responsiblePct: 0 }, deleted: false, deletedAt: null
    },
    {
        id: 'matter_71', number: '00071', displayNumber: '00071-PinnacleSoft', description: 'Pinnacle Software - SaaS licensing agreement and data privacy compliance', status: 'closed', billingMethod: 'hourly', clientId: 'contact_51', responsibleAttorneyId: 'user_12', originatingAttorneyId: 'user_4', responsibleStaffId: 'user_14', clientReferenceNumber: 'CORP-2024-0099', location: 'California', practiceAreaId: 'pa_5', stageId: 'stage_5_4', openDate: '2024-02-20', pendingDate: '2024-12-01', closedDate: '2025-01-15', createdDate: '2024-02-19T11:15:00Z', templateId: 'template_4',
        permissions: { type: 'everyone', userIds: [], groupIds: [] }, blockedUsers: [],
        relationships: [], customFields: { cf_6: 'California' },
        billing: { billable: true, method: 'hourly', currency: 'USD', rates: [], budget: 30000, budgetUsed: 24500, trustBalance: 2500, minimumTrust: 2000, contingencyFee: null, flatRate: null },
        personalInjury: null,
        notifications: [], documentFolders: [{ id: 'folder_71_1', name: 'License Agreements', category: 'Contracts' }, { id: 'folder_71_2', name: 'Privacy Policies', category: 'Compliance' }],
        reports: { useFirmSettings: true, originatingPct: 50, responsiblePct: 50 }, deleted: false, deletedAt: null
    },
    {
        id: 'matter_72', number: '00072', displayNumber: '00072-AlRashid', description: 'Al-Rashid & Partners - Partnership dissolution and asset distribution', status: 'pending', billingMethod: 'hourly', clientId: 'contact_23', responsibleAttorneyId: 'user_12', originatingAttorneyId: 'user_12', responsibleStaffId: 'user_14', clientReferenceNumber: 'CORP-2024-0101', location: 'Alameda County Superior Court', practiceAreaId: 'pa_5', stageId: 'stage_5_2', openDate: '2024-02-10', pendingDate: '2025-08-01', closedDate: null, createdDate: '2024-02-09T10:00:00Z', templateId: 'template_4',
        permissions: { type: 'everyone', userIds: [], groupIds: [] }, blockedUsers: [],
        relationships: [], customFields: { cf_1: 'AC-2024-CV-02345', cf_6: 'Alameda County' },
        billing: { billable: true, method: 'hourly', currency: 'USD', rates: [], budget: 35000, budgetUsed: 29800, trustBalance: 2000, minimumTrust: 2000, contingencyFee: null, flatRate: null },
        personalInjury: null,
        notifications: [], documentFolders: [{ id: 'folder_72_1', name: 'Partnership Documents', category: 'Corporate' }, { id: 'folder_72_2', name: 'Financial Records', category: 'Financial' }],
        reports: { useFirmSettings: true, originatingPct: 100, responsiblePct: 0 }, deleted: false, deletedAt: null
    },
    // === EMPLOYMENT LAW (8) ===
    {
        id: 'matter_73', number: '00073', displayNumber: '00073-Li', description: 'Li v. TechCorp Inc. - Gender discrimination and hostile work environment claim', status: 'open', billingMethod: 'contingency', clientId: 'contact_14', responsibleAttorneyId: 'user_16', originatingAttorneyId: 'user_1', responsibleStaffId: 'user_9', clientReferenceNumber: 'EMP-2024-0012', location: 'San Francisco County Superior Court', practiceAreaId: 'pa_6', stageId: 'stage_6_3', openDate: '2024-10-10', pendingDate: null, closedDate: null, createdDate: '2024-10-09T10:00:00Z', templateId: null,
        permissions: { type: 'everyone', userIds: [], groupIds: [] }, blockedUsers: [],
        relationships: [], customFields: { cf_1: 'SF-2024-CV-19567', cf_2: 'TechCorp Legal Dept', cf_6: 'San Francisco County' },
        billing: { billable: true, method: 'contingency', currency: 'USD', rates: [], budget: 40000, budgetUsed: 18900, trustBalance: 0, minimumTrust: 0, contingencyFee: { userId: 'user_16', percentage: 33.33 }, flatRate: null },
        personalInjury: null,
        notifications: [], documentFolders: [{ id: 'folder_73_1', name: 'EEOC Filings', category: 'Regulatory' }, { id: 'folder_73_2', name: 'Employment Records', category: 'Evidence' }],
        reports: { useFirmSettings: true, originatingPct: 50, responsiblePct: 50 }, deleted: false, deletedAt: null
    },
    {
        id: 'matter_74', number: '00074', displayNumber: '00074-Gutierrez', description: 'Gutierrez v. Bay Area Restaurant Group - Wage theft and unpaid overtime class action', status: 'open', billingMethod: 'contingency', clientId: 'contact_37', responsibleAttorneyId: 'user_16', originatingAttorneyId: 'user_16', responsibleStaffId: 'user_9', clientReferenceNumber: 'EMP-2024-0034', location: 'Northern District of California', practiceAreaId: 'pa_6', stageId: 'stage_6_4', openDate: '2024-06-15', pendingDate: null, closedDate: null, createdDate: '2024-06-14T14:30:00Z', templateId: null,
        permissions: { type: 'everyone', userIds: [], groupIds: [] }, blockedUsers: [],
        relationships: [], customFields: { cf_1: 'NDCA-2024-CV-06789', cf_2: 'Phillips & Associates', cf_6: 'Northern District of California' },
        billing: { billable: true, method: 'contingency', currency: 'USD', rates: [], budget: 80000, budgetUsed: 52300, trustBalance: 0, minimumTrust: 0, contingencyFee: { userId: 'user_16', percentage: 40 }, flatRate: null },
        personalInjury: null,
        notifications: [{ userId: 'user_16', types: ['matter_updates'] }], documentFolders: [{ id: 'folder_74_1', name: 'Payroll Records', category: 'Financial' }, { id: 'folder_74_2', name: 'Class Certification', category: 'Court' }],
        reports: { useFirmSettings: true, originatingPct: 100, responsiblePct: 0 }, deleted: false, deletedAt: null
    },
    {
        id: 'matter_75', number: '00075', displayNumber: '00075-Chang', description: 'Chang v. Pacific Healthcare - Wrongful termination after whistleblower complaint', status: 'open', billingMethod: 'contingency', clientId: 'contact_50', responsibleAttorneyId: 'user_16', originatingAttorneyId: 'user_1', responsibleStaffId: 'user_9', clientReferenceNumber: 'EMP-2024-0056', location: 'San Francisco County Superior Court', practiceAreaId: 'pa_6', stageId: 'stage_6_2', openDate: '2024-10-18', pendingDate: null, closedDate: null, createdDate: '2024-10-17T09:15:00Z', templateId: null,
        permissions: { type: 'everyone', userIds: [], groupIds: [] }, blockedUsers: [],
        relationships: [], customFields: { cf_2: 'Jackson Lewis LLP', cf_6: 'San Francisco County' },
        billing: { billable: true, method: 'contingency', currency: 'USD', rates: [], budget: 50000, budgetUsed: 12400, trustBalance: 0, minimumTrust: 0, contingencyFee: { userId: 'user_16', percentage: 33.33 }, flatRate: null },
        personalInjury: null,
        notifications: [], documentFolders: [{ id: 'folder_75_1', name: 'Employment Records', category: 'Evidence' }, { id: 'folder_75_2', name: 'Whistleblower Documentation', category: 'Evidence' }],
        reports: { useFirmSettings: true, originatingPct: 50, responsiblePct: 50 }, deleted: false, deletedAt: null
    },
    {
        id: 'matter_76', number: '00076', displayNumber: '00076-Petrovic', description: 'Petrovic v. Lakeside Management - Sexual harassment and retaliation claim', status: 'pending', billingMethod: 'contingency', clientId: 'contact_27', responsibleAttorneyId: 'user_16', originatingAttorneyId: 'user_16', responsibleStaffId: 'user_9', clientReferenceNumber: 'EMP-2024-0023', location: 'Alameda County Superior Court', practiceAreaId: 'pa_6', stageId: 'stage_6_5', openDate: '2024-07-02', pendingDate: '2025-11-15', closedDate: null, createdDate: '2024-07-01T11:00:00Z', templateId: null,
        permissions: { type: 'specific', userIds: ['user_1', 'user_16', 'user_9'], groupIds: [] }, blockedUsers: [],
        relationships: [], customFields: { cf_1: 'AC-2024-CV-11234', cf_2: 'Ogletree Deakins', cf_6: 'Alameda County' },
        billing: { billable: true, method: 'contingency', currency: 'USD', rates: [], budget: 35000, budgetUsed: 31200, trustBalance: 0, minimumTrust: 0, contingencyFee: { userId: 'user_16', percentage: 40 }, flatRate: null },
        personalInjury: null,
        notifications: [], documentFolders: [{ id: 'folder_76_1', name: 'EEOC Filings', category: 'Regulatory' }],
        reports: { useFirmSettings: true, originatingPct: 100, responsiblePct: 0 }, deleted: false, deletedAt: null
    },
    {
        id: 'matter_77', number: '00077', displayNumber: '00077-Petrovic-2', description: 'Petrovic Non-Compete Review - Analysis and challenge of overly broad non-compete clause', status: 'closed', billingMethod: 'hourly', clientId: 'contact_27', responsibleAttorneyId: 'user_10', originatingAttorneyId: 'user_16', responsibleStaffId: 'user_9', clientReferenceNumber: 'EMP-2024-0045', location: 'Alameda County', practiceAreaId: 'pa_6', stageId: 'stage_6_5', openDate: '2024-08-15', pendingDate: '2024-11-01', closedDate: '2025-01-10', createdDate: '2024-08-14T10:30:00Z', templateId: null,
        permissions: { type: 'everyone', userIds: [], groupIds: [] }, blockedUsers: [],
        relationships: [], customFields: { cf_6: 'Alameda County' },
        billing: { billable: true, method: 'hourly', currency: 'USD', rates: [], budget: 8000, budgetUsed: 7200, trustBalance: 0, minimumTrust: 0, contingencyFee: null, flatRate: null },
        personalInjury: null,
        notifications: [], documentFolders: [{ id: 'folder_77_1', name: 'Employment Contracts', category: 'Contracts' }],
        reports: { useFirmSettings: true, originatingPct: 50, responsiblePct: 50 }, deleted: false, deletedAt: null
    },
    {
        id: 'matter_78', number: '00078', displayNumber: '00078-Li-2', description: 'Li v. DataStream Analytics - Unpaid commission and breach of employment contract', status: 'open', billingMethod: 'hourly', clientId: 'contact_14', responsibleAttorneyId: 'user_10', originatingAttorneyId: 'user_16', responsibleStaffId: 'user_9', clientReferenceNumber: 'EMP-2025-0008', location: 'San Francisco County Superior Court', practiceAreaId: 'pa_6', stageId: 'stage_6_1', openDate: '2025-01-22', pendingDate: null, closedDate: null, createdDate: '2025-01-21T13:00:00Z', templateId: null,
        permissions: { type: 'everyone', userIds: [], groupIds: [] }, blockedUsers: [],
        relationships: [], customFields: { cf_6: 'San Francisco County' },
        billing: { billable: true, method: 'hourly', currency: 'USD', rates: [], budget: 15000, budgetUsed: 3400, trustBalance: 3000, minimumTrust: 2000, contingencyFee: null, flatRate: null },
        personalInjury: null,
        notifications: [], documentFolders: [{ id: 'folder_78_1', name: 'Employment Records', category: 'Evidence' }],
        reports: { useFirmSettings: true, originatingPct: 50, responsiblePct: 50 }, deleted: false, deletedAt: null
    },
    {
        id: 'matter_79', number: '00079', displayNumber: '00079-NovaBio-EMP', description: 'NovaBio Pharmaceuticals - Employee handbook revision and compliance with new CA labor laws', status: 'open', billingMethod: 'hourly', clientId: 'contact_17', responsibleAttorneyId: 'user_10', originatingAttorneyId: 'user_4', responsibleStaffId: 'user_9', clientReferenceNumber: 'EMP-2025-0015', location: 'California', practiceAreaId: 'pa_6', stageId: 'stage_6_1', openDate: '2025-02-01', pendingDate: null, closedDate: null, createdDate: '2025-01-31T09:30:00Z', templateId: null,
        permissions: { type: 'everyone', userIds: [], groupIds: [] }, blockedUsers: [],
        relationships: [], customFields: { cf_6: 'California' },
        billing: { billable: true, method: 'hourly', currency: 'USD', rates: [], budget: 12000, budgetUsed: 2800, trustBalance: 5000, minimumTrust: 3000, contingencyFee: null, flatRate: null },
        personalInjury: null,
        notifications: [], documentFolders: [{ id: 'folder_79_1', name: 'Policy Documents', category: 'Compliance' }],
        reports: { useFirmSettings: true, originatingPct: 50, responsiblePct: 50 }, deleted: false, deletedAt: null
    },
    {
        id: 'matter_80', number: '00080', displayNumber: '00080-MissionRestaurant-EMP', description: 'Mission District Restaurant Group - OSHA citation defense for kitchen safety violations', status: 'open', billingMethod: 'hourly', clientId: 'contact_48', responsibleAttorneyId: 'user_16', originatingAttorneyId: 'user_12', responsibleStaffId: 'user_9', clientReferenceNumber: 'EMP-2024-0067', location: 'OSHA / California', practiceAreaId: 'pa_6', stageId: 'stage_6_3', openDate: '2024-09-12', pendingDate: null, closedDate: null, createdDate: '2024-09-11T15:45:00Z', templateId: null,
        permissions: { type: 'everyone', userIds: [], groupIds: [] }, blockedUsers: [],
        relationships: [], customFields: { cf_1: 'OSHA-2024-SF-03456', cf_6: 'OSHA Region IX' },
        billing: { billable: true, method: 'hourly', currency: 'USD', rates: [], budget: 20000, budgetUsed: 14500, trustBalance: 2000, minimumTrust: 1500, contingencyFee: null, flatRate: null },
        personalInjury: null,
        notifications: [], documentFolders: [{ id: 'folder_80_1', name: 'OSHA Documents', category: 'Regulatory' }],
        reports: { useFirmSettings: true, originatingPct: 50, responsiblePct: 50 }, deleted: false, deletedAt: null
    },
    // === ESTATE PLANNING (6) ===
    {
        id: 'matter_81', number: '00081', displayNumber: '00081-Kowalski', description: 'Kowalski Estate Plan - Comprehensive will, trust, and power of attorney package', status: 'open', billingMethod: 'flat_rate', clientId: 'contact_8', responsibleAttorneyId: 'user_13', originatingAttorneyId: 'user_1', responsibleStaffId: 'user_11', clientReferenceNumber: 'EP-2024-0012', location: 'San Mateo County', practiceAreaId: 'pa_7', stageId: 'stage_7_2', openDate: '2024-07-18', pendingDate: null, closedDate: null, createdDate: '2024-07-17T09:00:00Z', templateId: 'template_6',
        permissions: { type: 'everyone', userIds: [], groupIds: [] }, blockedUsers: [],
        relationships: [], customFields: {},
        billing: { billable: true, method: 'flat_rate', currency: 'USD', rates: [], budget: 0, budgetUsed: 0, trustBalance: 3500, minimumTrust: 1500, contingencyFee: null, flatRate: { amount: 5000, recipientId: 'user_13' } },
        personalInjury: null,
        notifications: [], documentFolders: [{ id: 'folder_81_1', name: 'Wills', category: 'Estate' }, { id: 'folder_81_2', name: 'Trust Documents', category: 'Estate' }, { id: 'folder_81_3', name: 'Powers of Attorney', category: 'Estate' }],
        reports: { useFirmSettings: true, originatingPct: 50, responsiblePct: 50 }, deleted: false, deletedAt: null
    },
    {
        id: 'matter_82', number: '00082', displayNumber: '00082-Yamamoto', description: 'Yamamoto Living Trust - Revocable living trust with special needs provisions for disabled child', status: 'open', billingMethod: 'flat_rate', clientId: 'contact_19', responsibleAttorneyId: 'user_13', originatingAttorneyId: 'user_13', responsibleStaffId: 'user_11', clientReferenceNumber: 'EP-2024-0023', location: 'San Francisco County', practiceAreaId: 'pa_7', stageId: 'stage_7_1', openDate: '2024-08-18', pendingDate: null, closedDate: null, createdDate: '2024-08-17T11:30:00Z', templateId: 'template_6',
        permissions: { type: 'everyone', userIds: [], groupIds: [] }, blockedUsers: [],
        relationships: [], customFields: {},
        billing: { billable: true, method: 'flat_rate', currency: 'USD', rates: [], budget: 0, budgetUsed: 0, trustBalance: 6000, minimumTrust: 3000, contingencyFee: null, flatRate: { amount: 8500, recipientId: 'user_13' } },
        personalInjury: null,
        notifications: [], documentFolders: [{ id: 'folder_82_1', name: 'Trust Documents', category: 'Estate' }, { id: 'folder_82_2', name: 'Special Needs Trust', category: 'Estate' }],
        reports: { useFirmSettings: true, originatingPct: 100, responsiblePct: 0 }, deleted: false, deletedAt: null
    },
    {
        id: 'matter_83', number: '00083', displayNumber: '00083-Crawford', description: 'Crawford Estate Administration - Probate of $2.3M estate with contested beneficiaries', status: 'open', billingMethod: 'hourly', clientId: 'contact_39', responsibleAttorneyId: 'user_13', originatingAttorneyId: 'user_1', responsibleStaffId: 'user_11', clientReferenceNumber: 'EP-2024-0034', location: 'San Francisco Probate Court', practiceAreaId: 'pa_7', stageId: 'stage_7_2', openDate: '2024-10-05', pendingDate: null, closedDate: null, createdDate: '2024-10-04T14:00:00Z', templateId: 'template_6',
        permissions: { type: 'everyone', userIds: [], groupIds: [] }, blockedUsers: [],
        relationships: [], customFields: { cf_1: 'SF-2024-PR-00456' },
        billing: { billable: true, method: 'hourly', currency: 'USD', rates: [], budget: 30000, budgetUsed: 14500, trustBalance: 5000, minimumTrust: 3000, contingencyFee: null, flatRate: null },
        personalInjury: null,
        notifications: [], documentFolders: [{ id: 'folder_83_1', name: 'Probate Documents', category: 'Court' }, { id: 'folder_83_2', name: 'Asset Inventory', category: 'Financial' }],
        reports: { useFirmSettings: true, originatingPct: 50, responsiblePct: 50 }, deleted: false, deletedAt: null
    },
    {
        id: 'matter_84', number: '00084', displayNumber: '00084-Reed', description: 'Reed Estate Plan - Simple will and healthcare directive for retired veteran', status: 'closed', billingMethod: 'flat_rate', clientId: 'contact_52', responsibleAttorneyId: 'user_13', originatingAttorneyId: 'user_13', responsibleStaffId: 'user_11', clientReferenceNumber: 'EP-2024-0045', location: 'San Francisco County', practiceAreaId: 'pa_7', stageId: 'stage_7_3', openDate: '2024-07-12', pendingDate: '2024-09-01', closedDate: '2024-10-15', createdDate: '2024-07-11T10:00:00Z', templateId: 'template_6',
        permissions: { type: 'everyone', userIds: [], groupIds: [] }, blockedUsers: [],
        relationships: [], customFields: {},
        billing: { billable: true, method: 'flat_rate', currency: 'USD', rates: [], budget: 0, budgetUsed: 0, trustBalance: 0, minimumTrust: 0, contingencyFee: null, flatRate: { amount: 2500, recipientId: 'user_13' } },
        personalInjury: null,
        notifications: [], documentFolders: [{ id: 'folder_84_1', name: 'Estate Documents', category: 'Estate' }],
        reports: { useFirmSettings: true, originatingPct: 100, responsiblePct: 0 }, deleted: false, deletedAt: null
    },
    {
        id: 'matter_85', number: '00085', displayNumber: '00085-Morrison-EP', description: 'Morrison Family Trust Amendment - Updating trust to include new grandchildren', status: 'open', billingMethod: 'flat_rate', clientId: 'contact_41', responsibleAttorneyId: 'user_13', originatingAttorneyId: 'user_13', responsibleStaffId: 'user_11', clientReferenceNumber: 'EP-2025-0005', location: 'San Francisco County', practiceAreaId: 'pa_7', stageId: 'stage_7_1', openDate: '2025-01-15', pendingDate: null, closedDate: null, createdDate: '2025-01-14T09:00:00Z', templateId: 'template_6',
        permissions: { type: 'everyone', userIds: [], groupIds: [] }, blockedUsers: [],
        relationships: [], customFields: {},
        billing: { billable: true, method: 'flat_rate', currency: 'USD', rates: [], budget: 0, budgetUsed: 0, trustBalance: 2000, minimumTrust: 1000, contingencyFee: null, flatRate: { amount: 3500, recipientId: 'user_13' } },
        personalInjury: null,
        notifications: [], documentFolders: [{ id: 'folder_85_1', name: 'Trust Documents', category: 'Estate' }],
        reports: { useFirmSettings: true, originatingPct: 100, responsiblePct: 0 }, deleted: false, deletedAt: null
    },
    {
        id: 'matter_86', number: '00086', displayNumber: '00086-Yamamoto-2', description: 'Yamamoto Business Succession - Succession planning for family-owned import business', status: 'open', billingMethod: 'hourly', clientId: 'contact_19', responsibleAttorneyId: 'user_4', originatingAttorneyId: 'user_13', responsibleStaffId: 'user_14', clientReferenceNumber: 'EP-2025-0012', location: 'San Francisco County', practiceAreaId: 'pa_7', stageId: 'stage_7_1', openDate: '2025-02-10', pendingDate: null, closedDate: null, createdDate: '2025-02-09T10:30:00Z', templateId: 'template_6',
        permissions: { type: 'everyone', userIds: [], groupIds: [] }, blockedUsers: [],
        relationships: [{ contactId: 'contact_10', relationship: 'Employer', billRecipient: false }],
        customFields: {},
        billing: { billable: true, method: 'hourly', currency: 'USD', rates: [], budget: 20000, budgetUsed: 2100, trustBalance: 5000, minimumTrust: 3000, contingencyFee: null, flatRate: null },
        personalInjury: null,
        notifications: [], documentFolders: [{ id: 'folder_86_1', name: 'Succession Plan', category: 'Corporate' }, { id: 'folder_86_2', name: 'Trust Documents', category: 'Estate' }],
        reports: { useFirmSettings: true, originatingPct: 50, responsiblePct: 50 }, deleted: false, deletedAt: null
    },
    // === IMMIGRATION (5) ===
    {
        id: 'matter_87', number: '00087', displayNumber: '00087-Mbeki', description: 'Mbeki H-1B Visa - H-1B specialty occupation petition for software engineer', status: 'pending', billingMethod: 'flat_rate', clientId: 'contact_21', responsibleAttorneyId: 'user_10', originatingAttorneyId: 'user_1', responsibleStaffId: 'user_15', clientReferenceNumber: 'IMM-2024-0012', location: 'USCIS / California Service Center', practiceAreaId: 'pa_8', stageId: 'stage_8_3', openDate: '2024-04-25', pendingDate: '2025-06-01', closedDate: null, createdDate: '2024-04-24T10:00:00Z', templateId: null,
        permissions: { type: 'everyone', userIds: [], groupIds: [] }, blockedUsers: [],
        relationships: [], customFields: { cf_6: 'USCIS' },
        billing: { billable: true, method: 'flat_rate', currency: 'USD', rates: [], budget: 0, budgetUsed: 0, trustBalance: 3000, minimumTrust: 1500, contingencyFee: null, flatRate: { amount: 5000, recipientId: 'user_10' } },
        personalInjury: null,
        notifications: [], documentFolders: [{ id: 'folder_87_1', name: 'USCIS Forms', category: 'Immigration' }, { id: 'folder_87_2', name: 'Supporting Documents', category: 'Evidence' }],
        reports: { useFirmSettings: true, originatingPct: 50, responsiblePct: 50 }, deleted: false, deletedAt: null
    },
    {
        id: 'matter_88', number: '00088', displayNumber: '00088-Volkov', description: 'Volkov Asylum Application - Political asylum claim based on persecution in country of origin', status: 'open', billingMethod: 'hourly', clientId: 'contact_31', responsibleAttorneyId: 'user_10', originatingAttorneyId: 'user_10', responsibleStaffId: 'user_15', clientReferenceNumber: 'IMM-2024-0023', location: 'San Francisco Immigration Court', practiceAreaId: 'pa_8', stageId: 'stage_8_4', openDate: '2024-08-12', pendingDate: null, closedDate: null, createdDate: '2024-08-11T11:15:00Z', templateId: null,
        permissions: { type: 'specific', userIds: ['user_1', 'user_10', 'user_15'], groupIds: [] }, blockedUsers: [],
        relationships: [], customFields: { cf_1: 'A#-234-567-890', cf_6: 'EOIR / Immigration Court', cf_8: '2025-06-10' },
        billing: { billable: false, method: 'hourly', currency: 'USD', rates: [], budget: 0, budgetUsed: 0, trustBalance: 0, minimumTrust: 0, contingencyFee: null, flatRate: null },
        personalInjury: null,
        notifications: [{ userId: 'user_10', types: ['matter_updates'] }], documentFolders: [{ id: 'folder_88_1', name: 'Asylum Application', category: 'Immigration' }, { id: 'folder_88_2', name: 'Country Conditions', category: 'Evidence' }],
        reports: { useFirmSettings: true, originatingPct: 100, responsiblePct: 0 }, deleted: false, deletedAt: null
    },
    {
        id: 'matter_89', number: '00089', displayNumber: '00089-Tanaka', description: 'Tanaka Green Card - Employment-based EB-2 green card application with NIW waiver', status: 'open', billingMethod: 'flat_rate', clientId: 'contact_64', responsibleAttorneyId: 'user_10', originatingAttorneyId: 'user_1', responsibleStaffId: 'user_15', clientReferenceNumber: 'IMM-2025-0005', location: 'USCIS / Nebraska Service Center', practiceAreaId: 'pa_8', stageId: 'stage_8_2', openDate: '2025-01-22', pendingDate: null, closedDate: null, createdDate: '2025-01-21T09:45:00Z', templateId: null,
        permissions: { type: 'everyone', userIds: [], groupIds: [] }, blockedUsers: [],
        relationships: [], customFields: { cf_6: 'USCIS' },
        billing: { billable: true, method: 'flat_rate', currency: 'USD', rates: [], budget: 0, budgetUsed: 0, trustBalance: 5000, minimumTrust: 2500, contingencyFee: null, flatRate: { amount: 8000, recipientId: 'user_10' } },
        personalInjury: null,
        notifications: [], documentFolders: [{ id: 'folder_89_1', name: 'USCIS Forms', category: 'Immigration' }],
        reports: { useFirmSettings: true, originatingPct: 50, responsiblePct: 50 }, deleted: false, deletedAt: null
    },
    {
        id: 'matter_90', number: '00090', displayNumber: '00090-Mbeki-2', description: 'Mbeki Family Petition - I-130 family-based immigration petition for spouse', status: 'pending', billingMethod: 'flat_rate', clientId: 'contact_21', responsibleAttorneyId: 'user_10', originatingAttorneyId: 'user_10', responsibleStaffId: 'user_15', clientReferenceNumber: 'IMM-2024-0034', location: 'USCIS / California Service Center', practiceAreaId: 'pa_8', stageId: 'stage_8_4', openDate: '2024-06-15', pendingDate: '2025-04-01', closedDate: null, createdDate: '2024-06-14T13:00:00Z', templateId: null,
        permissions: { type: 'everyone', userIds: [], groupIds: [] }, blockedUsers: [],
        relationships: [], customFields: { cf_1: 'A#-234-567-891', cf_6: 'USCIS' },
        billing: { billable: true, method: 'flat_rate', currency: 'USD', rates: [], budget: 0, budgetUsed: 0, trustBalance: 1000, minimumTrust: 500, contingencyFee: null, flatRate: { amount: 3500, recipientId: 'user_10' } },
        personalInjury: null,
        notifications: [], documentFolders: [{ id: 'folder_90_1', name: 'USCIS Forms', category: 'Immigration' }],
        reports: { useFirmSettings: true, originatingPct: 100, responsiblePct: 0 }, deleted: false, deletedAt: null
    },
    {
        id: 'matter_91', number: '00091', displayNumber: '00091-Volkov-2', description: 'Volkov Work Authorization - Employment authorization document renewal while asylum pending', status: 'open', billingMethod: 'hourly', clientId: 'contact_31', responsibleAttorneyId: 'user_10', originatingAttorneyId: 'user_10', responsibleStaffId: 'user_15', clientReferenceNumber: 'IMM-2025-0012', location: 'USCIS / California Service Center', practiceAreaId: 'pa_8', stageId: 'stage_8_2', openDate: '2025-02-05', pendingDate: null, closedDate: null, createdDate: '2025-02-04T10:00:00Z', templateId: null,
        permissions: { type: 'specific', userIds: ['user_1', 'user_10', 'user_15'], groupIds: [] }, blockedUsers: [],
        relationships: [], customFields: { cf_1: 'A#-234-567-890', cf_6: 'USCIS' },
        billing: { billable: false, method: 'hourly', currency: 'USD', rates: [], budget: 0, budgetUsed: 0, trustBalance: 0, minimumTrust: 0, contingencyFee: null, flatRate: null },
        personalInjury: null,
        notifications: [], documentFolders: [{ id: 'folder_91_1', name: 'EAD Application', category: 'Immigration' }],
        reports: { useFirmSettings: true, originatingPct: 100, responsiblePct: 0 }, deleted: false, deletedAt: null
    },
    // === INTELLECTUAL PROPERTY (4) ===
    {
        id: 'matter_92', number: '00092', displayNumber: '00092-VertexTech-IP', description: 'Vertex Technologies - Patent application for AI-driven analytics platform', status: 'pending', billingMethod: 'hourly', clientId: 'contact_4', responsibleAttorneyId: 'user_12', originatingAttorneyId: 'user_4', responsibleStaffId: 'user_14', clientReferenceNumber: 'IP-2024-0012', location: 'USPTO', practiceAreaId: 'pa_9', stageId: 'stage_9_2', openDate: '2024-05-10', pendingDate: '2025-07-15', closedDate: null, createdDate: '2024-05-09T09:30:00Z', templateId: null,
        permissions: { type: 'everyone', userIds: [], groupIds: [] }, blockedUsers: [],
        relationships: [], customFields: { cf_1: 'USPTO-2024-APP-56789', cf_6: 'USPTO' },
        billing: { billable: true, method: 'hourly', currency: 'USD', rates: [], budget: 25000, budgetUsed: 18900, trustBalance: 3000, minimumTrust: 2000, contingencyFee: null, flatRate: null },
        personalInjury: null,
        notifications: [], documentFolders: [{ id: 'folder_92_1', name: 'Patent Application', category: 'IP' }, { id: 'folder_92_2', name: 'Prior Art', category: 'Research' }],
        reports: { useFirmSettings: true, originatingPct: 50, responsiblePct: 50 }, deleted: false, deletedAt: null
    },
    {
        id: 'matter_93', number: '00093', displayNumber: '00093-PinnacleSoft-IP', description: 'Pinnacle Software - Trademark registration for new product brand "CloudSync"', status: 'open', billingMethod: 'flat_rate', clientId: 'contact_51', responsibleAttorneyId: 'user_12', originatingAttorneyId: 'user_12', responsibleStaffId: 'user_14', clientReferenceNumber: 'IP-2024-0023', location: 'USPTO', practiceAreaId: 'pa_9', stageId: 'stage_9_1', openDate: '2024-08-20', pendingDate: null, closedDate: null, createdDate: '2024-08-19T14:00:00Z', templateId: null,
        permissions: { type: 'everyone', userIds: [], groupIds: [] }, blockedUsers: [],
        relationships: [], customFields: { cf_6: 'USPTO' },
        billing: { billable: true, method: 'flat_rate', currency: 'USD', rates: [], budget: 0, budgetUsed: 0, trustBalance: 2500, minimumTrust: 1000, contingencyFee: null, flatRate: { amount: 4000, recipientId: 'user_12' } },
        personalInjury: null,
        notifications: [], documentFolders: [{ id: 'folder_93_1', name: 'Trademark Application', category: 'IP' }],
        reports: { useFirmSettings: true, originatingPct: 100, responsiblePct: 0 }, deleted: false, deletedAt: null
    },
    {
        id: 'matter_94', number: '00094', displayNumber: '00094-NovaBio-IP', description: 'NovaBio v. GenericPharma Co. - Patent infringement litigation for drug formulation', status: 'open', billingMethod: 'hourly', clientId: 'contact_17', responsibleAttorneyId: 'user_4', originatingAttorneyId: 'user_4', responsibleStaffId: 'user_14', clientReferenceNumber: 'IP-2024-0034', location: 'Northern District of California', practiceAreaId: 'pa_9', stageId: 'stage_9_3', openDate: '2024-03-15', pendingDate: null, closedDate: null, createdDate: '2024-03-14T10:00:00Z', templateId: null,
        permissions: { type: 'specific', userIds: ['user_1', 'user_4', 'user_12', 'user_14'], groupIds: ['group_3'] }, blockedUsers: [],
        relationships: [], customFields: { cf_1: 'NDCA-2024-CV-03456', cf_2: 'Morrison Foerster LLP', cf_6: 'Northern District of California' },
        billing: { billable: true, method: 'hourly', currency: 'USD', rates: [{ userId: 'user_4', rate: 600 }], budget: 300000, budgetUsed: 187500, trustBalance: 25000, minimumTrust: 15000, contingencyFee: null, flatRate: null },
        personalInjury: null,
        notifications: [{ userId: 'user_4', types: ['matter_updates', 'budget_threshold'] }], documentFolders: [{ id: 'folder_94_1', name: 'Patent Documents', category: 'IP' }, { id: 'folder_94_2', name: 'Court Filings', category: 'Court' }],
        reports: { useFirmSettings: false, originatingPct: 100, responsiblePct: 0 }, deleted: false, deletedAt: null
    },
    {
        id: 'matter_95', number: '00095', displayNumber: '00095-Kim-IP', description: 'Kim v. CopyCat Studios - Copyright infringement claim for mobile app design', status: 'pending', billingMethod: 'contingency', clientId: 'contact_43', responsibleAttorneyId: 'user_12', originatingAttorneyId: 'user_1', responsibleStaffId: 'user_14', clientReferenceNumber: 'IP-2024-0045', location: 'Northern District of California', practiceAreaId: 'pa_9', stageId: 'stage_9_3', openDate: '2024-12-01', pendingDate: '2025-11-01', closedDate: null, createdDate: '2024-11-30T09:00:00Z', templateId: null,
        permissions: { type: 'everyone', userIds: [], groupIds: [] }, blockedUsers: [],
        relationships: [], customFields: { cf_1: 'NDCA-2024-CV-10345', cf_2: 'Fenwick & West', cf_6: 'Northern District of California' },
        billing: { billable: true, method: 'contingency', currency: 'USD', rates: [], budget: 50000, budgetUsed: 34200, trustBalance: 0, minimumTrust: 0, contingencyFee: { userId: 'user_12', percentage: 33.33 }, flatRate: null },
        personalInjury: null,
        notifications: [], documentFolders: [{ id: 'folder_95_1', name: 'Copyright Registration', category: 'IP' }, { id: 'folder_95_2', name: 'Court Filings', category: 'Court' }],
        reports: { useFirmSettings: true, originatingPct: 50, responsiblePct: 50 }, deleted: false, deletedAt: null
    },
    // === BANKRUPTCY (4) ===
    {
        id: 'matter_96', number: '00096', displayNumber: '00096-BayLogistics', description: 'Bay Logistics International - Chapter 11 reorganization with complex international creditors', status: 'open', billingMethod: 'hourly', clientId: 'contact_34', responsibleAttorneyId: 'user_4', originatingAttorneyId: 'user_12', responsibleStaffId: 'user_14', clientReferenceNumber: 'BK-2024-0012', location: 'Northern District of California Bankruptcy Court', practiceAreaId: 'pa_10', stageId: 'stage_10_4', openDate: '2024-04-15', pendingDate: null, closedDate: null, createdDate: '2024-04-14T09:00:00Z', templateId: null,
        permissions: { type: 'everyone', userIds: [], groupIds: [] }, blockedUsers: [],
        relationships: [], customFields: { cf_1: 'NDCA-BK-2024-01234', cf_6: 'NDCA Bankruptcy Court' },
        billing: { billable: true, method: 'hourly', currency: 'USD', rates: [{ userId: 'user_4', rate: 575 }], budget: 150000, budgetUsed: 112300, trustBalance: 15000, minimumTrust: 10000, contingencyFee: null, flatRate: null },
        personalInjury: null,
        notifications: [{ userId: 'user_4', types: ['matter_updates', 'budget_threshold'] }], documentFolders: [{ id: 'folder_96_1', name: 'Petition', category: 'Court' }, { id: 'folder_96_2', name: 'Creditor Lists', category: 'Financial' }],
        reports: { useFirmSettings: true, originatingPct: 50, responsiblePct: 50 }, deleted: false, deletedAt: null
    },
    {
        id: 'matter_97', number: '00097', displayNumber: '00097-Kim-BK', description: 'Kim Chapter 7 - Individual Chapter 7 bankruptcy filing for failed startup founder', status: 'closed', billingMethod: 'flat_rate', clientId: 'contact_43', responsibleAttorneyId: 'user_14', originatingAttorneyId: 'user_12', responsibleStaffId: 'user_15', clientReferenceNumber: 'BK-2024-0023', location: 'Northern District of California Bankruptcy Court', practiceAreaId: 'pa_10', stageId: 'stage_10_5', openDate: '2024-12-05', pendingDate: '2025-04-01', closedDate: '2025-06-30', createdDate: '2024-12-04T10:30:00Z', templateId: null,
        permissions: { type: 'everyone', userIds: [], groupIds: [] }, blockedUsers: [],
        relationships: [], customFields: { cf_1: 'NDCA-BK-2024-05678', cf_6: 'NDCA Bankruptcy Court' },
        billing: { billable: true, method: 'flat_rate', currency: 'USD', rates: [], budget: 0, budgetUsed: 0, trustBalance: 0, minimumTrust: 0, contingencyFee: null, flatRate: { amount: 3500, recipientId: 'user_14' } },
        personalInjury: null,
        notifications: [], documentFolders: [{ id: 'folder_97_1', name: 'Bankruptcy Petition', category: 'Court' }],
        reports: { useFirmSettings: true, originatingPct: 50, responsiblePct: 50 }, deleted: false, deletedAt: null
    },
    {
        id: 'matter_98', number: '00098', displayNumber: '00098-Hernandez-BK', description: 'Hernandez Chapter 13 - Chapter 13 wage earner plan with mortgage arrearage', status: 'open', billingMethod: 'flat_rate', clientId: 'contact_29', responsibleAttorneyId: 'user_14', originatingAttorneyId: 'user_14', responsibleStaffId: 'user_15', clientReferenceNumber: 'BK-2025-0005', location: 'Northern District of California Bankruptcy Court', practiceAreaId: 'pa_10', stageId: 'stage_10_2', openDate: '2025-02-01', pendingDate: null, closedDate: null, createdDate: '2025-01-31T14:00:00Z', templateId: null,
        permissions: { type: 'everyone', userIds: [], groupIds: [] }, blockedUsers: [],
        relationships: [], customFields: { cf_6: 'NDCA Bankruptcy Court' },
        billing: { billable: true, method: 'flat_rate', currency: 'USD', rates: [], budget: 0, budgetUsed: 0, trustBalance: 2500, minimumTrust: 1500, contingencyFee: null, flatRate: { amount: 4500, recipientId: 'user_14' } },
        personalInjury: null,
        notifications: [], documentFolders: [{ id: 'folder_98_1', name: 'Bankruptcy Petition', category: 'Court' }],
        reports: { useFirmSettings: true, originatingPct: 100, responsiblePct: 0 }, deleted: false, deletedAt: null
    },
    {
        id: 'matter_99', number: '00099', displayNumber: '00099-MissionRestaurant-BK', description: 'Mission District Restaurant Group - Chapter 11 subchapter V small business reorganization', status: 'open', billingMethod: 'hourly', clientId: 'contact_48', responsibleAttorneyId: 'user_4', originatingAttorneyId: 'user_4', responsibleStaffId: 'user_14', clientReferenceNumber: 'BK-2025-0012', location: 'Northern District of California Bankruptcy Court', practiceAreaId: 'pa_10', stageId: 'stage_10_1', openDate: '2025-02-15', pendingDate: null, closedDate: null, createdDate: '2025-02-14T09:00:00Z', templateId: null,
        permissions: { type: 'everyone', userIds: [], groupIds: [] }, blockedUsers: [],
        relationships: [], customFields: { cf_6: 'NDCA Bankruptcy Court' },
        billing: { billable: true, method: 'hourly', currency: 'USD', rates: [{ userId: 'user_4', rate: 575 }], budget: 60000, budgetUsed: 3400, trustBalance: 10000, minimumTrust: 5000, contingencyFee: null, flatRate: null },
        personalInjury: null,
        notifications: [{ userId: 'user_4', types: ['matter_updates'] }], documentFolders: [{ id: 'folder_99_1', name: 'Financial Statements', category: 'Financial' }],
        reports: { useFirmSettings: true, originatingPct: 100, responsiblePct: 0 }, deleted: false, deletedAt: null
    },
    // === TAX LAW (4) ===
    {
        id: 'matter_100', number: '00100', displayNumber: '00100-RedwoodFinancial-Tax', description: 'Redwood Financial - IRS audit defense for corporate tax returns 2021-2023', status: 'pending', billingMethod: 'hourly', clientId: 'contact_38', responsibleAttorneyId: 'user_4', originatingAttorneyId: 'user_4', responsibleStaffId: 'user_14', clientReferenceNumber: 'TAX-2024-0012', location: 'IRS / California', practiceAreaId: 'pa_11', stageId: 'stage_11_3', openDate: '2024-06-01', pendingDate: '2025-11-01', closedDate: null, createdDate: '2024-05-31T09:00:00Z', templateId: null,
        permissions: { type: 'specific', userIds: ['user_1', 'user_4', 'user_14'], groupIds: ['group_3'] }, blockedUsers: [],
        relationships: [], customFields: { cf_6: 'IRS / Federal' },
        billing: { billable: true, method: 'hourly', currency: 'USD', rates: [{ userId: 'user_4', rate: 600 }], budget: 50000, budgetUsed: 34500, trustBalance: 8000, minimumTrust: 5000, contingencyFee: null, flatRate: null },
        personalInjury: null,
        notifications: [{ userId: 'user_4', types: ['budget_threshold'] }], documentFolders: [{ id: 'folder_100_1', name: 'Tax Returns', category: 'Financial' }, { id: 'folder_100_2', name: 'IRS Correspondence', category: 'Correspondence' }],
        reports: { useFirmSettings: true, originatingPct: 100, responsiblePct: 0 }, deleted: false, deletedAt: null
    },
    {
        id: 'matter_101', number: '00101', displayNumber: '00101-PacificRim-Tax', description: 'Pacific Rim Imports - International tax planning and transfer pricing analysis', status: 'pending', billingMethod: 'hourly', clientId: 'contact_10', responsibleAttorneyId: 'user_4', originatingAttorneyId: 'user_12', responsibleStaffId: 'user_14', clientReferenceNumber: 'TAX-2024-0023', location: 'IRS / California / International', practiceAreaId: 'pa_11', stageId: 'stage_11_2', openDate: '2024-09-15', pendingDate: '2025-10-15', closedDate: null, createdDate: '2024-09-14T11:00:00Z', templateId: null,
        permissions: { type: 'everyone', userIds: [], groupIds: [] }, blockedUsers: [],
        relationships: [], customFields: { cf_6: 'IRS / International' },
        billing: { billable: true, method: 'hourly', currency: 'USD', rates: [], budget: 35000, budgetUsed: 18700, trustBalance: 5000, minimumTrust: 3000, contingencyFee: null, flatRate: null },
        personalInjury: null,
        notifications: [], documentFolders: [{ id: 'folder_101_1', name: 'Tax Analysis', category: 'Financial' }],
        reports: { useFirmSettings: true, originatingPct: 50, responsiblePct: 50 }, deleted: false, deletedAt: null
    },
    {
        id: 'matter_102', number: '00102', displayNumber: '00102-Kim-Tax', description: 'Kim State Tax Appeal - California FTB assessment appeal for unreported income', status: 'pending', billingMethod: 'hourly', clientId: 'contact_43', responsibleAttorneyId: 'user_14', originatingAttorneyId: 'user_4', responsibleStaffId: 'user_15', clientReferenceNumber: 'TAX-2024-0034', location: 'California FTB / OTA', practiceAreaId: 'pa_11', stageId: 'stage_11_4', openDate: '2024-10-20', pendingDate: '2025-08-01', closedDate: null, createdDate: '2024-10-19T10:30:00Z', templateId: null,
        permissions: { type: 'everyone', userIds: [], groupIds: [] }, blockedUsers: [],
        relationships: [], customFields: { cf_6: 'California FTB' },
        billing: { billable: true, method: 'hourly', currency: 'USD', rates: [], budget: 15000, budgetUsed: 12800, trustBalance: 0, minimumTrust: 0, contingencyFee: null, flatRate: null },
        personalInjury: null,
        notifications: [], documentFolders: [{ id: 'folder_102_1', name: 'Tax Returns', category: 'Financial' }, { id: 'folder_102_2', name: 'FTB Correspondence', category: 'Correspondence' }],
        reports: { useFirmSettings: true, originatingPct: 50, responsiblePct: 50 }, deleted: false, deletedAt: null
    },
    {
        id: 'matter_103', number: '00103', displayNumber: '00103-SierraNevada-Tax', description: 'Sierra Nevada Brewing - Sales tax compliance for multi-state distribution operations', status: 'closed', billingMethod: 'hourly', clientId: 'contact_20', responsibleAttorneyId: 'user_14', originatingAttorneyId: 'user_12', responsibleStaffId: 'user_15', clientReferenceNumber: 'TAX-2024-0045', location: 'California / Multi-state', practiceAreaId: 'pa_11', stageId: 'stage_11_4', openDate: '2024-03-10', pendingDate: '2024-08-01', closedDate: '2024-10-30', createdDate: '2024-03-09T09:00:00Z', templateId: null,
        permissions: { type: 'everyone', userIds: [], groupIds: [] }, blockedUsers: [],
        relationships: [], customFields: { cf_6: 'Multi-state' },
        billing: { billable: true, method: 'hourly', currency: 'USD', rates: [], budget: 20000, budgetUsed: 18500, trustBalance: 0, minimumTrust: 0, contingencyFee: null, flatRate: null },
        personalInjury: null,
        notifications: [], documentFolders: [{ id: 'folder_103_1', name: 'Sales Tax Records', category: 'Financial' }],
        reports: { useFirmSettings: true, originatingPct: 50, responsiblePct: 50 }, deleted: false, deletedAt: null
    },
    // === MEDICAL MALPRACTICE (additional, beyond 14 & 15 above) (3) ===
    {
        id: 'matter_104', number: '00104', displayNumber: '00104-Gonzalez-MedMal', description: 'Gonzalez v. Bay Area Surgical Center - Nerve damage from botched carpal tunnel surgery', status: 'open', billingMethod: 'contingency', clientId: 'contact_2', responsibleAttorneyId: 'user_8', originatingAttorneyId: 'user_2', responsibleStaffId: 'user_7', clientReferenceNumber: 'MM-2025-0023', location: 'Santa Clara County Superior Court', practiceAreaId: 'pa_12', stageId: 'stage_12_2', openDate: '2025-01-05', pendingDate: null, closedDate: null, createdDate: '2025-01-04T14:30:00Z', templateId: 'template_1',
        permissions: { type: 'everyone', userIds: [], groupIds: [] }, blockedUsers: [],
        relationships: [], customFields: { cf_2: 'CIGA Defense Panel', cf_3: '2027-01-01', cf_4: 'CIGA/ProAssurance', cf_5: '1000000', cf_12: '2024-07-15' },
        billing: { billable: true, method: 'contingency', currency: 'USD', rates: [], budget: 100000, budgetUsed: 8900, trustBalance: 0, minimumTrust: 0, contingencyFee: { userId: 'user_8', percentage: 40 }, flatRate: null },
        personalInjury: { deductionOrder: 'fees_first' },
        notifications: [], documentFolders: [{ id: 'folder_104_1', name: 'Medical Records', category: 'Medical' }, { id: 'folder_104_2', name: 'Expert Reports', category: 'Expert' }],
        reports: { useFirmSettings: true, originatingPct: 50, responsiblePct: 50 }, deleted: false, deletedAt: null
    },
    {
        id: 'matter_105', number: '00105', displayNumber: '00105-Crawford-MedMal', description: 'Crawford v. UCSF Medical Center - Failure to diagnose pulmonary embolism in ER', status: 'closed', billingMethod: 'contingency', clientId: 'contact_39', responsibleAttorneyId: 'user_2', originatingAttorneyId: 'user_1', responsibleStaffId: 'user_7', clientReferenceNumber: 'MM-2024-0056', location: 'San Francisco County Superior Court', practiceAreaId: 'pa_12', stageId: 'stage_12_5', openDate: '2024-03-01', pendingDate: '2025-01-15', closedDate: '2025-03-20', createdDate: '2024-02-29T10:00:00Z', templateId: 'template_1',
        permissions: { type: 'everyone', userIds: [], groupIds: [] }, blockedUsers: [],
        relationships: [], customFields: { cf_1: 'SF-2024-CV-04567', cf_2: 'UC Legal Department', cf_3: '2025-02-28', cf_4: 'UC Self-Insured', cf_5: '0', cf_12: '2023-03-01' },
        billing: { billable: true, method: 'contingency', currency: 'USD', rates: [], budget: 120000, budgetUsed: 98700, trustBalance: 0, minimumTrust: 0, contingencyFee: { userId: 'user_2', percentage: 40 }, flatRate: null },
        personalInjury: { deductionOrder: 'fees_first' },
        notifications: [], documentFolders: [{ id: 'folder_105_1', name: 'Medical Records', category: 'Medical' }, { id: 'folder_105_2', name: 'Settlement', category: 'Settlement' }],
        reports: { useFirmSettings: true, originatingPct: 50, responsiblePct: 50 }, deleted: false, deletedAt: null
    },
    {
        id: 'matter_106', number: '00106', displayNumber: '00106-Whitfield-MedMal', description: 'Whitfield v. Pacific Heights Dental - Permanent numbness from negligent wisdom tooth extraction', status: 'open', billingMethod: 'contingency', clientId: 'contact_61', responsibleAttorneyId: 'user_5', originatingAttorneyId: 'user_2', responsibleStaffId: 'user_9', clientReferenceNumber: 'MM-2025-0034', location: 'San Francisco County Superior Court', practiceAreaId: 'pa_12', stageId: 'stage_12_1', openDate: '2025-02-20', pendingDate: null, closedDate: null, createdDate: '2025-02-19T11:00:00Z', templateId: 'template_1',
        permissions: { type: 'everyone', userIds: [], groupIds: [] }, blockedUsers: [],
        relationships: [], customFields: { cf_3: '2026-08-15', cf_12: '2024-08-15' },
        billing: { billable: true, method: 'contingency', currency: 'USD', rates: [], budget: 0, budgetUsed: 1200, trustBalance: 0, minimumTrust: 0, contingencyFee: { userId: 'user_5', percentage: 33.33 }, flatRate: null },
        personalInjury: { deductionOrder: 'fees_first' },
        notifications: [], documentFolders: [{ id: 'folder_106_1', name: 'Dental Records', category: 'Medical' }],
        reports: { useFirmSettings: true, originatingPct: 50, responsiblePct: 50 }, deleted: false, deletedAt: null
    },
    // === ENVIRONMENTAL LAW (3) ===
    {
        id: 'matter_107', number: '00107', displayNumber: '00107-BayAreaConst-ENV', description: 'Bay Area Construction - CEQA compliance for new waterfront development project', status: 'open', billingMethod: 'hourly', clientId: 'contact_7', responsibleAttorneyId: 'user_12', originatingAttorneyId: 'user_4', responsibleStaffId: 'user_14', clientReferenceNumber: 'ENV-2024-0012', location: 'California / San Francisco County', practiceAreaId: 'pa_13', stageId: 'stage_13_2', openDate: '2024-07-15', pendingDate: null, closedDate: null, createdDate: '2024-07-14T10:00:00Z', templateId: null,
        permissions: { type: 'everyone', userIds: [], groupIds: [] }, blockedUsers: [],
        relationships: [], customFields: { cf_6: 'California / San Francisco' },
        billing: { billable: true, method: 'hourly', currency: 'USD', rates: [], budget: 45000, budgetUsed: 28900, trustBalance: 5000, minimumTrust: 3000, contingencyFee: null, flatRate: null },
        personalInjury: null,
        notifications: [], documentFolders: [{ id: 'folder_107_1', name: 'Environmental Reports', category: 'Regulatory' }, { id: 'folder_107_2', name: 'CEQA Documents', category: 'Regulatory' }],
        reports: { useFirmSettings: true, originatingPct: 50, responsiblePct: 50 }, deleted: false, deletedAt: null
    },
    {
        id: 'matter_108', number: '00108', displayNumber: '00108-GoldenGateProperties-ENV', description: 'Golden Gate Properties - Soil contamination remediation compliance for Ferry Building parcel', status: 'pending', billingMethod: 'hourly', clientId: 'contact_13', responsibleAttorneyId: 'user_12', originatingAttorneyId: 'user_13', responsibleStaffId: 'user_14', clientReferenceNumber: 'ENV-2024-0023', location: 'DTSC / San Francisco County', practiceAreaId: 'pa_13', stageId: 'stage_13_2', openDate: '2024-03-20', pendingDate: '2025-06-01', closedDate: null, createdDate: '2024-03-19T14:30:00Z', templateId: null,
        permissions: { type: 'everyone', userIds: [], groupIds: [] }, blockedUsers: [],
        relationships: [], customFields: { cf_6: 'DTSC / California' },
        billing: { billable: true, method: 'hourly', currency: 'USD', rates: [], budget: 60000, budgetUsed: 48700, trustBalance: 2000, minimumTrust: 2000, contingencyFee: null, flatRate: null },
        personalInjury: null,
        notifications: [], documentFolders: [{ id: 'folder_108_1', name: 'Remediation Plans', category: 'Regulatory' }],
        reports: { useFirmSettings: true, originatingPct: 50, responsiblePct: 50 }, deleted: false, deletedAt: null
    },
    {
        id: 'matter_109', number: '00109', displayNumber: '00109-SierraNevada-ENV', description: 'Sierra Nevada Brewing - Wastewater discharge permit renewal and EPA compliance', status: 'closed', billingMethod: 'hourly', clientId: 'contact_20', responsibleAttorneyId: 'user_12', originatingAttorneyId: 'user_12', responsibleStaffId: 'user_14', clientReferenceNumber: 'ENV-2024-0034', location: 'EPA Region IX / California', practiceAreaId: 'pa_13', stageId: 'stage_13_2', openDate: '2024-05-01', pendingDate: '2024-10-15', closedDate: '2024-12-20', createdDate: '2024-04-30T09:00:00Z', templateId: null,
        permissions: { type: 'everyone', userIds: [], groupIds: [] }, blockedUsers: [],
        relationships: [], customFields: { cf_6: 'EPA / California SWRCB' },
        billing: { billable: true, method: 'hourly', currency: 'USD', rates: [], budget: 25000, budgetUsed: 22800, trustBalance: 0, minimumTrust: 0, contingencyFee: null, flatRate: null },
        personalInjury: null,
        notifications: [], documentFolders: [{ id: 'folder_109_1', name: 'Permit Documents', category: 'Regulatory' }],
        reports: { useFirmSettings: true, originatingPct: 100, responsiblePct: 0 }, deleted: false, deletedAt: null
    },
    // === ADDITIONAL MIXED MATTERS (110-120) ===
    {
        id: 'matter_110', number: '00110', displayNumber: '00110-VertexTech-EMP', description: 'Vertex Technologies - Executive employment agreement negotiation and equity compensation', status: 'open', billingMethod: 'hourly', clientId: 'contact_4', responsibleAttorneyId: 'user_10', originatingAttorneyId: 'user_4', responsibleStaffId: 'user_14', clientReferenceNumber: 'EMP-2025-0023', location: 'California', practiceAreaId: 'pa_6', stageId: 'stage_6_1', openDate: '2025-02-28', pendingDate: null, closedDate: null, createdDate: '2025-02-27T09:30:00Z', templateId: null,
        permissions: { type: 'everyone', userIds: [], groupIds: [] }, blockedUsers: [],
        relationships: [], customFields: { cf_6: 'California' },
        billing: { billable: true, method: 'hourly', currency: 'USD', rates: [], budget: 10000, budgetUsed: 500, trustBalance: 5000, minimumTrust: 2500, contingencyFee: null, flatRate: null },
        personalInjury: null,
        notifications: [], documentFolders: [{ id: 'folder_110_1', name: 'Employment Agreements', category: 'Contracts' }],
        reports: { useFirmSettings: true, originatingPct: 50, responsiblePct: 50 }, deleted: false, deletedAt: null
    },
    {
        id: 'matter_111', number: '00111', displayNumber: '00111-TechVenture-2', description: 'TechVenture Capital - Portfolio company acquisition due diligence and closing', status: 'open', billingMethod: 'hourly', clientId: 'contact_28', responsibleAttorneyId: 'user_12', originatingAttorneyId: 'user_4', responsibleStaffId: 'user_14', clientReferenceNumber: 'CORP-2025-0012', location: 'Delaware / California', practiceAreaId: 'pa_5', stageId: 'stage_5_1', openDate: '2025-02-18', pendingDate: null, closedDate: null, createdDate: '2025-02-17T11:00:00Z', templateId: 'template_4',
        permissions: { type: 'everyone', userIds: [], groupIds: [] }, blockedUsers: [],
        relationships: [], customFields: { cf_6: 'Delaware / California' },
        billing: { billable: true, method: 'hourly', currency: 'USD', rates: [], budget: 80000, budgetUsed: 3200, trustBalance: 15000, minimumTrust: 10000, contingencyFee: null, flatRate: null },
        personalInjury: null,
        notifications: [], documentFolders: [{ id: 'folder_111_1', name: 'Due Diligence', category: 'Corporate' }],
        reports: { useFirmSettings: true, originatingPct: 50, responsiblePct: 50 }, deleted: false, deletedAt: null
    },
    {
        id: 'matter_112', number: '00112', displayNumber: '00112-Tanaka-FL', description: 'Tanaka Spousal Visa - Adjustment of status for spouse of H-1B holder', status: 'open', billingMethod: 'flat_rate', clientId: 'contact_64', responsibleAttorneyId: 'user_10', originatingAttorneyId: 'user_10', responsibleStaffId: 'user_15', clientReferenceNumber: 'IMM-2025-0018', location: 'USCIS', practiceAreaId: 'pa_8', stageId: 'stage_8_1', openDate: '2025-03-01', pendingDate: null, closedDate: null, createdDate: '2025-02-28T10:00:00Z', templateId: null,
        permissions: { type: 'everyone', userIds: [], groupIds: [] }, blockedUsers: [],
        relationships: [], customFields: { cf_6: 'USCIS' },
        billing: { billable: true, method: 'flat_rate', currency: 'USD', rates: [], budget: 0, budgetUsed: 0, trustBalance: 3000, minimumTrust: 1500, contingencyFee: null, flatRate: { amount: 4500, recipientId: 'user_10' } },
        personalInjury: null,
        notifications: [], documentFolders: [{ id: 'folder_112_1', name: 'USCIS Forms', category: 'Immigration' }],
        reports: { useFirmSettings: true, originatingPct: 100, responsiblePct: 0 }, deleted: false, deletedAt: null
    },
    {
        id: 'matter_113', number: '00113', displayNumber: '00113-Andersen-RE2', description: 'Andersen Commercial Lease - Triple-net lease negotiation for retail storefront', status: 'open', billingMethod: 'hourly', clientId: 'contact_69', responsibleAttorneyId: 'user_6', originatingAttorneyId: 'user_13', responsibleStaffId: 'user_7', clientReferenceNumber: 'RE-2025-0022', location: 'San Francisco County', practiceAreaId: 'pa_4', stageId: 'stage_4_2', openDate: '2025-02-25', pendingDate: null, closedDate: null, createdDate: '2025-02-24T14:00:00Z', templateId: 'template_5',
        permissions: { type: 'everyone', userIds: [], groupIds: [] }, blockedUsers: [],
        relationships: [], customFields: { cf_6: 'San Francisco County' },
        billing: { billable: true, method: 'hourly', currency: 'USD', rates: [], budget: 8000, budgetUsed: 900, trustBalance: 3000, minimumTrust: 1500, contingencyFee: null, flatRate: null },
        personalInjury: null,
        notifications: [], documentFolders: [{ id: 'folder_113_1', name: 'Lease Documents', category: 'Contracts' }],
        reports: { useFirmSettings: true, originatingPct: 50, responsiblePct: 50 }, deleted: false, deletedAt: null
    },
    {
        id: 'matter_114', number: '00114', displayNumber: '00114-Washington-2', description: 'Washington v. PremiumHealth Insurance - Insurance bad faith denial of medical coverage claim', status: 'open', billingMethod: 'contingency', clientId: 'contact_12', responsibleAttorneyId: 'user_16', originatingAttorneyId: 'user_8', responsibleStaffId: 'user_9', clientReferenceNumber: 'INS-2024-0023', location: 'San Francisco County Superior Court', practiceAreaId: 'pa_1', stageId: 'stage_1_3', openDate: '2024-11-05', pendingDate: null, closedDate: null, createdDate: '2024-11-04T10:00:00Z', templateId: null,
        permissions: { type: 'everyone', userIds: [], groupIds: [] }, blockedUsers: [],
        relationships: [], customFields: { cf_1: 'SF-2024-CV-21345', cf_2: 'PremiumHealth Legal Dept', cf_6: 'San Francisco County' },
        billing: { billable: true, method: 'contingency', currency: 'USD', rates: [], budget: 30000, budgetUsed: 11200, trustBalance: 0, minimumTrust: 0, contingencyFee: { userId: 'user_16', percentage: 33.33 }, flatRate: null },
        personalInjury: null,
        notifications: [], documentFolders: [{ id: 'folder_114_1', name: 'Insurance Documents', category: 'Evidence' }],
        reports: { useFirmSettings: true, originatingPct: 50, responsiblePct: 50 }, deleted: false, deletedAt: null
    },
    {
        id: 'matter_115', number: '00115', displayNumber: '00115-NovaBio-Corp2', description: 'NovaBio Pharmaceuticals - Board governance restructuring and bylaw amendments', status: 'open', billingMethod: 'hourly', clientId: 'contact_17', responsibleAttorneyId: 'user_4', originatingAttorneyId: 'user_4', responsibleStaffId: 'user_14', clientReferenceNumber: 'CORP-2025-0023', location: 'Delaware', practiceAreaId: 'pa_5', stageId: 'stage_5_1', openDate: '2025-01-10', pendingDate: null, closedDate: null, createdDate: '2025-01-09T09:00:00Z', templateId: 'template_4',
        permissions: { type: 'specific', userIds: ['user_1', 'user_4', 'user_14'], groupIds: ['group_3'] }, blockedUsers: [],
        relationships: [], customFields: { cf_6: 'Delaware' },
        billing: { billable: true, method: 'hourly', currency: 'USD', rates: [{ userId: 'user_4', rate: 600 }], budget: 40000, budgetUsed: 8900, trustBalance: 10000, minimumTrust: 5000, contingencyFee: null, flatRate: null },
        personalInjury: null,
        notifications: [], documentFolders: [{ id: 'folder_115_1', name: 'Corporate Documents', category: 'Corporate' }],
        reports: { useFirmSettings: true, originatingPct: 100, responsiblePct: 0 }, deleted: false, deletedAt: null
    },
    {
        id: 'matter_116', number: '00116', displayNumber: '00116-Vasquez-2', description: 'Vasquez VAWA Petition - Violence Against Women Act self-petition for abused spouse', status: 'open', billingMethod: 'hourly', clientId: 'contact_67', responsibleAttorneyId: 'user_10', originatingAttorneyId: 'user_3', responsibleStaffId: 'user_15', clientReferenceNumber: 'IMM-2025-0025', location: 'USCIS / Vermont Service Center', practiceAreaId: 'pa_8', stageId: 'stage_8_2', openDate: '2025-01-30', pendingDate: null, closedDate: null, createdDate: '2025-01-29T13:30:00Z', templateId: null,
        permissions: { type: 'specific', userIds: ['user_1', 'user_3', 'user_10', 'user_15'], groupIds: [] }, blockedUsers: [],
        relationships: [], customFields: { cf_6: 'USCIS' },
        billing: { billable: false, method: 'hourly', currency: 'USD', rates: [], budget: 0, budgetUsed: 0, trustBalance: 0, minimumTrust: 0, contingencyFee: null, flatRate: null },
        personalInjury: null,
        notifications: [{ userId: 'user_10', types: ['matter_updates'] }], documentFolders: [{ id: 'folder_116_1', name: 'VAWA Petition', category: 'Immigration' }],
        reports: { useFirmSettings: true, originatingPct: 50, responsiblePct: 50 }, deleted: false, deletedAt: null
    },
    {
        id: 'matter_117', number: '00117', displayNumber: '00117-Blackwell-EP', description: 'Blackwell Irrevocable Trust - Asset protection trust for high-net-worth client post-divorce', status: 'open', billingMethod: 'hourly', clientId: 'contact_16', responsibleAttorneyId: 'user_13', originatingAttorneyId: 'user_3', responsibleStaffId: 'user_11', clientReferenceNumber: 'EP-2025-0018', location: 'San Francisco / Nevada', practiceAreaId: 'pa_7', stageId: 'stage_7_2', openDate: '2025-02-01', pendingDate: null, closedDate: null, createdDate: '2025-01-31T11:00:00Z', templateId: 'template_6',
        permissions: { type: 'specific', userIds: ['user_1', 'user_3', 'user_13', 'user_11'], groupIds: [] }, blockedUsers: ['user_10'],
        relationships: [], customFields: {},
        billing: { billable: true, method: 'hourly', currency: 'USD', rates: [], budget: 25000, budgetUsed: 4500, trustBalance: 8000, minimumTrust: 5000, contingencyFee: null, flatRate: null },
        personalInjury: null,
        notifications: [], documentFolders: [{ id: 'folder_117_1', name: 'Trust Documents', category: 'Estate' }],
        reports: { useFirmSettings: true, originatingPct: 50, responsiblePct: 50 }, deleted: false, deletedAt: null
    },
    {
        id: 'matter_118', number: '00118', displayNumber: '00118-AlRashid-2', description: 'Al-Rashid v. Former Partner - Breach of fiduciary duty and accounting irregularities suit', status: 'open', billingMethod: 'hourly', clientId: 'contact_23', responsibleAttorneyId: 'user_16', originatingAttorneyId: 'user_12', responsibleStaffId: 'user_9', clientReferenceNumber: 'LIT-2025-0008', location: 'Alameda County Superior Court', practiceAreaId: 'pa_5', stageId: 'stage_5_2', openDate: '2025-02-12', pendingDate: null, closedDate: null, createdDate: '2025-02-11T10:00:00Z', templateId: null,
        permissions: { type: 'everyone', userIds: [], groupIds: [] }, blockedUsers: [],
        relationships: [], customFields: { cf_1: 'AC-2025-CV-02345', cf_2: 'Keller & Dunn LLP', cf_6: 'Alameda County' },
        billing: { billable: true, method: 'hourly', currency: 'USD', rates: [], budget: 50000, budgetUsed: 5600, trustBalance: 10000, minimumTrust: 5000, contingencyFee: null, flatRate: null },
        personalInjury: null,
        notifications: [], documentFolders: [{ id: 'folder_118_1', name: 'Financial Records', category: 'Financial' }, { id: 'folder_118_2', name: 'Court Documents', category: 'Court' }],
        reports: { useFirmSettings: true, originatingPct: 50, responsiblePct: 50 }, deleted: false, deletedAt: null
    },
    {
        id: 'matter_119', number: '00119', displayNumber: '00119-PinnacleSoft-2', description: 'Pinnacle Software v. DataMiner Inc. - Trade secret misappropriation by former employee who is now the CEO of DataMiner Inc. and who allegedly copied proprietary source code before departing', status: 'open', billingMethod: 'hourly', clientId: 'contact_51', responsibleAttorneyId: 'user_4', originatingAttorneyId: 'user_12', responsibleStaffId: 'user_14', clientReferenceNumber: 'LIT-2025-0015', location: 'Northern District of California', practiceAreaId: 'pa_9', stageId: 'stage_9_3', openDate: '2025-01-05', pendingDate: null, closedDate: null, createdDate: '2025-01-04T15:30:00Z', templateId: null,
        permissions: { type: 'specific', userIds: ['user_1', 'user_4', 'user_12', 'user_14'], groupIds: ['group_3'] }, blockedUsers: [],
        relationships: [], customFields: { cf_1: 'NDCA-2025-CV-00123', cf_2: 'Cooley LLP', cf_6: 'Northern District of California' },
        billing: { billable: true, method: 'hourly', currency: 'USD', rates: [{ userId: 'user_4', rate: 600 }], budget: 250000, budgetUsed: 34500, trustBalance: 30000, minimumTrust: 15000, contingencyFee: null, flatRate: null },
        personalInjury: null,
        notifications: [{ userId: 'user_4', types: ['matter_updates', 'budget_threshold'] }], documentFolders: [{ id: 'folder_119_1', name: 'Code Analysis', category: 'Evidence' }, { id: 'folder_119_2', name: 'Court Filings', category: 'Court' }],
        reports: { useFirmSettings: false, originatingPct: 40, responsiblePct: 60 }, deleted: false, deletedAt: null
    },
    {
        id: 'matter_120', number: '00120', displayNumber: '00120-Baptiste-CD', description: 'People v. Baptiste - Fraud charge related to insurance claim filing, maintaining innocence', status: 'open', billingMethod: 'hourly', clientId: 'contact_62', responsibleAttorneyId: 'user_8', originatingAttorneyId: 'user_3', responsibleStaffId: 'user_15', clientReferenceNumber: 'CD-2025-0045', location: 'San Francisco County Criminal Court', practiceAreaId: 'pa_3', stageId: 'stage_3_1', openDate: '2025-02-28', pendingDate: null, closedDate: null, createdDate: '2025-02-27T14:00:00Z', templateId: 'template_3',
        permissions: { type: 'everyone', userIds: [], groupIds: [] }, blockedUsers: [],
        relationships: [], customFields: { cf_1: 'SF-2025-CR-01567', cf_7: 'Hon. Elizabeth Chen', cf_8: '2025-05-10' },
        billing: { billable: true, method: 'hourly', currency: 'USD', rates: [], budget: 20000, budgetUsed: 800, trustBalance: 5000, minimumTrust: 3000, contingencyFee: null, flatRate: null },
        personalInjury: null,
        notifications: [], documentFolders: [{ id: 'folder_120_1', name: 'Court Documents', category: 'Court' }],
        reports: { useFirmSettings: true, originatingPct: 50, responsiblePct: 50 }, deleted: false, deletedAt: null
    }
];

const DAMAGES = [
    { id: 'dmg_1', matterId: 'matter_1', name: 'Emergency room visit - SF General Hospital', amount: 15750.00, type: 'special' },
    { id: 'dmg_2', matterId: 'matter_1', name: 'Lumbar MRI and diagnostic imaging', amount: 4200.00, type: 'special' },
    { id: 'dmg_3', matterId: 'matter_1', name: 'Physical therapy - 24 sessions', amount: 7200.00, type: 'special' },
    { id: 'dmg_4', matterId: 'matter_1', name: 'Lost wages - 6 weeks absence from work', amount: 12500.00, type: 'special' },
    { id: 'dmg_5', matterId: 'matter_1', name: 'Pain and suffering', amount: 75000.00, type: 'general' },
    { id: 'dmg_6', matterId: 'matter_2', name: 'Emergency room and hip surgery - UCSF Medical Center', amount: 42000.00, type: 'special' },
    { id: 'dmg_7', matterId: 'matter_2', name: 'Post-surgical rehabilitation - 16 weeks', amount: 12800.00, type: 'special' },
    { id: 'dmg_8', matterId: 'matter_2', name: 'Walker and mobility aids', amount: 850.00, type: 'special' },
    { id: 'dmg_9', matterId: 'matter_2', name: 'Lost wages - 4 months disability', amount: 28000.00, type: 'special' },
    { id: 'dmg_10', matterId: 'matter_2', name: 'Pain, suffering, and diminished quality of life', amount: 125000.00, type: 'general' },
    { id: 'dmg_11', matterId: 'matter_3', name: 'Emergency transport and ER treatment', amount: 8500.00, type: 'special' },
    { id: 'dmg_12', matterId: 'matter_3', name: 'Orthopedic surgery - multiple fractures', amount: 35000.00, type: 'special' },
    { id: 'dmg_13', matterId: 'matter_3', name: 'Physical therapy - 32 sessions', amount: 9600.00, type: 'special' },
    { id: 'dmg_14', matterId: 'matter_3', name: 'Lost income during recovery', amount: 22000.00, type: 'special' },
    { id: 'dmg_15', matterId: 'matter_3', name: 'Pain and suffering - settled amount', amount: 75000.00, type: 'general' },
    { id: 'dmg_16', matterId: 'matter_4', name: 'Hand surgery and microsurgery - SF General', amount: 28000.00, type: 'special' },
    { id: 'dmg_17', matterId: 'matter_4', name: 'Occupational therapy for hand rehabilitation', amount: 8400.00, type: 'special' },
    { id: 'dmg_18', matterId: 'matter_4', name: 'Permanent partial disability - reduced grip strength', amount: 45000.00, type: 'general' },
    { id: 'dmg_19', matterId: 'matter_4', name: 'Future lost earning capacity', amount: 120000.00, type: 'special' },
    { id: 'dmg_20', matterId: 'matter_5', name: 'Emergency room and spinal evaluation', amount: 18500.00, type: 'special' },
    { id: 'dmg_21', matterId: 'matter_5', name: 'Spinal surgery consultation', amount: 3500.00, type: 'special' },
    { id: 'dmg_22', matterId: 'matter_6', name: 'Emergency room visit after pedestrian accident', amount: 12000.00, type: 'special' },
    { id: 'dmg_23', matterId: 'matter_6', name: 'Knee surgery and ACL repair', amount: 22000.00, type: 'special' },
    { id: 'dmg_24', matterId: 'matter_6', name: 'Physical therapy - ongoing', amount: 5400.00, type: 'special' },
    { id: 'dmg_25', matterId: 'matter_6', name: 'Pain and suffering', amount: 80000.00, type: 'general' },
    { id: 'dmg_26', matterId: 'matter_7', name: 'Burn unit treatment - 3 weeks hospitalization', amount: 95000.00, type: 'special' },
    { id: 'dmg_27', matterId: 'matter_7', name: 'Skin grafting surgery', amount: 45000.00, type: 'special' },
    { id: 'dmg_28', matterId: 'matter_7', name: 'Ongoing wound care and scar treatment', amount: 12000.00, type: 'special' },
    { id: 'dmg_29', matterId: 'matter_7', name: 'Disfigurement and emotional distress', amount: 200000.00, type: 'general' },
    { id: 'dmg_30', matterId: 'matter_7', name: 'Punitive damages claim - manufacturer negligence', amount: 500000.00, type: 'other' },
    { id: 'dmg_31', matterId: 'matter_8', name: 'Neurological evaluation and TBI diagnosis', amount: 8500.00, type: 'special' },
    { id: 'dmg_32', matterId: 'matter_8', name: 'Cognitive rehabilitation therapy', amount: 15000.00, type: 'special' },
    { id: 'dmg_33', matterId: 'matter_14', name: 'Corrective surgery - emergency intervention', amount: 55000.00, type: 'special' },
    { id: 'dmg_34', matterId: 'matter_14', name: 'Extended ICU stay - 8 days', amount: 72000.00, type: 'special' },
    { id: 'dmg_35', matterId: 'matter_14', name: 'Pain, suffering, and emotional trauma', amount: 250000.00, type: 'general' },
    { id: 'dmg_36', matterId: 'matter_105', name: 'Emergency treatment for pulmonary embolism', amount: 38000.00, type: 'special' },
    { id: 'dmg_37', matterId: 'matter_105', name: 'Follow-up cardiac care', amount: 15000.00, type: 'special' },
    { id: 'dmg_38', matterId: 'matter_105', name: 'Permanent lung damage - reduced capacity', amount: 150000.00, type: 'general' }
];

const MEDICAL_PROVIDERS = [
    {
        id: 'mp_1', matterId: 'matter_1', contactId: 'contact_55', description: 'Emergency room treatment for back injury from bus accident',
        firstTreatmentDate: '2024-03-15', lastTreatmentDate: '2024-03-15', treatmentComplete: true,
        recordRequestDate: '2024-04-01', recordFollowUpDate: '2024-05-01', recordStatus: 'received',
        billRequestDate: '2024-04-01', billFollowUpDate: '2024-05-01', billStatus: 'received'
    },
    {
        id: 'mp_2', matterId: 'matter_1', contactId: 'contact_56', description: 'Orthopedic evaluation and treatment for lumbar disc herniation',
        firstTreatmentDate: '2024-03-22', lastTreatmentDate: '2025-06-15', treatmentComplete: false,
        recordRequestDate: '2024-04-15', recordFollowUpDate: '2024-05-15', recordStatus: 'received',
        billRequestDate: '2024-04-15', billFollowUpDate: '2024-05-15', billStatus: 'received'
    },
    {
        id: 'mp_3', matterId: 'matter_1', contactId: 'contact_57', description: 'Physical therapy for back rehabilitation - weekly sessions',
        firstTreatmentDate: '2024-04-10', lastTreatmentDate: '2025-08-15', treatmentComplete: false,
        recordRequestDate: '2024-06-01', recordFollowUpDate: '2024-07-01', recordStatus: 'received',
        billRequestDate: '2024-06-01', billFollowUpDate: '2024-07-01', billStatus: 'received'
    },
    {
        id: 'mp_4', matterId: 'matter_2', contactId: 'contact_59', description: 'Hip fracture surgery and post-operative care',
        firstTreatmentDate: '2024-05-12', lastTreatmentDate: '2024-09-20', treatmentComplete: true,
        recordRequestDate: '2024-06-15', recordFollowUpDate: '2024-07-15', recordStatus: 'certified',
        billRequestDate: '2024-06-15', billFollowUpDate: '2024-07-15', billStatus: 'received'
    },
    {
        id: 'mp_5', matterId: 'matter_2', contactId: 'contact_57', description: 'Post-surgical physical therapy for hip rehabilitation',
        firstTreatmentDate: '2024-06-15', lastTreatmentDate: '2024-12-20', treatmentComplete: true,
        recordRequestDate: '2024-08-01', recordFollowUpDate: '2024-09-01', recordStatus: 'received',
        billRequestDate: '2024-08-01', billFollowUpDate: '2024-09-01', billStatus: 'received'
    },
    {
        id: 'mp_6', matterId: 'matter_4', contactId: 'contact_55', description: 'Emergency hand surgery for crush injury',
        firstTreatmentDate: '2024-04-18', lastTreatmentDate: '2024-04-25', treatmentComplete: true,
        recordRequestDate: '2024-05-10', recordFollowUpDate: '2024-06-10', recordStatus: 'received',
        billRequestDate: '2024-05-10', billFollowUpDate: '2024-06-10', billStatus: 'received'
    },
    {
        id: 'mp_7', matterId: 'matter_4', contactId: 'contact_68', description: 'Hand therapy and occupational rehabilitation',
        firstTreatmentDate: '2024-05-15', lastTreatmentDate: '2025-03-01', treatmentComplete: false,
        recordRequestDate: '2024-07-01', recordFollowUpDate: '2024-08-01', recordStatus: 'incomplete',
        billRequestDate: '2024-07-01', billFollowUpDate: '2024-08-01', billStatus: 'requested'
    },
    {
        id: 'mp_8', matterId: 'matter_7', contactId: 'contact_55', description: 'Burn unit treatment and initial hospitalization',
        firstTreatmentDate: '2024-07-19', lastTreatmentDate: '2024-08-08', treatmentComplete: true,
        recordRequestDate: '2024-08-15', recordFollowUpDate: '2024-09-15', recordStatus: 'received',
        billRequestDate: '2024-08-15', billFollowUpDate: '2024-09-15', billStatus: 'received'
    },
    {
        id: 'mp_9', matterId: 'matter_7', contactId: 'contact_66', description: 'Plastic surgery for skin grafting and scar revision',
        firstTreatmentDate: '2024-09-01', lastTreatmentDate: '2025-04-15', treatmentComplete: false,
        recordRequestDate: '2024-10-01', recordFollowUpDate: '2024-11-01', recordStatus: 'requested',
        billRequestDate: '2024-10-01', billFollowUpDate: '2024-11-01', billStatus: 'not_requested'
    },
    {
        id: 'mp_10', matterId: 'matter_8', contactId: 'contact_59', description: 'Traumatic brain injury evaluation and treatment',
        firstTreatmentDate: '2024-09-11', lastTreatmentDate: '2025-02-28', treatmentComplete: false,
        recordRequestDate: '2024-10-15', recordFollowUpDate: '2024-11-15', recordStatus: 'received',
        billRequestDate: '2024-10-15', billFollowUpDate: '2024-11-15', billStatus: 'received'
    },
    {
        id: 'mp_11', matterId: 'matter_6', contactId: 'contact_56', description: 'ACL repair surgery for knee injury',
        firstTreatmentDate: '2024-10-05', lastTreatmentDate: '2024-10-05', treatmentComplete: true,
        recordRequestDate: '2024-11-01', recordFollowUpDate: '2024-12-01', recordStatus: 'received',
        billRequestDate: '2024-11-01', billFollowUpDate: '2024-12-01', billStatus: 'received'
    },
    {
        id: 'mp_12', matterId: 'matter_6', contactId: 'contact_60', description: 'Chiropractic care for neck and shoulder pain from accident',
        firstTreatmentDate: '2024-10-15', lastTreatmentDate: '2025-03-01', treatmentComplete: false,
        recordRequestDate: '2024-12-01', recordFollowUpDate: '2025-01-01', recordStatus: 'incomplete',
        billRequestDate: '2024-12-01', billFollowUpDate: '2025-01-01', billStatus: 'requested'
    }
];

const MEDICAL_RECORDS = [
    { id: 'mr_1', providerId: 'mp_1', matterId: 'matter_1', fileName: 'Initial_Assessment_Patterson_2024.pdf', receivedDate: '2024-05-10', startDate: '2024-03-15', endDate: '2024-03-15', status: 'received', comments: [{ id: 'mrc_1', userId: 'user_7', text: 'Confirmed diagnosis of L4-L5 disc herniation', createdAt: '2024-05-11T09:30:00Z' }] },
    { id: 'mr_2', providerId: 'mp_1', matterId: 'matter_1', fileName: 'ER_Records_Patterson_March2024.pdf', receivedDate: '2024-05-10', startDate: '2024-03-15', endDate: '2024-03-15', status: 'received', comments: [] },
    { id: 'mr_3', providerId: 'mp_2', matterId: 'matter_1', fileName: 'Ortho_Eval_Patterson_2024.pdf', receivedDate: '2024-05-20', startDate: '2024-03-22', endDate: '2024-06-15', status: 'received', comments: [{ id: 'mrc_2', userId: 'user_2', text: 'Dr. recommends possible surgical intervention if PT fails', createdAt: '2024-05-21T14:00:00Z' }] },
    { id: 'mr_4', providerId: 'mp_3', matterId: 'matter_1', fileName: 'PT_Progress_Notes_Patterson.pdf', receivedDate: '2024-08-15', startDate: '2024-04-10', endDate: '2024-08-01', status: 'received', comments: [] },
    { id: 'mr_5', providerId: 'mp_4', matterId: 'matter_2', fileName: 'Surgical_Report_Johnson_Hip.pdf', receivedDate: '2024-07-20', startDate: '2024-05-12', endDate: '2024-05-18', status: 'received', comments: [{ id: 'mrc_3', userId: 'user_7', text: 'Total hip arthroplasty performed successfully', createdAt: '2024-07-21T10:15:00Z' }] },
    { id: 'mr_6', providerId: 'mp_4', matterId: 'matter_2', fileName: 'Post_Op_Records_Johnson.pdf', receivedDate: '2024-10-15', startDate: '2024-05-18', endDate: '2024-09-20', status: 'received', comments: [] },
    { id: 'mr_7', providerId: 'mp_5', matterId: 'matter_2', fileName: 'PT_Records_Johnson_2024.pdf', receivedDate: '2024-10-30', startDate: '2024-06-15', endDate: '2024-12-20', status: 'received', comments: [] },
    { id: 'mr_8', providerId: 'mp_6', matterId: 'matter_4', fileName: 'ER_Surgery_Washington_Hand.pdf', receivedDate: '2024-06-15', startDate: '2024-04-18', endDate: '2024-04-25', status: 'received', comments: [{ id: 'mrc_4', userId: 'user_7', text: 'Microsurgery to repair severed tendons in left hand', createdAt: '2024-06-16T09:00:00Z' }] },
    { id: 'mr_9', providerId: 'mp_7', matterId: 'matter_4', fileName: 'OT_Progress_Washington_Partial.pdf', receivedDate: '2024-09-01', startDate: '2024-05-15', endDate: '2024-08-15', status: 'incomplete', comments: [{ id: 'mrc_5', userId: 'user_9', text: 'Records only through August - need to follow up for remaining', createdAt: '2024-09-02T11:30:00Z' }] },
    { id: 'mr_10', providerId: 'mp_8', matterId: 'matter_7', fileName: 'Burn_Unit_Records_Okafor.pdf', receivedDate: '2024-09-20', startDate: '2024-07-19', endDate: '2024-08-08', status: 'received', comments: [{ id: 'mrc_6', userId: 'user_7', text: 'Second and third degree burns on torso and left arm', createdAt: '2024-09-21T10:00:00Z' }] },
    { id: 'mr_11', providerId: 'mp_10', matterId: 'matter_8', fileName: 'TBI_Evaluation_Mills.pdf', receivedDate: '2024-11-20', startDate: '2024-09-11', endDate: '2024-11-15', status: 'received', comments: [{ id: 'mrc_7', userId: 'user_9', text: 'Moderate TBI with ongoing cognitive deficits', createdAt: '2024-11-21T14:30:00Z' }] },
    { id: 'mr_12', providerId: 'mp_11', matterId: 'matter_6', fileName: 'ACL_Surgery_McCarthy.pdf', receivedDate: '2024-12-10', startDate: '2024-10-05', endDate: '2024-10-05', status: 'received', comments: [] },
    { id: 'mr_13', providerId: 'mp_1', matterId: 'matter_1', fileName: 'MRI_Report_Patterson_Lumbar.pdf', receivedDate: '2024-05-15', startDate: '2024-03-20', endDate: '2024-03-20', status: 'received', comments: [{ id: 'mrc_8', userId: 'user_2', text: 'MRI confirms L4-L5 herniation with nerve impingement', createdAt: '2024-05-16T08:45:00Z' }] },
    { id: 'mr_14', providerId: 'mp_9', matterId: 'matter_7', fileName: 'PlasticSurgery_Consult_Okafor.pdf', receivedDate: '2024-11-01', startDate: '2024-09-01', endDate: '2024-10-15', status: 'received', comments: [] },
    { id: 'mr_15', providerId: 'mp_12', matterId: 'matter_6', fileName: 'Chiro_Records_McCarthy_Partial.pdf', receivedDate: '2025-01-15', startDate: '2024-10-15', endDate: '2024-12-31', status: 'incomplete', comments: [{ id: 'mrc_9', userId: 'user_7', text: 'Only partial records received - follow up for January onward', createdAt: '2025-01-16T09:00:00Z' }] },
    { id: 'mr_16', providerId: 'mp_10', matterId: 'matter_8', fileName: 'Neuro_Follow_Up_Mills.pdf', receivedDate: '2025-01-10', startDate: '2024-12-01', endDate: '2025-01-05', status: 'received', comments: [] }
];

const MEDICAL_BILLS = [
    { id: 'mb_1', providerId: 'mp_1', matterId: 'matter_1', fileName: 'Invoice_SFGeneral_March2024.pdf', billDate: '2024-04-15', receivedDate: '2024-05-10', billAmount: 15750.00, adjustment: 2500.00, payers: [{ contactId: 'contact_58', amountPaid: 8000.00, isLien: true }], balanceOwed: 5250.00, balanceLien: false, outstandingBalance: true, status: 'received' },
    { id: 'mb_2', providerId: 'mp_2', matterId: 'matter_1', fileName: 'Invoice_BayOrtho_2024.pdf', billDate: '2024-05-20', receivedDate: '2024-06-05', billAmount: 4200.00, adjustment: 0, payers: [], balanceOwed: 4200.00, balanceLien: false, outstandingBalance: true, status: 'received' },
    { id: 'mb_3', providerId: 'mp_3', matterId: 'matter_1', fileName: 'Invoice_PacificPT_2024.pdf', billDate: '2024-08-01', receivedDate: '2024-08-15', billAmount: 7200.00, adjustment: 800.00, payers: [{ contactId: 'contact_58', amountPaid: 3200.00, isLien: true }], balanceOwed: 3200.00, balanceLien: false, outstandingBalance: true, status: 'received' },
    { id: 'mb_4', providerId: 'mp_4', matterId: 'matter_2', fileName: 'Invoice_UCSF_Surgery_Johnson.pdf', billDate: '2024-06-15', receivedDate: '2024-07-20', billAmount: 42000.00, adjustment: 5000.00, payers: [{ contactId: 'contact_30', amountPaid: 25000.00, isLien: true }], balanceOwed: 12000.00, balanceLien: true, outstandingBalance: true, status: 'received' },
    { id: 'mb_5', providerId: 'mp_5', matterId: 'matter_2', fileName: 'Invoice_PacificPT_Johnson.pdf', billDate: '2024-11-01', receivedDate: '2024-11-15', billAmount: 12800.00, adjustment: 1500.00, payers: [], balanceOwed: 11300.00, balanceLien: false, outstandingBalance: true, status: 'received' },
    { id: 'mb_6', providerId: 'mp_6', matterId: 'matter_4', fileName: 'Invoice_SFGeneral_Washington.pdf', billDate: '2024-05-20', receivedDate: '2024-06-15', billAmount: 28000.00, adjustment: 3000.00, payers: [{ contactId: 'contact_42', amountPaid: 18000.00, isLien: true }], balanceOwed: 7000.00, balanceLien: false, outstandingBalance: true, status: 'received' },
    { id: 'mb_7', providerId: 'mp_7', matterId: 'matter_4', fileName: 'Invoice_Horizon_Washington_Partial.pdf', billDate: '2024-08-15', receivedDate: '2024-09-01', billAmount: 4200.00, adjustment: 0, payers: [], balanceOwed: 4200.00, balanceLien: false, outstandingBalance: true, status: 'received' },
    { id: 'mb_8', providerId: 'mp_8', matterId: 'matter_7', fileName: 'Invoice_SFGeneral_BurnUnit_Okafor.pdf', billDate: '2024-08-20', receivedDate: '2024-09-20', billAmount: 95000.00, adjustment: 10000.00, payers: [{ contactId: 'contact_30', amountPaid: 50000.00, isLien: true }], balanceOwed: 35000.00, balanceLien: true, outstandingBalance: true, status: 'received' },
    { id: 'mb_9', providerId: 'mp_10', matterId: 'matter_8', fileName: 'Invoice_UCSF_TBI_Mills.pdf', billDate: '2024-11-01', receivedDate: '2024-11-20', billAmount: 8500.00, adjustment: 500.00, payers: [], balanceOwed: 8000.00, balanceLien: false, outstandingBalance: true, status: 'received' },
    { id: 'mb_10', providerId: 'mp_11', matterId: 'matter_6', fileName: 'Invoice_BayOrtho_McCarthy_ACL.pdf', billDate: '2024-11-15', receivedDate: '2024-12-10', billAmount: 22000.00, adjustment: 2000.00, payers: [], balanceOwed: 20000.00, balanceLien: false, outstandingBalance: true, status: 'received' },
    { id: 'mb_11', providerId: 'mp_1', matterId: 'matter_1', fileName: 'Invoice_SFGeneral_FollowUp.pdf', billDate: '2024-06-01', receivedDate: '2024-06-20', billAmount: 1200.00, adjustment: 0, payers: [], balanceOwed: 1200.00, balanceLien: false, outstandingBalance: true, status: 'received' },
    { id: 'mb_12', providerId: 'mp_4', matterId: 'matter_2', fileName: 'Invoice_UCSF_FollowUp_Johnson.pdf', billDate: '2024-09-01', receivedDate: '2024-09-20', billAmount: 2500.00, adjustment: 0, payers: [], balanceOwed: 2500.00, balanceLien: false, outstandingBalance: true, status: 'received' },
    { id: 'mb_13', providerId: 'mp_9', matterId: 'matter_7', fileName: 'Invoice_MeridianRad_Okafor.pdf', billDate: '2024-10-15', receivedDate: '2024-11-01', billAmount: 3500.00, adjustment: 0, payers: [], balanceOwed: 3500.00, balanceLien: false, outstandingBalance: true, status: 'received' },
    { id: 'mb_14', providerId: 'mp_12', matterId: 'matter_6', fileName: 'Invoice_ReevesChiro_McCarthy.pdf', billDate: '2025-01-01', receivedDate: '2025-01-15', billAmount: 5400.00, adjustment: 400.00, payers: [], balanceOwed: 5000.00, balanceLien: false, outstandingBalance: true, status: 'received' },
    { id: 'mb_15', providerId: 'mp_10', matterId: 'matter_8', fileName: 'Invoice_UCSF_CogRehab_Mills.pdf', billDate: '2025-01-15', receivedDate: '2025-02-01', billAmount: 15000.00, adjustment: 1000.00, payers: [], balanceOwed: 14000.00, balanceLien: false, outstandingBalance: true, status: 'received' },
    { id: 'mb_16', providerId: 'mp_8', matterId: 'matter_7', fileName: 'Invoice_SFGeneral_SkinGraft_Okafor.pdf', billDate: '2024-10-01', receivedDate: '2024-10-20', billAmount: 45000.00, adjustment: 5000.00, payers: [], balanceOwed: 40000.00, balanceLien: false, outstandingBalance: true, status: 'received' }
];

const SETTLEMENTS = {
    'matter_3': {
        recoveries: [
            { id: 'rec_1', sourceContactId: 'contact_30', sourceName: 'ABC Insurance Co.', amount: 150000.00 }
        ],
        legalFees: [
            { id: 'lf_1', recoveryId: 'rec_1', recipientId: 'user_2', rate: 33.33, discount: 0, referralFees: [] }
        ],
        nonMedicalLiens: [
            { id: 'nml_1', holderContactId: 'contact_42', description: 'Workers comp subrogation lien', amount: 12000, reduction: 2000 }
        ],
        outstandingBalances: [
            { id: 'ob_1', responsibility: 'client', holderContactId: 'contact_57', description: 'Remaining balance - Pacific PT clinic', balanceOwing: 3500, reduction: 500 }
        ]
    },
    'matter_17': {
        recoveries: [
            { id: 'rec_2', sourceContactId: 'contact_30', sourceName: 'GEICO Insurance', amount: 85000.00 }
        ],
        legalFees: [
            { id: 'lf_2', recoveryId: 'rec_2', recipientId: 'user_2', rate: 33.33, discount: 0, referralFees: [] }
        ],
        nonMedicalLiens: [],
        outstandingBalances: [
            { id: 'ob_2', responsibility: 'attorney', holderContactId: 'contact_59', description: 'UCSF Medical Center balance', balanceOwing: 2800, reduction: 0 }
        ]
    },
    'matter_21': {
        recoveries: [
            { id: 'rec_3', sourceContactId: 'contact_30', sourceName: 'SFMTA Claims Division', amount: 45000.00 }
        ],
        legalFees: [
            { id: 'lf_3', recoveryId: 'rec_3', recipientId: 'user_2', rate: 33.33, discount: 5, referralFees: [] }
        ],
        nonMedicalLiens: [],
        outstandingBalances: []
    },
    'matter_105': {
        recoveries: [
            { id: 'rec_4', sourceContactId: 'contact_59', sourceName: 'UC Regents Settlement Fund', amount: 425000.00 }
        ],
        legalFees: [
            { id: 'lf_4', recoveryId: 'rec_4', recipientId: 'user_2', rate: 40, discount: 0, referralFees: [{ recipientId: 'user_1', percentage: 5 }] }
        ],
        nonMedicalLiens: [
            { id: 'nml_2', holderContactId: 'contact_58', description: 'Health insurance subrogation lien', amount: 28000, reduction: 8000 }
        ],
        outstandingBalances: [
            { id: 'ob_3', responsibility: 'client', holderContactId: 'contact_66', description: 'Radiology follow-up balance', balanceOwing: 1500, reduction: 0 },
            { id: 'ob_4', responsibility: 'attorney', holderContactId: 'contact_68', description: 'Horizon Healthcare outstanding', balanceOwing: 3200, reduction: 500 }
        ]
    },
    'matter_66': {
        recoveries: [
            { id: 'rec_5', sourceContactId: 'contact_20', sourceName: 'Sierra Nevada Brewing Co. (final payment)', amount: 28500.00 }
        ],
        legalFees: [
            { id: 'lf_5', recoveryId: 'rec_5', recipientId: 'user_12', rate: 0, discount: 0, referralFees: [] }
        ],
        nonMedicalLiens: [],
        outstandingBalances: []
    },
    'matter_49': {
        recoveries: [],
        legalFees: [
            { id: 'lf_6', recoveryId: null, recipientId: 'user_5', rate: 0, discount: 0, referralFees: [] }
        ],
        nonMedicalLiens: [],
        outstandingBalances: []
    }
};

const TIME_ENTRIES = [
    // Matter 1 - Patterson PI
    { id: 'te_1', matterId: 'matter_1', userId: 'user_2', date: '2024-03-20', hours: 1.5, rate: 425, description: 'Initial client consultation regarding bus accident', billable: true, status: 'approved' },
    { id: 'te_2', matterId: 'matter_1', userId: 'user_7', date: '2024-03-21', hours: 2.0, rate: 150, description: 'Gather police report and medical records from SF General', billable: true, status: 'approved' },
    { id: 'te_3', matterId: 'matter_1', userId: 'user_2', date: '2024-04-05', hours: 3.0, rate: 425, description: 'Draft and send demand letter to Metro Transit Authority', billable: true, status: 'approved' },
    { id: 'te_4', matterId: 'matter_1', userId: 'user_7', date: '2024-04-10', hours: 1.0, rate: 150, description: 'Follow up on medical records requests', billable: true, status: 'approved' },
    { id: 'te_5', matterId: 'matter_1', userId: 'user_2', date: '2024-05-15', hours: 2.5, rate: 425, description: 'Review opposing counsel response and prepare counter-demand', billable: true, status: 'approved' },
    { id: 'te_6', matterId: 'matter_1', userId: 'user_1', date: '2024-06-01', hours: 0.5, rate: 350, description: 'Case strategy review with Marcus Williams', billable: true, status: 'approved' },
    { id: 'te_7', matterId: 'matter_1', userId: 'user_7', date: '2024-06-15', hours: 1.5, rate: 150, description: 'Organize medical bills and prepare damages summary', billable: true, status: 'approved' },
    { id: 'te_8', matterId: 'matter_1', userId: 'user_2', date: '2024-07-10', hours: 2.0, rate: 425, description: 'Telephone conference with insurance adjuster re settlement', billable: true, status: 'approved' },
    { id: 'te_9', matterId: 'matter_1', userId: 'user_2', date: '2024-08-20', hours: 1.0, rate: 425, description: 'Review updated medical records and revise demand', billable: true, status: 'billed' },
    { id: 'te_10', matterId: 'matter_1', userId: 'user_7', date: '2024-09-05', hours: 2.0, rate: 150, description: 'Prepare chronological medical treatment summary', billable: true, status: 'billed' },
    // Matter 2 - Johnson slip and fall
    { id: 'te_11', matterId: 'matter_2', userId: 'user_2', date: '2024-05-16', hours: 1.0, rate: 425, description: 'Initial intake interview with Aisha Johnson', billable: true, status: 'approved' },
    { id: 'te_12', matterId: 'matter_2', userId: 'user_7', date: '2024-05-20', hours: 3.0, rate: 150, description: 'Investigate incident scene, photograph conditions, interview witnesses', billable: true, status: 'approved' },
    { id: 'te_13', matterId: 'matter_2', userId: 'user_2', date: '2024-06-10', hours: 2.0, rate: 425, description: 'Draft preservation letter and initial demand to Whole Foods', billable: true, status: 'approved' },
    { id: 'te_14', matterId: 'matter_2', userId: 'user_7', date: '2024-07-01', hours: 1.5, rate: 150, description: 'Request store surveillance footage and maintenance logs', billable: true, status: 'approved' },
    // Matter 3 - Russo (closed)
    { id: 'te_15', matterId: 'matter_3', userId: 'user_2', date: '2024-06-02', hours: 1.5, rate: 425, description: 'Client meeting to discuss Lyft accident case strategy', billable: true, status: 'billed' },
    { id: 'te_16', matterId: 'matter_3', userId: 'user_9', date: '2024-06-15', hours: 2.5, rate: 145, description: 'Compile accident evidence and police report analysis', billable: true, status: 'billed' },
    { id: 'te_17', matterId: 'matter_3', userId: 'user_2', date: '2024-07-20', hours: 4.0, rate: 425, description: 'Draft complaint and file with San Mateo Superior Court', billable: true, status: 'billed' },
    { id: 'te_18', matterId: 'matter_3', userId: 'user_2', date: '2024-09-15', hours: 3.0, rate: 425, description: 'Mediation preparation and settlement demand package', billable: true, status: 'billed' },
    { id: 'te_19', matterId: 'matter_3', userId: 'user_2', date: '2024-10-05', hours: 6.0, rate: 425, description: 'Full day mediation session with ABC Insurance', billable: true, status: 'billed' },
    { id: 'te_20', matterId: 'matter_3', userId: 'user_9', date: '2024-11-01', hours: 3.0, rate: 145, description: 'Prepare settlement disbursement statement and closing docs', billable: true, status: 'billed' },
    // Matter 4 - Washington workplace
    { id: 'te_21', matterId: 'matter_4', userId: 'user_8', date: '2024-04-22', hours: 1.5, rate: 400, description: 'Emergency client consultation at hospital re workplace injury', billable: true, status: 'approved' },
    { id: 'te_22', matterId: 'matter_4', userId: 'user_7', date: '2024-04-25', hours: 2.0, rate: 150, description: 'Obtain OSHA violation records and employer safety reports', billable: true, status: 'approved' },
    { id: 'te_23', matterId: 'matter_4', userId: 'user_8', date: '2024-05-15', hours: 3.5, rate: 400, description: 'Draft complaint against Pacific Steel Works', billable: true, status: 'approved' },
    { id: 'te_24', matterId: 'matter_4', userId: 'user_8', date: '2024-07-01', hours: 2.0, rate: 400, description: 'Deposition preparation and witness outline', billable: true, status: 'approved' },
    { id: 'te_25', matterId: 'matter_4', userId: 'user_7', date: '2024-08-10', hours: 4.0, rate: 150, description: 'Review and organize 200+ pages of employer safety records', billable: true, status: 'approved' },
    { id: 'te_26', matterId: 'matter_4', userId: 'user_8', date: '2024-09-20', hours: 5.0, rate: 400, description: 'Take deposition of plant safety manager', billable: true, status: 'approved' },
    // Matter 7 - Okafor product liability
    { id: 'te_27', matterId: 'matter_7', userId: 'user_2', date: '2024-07-25', hours: 2.0, rate: 425, description: 'Initial client meeting regarding burn injuries from space heater', billable: true, status: 'approved' },
    { id: 'te_28', matterId: 'matter_7', userId: 'user_7', date: '2024-08-01', hours: 3.0, rate: 150, description: 'Research product recall history and CPSC complaints', billable: true, status: 'approved' },
    { id: 'te_29', matterId: 'matter_7', userId: 'user_2', date: '2024-08-15', hours: 4.0, rate: 425, description: 'Draft federal complaint for product liability', billable: true, status: 'approved' },
    { id: 'te_30', matterId: 'matter_7', userId: 'user_2', date: '2024-09-10', hours: 2.5, rate: 425, description: 'Retain product safety expert and review engagement terms', billable: true, status: 'approved' },
    { id: 'te_31', matterId: 'matter_7', userId: 'user_7', date: '2024-10-01', hours: 2.0, rate: 150, description: 'Prepare product testing chain of custody documentation', billable: true, status: 'approved' },
    { id: 'te_32', matterId: 'matter_7', userId: 'user_2', date: '2024-11-15', hours: 6.0, rate: 425, description: 'Prepare for and attend case management conference', billable: true, status: 'approved' },
    // Matter 28 - Gonzalez family law
    { id: 'te_33', matterId: 'matter_28', userId: 'user_3', date: '2024-01-15', hours: 1.5, rate: 475, description: 'Initial divorce consultation with Maria Gonzalez', billable: true, status: 'approved' },
    { id: 'te_34', matterId: 'matter_28', userId: 'user_11', date: '2024-01-20', hours: 3.0, rate: 125, description: 'Prepare initial financial disclosure documents', billable: true, status: 'approved' },
    { id: 'te_35', matterId: 'matter_28', userId: 'user_3', date: '2024-02-10', hours: 2.0, rate: 475, description: 'Draft petition for dissolution and temporary orders', billable: true, status: 'approved' },
    { id: 'te_36', matterId: 'matter_28', userId: 'user_3', date: '2024-03-15', hours: 3.5, rate: 475, description: 'Attend temporary orders hearing', billable: true, status: 'approved' },
    { id: 'te_37', matterId: 'matter_28', userId: 'user_11', date: '2024-04-20', hours: 4.0, rate: 125, description: 'Compile property division spreadsheet and asset inventory', billable: true, status: 'approved' },
    { id: 'te_38', matterId: 'matter_28', userId: 'user_3', date: '2024-06-01', hours: 2.0, rate: 475, description: 'Review custody evaluator report and prepare response', billable: true, status: 'approved' },
    { id: 'te_39', matterId: 'matter_28', userId: 'user_3', date: '2024-08-15', hours: 5.0, rate: 475, description: 'Participate in settlement conference with opposing counsel', billable: true, status: 'approved' },
    // Matter 44 - Thompson criminal
    { id: 'te_40', matterId: 'matter_44', userId: 'user_8', date: '2024-08-26', hours: 1.0, rate: 400, description: 'Emergency client meeting at county jail', billable: true, status: 'approved' },
    { id: 'te_41', matterId: 'matter_44', userId: 'user_8', date: '2024-08-28', hours: 2.0, rate: 400, description: 'Arraignment hearing and bail argument', billable: true, status: 'approved' },
    { id: 'te_42', matterId: 'matter_44', userId: 'user_5', date: '2024-09-05', hours: 4.0, rate: 275, description: 'Review discovery materials and surveillance footage', billable: true, status: 'approved' },
    { id: 'te_43', matterId: 'matter_44', userId: 'user_8', date: '2024-10-01', hours: 3.0, rate: 400, description: 'File motion to suppress evidence', billable: true, status: 'approved' },
    { id: 'te_44', matterId: 'matter_44', userId: 'user_8', date: '2024-11-15', hours: 4.0, rate: 400, description: 'Hearing on motion to suppress', billable: true, status: 'approved' },
    { id: 'te_45', matterId: 'matter_44', userId: 'user_15', date: '2024-12-01', hours: 2.0, rate: 130, description: 'Compile witness contact list and interview notes', billable: true, status: 'approved' },
    // Matter 46 - Hernandez robbery
    { id: 'te_46', matterId: 'matter_46', userId: 'user_8', date: '2024-07-08', hours: 2.0, rate: 400, description: 'Initial client meeting at detention facility', billable: true, status: 'approved' },
    { id: 'te_47', matterId: 'matter_46', userId: 'user_8', date: '2024-07-15', hours: 3.0, rate: 400, description: 'Arraignment and bail hearing', billable: true, status: 'approved' },
    { id: 'te_48', matterId: 'matter_46', userId: 'user_5', date: '2024-08-01', hours: 6.0, rate: 275, description: 'Extensive discovery review - 500+ pages', billable: true, status: 'approved' },
    { id: 'te_49', matterId: 'matter_46', userId: 'user_8', date: '2024-09-10', hours: 4.0, rate: 400, description: 'Interview alibi witnesses and prepare declarations', billable: true, status: 'approved' },
    { id: 'te_50', matterId: 'matter_46', userId: 'user_8', date: '2024-10-20', hours: 5.0, rate: 400, description: 'Pre-trial motions and evidence challenges', billable: true, status: 'approved' },
    // Matter 47 - Franklin white collar
    { id: 'te_51', matterId: 'matter_47', userId: 'user_4', date: '2024-12-22', hours: 3.0, rate: 550, description: 'Initial case review and strategy discussion with client', billable: true, status: 'approved' },
    { id: 'te_52', matterId: 'matter_47', userId: 'user_8', date: '2025-01-05', hours: 4.0, rate: 400, description: 'Review SEC investigation documents', billable: true, status: 'approved' },
    { id: 'te_53', matterId: 'matter_47', userId: 'user_15', date: '2025-01-10', hours: 3.0, rate: 130, description: 'Organize financial transaction records chronologically', billable: true, status: 'approved' },
    { id: 'te_54', matterId: 'matter_47', userId: 'user_4', date: '2025-01-20', hours: 2.5, rate: 550, description: 'Conference call with U.S. Attorney regarding plea discussions', billable: true, status: 'approved' },
    // Matter 55 - O'Malley real estate
    { id: 'te_55', matterId: 'matter_55', userId: 'user_13', date: '2024-04-01', hours: 1.0, rate: 525, description: 'Initial consultation for residential home purchase', billable: true, status: 'approved' },
    { id: 'te_56', matterId: 'matter_55', userId: 'user_7', date: '2024-04-05', hours: 2.0, rate: 150, description: 'Review purchase agreement and title search results', billable: true, status: 'approved' },
    { id: 'te_57', matterId: 'matter_55', userId: 'user_13', date: '2024-04-15', hours: 1.5, rate: 525, description: 'Negotiate inspection contingency modifications', billable: true, status: 'approved' },
    // Matter 63 - Vertex corporate
    { id: 'te_58', matterId: 'matter_63', userId: 'user_4', date: '2024-04-08', hours: 2.0, rate: 600, description: 'Meeting with Vertex board regarding Series B terms', billable: true, status: 'approved' },
    { id: 'te_59', matterId: 'matter_63', userId: 'user_14', date: '2024-04-12', hours: 5.0, rate: 260, description: 'Draft term sheet and review investor requirements', billable: true, status: 'approved' },
    { id: 'te_60', matterId: 'matter_63', userId: 'user_4', date: '2024-05-01', hours: 4.0, rate: 600, description: 'Negotiate investment agreement terms with lead investor counsel', billable: true, status: 'approved' },
    { id: 'te_61', matterId: 'matter_63', userId: 'user_14', date: '2024-05-15', hours: 6.0, rate: 260, description: 'Prepare shareholder agreement and board resolutions', billable: true, status: 'approved' },
    { id: 'te_62', matterId: 'matter_63', userId: 'user_4', date: '2024-06-10', hours: 3.0, rate: 600, description: 'Final review of closing documents and conditions precedent', billable: true, status: 'approved' },
    // Matter 65 - NovaBio FDA
    { id: 'te_63', matterId: 'matter_65', userId: 'user_4', date: '2024-03-12', hours: 3.0, rate: 600, description: 'Review FDA submission package and regulatory strategy', billable: true, status: 'approved' },
    { id: 'te_64', matterId: 'matter_65', userId: 'user_14', date: '2024-03-20', hours: 4.0, rate: 260, description: 'Research FDA guidance documents for drug class', billable: true, status: 'approved' },
    { id: 'te_65', matterId: 'matter_65', userId: 'user_4', date: '2024-04-15', hours: 5.0, rate: 600, description: 'Pre-IND meeting preparation and document review', billable: true, status: 'approved' },
    { id: 'te_66', matterId: 'matter_65', userId: 'user_4', date: '2024-06-01', hours: 4.0, rate: 600, description: 'Attend Type B meeting with FDA', billable: true, status: 'billed' },
    { id: 'te_67', matterId: 'matter_65', userId: 'user_14', date: '2024-07-15', hours: 8.0, rate: 260, description: 'Draft regulatory response to FDA information request', billable: true, status: 'billed' },
    { id: 'te_68', matterId: 'matter_65', userId: 'user_4', date: '2024-09-01', hours: 3.0, rate: 600, description: 'Review Phase II clinical trial data for regulatory implications', billable: true, status: 'approved' },
    // Matter 73 - Li employment
    { id: 'te_69', matterId: 'matter_73', userId: 'user_16', date: '2024-10-12', hours: 1.5, rate: 410, description: 'Initial consultation with Jennifer Li regarding discrimination', billable: true, status: 'approved' },
    { id: 'te_70', matterId: 'matter_73', userId: 'user_9', date: '2024-10-18', hours: 3.0, rate: 145, description: 'Compile employment records and performance reviews', billable: true, status: 'approved' },
    { id: 'te_71', matterId: 'matter_73', userId: 'user_16', date: '2024-11-05', hours: 4.0, rate: 410, description: 'Draft EEOC charge of discrimination', billable: true, status: 'approved' },
    { id: 'te_72', matterId: 'matter_73', userId: 'user_16', date: '2024-12-10', hours: 2.5, rate: 410, description: 'EEOC mediation session', billable: true, status: 'approved' },
    // Matter 74 - Gutierrez wage theft
    { id: 'te_73', matterId: 'matter_74', userId: 'user_16', date: '2024-06-18', hours: 2.0, rate: 410, description: 'Initial class representative interview', billable: true, status: 'approved' },
    { id: 'te_74', matterId: 'matter_74', userId: 'user_9', date: '2024-07-01', hours: 6.0, rate: 145, description: 'Analyze payroll records for 150+ employees', billable: true, status: 'approved' },
    { id: 'te_75', matterId: 'matter_74', userId: 'user_16', date: '2024-08-15', hours: 8.0, rate: 410, description: 'Draft class action complaint and supporting declarations', billable: true, status: 'approved' },
    { id: 'te_76', matterId: 'matter_74', userId: 'user_16', date: '2024-10-01', hours: 5.0, rate: 410, description: 'File motion for class certification', billable: true, status: 'approved' },
    { id: 'te_77', matterId: 'matter_74', userId: 'user_9', date: '2024-11-15', hours: 4.0, rate: 145, description: 'Prepare class notification documents', billable: true, status: 'approved' },
    // Matter 81 - Kowalski estate
    { id: 'te_78', matterId: 'matter_81', userId: 'user_13', date: '2024-07-20', hours: 1.5, rate: 525, description: 'Estate planning consultation with Diane Kowalski', billable: true, status: 'approved' },
    { id: 'te_79', matterId: 'matter_81', userId: 'user_11', date: '2024-07-25', hours: 3.0, rate: 125, description: 'Prepare asset questionnaire and gather financial information', billable: true, status: 'approved' },
    { id: 'te_80', matterId: 'matter_81', userId: 'user_13', date: '2024-08-10', hours: 4.0, rate: 525, description: 'Draft will, revocable living trust, and healthcare directive', billable: true, status: 'approved' },
    // Matter 87 - Mbeki immigration
    { id: 'te_81', matterId: 'matter_87', userId: 'user_10', date: '2024-04-28', hours: 1.0, rate: 285, description: 'Initial H-1B petition consultation', billable: true, status: 'approved' },
    { id: 'te_82', matterId: 'matter_87', userId: 'user_15', date: '2024-05-05', hours: 4.0, rate: 130, description: 'Prepare H-1B petition forms and supporting documentation', billable: true, status: 'approved' },
    { id: 'te_83', matterId: 'matter_87', userId: 'user_10', date: '2024-05-20', hours: 2.0, rate: 285, description: 'Draft specialty occupation support letter and review petition', billable: true, status: 'approved' },
    // Matter 94 - NovaBio patent
    { id: 'te_84', matterId: 'matter_94', userId: 'user_4', date: '2024-03-18', hours: 3.0, rate: 600, description: 'Review patent portfolio and infringement analysis', billable: true, status: 'approved' },
    { id: 'te_85', matterId: 'matter_94', userId: 'user_14', date: '2024-04-01', hours: 8.0, rate: 260, description: 'Detailed claim construction analysis for asserted patents', billable: true, status: 'approved' },
    { id: 'te_86', matterId: 'matter_94', userId: 'user_4', date: '2024-05-15', hours: 6.0, rate: 600, description: 'Draft patent infringement complaint', billable: true, status: 'billed' },
    { id: 'te_87', matterId: 'matter_94', userId: 'user_12', date: '2024-06-20', hours: 5.0, rate: 450, description: 'Review defendant motion to dismiss and prepare opposition', billable: true, status: 'billed' },
    { id: 'te_88', matterId: 'matter_94', userId: 'user_4', date: '2024-08-01', hours: 4.0, rate: 600, description: 'Markman hearing preparation and claim construction brief', billable: true, status: 'approved' },
    { id: 'te_89', matterId: 'matter_94', userId: 'user_14', date: '2024-09-15', hours: 10.0, rate: 260, description: 'Document production review and privilege log preparation', billable: true, status: 'approved' },
    { id: 'te_90', matterId: 'matter_94', userId: 'user_4', date: '2024-11-01', hours: 8.0, rate: 600, description: 'Attend Markman hearing and present claim construction arguments', billable: true, status: 'approved' },
    // Matter 96 - Bay Logistics bankruptcy
    { id: 'te_91', matterId: 'matter_96', userId: 'user_4', date: '2024-04-18', hours: 3.0, rate: 575, description: 'Initial Chapter 11 case assessment and strategy session', billable: true, status: 'approved' },
    { id: 'te_92', matterId: 'matter_96', userId: 'user_14', date: '2024-04-25', hours: 6.0, rate: 260, description: 'Prepare bankruptcy schedules and statement of financial affairs', billable: true, status: 'approved' },
    { id: 'te_93', matterId: 'matter_96', userId: 'user_4', date: '2024-05-10', hours: 4.0, rate: 575, description: 'File Chapter 11 petition and first day motions', billable: true, status: 'approved' },
    { id: 'te_94', matterId: 'matter_96', userId: 'user_4', date: '2024-06-15', hours: 5.0, rate: 575, description: 'Attend 341 meeting of creditors', billable: true, status: 'billed' },
    { id: 'te_95', matterId: 'matter_96', userId: 'user_14', date: '2024-07-20', hours: 8.0, rate: 260, description: 'Draft reorganization plan and disclosure statement', billable: true, status: 'billed' },
    { id: 'te_96', matterId: 'matter_96', userId: 'user_4', date: '2024-09-01', hours: 6.0, rate: 575, description: 'Negotiate with creditor committee on plan terms', billable: true, status: 'approved' },
    // Matters 5, 6, 8 - More PI entries
    { id: 'te_97', matterId: 'matter_5', userId: 'user_2', date: '2024-10-30', hours: 1.5, rate: 425, description: 'Initial consultation regarding scaffolding fall', billable: true, status: 'approved' },
    { id: 'te_98', matterId: 'matter_5', userId: 'user_9', date: '2024-11-05', hours: 3.0, rate: 145, description: 'Obtain construction site safety records and OSHA reports', billable: true, status: 'approved' },
    { id: 'te_99', matterId: 'matter_5', userId: 'user_2', date: '2024-12-01', hours: 2.0, rate: 425, description: 'Research contractor liability and safety regulation violations', billable: true, status: 'approved' },
    { id: 'te_100', matterId: 'matter_6', userId: 'user_8', date: '2024-10-02', hours: 1.5, rate: 400, description: 'Client intake regarding pedestrian accident', billable: true, status: 'approved' },
    { id: 'te_101', matterId: 'matter_6', userId: 'user_7', date: '2024-10-08', hours: 2.0, rate: 150, description: 'Obtain accident report from SFPD', billable: true, status: 'approved' },
    { id: 'te_102', matterId: 'matter_6', userId: 'user_8', date: '2024-11-20', hours: 3.0, rate: 400, description: 'Draft government tort claim against City of SF', billable: true, status: 'approved' },
    { id: 'te_103', matterId: 'matter_8', userId: 'user_8', date: '2024-09-16', hours: 1.5, rate: 400, description: 'Emergency client meeting at trauma center', billable: true, status: 'approved' },
    { id: 'te_104', matterId: 'matter_8', userId: 'user_9', date: '2024-09-20', hours: 2.0, rate: 145, description: 'Gather motorcycle accident evidence and witness info', billable: true, status: 'approved' },
    // More family law
    { id: 'te_105', matterId: 'matter_30', userId: 'user_3', date: '2024-06-24', hours: 2.0, rate: 500, description: 'Initial consultation - high asset divorce', billable: true, status: 'approved' },
    { id: 'te_106', matterId: 'matter_30', userId: 'user_11', date: '2024-07-01', hours: 5.0, rate: 125, description: 'Compile comprehensive financial disclosure for multiple properties', billable: true, status: 'approved' },
    { id: 'te_107', matterId: 'matter_30', userId: 'user_3', date: '2024-08-01', hours: 3.0, rate: 500, description: 'Negotiate temporary support order', billable: true, status: 'approved' },
    { id: 'te_108', matterId: 'matter_30', userId: 'user_3', date: '2024-09-15', hours: 4.0, rate: 500, description: 'Retain forensic accountant for business valuation', billable: true, status: 'approved' },
    { id: 'te_109', matterId: 'matter_30', userId: 'user_11', date: '2024-10-20', hours: 6.0, rate: 125, description: 'Organize retirement account and real property documentation', billable: true, status: 'approved' },
    { id: 'te_110', matterId: 'matter_33', userId: 'user_3', date: '2024-08-06', hours: 2.0, rate: 400, description: 'Emergency DVRO petition preparation and filing', billable: true, status: 'approved' },
    { id: 'te_111', matterId: 'matter_33', userId: 'user_3', date: '2024-08-08', hours: 3.0, rate: 400, description: 'Attend DVRO hearing - temporary restraining order granted', billable: true, status: 'approved' },
    { id: 'te_112', matterId: 'matter_33', userId: 'user_11', date: '2024-08-15', hours: 2.0, rate: 125, description: 'Prepare safety plan and connect client with DV resources', billable: true, status: 'approved' },
    // More corporate
    { id: 'te_113', matterId: 'matter_67', userId: 'user_4', date: '2024-01-22', hours: 4.0, rate: 600, description: 'Fund structure analysis and LP agreement framework', billable: true, status: 'billed' },
    { id: 'te_114', matterId: 'matter_67', userId: 'user_14', date: '2024-02-01', hours: 8.0, rate: 260, description: 'Draft limited partnership agreement and PPM', billable: true, status: 'billed' },
    { id: 'te_115', matterId: 'matter_67', userId: 'user_4', date: '2024-03-15', hours: 3.0, rate: 600, description: 'Negotiate side letter terms with anchor investor', billable: true, status: 'billed' },
    { id: 'te_116', matterId: 'matter_67', userId: 'user_4', date: '2024-05-20', hours: 2.0, rate: 600, description: 'Review regulatory compliance for fund formation', billable: true, status: 'approved' },
    { id: 'te_117', matterId: 'matter_70', userId: 'user_4', date: '2024-03-05', hours: 3.0, rate: 600, description: 'Initial SEC compliance assessment meeting', billable: true, status: 'approved' },
    { id: 'te_118', matterId: 'matter_70', userId: 'user_14', date: '2024-03-15', hours: 6.0, rate: 260, description: 'Review existing compliance policies against current SEC rules', billable: true, status: 'approved' },
    { id: 'te_119', matterId: 'matter_70', userId: 'user_4', date: '2024-04-20', hours: 4.0, rate: 600, description: 'Draft advisory opinion on new investment product compliance', billable: true, status: 'approved' },
    { id: 'te_120', matterId: 'matter_70', userId: 'user_4', date: '2024-06-15', hours: 2.0, rate: 600, description: 'Respond to SEC examination request', billable: true, status: 'billed' },
    // More entries to reach 200+
    { id: 'te_121', matterId: 'matter_9', userId: 'user_2', date: '2024-05-02', hours: 1.5, rate: 425, description: 'Initial intake for falling merchandise claim', billable: true, status: 'approved' },
    { id: 'te_122', matterId: 'matter_9', userId: 'user_7', date: '2024-05-10', hours: 2.0, rate: 150, description: 'Obtain store incident report and witness statements', billable: true, status: 'approved' },
    { id: 'te_123', matterId: 'matter_10', userId: 'user_5', date: '2024-11-27', hours: 1.0, rate: 275, description: 'Dog bite case initial client interview', billable: true, status: 'approved' },
    { id: 'te_124', matterId: 'matter_10', userId: 'user_7', date: '2024-12-05', hours: 1.5, rate: 150, description: 'Research dog owner liability and prior bite history', billable: true, status: 'approved' },
    { id: 'te_125', matterId: 'matter_13', userId: 'user_2', date: '2024-11-20', hours: 1.5, rate: 425, description: 'Client meeting regarding Uber rear-end collision', billable: true, status: 'approved' },
    { id: 'te_126', matterId: 'matter_13', userId: 'user_7', date: '2024-12-01', hours: 2.5, rate: 150, description: 'Compile medical documentation and treatment timeline', billable: true, status: 'approved' },
    { id: 'te_127', matterId: 'matter_13', userId: 'user_2', date: '2025-01-15', hours: 3.0, rate: 425, description: 'Prepare demand package to James River Insurance', billable: true, status: 'approved' },
    { id: 'te_128', matterId: 'matter_14', userId: 'user_8', date: '2024-09-10', hours: 2.0, rate: 400, description: 'Initial consultation regarding surgical error claim', billable: true, status: 'approved' },
    { id: 'te_129', matterId: 'matter_14', userId: 'user_7', date: '2024-09-20', hours: 4.0, rate: 150, description: 'Obtain all surgical and post-operative medical records', billable: true, status: 'approved' },
    { id: 'te_130', matterId: 'matter_14', userId: 'user_8', date: '2024-10-15', hours: 3.0, rate: 400, description: 'Retain medical expert and review case with surgeon', billable: true, status: 'approved' },
    { id: 'te_131', matterId: 'matter_14', userId: 'user_5', date: '2024-11-01', hours: 5.0, rate: 275, description: 'Research Kaiser internal incident reports via discovery', billable: true, status: 'approved' },
    { id: 'te_132', matterId: 'matter_14', userId: 'user_8', date: '2024-12-01', hours: 6.0, rate: 400, description: 'Draft medical malpractice complaint with expert declaration', billable: true, status: 'approved' },
    { id: 'te_133', matterId: 'matter_29', userId: 'user_3', date: '2024-09-08', hours: 1.5, rate: 475, description: 'Client meeting regarding custody modification request', billable: true, status: 'approved' },
    { id: 'te_134', matterId: 'matter_29', userId: 'user_9', date: '2024-09-15', hours: 3.0, rate: 145, description: 'Prepare motion for modification of custody order', billable: true, status: 'approved' },
    { id: 'te_135', matterId: 'matter_29', userId: 'user_3', date: '2024-10-20', hours: 4.0, rate: 475, description: 'Attend mediation session regarding relocation request', billable: true, status: 'approved' },
    { id: 'te_136', matterId: 'matter_34', userId: 'user_6', date: '2024-04-18', hours: 1.0, rate: 250, description: 'Initial consultation for child support modification', billable: true, status: 'approved' },
    { id: 'te_137', matterId: 'matter_34', userId: 'user_9', date: '2024-05-01', hours: 2.5, rate: 145, description: 'Prepare income and expense declarations', billable: true, status: 'approved' },
    { id: 'te_138', matterId: 'matter_34', userId: 'user_6', date: '2024-06-15', hours: 3.0, rate: 250, description: 'Hearing on motion to modify child support', billable: true, status: 'approved' },
    { id: 'te_139', matterId: 'matter_40', userId: 'user_3', date: '2024-10-03', hours: 2.0, rate: 400, description: 'File petition for dissolution following DVRO', billable: true, status: 'approved' },
    { id: 'te_140', matterId: 'matter_40', userId: 'user_11', date: '2024-10-15', hours: 3.0, rate: 125, description: 'Prepare financial disclosures and asset lists', billable: true, status: 'approved' },
    { id: 'te_141', matterId: 'matter_40', userId: 'user_3', date: '2024-12-01', hours: 4.0, rate: 400, description: 'Discovery conference and document exchange', billable: true, status: 'approved' },
    { id: 'te_142', matterId: 'matter_45', userId: 'user_8', date: '2024-08-02', hours: 1.0, rate: 400, description: 'Initial meeting regarding drug possession charge', billable: true, status: 'approved' },
    { id: 'te_143', matterId: 'matter_45', userId: 'user_5', date: '2024-08-15', hours: 2.0, rate: 275, description: 'Research diversion program eligibility requirements', billable: true, status: 'approved' },
    { id: 'te_144', matterId: 'matter_48', userId: 'user_5', date: '2024-12-10', hours: 1.5, rate: 275, description: 'Initial client meeting for felony DUI defense', billable: true, status: 'approved' },
    { id: 'te_145', matterId: 'matter_48', userId: 'user_15', date: '2024-12-15', hours: 2.0, rate: 130, description: 'Obtain BAC test records and DMV administrative hearing docs', billable: true, status: 'approved' },
    { id: 'te_146', matterId: 'matter_56', userId: 'user_13', date: '2024-02-18', hours: 2.0, rate: 525, description: 'Review commercial lease terms for office building', billable: true, status: 'approved' },
    { id: 'te_147', matterId: 'matter_56', userId: 'user_6', date: '2024-03-01', hours: 4.0, rate: 250, description: 'Draft lease amendment and tenant improvement addendum', billable: true, status: 'approved' },
    { id: 'te_148', matterId: 'matter_56', userId: 'user_13', date: '2024-04-15', hours: 3.0, rate: 525, description: 'Negotiate rent escalation and option to renew clauses', billable: true, status: 'approved' },
    { id: 'te_149', matterId: 'matter_60', userId: 'user_13', date: '2024-05-20', hours: 2.0, rate: 525, description: 'Review eviction procedures and tenant rights', billable: true, status: 'approved' },
    { id: 'te_150', matterId: 'matter_60', userId: 'user_6', date: '2024-06-01', hours: 3.0, rate: 250, description: 'Draft 3-day notice and unlawful detainer complaint', billable: true, status: 'approved' },
    { id: 'te_151', matterId: 'matter_64', userId: 'user_12', date: '2024-02-01', hours: 3.0, rate: 450, description: 'Initial assessment of import/export compliance issues', billable: true, status: 'approved' },
    { id: 'te_152', matterId: 'matter_64', userId: 'user_14', date: '2024-02-15', hours: 5.0, rate: 260, description: 'Review customs documentation and tariff classifications', billable: true, status: 'approved' },
    { id: 'te_153', matterId: 'matter_64', userId: 'user_12', date: '2024-04-01', hours: 4.0, rate: 450, description: 'Draft trade compliance policy manual', billable: true, status: 'approved' },
    { id: 'te_154', matterId: 'matter_69', userId: 'user_12', date: '2024-07-01', hours: 2.0, rate: 450, description: 'Initial franchise structure consultation', billable: true, status: 'approved' },
    { id: 'te_155', matterId: 'matter_69', userId: 'user_14', date: '2024-07-15', hours: 4.0, rate: 260, description: 'Draft franchise disclosure document (FDD)', billable: true, status: 'approved' },
    { id: 'te_156', matterId: 'matter_71', userId: 'user_12', date: '2024-02-22', hours: 2.0, rate: 450, description: 'Review existing SaaS license agreements', billable: true, status: 'approved' },
    { id: 'te_157', matterId: 'matter_71', userId: 'user_14', date: '2024-03-05', hours: 5.0, rate: 260, description: 'Draft CCPA/GDPR compliant privacy policy', billable: true, status: 'approved' },
    { id: 'te_158', matterId: 'matter_72', userId: 'user_12', date: '2024-02-12', hours: 2.0, rate: 450, description: 'Partnership dissolution strategy meeting', billable: true, status: 'approved' },
    { id: 'te_159', matterId: 'matter_72', userId: 'user_14', date: '2024-03-01', hours: 4.0, rate: 260, description: 'Value partnership assets and prepare distribution proposal', billable: true, status: 'approved' },
    { id: 'te_160', matterId: 'matter_75', userId: 'user_16', date: '2024-10-20', hours: 1.5, rate: 410, description: 'Whistleblower case initial consultation', billable: true, status: 'approved' },
    { id: 'te_161', matterId: 'matter_75', userId: 'user_9', date: '2024-11-01', hours: 3.0, rate: 145, description: 'Compile whistleblower documentation and timeline', billable: true, status: 'approved' },
    { id: 'te_162', matterId: 'matter_80', userId: 'user_16', date: '2024-09-15', hours: 2.0, rate: 410, description: 'OSHA citation review and defense strategy', billable: true, status: 'approved' },
    { id: 'te_163', matterId: 'matter_80', userId: 'user_9', date: '2024-09-25', hours: 4.0, rate: 145, description: 'Compile restaurant safety records and training logs', billable: true, status: 'approved' },
    { id: 'te_164', matterId: 'matter_82', userId: 'user_13', date: '2024-08-20', hours: 2.0, rate: 525, description: 'Special needs trust planning consultation', billable: true, status: 'approved' },
    { id: 'te_165', matterId: 'matter_83', userId: 'user_13', date: '2024-10-08', hours: 3.0, rate: 525, description: 'Probate petition preparation and beneficiary notification', billable: true, status: 'approved' },
    { id: 'te_166', matterId: 'matter_83', userId: 'user_11', date: '2024-10-20', hours: 5.0, rate: 125, description: 'Compile estate inventory and asset valuations', billable: true, status: 'approved' },
    { id: 'te_167', matterId: 'matter_88', userId: 'user_10', date: '2024-08-15', hours: 3.0, rate: 285, description: 'Prepare asylum declaration and supporting evidence', billable: false, status: 'approved' },
    { id: 'te_168', matterId: 'matter_88', userId: 'user_15', date: '2024-09-01', hours: 4.0, rate: 130, description: 'Research country conditions and gather supporting documentation', billable: false, status: 'approved' },
    { id: 'te_169', matterId: 'matter_88', userId: 'user_10', date: '2024-10-15', hours: 5.0, rate: 285, description: 'Asylum interview preparation and mock interview', billable: false, status: 'approved' },
    { id: 'te_170', matterId: 'matter_92', userId: 'user_12', date: '2024-05-12', hours: 3.0, rate: 450, description: 'Patent application prior art search review', billable: true, status: 'approved' },
    { id: 'te_171', matterId: 'matter_92', userId: 'user_14', date: '2024-06-01', hours: 8.0, rate: 260, description: 'Draft patent application claims and specifications', billable: true, status: 'approved' },
    { id: 'te_172', matterId: 'matter_100', userId: 'user_4', date: '2024-06-05', hours: 3.0, rate: 600, description: 'Initial IRS audit response strategy meeting', billable: true, status: 'approved' },
    { id: 'te_173', matterId: 'matter_100', userId: 'user_14', date: '2024-06-15', hours: 6.0, rate: 260, description: 'Review tax returns and prepare document production', billable: true, status: 'approved' },
    { id: 'te_174', matterId: 'matter_100', userId: 'user_4', date: '2024-08-01', hours: 4.0, rate: 600, description: 'Attend IRS examination conference', billable: true, status: 'billed' },
    { id: 'te_175', matterId: 'matter_107', userId: 'user_12', date: '2024-07-18', hours: 2.0, rate: 450, description: 'CEQA compliance assessment for waterfront project', billable: true, status: 'approved' },
    { id: 'te_176', matterId: 'matter_107', userId: 'user_14', date: '2024-08-01', hours: 5.0, rate: 260, description: 'Prepare environmental impact assessment documentation', billable: true, status: 'approved' },
    // Additional diverse entries
    { id: 'te_177', matterId: 'matter_15', userId: 'user_8', date: '2024-09-22', hours: 2.0, rate: 400, description: 'Review misdiagnosis case records with medical expert', billable: true, status: 'approved' },
    { id: 'te_178', matterId: 'matter_15', userId: 'user_9', date: '2024-10-01', hours: 4.0, rate: 145, description: 'Compile breast cancer treatment timeline and delay analysis', billable: true, status: 'approved' },
    { id: 'te_179', matterId: 'matter_15', userId: 'user_8', date: '2024-11-15', hours: 6.0, rate: 400, description: 'Draft medical malpractice complaint with expert cert', billable: true, status: 'approved' },
    { id: 'te_180', matterId: 'matter_24', userId: 'user_8', date: '2024-10-18', hours: 1.5, rate: 400, description: 'Client intake for electrical shock injury', billable: true, status: 'approved' },
    { id: 'te_181', matterId: 'matter_24', userId: 'user_7', date: '2024-10-25', hours: 3.0, rate: 150, description: 'Research PG&E inspection records for client address', billable: true, status: 'approved' },
    { id: 'te_182', matterId: 'matter_24', userId: 'user_8', date: '2024-11-10', hours: 4.0, rate: 400, description: 'Draft demand letter to PG&E legal department', billable: true, status: 'approved' },
    { id: 'te_183', matterId: 'matter_35', userId: 'user_3', date: '2025-01-10', hours: 2.0, rate: 475, description: 'Initial divorce consultation with business valuation issues', billable: true, status: 'approved' },
    { id: 'te_184', matterId: 'matter_35', userId: 'user_11', date: '2025-01-20', hours: 3.0, rate: 125, description: 'Prepare preliminary financial disclosure', billable: true, status: 'approved' },
    { id: 'te_185', matterId: 'matter_37', userId: 'user_6', date: '2025-02-17', hours: 1.5, rate: 250, description: 'Guardianship petition consultation', billable: true, status: 'approved' },
    { id: 'te_186', matterId: 'matter_37', userId: 'user_11', date: '2025-02-22', hours: 2.0, rate: 125, description: 'Prepare guardianship petition and medical evaluation', billable: true, status: 'approved' },
    { id: 'te_187', matterId: 'matter_58', userId: 'user_13', date: '2024-12-08', hours: 2.0, rate: 525, description: 'Review zoning dispute and prepare opposition', billable: true, status: 'approved' },
    { id: 'te_188', matterId: 'matter_58', userId: 'user_6', date: '2024-12-20', hours: 3.0, rate: 250, description: 'Research zoning ordinance history and precedents', billable: true, status: 'approved' },
    { id: 'te_189', matterId: 'matter_62', userId: 'user_13', date: '2025-01-30', hours: 2.0, rate: 525, description: 'Initial assessment of construction defect claims', billable: true, status: 'approved' },
    { id: 'te_190', matterId: 'matter_76', userId: 'user_16', date: '2024-07-05', hours: 2.0, rate: 410, description: 'Sexual harassment case intake and evidence review', billable: true, status: 'approved' },
    { id: 'te_191', matterId: 'matter_76', userId: 'user_9', date: '2024-07-15', hours: 4.0, rate: 145, description: 'Document workplace communications and incident timeline', billable: true, status: 'approved' },
    { id: 'te_192', matterId: 'matter_76', userId: 'user_16', date: '2024-09-01', hours: 3.0, rate: 410, description: 'File complaint with DFEH', billable: true, status: 'approved' },
    { id: 'te_193', matterId: 'matter_89', userId: 'user_10', date: '2025-01-25', hours: 2.0, rate: 285, description: 'EB-2 NIW petition strategy and evidence planning', billable: true, status: 'approved' },
    { id: 'te_194', matterId: 'matter_89', userId: 'user_15', date: '2025-02-05', hours: 5.0, rate: 130, description: 'Prepare NIW petition with supporting documentation', billable: true, status: 'approved' },
    { id: 'te_195', matterId: 'matter_95', userId: 'user_12', date: '2024-12-05', hours: 2.0, rate: 450, description: 'Copyright infringement analysis for mobile app', billable: true, status: 'approved' },
    { id: 'te_196', matterId: 'matter_95', userId: 'user_14', date: '2024-12-15', hours: 4.0, rate: 260, description: 'Draft copyright infringement complaint', billable: true, status: 'approved' },
    { id: 'te_197', matterId: 'matter_99', userId: 'user_4', date: '2025-02-18', hours: 3.0, rate: 575, description: 'Chapter 11 Sub V case planning and strategy', billable: true, status: 'pending' },
    { id: 'te_198', matterId: 'matter_99', userId: 'user_14', date: '2025-02-25', hours: 4.0, rate: 260, description: 'Prepare financial statements for bankruptcy petition', billable: true, status: 'draft' },
    { id: 'te_199', matterId: 'matter_104', userId: 'user_8', date: '2025-01-08', hours: 2.0, rate: 400, description: 'Medical malpractice intake - nerve damage claim', billable: true, status: 'approved' },
    { id: 'te_200', matterId: 'matter_104', userId: 'user_7', date: '2025-01-15', hours: 3.0, rate: 150, description: 'Obtain surgical records and pathology reports', billable: true, status: 'approved' },
    { id: 'te_201', matterId: 'matter_119', userId: 'user_4', date: '2025-01-08', hours: 4.0, rate: 600, description: 'Review source code comparison and trade secret analysis', billable: true, status: 'approved' },
    { id: 'te_202', matterId: 'matter_119', userId: 'user_12', date: '2025-01-20', hours: 5.0, rate: 450, description: 'Draft TRO motion for trade secret misappropriation', billable: true, status: 'approved' },
    { id: 'te_203', matterId: 'matter_119', userId: 'user_14', date: '2025-02-01', hours: 8.0, rate: 260, description: 'Prepare exhibit binder and forensic expert declaration', billable: true, status: 'pending' },
    { id: 'te_204', matterId: 'matter_111', userId: 'user_12', date: '2025-02-20', hours: 3.0, rate: 450, description: 'Due diligence kickoff and document request list', billable: true, status: 'draft' },
    { id: 'te_205', matterId: 'matter_115', userId: 'user_4', date: '2025-01-12', hours: 2.0, rate: 600, description: 'Board governance restructuring strategy session', billable: true, status: 'approved' },
    { id: 'te_206', matterId: 'matter_115', userId: 'user_14', date: '2025-01-25', hours: 4.0, rate: 260, description: 'Draft amended bylaws and board committee charters', billable: true, status: 'approved' },
    { id: 'te_207', matterId: 'matter_118', userId: 'user_16', date: '2025-02-15', hours: 2.0, rate: 410, description: 'Breach of fiduciary duty case assessment', billable: true, status: 'pending' },
    { id: 'te_208', matterId: 'matter_120', userId: 'user_8', date: '2025-03-01', hours: 1.5, rate: 400, description: 'Initial client meeting regarding insurance fraud charge', billable: true, status: 'draft' }
];

const EXPENSES = [
    { id: 'exp_1', matterId: 'matter_1', userId: 'user_7', date: '2024-04-02', amount: 350.00, category: 'Filing Fees', description: 'Court filing fee - Complaint', billable: true },
    { id: 'exp_2', matterId: 'matter_1', userId: 'user_7', date: '2024-04-10', amount: 125.00, category: 'Medical Records', description: 'SF General medical records retrieval fee', billable: true },
    { id: 'exp_3', matterId: 'matter_1', userId: 'user_7', date: '2024-05-15', amount: 75.00, category: 'Copying/Printing', description: 'Copying medical records - 300 pages', billable: true },
    { id: 'exp_4', matterId: 'matter_1', userId: 'user_2', date: '2024-06-20', amount: 250.00, category: 'Service of Process', description: 'Process server for complaint service on MTA', billable: true },
    { id: 'exp_5', matterId: 'matter_2', userId: 'user_7', date: '2024-05-22', amount: 45.00, category: 'Postage', description: 'Certified mail - preservation letters', billable: true },
    { id: 'exp_6', matterId: 'matter_2', userId: 'user_7', date: '2024-06-15', amount: 175.00, category: 'Medical Records', description: 'UCSF medical records request fee', billable: true },
    { id: 'exp_7', matterId: 'matter_3', userId: 'user_9', date: '2024-06-20', amount: 435.00, category: 'Filing Fees', description: 'San Mateo County Superior Court filing fee', billable: true },
    { id: 'exp_8', matterId: 'matter_3', userId: 'user_9', date: '2024-07-25', amount: 300.00, category: 'Service of Process', description: 'Service of summons on Lyft registered agent', billable: true },
    { id: 'exp_9', matterId: 'matter_3', userId: 'user_2', date: '2024-09-20', amount: 2500.00, category: 'Mediation Fees', description: 'Private mediation - half day session', billable: true },
    { id: 'exp_10', matterId: 'matter_4', userId: 'user_7', date: '2024-05-01', amount: 350.00, category: 'Filing Fees', description: 'Complaint filing fee', billable: true },
    { id: 'exp_11', matterId: 'matter_4', userId: 'user_7', date: '2024-06-15', amount: 200.00, category: 'Medical Records', description: 'SF General records retrieval - hand surgery', billable: true },
    { id: 'exp_12', matterId: 'matter_4', userId: 'user_7', date: '2024-07-10', amount: 450.00, category: 'Investigation', description: 'Workplace safety investigator retainer', billable: true },
    { id: 'exp_13', matterId: 'matter_4', userId: 'user_8', date: '2024-09-18', amount: 1800.00, category: 'Deposition Costs', description: 'Court reporter for safety manager deposition', billable: true },
    { id: 'exp_14', matterId: 'matter_7', userId: 'user_7', date: '2024-08-05', amount: 435.00, category: 'Filing Fees', description: 'Federal court filing fee', billable: true },
    { id: 'exp_15', matterId: 'matter_7', userId: 'user_7', date: '2024-09-01', amount: 5000.00, category: 'Expert Witness Fees', description: 'Product safety expert initial retainer', billable: true },
    { id: 'exp_16', matterId: 'matter_7', userId: 'user_7', date: '2024-10-15', amount: 1200.00, category: 'Investigation', description: 'Product testing lab fees', billable: true },
    { id: 'exp_17', matterId: 'matter_7', userId: 'user_2', date: '2024-11-10', amount: 350.00, category: 'Service of Process', description: 'International service on manufacturer', billable: true },
    { id: 'exp_18', matterId: 'matter_14', userId: 'user_7', date: '2024-09-25', amount: 7500.00, category: 'Expert Witness Fees', description: 'Surgical expert review - medical malpractice case', billable: true },
    { id: 'exp_19', matterId: 'matter_14', userId: 'user_7', date: '2024-10-10', amount: 350.00, category: 'Filing Fees', description: 'Medical malpractice complaint filing fee', billable: true },
    { id: 'exp_20', matterId: 'matter_14', userId: 'user_7', date: '2024-11-01', amount: 250.00, category: 'Medical Records', description: 'Kaiser surgical records retrieval', billable: true },
    { id: 'exp_21', matterId: 'matter_28', userId: 'user_11', date: '2024-01-25', amount: 435.00, category: 'Filing Fees', description: 'Petition for dissolution filing fee', billable: true },
    { id: 'exp_22', matterId: 'matter_28', userId: 'user_11', date: '2024-04-10', amount: 3500.00, category: 'Expert Witness Fees', description: 'Forensic accountant for property valuation', billable: true },
    { id: 'exp_23', matterId: 'matter_28', userId: 'user_11', date: '2024-06-15', amount: 2800.00, category: 'Expert Witness Fees', description: 'Custody evaluator fee', billable: true },
    { id: 'exp_24', matterId: 'matter_28', userId: 'user_3', date: '2024-08-10', amount: 150.00, category: 'Travel', description: 'Mileage to Santa Clara County courthouse', billable: true },
    { id: 'exp_25', matterId: 'matter_30', userId: 'user_11', date: '2024-07-05', amount: 435.00, category: 'Filing Fees', description: 'High asset divorce petition filing', billable: true },
    { id: 'exp_26', matterId: 'matter_30', userId: 'user_11', date: '2024-08-20', amount: 5000.00, category: 'Expert Witness Fees', description: 'Forensic accountant - business valuation', billable: true },
    { id: 'exp_27', matterId: 'matter_30', userId: 'user_11', date: '2024-09-10', amount: 2500.00, category: 'Expert Witness Fees', description: 'Real estate appraiser for 3 properties', billable: true },
    { id: 'exp_28', matterId: 'matter_33', userId: 'user_11', date: '2024-08-06', amount: 0, category: 'Filing Fees', description: 'DVRO filing fee - waived for DV victims', billable: false },
    { id: 'exp_29', matterId: 'matter_44', userId: 'user_15', date: '2024-09-10', amount: 500.00, category: 'Investigation', description: 'Private investigator for witness location', billable: true },
    { id: 'exp_30', matterId: 'matter_44', userId: 'user_8', date: '2024-10-15', amount: 85.00, category: 'Copying/Printing', description: 'Discovery document reproduction', billable: true },
    { id: 'exp_31', matterId: 'matter_46', userId: 'user_15', date: '2024-07-20', amount: 1500.00, category: 'Investigation', description: 'Private investigator - alibi verification', billable: true },
    { id: 'exp_32', matterId: 'matter_46', userId: 'user_5', date: '2024-08-10', amount: 2200.00, category: 'Expert Witness Fees', description: 'Forensic video analysis expert', billable: true },
    { id: 'exp_33', matterId: 'matter_46', userId: 'user_15', date: '2024-09-05', amount: 350.00, category: 'Transcripts', description: 'Preliminary hearing transcript', billable: true },
    { id: 'exp_34', matterId: 'matter_47', userId: 'user_15', date: '2025-01-10', amount: 10000.00, category: 'Expert Witness Fees', description: 'Forensic accounting expert - securities analysis', billable: true },
    { id: 'exp_35', matterId: 'matter_47', userId: 'user_15', date: '2025-01-15', amount: 250.00, category: 'Copying/Printing', description: 'Financial record reproduction - 1000+ pages', billable: true },
    { id: 'exp_36', matterId: 'matter_55', userId: 'user_7', date: '2024-04-08', amount: 450.00, category: 'Other', description: 'Title search fee', billable: true },
    { id: 'exp_37', matterId: 'matter_55', userId: 'user_7', date: '2024-04-15', amount: 125.00, category: 'Postage', description: 'Overnight delivery - closing documents', billable: true },
    { id: 'exp_38', matterId: 'matter_56', userId: 'user_6', date: '2024-03-10', amount: 85.00, category: 'Copying/Printing', description: 'Lease document printing and binding', billable: true },
    { id: 'exp_39', matterId: 'matter_63', userId: 'user_14', date: '2024-04-15', amount: 500.00, category: 'Filing Fees', description: 'Delaware corporate filing fees', billable: true },
    { id: 'exp_40', matterId: 'matter_63', userId: 'user_14', date: '2024-05-10', amount: 2500.00, category: 'Other', description: 'Bloomberg terminal access for financial analysis', billable: true },
    { id: 'exp_41', matterId: 'matter_65', userId: 'user_14', date: '2024-04-01', amount: 1500.00, category: 'Research', description: 'FDA regulatory database subscription access', billable: true },
    { id: 'exp_42', matterId: 'matter_65', userId: 'user_4', date: '2024-06-01', amount: 850.00, category: 'Travel', description: 'Travel to FDA headquarters for Type B meeting', billable: true },
    { id: 'exp_43', matterId: 'matter_67', userId: 'user_14', date: '2024-02-10', amount: 750.00, category: 'Filing Fees', description: 'Delaware LP formation and filing', billable: true },
    { id: 'exp_44', matterId: 'matter_70', userId: 'user_14', date: '2024-04-01', amount: 2000.00, category: 'Research', description: 'SEC compliance research database access', billable: true },
    { id: 'exp_45', matterId: 'matter_73', userId: 'user_9', date: '2024-11-10', amount: 0, category: 'Filing Fees', description: 'EEOC charge filing - no fee', billable: false },
    { id: 'exp_46', matterId: 'matter_74', userId: 'user_9', date: '2024-08-20', amount: 435.00, category: 'Filing Fees', description: 'Federal court class action filing fee', billable: true },
    { id: 'exp_47', matterId: 'matter_74', userId: 'user_16', date: '2024-10-05', amount: 3500.00, category: 'Expert Witness Fees', description: 'Labor economics expert for damages calculation', billable: true },
    { id: 'exp_48', matterId: 'matter_81', userId: 'user_11', date: '2024-08-15', amount: 150.00, category: 'Other', description: 'Notary fees for estate documents', billable: true },
    { id: 'exp_49', matterId: 'matter_83', userId: 'user_11', date: '2024-10-10', amount: 435.00, category: 'Court Costs', description: 'Probate petition filing fee', billable: true },
    { id: 'exp_50', matterId: 'matter_83', userId: 'user_11', date: '2024-11-01', amount: 1200.00, category: 'Expert Witness Fees', description: 'Estate appraisal services', billable: true },
    { id: 'exp_51', matterId: 'matter_87', userId: 'user_15', date: '2024-05-15', amount: 460.00, category: 'Filing Fees', description: 'H-1B petition filing fee', billable: true },
    { id: 'exp_52', matterId: 'matter_87', userId: 'user_15', date: '2024-05-15', amount: 500.00, category: 'Other', description: 'ACWIA training fee', billable: true },
    { id: 'exp_53', matterId: 'matter_88', userId: 'user_15', date: '2024-09-15', amount: 0, category: 'Filing Fees', description: 'Asylum application - no filing fee', billable: false },
    { id: 'exp_54', matterId: 'matter_88', userId: 'user_10', date: '2024-10-01', amount: 350.00, category: 'Other', description: 'Document translation services', billable: false },
    { id: 'exp_55', matterId: 'matter_92', userId: 'user_14', date: '2024-06-15', amount: 1600.00, category: 'Filing Fees', description: 'USPTO patent application filing fees', billable: true },
    { id: 'exp_56', matterId: 'matter_92', userId: 'user_14', date: '2024-05-20', amount: 3000.00, category: 'Research', description: 'Professional prior art search service', billable: true },
    { id: 'exp_57', matterId: 'matter_94', userId: 'user_14', date: '2024-04-10', amount: 435.00, category: 'Filing Fees', description: 'Federal court filing fee - patent infringement', billable: true },
    { id: 'exp_58', matterId: 'matter_94', userId: 'user_4', date: '2024-06-01', amount: 15000.00, category: 'Expert Witness Fees', description: 'Patent claim construction expert retainer', billable: true },
    { id: 'exp_59', matterId: 'matter_94', userId: 'user_14', date: '2024-08-15', amount: 4500.00, category: 'Deposition Costs', description: 'Inventor deposition - court reporter and videographer', billable: true },
    { id: 'exp_60', matterId: 'matter_96', userId: 'user_14', date: '2024-05-01', amount: 1738.00, category: 'Filing Fees', description: 'Chapter 11 petition filing fee', billable: true },
    { id: 'exp_61', matterId: 'matter_96', userId: 'user_14', date: '2024-05-15', amount: 850.00, category: 'Postage', description: 'Certified mail to 200+ creditors', billable: true },
    { id: 'exp_62', matterId: 'matter_96', userId: 'user_4', date: '2024-07-01', amount: 500.00, category: 'Court Costs', description: 'Bankruptcy court appearance fee', billable: true },
    { id: 'exp_63', matterId: 'matter_100', userId: 'user_14', date: '2024-06-20', amount: 250.00, category: 'Copying/Printing', description: 'IRS document production printing', billable: true },
    { id: 'exp_64', matterId: 'matter_100', userId: 'user_4', date: '2024-08-01', amount: 500.00, category: 'Travel', description: 'Travel to IRS Oakland office for examination', billable: true },
    { id: 'exp_65', matterId: 'matter_107', userId: 'user_14', date: '2024-08-15', amount: 8000.00, category: 'Expert Witness Fees', description: 'Environmental impact assessment consultant', billable: true },
    { id: 'exp_66', matterId: 'matter_5', userId: 'user_9', date: '2024-11-10', amount: 350.00, category: 'Medical Records', description: 'Emergency room records retrieval', billable: true },
    { id: 'exp_67', matterId: 'matter_6', userId: 'user_7', date: '2024-10-10', amount: 50.00, category: 'Postage', description: 'Government tort claim certified mail', billable: true },
    { id: 'exp_68', matterId: 'matter_8', userId: 'user_9', date: '2024-09-22', amount: 125.00, category: 'Medical Records', description: 'UCSF neurology records', billable: true },
    { id: 'exp_69', matterId: 'matter_13', userId: 'user_7', date: '2024-12-10', amount: 175.00, category: 'Medical Records', description: 'Cervical spine treatment records', billable: true },
    { id: 'exp_70', matterId: 'matter_15', userId: 'user_9', date: '2024-10-15', amount: 350.00, category: 'Medical Records', description: 'Cancer treatment records retrieval', billable: true },
    { id: 'exp_71', matterId: 'matter_15', userId: 'user_8', date: '2024-11-20', amount: 10000.00, category: 'Expert Witness Fees', description: 'Oncology expert witness retainer', billable: true },
    { id: 'exp_72', matterId: 'matter_29', userId: 'user_9', date: '2024-09-20', amount: 435.00, category: 'Filing Fees', description: 'Motion to modify custody filing fee', billable: true },
    { id: 'exp_73', matterId: 'matter_40', userId: 'user_11', date: '2024-10-05', amount: 435.00, category: 'Filing Fees', description: 'Petition for dissolution filing fee', billable: true },
    { id: 'exp_74', matterId: 'matter_45', userId: 'user_5', date: '2024-08-20', amount: 100.00, category: 'Copying/Printing', description: 'Discovery packet copying', billable: true },
    { id: 'exp_75', matterId: 'matter_48', userId: 'user_15', date: '2024-12-18', amount: 75.00, category: 'Postage', description: 'DMV hearing request certified mail', billable: true },
    { id: 'exp_76', matterId: 'matter_60', userId: 'user_6', date: '2024-06-10', amount: 435.00, category: 'Filing Fees', description: 'Unlawful detainer complaint filing', billable: true },
    { id: 'exp_77', matterId: 'matter_60', userId: 'user_6', date: '2024-06-15', amount: 200.00, category: 'Service of Process', description: 'Tenant service of 3-day notice', billable: true },
    { id: 'exp_78', matterId: 'matter_75', userId: 'user_9', date: '2024-11-05', amount: 0, category: 'Filing Fees', description: 'DFEH complaint filing - no fee', billable: false },
    { id: 'exp_79', matterId: 'matter_80', userId: 'user_9', date: '2024-09-30', amount: 250.00, category: 'Copying/Printing', description: 'OSHA document production copies', billable: true },
    { id: 'exp_80', matterId: 'matter_105', userId: 'user_7', date: '2024-03-10', amount: 350.00, category: 'Filing Fees', description: 'Medical malpractice complaint filing', billable: true },
    { id: 'exp_81', matterId: 'matter_105', userId: 'user_7', date: '2024-04-01', amount: 12000.00, category: 'Expert Witness Fees', description: 'Cardiology expert - case review and testimony', billable: true },
    { id: 'exp_82', matterId: 'matter_119', userId: 'user_14', date: '2025-01-10', amount: 435.00, category: 'Filing Fees', description: 'Federal court filing fee - trade secret case', billable: true },
    { id: 'exp_83', matterId: 'matter_119', userId: 'user_14', date: '2025-01-25', amount: 8000.00, category: 'Expert Witness Fees', description: 'Source code forensic analysis expert', billable: true },
    { id: 'exp_84', matterId: 'matter_24', userId: 'user_7', date: '2024-10-30', amount: 300.00, category: 'Investigation', description: 'Electrical inspection report for apartment', billable: true },
    { id: 'exp_85', matterId: 'matter_35', userId: 'user_11', date: '2025-01-15', amount: 435.00, category: 'Filing Fees', description: 'Divorce petition filing fee', billable: true }
];

const ACTIVITY_LOG = [
    { id: 'log_1', matterId: 'matter_1', userId: 'user_1', action: 'created', entityType: 'matter', entityId: 'matter_1', details: 'Created matter Patterson v. Metro Transit Authority', timestamp: '2024-03-18T14:30:00Z' },
    { id: 'log_2', matterId: 'matter_1', userId: 'user_1', action: 'edited', entityType: 'matter', entityId: 'matter_1', details: 'Assigned Marcus Williams as responsible attorney', timestamp: '2024-03-18T14:35:00Z' },
    { id: 'log_3', matterId: 'matter_1', userId: 'user_2', action: 'stage_changed', entityType: 'matter', entityId: 'matter_1', details: 'Changed stage from Intake to Investigation', timestamp: '2024-04-15T10:00:00Z' },
    { id: 'log_4', matterId: 'matter_1', userId: 'user_2', action: 'stage_changed', entityType: 'matter', entityId: 'matter_1', details: 'Changed stage from Investigation to Demand', timestamp: '2024-06-20T14:30:00Z' },
    { id: 'log_5', matterId: 'matter_1', userId: 'user_7', action: 'edited', entityType: 'matter', entityId: 'matter_1', details: 'Added related contact Linda Patterson (Spouse)', timestamp: '2024-03-20T09:00:00Z' },
    { id: 'log_6', matterId: 'matter_2', userId: 'user_2', action: 'created', entityType: 'matter', entityId: 'matter_2', details: 'Created matter Johnson v. Whole Foods Market', timestamp: '2024-05-14T09:00:00Z' },
    { id: 'log_7', matterId: 'matter_3', userId: 'user_1', action: 'created', entityType: 'matter', entityId: 'matter_3', details: 'Created matter Russo v. Lyft Inc.', timestamp: '2024-05-30T11:20:00Z' },
    { id: 'log_8', matterId: 'matter_3', userId: 'user_2', action: 'status_changed', entityType: 'matter', entityId: 'matter_3', details: 'Changed status from Open to Pending', timestamp: '2025-04-10T09:00:00Z' },
    { id: 'log_9', matterId: 'matter_3', userId: 'user_2', action: 'status_changed', entityType: 'matter', entityId: 'matter_3', details: 'Changed status from Pending to Closed - settlement finalized', timestamp: '2025-06-15T16:00:00Z' },
    { id: 'log_10', matterId: 'matter_4', userId: 'user_2', action: 'created', entityType: 'matter', entityId: 'matter_4', details: 'Created matter Washington v. Pacific Steel Works', timestamp: '2024-04-19T10:15:00Z' },
    { id: 'log_11', matterId: 'matter_4', userId: 'user_8', action: 'stage_changed', entityType: 'matter', entityId: 'matter_4', details: 'Changed stage from Investigation to Demand', timestamp: '2024-06-01T11:00:00Z' },
    { id: 'log_12', matterId: 'matter_4', userId: 'user_8', action: 'stage_changed', entityType: 'matter', entityId: 'matter_4', details: 'Changed stage from Demand to Litigation', timestamp: '2024-08-15T09:30:00Z' },
    { id: 'log_13', matterId: 'matter_7', userId: 'user_2', action: 'created', entityType: 'matter', entityId: 'matter_7', details: 'Created matter Okafor v. HomeComfort Appliances', timestamp: '2024-07-21T15:30:00Z' },
    { id: 'log_14', matterId: 'matter_7', userId: 'user_1', action: 'permission_changed', entityType: 'matter', entityId: 'matter_7', details: 'Changed permissions to Specific - restricted access', timestamp: '2024-07-22T09:00:00Z' },
    { id: 'log_15', matterId: 'matter_7', userId: 'user_1', action: 'edited', entityType: 'matter', entityId: 'matter_7', details: 'Blocked user James Cooper from matter access', timestamp: '2024-07-22T09:05:00Z' },
    { id: 'log_16', matterId: 'matter_28', userId: 'user_1', action: 'created', entityType: 'matter', entityId: 'matter_28', details: 'Created matter Gonzalez Divorce', timestamp: '2024-01-11T10:00:00Z' },
    { id: 'log_17', matterId: 'matter_28', userId: 'user_3', action: 'stage_changed', entityType: 'matter', entityId: 'matter_28', details: 'Changed stage from Consultation to Filing', timestamp: '2024-01-25T14:00:00Z' },
    { id: 'log_18', matterId: 'matter_28', userId: 'user_3', action: 'stage_changed', entityType: 'matter', entityId: 'matter_28', details: 'Changed stage from Filing to Discovery', timestamp: '2024-04-01T10:00:00Z' },
    { id: 'log_19', matterId: 'matter_30', userId: 'user_1', action: 'created', entityType: 'matter', entityId: 'matter_30', details: 'Created matter Blackwell Divorce - High Asset', timestamp: '2024-06-21T09:30:00Z' },
    { id: 'log_20', matterId: 'matter_30', userId: 'user_1', action: 'permission_changed', entityType: 'matter', entityId: 'matter_30', details: 'Set restricted permissions for high-asset case', timestamp: '2024-06-21T09:35:00Z' },
    { id: 'log_21', matterId: 'matter_33', userId: 'user_1', action: 'created', entityType: 'matter', entityId: 'matter_33', details: 'Created matter Stone v. Stone - DV protective order', timestamp: '2024-08-05T16:30:00Z' },
    { id: 'log_22', matterId: 'matter_33', userId: 'user_1', action: 'permission_changed', entityType: 'matter', entityId: 'matter_33', details: 'Restricted access due to DV safety concerns', timestamp: '2024-08-05T16:35:00Z' },
    { id: 'log_23', matterId: 'matter_44', userId: 'user_1', action: 'created', entityType: 'matter', entityId: 'matter_44', details: 'Created matter People v. Thompson - Felony assault', timestamp: '2024-08-24T14:30:00Z' },
    { id: 'log_24', matterId: 'matter_46', userId: 'user_1', action: 'created', entityType: 'matter', entityId: 'matter_46', details: 'Created matter People v. Hernandez - Armed robbery', timestamp: '2024-07-05T11:00:00Z' },
    { id: 'log_25', matterId: 'matter_46', userId: 'user_8', action: 'stage_changed', entityType: 'matter', entityId: 'matter_46', details: 'Changed stage from Pre-Trial to Trial', timestamp: '2025-01-15T09:00:00Z' },
    { id: 'log_26', matterId: 'matter_47', userId: 'user_4', action: 'created', entityType: 'matter', entityId: 'matter_47', details: 'Created matter People v. Franklin - Securities fraud', timestamp: '2024-12-19T15:00:00Z' },
    { id: 'log_27', matterId: 'matter_49', userId: 'user_8', action: 'status_changed', entityType: 'matter', entityId: 'matter_49', details: 'Changed status from Open to Closed - plea agreement', timestamp: '2025-01-15T14:00:00Z' },
    { id: 'log_28', matterId: 'matter_55', userId: 'user_1', action: 'created', entityType: 'matter', entityId: 'matter_55', details: "Created matter O'Malley Residential Purchase", timestamp: '2024-03-29T10:00:00Z' },
    { id: 'log_29', matterId: 'matter_63', userId: 'user_1', action: 'created', entityType: 'matter', entityId: 'matter_63', details: 'Created matter Vertex Technologies - Series B', timestamp: '2024-04-04T09:00:00Z' },
    { id: 'log_30', matterId: 'matter_65', userId: 'user_4', action: 'created', entityType: 'matter', entityId: 'matter_65', details: 'Created matter NovaBio Pharmaceuticals - FDA compliance', timestamp: '2024-03-07T10:00:00Z' },
    { id: 'log_31', matterId: 'matter_65', userId: 'user_4', action: 'permission_changed', entityType: 'matter', entityId: 'matter_65', details: 'Restricted access to Corporate & Business group', timestamp: '2024-03-07T10:05:00Z' },
    { id: 'log_32', matterId: 'matter_66', userId: 'user_12', action: 'status_changed', entityType: 'matter', entityId: 'matter_66', details: 'Changed status from Pending to Closed', timestamp: '2025-08-15T11:00:00Z' },
    { id: 'log_33', matterId: 'matter_67', userId: 'user_12', action: 'created', entityType: 'matter', entityId: 'matter_67', details: 'Created matter TechVenture Capital - Fund Formation', timestamp: '2024-01-17T14:00:00Z' },
    { id: 'log_34', matterId: 'matter_73', userId: 'user_1', action: 'created', entityType: 'matter', entityId: 'matter_73', details: 'Created matter Li v. TechCorp - Employment discrimination', timestamp: '2024-10-09T10:00:00Z' },
    { id: 'log_35', matterId: 'matter_74', userId: 'user_16', action: 'created', entityType: 'matter', entityId: 'matter_74', details: 'Created matter Gutierrez v. Bay Area Restaurant - Wage theft', timestamp: '2024-06-14T14:30:00Z' },
    { id: 'log_36', matterId: 'matter_81', userId: 'user_1', action: 'created', entityType: 'matter', entityId: 'matter_81', details: 'Created matter Kowalski Estate Plan', timestamp: '2024-07-17T09:00:00Z' },
    { id: 'log_37', matterId: 'matter_84', userId: 'user_13', action: 'status_changed', entityType: 'matter', entityId: 'matter_84', details: 'Changed status from Pending to Closed - documents executed', timestamp: '2024-10-15T14:00:00Z' },
    { id: 'log_38', matterId: 'matter_87', userId: 'user_1', action: 'created', entityType: 'matter', entityId: 'matter_87', details: 'Created matter Mbeki H-1B Visa Petition', timestamp: '2024-04-24T10:00:00Z' },
    { id: 'log_39', matterId: 'matter_88', userId: 'user_10', action: 'created', entityType: 'matter', entityId: 'matter_88', details: 'Created matter Volkov Asylum Application', timestamp: '2024-08-11T11:15:00Z' },
    { id: 'log_40', matterId: 'matter_94', userId: 'user_4', action: 'created', entityType: 'matter', entityId: 'matter_94', details: 'Created matter NovaBio v. GenericPharma - Patent infringement', timestamp: '2024-03-14T10:00:00Z' },
    { id: 'log_41', matterId: 'matter_96', userId: 'user_12', action: 'created', entityType: 'matter', entityId: 'matter_96', details: 'Created matter Bay Logistics - Chapter 11', timestamp: '2024-04-14T09:00:00Z' },
    { id: 'log_42', matterId: 'matter_100', userId: 'user_4', action: 'created', entityType: 'matter', entityId: 'matter_100', details: 'Created matter Redwood Financial - IRS Audit Defense', timestamp: '2024-05-31T09:00:00Z' },
    { id: 'log_43', matterId: 'matter_105', userId: 'user_1', action: 'created', entityType: 'matter', entityId: 'matter_105', details: 'Created matter Crawford v. UCSF - Missed PE diagnosis', timestamp: '2024-02-29T10:00:00Z' },
    { id: 'log_44', matterId: 'matter_105', userId: 'user_2', action: 'status_changed', entityType: 'matter', entityId: 'matter_105', details: 'Changed status from Open to Pending - settlement talks', timestamp: '2025-01-15T11:00:00Z' },
    { id: 'log_45', matterId: 'matter_105', userId: 'user_2', action: 'status_changed', entityType: 'matter', entityId: 'matter_105', details: 'Changed status from Pending to Closed - $425K settlement', timestamp: '2025-03-20T15:00:00Z' },
    { id: 'log_46', matterId: 'matter_107', userId: 'user_4', action: 'created', entityType: 'matter', entityId: 'matter_107', details: 'Created matter Bay Area Construction - CEQA', timestamp: '2024-07-14T10:00:00Z' },
    { id: 'log_47', matterId: 'matter_119', userId: 'user_12', action: 'created', entityType: 'matter', entityId: 'matter_119', details: 'Created matter Pinnacle v. DataMiner - Trade secrets', timestamp: '2025-01-04T15:30:00Z' },
    { id: 'log_48', matterId: 'matter_5', userId: 'user_8', action: 'created', entityType: 'matter', entityId: 'matter_5', details: 'Created matter Doyle v. Summit Construction', timestamp: '2024-10-27T08:45:00Z' },
    { id: 'log_49', matterId: 'matter_6', userId: 'user_1', action: 'created', entityType: 'matter', entityId: 'matter_6', details: 'Created matter McCarthy v. City of San Francisco', timestamp: '2024-09-29T13:00:00Z' },
    { id: 'log_50', matterId: 'matter_8', userId: 'user_2', action: 'created', entityType: 'matter', entityId: 'matter_8', details: 'Created matter Mills v. Rodriguez - Motorcycle TBI', timestamp: '2024-09-14T10:00:00Z' },
    { id: 'log_51', matterId: 'matter_9', userId: 'user_1', action: 'created', entityType: 'matter', entityId: 'matter_9', details: 'Created matter Ababio v. SafeMart Grocery', timestamp: '2024-04-29T11:45:00Z' },
    { id: 'log_52', matterId: 'matter_9', userId: 'user_2', action: 'status_changed', entityType: 'matter', entityId: 'matter_9', details: 'Changed status from Open to Pending - settlement offer received', timestamp: '2025-09-01T10:00:00Z' },
    { id: 'log_53', matterId: 'matter_10', userId: 'user_2', action: 'created', entityType: 'matter', entityId: 'matter_10', details: 'Created matter Dimitriou v. Lawson - Dog bite', timestamp: '2024-11-24T09:30:00Z' },
    { id: 'log_54', matterId: 'matter_11', userId: 'user_8', action: 'created', entityType: 'matter', entityId: 'matter_11', details: 'Created matter Whitfield v. BART - Escalator injury', timestamp: '2024-12-11T14:00:00Z' },
    { id: 'log_55', matterId: 'matter_12', userId: 'user_1', action: 'created', entityType: 'matter', entityId: 'matter_12', details: 'Created matter Brennan v. Oceanview Hotel', timestamp: '2025-02-04T10:30:00Z' },
    { id: 'log_56', matterId: 'matter_13', userId: 'user_2', action: 'created', entityType: 'matter', entityId: 'matter_13', details: 'Created matter Simmons v. Uber Technologies', timestamp: '2024-11-17T16:00:00Z' },
    { id: 'log_57', matterId: 'matter_14', userId: 'user_1', action: 'created', entityType: 'matter', entityId: 'matter_14', details: 'Created matter Sullivan-Wright v. Kaiser Permanente', timestamp: '2024-09-07T11:15:00Z' },
    { id: 'log_58', matterId: 'matter_15', userId: 'user_2', action: 'created', entityType: 'matter', entityId: 'matter_15', details: 'Created matter Fitzgerald v. St. Mary Medical Center', timestamp: '2024-09-19T14:30:00Z' },
    { id: 'log_59', matterId: 'matter_17', userId: 'user_1', action: 'created', entityType: 'matter', entityId: 'matter_17', details: 'Created matter Gonzalez v. DoorDash', timestamp: '2024-01-14T11:00:00Z' },
    { id: 'log_60', matterId: 'matter_17', userId: 'user_2', action: 'status_changed', entityType: 'matter', entityId: 'matter_17', details: 'Changed status from Pending to Closed - $85K settlement', timestamp: '2024-12-20T16:00:00Z' },
    { id: 'log_61', matterId: 'matter_21', userId: 'user_2', action: 'created', entityType: 'matter', entityId: 'matter_21', details: 'Created matter Okafor v. SF Municipal Railway', timestamp: '2024-01-31T09:00:00Z' },
    { id: 'log_62', matterId: 'matter_21', userId: 'user_2', action: 'status_changed', entityType: 'matter', entityId: 'matter_21', details: 'Changed status to Closed - $45K settlement', timestamp: '2024-11-30T15:00:00Z' },
    { id: 'log_63', matterId: 'matter_29', userId: 'user_3', action: 'created', entityType: 'matter', entityId: 'matter_29', details: 'Created matter Nguyen v. Nguyen - Custody modification', timestamp: '2024-09-04T14:15:00Z' },
    { id: 'log_64', matterId: 'matter_34', userId: 'user_3', action: 'created', entityType: 'matter', entityId: 'matter_34', details: 'Created matter Vasquez v. Vasquez - Child support mod', timestamp: '2024-04-15T10:20:00Z' },
    { id: 'log_65', matterId: 'matter_35', userId: 'user_3', action: 'created', entityType: 'matter', entityId: 'matter_35', details: 'Created matter Baptiste v. Baptiste - Divorce', timestamp: '2025-01-07T14:00:00Z' },
    { id: 'log_66', matterId: 'matter_36', userId: 'user_3', action: 'status_changed', entityType: 'matter', entityId: 'matter_36', details: 'Changed status to Closed - visitation order granted', timestamp: '2025-04-15T14:00:00Z' },
    { id: 'log_67', matterId: 'matter_40', userId: 'user_1', action: 'created', entityType: 'matter', entityId: 'matter_40', details: 'Created matter Stone v. Stone - Divorce', timestamp: '2024-09-30T09:00:00Z' },
    { id: 'log_68', matterId: 'matter_43', userId: 'user_8', action: 'created', entityType: 'matter', entityId: 'matter_43', details: "Created matter People v. Chen-Ramirez - DUI", timestamp: '2024-02-21T16:00:00Z' },
    { id: 'log_69', matterId: 'matter_45', userId: 'user_8', action: 'created', entityType: 'matter', entityId: 'matter_45', details: "Created matter People v. O'Connor - Drug possession", timestamp: '2024-07-29T09:00:00Z' },
    { id: 'log_70', matterId: 'matter_48', userId: 'user_8', action: 'created', entityType: 'matter', entityId: 'matter_48', details: 'Created matter People v. DeLuca - Felony DUI', timestamp: '2024-12-07T08:30:00Z' },
    { id: 'log_71', matterId: 'matter_53', userId: 'user_8', action: 'status_changed', entityType: 'matter', entityId: 'matter_53', details: 'Changed status to Closed - charges dismissed', timestamp: '2024-11-15T14:00:00Z' },
    { id: 'log_72', matterId: 'matter_56', userId: 'user_4', action: 'created', entityType: 'matter', entityId: 'matter_56', details: 'Created matter Golden Gate Properties - Commercial lease', timestamp: '2024-02-15T14:00:00Z' },
    { id: 'log_73', matterId: 'matter_57', userId: 'user_13', action: 'status_changed', entityType: 'matter', entityId: 'matter_57', details: 'Changed status to Closed - sale completed', timestamp: '2024-11-15T16:00:00Z' },
    { id: 'log_74', matterId: 'matter_60', userId: 'user_4', action: 'created', entityType: 'matter', entityId: 'matter_60', details: 'Created matter Alliance Property - Eviction dispute', timestamp: '2024-05-17T13:30:00Z' },
    { id: 'log_75', matterId: 'matter_64', userId: 'user_4', action: 'created', entityType: 'matter', entityId: 'matter_64', details: 'Created matter Pacific Rim Imports - Trade compliance', timestamp: '2024-01-27T11:30:00Z' },
    { id: 'log_76', matterId: 'matter_69', userId: 'user_1', action: 'created', entityType: 'matter', entityId: 'matter_69', details: 'Created matter Mission District Restaurant - Franchise', timestamp: '2024-06-27T09:00:00Z' },
    { id: 'log_77', matterId: 'matter_70', userId: 'user_4', action: 'created', entityType: 'matter', entityId: 'matter_70', details: 'Created matter Redwood Financial - SEC compliance', timestamp: '2024-02-29T15:00:00Z' },
    { id: 'log_78', matterId: 'matter_71', userId: 'user_4', action: 'created', entityType: 'matter', entityId: 'matter_71', details: 'Created matter Pinnacle Software - SaaS licensing', timestamp: '2024-02-19T11:15:00Z' },
    { id: 'log_79', matterId: 'matter_72', userId: 'user_12', action: 'created', entityType: 'matter', entityId: 'matter_72', details: 'Created matter Al-Rashid - Partnership dissolution', timestamp: '2024-02-09T10:00:00Z' },
    { id: 'log_80', matterId: 'matter_75', userId: 'user_1', action: 'created', entityType: 'matter', entityId: 'matter_75', details: 'Created matter Chang v. Pacific Healthcare - Whistleblower', timestamp: '2024-10-17T09:15:00Z' },
    { id: 'log_81', matterId: 'matter_76', userId: 'user_16', action: 'created', entityType: 'matter', entityId: 'matter_76', details: 'Created matter Petrovic v. Lakeside - Sexual harassment', timestamp: '2024-07-01T11:00:00Z' },
    { id: 'log_82', matterId: 'matter_77', userId: 'user_16', action: 'status_changed', entityType: 'matter', entityId: 'matter_77', details: 'Changed status to Closed - non-compete invalidated', timestamp: '2025-01-10T10:00:00Z' },
    { id: 'log_83', matterId: 'matter_82', userId: 'user_13', action: 'created', entityType: 'matter', entityId: 'matter_82', details: 'Created matter Yamamoto Living Trust', timestamp: '2024-08-17T11:30:00Z' },
    { id: 'log_84', matterId: 'matter_83', userId: 'user_1', action: 'created', entityType: 'matter', entityId: 'matter_83', details: 'Created matter Crawford Estate Administration', timestamp: '2024-10-04T14:00:00Z' },
    { id: 'log_85', matterId: 'matter_89', userId: 'user_1', action: 'created', entityType: 'matter', entityId: 'matter_89', details: 'Created matter Tanaka Green Card - EB-2 NIW', timestamp: '2025-01-21T09:45:00Z' },
    { id: 'log_86', matterId: 'matter_92', userId: 'user_4', action: 'created', entityType: 'matter', entityId: 'matter_92', details: 'Created matter Vertex Technologies - Patent application', timestamp: '2024-05-09T09:30:00Z' },
    { id: 'log_87', matterId: 'matter_97', userId: 'user_12', action: 'status_changed', entityType: 'matter', entityId: 'matter_97', details: 'Changed status to Closed - Chapter 7 discharge granted', timestamp: '2025-06-30T14:00:00Z' },
    { id: 'log_88', matterId: 'matter_99', userId: 'user_4', action: 'created', entityType: 'matter', entityId: 'matter_99', details: 'Created matter Mission Restaurant - Chapter 11 Sub V', timestamp: '2025-02-14T09:00:00Z' },
    { id: 'log_89', matterId: 'matter_102', userId: 'user_4', action: 'created', entityType: 'matter', entityId: 'matter_102', details: 'Created matter Kim State Tax Appeal', timestamp: '2024-10-19T10:30:00Z' },
    { id: 'log_90', matterId: 'matter_103', userId: 'user_12', action: 'status_changed', entityType: 'matter', entityId: 'matter_103', details: 'Changed status to Closed - compliance achieved', timestamp: '2024-10-30T15:00:00Z' },
    { id: 'log_91', matterId: 'matter_104', userId: 'user_2', action: 'created', entityType: 'matter', entityId: 'matter_104', details: 'Created matter Gonzalez v. Bay Area Surgical - MedMal', timestamp: '2025-01-04T14:30:00Z' },
    { id: 'log_92', matterId: 'matter_106', userId: 'user_2', action: 'created', entityType: 'matter', entityId: 'matter_106', details: 'Created matter Whitfield v. Pacific Heights Dental', timestamp: '2025-02-19T11:00:00Z' },
    { id: 'log_93', matterId: 'matter_108', userId: 'user_13', action: 'created', entityType: 'matter', entityId: 'matter_108', details: 'Created matter Golden Gate - Soil contamination', timestamp: '2024-03-19T14:30:00Z' },
    { id: 'log_94', matterId: 'matter_108', userId: 'user_12', action: 'status_changed', entityType: 'matter', entityId: 'matter_108', details: 'Changed status to Pending - awaiting DTSC review', timestamp: '2025-06-01T09:00:00Z' },
    { id: 'log_95', matterId: 'matter_109', userId: 'user_12', action: 'status_changed', entityType: 'matter', entityId: 'matter_109', details: 'Changed status to Closed - permit renewed', timestamp: '2024-12-20T14:00:00Z' },
    { id: 'log_96', matterId: 'matter_110', userId: 'user_4', action: 'created', entityType: 'matter', entityId: 'matter_110', details: 'Created matter Vertex Technologies - Executive agreement', timestamp: '2025-02-27T09:30:00Z' },
    { id: 'log_97', matterId: 'matter_111', userId: 'user_4', action: 'created', entityType: 'matter', entityId: 'matter_111', details: 'Created matter TechVenture - Acquisition due diligence', timestamp: '2025-02-17T11:00:00Z' },
    { id: 'log_98', matterId: 'matter_112', userId: 'user_10', action: 'created', entityType: 'matter', entityId: 'matter_112', details: 'Created matter Tanaka Spousal Visa', timestamp: '2025-02-28T10:00:00Z' },
    { id: 'log_99', matterId: 'matter_115', userId: 'user_4', action: 'created', entityType: 'matter', entityId: 'matter_115', details: 'Created matter NovaBio - Board governance restructuring', timestamp: '2025-01-09T09:00:00Z' },
    { id: 'log_100', matterId: 'matter_116', userId: 'user_3', action: 'created', entityType: 'matter', entityId: 'matter_116', details: 'Created matter Vasquez VAWA Petition', timestamp: '2025-01-29T13:30:00Z' },
    { id: 'log_101', matterId: 'matter_117', userId: 'user_3', action: 'created', entityType: 'matter', entityId: 'matter_117', details: 'Created matter Blackwell Irrevocable Trust', timestamp: '2025-01-31T11:00:00Z' },
    { id: 'log_102', matterId: 'matter_118', userId: 'user_12', action: 'created', entityType: 'matter', entityId: 'matter_118', details: 'Created matter Al-Rashid - Breach of fiduciary duty', timestamp: '2025-02-11T10:00:00Z' },
    { id: 'log_103', matterId: 'matter_120', userId: 'user_3', action: 'created', entityType: 'matter', entityId: 'matter_120', details: 'Created matter People v. Baptiste - Insurance fraud', timestamp: '2025-02-27T14:00:00Z' },
    { id: 'log_104', matterId: null, userId: 'user_1', action: 'deleted', entityType: 'matter', entityId: 'matter_deleted_1', details: 'Deleted duplicate matter TechStartup Inc. - Contract review', timestamp: '2025-12-15T10:30:00Z' },
    { id: 'log_105', matterId: null, userId: 'user_1', action: 'deleted', entityType: 'matter', entityId: 'matter_deleted_2', details: 'Deleted test matter created in error', timestamp: '2025-11-20T14:15:00Z' },
    { id: 'log_106', matterId: null, userId: 'user_3', action: 'deleted', entityType: 'matter', entityId: 'matter_deleted_3', details: 'Deleted matter Smith consultation - client did not retain', timestamp: '2025-10-05T09:30:00Z' },
    { id: 'log_107', matterId: 'matter_1', userId: 'user_2', action: 'edited', entityType: 'matter', entityId: 'matter_1', details: 'Updated custom field: Court Case Number to SF-2024-CV-08821', timestamp: '2024-04-20T10:00:00Z' },
    { id: 'log_108', matterId: 'matter_1', userId: 'user_7', action: 'edited', entityType: 'matter', entityId: 'matter_1', details: 'Updated budget to $50,000', timestamp: '2024-05-01T09:00:00Z' },
    { id: 'log_109', matterId: 'matter_30', userId: 'user_3', action: 'edited', entityType: 'matter', entityId: 'matter_30', details: 'Updated billing rate override for Diana Reyes to $500/hr', timestamp: '2024-07-01T11:00:00Z' },
    { id: 'log_110', matterId: 'matter_94', userId: 'user_4', action: 'edited', entityType: 'matter', entityId: 'matter_94', details: 'Updated budget to $300,000 based on expanded discovery needs', timestamp: '2024-07-15T14:00:00Z' },
    { id: 'log_111', matterId: 'matter_1', userId: 'user_1', action: 'edited', entityType: 'matter', entityId: 'matter_1', details: 'Added notification preferences for matter updates and budget threshold', timestamp: '2024-03-20T15:00:00Z' },
    { id: 'log_112', matterId: 'matter_47', userId: 'user_4', action: 'edited', entityType: 'matter', entityId: 'matter_47', details: 'Added Thomas O\'Brien as of-counsel with $600/hr rate', timestamp: '2024-12-22T16:00:00Z' },
    { id: 'log_113', matterId: 'matter_96', userId: 'user_4', action: 'stage_changed', entityType: 'matter', entityId: 'matter_96', details: 'Changed stage from Creditor Meeting to Plan Confirmation', timestamp: '2024-08-01T10:00:00Z' },
    { id: 'log_114', matterId: 'matter_88', userId: 'user_10', action: 'stage_changed', entityType: 'matter', entityId: 'matter_88', details: 'Changed stage from Filing to Adjudication', timestamp: '2024-10-30T09:00:00Z' },
    { id: 'log_115', matterId: 'matter_73', userId: 'user_16', action: 'stage_changed', entityType: 'matter', entityId: 'matter_73', details: 'Changed stage from EEOC/Admin Filing to Negotiation', timestamp: '2024-12-15T11:00:00Z' },
    { id: 'log_116', matterId: 'matter_14', userId: 'user_8', action: 'stage_changed', entityType: 'matter', entityId: 'matter_14', details: 'Changed stage from Expert Consultation to Filing', timestamp: '2024-12-05T14:00:00Z' },
    { id: 'log_117', matterId: 'matter_56', userId: 'user_13', action: 'edited', entityType: 'matter', entityId: 'matter_56', details: 'Updated location to include specific suite number', timestamp: '2024-03-01T10:00:00Z' },
    { id: 'log_118', matterId: 'matter_119', userId: 'user_4', action: 'permission_changed', entityType: 'matter', entityId: 'matter_119', details: 'Restricted access to Corporate & Business group', timestamp: '2025-01-05T09:00:00Z' },
    { id: 'log_119', matterId: 'matter_33', userId: 'user_3', action: 'edited', entityType: 'matter', entityId: 'matter_33', details: 'Added blocked users for safety: Kevin Nakamura, James Cooper', timestamp: '2024-08-06T10:00:00Z' },
    { id: 'log_120', matterId: 'matter_76', userId: 'user_16', action: 'status_changed', entityType: 'matter', entityId: 'matter_76', details: 'Changed status from Open to Pending - settlement negotiations', timestamp: '2025-11-15T10:00:00Z' },
    { id: 'log_121', matterId: 'matter_25', userId: 'user_2', action: 'status_changed', entityType: 'matter', entityId: 'matter_25', details: 'Changed status from Open to Pending - settlement offer', timestamp: '2025-07-15T09:00:00Z' },
    { id: 'log_122', matterId: 'matter_41', userId: 'user_3', action: 'status_changed', entityType: 'matter', entityId: 'matter_41', details: 'Changed status from Open to Pending - annulment hearing scheduled', timestamp: '2025-06-15T11:00:00Z' },
    { id: 'log_123', matterId: 'matter_50', userId: 'user_8', action: 'status_changed', entityType: 'matter', entityId: 'matter_50', details: 'Changed status from Open to Pending - plea negotiations', timestamp: '2025-12-01T10:00:00Z' },
    { id: 'log_124', matterId: 'matter_54', userId: 'user_5', action: 'status_changed', entityType: 'matter', entityId: 'matter_54', details: 'Changed status from Open to Pending - plea offer received', timestamp: '2025-10-01T09:00:00Z' },
    { id: 'log_125', matterId: 'matter_61', userId: 'user_13', action: 'status_changed', entityType: 'matter', entityId: 'matter_61', details: 'Changed status from Open to Pending - survey ordered', timestamp: '2025-09-01T10:00:00Z' },
    { id: 'log_126', matterId: 'matter_68', userId: 'user_12', action: 'status_changed', entityType: 'matter', entityId: 'matter_68', details: 'Changed status from Open to Pending - CSLB hearing', timestamp: '2025-08-01T09:00:00Z' },
    { id: 'log_127', matterId: 'matter_90', userId: 'user_10', action: 'status_changed', entityType: 'matter', entityId: 'matter_90', details: 'Changed status from Open to Pending - petition adjudicating', timestamp: '2025-04-01T10:00:00Z' },
    { id: 'log_128', matterId: 'matter_95', userId: 'user_12', action: 'status_changed', entityType: 'matter', entityId: 'matter_95', details: 'Changed status from Open to Pending - settlement conference', timestamp: '2025-11-01T10:00:00Z' },
    { id: 'log_129', matterId: 'matter_102', userId: 'user_14', action: 'status_changed', entityType: 'matter', entityId: 'matter_102', details: 'Changed status from Open to Pending - OTA hearing', timestamp: '2025-08-01T14:00:00Z' },
    { id: 'log_130', matterId: 'matter_108', userId: 'user_12', action: 'status_changed', entityType: 'matter', entityId: 'matter_108', details: 'Changed status from Open to Pending - DTSC review', timestamp: '2025-06-01T09:00:00Z' },
    { id: 'log_131', matterId: 'matter_15', userId: 'user_8', action: 'status_changed', entityType: 'matter', entityId: 'matter_15', details: 'Changed status from Open to Pending - mediation scheduled', timestamp: '2025-11-01T11:00:00Z' },
    { id: 'log_132', matterId: 'matter_19', userId: 'user_5', action: 'status_changed', entityType: 'matter', entityId: 'matter_19', details: 'Changed status from Open to Pending - settlement talks', timestamp: '2025-08-20T14:00:00Z' },
    { id: 'log_133', matterId: 'matter_32', userId: 'user_3', action: 'status_changed', entityType: 'matter', entityId: 'matter_32', details: 'Changed status from Open to Pending - adoption hearing', timestamp: '2025-10-01T09:00:00Z' },
    { id: 'log_134', matterId: 'matter_38', userId: 'user_3', action: 'status_changed', entityType: 'matter', entityId: 'matter_38', details: 'Changed status to Closed - paternity established', timestamp: '2024-08-30T15:00:00Z' },
    { id: 'log_135', matterId: 'matter_36', userId: 'user_6', action: 'status_changed', entityType: 'matter', entityId: 'matter_36', details: 'Changed status from Open to Pending', timestamp: '2025-02-01T10:00:00Z' },
    { id: 'log_136', matterId: null, userId: 'user_1', action: 'deleted', entityType: 'matter', entityId: 'matter_deleted_4', details: 'Deleted accidental duplicate of Brennan matter', timestamp: '2025-09-01T08:30:00Z' },
    { id: 'log_137', matterId: null, userId: 'user_12', action: 'deleted', entityType: 'matter', entityId: 'matter_deleted_5', details: 'Deleted old template matter no longer needed', timestamp: '2025-08-10T16:00:00Z' },
    { id: 'log_138', matterId: 'matter_1', userId: 'user_7', action: 'edited', entityType: 'document', entityId: 'folder_1_1', details: 'Uploaded Initial_Assessment_Patterson_2024.pdf to Medical Records', timestamp: '2024-05-10T10:00:00Z' },
    { id: 'log_139', matterId: 'matter_1', userId: 'user_7', action: 'edited', entityType: 'document', entityId: 'folder_1_2', details: 'Uploaded police report to Police Reports folder', timestamp: '2024-04-01T09:30:00Z' },
    { id: 'log_140', matterId: 'matter_94', userId: 'user_14', action: 'edited', entityType: 'document', entityId: 'folder_94_1', details: 'Uploaded patent claims analysis to Patent Documents', timestamp: '2024-04-05T14:00:00Z' },
    { id: 'log_141', matterId: 'matter_47', userId: 'user_15', action: 'edited', entityType: 'document', entityId: 'folder_47_1', details: 'Uploaded financial transaction records', timestamp: '2025-01-12T10:30:00Z' },
    { id: 'log_142', matterId: 'matter_7', userId: 'user_2', action: 'edited', entityType: 'matter', entityId: 'matter_7', details: 'Updated contingency fee to 40% due to complex product liability', timestamp: '2024-08-01T14:00:00Z' },
    { id: 'log_143', matterId: 'matter_96', userId: 'user_14', action: 'edited', entityType: 'document', entityId: 'folder_96_2', details: 'Uploaded updated creditor list with international creditors', timestamp: '2024-06-01T11:00:00Z' },
    { id: 'log_144', matterId: 'matter_28', userId: 'user_11', action: 'edited', entityType: 'document', entityId: 'folder_28_1', details: 'Uploaded final property division spreadsheet', timestamp: '2024-05-01T15:00:00Z' },
    { id: 'log_145', matterId: 'matter_88', userId: 'user_15', action: 'edited', entityType: 'document', entityId: 'folder_88_2', details: 'Uploaded country conditions reports from State Department', timestamp: '2024-09-15T09:00:00Z' },
    { id: 'log_146', matterId: 'matter_65', userId: 'user_14', action: 'edited', entityType: 'document', entityId: 'folder_65_1', details: 'Uploaded FDA Type B meeting minutes', timestamp: '2024-06-15T16:00:00Z' },
    { id: 'log_147', matterId: 'matter_74', userId: 'user_16', action: 'edited', entityType: 'matter', entityId: 'matter_74', details: 'Updated case value estimate to reflect expanded class size', timestamp: '2024-11-01T10:00:00Z' },
    { id: 'log_148', matterId: 'matter_30', userId: 'user_3', action: 'edited', entityType: 'matter', entityId: 'matter_30', details: 'Added estimated case value of $4.5M', timestamp: '2024-09-20T14:00:00Z' },
    { id: 'log_149', matterId: 'matter_119', userId: 'user_12', action: 'edited', entityType: 'matter', entityId: 'matter_119', details: 'Updated budget to $250K after initial forensic analysis', timestamp: '2025-02-01T10:00:00Z' },
    { id: 'log_150', matterId: 'matter_120', userId: 'user_8', action: 'edited', entityType: 'matter', entityId: 'matter_120', details: 'Assigned to Criminal Defense Unit group', timestamp: '2025-03-01T09:00:00Z' },
    { id: 'log_151', matterId: 'matter_99', userId: 'user_4', action: 'edited', entityType: 'matter', entityId: 'matter_99', details: 'Set billing rate override for Thomas O\'Brien at $575/hr', timestamp: '2025-02-15T10:00:00Z' },
    { id: 'log_152', matterId: 'matter_116', userId: 'user_10', action: 'permission_changed', entityType: 'matter', entityId: 'matter_116', details: 'Restricted access for VAWA case safety', timestamp: '2025-01-30T09:00:00Z' },
    { id: 'log_153', matterId: 'matter_117', userId: 'user_3', action: 'edited', entityType: 'matter', entityId: 'matter_117', details: 'Blocked user David Kim from trust matter', timestamp: '2025-02-01T10:00:00Z' },
    { id: 'log_154', matterId: 'matter_62', userId: 'user_13', action: 'edited', entityType: 'matter', entityId: 'matter_62', details: 'Added Bay Area Construction LLC as related contact (Opposing Party)', timestamp: '2025-01-28T11:00:00Z' },
    { id: 'log_155', matterId: 'matter_86', userId: 'user_13', action: 'created', entityType: 'matter', entityId: 'matter_86', details: 'Created matter Yamamoto Business Succession', timestamp: '2025-02-09T10:30:00Z' }
];

const DELETED_MATTERS = [
    {
        id: 'del_matter_1', originalMatterId: 'matter_deleted_1', number: '00098', displayNumber: '00098-TechStartup',
        description: 'TechStartup Inc. - Contract review (duplicate)', clientName: 'TechStartup Inc.',
        deletedBy: 'user_1', deletedAt: '2025-12-15T10:30:00Z', type: 'matter'
    },
    {
        id: 'del_matter_2', originalMatterId: 'matter_deleted_2', number: '00099', displayNumber: '00099-TestMatter',
        description: 'Test Matter - Created in error during system testing', clientName: 'Test Client',
        deletedBy: 'user_1', deletedAt: '2025-11-20T14:15:00Z', type: 'matter'
    },
    {
        id: 'del_matter_3', originalMatterId: 'matter_deleted_3', number: '00078', displayNumber: '00078-Smith',
        description: 'Smith Consultation - Initial consultation, client did not retain firm', clientName: 'Robert Smith',
        deletedBy: 'user_3', deletedAt: '2025-10-05T09:30:00Z', type: 'matter'
    },
    {
        id: 'del_matter_4', originalMatterId: 'matter_deleted_4', number: '00102', displayNumber: '00102-Brennan-Dup',
        description: 'Brennan v. Oceanview Hotel (duplicate entry)', clientName: 'Paul Brennan',
        deletedBy: 'user_1', deletedAt: '2025-09-01T08:30:00Z', type: 'matter'
    },
    {
        id: 'del_matter_5', originalMatterId: 'matter_deleted_5', number: '00045', displayNumber: '00045-OldTemplate',
        description: 'Template Matter - Old template format, no longer in use', clientName: 'N/A',
        deletedBy: 'user_12', deletedAt: '2025-08-10T16:00:00Z', type: 'matter'
    },
    {
        id: 'del_matter_6', originalMatterId: 'matter_deleted_6', number: '00067', displayNumber: '00067-JonesInquiry',
        description: 'Jones Initial Inquiry - Conflict check revealed existing adverse representation', clientName: 'Patricia Jones',
        deletedBy: 'user_1', deletedAt: '2025-07-22T11:45:00Z', type: 'matter'
    }
];

const EXPENSE_CATEGORIES = [
    'Filing Fees', 'Court Costs', 'Expert Witness Fees', 'Deposition Costs',
    'Travel', 'Copying/Printing', 'Postage', 'Service of Process',
    'Medical Records', 'Investigation', 'Research', 'Transcripts',
    'Mediation Fees', 'Arbitration Fees', 'Other'
];

const CURRENCIES = [
    { code: 'USD', name: 'US Dollar' },
    { code: 'CAD', name: 'Canadian Dollar' },
    { code: 'GBP', name: 'British Pound' },
    { code: 'EUR', name: 'Euro' },
    { code: 'AUD', name: 'Australian Dollar' }
];

const RELATIONSHIP_TYPES = [
    'Spouse', 'Parent', 'Child', 'Sibling', 'Guardian',
    'Employer', 'Co-defendant', 'Witness', 'Expert Witness',
    'Insurance Adjuster', 'Opposing Party', 'Opposing Counsel',
    'Medical Provider', 'Caretaker', 'Other'
];

const NOTIFICATION_SETTINGS = {
    matter_updates: true,
    matter_deletions: true,
    budget_updates: true,
    budget_threshold: true,
    trust_balance: true
};

const FIRM_SETTINGS = {
    name: 'Meridian Law Group',
    defaultTemplateId: 'template_1',
    updateMatterNameOnSave: true,
    recoveryBinRetentionDays: 180,
    primaryPracticeAreaId: 'pa_1'
};
