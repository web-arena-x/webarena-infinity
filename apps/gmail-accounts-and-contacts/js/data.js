// ============================================================
// data.js — Rich, realistic seed data for Gmail Accounts & Contacts
// ============================================================
const SEED_DATA_VERSION = 1;

// ---- Current User ----
const CURRENT_USER = {
    id: 'user_1',
    name: 'Alex Johnson',
    email: 'alex.johnson@gmail.com',
    alternateEmails: ['a.johnson@workplace.io', 'alexj.dev@gmail.com'],
    phone: '+1 (415) 555-0142',
    avatarColor: '#1a73e8',
    recoveryEmail: 'alex.backup@outlook.com',
    recoveryPhone: '+1 (415) 555-0199',
    language: 'English (US)',
    timezone: 'America/Los_Angeles',
    profilePicture: null,
    createdAt: '2018-03-14T10:00:00Z',
    lastLogin: '2026-03-07T08:30:00Z'
};

// ---- Contact Labels/Groups ----
const CONTACT_LABELS = [
    { id: 'clabel_1', name: 'Family', color: '#EA4335', contactCount: 0 },
    { id: 'clabel_2', name: 'Friends', color: '#34A853', contactCount: 0 },
    { id: 'clabel_3', name: 'Work', color: '#4285F4', contactCount: 0 },
    { id: 'clabel_4', name: 'VIP Clients', color: '#FBBC04', contactCount: 0 },
    { id: 'clabel_5', name: 'Gym Buddies', color: '#FF6D01', contactCount: 0 },
    { id: 'clabel_6', name: 'College Alumni', color: '#9C27B0', contactCount: 0 },
    { id: 'clabel_7', name: 'Neighbors', color: '#009688', contactCount: 0 },
    { id: 'clabel_8', name: 'Book Club', color: '#795548', contactCount: 0 },
    { id: 'clabel_9', name: 'Vendors', color: '#607D8B', contactCount: 0 },
    { id: 'clabel_10', name: 'Emergency', color: '#F44336', contactCount: 0 },
    { id: 'clabel_11', name: 'Travel Contacts', color: '#00BCD4', contactCount: 0 },
    { id: 'clabel_12', name: 'Healthcare', color: '#E91E63', contactCount: 0 }
];

