/* data.js — Seed data for Gmail Accounts & Contacts */

const SEED_DATA_VERSION = 1;

// ─── Current User (the logged-in Google account) ───
const CURRENT_USER = {
    id: 'usr_self',
    firstName: 'Sarah',
    lastName: 'Chen',
    email: 'sarah.chen@techcorp.io',
    recoveryEmail: 'sarahchen.personal@gmail.com',
    recoveryPhone: '+1 (415) 555-0192',
    profilePhoto: null,
    twoStepVerification: true,
    lastPasswordChange: '2026-01-15T10:30:00Z',
    createdAt: '2021-03-08T14:00:00Z'
};

// ─── Send Mail As (Aliases) ───
const ALIASES = [
    {
        id: 'alias_1',
        name: 'Sarah Chen',
        email: 'sarah.chen@techcorp.io',
        isPrimary: true,
        isDefault: true,
        replyFrom: 'default',
        smtpServer: '',
        smtpPort: '',
        smtpUsername: '',
        useSSL: true,
        createdAt: '2021-03-08T14:00:00Z'
    },
    {
        id: 'alias_2',
        name: 'Sarah Chen (Support)',
        email: 'support@techcorp.io',
        isPrimary: false,
        isDefault: false,
        replyFrom: 'alias',
        smtpServer: 'smtp.techcorp.io',
        smtpPort: '587',
        smtpUsername: 'support@techcorp.io',
        useSSL: true,
        createdAt: '2023-06-12T09:15:00Z'
    },
    {
        id: 'alias_3',
        name: 'S. Chen',
        email: 'schen@alumni.stanford.edu',
        isPrimary: false,
        isDefault: false,
        replyFrom: 'default',
        smtpServer: 'smtp.stanford.edu',
        smtpPort: '465',
        smtpUsername: 'schen@alumni.stanford.edu',
        useSSL: true,
        createdAt: '2022-09-01T11:00:00Z'
    },
    {
        id: 'alias_4',
        name: 'Sarah Chen',
        email: 'sarah@chen-family.org',
        isPrimary: false,
        isDefault: false,
        replyFrom: 'alias',
        smtpServer: 'mail.chen-family.org',
        smtpPort: '587',
        smtpUsername: 'sarah@chen-family.org',
        useSSL: true,
        createdAt: '2024-01-20T16:45:00Z'
    }
];

// ─── Delegates ───
const DELEGATES = [
    {
        id: 'del_1',
        email: 'james.wu@techcorp.io',
        name: 'James Wu',
        status: 'active',
        addedAt: '2025-04-10T08:00:00Z'
    },
    {
        id: 'del_2',
        email: 'priya.sharma@techcorp.io',
        name: 'Priya Sharma',
        status: 'active',
        addedAt: '2025-08-22T13:30:00Z'
    },
    {
        id: 'del_3',
        email: 'alex.martinez@techcorp.io',
        name: 'Alex Martinez',
        status: 'pending',
        addedAt: '2026-03-15T09:00:00Z'
    }
];

// ─── Import Accounts (Check mail from other accounts via POP3) ───
const IMPORT_ACCOUNTS = [
    {
        id: 'imp_1',
        email: 'sarahchen.personal@gmail.com',
        server: 'pop.gmail.com',
        port: '995',
        username: 'sarahchen.personal@gmail.com',
        useSSL: true,
        leaveOnServer: true,
        labelIncoming: 'personal-gmail',
        status: 'active',
        lastChecked: '2026-03-18T06:30:00Z',
        addedAt: '2022-05-10T14:00:00Z'
    },
    {
        id: 'imp_2',
        email: 'sarah@old-startup.com',
        server: 'mail.old-startup.com',
        port: '995',
        username: 'sarah',
        useSSL: true,
        leaveOnServer: false,
        labelIncoming: 'old-startup',
        status: 'error',
        lastChecked: '2026-02-28T12:00:00Z',
        errorMessage: 'Connection refused: server unreachable',
        addedAt: '2023-01-15T10:00:00Z'
    }
];

// ─── Contact Groups / Labels ───
const CONTACT_GROUPS = [
    { id: 'grp_1', name: 'Family', system: false, createdAt: '2021-04-01T10:00:00Z', updatedAt: '2026-02-10T08:00:00Z' },
    { id: 'grp_2', name: 'Work', system: false, createdAt: '2021-04-01T10:00:00Z', updatedAt: '2026-03-01T14:00:00Z' },
    { id: 'grp_3', name: 'Friends', system: false, createdAt: '2021-04-15T10:00:00Z', updatedAt: '2025-12-20T16:00:00Z' },
    { id: 'grp_4', name: 'Engineering Team', system: false, createdAt: '2022-01-10T09:00:00Z', updatedAt: '2026-03-10T11:00:00Z' },
    { id: 'grp_5', name: 'Investors', system: false, createdAt: '2023-03-01T08:00:00Z', updatedAt: '2025-11-05T10:00:00Z' },
    { id: 'grp_6', name: 'College Alumni', system: false, createdAt: '2022-09-01T12:00:00Z', updatedAt: '2026-01-15T09:00:00Z' },
    { id: 'grp_7', name: 'Book Club', system: false, createdAt: '2024-06-01T18:00:00Z', updatedAt: '2026-03-05T20:00:00Z' },
    { id: 'grp_8', name: 'Conference Contacts', system: false, createdAt: '2025-09-15T10:00:00Z', updatedAt: '2026-02-20T14:00:00Z' },
    { id: 'grp_9', name: 'Vendors', system: false, createdAt: '2024-02-01T10:00:00Z', updatedAt: '2026-03-12T09:00:00Z' },
    { id: 'grp_10', name: 'VIP', system: false, createdAt: '2025-01-01T08:00:00Z', updatedAt: '2026-03-17T16:00:00Z' }
];