// ---- Contacts (main / manually saved) ----
const CONTACTS = [
    {
        id: 'contact_01', firstName: 'Sarah', lastName: 'Chen', email: 'sarah.chen@techcorp.io',
        phone: '+1 (650) 555-0101', company: 'TechCorp', jobTitle: 'VP of Product',
        address: '2100 Sand Hill Rd, Menlo Park, CA 94025',
        secondaryEmail: 'sarah.c.personal@gmail.com', secondaryPhone: '+1 (650) 555-0102',
        birthday: '1988-06-15', website: 'https://sarahchen.dev',
        notes: 'Met at AWS re:Invent 2024. Key partner for Q1 integration project.',
        labels: ['clabel_3', 'clabel_4'], isStarred: true, avatarColor: '#EA4335',
        createdAt: '2020-01-10T08:00:00Z', updatedAt: '2026-02-20T14:30:00Z', source: 'manual'
    },
    {
        id: 'contact_02', firstName: 'Marcus', lastName: 'Williams', email: 'marcus.w@designhub.com',
        phone: '+1 (415) 555-0203', company: 'DesignHub', jobTitle: 'Creative Director',
        address: '450 Mission St, San Francisco, CA 94105',
        secondaryEmail: '', secondaryPhone: '',
        birthday: '1990-11-22', website: 'https://marcuswilliams.design',
        notes: 'Design system collaborator. Prefers async communication.',
        labels: ['clabel_3', 'clabel_2'], isStarred: true, avatarColor: '#34A853',
        createdAt: '2019-06-15T12:00:00Z', updatedAt: '2026-01-18T09:00:00Z', source: 'manual'
    },
    {
        id: 'contact_03', firstName: 'Emily', lastName: 'Rodriguez', email: 'emily.r@startupventures.co',
        phone: '+1 (408) 555-0304', company: 'StartupVentures', jobTitle: 'Managing Partner',
        address: '1 Infinite Loop, Cupertino, CA 95014',
        secondaryEmail: 'emily.rodriguez@gmail.com', secondaryPhone: '',
        birthday: '1985-03-08', website: 'https://startupventures.co/team/emily',
        notes: 'Series B connector. Introduced us to 3 portfolio companies.',
        labels: ['clabel_3', 'clabel_4'], isStarred: true, avatarColor: '#FBBC04',
        createdAt: '2021-03-20T16:00:00Z', updatedAt: '2026-02-23T10:00:00Z', source: 'manual'
    },
    {
        id: 'contact_04', firstName: 'James', lastName: "O'Brien", email: 'james.obrien@lawfirm.legal',
        phone: '+1 (212) 555-0405', company: 'Morrison & Associates', jobTitle: 'Senior Partner',
        address: '375 Park Ave, New York, NY 10152',
        secondaryEmail: '', secondaryPhone: '+1 (212) 555-0406',
        birthday: '1972-09-30', website: '',
        notes: 'Corporate counsel. Handles all vendor agreements and NDAs.',
        labels: ['clabel_3', 'clabel_9'], isStarred: false, avatarColor: '#4285F4',
        createdAt: '2022-07-01T10:00:00Z', updatedAt: '2026-02-21T16:00:00Z', source: 'manual'
    },
    {
        id: 'contact_05', firstName: 'Priya', lastName: 'Sharma', email: 'priya.sharma@cloudnine.dev',
        phone: '+1 (510) 555-0507', company: 'CloudNine', jobTitle: 'Lead Backend Engineer',
        address: '1600 Amphitheatre Pkwy, Mountain View, CA 94043',
        secondaryEmail: 'priya.codes@gmail.com', secondaryPhone: '',
        birthday: '1992-12-04', website: 'https://github.com/priyasharma',
        notes: 'Key technical collaborator. Expert in distributed systems.',
        labels: ['clabel_3'], isStarred: true, avatarColor: '#9C27B0',
        createdAt: '2020-09-05T11:00:00Z', updatedAt: '2026-02-24T08:42:00Z', source: 'manual'
    },
    {
        id: 'contact_06', firstName: 'David', lastName: 'Kim', email: 'david.kim@financeplus.com',
        phone: '+1 (312) 555-0608', company: 'FinancePlus', jobTitle: 'CFO',
        address: '233 S Wacker Dr, Chicago, IL 60606',
        secondaryEmail: 'dkim.personal@yahoo.com', secondaryPhone: '+1 (312) 555-0609',
        birthday: '1980-07-19', website: '',
        notes: 'Financial advisor. Handles tax prep and quarterly reports.',
        labels: ['clabel_3', 'clabel_4'], isStarred: false, avatarColor: '#FF5722',
        createdAt: '2019-01-15T09:00:00Z', updatedAt: '2026-02-23T14:00:00Z', source: 'manual'
    },
    {
        id: 'contact_07', firstName: 'Lisa', lastName: 'Nakamura', email: 'lisa.n@creativeagency.co',
        phone: '+1 (310) 555-0710', company: 'Creative Agency Co.', jobTitle: 'Art Director',
        address: '8560 Sunset Blvd, West Hollywood, CA 90069',
        secondaryEmail: '', secondaryPhone: '',
        birthday: '1993-04-27', website: 'https://lisanakamura.art',
        notes: 'Brand refresh project lead. Excellent eye for typography.',
        labels: ['clabel_3'], isStarred: false, avatarColor: '#009688',
        createdAt: '2023-02-14T14:00:00Z', updatedAt: '2026-02-15T11:00:00Z', source: 'manual'
    },
    {
        id: 'contact_08', firstName: 'Tom', lastName: 'Bradley', email: 'tom.bradley@realtyhome.com',
        phone: '+1 (925) 555-0811', company: 'Realty Home', jobTitle: 'Real Estate Agent',
        address: '1850 Mt. Diablo Blvd, Walnut Creek, CA 94596',
        secondaryEmail: 'tombradley90@gmail.com', secondaryPhone: '',
        birthday: '1978-01-13', website: 'https://realtyhome.com/agents/tom',
        notes: 'Helping with property search in East Bay. Licensed since 2005.',
        labels: ['clabel_9'], isStarred: false, avatarColor: '#795548',
        createdAt: '2025-11-01T10:00:00Z', updatedAt: '2026-02-20T11:00:00Z', source: 'manual'
    },
    {
        id: 'contact_09', firstName: 'Ana', lastName: 'Gutierrez', email: 'ana.g@globalhealth.org',
        phone: '+1 (415) 555-0912', company: 'GlobalHealth.org', jobTitle: 'Community Outreach Director',
        address: '500 Sansome St, San Francisco, CA 94111',
        secondaryEmail: '', secondaryPhone: '+1 (415) 555-0913',
        birthday: '1987-08-02', website: '',
        notes: 'Volunteer coordinator. Spring health fair contact.',
        labels: ['clabel_2', 'clabel_5'], isStarred: false, avatarColor: '#E91E63',
        createdAt: '2024-06-20T15:00:00Z', updatedAt: '2026-02-21T12:15:00Z', source: 'manual'
    },
    {
        id: 'contact_10', firstName: 'Robert', lastName: 'Singh', email: 'robert.singh@university.edu',
        phone: '+1 (650) 555-1013', company: 'Stanford University', jobTitle: 'Professor of Computer Science',
        address: '353 Jane Stanford Way, Stanford, CA 94305',
        secondaryEmail: 'r.singh@cs.stanford.edu', secondaryPhone: '',
        birthday: '1975-05-11', website: 'https://cs.stanford.edu/~rsingh',
        notes: 'Guest lecture contact. Research focus: distributed systems.',
        labels: ['clabel_6'], isStarred: false, avatarColor: '#3F51B5',
        createdAt: '2022-10-05T13:00:00Z', updatedAt: '2026-02-18T11:00:00Z', source: 'manual'
    },
    {
        id: 'contact_11', firstName: 'Michelle', lastName: 'Park', email: 'michelle.park@mediaco.tv',
        phone: '+1 (213) 555-1114', company: 'MediaCo TV', jobTitle: 'Senior Producer',
        address: '4000 Warner Blvd, Burbank, CA 91522',
        secondaryEmail: 'michellepark@gmail.com', secondaryPhone: '',
        birthday: '1991-10-16', website: '',
        notes: 'Media contact for interviews and tech panels.',
        labels: ['clabel_3'], isStarred: false, avatarColor: '#FF9800',
        createdAt: '2025-01-20T09:00:00Z', updatedAt: '2026-02-20T08:20:00Z', source: 'manual'
    },
    {
        id: 'contact_12', firstName: 'Carlos', lastName: 'Mendez', email: 'carlos.m@logisticspro.net',
        phone: '+1 (305) 555-1215', company: 'LogisticsPro', jobTitle: 'Account Manager',
        address: '100 SE 2nd St, Miami, FL 33131',
        secondaryEmail: '', secondaryPhone: '+1 (305) 555-1216',
        birthday: '1983-02-28', website: '',
        notes: 'Primary shipping vendor. Reliable for express deliveries.',
        labels: ['clabel_9'], isStarred: false, avatarColor: '#607D8B',
        createdAt: '2023-08-10T11:00:00Z', updatedAt: '2026-02-19T10:30:00Z', source: 'manual'
    },
    {
        id: 'contact_13', firstName: 'Rachel', lastName: 'Foster', email: 'rachel.foster@nonprofitaid.org',
        phone: '+1 (503) 555-1316', company: 'NonprofitAid', jobTitle: 'Executive Director',
        address: '411 NW Park Ave, Portland, OR 97209',
        secondaryEmail: 'rachel.f.pdx@gmail.com', secondaryPhone: '',
        birthday: '1979-12-25', website: 'https://nonprofitaid.org',
        notes: 'Annual donation contact. Tax receipt handler.',
        labels: ['clabel_2'], isStarred: false, avatarColor: '#8BC34A',
        createdAt: '2021-12-01T10:00:00Z', updatedAt: '2026-02-17T09:00:00Z', source: 'manual'
    },
    {
        id: 'contact_14', firstName: 'Kevin', lastName: 'Zhao', email: 'kevin.zhao@quantumlab.tech',
        phone: '+1 (650) 555-1417', company: 'QuantumLab', jobTitle: 'Principal Research Scientist',
        address: '1 Hacker Way, Menlo Park, CA 94025',
        secondaryEmail: '', secondaryPhone: '',
        birthday: '1989-07-04', website: 'https://scholar.google.com/citations?user=kzhao',
        notes: 'Quantum computing researcher. Published 40+ papers.',
        labels: ['clabel_3', 'clabel_6'], isStarred: true, avatarColor: '#00BCD4',
        createdAt: '2020-04-15T16:00:00Z', updatedAt: '2026-02-22T17:45:00Z', source: 'manual'
    },
    {
        id: 'contact_15', firstName: 'Sophie', lastName: 'Laurent', email: 'sophie.l@eurodesign.fr',
        phone: '+33 1 42 68 5318', company: 'EuroDesign', jobTitle: 'Conference Director',
        address: '8 Rue de la Paix, 75002 Paris, France',
        secondaryEmail: 'sophie.laurent@gmail.com', secondaryPhone: '',
        birthday: '1986-11-03', website: 'https://eurodesign.fr',
        notes: 'EuroDesign Summit organizer. Invited me to speak in 2026.',
        labels: ['clabel_3', 'clabel_11'], isStarred: false, avatarColor: '#673AB7',
        createdAt: '2025-09-12T08:00:00Z', updatedAt: '2026-02-20T14:30:00Z', source: 'manual'
    },
    {
        id: 'contact_16', firstName: 'Nate', lastName: 'Patel', email: 'nate.patel@devops.tools',
        phone: '+1 (408) 555-1619', company: 'DevOps.tools', jobTitle: 'Infrastructure Lead',
        address: '345 Park Ave, San Jose, CA 95110',
        secondaryEmail: 'nate.p.dev@gmail.com', secondaryPhone: '',
        birthday: '1994-09-17', website: 'https://github.com/natepatel',
        notes: 'CI/CD migration collaborator. Jenkins to GitHub Actions.',
        labels: ['clabel_3'], isStarred: false, avatarColor: '#2196F3',
        createdAt: '2021-07-20T10:00:00Z', updatedAt: '2026-02-22T15:20:00Z', source: 'manual'
    },
    {
        id: 'contact_17', firstName: 'Hannah', lastName: 'Brooks', email: 'hannah.b@fitnessfirst.com',
        phone: '+1 (415) 555-1720', company: 'FitnessFirst', jobTitle: 'Personal Trainer',
        address: '2145 Market St, San Francisco, CA 94114',
        secondaryEmail: '', secondaryPhone: '',
        birthday: '1995-06-21', website: '',
        notes: 'Personal trainer since 2025. Specializes in HIIT and strength.',
        labels: ['clabel_5', 'clabel_12'], isStarred: false, avatarColor: '#F44336',
        createdAt: '2025-01-05T14:00:00Z', updatedAt: '2026-02-16T14:00:00Z', source: 'manual'
    },
    {
        id: 'contact_18', firstName: 'Omar', lastName: 'Al-Rashid', email: 'omar.ar@consulting.group',
        phone: '+1 (202) 555-1821', company: 'Consulting Group', jobTitle: 'Senior Strategy Consultant',
        address: '1001 Pennsylvania Ave NW, Washington, DC 20004',
        secondaryEmail: 'omar.alrashid@gmail.com', secondaryPhone: '+1 (202) 555-1822',
        birthday: '1981-04-12', website: '',
        notes: 'Strategy workshop facilitator. Based in DC, travels frequently.',
        labels: ['clabel_3'], isStarred: false, avatarColor: '#CDDC39',
        createdAt: '2024-01-10T09:00:00Z', updatedAt: '2026-02-17T07:30:00Z', source: 'manual'
    },
    {
        id: 'contact_19', firstName: 'Jennifer', lastName: 'Wu', email: 'jennifer.wu@biomedresearch.com',
        phone: '+1 (617) 555-1922', company: 'BioMed Research', jobTitle: 'Director of Research',
        address: '75 Francis St, Boston, MA 02115',
        secondaryEmail: '', secondaryPhone: '',
        birthday: '1984-08-29', website: 'https://biomedresearch.com/team/jwu',
        notes: 'Potential collaboration partner. Expertise in AI for healthcare.',
        labels: ['clabel_3'], isStarred: false, avatarColor: '#FF6F00',
        createdAt: '2025-12-01T15:00:00Z', updatedAt: '2026-02-18T15:00:00Z', source: 'manual'
    },
    {
        id: 'contact_20', firstName: 'Daniel', lastName: 'Thompson', email: 'daniel.t@architectsllp.com',
        phone: '+1 (415) 555-2023', company: 'Thompson Architects LLP', jobTitle: 'Principal Architect',
        address: '2200 Broadway, San Francisco, CA 94115',
        secondaryEmail: '', secondaryPhone: '',
        birthday: '1976-03-14', website: 'https://architectsllp.com',
        notes: 'Handling office renovation. Great attention to detail.',
        labels: ['clabel_9'], isStarred: false, avatarColor: '#455A64',
        createdAt: '2025-10-15T11:00:00Z', updatedAt: '2026-02-19T16:45:00Z', source: 'manual'
    },
    {
        id: 'contact_21', firstName: 'Maya', lastName: 'Patel', email: 'maya.patel@techcorp.io',
        phone: '+1 (650) 555-2124', company: 'TechCorp', jobTitle: 'Engineering Manager',
        address: '2100 Sand Hill Rd, Menlo Park, CA 94025',
        secondaryEmail: 'maya.p.sf@gmail.com', secondaryPhone: '',
        birthday: '1990-01-30', website: '',
        notes: 'Direct report at TechCorp. Manages backend team.',
        labels: ['clabel_3'], isStarred: true, avatarColor: '#7B1FA2',
        createdAt: '2020-01-10T08:30:00Z', updatedAt: '2026-02-22T10:30:00Z', source: 'manual'
    },
    {
        id: 'contact_22', firstName: 'Chris', lastName: 'Evans', email: 'chris.evans@sportsnews.com',
        phone: '+1 (925) 555-2225', company: 'SportsNews', jobTitle: 'Sports Editor',
        address: '1901 Harrison St, Oakland, CA 94612',
        secondaryEmail: 'chrisevans.sf@gmail.com', secondaryPhone: '',
        birthday: '1991-06-13', website: '',
        notes: 'Friend from college. Season ticket holder.',
        labels: ['clabel_2', 'clabel_6', 'clabel_5'], isStarred: false, avatarColor: '#1B5E20',
        createdAt: '2018-09-01T10:00:00Z', updatedAt: '2026-02-14T20:00:00Z', source: 'manual'
    },
    {
        id: 'contact_23', firstName: 'Aisha', lastName: 'Mohammed', email: 'aisha.m@edtech.academy',
        phone: '+1 (510) 555-2326', company: 'EdTech Academy', jobTitle: 'Head of Curriculum',
        address: '2025 Addison St, Berkeley, CA 94704',
        secondaryEmail: '', secondaryPhone: '',
        birthday: '1988-10-07', website: 'https://edtech.academy/team',
        notes: 'Enrolled in her Advanced ML course starting March 2026.',
        labels: ['clabel_3'], isStarred: false, avatarColor: '#BF360C',
        createdAt: '2025-02-10T16:00:00Z', updatedAt: '2026-02-15T16:30:00Z', source: 'manual'
    },
    {
        id: 'contact_24', firstName: 'Ryan', lastName: 'Cooper', email: 'ryan.cooper@saasplatform.io',
        phone: '+1 (206) 555-2427', company: 'SaaSPlatform', jobTitle: 'CTO',
        address: '400 Broad St, Seattle, WA 98109',
        secondaryEmail: 'rcooper.dev@gmail.com', secondaryPhone: '+1 (206) 555-2428',
        birthday: '1987-05-25', website: 'https://linkedin.com/in/ryancooper',
        notes: 'SaaS integration partner. Strong technical leader.',
        labels: ['clabel_3', 'clabel_4'], isStarred: false, avatarColor: '#0097A7',
        createdAt: '2021-11-08T14:00:00Z', updatedAt: '2026-02-21T09:45:00Z', source: 'manual'
    },
    // Family contacts
    {
        id: 'contact_25', firstName: 'Margaret', lastName: 'Johnson', email: 'margaret.johnson@gmail.com',
        phone: '+1 (916) 555-2500', company: '', jobTitle: 'Retired Teacher',
        address: '8725 Folsom Blvd, Sacramento, CA 95826',
        secondaryEmail: '', secondaryPhone: '+1 (916) 555-2501',
        birthday: '1958-12-20', website: '',
        notes: 'Mom. Prefers phone calls over email.',
        labels: ['clabel_1', 'clabel_10'], isStarred: true, avatarColor: '#C62828',
        createdAt: '2018-03-14T10:05:00Z', updatedAt: '2026-01-15T18:00:00Z', source: 'manual'
    },
    {
        id: 'contact_26', firstName: 'Richard', lastName: 'Johnson', email: 'rjohnson.sr@gmail.com',
        phone: '+1 (916) 555-2602', company: '', jobTitle: 'Retired Engineer',
        address: '8725 Folsom Blvd, Sacramento, CA 95826',
        secondaryEmail: '', secondaryPhone: '',
        birthday: '1956-08-04', website: '',
        notes: 'Dad. Interested in tech updates.',
        labels: ['clabel_1', 'clabel_10'], isStarred: true, avatarColor: '#1565C0',
        createdAt: '2018-03-14T10:06:00Z', updatedAt: '2025-12-25T10:00:00Z', source: 'manual'
    },
    {
        id: 'contact_27', firstName: 'Laura', lastName: 'Johnson-Martinez', email: 'laura.jm@gmail.com',
        phone: '+1 (503) 555-2703', company: 'Nike', jobTitle: 'Marketing Manager',
        address: '1 Bowerman Dr, Beaverton, OR 97005',
        secondaryEmail: 'laura.johnson@nike.com', secondaryPhone: '',
        birthday: '1992-04-11', website: '',
        notes: 'Sister. Lives in Portland with husband Miguel.',
        labels: ['clabel_1'], isStarred: true, avatarColor: '#AD1457',
        createdAt: '2018-03-14T10:07:00Z', updatedAt: '2026-02-10T20:00:00Z', source: 'manual'
    },
    {
        id: 'contact_28', firstName: 'Dr. Patricia', lastName: 'Nguyen', email: 'dr.nguyen@baymedical.org',
        phone: '+1 (415) 555-2804', company: 'Bay Medical Center', jobTitle: 'Primary Care Physician',
        address: '3801 Sacramento St, San Francisco, CA 94118',
        secondaryEmail: '', secondaryPhone: '+1 (415) 555-2805',
        birthday: '', website: 'https://baymedical.org/providers/nguyen',
        notes: 'Primary doctor since 2020. Annual checkup in April.',
        labels: ['clabel_12', 'clabel_10'], isStarred: false, avatarColor: '#00695C',
        createdAt: '2020-05-10T09:00:00Z', updatedAt: '2025-11-15T14:00:00Z', source: 'manual'
    },
    {
        id: 'contact_29', firstName: 'Mike', lastName: 'Chen', email: 'mike.chen.dds@gmail.com',
        phone: '+1 (415) 555-2905', company: 'Sunset Dental', jobTitle: 'Dentist',
        address: '1399 9th Ave, San Francisco, CA 94122',
        secondaryEmail: 'dr.chen@sunsetdental.com', secondaryPhone: '',
        birthday: '', website: '',
        notes: 'Dentist. Next cleaning scheduled for March 20.',
        labels: ['clabel_12'], isStarred: false, avatarColor: '#4E342E',
        createdAt: '2021-03-01T10:00:00Z', updatedAt: '2025-09-20T11:00:00Z', source: 'manual'
    },
    {
        id: 'contact_30', firstName: 'Jake', lastName: 'Morrison', email: 'jake.morrison@gmail.com',
        phone: '+1 (415) 555-3006', company: 'Stripe', jobTitle: 'Staff Engineer',
        address: '510 Townsend St, San Francisco, CA 94103',
        secondaryEmail: 'jmorrison@stripe.com', secondaryPhone: '',
        birthday: '1989-07-22', website: '',
        notes: 'Best friend from college. Weekly basketball games.',
        labels: ['clabel_2', 'clabel_5', 'clabel_6'], isStarred: true, avatarColor: '#1E88E5',
        createdAt: '2018-04-01T08:00:00Z', updatedAt: '2026-03-01T19:00:00Z', source: 'manual'
    },
    {
        id: 'contact_31', firstName: 'Samantha', lastName: 'Lee', email: 'samantha.lee@gmail.com',
        phone: '+1 (415) 555-3107', company: 'Airbnb', jobTitle: 'Product Designer',
        address: '888 Brannan St, San Francisco, CA 94103',
        secondaryEmail: 'sam.lee@airbnb.com', secondaryPhone: '',
        birthday: '1993-02-14', website: 'https://samlee.design',
        notes: 'Neighbor in building. Book club co-organizer.',
        labels: ['clabel_2', 'clabel_7', 'clabel_8'], isStarred: false, avatarColor: '#F06292',
        createdAt: '2023-05-01T16:00:00Z', updatedAt: '2026-02-28T10:00:00Z', source: 'manual'
    },
    {
        id: 'contact_32', firstName: 'Greg', lastName: 'Hoffman', email: 'greg.hoffman@wellsfargo.com',
        phone: '+1 (415) 555-3208', company: 'Wells Fargo', jobTitle: 'Financial Advisor',
        address: '420 Montgomery St, San Francisco, CA 94104',
        secondaryEmail: '', secondaryPhone: '',
        birthday: '', website: '',
        notes: 'Investment advisor. Quarterly portfolio review.',
        labels: ['clabel_9'], isStarred: false, avatarColor: '#5D4037',
        createdAt: '2022-01-15T10:00:00Z', updatedAt: '2025-12-20T15:00:00Z', source: 'manual'
    },
    {
        id: 'contact_33', firstName: 'Yuki', lastName: 'Tanaka', email: 'yuki.tanaka@gmail.com',
        phone: '+81 3-5555-3309', company: '', jobTitle: 'Freelance Translator',
        address: 'Shibuya, Tokyo, Japan',
        secondaryEmail: '', secondaryPhone: '',
        birthday: '1990-03-03', website: '',
        notes: 'Met during Tokyo trip 2024. Helped with conference translation.',
        labels: ['clabel_2', 'clabel_11'], isStarred: false, avatarColor: '#D81B60',
        createdAt: '2024-11-15T06:00:00Z', updatedAt: '2025-08-20T03:00:00Z', source: 'manual'
    },
    {
        id: 'contact_34', firstName: 'Ben', lastName: 'Walker', email: 'ben.walker@gmail.com',
        phone: '+1 (415) 555-3410', company: '', jobTitle: '',
        address: '1200 Folsom St, San Francisco, CA 94103',
        secondaryEmail: '', secondaryPhone: '',
        birthday: '1988-11-09', website: '',
        notes: 'Neighbor. Has our spare key for emergencies.',
        labels: ['clabel_7', 'clabel_10'], isStarred: false, avatarColor: '#546E7A',
        createdAt: '2023-08-01T12:00:00Z', updatedAt: '2025-06-15T18:00:00Z', source: 'manual'
    },
    {
        id: 'contact_35', firstName: 'Diana', lastName: 'Castillo', email: 'diana.castillo@gmail.com',
        phone: '+1 (415) 555-3511', company: 'Self-employed', jobTitle: 'Yoga Instructor',
        address: '3150 18th St, San Francisco, CA 94110',
        secondaryEmail: 'diana@zenflowstudio.com', secondaryPhone: '',
        birthday: '1996-01-18', website: 'https://zenflowstudio.com',
        notes: 'Tuesday and Thursday yoga classes. Great for stress relief.',
        labels: ['clabel_5', 'clabel_12'], isStarred: false, avatarColor: '#7CB342',
        createdAt: '2025-06-01T09:00:00Z', updatedAt: '2026-01-10T08:00:00Z', source: 'manual'
    },
    {
        id: 'contact_36', firstName: 'Raj', lastName: 'Kapoor', email: 'raj.kapoor@cloudnine.dev',
        phone: '+91 98765-43210', company: 'CloudNine', jobTitle: 'DevOps Engineer',
        address: 'Whitefield, Bangalore, India',
        secondaryEmail: 'raj.k.dev@gmail.com', secondaryPhone: '',
        birthday: '1995-08-15', website: '',
        notes: 'Works with Priya on the backend team. Timezone: IST.',
        labels: ['clabel_3'], isStarred: false, avatarColor: '#F9A825',
        createdAt: '2024-03-10T05:30:00Z', updatedAt: '2025-11-20T07:00:00Z', source: 'manual'
    },
    {
        id: 'contact_37', firstName: 'Elena', lastName: 'Volkov', email: 'elena.volkov@eurodesign.fr',
        phone: '+33 6 12 34 5678', company: 'EuroDesign', jobTitle: 'UX Research Lead',
        address: '15 Rue du Louvre, 75001 Paris, France',
        secondaryEmail: '', secondaryPhone: '',
        birthday: '1991-06-30', website: '',
        notes: 'Works with Sophie on the EuroDesign Summit. Panel moderator.',
        labels: ['clabel_3', 'clabel_11'], isStarred: false, avatarColor: '#AB47BC',
        createdAt: '2025-09-12T08:30:00Z', updatedAt: '2025-12-01T14:00:00Z', source: 'manual'
    },
    {
        id: 'contact_38', firstName: 'Tony', lastName: 'Russo', email: 'tony.russo@gmail.com',
        phone: '+1 (415) 555-3812', company: '', jobTitle: 'Retired Chef',
        address: '722 Columbus Ave, San Francisco, CA 94133',
        secondaryEmail: '', secondaryPhone: '',
        birthday: '1965-09-05', website: '',
        notes: 'Book club member. Makes amazing focaccia for meetings.',
        labels: ['clabel_7', 'clabel_8'], isStarred: false, avatarColor: '#D84315',
        createdAt: '2023-09-01T18:00:00Z', updatedAt: '2025-10-15T19:00:00Z', source: 'manual'
    },
    {
        id: 'contact_39', firstName: 'Patricia', lastName: 'Wong-Anderson', email: 'p.wong.anderson@techcorp.io',
        phone: '+1 (650) 555-3913', company: 'TechCorp', jobTitle: 'Head of People Operations',
        address: '2100 Sand Hill Rd, Menlo Park, CA 94025',
        secondaryEmail: '', secondaryPhone: '',
        birthday: '1982-07-08', website: '',
        notes: 'HR lead at TechCorp. Handles benefits and onboarding.',
        labels: ['clabel_3'], isStarred: false, avatarColor: '#6A1B9A',
        createdAt: '2020-02-01T09:00:00Z', updatedAt: '2025-08-30T11:00:00Z', source: 'manual'
    },
    {
        id: 'contact_40', firstName: 'Leo', lastName: 'Martinez', email: 'leo.martinez@gmail.com',
        phone: '+1 (503) 555-4014', company: 'Adidas', jobTitle: 'Supply Chain Analyst',
        address: '5055 N Greeley Ave, Portland, OR 97217',
        secondaryEmail: '', secondaryPhone: '',
        birthday: '1990-12-01', website: '',
        notes: "Laura's husband. Good with data analysis.",
        labels: ['clabel_1'], isStarred: false, avatarColor: '#00838F',
        createdAt: '2019-06-15T12:00:00Z', updatedAt: '2025-12-25T10:00:00Z', source: 'manual'
    }
];