// ─── Contacts (main contacts list — 120+ contacts) ───
const CONTACTS = [
    // Family
    { id: 'ct_1', firstName: 'David', lastName: 'Chen', email: 'david.chen@gmail.com', phone: '+1 (415) 555-0101', company: '', jobTitle: '', address: '142 Oak Street, San Francisco, CA 94102', birthday: '1965-08-22', notes: 'Dad - prefers calls after 6pm', starred: true, groups: ['grp_1'], createdAt: '2021-04-01T10:00:00Z', updatedAt: '2026-01-05T08:00:00Z' },
    { id: 'ct_2', firstName: 'Linda', lastName: 'Chen', email: 'linda.chen@gmail.com', phone: '+1 (415) 555-0102', company: '', jobTitle: '', address: '142 Oak Street, San Francisco, CA 94102', birthday: '1967-11-03', notes: 'Mom', starred: true, groups: ['grp_1'], createdAt: '2021-04-01T10:01:00Z', updatedAt: '2025-12-25T09:00:00Z' },
    { id: 'ct_3', firstName: 'Kevin', lastName: 'Chen', email: 'kevin.chen@outlook.com', phone: '+1 (650) 555-0201', company: 'Stripe', jobTitle: 'Product Manager', address: '88 Colin P Kelly Jr St, San Francisco, CA 94107', birthday: '1995-03-15', notes: 'Brother - birthday coming up', starred: true, groups: ['grp_1'], createdAt: '2021-04-01T10:02:00Z', updatedAt: '2026-03-10T12:00:00Z' },
    { id: 'ct_4', firstName: 'Amy', lastName: 'Chen-Wu', email: 'amy.chenwu@yahoo.com', phone: '+1 (510) 555-0301', company: 'Kaiser Permanente', jobTitle: 'Pediatrician', address: '2500 Merced St, Oakland, CA 94602', birthday: '1993-07-28', notes: 'Sister - new address since June', starred: false, groups: ['grp_1'], createdAt: '2021-04-01T10:03:00Z', updatedAt: '2026-02-14T10:00:00Z' },
    { id: 'ct_5', firstName: 'Robert', lastName: 'Chen', email: 'robert.chen@protonmail.com', phone: '+1 (408) 555-0401', company: '', jobTitle: 'Retired', address: '1200 Elm Avenue, San Jose, CA 95126', birthday: '1940-12-01', notes: 'Uncle Robert - does not use email often', starred: false, groups: ['grp_1'], createdAt: '2021-04-02T10:00:00Z', updatedAt: '2024-06-10T08:00:00Z' },

    // Work - Engineering Team
    { id: 'ct_6', firstName: 'James', lastName: 'Wu', email: 'james.wu@techcorp.io', phone: '+1 (415) 555-1001', company: 'TechCorp', jobTitle: 'Senior Backend Engineer', address: '500 Howard St, San Francisco, CA 94105', birthday: '1990-04-12', notes: 'Tech lead for payments team', starred: true, groups: ['grp_2', 'grp_4'], createdAt: '2021-06-15T09:00:00Z', updatedAt: '2026-03-15T10:00:00Z' },
    { id: 'ct_7', firstName: 'Priya', lastName: 'Sharma', email: 'priya.sharma@techcorp.io', phone: '+1 (415) 555-1002', company: 'TechCorp', jobTitle: 'Engineering Manager', address: '500 Howard St, San Francisco, CA 94105', birthday: '1988-09-05', notes: 'Direct manager', starred: true, groups: ['grp_2', 'grp_4'], createdAt: '2021-06-15T09:01:00Z', updatedAt: '2026-03-14T11:00:00Z' },
    { id: 'ct_8', firstName: 'Alex', lastName: 'Martinez', email: 'alex.martinez@techcorp.io', phone: '+1 (415) 555-1003', company: 'TechCorp', jobTitle: 'Frontend Engineer', address: '500 Howard St, San Francisco, CA 94105', birthday: '1994-01-20', notes: '', starred: false, groups: ['grp_2', 'grp_4'], createdAt: '2022-01-10T09:00:00Z', updatedAt: '2026-03-12T14:00:00Z' },
    { id: 'ct_9', firstName: 'Mei', lastName: 'Zhang', email: 'mei.zhang@techcorp.io', phone: '+1 (415) 555-1004', company: 'TechCorp', jobTitle: 'DevOps Engineer', address: '500 Howard St, San Francisco, CA 94105', birthday: '1992-06-30', notes: 'On-call rotation partner', starred: false, groups: ['grp_2', 'grp_4'], createdAt: '2022-03-20T09:00:00Z', updatedAt: '2026-02-28T16:00:00Z' },
    { id: 'ct_10', firstName: 'Tom', lastName: 'O\'Brien', email: 'tom.obrien@techcorp.io', phone: '+1 (415) 555-1005', company: 'TechCorp', jobTitle: 'QA Lead', address: '500 Howard St, San Francisco, CA 94105', birthday: '1985-11-11', notes: 'Handles release testing', starred: false, groups: ['grp_2', 'grp_4'], createdAt: '2021-09-01T09:00:00Z', updatedAt: '2026-01-20T10:00:00Z' },
    { id: 'ct_11', firstName: 'Nina', lastName: 'Patel', email: 'nina.patel@techcorp.io', phone: '+1 (415) 555-1006', company: 'TechCorp', jobTitle: 'Data Scientist', address: '500 Howard St, San Francisco, CA 94105', birthday: '1991-02-14', notes: 'ML team - collaborating on recommendation engine', starred: false, groups: ['grp_2', 'grp_4'], createdAt: '2023-02-01T09:00:00Z', updatedAt: '2026-03-08T09:00:00Z' },
    { id: 'ct_12', firstName: 'Marcus', lastName: 'Johnson', email: 'marcus.johnson@techcorp.io', phone: '+1 (415) 555-1007', company: 'TechCorp', jobTitle: 'VP of Engineering', address: '500 Howard St, San Francisco, CA 94105', birthday: '1980-07-04', notes: 'Skip-level manager', starred: true, groups: ['grp_2', 'grp_4', 'grp_10'], createdAt: '2021-06-15T09:02:00Z', updatedAt: '2026-03-16T08:00:00Z' },
    { id: 'ct_13', firstName: 'Lisa', lastName: 'Kim', email: 'lisa.kim@techcorp.io', phone: '+1 (415) 555-1008', company: 'TechCorp', jobTitle: 'Product Designer', address: '500 Howard St, San Francisco, CA 94105', birthday: '1993-10-18', notes: 'Design system owner', starred: false, groups: ['grp_2'], createdAt: '2022-06-01T09:00:00Z', updatedAt: '2026-02-15T13:00:00Z' },
    { id: 'ct_14', firstName: 'Ryan', lastName: 'Nguyen', email: 'ryan.nguyen@techcorp.io', phone: '+1 (415) 555-1009', company: 'TechCorp', jobTitle: 'Security Engineer', address: '500 Howard St, San Francisco, CA 94105', birthday: '1989-05-22', notes: 'Security review contact', starred: false, groups: ['grp_2', 'grp_4'], createdAt: '2023-04-15T09:00:00Z', updatedAt: '2026-03-11T15:00:00Z' },
    { id: 'ct_15', firstName: 'Hannah', lastName: 'Cohen', email: 'hannah.cohen@techcorp.io', phone: '+1 (415) 555-1010', company: 'TechCorp', jobTitle: 'Technical Writer', address: '500 Howard St, San Francisco, CA 94105', birthday: '1996-08-09', notes: 'API docs collaboration', starred: false, groups: ['grp_2'], createdAt: '2024-01-08T09:00:00Z', updatedAt: '2026-01-30T11:00:00Z' },

    // Work - Other departments
    { id: 'ct_16', firstName: 'Diana', lastName: 'Ross-Taylor', email: 'diana.ross-taylor@techcorp.io', phone: '+1 (415) 555-1011', company: 'TechCorp', jobTitle: 'CFO', address: '500 Howard St, San Francisco, CA 94105', birthday: '1978-03-26', notes: 'Budget approvals', starred: false, groups: ['grp_2', 'grp_10'], createdAt: '2021-06-15T09:03:00Z', updatedAt: '2025-12-01T10:00:00Z' },
    { id: 'ct_17', firstName: 'Carlos', lastName: 'Mendoza', email: 'carlos.mendoza@techcorp.io', phone: '+1 (415) 555-1012', company: 'TechCorp', jobTitle: 'Head of Sales', address: '500 Howard St, San Francisco, CA 94105', birthday: '1982-12-10', notes: 'Enterprise deals contact', starred: false, groups: ['grp_2'], createdAt: '2022-08-01T09:00:00Z', updatedAt: '2026-02-20T14:00:00Z' },
    { id: 'ct_18', firstName: 'Sophia', lastName: 'Andersson', email: 'sophia.andersson@techcorp.io', phone: '+46 70 123 4567', company: 'TechCorp', jobTitle: 'Head of EU Operations', address: 'Kungsgatan 44, Stockholm, Sweden', birthday: '1986-04-15', notes: 'Stockholm office - 9 hours ahead', starred: false, groups: ['grp_2'], createdAt: '2023-06-01T09:00:00Z', updatedAt: '2026-03-05T08:00:00Z' },

    // Friends
    { id: 'ct_19', firstName: 'Jake', lastName: 'Morrison', email: 'jake.morrison@gmail.com', phone: '+1 (503) 555-2001', company: 'Nike', jobTitle: 'Brand Strategist', address: '1 Bowerman Dr, Beaverton, OR 97005', birthday: '1993-06-14', notes: 'College roommate', starred: true, groups: ['grp_3', 'grp_6'], createdAt: '2021-04-15T10:00:00Z', updatedAt: '2026-01-08T20:00:00Z' },
    { id: 'ct_20', firstName: 'Emma', lastName: 'Thompson', email: 'emma.t@protonmail.com', phone: '+1 (212) 555-2002', company: 'The New York Times', jobTitle: 'Investigative Reporter', address: '620 8th Ave, New York, NY 10018', birthday: '1992-11-30', notes: 'Met at journalism workshop 2019', starred: false, groups: ['grp_3'], createdAt: '2021-05-20T15:00:00Z', updatedAt: '2025-11-30T09:00:00Z' },
    { id: 'ct_21', firstName: 'Liam', lastName: 'O\'Sullivan', email: 'liam.osullivan@hotmail.com', phone: '+353 87 123 4567', company: 'Accenture', jobTitle: 'Management Consultant', address: '1 Grand Canal Square, Dublin 2, Ireland', birthday: '1991-09-08', notes: 'Study abroad friend - Dublin', starred: false, groups: ['grp_3'], createdAt: '2021-06-01T10:00:00Z', updatedAt: '2025-09-08T12:00:00Z' },
    { id: 'ct_22', firstName: 'Aisha', lastName: 'Rahman', email: 'aisha.rahman@gmail.com', phone: '+1 (310) 555-2003', company: 'SpaceX', jobTitle: 'Propulsion Engineer', address: '1 Rocket Rd, Hawthorne, CA 90250', birthday: '1993-01-25', notes: 'High school friend', starred: false, groups: ['grp_3'], createdAt: '2021-04-15T10:01:00Z', updatedAt: '2026-02-25T18:00:00Z' },
    { id: 'ct_23', firstName: 'Ben', lastName: 'Watkins', email: 'ben.watkins@gmail.com', phone: '+1 (415) 555-2004', company: '', jobTitle: 'Freelance Photographer', address: '2040 Mission St, San Francisco, CA 94110', birthday: '1990-10-31', notes: 'Book club & hiking buddy', starred: true, groups: ['grp_3', 'grp_7'], createdAt: '2022-03-10T14:00:00Z', updatedAt: '2026-03-05T20:00:00Z' },

    // College Alumni
    { id: 'ct_24', firstName: 'Rachel', lastName: 'Park', email: 'rachel.park@stanford.edu', phone: '+1 (650) 555-3001', company: 'Stanford University', jobTitle: 'Associate Professor, CS', address: 'Gates Building, Stanford, CA 94305', birthday: '1990-05-17', notes: 'CS 229 study group', starred: false, groups: ['grp_6'], createdAt: '2022-09-01T12:00:00Z', updatedAt: '2025-10-15T10:00:00Z' },
    { id: 'ct_25', firstName: 'Derek', lastName: 'Hoffman', email: 'derek.hoffman@a16z.com', phone: '+1 (650) 555-3002', company: 'Andreessen Horowitz', jobTitle: 'Partner', address: '2865 Sand Hill Rd, Menlo Park, CA 94025', birthday: '1989-08-03', notes: 'Good VC contact', starred: true, groups: ['grp_6', 'grp_5', 'grp_10'], createdAt: '2022-09-01T12:01:00Z', updatedAt: '2026-03-01T09:00:00Z' },
    { id: 'ct_26', firstName: 'Mia', lastName: 'Santos-Rivera', email: 'mia.santosrivera@google.com', phone: '+1 (650) 555-3003', company: 'Google', jobTitle: 'Staff Engineer', address: '1600 Amphitheatre Pkwy, Mountain View, CA 94043', birthday: '1991-12-22', notes: 'Potential hire referral', starred: false, groups: ['grp_6'], createdAt: '2022-09-01T12:02:00Z', updatedAt: '2026-02-10T14:00:00Z' },
    { id: 'ct_27', firstName: 'Tyler', lastName: 'Brooks', email: 'tyler.brooks@gmail.com', phone: '+1 (206) 555-3004', company: 'Amazon', jobTitle: 'Principal PM', address: '410 Terry Ave N, Seattle, WA 98109', birthday: '1990-02-28', notes: '', starred: false, groups: ['grp_6'], createdAt: '2022-09-01T12:03:00Z', updatedAt: '2025-08-20T16:00:00Z' },

    // Investors
    { id: 'ct_28', firstName: 'Victoria', lastName: 'Blackwell', email: 'vblackwell@sequoiacap.com', phone: '+1 (650) 555-4001', company: 'Sequoia Capital', jobTitle: 'Managing Partner', address: '2800 Sand Hill Rd, Menlo Park, CA 94025', birthday: '', notes: 'Series A lead', starred: true, groups: ['grp_5', 'grp_10'], createdAt: '2023-03-01T08:00:00Z', updatedAt: '2026-03-10T10:00:00Z' },
    { id: 'ct_29', firstName: 'Hiroshi', lastName: 'Tanaka', email: 'h.tanaka@softbank.com', phone: '+81 3 6889 1234', company: 'SoftBank Vision Fund', jobTitle: 'Investment Director', address: '1-9-1 Higashi-Shimbashi, Minato-ku, Tokyo', birthday: '1975-04-05', notes: 'Met at TechCrunch Disrupt 2023', starred: false, groups: ['grp_5'], createdAt: '2023-09-20T10:00:00Z', updatedAt: '2025-06-15T08:00:00Z' },
    { id: 'ct_30', firstName: 'Catherine', lastName: 'Duval', email: 'catherine.duval@indexventures.com', phone: '+44 20 7154 4567', company: 'Index Ventures', jobTitle: 'General Partner', address: '1 Neal Street, London WC2H 9QL, UK', birthday: '1980-09-12', notes: 'European expansion advisor', starred: false, groups: ['grp_5', 'grp_10'], createdAt: '2024-01-15T09:00:00Z', updatedAt: '2026-02-01T11:00:00Z' },

    // Book Club
    { id: 'ct_31', firstName: 'Olivia', lastName: 'Grant', email: 'olivia.grant@gmail.com', phone: '+1 (415) 555-5001', company: 'UCSF Medical Center', jobTitle: 'Neurologist', address: '505 Parnassus Ave, San Francisco, CA 94143', birthday: '1988-07-19', notes: 'Hosts book club monthly', starred: false, groups: ['grp_7'], createdAt: '2024-06-01T18:00:00Z', updatedAt: '2026-03-02T20:00:00Z' },
    { id: 'ct_32', firstName: 'Daniel', lastName: 'Reeves', email: 'dan.reeves@outlook.com', phone: '+1 (415) 555-5002', company: 'Dolby Laboratories', jobTitle: 'Audio Engineer', address: '1275 Market St, San Francisco, CA 94103', birthday: '1987-03-08', notes: '', starred: false, groups: ['grp_7'], createdAt: '2024-06-01T18:01:00Z', updatedAt: '2025-12-10T19:00:00Z' },
    { id: 'ct_33', firstName: 'Grace', lastName: 'Liu', email: 'grace.liu@gmail.com', phone: '+1 (415) 555-5003', company: 'Public Library SF', jobTitle: 'Head Librarian', address: '100 Larkin St, San Francisco, CA 94102', birthday: '1985-05-05', notes: 'Gets us early copies sometimes', starred: false, groups: ['grp_7'], createdAt: '2024-06-15T18:00:00Z', updatedAt: '2026-01-20T20:00:00Z' },

    // Conference Contacts
    { id: 'ct_34', firstName: 'Satoshi', lastName: 'Yamamoto', email: 'satoshi.yamamoto@sony.co.jp', phone: '+81 3 6748 2111', company: 'Sony Group', jobTitle: 'CTO, AI Division', address: '1-7-1 Konan, Minato-ku, Tokyo 108-0075', birthday: '', notes: 'Met at AWS re:Invent 2025 - interested in partnership', starred: true, groups: ['grp_8', 'grp_10'], createdAt: '2025-09-15T10:00:00Z', updatedAt: '2026-03-01T09:00:00Z' },
    { id: 'ct_35', firstName: 'Fatima', lastName: 'Al-Hassan', email: 'fatima.alhassan@aramco.com', phone: '+966 13 880 1234', company: 'Saudi Aramco', jobTitle: 'Digital Transformation Lead', address: 'Dhahran 31311, Saudi Arabia', birthday: '1984-02-19', notes: 'KubeCon 2025 keynote speaker', starred: false, groups: ['grp_8'], createdAt: '2025-10-01T14:00:00Z', updatedAt: '2026-01-05T10:00:00Z' },
    { id: 'ct_36', firstName: 'Patrick', lastName: 'van der Berg', email: 'p.vanderberg@booking.com', phone: '+31 20 712 3456', company: 'Booking.com', jobTitle: 'Principal Architect', address: 'Herengracht 597, Amsterdam, Netherlands', birthday: '1983-11-25', notes: 'Microservices talk was excellent', starred: false, groups: ['grp_8'], createdAt: '2025-09-16T10:00:00Z', updatedAt: '2025-12-20T09:00:00Z' },
    { id: 'ct_37', firstName: 'Ingrid', lastName: 'Johansson', email: 'ingrid.johansson@spotify.com', phone: '+46 76 234 5678', company: 'Spotify', jobTitle: 'VP of Engineering', address: 'Regeringsgatan 19, Stockholm, Sweden', birthday: '1981-06-21', notes: 'Connected via Sophia Andersson', starred: false, groups: ['grp_8'], createdAt: '2025-09-17T10:00:00Z', updatedAt: '2026-02-10T15:00:00Z' },
    { id: 'ct_38', firstName: 'Wei', lastName: 'Zhao', email: 'wei.zhao@bytedance.com', phone: '+86 10 5765 4321', company: 'ByteDance', jobTitle: 'Director of Infrastructure', address: 'Zhongguancun, Haidian, Beijing', birthday: '1986-08-14', notes: 'Potential cloud migration partner', starred: false, groups: ['grp_8'], createdAt: '2025-10-02T11:00:00Z', updatedAt: '2026-01-18T08:00:00Z' },

    // Vendors
    { id: 'ct_39', firstName: 'Gregory', lastName: 'Foster', email: 'greg.foster@datadog.com', phone: '+1 (646) 555-6001', company: 'Datadog', jobTitle: 'Enterprise Account Executive', address: '620 8th Ave, 45th Floor, New York, NY 10018', birthday: '', notes: 'Annual contract renewal in April', starred: false, groups: ['grp_9'], createdAt: '2024-02-01T10:00:00Z', updatedAt: '2026-03-12T09:00:00Z' },
    { id: 'ct_40', firstName: 'Michelle', lastName: 'Torres', email: 'mtorres@cloudflare.com', phone: '+1 (650) 555-6002', company: 'Cloudflare', jobTitle: 'Solutions Architect', address: '101 Townsend St, San Francisco, CA 94107', birthday: '1990-12-03', notes: 'Helped with DDoS mitigation setup', starred: false, groups: ['grp_9'], createdAt: '2024-03-15T10:00:00Z', updatedAt: '2026-02-28T14:00:00Z' },
    { id: 'ct_41', firstName: 'Andrew', lastName: 'Blackstone', email: 'a.blackstone@snowflake.com', phone: '+1 (650) 555-6003', company: 'Snowflake', jobTitle: 'Sales Engineer', address: '106 E Babcock St, Bozeman, MT 59715', birthday: '', notes: 'Data warehouse migration POC', starred: false, groups: ['grp_9'], createdAt: '2024-08-01T10:00:00Z', updatedAt: '2026-03-05T11:00:00Z' },
    { id: 'ct_42', firstName: 'Jessica', lastName: 'Singh', email: 'jessica.singh@aws.amazon.com', phone: '+1 (206) 555-6004', company: 'Amazon Web Services', jobTitle: 'Technical Account Manager', address: '440 Terry Ave N, Seattle, WA 98109', birthday: '1988-10-28', notes: 'Primary AWS support contact - Enterprise tier', starred: true, groups: ['grp_9', 'grp_10'], createdAt: '2023-07-01T09:00:00Z', updatedAt: '2026-03-17T10:00:00Z' },
    { id: 'ct_43', firstName: 'Samuel', lastName: 'Lee', email: 'samuel.lee@pagerduty.com', phone: '+1 (415) 555-6005', company: 'PagerDuty', jobTitle: 'Customer Success Manager', address: '600 Townsend St, San Francisco, CA 94103', birthday: '', notes: '', starred: false, groups: ['grp_9'], createdAt: '2025-01-15T10:00:00Z', updatedAt: '2026-01-20T14:00:00Z' },

    // Misc contacts (no specific group or multiple groups)
    { id: 'ct_44', firstName: 'Natalie', lastName: 'Dubois', email: 'natalie.dubois@gmail.com', phone: '+33 6 12 34 56 78', company: 'Freelance', jobTitle: 'UX Consultant', address: '15 Rue de Rivoli, 75001 Paris, France', birthday: '1994-04-01', notes: 'Recommended by Lisa Kim for freelance design work', starred: false, groups: [], createdAt: '2025-11-01T10:00:00Z', updatedAt: '2026-02-15T16:00:00Z' },
    { id: 'ct_45', firstName: 'Ibrahim', lastName: 'Okafor', email: 'ibrahim.okafor@techstars.com', phone: '+234 803 123 4567', company: 'Techstars', jobTitle: 'Program Director', address: 'Victoria Island, Lagos, Nigeria', birthday: '1987-01-10', notes: 'Accelerator program mentor', starred: false, groups: ['grp_5'], createdAt: '2024-05-01T10:00:00Z', updatedAt: '2026-01-10T09:00:00Z' },
    { id: 'ct_46', firstName: 'Elena', lastName: 'Petrova', email: 'elena.petrova@yandex.ru', phone: '+7 495 123 4567', company: 'Yandex', jobTitle: 'Machine Learning Researcher', address: 'Lva Tolstogo 16, Moscow, Russia', birthday: '1991-07-14', notes: 'Co-authored paper on transformer architectures', starred: false, groups: ['grp_8'], createdAt: '2025-09-20T10:00:00Z', updatedAt: '2026-01-05T12:00:00Z' },
    { id: 'ct_47', firstName: 'Charlotte', lastName: 'Müller', email: 'charlotte.mueller@sap.com', phone: '+49 6227 7 12345', company: 'SAP', jobTitle: 'Cloud Solutions Director', address: 'Dietmar-Hopp-Allee 16, Walldorf, Germany', birthday: '1979-10-08', notes: 'Enterprise integration discussion', starred: false, groups: ['grp_8', 'grp_9'], createdAt: '2025-09-18T10:00:00Z', updatedAt: '2026-02-05T09:00:00Z' },
    { id: 'ct_48', firstName: 'Max', lastName: 'Wellington', email: 'max.wellington@gmail.com', phone: '+1 (773) 555-7001', company: '', jobTitle: '', address: '1400 N Lake Shore Dr, Chicago, IL 60610', birthday: '1995-08-22', notes: 'Fantasy football league commissioner', starred: false, groups: ['grp_3'], createdAt: '2022-08-15T14:00:00Z', updatedAt: '2025-09-01T10:00:00Z' },
    { id: 'ct_49', firstName: 'Samantha', lastName: 'Park-Williams', email: 'sam.parkwilliams@gmail.com', phone: '+1 (415) 555-7002', company: 'Lyft', jobTitle: 'Staff Software Engineer', address: '185 Berry St, San Francisco, CA 94107', birthday: '1992-02-29', notes: 'Leap year birthday! Met at Women in Tech meetup', starred: false, groups: ['grp_3', 'grp_6'], createdAt: '2023-03-01T14:00:00Z', updatedAt: '2026-02-29T09:00:00Z' },
    { id: 'ct_50', firstName: 'Raj', lastName: 'Kapoor', email: 'raj.kapoor@infosys.com', phone: '+91 80 2852 1234', company: 'Infosys', jobTitle: 'Delivery Manager', address: 'Electronics City, Bengaluru 560100, India', birthday: '1983-03-15', notes: 'Offshore development partnership', starred: false, groups: ['grp_9'], createdAt: '2024-11-01T10:00:00Z', updatedAt: '2026-03-01T08:00:00Z' },

    // More contacts for volume
    { id: 'ct_51', firstName: 'Zoe', lastName: 'Adams', email: 'zoe.adams@gmail.com', phone: '+1 (720) 555-8001', company: 'Zoom', jobTitle: 'Product Manager', address: '55 Almaden Blvd, San Jose, CA 95113', birthday: '1994-11-15', notes: '', starred: false, groups: ['grp_6'], createdAt: '2022-09-05T12:00:00Z', updatedAt: '2025-07-20T10:00:00Z' },
    { id: 'ct_52', firstName: 'Brandon', lastName: 'Cooper', email: 'brandon.cooper@microsoft.com', phone: '+1 (425) 555-8002', company: 'Microsoft', jobTitle: 'Azure Program Manager', address: '1 Microsoft Way, Redmond, WA 98052', birthday: '1988-06-08', notes: 'Cloud cost optimization workshop', starred: false, groups: ['grp_8', 'grp_9'], createdAt: '2025-09-15T14:00:00Z', updatedAt: '2026-03-10T09:00:00Z' },
    { id: 'ct_53', firstName: 'Alicia', lastName: 'Hernandez', email: 'alicia.hernandez@stripe.com', phone: '+1 (415) 555-8003', company: 'Stripe', jobTitle: 'Payments Integration Lead', address: '354 Oyster Point Blvd, South San Francisco, CA 94080', birthday: '1990-09-22', notes: 'Kevin Chen introduced us', starred: false, groups: ['grp_2'], createdAt: '2024-06-01T10:00:00Z', updatedAt: '2026-02-20T11:00:00Z' },
    { id: 'ct_54', firstName: 'Oscar', lastName: 'Lindqvist', email: 'oscar.lindqvist@klarna.com', phone: '+46 8 120 120 00', company: 'Klarna', jobTitle: 'Head of Risk', address: 'Sveavagen 46, Stockholm, Sweden', birthday: '1984-01-30', notes: 'Fintech meetup Stockholm', starred: false, groups: ['grp_8'], createdAt: '2025-10-05T10:00:00Z', updatedAt: '2026-01-20T09:00:00Z' },
    { id: 'ct_55', firstName: 'Yuki', lastName: 'Nakamura', email: 'yuki.nakamura@rakuten.co.jp', phone: '+81 50 5581 1234', company: 'Rakuten', jobTitle: 'Senior Platform Engineer', address: 'Setagaya-ku, Tokyo 158-0094', birthday: '1992-12-05', notes: '', starred: false, groups: ['grp_8'], createdAt: '2025-09-18T10:00:00Z', updatedAt: '2025-12-05T09:00:00Z' },
    { id: 'ct_56', firstName: 'Paula', lastName: 'Fernandez', email: 'paula.fernandez@mercadolibre.com', phone: '+54 11 4640 1234', company: 'MercadoLibre', jobTitle: 'Engineering Director', address: 'Arias 3751, Buenos Aires, Argentina', birthday: '1985-07-08', notes: 'LatAm expansion contact', starred: false, groups: ['grp_8'], createdAt: '2025-10-10T10:00:00Z', updatedAt: '2026-02-01T09:00:00Z' },
    { id: 'ct_57', firstName: 'Henry', lastName: 'Wright', email: 'henry.wright@gmail.com', phone: '+1 (415) 555-8004', company: 'Self-employed', jobTitle: 'Real Estate Agent', address: '1 Market St, San Francisco, CA 94105', birthday: '1978-04-20', notes: 'Helped us find the office space', starred: false, groups: [], createdAt: '2023-05-01T10:00:00Z', updatedAt: '2025-05-01T10:00:00Z' },
    { id: 'ct_58', firstName: 'Leah', lastName: 'Mitchell', email: 'leah.mitchell@gmail.com', phone: '+1 (415) 555-8005', company: 'Sutter Health', jobTitle: 'Physical Therapist', address: '2300 Sutter St, San Francisco, CA 94115', birthday: '1990-03-12', notes: 'PT for running injury', starred: false, groups: [], createdAt: '2025-06-01T10:00:00Z', updatedAt: '2026-01-15T14:00:00Z' },
    { id: 'ct_59', firstName: 'Ethan', lastName: 'Goldstein', email: 'ethan.goldstein@ycombinator.com', phone: '+1 (415) 555-8006', company: 'Y Combinator', jobTitle: 'Group Partner', address: '335 Pioneer Way, Mountain View, CA 94041', birthday: '1986-11-02', notes: 'YC W22 batch advisor', starred: true, groups: ['grp_5', 'grp_10'], createdAt: '2023-03-05T09:00:00Z', updatedAt: '2026-03-15T09:00:00Z' },
    { id: 'ct_60', firstName: 'Jasmine', lastName: 'Tran', email: 'jasmine.tran@notion.so', phone: '+1 (415) 555-8007', company: 'Notion', jobTitle: 'Chief of Staff', address: '2300 Harrison St, San Francisco, CA 94110', birthday: '1993-05-28', notes: 'Productivity tools discussion', starred: false, groups: [], createdAt: '2025-02-01T10:00:00Z', updatedAt: '2026-02-15T10:00:00Z' },

    // Even more for realistic volume (abbreviated fields)
    { id: 'ct_61', firstName: 'Adrian', lastName: 'Costa', email: 'adrian.costa@uber.com', phone: '+1 (415) 555-9001', company: 'Uber', jobTitle: 'Staff Engineer', address: '1515 3rd St, San Francisco, CA 94158', birthday: '1989-02-14', notes: '', starred: false, groups: ['grp_6'], createdAt: '2022-09-10T12:00:00Z', updatedAt: '2025-06-01T10:00:00Z' },
    { id: 'ct_62', firstName: 'Nora', lastName: 'Eriksson', email: 'nora.eriksson@gmail.com', phone: '+46 73 456 7890', company: '', jobTitle: '', address: 'Goteborg, Sweden', birthday: '1996-08-30', notes: 'Sophia colleague, met at dinner', starred: false, groups: ['grp_3'], createdAt: '2024-01-15T19:00:00Z', updatedAt: '2025-08-30T10:00:00Z' },
    { id: 'ct_63', firstName: 'Philip', lastName: 'Okonkwo', email: 'philip.okonkwo@andela.com', phone: '+234 802 987 6543', company: 'Andela', jobTitle: 'Senior Developer', address: 'Ikoyi, Lagos, Nigeria', birthday: '1991-04-18', notes: 'Remote contractor candidate', starred: false, groups: ['grp_4'], createdAt: '2025-05-01T10:00:00Z', updatedAt: '2026-01-15T09:00:00Z' },
    { id: 'ct_64', firstName: 'Rebecca', lastName: 'Stone', email: 'rebecca.stone@aclu.org', phone: '+1 (212) 555-9002', company: 'ACLU', jobTitle: 'Digital Rights Attorney', address: '125 Broad St, New York, NY 10004', birthday: '1987-12-15', notes: 'Privacy policy review', starred: false, groups: [], createdAt: '2025-08-01T10:00:00Z', updatedAt: '2026-02-01T14:00:00Z' },
    { id: 'ct_65', firstName: 'Marco', lastName: 'Rossi', email: 'marco.rossi@ferrari.com', phone: '+39 0536 949111', company: 'Ferrari', jobTitle: 'Head of Digital', address: 'Via Emilia Est 1163, Modena, Italy', birthday: '1982-09-14', notes: 'Met at Dreamforce - car enthusiast chat', starred: false, groups: ['grp_8'], createdAt: '2025-09-20T10:00:00Z', updatedAt: '2025-12-01T09:00:00Z' },
    { id: 'ct_66', firstName: 'Diane', lastName: 'Chen', email: 'diane.chen@gmail.com', phone: '+1 (626) 555-9003', company: 'UCLA Health', jobTitle: 'Cardiologist', address: '757 Westwood Plaza, Los Angeles, CA 90095', birthday: '1968-05-22', notes: 'Cousin Diane - Pasadena branch of family', starred: false, groups: ['grp_1'], createdAt: '2021-04-05T10:00:00Z', updatedAt: '2025-05-22T09:00:00Z' },
    { id: 'ct_67', firstName: 'Steven', lastName: 'Park', email: 'steven.park@coinbase.com', phone: '+1 (415) 555-9004', company: 'Coinbase', jobTitle: 'Compliance Officer', address: '100 Pine St, San Francisco, CA 94111', birthday: '1986-10-09', notes: 'Crypto regulatory advisor', starred: false, groups: ['grp_8'], createdAt: '2025-09-22T10:00:00Z', updatedAt: '2026-01-10T11:00:00Z' },
    { id: 'ct_68', firstName: 'Laura', lastName: 'Chen-Watkins', email: 'laura.chenwatkins@gmail.com', phone: '+1 (415) 555-9005', company: '', jobTitle: 'Stay-at-home parent', address: '1200 Masonic Ave, San Francisco, CA 94117', birthday: '1993-11-08', notes: 'Kevin cousin, married Ben Watkins\'s brother', starred: false, groups: ['grp_1', 'grp_3'], createdAt: '2022-06-01T10:00:00Z', updatedAt: '2025-11-08T10:00:00Z' },
    { id: 'ct_69', firstName: 'Anders', lastName: 'Bjornsson', email: 'anders.bjornsson@volvo.com', phone: '+46 31 325 0000', company: 'Volvo Group', jobTitle: 'Autonomous Driving Lead', address: 'Gotaverksgatan 2, Gothenburg, Sweden', birthday: '1980-03-25', notes: 'Connected through Ingrid Johansson', starred: false, groups: ['grp_8'], createdAt: '2025-11-01T10:00:00Z', updatedAt: '2026-02-15T09:00:00Z' },
    { id: 'ct_70', firstName: 'Christine', lastName: 'Abara', email: 'c.abara@who.int', phone: '+41 22 791 2111', company: 'World Health Organization', jobTitle: 'Digital Health Specialist', address: 'Avenue Appia 20, Geneva, Switzerland', birthday: '1984-06-30', notes: 'Health tech initiative collaboration', starred: false, groups: ['grp_8'], createdAt: '2025-10-15T10:00:00Z', updatedAt: '2026-03-01T10:00:00Z' },

    // More contacts for 100+ total
    { id: 'ct_71', firstName: 'Martin', lastName: 'Schneider', email: 'martin.schneider@siemens.com', phone: '+49 89 636 00', company: 'Siemens', jobTitle: 'IoT Solutions Architect', address: 'Werner-von-Siemens-Str. 1, Munich, Germany', birthday: '1981-07-12', notes: '', starred: false, groups: ['grp_8'], createdAt: '2025-09-19T10:00:00Z', updatedAt: '2025-12-15T09:00:00Z' },
    { id: 'ct_72', firstName: 'Aria', lastName: 'Pham', email: 'aria.pham@figma.com', phone: '+1 (415) 555-9006', company: 'Figma', jobTitle: 'Design Systems Lead', address: '760 Market St, San Francisco, CA 94102', birthday: '1994-12-20', notes: 'Design tool migration POC', starred: false, groups: ['grp_9'], createdAt: '2025-04-01T10:00:00Z', updatedAt: '2026-02-20T14:00:00Z' },
    { id: 'ct_73', firstName: 'Jonathan', lastName: 'Price', email: 'j.price@mongodb.com', phone: '+1 (646) 555-9007', company: 'MongoDB', jobTitle: 'Senior Solutions Architect', address: '1633 Broadway, New York, NY 10019', birthday: '', notes: 'Database migration advisor', starred: false, groups: ['grp_9'], createdAt: '2024-09-01T10:00:00Z', updatedAt: '2026-01-05T10:00:00Z' },
    { id: 'ct_74', firstName: 'Simone', lastName: 'Laurent', email: 'simone.laurent@doctolib.fr', phone: '+33 1 86 65 00 00', company: 'Doctolib', jobTitle: 'Head of Engineering', address: '54 Quai Charles Pasqua, Levallois-Perret, France', birthday: '1988-02-22', notes: 'Scaling advice for EU market', starred: false, groups: ['grp_8'], createdAt: '2025-09-25T10:00:00Z', updatedAt: '2026-01-22T09:00:00Z' },
    { id: 'ct_75', firstName: 'Douglas', lastName: 'Kim', email: 'douglas.kim@samsung.com', phone: '+82 2 2255 0114', company: 'Samsung Electronics', jobTitle: 'VP Mobile Platforms', address: 'Seocho-gu, Seoul, South Korea', birthday: '1977-08-05', notes: 'SDK integration partner', starred: false, groups: ['grp_8', 'grp_10'], createdAt: '2025-10-01T10:00:00Z', updatedAt: '2026-03-08T08:00:00Z' },
    { id: 'ct_76', firstName: 'Monica', lastName: 'Reyes', email: 'monica.reyes@gmail.com', phone: '+1 (305) 555-9008', company: 'Wix', jobTitle: 'Growth Marketing Manager', address: '1000 Brickell Ave, Miami, FL 33131', birthday: '1991-10-31', notes: 'Friend from marketing conference', starred: false, groups: ['grp_3'], createdAt: '2024-04-01T14:00:00Z', updatedAt: '2025-10-31T10:00:00Z' },
    { id: 'ct_77', firstName: 'Tomas', lastName: 'Novak', email: 'tomas.novak@avast.com', phone: '+420 274 005 555', company: 'Avast', jobTitle: 'Threat Intelligence Analyst', address: 'Pikrtova 1737/1a, Prague, Czech Republic', birthday: '1990-01-17', notes: 'Security vendor evaluation', starred: false, groups: ['grp_9'], createdAt: '2025-02-01T10:00:00Z', updatedAt: '2026-02-01T14:00:00Z' },
    { id: 'ct_78', firstName: 'Julia', lastName: 'Svensson', email: 'julia.svensson@king.com', phone: '+46 8 510 600 00', company: 'King (Activision Blizzard)', jobTitle: 'Game Economy Designer', address: 'Sveavagen 44, Stockholm, Sweden', birthday: '1993-03-19', notes: 'Gamification consulting', starred: false, groups: ['grp_8'], createdAt: '2025-09-20T10:00:00Z', updatedAt: '2026-01-19T09:00:00Z' },
    { id: 'ct_79', firstName: 'Aaron', lastName: 'Blake', email: 'aaron.blake@hashicorp.com', phone: '+1 (415) 555-9009', company: 'HashiCorp', jobTitle: 'Developer Advocate', address: '101 2nd St, San Francisco, CA 94105', birthday: '1992-07-04', notes: 'Terraform workshop instructor', starred: false, groups: ['grp_9'], createdAt: '2024-10-01T10:00:00Z', updatedAt: '2026-03-04T10:00:00Z' },
    { id: 'ct_80', firstName: 'Chloe', lastName: 'Delacroix', email: 'chloe.delacroix@airbus.com', phone: '+33 5 61 93 33 33', company: 'Airbus', jobTitle: 'AI Research Scientist', address: '1 Rond-Point Maurice Bellonte, Toulouse, France', birthday: '1989-09-15', notes: 'Met at NeurIPS poster session', starred: false, groups: ['grp_8'], createdAt: '2025-12-01T10:00:00Z', updatedAt: '2026-02-15T09:00:00Z' },

    // Additional contacts to push past 100
    { id: 'ct_81', firstName: 'Victor', lastName: 'Huang', email: 'victor.huang@tencent.com', phone: '+86 755 8601 3388', company: 'Tencent', jobTitle: 'VP Cloud Services', address: 'Nanshan District, Shenzhen, China', birthday: '1979-04-28', notes: '', starred: false, groups: ['grp_8'], createdAt: '2025-10-05T10:00:00Z', updatedAt: '2026-01-05T08:00:00Z' },
    { id: 'ct_82', firstName: 'Anna', lastName: 'Kowalski', email: 'anna.kowalski@allegro.pl', phone: '+48 61 856 5000', company: 'Allegro', jobTitle: 'CTO', address: 'Grunwaldzka 182, Poznan, Poland', birthday: '1983-12-28', notes: 'Polish ecommerce leader', starred: false, groups: ['grp_8'], createdAt: '2025-09-28T10:00:00Z', updatedAt: '2025-12-28T09:00:00Z' },
    { id: 'ct_83', firstName: 'Lucas', lastName: 'De Souza', email: 'lucas.desouza@nubank.com.br', phone: '+55 11 4020 1234', company: 'Nubank', jobTitle: 'Head of Platform Engineering', address: 'Rua Capote Valente 39, Sao Paulo, Brazil', birthday: '1987-05-02', notes: 'Fintech infrastructure discussion', starred: false, groups: ['grp_8'], createdAt: '2025-10-12T10:00:00Z', updatedAt: '2026-02-02T09:00:00Z' },
    { id: 'ct_84', firstName: 'Sarah', lastName: 'Mitchell', email: 'sarah.mitchell@deloitte.com', phone: '+1 (212) 555-9010', company: 'Deloitte', jobTitle: 'Senior Manager, Tech Advisory', address: '30 Rockefeller Plaza, New York, NY 10112', birthday: '1985-06-11', notes: 'Compliance audit preparation', starred: false, groups: ['grp_9'], createdAt: '2025-03-01T10:00:00Z', updatedAt: '2026-03-11T10:00:00Z' },
    { id: 'ct_85', firstName: 'George', lastName: 'Papadopoulos', email: 'george.papadopoulos@deliveryhero.com', phone: '+49 30 5444 590 00', company: 'Delivery Hero', jobTitle: 'Platform Architect', address: 'Oranienburger Str. 70, Berlin, Germany', birthday: '1986-11-23', notes: '', starred: false, groups: ['grp_8'], createdAt: '2025-09-22T10:00:00Z', updatedAt: '2025-11-23T09:00:00Z' },
    { id: 'ct_86', firstName: 'Lily', lastName: 'Tan', email: 'lily.tan@grab.com', phone: '+65 6514 2323', company: 'Grab', jobTitle: 'Director of Engineering', address: '3 Media Close, Singapore 138498', birthday: '1988-08-18', notes: 'SEA market insights', starred: false, groups: ['grp_8'], createdAt: '2025-10-08T10:00:00Z', updatedAt: '2026-01-18T09:00:00Z' },
    { id: 'ct_87', firstName: 'Robert', lastName: 'Campbell', email: 'robert.campbell@atlassian.com', phone: '+61 2 9262 1443', company: 'Atlassian', jobTitle: 'Head of Enterprise Sales', address: '341 George St, Sydney NSW 2000, Australia', birthday: '1981-03-07', notes: 'Jira enterprise license negotiation', starred: false, groups: ['grp_9'], createdAt: '2024-07-01T10:00:00Z', updatedAt: '2026-03-07T08:00:00Z' },
    { id: 'ct_88', firstName: 'Karen', lastName: 'White', email: 'karen.white@gmail.com', phone: '+1 (415) 555-9011', company: '', jobTitle: 'Yoga Instructor', address: '3150 18th St, San Francisco, CA 94110', birthday: '1991-01-05', notes: 'Tuesday/Thursday yoga class', starred: false, groups: ['grp_3'], createdAt: '2024-09-01T08:00:00Z', updatedAt: '2025-09-01T08:00:00Z' },
    { id: 'ct_89', firstName: 'Nathan', lastName: 'Ford', email: 'nathan.ford@palantir.com', phone: '+1 (650) 555-9012', company: 'Palantir Technologies', jobTitle: 'Forward Deployed Engineer', address: '100 Hamilton Ave, Palo Alto, CA 94301', birthday: '1990-12-12', notes: 'Data analytics platform demo', starred: false, groups: ['grp_9'], createdAt: '2025-06-01T10:00:00Z', updatedAt: '2026-02-12T14:00:00Z' },
    { id: 'ct_90', firstName: 'Wendy', lastName: 'Zhao', email: 'wendy.zhao@pinduoduo.com', phone: '+86 21 6185 1234', company: 'Pinduoduo', jobTitle: 'International Growth Lead', address: 'Changning District, Shanghai, China', birthday: '1992-10-05', notes: '', starred: false, groups: ['grp_8'], createdAt: '2025-10-15T10:00:00Z', updatedAt: '2026-01-05T08:00:00Z' },
    { id: 'ct_91', firstName: 'Chris', lastName: 'Evans', email: 'chris.evans@vercel.com', phone: '+1 (415) 555-9013', company: 'Vercel', jobTitle: 'Solutions Architect', address: '340 S Lemon Ave, Walnut, CA 91789', birthday: '1993-06-13', notes: 'Frontend deployment optimization', starred: false, groups: ['grp_9'], createdAt: '2025-07-01T10:00:00Z', updatedAt: '2026-03-13T10:00:00Z' },
    { id: 'ct_92', firstName: 'Priscilla', lastName: 'Obi', email: 'priscilla.obi@flutterwave.com', phone: '+234 701 234 5678', company: 'Flutterwave', jobTitle: 'API Integration Lead', address: 'Victoria Island, Lagos, Nigeria', birthday: '1991-09-30', notes: 'African payments gateway partner', starred: false, groups: ['grp_9'], createdAt: '2025-04-01T10:00:00Z', updatedAt: '2026-02-28T09:00:00Z' },
    { id: 'ct_93', firstName: 'Timothy', lastName: 'Buchanan', email: 'tim.buchanan@gmail.com', phone: '+1 (415) 555-9014', company: 'Retired', jobTitle: '', address: '1600 Holloway Ave, San Francisco, CA 94132', birthday: '1960-08-15', notes: 'Neighbor - helps with mail when traveling', starred: false, groups: [], createdAt: '2022-01-01T10:00:00Z', updatedAt: '2024-12-15T10:00:00Z' },
    { id: 'ct_94', firstName: 'Fiona', lastName: 'MacLeod', email: 'fiona.macleod@skyscanner.net', phone: '+44 131 220 6012', company: 'Skyscanner', jobTitle: 'Head of ML', address: '1 Lochrin Square, Edinburgh EH3 9QA, UK', birthday: '1986-04-22', notes: 'Travel tech + ML discussion', starred: false, groups: ['grp_8'], createdAt: '2025-09-25T10:00:00Z', updatedAt: '2026-01-22T09:00:00Z' },
    { id: 'ct_95', firstName: 'Hugo', lastName: 'Morales', email: 'hugo.morales@rappi.com', phone: '+57 1 381 1234', company: 'Rappi', jobTitle: 'VP of Technology', address: 'Carrera 13, Bogota, Colombia', birthday: '1984-11-08', notes: '', starred: false, groups: ['grp_8'], createdAt: '2025-10-20T10:00:00Z', updatedAt: '2026-01-08T09:00:00Z' },
    { id: 'ct_96', firstName: 'Diana', lastName: 'Petrova', email: 'diana.petrova@wolt.com', phone: '+358 20 770 0123', company: 'Wolt', jobTitle: 'Engineering Manager', address: 'Arkadiankatu 6, Helsinki, Finland', birthday: '1990-07-16', notes: 'Nordic tech scene introduction', starred: false, groups: ['grp_8'], createdAt: '2025-11-05T10:00:00Z', updatedAt: '2026-02-16T09:00:00Z' },
    { id: 'ct_97', firstName: 'Keith', lastName: 'Robinson', email: 'keith.robinson@twilio.com', phone: '+1 (415) 555-9015', company: 'Twilio', jobTitle: 'API Products Director', address: '101 Spear St, San Francisco, CA 94105', birthday: '1987-02-08', notes: 'SMS/voice notification integration', starred: false, groups: ['grp_9'], createdAt: '2024-12-01T10:00:00Z', updatedAt: '2026-03-08T10:00:00Z' },
    { id: 'ct_98', firstName: 'Amelia', lastName: 'Chang', email: 'amelia.chang@shopify.com', phone: '+1 (613) 555-9016', company: 'Shopify', jobTitle: 'Staff Developer', address: '150 Elgin St, Ottawa, ON K2P 1L4, Canada', birthday: '1992-03-28', notes: 'E-commerce platform evaluation', starred: false, groups: ['grp_9'], createdAt: '2025-01-01T10:00:00Z', updatedAt: '2026-02-28T10:00:00Z' },
    { id: 'ct_99', firstName: 'Walter', lastName: 'Brandt', email: 'walter.brandt@bosch.com', phone: '+49 711 811 0', company: 'Bosch', jobTitle: 'IoT Division Director', address: 'Robert-Bosch-Platz 1, Gerlingen, Germany', birthday: '1976-09-01', notes: 'Industrial IoT partnership exploration', starred: false, groups: ['grp_8'], createdAt: '2025-09-30T10:00:00Z', updatedAt: '2026-01-01T09:00:00Z' },
    { id: 'ct_100', firstName: 'Isabelle', lastName: 'Martin', email: 'isabelle.martin@blablacar.com', phone: '+33 1 85 76 22 22', company: 'BlaBlaCar', jobTitle: 'Head of Platform', address: '84 Rue de Grenelle, Paris, France', birthday: '1988-12-10', notes: '', starred: false, groups: ['grp_8'], createdAt: '2025-10-25T10:00:00Z', updatedAt: '2025-12-10T09:00:00Z' },
    { id: 'ct_101', firstName: 'Damian', lastName: 'Kowalczyk', email: 'damian.kowalczyk@gmail.com', phone: '+48 22 123 4567', company: '', jobTitle: 'Freelance DevOps', address: 'Warsaw, Poland', birthday: '1994-05-19', notes: 'Contractor for Kubernetes migration', starred: false, groups: ['grp_4'], createdAt: '2025-08-01T10:00:00Z', updatedAt: '2026-03-01T09:00:00Z' },
    { id: 'ct_102', firstName: 'Naomi', lastName: 'Ito', email: 'naomi.ito@line.me', phone: '+81 3 4316 2500', company: 'LINE Corporation', jobTitle: 'Product Strategy Lead', address: 'Shibuya-ku, Tokyo 150-8512', birthday: '1990-01-23', notes: 'Messaging platform comparison', starred: false, groups: ['grp_8'], createdAt: '2025-10-28T10:00:00Z', updatedAt: '2026-01-23T09:00:00Z' },
    { id: 'ct_103', firstName: 'Peter', lastName: 'Strand', email: 'peter.strand@ericsson.com', phone: '+46 10 719 0000', company: 'Ericsson', jobTitle: '5G Solutions Architect', address: 'Torshamnsgatan 21, Stockholm, Sweden', birthday: '1982-10-14', notes: '5G edge computing discussion', starred: false, groups: ['grp_8'], createdAt: '2025-09-23T10:00:00Z', updatedAt: '2025-12-14T09:00:00Z' },
    { id: 'ct_104', firstName: 'Alice', lastName: 'Nakamura', email: 'alice.nakamura@gmail.com', phone: '+1 (408) 555-9017', company: 'Apple', jobTitle: 'Privacy Engineer', address: 'One Apple Park Way, Cupertino, CA 95014', birthday: '1993-07-07', notes: 'Met through Rachel Park - privacy-preserving ML', starred: false, groups: ['grp_6'], createdAt: '2023-01-15T12:00:00Z', updatedAt: '2026-01-07T10:00:00Z' },
    { id: 'ct_105', firstName: 'Frank', lastName: 'Dubois', email: 'frank.dubois@gmail.com', phone: '+1 (415) 555-9018', company: '', jobTitle: 'Sommelier', address: '345 California St, San Francisco, CA 94104', birthday: '1975-11-20', notes: 'Wine tasting events organizer', starred: false, groups: ['grp_3'], createdAt: '2023-09-01T19:00:00Z', updatedAt: '2025-11-20T10:00:00Z' },
    { id: 'ct_106', firstName: 'Megan', lastName: 'Foster-Kim', email: 'megan.fosterkim@techcorp.io', phone: '+1 (415) 555-1020', company: 'TechCorp', jobTitle: 'HR Business Partner', address: '500 Howard St, San Francisco, CA 94105', birthday: '1989-08-24', notes: 'HR contact for eng team', starred: false, groups: ['grp_2'], createdAt: '2022-04-01T09:00:00Z', updatedAt: '2026-02-24T10:00:00Z' },
    { id: 'ct_107', firstName: 'Ivan', lastName: 'Volkov', email: 'ivan.volkov@kaspersky.com', phone: '+7 495 797 8700', company: 'Kaspersky', jobTitle: 'Threat Research Lead', address: 'Leningradskoe Shosse 39A, Moscow, Russia', birthday: '1985-03-02', notes: 'Cybersecurity intelligence sharing', starred: false, groups: ['grp_9'], createdAt: '2025-05-15T10:00:00Z', updatedAt: '2026-01-02T09:00:00Z' },
    { id: 'ct_108', firstName: 'Sophie', lastName: 'Williams', email: 'sophie.williams@bbc.co.uk', phone: '+44 20 7580 4468', company: 'BBC', jobTitle: 'Technology Correspondent', address: 'Broadcasting House, London W1A 1AA, UK', birthday: '1990-06-15', notes: 'Interview request about AI ethics', starred: false, groups: [], createdAt: '2026-01-10T10:00:00Z', updatedAt: '2026-03-15T16:00:00Z' },
    { id: 'ct_109', firstName: 'Takeshi', lastName: 'Mori', email: 'takeshi.mori@toyota.co.jp', phone: '+81 565 28 2121', company: 'Toyota Motor Corporation', jobTitle: 'Connected Services Director', address: 'Toyota City, Aichi, Japan', birthday: '1978-02-11', notes: 'Connected vehicle API partnership', starred: false, groups: ['grp_8'], createdAt: '2025-11-10T10:00:00Z', updatedAt: '2026-02-11T09:00:00Z' },
    { id: 'ct_110', firstName: 'Gabriella', lastName: 'Romano', email: 'gabriella.romano@unicredit.eu', phone: '+39 02 8862 1', company: 'UniCredit', jobTitle: 'Head of Digital Banking', address: 'Piazza Gae Aulenti 3, Milan, Italy', birthday: '1983-04-30', notes: 'Banking API standardization', starred: false, groups: ['grp_8'], createdAt: '2025-10-30T10:00:00Z', updatedAt: '2026-01-30T09:00:00Z' },
    { id: 'ct_111', firstName: 'Helen', lastName: 'Zhao', email: 'helen.zhao@bytedance.com', phone: '+86 10 5765 9999', company: 'ByteDance', jobTitle: 'Data Privacy Counsel', address: 'Zhongguancun, Haidian, Beijing', birthday: '1986-05-18', notes: 'Wei Zhao referred - data governance questions', starred: false, groups: ['grp_8'], createdAt: '2025-11-15T10:00:00Z', updatedAt: '2026-02-18T09:00:00Z' },
    { id: 'ct_112', firstName: 'Omar', lastName: 'Hassan', email: 'omar.hassan@careem.com', phone: '+971 4 456 1234', company: 'Careem', jobTitle: 'CTO', address: 'Dubai Internet City, Dubai, UAE', birthday: '1982-01-15', notes: 'MENA market expansion discussion', starred: false, groups: ['grp_8'], createdAt: '2025-11-20T10:00:00Z', updatedAt: '2026-02-15T08:00:00Z' },
    { id: 'ct_113', firstName: 'Penny', lastName: 'Crawford', email: 'penny.crawford@gmail.com', phone: '+1 (415) 555-9019', company: '', jobTitle: 'Dog Walker', address: '2750 Geary Blvd, San Francisco, CA 94118', birthday: '1998-09-10', notes: 'Walks Max on Wednesdays', starred: false, groups: [], createdAt: '2025-04-01T10:00:00Z', updatedAt: '2025-09-10T10:00:00Z' },
    { id: 'ct_114', firstName: 'Raymond', lastName: 'Torres', email: 'raymond.torres@elastic.co', phone: '+1 (650) 555-9020', company: 'Elastic', jobTitle: 'Principal Consultant', address: '800 W El Camino Real, Mountain View, CA 94040', birthday: '1984-08-31', notes: 'Elasticsearch cluster optimization', starred: false, groups: ['grp_9'], createdAt: '2025-02-15T10:00:00Z', updatedAt: '2026-02-28T14:00:00Z' },
    { id: 'ct_115', firstName: 'Kira', lastName: 'Volkov', email: 'kira.volkov@techcorp.io', phone: '+1 (415) 555-1021', company: 'TechCorp', jobTitle: 'Intern, Backend Engineering', address: '500 Howard St, San Francisco, CA 94105', birthday: '2002-04-15', notes: 'Summer 2026 intern - mentoring', starred: false, groups: ['grp_2', 'grp_4'], createdAt: '2026-03-01T09:00:00Z', updatedAt: '2026-03-15T10:00:00Z' },
    { id: 'ct_116', firstName: 'Nicholas', lastName: 'Harper', email: 'nicholas.harper.esq@gmail.com', phone: '+1 (415) 555-9021', company: 'Harper & Associates', jobTitle: 'Attorney at Law', address: '580 California St, Suite 1200, San Francisco, CA 94104', birthday: '1970-10-05', notes: 'Corporate counsel - IP matters', starred: true, groups: ['grp_10'], createdAt: '2023-08-01T10:00:00Z', updatedAt: '2026-03-05T10:00:00Z' },
    { id: 'ct_117', firstName: 'Sonia', lastName: 'Gupta', email: 'sonia.gupta@wipro.com', phone: '+91 80 2844 0011', company: 'Wipro', jobTitle: 'Cloud Practice Head', address: 'Sarjapur Road, Bengaluru 560035, India', birthday: '1982-11-28', notes: 'Managed services evaluation', starred: false, groups: ['grp_9'], createdAt: '2025-01-15T10:00:00Z', updatedAt: '2026-01-28T09:00:00Z' },
    { id: 'ct_118', firstName: 'Felix', lastName: 'Bergmann', email: 'felix.bergmann@zalando.de', phone: '+49 30 2096 0', company: 'Zalando', jobTitle: 'Senior Data Engineer', address: 'Valeska-Gert-Str. 5, Berlin, Germany', birthday: '1991-06-25', notes: 'Data pipeline architecture discussion', starred: false, groups: ['grp_8'], createdAt: '2025-09-28T10:00:00Z', updatedAt: '2025-12-25T09:00:00Z' },
    { id: 'ct_119', firstName: 'Rosa', lastName: 'Gonzalez', email: 'rosa.gonzalez@bbva.com', phone: '+34 91 374 6000', company: 'BBVA', jobTitle: 'Open Banking Director', address: 'Calle Azul 4, Madrid, Spain', birthday: '1984-08-08', notes: 'Open banking API standards', starred: false, groups: ['grp_8'], createdAt: '2025-10-18T10:00:00Z', updatedAt: '2026-02-08T09:00:00Z' },
    { id: 'ct_120', firstName: 'Stanley', lastName: 'Chen', email: 'stanley.chen@gmail.com', phone: '+1 (510) 555-9022', company: 'UC Berkeley', jobTitle: 'Professor of EECS', address: 'Soda Hall, Berkeley, CA 94720', birthday: '1958-12-30', notes: 'Uncle Stanley - academic side of family', starred: false, groups: ['grp_1'], createdAt: '2021-04-10T10:00:00Z', updatedAt: '2025-12-30T09:00:00Z' }
];