// ---- Other Contacts (auto-saved from email interactions) ----
const OTHER_CONTACTS = [
    {
        id: 'other_01', firstName: '', lastName: '', email: 'support@vercel.com',
        name: 'Vercel Support', source: 'auto', savedAt: '2026-02-23T02:15:00Z',
        interactionCount: 8, lastInteraction: '2026-02-23T02:15:00Z'
    },
    {
        id: 'other_02', firstName: '', lastName: '', email: 'billing@aws.amazon.com',
        name: 'AWS Billing', source: 'auto', savedAt: '2026-02-22T03:00:00Z',
        interactionCount: 15, lastInteraction: '2026-02-22T03:00:00Z'
    },
    {
        id: 'other_03', firstName: '', lastName: '', email: 'hr@techcorp.io',
        name: 'TechCorp HR', source: 'auto', savedAt: '2026-01-15T10:00:00Z',
        interactionCount: 4, lastInteraction: '2026-01-15T10:00:00Z'
    },
    {
        id: 'other_04', firstName: 'Jason', lastName: 'Blake', email: 'jason.blake@salesforce.com',
        name: 'Jason Blake', source: 'auto', savedAt: '2026-02-10T14:00:00Z',
        interactionCount: 3, lastInteraction: '2026-02-10T14:00:00Z'
    },
    {
        id: 'other_05', firstName: '', lastName: '', email: 'no-reply@stripe.com',
        name: 'Stripe Notifications', source: 'auto', savedAt: '2026-02-22T16:00:00Z',
        interactionCount: 22, lastInteraction: '2026-02-22T16:00:00Z'
    },
    {
        id: 'other_06', firstName: 'Tina', lastName: 'Marshall', email: 'tina.marshall@designhub.com',
        name: 'Tina Marshall', source: 'auto', savedAt: '2025-12-05T09:00:00Z',
        interactionCount: 2, lastInteraction: '2025-12-05T09:00:00Z'
    },
    {
        id: 'other_07', firstName: '', lastName: '', email: 'noreply@github.com',
        name: 'GitHub', source: 'auto', savedAt: '2026-02-23T15:30:00Z',
        interactionCount: 45, lastInteraction: '2026-02-23T15:30:00Z'
    },
    {
        id: 'other_08', firstName: 'Alex', lastName: 'Rivera', email: 'alex.rivera@notion.so',
        name: 'Alex Rivera', source: 'auto', savedAt: '2026-01-20T11:00:00Z',
        interactionCount: 6, lastInteraction: '2026-01-20T11:00:00Z'
    },
    {
        id: 'other_09', firstName: '', lastName: '', email: 'receipts@uber.com',
        name: 'Uber Receipts', source: 'auto', savedAt: '2026-03-01T22:00:00Z',
        interactionCount: 31, lastInteraction: '2026-03-01T22:00:00Z'
    },
    {
        id: 'other_10', firstName: '', lastName: '', email: 'team@linear.app',
        name: 'Linear', source: 'auto', savedAt: '2025-11-10T08:00:00Z',
        interactionCount: 12, lastInteraction: '2025-11-10T08:00:00Z'
    },
    {
        id: 'other_11', firstName: 'Mike', lastName: 'Santos', email: 'mike.santos@cloudflare.com',
        name: 'Mike Santos', source: 'auto', savedAt: '2026-02-05T15:00:00Z',
        interactionCount: 5, lastInteraction: '2026-02-05T15:00:00Z'
    },
    {
        id: 'other_12', firstName: '', lastName: '', email: 'do-not-reply@zoom.us',
        name: 'Zoom', source: 'auto', savedAt: '2026-02-18T09:00:00Z',
        interactionCount: 19, lastInteraction: '2026-02-18T09:00:00Z'
    },
    {
        id: 'other_13', firstName: 'Wendy', lastName: 'Chung', email: 'wendy.chung@techcorp.io',
        name: 'Wendy Chung', source: 'auto', savedAt: '2025-10-22T13:00:00Z',
        interactionCount: 7, lastInteraction: '2025-10-22T13:00:00Z'
    },
    {
        id: 'other_14', firstName: '', lastName: '', email: 'alerts@datadog.com',
        name: 'Datadog Alerts', source: 'auto', savedAt: '2026-02-18T03:45:00Z',
        interactionCount: 28, lastInteraction: '2026-02-18T03:45:00Z'
    },
    {
        id: 'other_15', firstName: '', lastName: '', email: 'notifications@jira.atlassian.com',
        name: 'Jira Notifications', source: 'auto', savedAt: '2026-02-21T18:00:00Z',
        interactionCount: 55, lastInteraction: '2026-02-21T18:00:00Z'
    },
    {
        id: 'other_16', firstName: 'Chloe', lastName: 'Bennett', email: 'chloe.b@sequoiacap.com',
        name: 'Chloe Bennett', source: 'auto', savedAt: '2025-09-18T16:00:00Z',
        interactionCount: 1, lastInteraction: '2025-09-18T16:00:00Z'
    },
    {
        id: 'other_17', firstName: '', lastName: '', email: 'newsletter@hackernews.com',
        name: 'Hacker News Newsletter', source: 'auto', savedAt: '2026-02-22T06:00:00Z',
        interactionCount: 40, lastInteraction: '2026-02-22T06:00:00Z'
    },
    {
        id: 'other_18', firstName: 'Peter', lastName: 'Grant', email: 'peter.grant@mongodb.com',
        name: 'Peter Grant', source: 'auto', savedAt: '2025-08-12T10:00:00Z',
        interactionCount: 3, lastInteraction: '2025-08-12T10:00:00Z'
    },
    {
        id: 'other_19', firstName: '', lastName: '', email: 'no-reply@docusign.net',
        name: 'DocuSign', source: 'auto', savedAt: '2026-02-19T14:00:00Z',
        interactionCount: 9, lastInteraction: '2026-02-19T14:00:00Z'
    },
    {
        id: 'other_20', firstName: 'Nina', lastName: 'Kovalenko', email: 'nina.k@figma.com',
        name: 'Nina Kovalenko', source: 'auto', savedAt: '2025-07-30T11:00:00Z',
        interactionCount: 4, lastInteraction: '2025-07-30T11:00:00Z'
    }
];