// ─── Other Contacts (auto-saved from email interactions) ───
const OTHER_CONTACTS = [
    { id: 'oc_1', firstName: '', lastName: '', email: 'noreply@github.com', lastInteraction: '2026-03-18T05:00:00Z', interactionCount: 342 },
    { id: 'oc_2', firstName: 'Jason', lastName: '', email: 'jason.recruiter@linkedin.com', lastInteraction: '2026-03-17T14:00:00Z', interactionCount: 3 },
    { id: 'oc_3', firstName: 'Support', lastName: '', email: 'support@vercel.com', lastInteraction: '2026-03-16T10:00:00Z', interactionCount: 8 },
    { id: 'oc_4', firstName: 'Meeting', lastName: 'Bot', email: 'meetingbot@calendly.com', lastInteraction: '2026-03-15T09:00:00Z', interactionCount: 45 },
    { id: 'oc_5', firstName: '', lastName: '', email: 'billing@aws.amazon.com', lastInteraction: '2026-03-14T06:00:00Z', interactionCount: 24 },
    { id: 'oc_6', firstName: 'Mike', lastName: '', email: 'mike.sales@hubspot.com', lastInteraction: '2026-03-13T11:00:00Z', interactionCount: 5 },
    { id: 'oc_7', firstName: '', lastName: '', email: 'events@eventbrite.com', lastInteraction: '2026-03-10T15:00:00Z', interactionCount: 12 },
    { id: 'oc_8', firstName: 'Sarah', lastName: '', email: 'sarah@restaurant-reservation.com', lastInteraction: '2026-03-08T18:00:00Z', interactionCount: 2 },
    { id: 'oc_9', firstName: '', lastName: '', email: 'notifications@slack.com', lastInteraction: '2026-03-07T12:00:00Z', interactionCount: 156 },
    { id: 'oc_10', firstName: 'Travel', lastName: 'Desk', email: 'travel@corporatetravel.com', lastInteraction: '2026-03-05T09:00:00Z', interactionCount: 18 },
    { id: 'oc_11', firstName: '', lastName: '', email: 'receipts@uber.com', lastInteraction: '2026-03-04T22:00:00Z', interactionCount: 67 },
    { id: 'oc_12', firstName: 'Newsletter', lastName: '', email: 'hello@morningbrew.com', lastInteraction: '2026-03-04T06:00:00Z', interactionCount: 89 },
    { id: 'oc_13', firstName: '', lastName: '', email: 'no-reply@zoom.us', lastInteraction: '2026-03-03T14:00:00Z', interactionCount: 203 },
    { id: 'oc_14', firstName: 'IT', lastName: 'Help', email: 'it-helpdesk@techcorp.io', lastInteraction: '2026-03-01T10:00:00Z', interactionCount: 31 },
    { id: 'oc_15', firstName: '', lastName: '', email: 'alerts@sentry.io', lastInteraction: '2026-02-28T03:00:00Z', interactionCount: 112 },
    { id: 'oc_16', firstName: 'Dr.', lastName: 'Patel', email: 'appointments@sfmedical.com', lastInteraction: '2026-02-25T09:00:00Z', interactionCount: 4 },
    { id: 'oc_17', firstName: '', lastName: '', email: 'order-confirm@amazon.com', lastInteraction: '2026-02-20T16:00:00Z', interactionCount: 38 },
    { id: 'oc_18', firstName: 'Lisa', lastName: '', email: 'lisa@drycleaners-sf.com', lastInteraction: '2026-02-15T10:00:00Z', interactionCount: 7 },
    { id: 'oc_19', firstName: '', lastName: '', email: 'team@figma.com', lastInteraction: '2026-02-10T14:00:00Z', interactionCount: 15 },
    { id: 'oc_20', firstName: 'Alex', lastName: '', email: 'alex@doordash-driver.com', lastInteraction: '2026-02-05T19:00:00Z', interactionCount: 1 },
    { id: 'oc_21', firstName: '', lastName: '', email: 'security@1password.com', lastInteraction: '2026-01-30T08:00:00Z', interactionCount: 9 },
    { id: 'oc_22', firstName: '', lastName: '', email: 'updates@linear.app', lastInteraction: '2026-01-25T11:00:00Z', interactionCount: 56 },
    { id: 'oc_23', firstName: 'Amy', lastName: '', email: 'amy.realtor@compass.com', lastInteraction: '2026-01-20T14:00:00Z', interactionCount: 11 },
    { id: 'oc_24', firstName: '', lastName: '', email: 'digest@medium.com', lastInteraction: '2026-01-15T06:00:00Z', interactionCount: 124 },
    { id: 'oc_25', firstName: '', lastName: '', email: 'noreply@stripe.com', lastInteraction: '2026-01-10T10:00:00Z', interactionCount: 29 }
];