// ---- Delegates ----
const DELEGATES = [
    {
        id: 'delegate_1', email: 'maya.patel@techcorp.io', name: 'Maya Patel',
        status: 'active', addedAt: '2025-06-15T10:00:00Z', activatedAt: '2025-06-16T08:30:00Z',
        permissions: { readEmail: true, sendEmail: true, deleteEmail: true, manageChat: false, changePassword: false }
    },
    {
        id: 'delegate_2', email: 'laura.jm@gmail.com', name: 'Laura Johnson-Martinez',
        status: 'active', addedAt: '2024-12-01T14:00:00Z', activatedAt: '2024-12-02T09:00:00Z',
        permissions: { readEmail: true, sendEmail: true, deleteEmail: true, manageChat: false, changePassword: false }
    },
    {
        id: 'delegate_3', email: 'priya.sharma@cloudnine.dev', name: 'Priya Sharma',
        status: 'pending', addedAt: '2026-03-05T11:00:00Z', activatedAt: null,
        permissions: { readEmail: true, sendEmail: true, deleteEmail: true, manageChat: false, changePassword: false }
    },
    {
        id: 'delegate_4', email: 'jake.morrison@gmail.com', name: 'Jake Morrison',
        status: 'expired', addedAt: '2026-02-20T09:00:00Z', activatedAt: null,
        permissions: { readEmail: true, sendEmail: true, deleteEmail: true, manageChat: false, changePassword: false }
    }
];

// ---- Linked Google Services (DMA) ----
const LINKED_SERVICES = [
    { id: 'svc_1', name: 'Google Search', icon: 'search', isLinked: true, category: 'core', description: 'Personalized search results and recommendations' },
    { id: 'svc_2', name: 'YouTube', icon: 'play_circle', isLinked: true, category: 'core', description: 'Video recommendations and watch history' },
    { id: 'svc_3', name: 'Google Ads', icon: 'campaign', isLinked: false, category: 'advertising', description: 'Personalized ad experiences across Google services' },
    { id: 'svc_4', name: 'Google Play', icon: 'shop', isLinked: true, category: 'core', description: 'App recommendations and purchase history' },
    { id: 'svc_5', name: 'Chrome', icon: 'language', isLinked: true, category: 'core', description: 'Browsing data sync and personalized suggestions' },
    { id: 'svc_6', name: 'Google Shopping', icon: 'shopping_cart', isLinked: false, category: 'commerce', description: 'Shopping recommendations and price tracking' },
    { id: 'svc_7', name: 'Google Maps', icon: 'map', isLinked: true, category: 'core', description: 'Location history and place recommendations' }
];

const ALWAYS_LINKED_SERVICES = [
    { id: 'asvc_1', name: 'Google Contacts', description: 'Contact sync across devices' },
    { id: 'asvc_2', name: 'Android Services', description: 'Core device functionality' },
    { id: 'asvc_3', name: 'Google Drive', description: 'File storage and sync' },
    { id: 'asvc_4', name: 'Gmail', description: 'Email service' },
    { id: 'asvc_5', name: 'Google Calendar', description: 'Calendar sync and scheduling' },
    { id: 'asvc_6', name: 'Google Photos', description: 'Photo backup and storage' },
    { id: 'asvc_7', name: 'Google Keep', description: 'Notes and lists' },
    { id: 'asvc_8', name: 'Google Meet', description: 'Video conferencing' },
    { id: 'asvc_9', name: 'Google Chat', description: 'Messaging service' },
    { id: 'asvc_10', name: 'Google Docs', description: 'Document editing' },
    { id: 'asvc_11', name: 'Google Sheets', description: 'Spreadsheet editing' },
    { id: 'asvc_12', name: 'Google Slides', description: 'Presentation editing' },
    { id: 'asvc_13', name: 'Google Translate', description: 'Translation service' },
    { id: 'asvc_14', name: 'Google Assistant', description: 'AI assistant' },
    { id: 'asvc_15', name: 'Google Fit', description: 'Health and fitness tracking' }
];