// ─── Directory (organization/workspace colleagues) ───
const DIRECTORY = [
    { id: 'dir_1', name: 'Sarah Chen', email: 'sarah.chen@techcorp.io', department: 'Engineering', title: 'Senior Software Engineer', location: 'San Francisco', phone: '+1 (415) 555-0192', manager: 'Priya Sharma' },
    { id: 'dir_2', name: 'James Wu', email: 'james.wu@techcorp.io', department: 'Engineering', title: 'Senior Backend Engineer', location: 'San Francisco', phone: '+1 (415) 555-1001', manager: 'Priya Sharma' },
    { id: 'dir_3', name: 'Priya Sharma', email: 'priya.sharma@techcorp.io', department: 'Engineering', title: 'Engineering Manager', location: 'San Francisco', phone: '+1 (415) 555-1002', manager: 'Marcus Johnson' },
    { id: 'dir_4', name: 'Alex Martinez', email: 'alex.martinez@techcorp.io', department: 'Engineering', title: 'Frontend Engineer', location: 'San Francisco', phone: '+1 (415) 555-1003', manager: 'Priya Sharma' },
    { id: 'dir_5', name: 'Mei Zhang', email: 'mei.zhang@techcorp.io', department: 'Engineering', title: 'DevOps Engineer', location: 'San Francisco', phone: '+1 (415) 555-1004', manager: 'Priya Sharma' },
    { id: 'dir_6', name: 'Tom O\'Brien', email: 'tom.obrien@techcorp.io', department: 'Engineering', title: 'QA Lead', location: 'San Francisco', phone: '+1 (415) 555-1005', manager: 'Marcus Johnson' },
    { id: 'dir_7', name: 'Nina Patel', email: 'nina.patel@techcorp.io', department: 'Engineering', title: 'Data Scientist', location: 'San Francisco', phone: '+1 (415) 555-1006', manager: 'Marcus Johnson' },
    { id: 'dir_8', name: 'Marcus Johnson', email: 'marcus.johnson@techcorp.io', department: 'Engineering', title: 'VP of Engineering', location: 'San Francisco', phone: '+1 (415) 555-1007', manager: 'CEO' },
    { id: 'dir_9', name: 'Lisa Kim', email: 'lisa.kim@techcorp.io', department: 'Design', title: 'Product Designer', location: 'San Francisco', phone: '+1 (415) 555-1008', manager: 'Diana Ross-Taylor' },
    { id: 'dir_10', name: 'Ryan Nguyen', email: 'ryan.nguyen@techcorp.io', department: 'Engineering', title: 'Security Engineer', location: 'San Francisco', phone: '+1 (415) 555-1009', manager: 'Marcus Johnson' },
    { id: 'dir_11', name: 'Hannah Cohen', email: 'hannah.cohen@techcorp.io', department: 'Engineering', title: 'Technical Writer', location: 'San Francisco', phone: '+1 (415) 555-1010', manager: 'Priya Sharma' },
    { id: 'dir_12', name: 'Diana Ross-Taylor', email: 'diana.ross-taylor@techcorp.io', department: 'Finance', title: 'CFO', location: 'San Francisco', phone: '+1 (415) 555-1011', manager: 'CEO' },
    { id: 'dir_13', name: 'Carlos Mendoza', email: 'carlos.mendoza@techcorp.io', department: 'Sales', title: 'Head of Sales', location: 'San Francisco', phone: '+1 (415) 555-1012', manager: 'CEO' },
    { id: 'dir_14', name: 'Sophia Andersson', email: 'sophia.andersson@techcorp.io', department: 'Operations', title: 'Head of EU Operations', location: 'Stockholm', phone: '+46 70 123 4567', manager: 'CEO' },
    { id: 'dir_15', name: 'Megan Foster-Kim', email: 'megan.fosterkim@techcorp.io', department: 'Human Resources', title: 'HR Business Partner', location: 'San Francisco', phone: '+1 (415) 555-1020', manager: 'Diana Ross-Taylor' },
    { id: 'dir_16', name: 'Kira Volkov', email: 'kira.volkov@techcorp.io', department: 'Engineering', title: 'Intern, Backend Engineering', location: 'San Francisco', phone: '+1 (415) 555-1021', manager: 'Priya Sharma' },
    { id: 'dir_17', name: 'David Park', email: 'david.park@techcorp.io', department: 'Product', title: 'Senior Product Manager', location: 'San Francisco', phone: '+1 (415) 555-1022', manager: 'Marcus Johnson' },
    { id: 'dir_18', name: 'Jennifer Walsh', email: 'jennifer.walsh@techcorp.io', department: 'Legal', title: 'General Counsel', location: 'San Francisco', phone: '+1 (415) 555-1023', manager: 'CEO' },
    { id: 'dir_19', name: 'Tony Russo', email: 'tony.russo@techcorp.io', department: 'Sales', title: 'Account Executive', location: 'New York', phone: '+1 (212) 555-1024', manager: 'Carlos Mendoza' },
    { id: 'dir_20', name: 'Elaine Cho', email: 'elaine.cho@techcorp.io', department: 'Marketing', title: 'Marketing Director', location: 'San Francisco', phone: '+1 (415) 555-1025', manager: 'CEO' },
    { id: 'dir_21', name: 'Brian Foster', email: 'brian.foster@techcorp.io', department: 'Engineering', title: 'Site Reliability Engineer', location: 'San Francisco', phone: '+1 (415) 555-1026', manager: 'Priya Sharma' },
    { id: 'dir_22', name: 'Alisha Patel', email: 'alisha.patel@techcorp.io', department: 'Design', title: 'UX Researcher', location: 'San Francisco', phone: '+1 (415) 555-1027', manager: 'Lisa Kim' },
    { id: 'dir_23', name: 'Kevin Zhang', email: 'kevin.zhang@techcorp.io', department: 'Engineering', title: 'Mobile Engineer', location: 'San Francisco', phone: '+1 (415) 555-1028', manager: 'Priya Sharma' },
    { id: 'dir_24', name: 'Maria Santos', email: 'maria.santos@techcorp.io', department: 'Customer Support', title: 'Support Team Lead', location: 'San Francisco', phone: '+1 (415) 555-1029', manager: 'Carlos Mendoza' },
    { id: 'dir_25', name: 'Eric Johansson', email: 'eric.johansson@techcorp.io', department: 'Engineering', title: 'Backend Engineer', location: 'Stockholm', phone: '+46 70 234 5678', manager: 'Sophia Andersson' }
];

// ─── App password entries (for sign-in security section) ───
const APP_PASSWORDS = [
    { id: 'ap_1', name: 'Thunderbird on MacBook', createdAt: '2025-06-15T10:00:00Z', lastUsed: '2026-03-18T07:00:00Z' },
    { id: 'ap_2', name: 'Mail on iPhone', createdAt: '2024-12-01T14:00:00Z', lastUsed: '2026-03-17T22:00:00Z' },
    { id: 'ap_3', name: 'Outlook Desktop', createdAt: '2025-09-20T09:00:00Z', lastUsed: '2026-03-10T08:00:00Z' }
];

// ─── Merge suggestions (duplicate contacts) ───
const MERGE_SUGGESTIONS = [
    {
        id: 'merge_1',
        contactIds: ['ct_46', 'oc_15_promoted'],
        reason: 'Similar email domain: yandex.ru',
        dismissed: false
    }
];

// ─── Reply-from setting ───
const REPLY_FROM_SETTING = 'default'; // 'default' = always reply from default, 'same' = reply from same address message was sent to