// ---- Account Settings ----
const ACCOUNT_SETTINGS = {
    autoSaveContacts: true,
    contactsSortBy: 'firstName',
    contactsDisplayOrder: 'firstLast',
    loginSettings: {
        rememberPassword: true,
        autoSignIn: true,
        twoFactorEnabled: true,
        twoFactorMethod: 'authenticator',
        recoveryEmailVerified: true,
        recoveryPhoneVerified: true
    },
    syncSettings: {
        googleSyncEnabled: false,
        googleSyncDeprecationAcknowledged: true,
        contactsSync: true,
        calendarSync: true,
        emailSync: true
    },
    collaborationSettings: {
        allowDelegates: true,
        maxDelegates: 10,
        shareDocsInEmail: true,
        showContactInfo: true
    },
    privacySettings: {
        showProfilePhoto: 'everyone',
        showEmail: 'contacts_only',
        showPhone: 'nobody',
        activityTracking: true
    },
    notificationSettings: {
        delegateActivity: true,
        contactChanges: false,
        securityAlerts: true,
        linkedServiceUpdates: true
    }
};

// ---- Contact Edit History (for "View contact edit history" feature) ----
const CONTACT_HISTORY = [
    { id: 'hist_1', contactId: 'contact_01', action: 'created', field: null, oldValue: null, newValue: null, timestamp: '2020-01-10T08:00:00Z', actor: 'alex.johnson@gmail.com' },
    { id: 'hist_2', contactId: 'contact_01', action: 'edited', field: 'jobTitle', oldValue: 'Product Manager', newValue: 'VP of Product', timestamp: '2024-03-15T10:00:00Z', actor: 'alex.johnson@gmail.com' },
    { id: 'hist_3', contactId: 'contact_01', action: 'edited', field: 'phone', oldValue: '+1 (650) 555-0100', newValue: '+1 (650) 555-0101', timestamp: '2025-06-20T14:00:00Z', actor: 'alex.johnson@gmail.com' },
    { id: 'hist_4', contactId: 'contact_01', action: 'label_added', field: 'labels', oldValue: null, newValue: 'VIP Clients', timestamp: '2025-09-01T09:00:00Z', actor: 'alex.johnson@gmail.com' },
    { id: 'hist_5', contactId: 'contact_02', action: 'created', field: null, oldValue: null, newValue: null, timestamp: '2019-06-15T12:00:00Z', actor: 'alex.johnson@gmail.com' },
    { id: 'hist_6', contactId: 'contact_02', action: 'edited', field: 'company', oldValue: 'Freelance', newValue: 'DesignHub', timestamp: '2021-01-10T11:00:00Z', actor: 'alex.johnson@gmail.com' },
    { id: 'hist_7', contactId: 'contact_05', action: 'created', field: null, oldValue: null, newValue: null, timestamp: '2020-09-05T11:00:00Z', actor: 'alex.johnson@gmail.com' },
    { id: 'hist_8', contactId: 'contact_05', action: 'edited', field: 'email', oldValue: 'priya.s@techcorp.io', newValue: 'priya.sharma@cloudnine.dev', timestamp: '2022-08-01T16:00:00Z', actor: 'alex.johnson@gmail.com' },
    { id: 'hist_9', contactId: 'contact_25', action: 'created', field: null, oldValue: null, newValue: null, timestamp: '2018-03-14T10:05:00Z', actor: 'alex.johnson@gmail.com' },
    { id: 'hist_10', contactId: 'contact_25', action: 'edited', field: 'address', oldValue: '123 Oak St, Sacramento, CA 95816', newValue: '8725 Folsom Blvd, Sacramento, CA 95826', timestamp: '2023-07-01T09:00:00Z', actor: 'alex.johnson@gmail.com' },
    { id: 'hist_11', contactId: 'contact_30', action: 'created', field: null, oldValue: null, newValue: null, timestamp: '2018-04-01T08:00:00Z', actor: 'alex.johnson@gmail.com' },
    { id: 'hist_12', contactId: 'contact_30', action: 'edited', field: 'company', oldValue: 'Google', newValue: 'Stripe', timestamp: '2023-03-15T10:00:00Z', actor: 'alex.johnson@gmail.com' },
    { id: 'hist_13', contactId: 'contact_14', action: 'edited', field: 'notes', oldValue: 'Quantum computing researcher.', newValue: 'Quantum computing researcher. Published 40+ papers.', timestamp: '2026-01-05T11:00:00Z', actor: 'alex.johnson@gmail.com' },
    { id: 'hist_14', contactId: 'contact_21', action: 'edited', field: 'jobTitle', oldValue: 'Senior Engineer', newValue: 'Engineering Manager', timestamp: '2025-04-01T09:00:00Z', actor: 'alex.johnson@gmail.com' },
    { id: 'hist_15', contactId: 'contact_03', action: 'label_added', field: 'labels', oldValue: null, newValue: 'VIP Clients', timestamp: '2024-11-15T14:00:00Z', actor: 'alex.johnson@gmail.com' }
];

// ---- Import/Export History ----
const IMPORT_EXPORT_HISTORY = [
    { id: 'ie_1', type: 'import', format: 'CSV', fileName: 'outlook_contacts.csv', count: 45, timestamp: '2020-01-10T08:00:00Z', status: 'completed' },
    { id: 'ie_2', type: 'export', format: 'Google CSV', fileName: 'gmail_contacts_backup.csv', count: 28, timestamp: '2025-06-15T14:00:00Z', status: 'completed' },
    { id: 'ie_3', type: 'import', format: 'vCard', fileName: 'iphone_contacts.vcf', count: 12, timestamp: '2024-08-20T10:00:00Z', status: 'completed' },
    { id: 'ie_4', type: 'export', format: 'vCard', fileName: 'all_contacts.vcf', count: 35, timestamp: '2026-01-05T09:00:00Z', status: 'completed' }
];

// ---- Merge Suggestions (duplicate contacts) ----
const MERGE_SUGGESTIONS = [
    {
        id: 'merge_1',
        contacts: ['contact_05', 'contact_36'],
        reason: 'Same company (CloudNine)',
        dismissed: false
    },
    {
        id: 'merge_2',
        contacts: ['contact_15', 'contact_37'],
        reason: 'Same company (EuroDesign)',
        dismissed: false
    }
];
