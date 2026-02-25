// ============================================================
// data.js — Rich, realistic seed data for Gmail Organize & Manage
// ============================================================
const SEED_DATA_VERSION = 1;

// ---- Current User ----
const CURRENT_USER = {
    id: 'user_1', name: 'Alex Johnson', email: 'alex.johnson@gmail.com', avatarColor: '#1a73e8'
};

// ---- Contacts ----
const CONTACTS = [
    { id: 'contact_01', name: 'Sarah Chen', email: 'sarah.chen@techcorp.io', avatarColor: '#EA4335', isFrequent: true },
    { id: 'contact_02', name: 'Marcus Williams', email: 'marcus.w@designhub.com', avatarColor: '#34A853', isFrequent: true },
    { id: 'contact_03', name: 'Emily Rodriguez', email: 'emily.r@startupventures.co', avatarColor: '#FBBC04', isFrequent: true },
    { id: 'contact_04', name: 'James O\'Brien', email: 'james.obrien@lawfirm.legal', avatarColor: '#4285F4', isFrequent: false },
    { id: 'contact_05', name: 'Priya Sharma', email: 'priya.sharma@cloudnine.dev', avatarColor: '#9C27B0', isFrequent: true },
    { id: 'contact_06', name: 'David Kim', email: 'david.kim@financeplus.com', avatarColor: '#FF5722', isFrequent: true },
    { id: 'contact_07', name: 'Lisa Nakamura', email: 'lisa.n@creativeagency.co', avatarColor: '#009688', isFrequent: false },
    { id: 'contact_08', name: 'Tom Bradley', email: 'tom.bradley@realtyhome.com', avatarColor: '#795548', isFrequent: false },
    { id: 'contact_09', name: 'Ana Gutierrez', email: 'ana.g@globalhealth.org', avatarColor: '#E91E63', isFrequent: true },
    { id: 'contact_10', name: 'Robert Singh', email: 'robert.singh@university.edu', avatarColor: '#3F51B5', isFrequent: false },
    { id: 'contact_11', name: 'Michelle Park', email: 'michelle.park@mediaco.tv', avatarColor: '#FF9800', isFrequent: true },
    { id: 'contact_12', name: 'Carlos Mendez', email: 'carlos.m@logisticspro.net', avatarColor: '#607D8B', isFrequent: false },
    { id: 'contact_13', name: 'Rachel Foster', email: 'rachel.foster@nonprofitaid.org', avatarColor: '#8BC34A', isFrequent: false },
    { id: 'contact_14', name: 'Kevin Zhao', email: 'kevin.zhao@quantumlab.tech', avatarColor: '#00BCD4', isFrequent: true },
    { id: 'contact_15', name: 'Sophie Laurent', email: 'sophie.l@eurodesign.fr', avatarColor: '#673AB7', isFrequent: false },
    { id: 'contact_16', name: 'Nate Patel', email: 'nate.patel@devops.tools', avatarColor: '#2196F3', isFrequent: true },
    { id: 'contact_17', name: 'Hannah Brooks', email: 'hannah.b@fitnessfirst.com', avatarColor: '#F44336', isFrequent: false },
    { id: 'contact_18', name: 'Omar Al-Rashid', email: 'omar.ar@consulting.group', avatarColor: '#CDDC39', isFrequent: false },
    { id: 'contact_19', name: 'Jennifer Wu', email: 'jennifer.wu@biomedresearch.com', avatarColor: '#FF6F00', isFrequent: true },
    { id: 'contact_20', name: 'Daniel Thompson', email: 'daniel.t@architectsllp.com', avatarColor: '#455A64', isFrequent: false },
    { id: 'contact_21', name: 'Maya Patel', email: 'maya.patel@techcorp.io', avatarColor: '#7B1FA2', isFrequent: true },
    { id: 'contact_22', name: 'Chris Evans', email: 'chris.evans@sportsnews.com', avatarColor: '#1B5E20', isFrequent: false },
    { id: 'contact_23', name: 'Aisha Mohammed', email: 'aisha.m@edtech.academy', avatarColor: '#BF360C', isFrequent: false },
    { id: 'contact_24', name: 'Ryan Cooper', email: 'ryan.cooper@saasplatform.io', avatarColor: '#0097A7', isFrequent: true },
];

// ---- Labels ----
const LABELS = [
    // System labels
    { id: 'INBOX', name: 'Inbox', type: 'system', color: null, visible: true, parentId: null, messageCount: 0, unreadCount: 0 },
    { id: 'STARRED', name: 'Starred', type: 'system', color: null, visible: true, parentId: null, messageCount: 0, unreadCount: 0 },
    { id: 'SNOOZED', name: 'Snoozed', type: 'system', color: null, visible: true, parentId: null, messageCount: 0, unreadCount: 0 },
    { id: 'SENT', name: 'Sent', type: 'system', color: null, visible: true, parentId: null, messageCount: 0, unreadCount: 0 },
    { id: 'DRAFT', name: 'Drafts', type: 'system', color: null, visible: true, parentId: null, messageCount: 0, unreadCount: 0 },
    { id: 'IMPORTANT', name: 'Important', type: 'system', color: null, visible: true, parentId: null, messageCount: 0, unreadCount: 0 },
    { id: 'ALL_MAIL', name: 'All Mail', type: 'system', color: null, visible: true, parentId: null, messageCount: 0, unreadCount: 0 },
    { id: 'SPAM', name: 'Spam', type: 'system', color: null, visible: true, parentId: null, messageCount: 0, unreadCount: 0 },
    { id: 'TRASH', name: 'Trash', type: 'system', color: null, visible: true, parentId: null, messageCount: 0, unreadCount: 0 },
    { id: 'CATEGORY_PRIMARY', name: 'Primary', type: 'system', color: null, visible: false, parentId: null, messageCount: 0, unreadCount: 0 },
    { id: 'CATEGORY_SOCIAL', name: 'Social', type: 'system', color: null, visible: false, parentId: null, messageCount: 0, unreadCount: 0 },
    { id: 'CATEGORY_PROMOTIONS', name: 'Promotions', type: 'system', color: null, visible: false, parentId: null, messageCount: 0, unreadCount: 0 },
    { id: 'CATEGORY_UPDATES', name: 'Updates', type: 'system', color: null, visible: false, parentId: null, messageCount: 0, unreadCount: 0 },
    { id: 'CATEGORY_FORUMS', name: 'Forums', type: 'system', color: null, visible: false, parentId: null, messageCount: 0, unreadCount: 0 },

    // User labels — top-level
    { id: 'label_1', name: 'Work', type: 'user', color: { background: '#2962ff', text: '#fff' }, visible: true, parentId: null, messageCount: 0, unreadCount: 0 },
    { id: 'label_2', name: 'Personal', type: 'user', color: { background: '#2a8547', text: '#fff' }, visible: true, parentId: null, messageCount: 0, unreadCount: 0 },
    { id: 'label_3', name: 'Finance', type: 'user', color: { background: '#e37400', text: '#fff' }, visible: true, parentId: null, messageCount: 0, unreadCount: 0 },
    { id: 'label_4', name: 'Travel', type: 'user', color: { background: '#13828b', text: '#fff' }, visible: true, parentId: null, messageCount: 0, unreadCount: 0 },
    { id: 'label_5', name: 'Receipts', type: 'user', color: { background: '#d5ae49', text: '#000' }, visible: true, parentId: null, messageCount: 0, unreadCount: 0 },
    { id: 'label_6', name: 'Newsletters', type: 'user', color: { background: '#7e57c2', text: '#fff' }, visible: true, parentId: null, messageCount: 0, unreadCount: 0 },
    { id: 'label_7', name: 'Health', type: 'user', color: { background: '#cc3333', text: '#fff' }, visible: true, parentId: null, messageCount: 0, unreadCount: 0 },
    { id: 'label_8', name: 'Education', type: 'user', color: { background: '#bbdefb', text: '#1565c0' }, visible: true, parentId: null, messageCount: 0, unreadCount: 0 },

    // User labels — nested under Work
    { id: 'label_9', name: 'Projects', type: 'user', color: { background: '#bbdefb', text: '#1565c0' }, visible: true, parentId: 'label_1', messageCount: 0, unreadCount: 0 },
    { id: 'label_10', name: 'Meetings', type: 'user', color: { background: '#c8e6c9', text: '#2e7d32' }, visible: true, parentId: 'label_1', messageCount: 0, unreadCount: 0 },
    { id: 'label_11', name: 'Clients', type: 'user', color: { background: '#ffe0b2', text: '#e65100' }, visible: true, parentId: 'label_1', messageCount: 0, unreadCount: 0 },
    { id: 'label_12', name: 'HR', type: 'user', color: { background: '#e1bee7', text: '#7b1fa2' }, visible: true, parentId: 'label_1', messageCount: 0, unreadCount: 0 },

    // User labels — nested under Personal
    { id: 'label_13', name: 'Family', type: 'user', color: { background: '#fce4ec', text: '#880e4f' }, visible: true, parentId: 'label_2', messageCount: 0, unreadCount: 0 },
    { id: 'label_14', name: 'Friends', type: 'user', color: { background: '#b2dfdb', text: '#00695c' }, visible: true, parentId: 'label_2', messageCount: 0, unreadCount: 0 },

    // User labels — nested under Finance
    { id: 'label_15', name: 'Invoices', type: 'user', color: { background: '#fff9c4', text: '#f57f17' }, visible: true, parentId: 'label_3', messageCount: 0, unreadCount: 0 },
    { id: 'label_16', name: 'Banking', type: 'user', color: { background: '#ffcdd2', text: '#c62828' }, visible: true, parentId: 'label_3', messageCount: 0, unreadCount: 0 },

    // More top-level
    { id: 'label_17', name: 'Action Required', type: 'user', color: { background: '#b3005e', text: '#fff' }, visible: true, parentId: null, messageCount: 0, unreadCount: 0 },
    { id: 'label_18', name: 'Waiting For Reply', type: 'user', color: { background: '#666', text: '#fff' }, visible: true, parentId: null, messageCount: 0, unreadCount: 0 },
    { id: 'label_19', name: 'Reference', type: 'user', color: { background: '#e0e0e0', text: '#424242' }, visible: true, parentId: null, messageCount: 0, unreadCount: 0 },
];

// Helper: create email
const _u = CURRENT_USER;
const _to = [{ name: _u.name, email: _u.email }];
function _e(id, threadId, from, subject, snippet, date, opts = {}) {
    return {
        id, threadId: 'thread_' + threadId,
        from, to: opts.to || _to, cc: opts.cc || [], bcc: [],
        subject, snippet, body: opts.body || snippet,
        date,
        isRead: opts.isRead !== undefined ? opts.isRead : true,
        isStarred: opts.isStarred || false,
        starType: opts.starType || null,
        isImportant: opts.isImportant || false,
        labels: opts.labels || ['INBOX', 'CATEGORY_PRIMARY'],
        category: opts.category || 'primary',
        hasAttachments: opts.hasAttachments || false,
        attachments: opts.attachments || [],
        isSnoozed: opts.isSnoozed || false,
        snoozeUntil: opts.snoozeUntil || null,
        isTrashed: opts.isTrashed || false,
        isSpam: opts.isSpam || false,
        isArchived: opts.isArchived || false,
        isDraft: opts.isDraft || false,
        isSent: opts.isSent || false,
        isMuted: opts.isMuted || false,
    };
}

const EMAILS = [
    // ---- Primary: Work emails ----
    _e(1, 1, {name:'Sarah Chen',email:'sarah.chen@techcorp.io'}, 'Q1 Product Roadmap Review', 'Hi Alex, I\'ve attached the updated Q1 product roadmap for your review. Please take a look before our meeting on Thursday.', '2026-02-24T09:15:00Z', {isRead:false, isImportant:true, hasAttachments:true, attachments:[{name:'Q1_Roadmap_v3.pdf',size:'2.4 MB'}], labels:['INBOX','CATEGORY_PRIMARY','label_1','label_9']}),
    _e(2, 2, {name:'Priya Sharma',email:'priya.sharma@cloudnine.dev'}, 'Re: API Integration Issue', 'I found the root cause. The timeout was set to 30s but the new endpoint needs at least 45s. I\'ll push a fix today.', '2026-02-24T08:42:00Z', {isRead:false, isImportant:true, labels:['INBOX','CATEGORY_PRIMARY','label_1','label_9']}),
    _e(3, 2, {name:'Alex Johnson',email:'alex.johnson@gmail.com'}, 'Re: API Integration Issue', 'Thanks Priya, that makes sense. Can you also add retry logic while you\'re at it?', '2026-02-24T07:30:00Z', {isRead:true, isSent:true, labels:['SENT','CATEGORY_PRIMARY','label_1']}),
    _e(4, 2, {name:'Priya Sharma',email:'priya.sharma@cloudnine.dev'}, 'API Integration Issue', 'Hey Alex, we\'re seeing intermittent failures on the payment gateway API. Getting 504 errors about 15% of the time.', '2026-02-23T16:20:00Z', {isRead:true, isStarred:true, starType:'yellow-star', labels:['INBOX','CATEGORY_PRIMARY','label_1','label_9']}),
    _e(5, 3, {name:'David Kim',email:'david.kim@financeplus.com'}, 'Monthly Financial Report - January 2026', 'Please find attached the January financial summary. Revenue was up 12% MoM, with notable growth in enterprise segment.', '2026-02-23T14:00:00Z', {isRead:true, isImportant:true, hasAttachments:true, attachments:[{name:'Jan2026_Financial_Report.xlsx',size:'1.8 MB'},{name:'Revenue_Breakdown.pdf',size:'890 KB'}], labels:['INBOX','CATEGORY_PRIMARY','label_3','label_15']}),
    _e(6, 4, {name:'Marcus Williams',email:'marcus.w@designhub.com'}, 'Design System Update v4.2', 'The new component library is ready for review. Key changes: updated color tokens, new navigation patterns, and improved responsive breakpoints.', '2026-02-23T11:30:00Z', {isRead:false, hasAttachments:true, attachments:[{name:'DesignSystem_v4.2.fig',size:'15.3 MB'}], labels:['INBOX','CATEGORY_PRIMARY','label_1']}),
    _e(7, 5, {name:'Emily Rodriguez',email:'emily.r@startupventures.co'}, 'Partnership Opportunity - Series B Company', 'Alex, I\'d like to introduce you to a Series B company in the AI space. They\'re looking for integration partners and I think there\'s a great fit.', '2026-02-23T09:00:00Z', {isRead:true, isStarred:true, starType:'yellow-star', isImportant:true, labels:['INBOX','CATEGORY_PRIMARY','label_1','label_11','label_17']}),
    _e(8, 6, {name:'Kevin Zhao',email:'kevin.zhao@quantumlab.tech'}, 'Research Paper: Quantum Error Correction', 'Our team just published a new paper on quantum error correction codes. Thought you might find it interesting given our conversation last week.', '2026-02-22T17:45:00Z', {isRead:true, hasAttachments:true, attachments:[{name:'QEC_Paper_2026.pdf',size:'3.1 MB'}], labels:['INBOX','CATEGORY_PRIMARY','label_8','label_19']}),
    _e(9, 7, {name:'Nate Patel',email:'nate.patel@devops.tools'}, 'CI/CD Pipeline Migration Plan', 'Here\'s the migration plan for moving our CI/CD from Jenkins to GitHub Actions. Estimated 3 weeks for full cutover.', '2026-02-22T15:20:00Z', {isRead:false, isImportant:true, hasAttachments:true, attachments:[{name:'Migration_Plan.pdf',size:'1.2 MB'}], labels:['INBOX','CATEGORY_PRIMARY','label_1','label_9','label_17']}),
    _e(10, 8, {name:'Maya Patel',email:'maya.patel@techcorp.io'}, 'Team Standup Notes - Feb 22', 'Quick summary from today\'s standup: Backend team finishing auth refactor, Frontend starting dashboard redesign, QA blocked on staging env.', '2026-02-22T10:30:00Z', {isRead:true, labels:['INBOX','CATEGORY_PRIMARY','label_1','label_10']}),
    _e(11, 9, {name:'James O\'Brien',email:'james.obrien@lawfirm.legal'}, 'Contract Review: Vendor Agreement', 'Alex, I\'ve reviewed the vendor agreement. A few clauses need attention - see my redlined version attached. Let\'s discuss by end of week.', '2026-02-21T16:00:00Z', {isRead:true, isStarred:true, starType:'red-star', isImportant:true, hasAttachments:true, attachments:[{name:'Vendor_Agreement_Redlined.docx',size:'456 KB'}], labels:['INBOX','CATEGORY_PRIMARY','label_1','label_11','label_17']}),
    _e(12, 10, {name:'Ana Gutierrez',email:'ana.g@globalhealth.org'}, 'Volunteer Event: Spring Health Fair', 'We\'re organizing a spring health fair on March 15th. Would you be interested in volunteering? We need help with registration and logistics.', '2026-02-21T12:15:00Z', {isRead:true, labels:['INBOX','CATEGORY_PRIMARY','label_2']}),
    _e(13, 11, {name:'Ryan Cooper',email:'ryan.cooper@saasplatform.io'}, 'Re: Platform Performance Issues', 'Good news - we identified the bottleneck. It was a missing database index on the analytics table. Response times are back to normal.', '2026-02-21T09:45:00Z', {isRead:true, labels:['INBOX','CATEGORY_PRIMARY','label_1','label_9']}),
    _e(14, 12, {name:'Sophie Laurent',email:'sophie.l@eurodesign.fr'}, 'Bonjour! Conference Speaker Invitation', 'We\'d love to have you speak at EuroDesign Summit 2026 in Paris. The theme is "AI-Driven Design Systems." Travel and accommodation covered.', '2026-02-20T14:30:00Z', {isRead:false, isStarred:true, starType:'blue-star', isImportant:true, labels:['INBOX','CATEGORY_PRIMARY','label_4','label_17']}),
    _e(15, 13, {name:'Tom Bradley',email:'tom.bradley@realtyhome.com'}, 'Property Listing: 45 Oak Avenue', 'New listing matching your criteria - 3BR/2BA, 1,800 sqft, updated kitchen, large backyard. Open house this Saturday 1-4pm.', '2026-02-20T11:00:00Z', {isRead:true, labels:['INBOX','CATEGORY_PRIMARY','label_2']}),
    _e(16, 14, {name:'Michelle Park',email:'michelle.park@mediaco.tv'}, 'Interview Request: Tech Innovation Panel', 'Hi Alex, we\'re producing a segment on tech innovation in 2026. Would you be available for a 15-minute interview next week?', '2026-02-20T08:20:00Z', {isRead:true, labels:['INBOX','CATEGORY_PRIMARY','label_18']}),
    _e(17, 15, {name:'Daniel Thompson',email:'daniel.t@architectsllp.com'}, 'Office Renovation Plans', 'Attached are the revised floor plans for the office renovation. The open workspace area has been expanded per your feedback.', '2026-02-19T16:45:00Z', {isRead:true, hasAttachments:true, attachments:[{name:'Office_FloorPlan_v2.pdf',size:'5.6 MB'}], labels:['INBOX','CATEGORY_PRIMARY','label_1']}),
    _e(18, 16, {name:'Sarah Chen',email:'sarah.chen@techcorp.io'}, 'Quarterly Team Dinner', 'Hey everyone! Let\'s plan our Q1 team dinner. I\'m thinking March 7th at Zafferano. Please reply with your availability.', '2026-02-19T13:00:00Z', {isRead:true, labels:['INBOX','CATEGORY_PRIMARY','label_1','label_10'], cc:[{name:'Maya Patel',email:'maya.patel@techcorp.io'},{name:'Priya Sharma',email:'priya.sharma@cloudnine.dev'}]}),
    _e(19, 17, {name:'Carlos Mendez',email:'carlos.m@logisticspro.net'}, 'Shipping Update: Order #LP-2026-8834', 'Your order has been shipped via FedEx Express. Tracking: FX9283746510. Estimated delivery: Feb 21.', '2026-02-19T10:30:00Z', {isRead:true, category:'updates', labels:['INBOX','CATEGORY_UPDATES','label_5']}),
    _e(20, 18, {name:'Jennifer Wu',email:'jennifer.wu@biomedresearch.com'}, 'Re: Collaboration Proposal', 'Alex, this sounds promising. Let\'s set up a call with our research team. How does Thursday at 2pm PST work for you?', '2026-02-18T15:00:00Z', {isRead:false, isImportant:true, labels:['INBOX','CATEGORY_PRIMARY','label_1','label_18']}),

    // ---- More Primary emails (older) ----
    _e(21, 19, {name:'Robert Singh',email:'robert.singh@university.edu'}, 'Guest Lecture Invitation - CS 401', 'The department would be honored if you could give a guest lecture on distributed systems. We have an opening on March 20th.', '2026-02-18T11:00:00Z', {isRead:true, labels:['INBOX','CATEGORY_PRIMARY','label_8']}),
    _e(22, 20, {name:'Rachel Foster',email:'rachel.foster@nonprofitaid.org'}, 'Donation Receipt - Tax Year 2025', 'Thank you for your generous contribution of $500 to NonprofitAid. Attached is your tax receipt for the 2025 fiscal year.', '2026-02-17T09:00:00Z', {isRead:true, hasAttachments:true, attachments:[{name:'Donation_Receipt_2025.pdf',size:'120 KB'}], labels:['INBOX','CATEGORY_PRIMARY','label_3','label_5']}),
    _e(23, 21, {name:'Omar Al-Rashid',email:'omar.ar@consulting.group'}, 'Strategy Workshop Follow-up', 'Great workshop yesterday. Attached are the whiteboard photos and action items. Please review your assigned items by Friday.', '2026-02-17T07:30:00Z', {isRead:true, hasAttachments:true, attachments:[{name:'Workshop_Notes.pdf',size:'2.1 MB'},{name:'Action_Items.xlsx',size:'45 KB'}], labels:['INBOX','CATEGORY_PRIMARY','label_1','label_10']}),
    _e(24, 22, {name:'Hannah Brooks',email:'hannah.b@fitnessfirst.com'}, 'Your Workout Plan for March', 'Hi Alex! I\'ve customized your workout plan for March based on your progress. Let me know if you want any adjustments.', '2026-02-16T14:00:00Z', {isRead:true, hasAttachments:true, attachments:[{name:'March_Workout_Plan.pdf',size:'340 KB'}], labels:['INBOX','CATEGORY_PRIMARY','label_7','label_2']}),
    _e(25, 23, {name:'Aisha Mohammed',email:'aisha.m@edtech.academy'}, 'Course Enrollment Confirmation', 'You\'re enrolled in "Advanced Machine Learning" starting March 3rd. Your first module materials are attached.', '2026-02-15T16:30:00Z', {isRead:true, hasAttachments:true, attachments:[{name:'ML_Module1.pdf',size:'4.2 MB'}], category:'updates', labels:['INBOX','CATEGORY_UPDATES','label_8']}),
    _e(26, 24, {name:'Lisa Nakamura',email:'lisa.n@creativeagency.co'}, 'Brand Refresh Concepts', 'Here are three brand refresh concepts for review. Each explores a different direction. Let me know your thoughts.', '2026-02-15T11:00:00Z', {isRead:false, isStarred:true, starType:'yellow-star', hasAttachments:true, attachments:[{name:'Brand_Concepts.pdf',size:'8.7 MB'}], labels:['INBOX','CATEGORY_PRIMARY','label_1','label_11']}),
    _e(27, 25, {name:'Chris Evans',email:'chris.evans@sportsnews.com'}, 'Sunday Game Tickets Available', 'Hey Alex, my friend can\'t make it to the game this Sunday. Want his ticket? Section 108, Row 12. Face value $85.', '2026-02-14T20:00:00Z', {isRead:true, labels:['INBOX','CATEGORY_PRIMARY','label_2','label_14']}),
    _e(28, 26, {name:'David Kim',email:'david.kim@financeplus.com'}, 'Tax Season Reminder: Documents Needed', 'Friendly reminder: we need your W-2 and 1099 forms by March 1st to prepare your 2025 tax return on time.', '2026-02-14T10:00:00Z', {isRead:true, isImportant:true, labels:['INBOX','CATEGORY_PRIMARY','label_3','label_17']}),
    _e(29, 27, {name:'Priya Sharma',email:'priya.sharma@cloudnine.dev'}, 'Sprint Retro Action Items', 'From our retro: 1) Improve code review turnaround, 2) Set up automated E2E tests, 3) Reduce meeting overhead. Owners assigned.', '2026-02-13T17:00:00Z', {isRead:true, labels:['INBOX','CATEGORY_PRIMARY','label_1','label_9']}),
    _e(30, 28, {name:'Emily Rodriguez',email:'emily.r@startupventures.co'}, 'VC Meetup Next Thursday', 'There\'s a VC networking event at The Grand Hotel on Feb 20th, 6-9pm. Great opportunity to meet Series A/B investors. Want to go?', '2026-02-13T09:30:00Z', {isRead:true, labels:['INBOX','CATEGORY_PRIMARY','label_2']}),

    // ---- Social category ----
    _e(31, 31, {name:'LinkedIn',email:'notifications@linkedin.com'}, 'Sarah Chen endorsed you for Cloud Architecture', 'Sarah Chen has endorsed you for Cloud Architecture. You now have 47 endorsements for this skill.', '2026-02-24T07:00:00Z', {isRead:false, category:'social', labels:['INBOX','CATEGORY_SOCIAL']}),
    _e(32, 32, {name:'Twitter',email:'notify@twitter.com'}, 'Your tweet got 250 likes', 'Your tweet about microservices architecture is trending. 250 likes, 89 retweets, 34 replies.', '2026-02-23T19:00:00Z', {isRead:true, category:'social', labels:['INBOX','CATEGORY_SOCIAL']}),
    _e(33, 33, {name:'GitHub',email:'notifications@github.com'}, '[techcorp/api-gateway] PR #847 merged', 'Pull request "feat: add rate limiting middleware" has been merged into main by priya-sharma.', '2026-02-23T15:30:00Z', {isRead:false, category:'social', labels:['INBOX','CATEGORY_SOCIAL','label_1']}),
    _e(34, 34, {name:'Slack',email:'feedback@slack.com'}, 'Weekly Activity Summary', 'You sent 142 messages last week across 8 channels. Your most active channel was #engineering.', '2026-02-23T06:00:00Z', {isRead:true, category:'social', labels:['INBOX','CATEGORY_SOCIAL']}),
    _e(35, 35, {name:'Facebook',email:'notification@facebookmail.com'}, 'Marcus Williams posted in Bay Area Tech', 'Marcus shared: "Excited to announce our new design system is now open source! Check it out at..."', '2026-02-22T20:00:00Z', {isRead:true, category:'social', labels:['INBOX','CATEGORY_SOCIAL']}),
    _e(36, 36, {name:'LinkedIn',email:'notifications@linkedin.com'}, '15 people viewed your profile this week', 'Your profile views are up 30% from last week. Top viewers are from companies like Google, Microsoft, and Stripe.', '2026-02-22T08:00:00Z', {isRead:true, category:'social', labels:['INBOX','CATEGORY_SOCIAL']}),
    _e(37, 37, {name:'GitHub',email:'notifications@github.com'}, '[cloudnine/auth-service] Issue #312 assigned to you', 'Issue "Implement OAuth2 PKCE flow" has been assigned to you by nate-patel.', '2026-02-21T14:20:00Z', {isRead:false, category:'social', labels:['INBOX','CATEGORY_SOCIAL','label_1']}),
    _e(38, 38, {name:'Instagram',email:'no-reply@mail.instagram.com'}, 'You have new followers', '5 new people followed you this week, including @techconference2026 and @designweekly.', '2026-02-21T07:00:00Z', {isRead:true, category:'social', labels:['INBOX','CATEGORY_SOCIAL']}),
    _e(39, 39, {name:'Meetup',email:'info@meetup.com'}, 'New event: Bay Area JavaScript Meetup', 'Monthly JS meetup on Feb 27th at Google SF. Topic: "Server Components in Production." RSVP now.', '2026-02-20T16:00:00Z', {isRead:true, category:'social', labels:['INBOX','CATEGORY_SOCIAL','label_8']}),
    _e(40, 40, {name:'Reddit',email:'noreply@reddit.com'}, 'Trending in r/programming', 'Your comment on "Why Rust is eating the world" received 500+ upvotes.', '2026-02-20T12:00:00Z', {isRead:true, category:'social', labels:['INBOX','CATEGORY_SOCIAL']}),
    _e(41, 41, {name:'Discord',email:'noreply@discord.com'}, 'New messages in Tech Community', 'You have 23 unread messages in #general and 8 in #help-wanted.', '2026-02-19T21:00:00Z', {isRead:true, category:'social', labels:['INBOX','CATEGORY_SOCIAL']}),
    _e(42, 42, {name:'LinkedIn',email:'notifications@linkedin.com'}, 'Kevin Zhao shared a post', 'Kevin shared: "Our quantum error correction paper just hit 1000 citations! Humbled by the response from the research community."', '2026-02-18T10:00:00Z', {isRead:true, category:'social', labels:['INBOX','CATEGORY_SOCIAL']}),
    _e(43, 43, {name:'GitHub',email:'notifications@github.com'}, 'Dependabot: 3 security advisories', 'New security advisories for lodash (high), express (medium), and jsonwebtoken (critical).', '2026-02-17T09:00:00Z', {isRead:false, isImportant:true, category:'social', labels:['INBOX','CATEGORY_SOCIAL','label_1','label_17']}),

    // ---- Promotions category ----
    _e(44, 44, {name:'Amazon',email:'store-news@amazon.com'}, 'Your recommendations: Tech deals of the week', 'Based on your browsing: Sony WH-1000XM6 at $299 (20% off), MacBook Pro sleeve at $39, USB-C hub bundle at $45.', '2026-02-24T06:00:00Z', {isRead:false, category:'promotions', labels:['INBOX','CATEGORY_PROMOTIONS']}),
    _e(45, 45, {name:'Coursera',email:'no-reply@coursera.org'}, 'Last chance: 40% off Professional Certificates', 'Upgrade your skills with Google, Meta, and IBM professional certificates. Sale ends February 28th.', '2026-02-23T10:00:00Z', {isRead:true, category:'promotions', labels:['INBOX','CATEGORY_PROMOTIONS','label_8']}),
    _e(46, 46, {name:'Figma',email:'newsletter@figma.com'}, 'Config 2026: Early bird tickets now available', 'Join 10,000+ designers at Config 2026 in San Francisco. Early bird pricing: $499 (save $200).', '2026-02-22T12:00:00Z', {isRead:true, category:'promotions', labels:['INBOX','CATEGORY_PROMOTIONS']}),
    _e(47, 47, {name:'JetBrains',email:'news@jetbrains.com'}, 'IntelliJ IDEA 2026.1 is here!', 'AI-powered code completion, improved Kubernetes support, and 40% faster indexing. Upgrade today.', '2026-02-21T08:00:00Z', {isRead:false, category:'promotions', labels:['INBOX','CATEGORY_PROMOTIONS']}),
    _e(48, 48, {name:'Uniqlo',email:'newsletter@uniqlo.com'}, 'Spring Collection: New arrivals', 'Discover lightweight layers perfect for spring. Free shipping on orders $75+.', '2026-02-20T07:00:00Z', {isRead:true, category:'promotions', labels:['INBOX','CATEGORY_PROMOTIONS']}),
    _e(49, 49, {name:'United Airlines',email:'deals@united.com'}, 'Flash Sale: SFO to Paris from $489', 'Limited time fares to Europe. San Francisco to Paris from $489, London from $399, Barcelona from $459.', '2026-02-19T09:00:00Z', {isRead:true, isStarred:true, starType:'yellow-star', category:'promotions', labels:['INBOX','CATEGORY_PROMOTIONS','label_4']}),
    _e(50, 50, {name:'Apple',email:'news@apple.com'}, 'Introducing iPhone 17 Pro', 'The most powerful iPhone ever. A18 Pro chip, 48MP camera system, all-day battery. Pre-order now.', '2026-02-18T08:00:00Z', {isRead:true, category:'promotions', labels:['INBOX','CATEGORY_PROMOTIONS']}),
    _e(51, 51, {name:'Audible',email:'recommendations@audible.com'}, 'Your next great listen: AI Superpowers', 'Based on your library: "AI Superpowers" by Kai-Fu Lee. Free with your membership.', '2026-02-17T10:00:00Z', {isRead:true, category:'promotions', labels:['INBOX','CATEGORY_PROMOTIONS']}),
    _e(52, 52, {name:'Nike',email:'promo@nike.com'}, 'Members Week: 25% off everything', 'Exclusive for Nike Members. Use code MEMBER25 at checkout. Valid through February 28.', '2026-02-16T06:00:00Z', {isRead:true, category:'promotions', labels:['INBOX','CATEGORY_PROMOTIONS']}),
    _e(53, 53, {name:'Spotify',email:'no-reply@spotify.com'}, 'Your 2026 music journey starts here', 'We curated playlists based on your taste. Check out your Discover Weekly and Release Radar.', '2026-02-15T07:00:00Z', {isRead:true, category:'promotions', labels:['INBOX','CATEGORY_PROMOTIONS']}),
    _e(54, 54, {name:'Airbnb',email:'marketing@airbnb.com'}, 'Dream destinations for spring', 'Trending spots for March: Kyoto cherry blossoms, Amalfi Coast, Iceland Northern Lights. Book now.', '2026-02-14T12:00:00Z', {isRead:true, category:'promotions', labels:['INBOX','CATEGORY_PROMOTIONS','label_4']}),
    _e(55, 55, {name:'REI',email:'promotions@rei.com'}, 'Garage Sale: Up to 50% off', 'Annual Garage Sale starts this weekend. Deals on hiking gear, camping equipment, and outdoor apparel.', '2026-02-13T06:00:00Z', {isRead:true, category:'promotions', labels:['INBOX','CATEGORY_PROMOTIONS']}),

    // ---- Updates category ----
    _e(56, 56, {name:'Google',email:'no-reply@accounts.google.com'}, 'Security alert: New sign-in from Chrome on Windows', 'We noticed a new sign-in to your Google Account from Chrome on Windows. If this was you, you can disregard this email.', '2026-02-24T04:30:00Z', {isRead:false, isImportant:true, category:'updates', labels:['INBOX','CATEGORY_UPDATES']}),
    _e(57, 57, {name:'Chase Bank',email:'no-reply@chase.com'}, 'Your January statement is ready', 'Your Chase Sapphire Reserve statement for January 2026 is now available. Total balance: $3,247.82.', '2026-02-23T05:00:00Z', {isRead:true, category:'updates', labels:['INBOX','CATEGORY_UPDATES','label_3','label_16']}),
    _e(58, 58, {name:'Vercel',email:'notifications@vercel.com'}, 'Deployment successful: production', 'Project techcorp-dashboard deployed to production. Build time: 42s. URL: https://dashboard.techcorp.io', '2026-02-23T02:15:00Z', {isRead:true, category:'updates', labels:['INBOX','CATEGORY_UPDATES','label_1']}),
    _e(59, 59, {name:'Google Calendar',email:'calendar-notification@google.com'}, 'Reminder: Team Standup in 30 minutes', 'Team Standup · Monday Feb 24, 2026 10:00 AM. Google Meet link: meet.google.com/abc-defg-hij', '2026-02-24T09:30:00Z', {isRead:false, category:'updates', labels:['INBOX','CATEGORY_UPDATES','label_1','label_10']}),
    _e(60, 60, {name:'Stripe',email:'notifications@stripe.com'}, 'Payment received: $4,500.00', 'Payment of $4,500.00 from TechCorp Inc. has been processed. It will be deposited in 2 business days.', '2026-02-22T16:00:00Z', {isRead:true, category:'updates', labels:['INBOX','CATEGORY_UPDATES','label_3']}),
    _e(61, 61, {name:'AWS',email:'no-reply@aws.amazon.com'}, 'AWS Monthly Bill: $847.23', 'Your AWS bill for January 2026 is $847.23. This is 8% higher than last month due to increased EC2 usage.', '2026-02-22T03:00:00Z', {isRead:true, isImportant:true, category:'updates', labels:['INBOX','CATEGORY_UPDATES','label_3','label_15']}),
    _e(62, 62, {name:'Jira',email:'jira@techcorp.atlassian.net'}, 'TECH-2847: Status changed to In Review', 'Issue "Implement user analytics dashboard" was moved to In Review by Priya Sharma.', '2026-02-21T18:00:00Z', {isRead:true, category:'updates', labels:['INBOX','CATEGORY_UPDATES','label_1']}),
    _e(63, 63, {name:'Dropbox',email:'no-reply@dropbox.com'}, 'Sarah Chen shared "Q1 Planning Docs" with you', 'Sarah Chen shared a folder with you. Open the folder to view 12 files including presentations and spreadsheets.', '2026-02-21T10:00:00Z', {isRead:true, category:'updates', labels:['INBOX','CATEGORY_UPDATES','label_1']}),
    _e(64, 64, {name:'Google Photos',email:'noreply-photos@google.com'}, 'Your memories from February 2025', 'Take a look back at your photos from this time last year. 23 photos and 2 videos.', '2026-02-20T08:00:00Z', {isRead:true, category:'updates', labels:['INBOX','CATEGORY_UPDATES','label_2']}),
    _e(65, 65, {name:'DocuSign',email:'dse@docusign.net'}, 'Please sign: NDA - TechPartners Inc.', 'James O\'Brien sent you a document to sign. "Non-Disclosure Agreement - TechPartners Inc." Please review and sign by Feb 25.', '2026-02-19T14:00:00Z', {isRead:false, isStarred:true, starType:'yellow-star', isImportant:true, category:'updates', labels:['INBOX','CATEGORY_UPDATES','label_1','label_17']}),
    _e(66, 66, {name:'Notion',email:'notifications@makenotion.com'}, 'Weekly digest: 8 pages updated', 'This week in your workspace: 8 pages updated, 3 new pages created, 2 comments added.', '2026-02-19T07:00:00Z', {isRead:true, category:'updates', labels:['INBOX','CATEGORY_UPDATES','label_1']}),
    _e(67, 67, {name:'FedEx',email:'tracking@fedex.com'}, 'Your package has been delivered', 'Package delivered to front door at 2:34 PM. Tracking #: FX7294610583. Signed by: AJOHNSON.', '2026-02-18T14:34:00Z', {isRead:true, category:'updates', labels:['INBOX','CATEGORY_UPDATES','label_5']}),
    _e(68, 68, {name:'Datadog',email:'alerts@datadog.com'}, 'Alert: High CPU usage on prod-api-3', 'CPU usage on prod-api-3 exceeded 90% for 5 minutes. Current: 92%. Threshold: 85%.', '2026-02-18T03:45:00Z', {isRead:true, isImportant:true, category:'updates', labels:['INBOX','CATEGORY_UPDATES','label_1','label_17']}),
    _e(69, 69, {name:'Google',email:'googleplay-noreply@google.com'}, 'Your Google Play order receipt', 'Order #GPA.3394-0721-5892. YouTube Premium (Family) - $22.99/month. Next billing: Mar 18.', '2026-02-18T00:01:00Z', {isRead:true, category:'updates', labels:['INBOX','CATEGORY_UPDATES','label_5']}),
    _e(70, 70, {name:'1Password',email:'support@1password.com'}, 'Your 1Password security report', 'Your security score is 87/100. 3 weak passwords found, 1 reused password, 0 compromised passwords.', '2026-02-16T08:00:00Z', {isRead:true, category:'updates', labels:['INBOX','CATEGORY_UPDATES']}),

    // ---- Forums category ----
    _e(71, 71, {name:'Stack Overflow',email:'do-not-reply@stackoverflow.email'}, 'Your answer was accepted: "How to optimize React re-renders"', 'Your answer on "How to optimize React re-renders with useMemo" was accepted. +15 reputation.', '2026-02-23T13:00:00Z', {isRead:true, category:'forums', labels:['INBOX','CATEGORY_FORUMS','label_8']}),
    _e(72, 72, {name:'Hacker News',email:'hn@ycombinator.com'}, 'HN Digest: Top stories this week', 'Top stories: "Show HN: Open-source AI coding assistant," "Why we moved from microservices back to monolith."', '2026-02-22T06:00:00Z', {isRead:true, category:'forums', labels:['INBOX','CATEGORY_FORUMS','label_6']}),
    _e(73, 73, {name:'Dev.to',email:'digest@dev.to'}, 'Trending: "Building a real-time collaboration engine"', 'Top articles this week: Real-time collaboration, Deno 3.0 deep dive, Understanding WebTransport.', '2026-02-21T06:00:00Z', {isRead:false, category:'forums', labels:['INBOX','CATEGORY_FORUMS','label_6']}),
    _e(74, 74, {name:'Product Hunt',email:'hello@producthunt.com'}, 'Product of the Day: CodeFlow AI', 'CodeFlow AI - Your intelligent code review assistant. 1,247 upvotes. "This is exactly what we needed!"', '2026-02-20T06:00:00Z', {isRead:true, category:'forums', labels:['INBOX','CATEGORY_FORUMS']}),
    _e(75, 75, {name:'Lobsters',email:'digest@lobste.rs'}, 'Lobsters Weekly: Systems Programming', 'Popular stories: "Writing a TCP stack from scratch," "Memory allocator benchmarks," "New LLVM optimizations."', '2026-02-19T06:00:00Z', {isRead:true, category:'forums', labels:['INBOX','CATEGORY_FORUMS','label_6']}),
    _e(76, 76, {name:'Stack Overflow',email:'do-not-reply@stackoverflow.email'}, 'New answer on your question about TypeScript generics', 'Someone posted an answer to "TypeScript conditional types with nested generics." View the answer.', '2026-02-17T11:00:00Z', {isRead:true, category:'forums', labels:['INBOX','CATEGORY_FORUMS','label_8']}),

    // ---- Newsletters (labeled) ----
    _e(77, 77, {name:'Morning Brew',email:'crew@morningbrew.com'}, 'Daily Brew: Fed signals rate cuts', 'Fed Chair signals possible rate cuts in Q2. Tesla hits $300/share. Apple Vision Pro sales surge 200%.', '2026-02-24T06:30:00Z', {isRead:false, labels:['INBOX','CATEGORY_PRIMARY','label_6']}),
    _e(78, 78, {name:'The Pragmatic Engineer',email:'gergely@pragmaticengineer.com'}, 'Big Tech hiring is back - what changed?', 'After 2 years of hiring freezes, FAANG companies are ramping up. Here\'s what\'s different this time.', '2026-02-22T07:00:00Z', {isRead:true, isStarred:true, starType:'yellow-star', labels:['INBOX','CATEGORY_PRIMARY','label_6','label_19']}),
    _e(79, 79, {name:'TLDR Newsletter',email:'dan@tldrnewsletter.com'}, 'TLDR: GPT-5 benchmarks leaked', 'GPT-5 benchmarks, Rust 2.0 announced, Docker alternatives, PostgreSQL 17 features.', '2026-02-21T06:00:00Z', {isRead:true, labels:['INBOX','CATEGORY_PRIMARY','label_6']}),
    _e(80, 80, {name:'Benedict Evans',email:'newsletter@ben-evans.com'}, 'AI and the future of search', 'Long-form analysis of how AI is reshaping information retrieval and what it means for Google.', '2026-02-19T08:00:00Z', {isRead:true, labels:['INBOX','CATEGORY_PRIMARY','label_6','label_19']}),
    _e(81, 81, {name:'Stratechery',email:'ben@stratechery.com'}, 'The Great AI Unbundling', 'How AI is disrupting SaaS businesses by enabling customers to build their own tools.', '2026-02-17T07:00:00Z', {isRead:true, labels:['INBOX','CATEGORY_PRIMARY','label_6']}),

    // ---- Snoozed emails ----
    _e(82, 82, {name:'Emily Rodriguez',email:'emily.r@startupventures.co'}, 'Investor Deck Review', 'Can you review our updated investor deck? We\'re presenting to Sequoia next week.', '2026-02-15T09:00:00Z', {isRead:true, isSnoozed:true, snoozeUntil:'2026-02-25T08:00:00Z', labels:['CATEGORY_PRIMARY','label_1','label_11']}),
    _e(83, 83, {name:'Tom Bradley',email:'tom.bradley@realtyhome.com'}, 'Mortgage Pre-approval Documents', 'Please submit the following documents for mortgage pre-approval: pay stubs, tax returns, bank statements.', '2026-02-12T10:00:00Z', {isRead:true, isSnoozed:true, snoozeUntil:'2026-02-26T09:00:00Z', labels:['CATEGORY_PRIMARY','label_3']}),
    _e(84, 84, {name:'Ana Gutierrez',email:'ana.g@globalhealth.org'}, 'Annual Check-up Reminder', 'Hi Alex, it\'s been a year since your last check-up. Please schedule an appointment at your convenience.', '2026-02-10T08:00:00Z', {isRead:true, isSnoozed:true, snoozeUntil:'2026-03-01T08:00:00Z', labels:['CATEGORY_PRIMARY','label_7']}),

    // ---- Archived emails ----
    _e(85, 85, {name:'Sarah Chen',email:'sarah.chen@techcorp.io'}, 'Meeting notes: Sprint planning', 'Sprint 14 goals: Complete auth refactor, start dashboard redesign, fix top 5 bugs.', '2026-02-10T11:00:00Z', {isRead:true, isArchived:true, labels:['CATEGORY_PRIMARY','label_1','label_10']}),
    _e(86, 86, {name:'Nate Patel',email:'nate.patel@devops.tools'}, 'Server maintenance complete', 'All servers have been updated to the latest patch. No downtime observed. Monitoring for 24h.', '2026-02-08T22:00:00Z', {isRead:true, isArchived:true, labels:['CATEGORY_PRIMARY','label_1']}),
    _e(87, 87, {name:'Marcus Williams',email:'marcus.w@designhub.com'}, 'Icon library update', 'Updated the icon library with 50 new icons. Download link in the design Slack channel.', '2026-02-06T14:00:00Z', {isRead:true, isArchived:true, labels:['CATEGORY_PRIMARY','label_1']}),
    _e(88, 88, {name:'Amazon',email:'ship-confirm@amazon.com'}, 'Your order has shipped: Mechanical Keyboard', 'Your order #114-3847291-5738261 has shipped. Estimated delivery: Feb 10.', '2026-02-05T08:00:00Z', {isRead:true, isArchived:true, category:'updates', labels:['CATEGORY_UPDATES','label_5']}),

    // ---- Trashed emails ----
    _e(89, 89, {name:'Unknown Sender',email:'prince.of.lagos@hotmail.com'}, 'You have inherited $5,000,000', 'Dear beneficiary, you have been selected to receive a sum of five million dollars...', '2026-02-20T03:00:00Z', {isRead:true, isTrashed:true, labels:[]}),
    _e(90, 90, {name:'Casino Online',email:'winner@luckycasino.xxx'}, 'Congratulations! You won $10,000!', 'Click here to claim your prize. Limited time offer. Act now!', '2026-02-19T02:00:00Z', {isRead:true, isTrashed:true, labels:[]}),
    _e(91, 91, {name:'Flash Sale',email:'deals@cheapelectronics.biz'}, 'AMAZING DEAL: iPhone for $1!!!', 'Limited stock! Get the latest iPhone for only $1. Click here before it\'s gone!', '2026-02-18T05:00:00Z', {isRead:true, isTrashed:true, labels:[]}),
    _e(92, 92, {name:'Newsletter Spam',email:'updates@randomnews247.com'}, 'You won\'t believe what happened next', 'Click here for the most shocking news of 2026. This will change everything you know!', '2026-02-17T03:00:00Z', {isRead:true, isTrashed:true, labels:[]}),

    // ---- Spam emails ----
    _e(93, 93, {name:'Crypto Gains',email:'invest@cryptomoon.xyz'}, 'Turn $100 into $100,000 with this coin!', 'The next Bitcoin is here. Invest now before it\'s too late. Guaranteed 1000x returns.', '2026-02-22T01:00:00Z', {isRead:false, isSpam:true, labels:[]}),
    _e(94, 94, {name:'Weight Loss Miracle',email:'health@dietpills4u.com'}, 'Lose 30 pounds in 30 days!', 'Revolutionary new supplement burns fat while you sleep. No exercise needed!', '2026-02-21T04:00:00Z', {isRead:false, isSpam:true, labels:[]}),
    _e(95, 95, {name:'Lottery Winner',email:'claims@eurolottery.scam'}, 'Your email won the EU Lottery!', 'Your email address was selected in our annual draw. You\'ve won EUR 750,000.', '2026-02-20T06:00:00Z', {isRead:false, isSpam:true, labels:[]}),
    _e(96, 96, {name:'Account Alert',email:'security@bankofamerica-verify.com'}, 'Urgent: Verify your account now', 'Your Bank of America account has been suspended. Click here to verify your identity.', '2026-02-19T03:00:00Z', {isRead:false, isSpam:true, labels:[]}),
    _e(97, 97, {name:'Free Gift Cards',email:'rewards@amazongiftcard.fake'}, 'Claim your $500 Amazon Gift Card', 'You\'ve been selected to receive a $500 Amazon Gift Card. Complete a short survey to claim.', '2026-02-18T02:00:00Z', {isRead:false, isSpam:true, labels:[]}),

    // ---- Draft emails ----
    _e(98, 98, {name:'Alex Johnson',email:'alex.johnson@gmail.com'}, 'Re: Conference Talk Proposal', 'Hi Sophie, Thank you for the invitation to speak at EuroDesign Summit. I\'d be happy to present on...', '2026-02-23T20:00:00Z', {isRead:true, isDraft:true, labels:['DRAFT'], to:[{name:'Sophie Laurent',email:'sophie.l@eurodesign.fr'}]}),
    _e(99, 99, {name:'Alex Johnson',email:'alex.johnson@gmail.com'}, 'Project Proposal: AI-Powered Analytics', 'Dear Sarah, I\'d like to propose a new project for Q2: building an AI-powered analytics dashboard that...', '2026-02-22T21:00:00Z', {isRead:true, isDraft:true, labels:['DRAFT'], to:[{name:'Sarah Chen',email:'sarah.chen@techcorp.io'}]}),

    // ---- Sent emails ----
    _e(100, 100, {name:'Alex Johnson',email:'alex.johnson@gmail.com'}, 'Re: Team Dinner', 'March 7th works for me! Zafferano is a great choice. See you all there.', '2026-02-19T13:30:00Z', {isRead:true, isSent:true, labels:['SENT'], to:[{name:'Sarah Chen',email:'sarah.chen@techcorp.io'}]}),
    _e(101, 101, {name:'Alex Johnson',email:'alex.johnson@gmail.com'}, 'Budget Approval Request', 'Hi David, I need approval for the Q2 infrastructure budget. Attached is the breakdown.', '2026-02-18T16:00:00Z', {isRead:true, isSent:true, labels:['SENT'], to:[{name:'David Kim',email:'david.kim@financeplus.com'}], hasAttachments:true, attachments:[{name:'Q2_Budget.xlsx',size:'230 KB'}]}),
    _e(102, 102, {name:'Alex Johnson',email:'alex.johnson@gmail.com'}, 'Recommendation Letter', 'Dear Robert, I\'m happy to write a recommendation letter for your graduate program. I\'ve attached it here.', '2026-02-16T10:00:00Z', {isRead:true, isSent:true, labels:['SENT'], to:[{name:'Robert Singh',email:'robert.singh@university.edu'}], hasAttachments:true, attachments:[{name:'Recommendation_RobertSingh.pdf',size:'180 KB'}]}),

    // ---- Muted conversation ----
    _e(103, 103, {name:'HR Team',email:'hr@techcorp.io'}, 'Re: Office Snack Preferences Survey', 'Thanks everyone for your responses! We\'ll update the snack selection based on your preferences.', '2026-02-17T15:00:00Z', {isRead:true, isMuted:true, isArchived:true, labels:['CATEGORY_PRIMARY','label_12']}),

    // ---- More Primary emails for volume ----
    _e(104, 104, {name:'Sarah Chen',email:'sarah.chen@techcorp.io'}, 'Re: Quarterly Team Dinner', 'March 7th is perfect! I\'ll make the reservation for 8 people. Any dietary restrictions?', '2026-02-19T14:30:00Z', {isRead:true, labels:['INBOX','CATEGORY_PRIMARY','label_1']}),
    _e(105, 105, {name:'Priya Sharma',email:'priya.sharma@cloudnine.dev'}, 'Code Review Request: auth-service PR #42', 'Hey Alex, can you review my PR for the OAuth2 PKCE implementation? It\'s about 400 lines.', '2026-02-18T09:00:00Z', {isRead:false, labels:['INBOX','CATEGORY_PRIMARY','label_1','label_9']}),
    _e(106, 106, {name:'Ryan Cooper',email:'ryan.cooper@saasplatform.io'}, 'SaaS Platform Q1 Pricing Update', 'Heads up - we\'re adjusting enterprise tier pricing starting March 1st. Existing contracts unaffected.', '2026-02-17T14:00:00Z', {isRead:true, labels:['INBOX','CATEGORY_PRIMARY','label_1']}),
    _e(107, 107, {name:'Kevin Zhao',email:'kevin.zhao@quantumlab.tech'}, 'Lab Tour Invitation', 'We\'re hosting an open lab day on March 5th. Would love to show you our new quantum processor setup.', '2026-02-16T11:00:00Z', {isRead:true, labels:['INBOX','CATEGORY_PRIMARY','label_2']}),
    _e(108, 108, {name:'Jennifer Wu',email:'jennifer.wu@biomedresearch.com'}, 'BioMed Conference Recap', 'Great seeing you at the conference! Here are the slides from the panel we discussed.', '2026-02-15T16:00:00Z', {isRead:true, hasAttachments:true, attachments:[{name:'BioMed_Panel_Slides.pdf',size:'3.8 MB'}], labels:['INBOX','CATEGORY_PRIMARY','label_8']}),
    _e(109, 109, {name:'Maya Patel',email:'maya.patel@techcorp.io'}, 'Performance Review Self-Assessment Due', 'Reminder: please submit your self-assessment by end of day Friday. Template link in the HR portal.', '2026-02-14T09:00:00Z', {isRead:true, isImportant:true, labels:['INBOX','CATEGORY_PRIMARY','label_1','label_12','label_17']}),
    _e(110, 110, {name:'Daniel Thompson',email:'daniel.t@architectsllp.com'}, 'Permit Application Status', 'Good news - the city approved our renovation permit. Construction can begin March 10th.', '2026-02-13T15:00:00Z', {isRead:true, labels:['INBOX','CATEGORY_PRIMARY']}),

    // ---- Older emails across categories ----
    _e(111, 111, {name:'Google',email:'no-reply@google.com'}, 'Your Google Cloud billing summary', 'January 2026 summary: Total spend $234.56. Top services: Compute Engine, Cloud Storage, BigQuery.', '2026-02-01T06:00:00Z', {isRead:true, category:'updates', labels:['INBOX','CATEGORY_UPDATES','label_3','label_15']}),
    _e(112, 112, {name:'Medium',email:'noreply@medium.com'}, 'Daily Digest: Top stories in Technology', 'Trending: "The end of traditional databases," "Why WebAssembly changes everything," "Lessons from building at scale."', '2026-02-01T07:00:00Z', {isRead:true, category:'forums', labels:['INBOX','CATEGORY_FORUMS','label_6']}),
    _e(113, 113, {name:'LinkedIn',email:'notifications@linkedin.com'}, 'Job alert: Senior Engineering Manager', '12 new jobs matching your preferences. Top match: Senior Engineering Manager at Stripe - San Francisco.', '2026-01-31T08:00:00Z', {isRead:true, category:'social', labels:['INBOX','CATEGORY_SOCIAL']}),
    _e(114, 114, {name:'Netflix',email:'info@mailer.netflix.com'}, 'New arrivals you might enjoy', 'Based on your watching: "The Algorithm" (new series), "Code Black" (documentary), "Silicon Valley: The Return."', '2026-01-30T06:00:00Z', {isRead:true, category:'promotions', labels:['INBOX','CATEGORY_PROMOTIONS']}),
    _e(115, 115, {name:'James O\'Brien',email:'james.obrien@lawfirm.legal'}, 'Annual Retainer Renewal', 'Alex, our retainer agreement is up for renewal in March. Let\'s schedule a call to discuss terms.', '2026-01-28T10:00:00Z', {isRead:true, labels:['INBOX','CATEGORY_PRIMARY','label_3']}),
    _e(116, 116, {name:'GitHub',email:'notifications@github.com'}, '[techcorp/frontend] Release v3.2.0', 'New release: v3.2.0 - Dashboard redesign, improved accessibility, performance optimizations.', '2026-01-27T16:00:00Z', {isRead:true, category:'social', labels:['INBOX','CATEGORY_SOCIAL','label_1']}),
    _e(117, 117, {name:'Omar Al-Rashid',email:'omar.ar@consulting.group'}, 'Digital Transformation Assessment', 'Attached is our initial assessment of your digital transformation readiness. Executive summary on page 3.', '2026-01-25T09:00:00Z', {isRead:true, hasAttachments:true, attachments:[{name:'DT_Assessment_2026.pdf',size:'4.5 MB'}], labels:['INBOX','CATEGORY_PRIMARY','label_1','label_19']}),
    _e(118, 118, {name:'Morning Brew',email:'crew@morningbrew.com'}, 'Daily Brew: Tech IPOs heat up', 'Three tech companies filed S-1s this week. The IPO market is back in full swing.', '2026-01-24T06:30:00Z', {isRead:true, labels:['INBOX','CATEGORY_PRIMARY','label_6']}),
    _e(119, 119, {name:'Aisha Mohammed',email:'aisha.m@edtech.academy'}, 'New Course: Kubernetes Mastery', 'We just launched "Kubernetes Mastery" - from basics to production. Early enrollment discount: 30% off.', '2026-01-22T10:00:00Z', {isRead:true, category:'promotions', labels:['INBOX','CATEGORY_PROMOTIONS','label_8']}),
    _e(120, 120, {name:'Rachel Foster',email:'rachel.foster@nonprofitaid.org'}, 'Volunteer Appreciation Dinner', 'You\'re invited to our annual volunteer appreciation dinner on Feb 8th. RSVP by Jan 31.', '2026-01-20T12:00:00Z', {isRead:true, labels:['INBOX','CATEGORY_PRIMARY','label_2']}),
    _e(121, 121, {name:'Google',email:'no-reply@accounts.google.com'}, '2-Step Verification: New phone added', 'A new phone was added to your 2-Step Verification. If you didn\'t do this, review your security settings.', '2026-01-19T15:00:00Z', {isRead:true, category:'updates', labels:['INBOX','CATEGORY_UPDATES']}),
    _e(122, 122, {name:'David Kim',email:'david.kim@financeplus.com'}, 'Year-End Financial Summary 2025', 'Attached: your 2025 financial summary with investment returns, tax estimates, and 2026 planning recommendations.', '2026-01-18T09:00:00Z', {isRead:true, isStarred:true, starType:'yellow-star', hasAttachments:true, attachments:[{name:'2025_YearEnd_Summary.pdf',size:'2.3 MB'}], labels:['INBOX','CATEGORY_PRIMARY','label_3','label_19']}),
    _e(123, 123, {name:'Lisa Nakamura',email:'lisa.n@creativeagency.co'}, 'Portfolio Website Mockups', 'Three mockup options for your personal portfolio site. Modern, minimal, or creative direction?', '2026-01-17T13:00:00Z', {isRead:true, hasAttachments:true, attachments:[{name:'Portfolio_Mockups.pdf',size:'12.5 MB'}], labels:['INBOX','CATEGORY_PRIMARY','label_2']}),
    _e(124, 124, {name:'Vercel',email:'notifications@vercel.com'}, 'Build failed: staging branch', 'Build #4821 failed for staging. Error: TypeScript compilation error in src/components/Dashboard.tsx:47.', '2026-01-16T02:30:00Z', {isRead:true, category:'updates', labels:['INBOX','CATEGORY_UPDATES','label_1']}),
    _e(125, 125, {name:'Hannah Brooks',email:'hannah.b@fitnessfirst.com'}, 'February Fitness Challenge', 'Join our 28-day fitness challenge! Daily workouts, nutrition tips, and weekly check-ins. Starts Feb 1.', '2026-01-15T10:00:00Z', {isRead:true, labels:['INBOX','CATEGORY_PRIMARY','label_7']}),

    // More sent emails for volume
    _e(126, 16, {name:'Alex Johnson',email:'alex.johnson@gmail.com'}, 'Re: Interview Request: Tech Innovation Panel', 'Hi Michelle, I\'d be happy to participate. Next Tuesday or Wednesday afternoon works best for me.', '2026-02-20T09:00:00Z', {isRead:true, isSent:true, labels:['SENT'], to:[{name:'Michelle Park',email:'michelle.park@mediaco.tv'}]}),
    _e(127, 127, {name:'Alex Johnson',email:'alex.johnson@gmail.com'}, 'Meeting Agenda: Product Strategy', 'Team, here\'s the agenda for our product strategy meeting on Thursday. Please review and add any items.', '2026-02-19T08:00:00Z', {isRead:true, isSent:true, labels:['SENT'], to:[{name:'Sarah Chen',email:'sarah.chen@techcorp.io'},{name:'Maya Patel',email:'maya.patel@techcorp.io'}]}),
    _e(128, 128, {name:'Alex Johnson',email:'alex.johnson@gmail.com'}, 'Feedback on Design Mockups', 'Hi Lisa, love direction #2 (minimal). A few tweaks: can we try a darker header and add a project filter?', '2026-02-17T14:00:00Z', {isRead:true, isSent:true, labels:['SENT'], to:[{name:'Lisa Nakamura',email:'lisa.n@creativeagency.co'}]}),

    // Additional emails with multiple star types
    _e(129, 129, {name:'Sarah Chen',email:'sarah.chen@techcorp.io'}, 'URGENT: Production database issue', 'Database connections maxing out. Need immediate attention. I\'m pulling in the on-call team.', '2026-02-14T02:00:00Z', {isRead:true, isStarred:true, starType:'red-bang', isImportant:true, labels:['INBOX','CATEGORY_PRIMARY','label_1','label_17']}),
    _e(130, 130, {name:'Kevin Zhao',email:'kevin.zhao@quantumlab.tech'}, 'Interesting paper on LLM optimization', 'Found this paper on efficient LLM inference. The pruning technique is fascinating.', '2026-02-12T11:00:00Z', {isRead:true, isStarred:true, starType:'purple-question', labels:['INBOX','CATEGORY_PRIMARY','label_8','label_19']}),
];

// ---- Filters ----
const FILTERS = [
    { id: 'filter_1', criteria: { from: 'notifications@github.com', to: '', subject: '', hasWords: '', doesntHave: '', hasAttachment: false, size: null, sizeUnit: 'MB', sizeComparison: 'greater' }, actions: { label: 'label_1', archive: false, markRead: false, star: false, forward: null, delete: false, neverSpam: true, alwaysImportant: false, neverImportant: false, category: null }, enabled: true, createdAt: '2025-06-10T09:00:00Z' },
    { id: 'filter_2', criteria: { from: 'crew@morningbrew.com', to: '', subject: '', hasWords: '', doesntHave: '', hasAttachment: false, size: null, sizeUnit: 'MB', sizeComparison: 'greater' }, actions: { label: 'label_6', archive: false, markRead: false, star: false, forward: null, delete: false, neverSpam: true, alwaysImportant: false, neverImportant: false, category: null }, enabled: true, createdAt: '2025-07-15T10:00:00Z' },
    { id: 'filter_3', criteria: { from: '', to: '', subject: 'invoice', hasWords: 'payment receipt', doesntHave: '', hasAttachment: false, size: null, sizeUnit: 'MB', sizeComparison: 'greater' }, actions: { label: 'label_15', archive: false, markRead: false, star: false, forward: null, delete: false, neverSpam: false, alwaysImportant: false, neverImportant: false, category: null }, enabled: true, createdAt: '2025-08-20T14:00:00Z' },
    { id: 'filter_4', criteria: { from: '', to: '', subject: '', hasWords: 'unsubscribe', doesntHave: '', hasAttachment: false, size: null, sizeUnit: 'MB', sizeComparison: 'greater' }, actions: { label: null, archive: false, markRead: false, star: false, forward: null, delete: false, neverSpam: false, alwaysImportant: false, neverImportant: true, category: 'promotions' }, enabled: true, createdAt: '2025-09-05T11:00:00Z' },
    { id: 'filter_5', criteria: { from: 'sarah.chen@techcorp.io', to: '', subject: '', hasWords: '', doesntHave: '', hasAttachment: false, size: null, sizeUnit: 'MB', sizeComparison: 'greater' }, actions: { label: 'label_1', archive: false, markRead: false, star: false, forward: null, delete: false, neverSpam: true, alwaysImportant: true, neverImportant: false, category: null }, enabled: true, createdAt: '2025-10-12T08:00:00Z' },
    { id: 'filter_6', criteria: { from: '', to: '', subject: '', hasWords: '', doesntHave: '', hasAttachment: true, size: 10, sizeUnit: 'MB', sizeComparison: 'greater' }, actions: { label: null, archive: false, markRead: false, star: true, forward: null, delete: false, neverSpam: false, alwaysImportant: false, neverImportant: false, category: null }, enabled: true, createdAt: '2025-11-01T09:00:00Z' },
    { id: 'filter_7', criteria: { from: 'no-reply@accounts.google.com', to: '', subject: 'security', hasWords: '', doesntHave: '', hasAttachment: false, size: null, sizeUnit: 'MB', sizeComparison: 'greater' }, actions: { label: null, archive: false, markRead: false, star: false, forward: null, delete: false, neverSpam: true, alwaysImportant: true, neverImportant: false, category: null }, enabled: true, createdAt: '2025-12-15T10:00:00Z' },
    { id: 'filter_8', criteria: { from: '', to: '', subject: '', hasWords: 'meeting agenda standup', doesntHave: '', hasAttachment: false, size: null, sizeUnit: 'MB', sizeComparison: 'greater' }, actions: { label: 'label_10', archive: false, markRead: false, star: false, forward: null, delete: false, neverSpam: false, alwaysImportant: false, neverImportant: false, category: null }, enabled: true, createdAt: '2026-01-05T08:00:00Z' },
    { id: 'filter_9', criteria: { from: 'hr@techcorp.io', to: '', subject: '', hasWords: '', doesntHave: '', hasAttachment: false, size: null, sizeUnit: 'MB', sizeComparison: 'greater' }, actions: { label: 'label_12', archive: false, markRead: false, star: false, forward: null, delete: false, neverSpam: false, alwaysImportant: false, neverImportant: false, category: null }, enabled: true, createdAt: '2026-01-15T09:00:00Z' },
    { id: 'filter_10', criteria: { from: 'alerts@datadog.com', to: '', subject: '', hasWords: 'alert critical', doesntHave: '', hasAttachment: false, size: null, sizeUnit: 'MB', sizeComparison: 'greater' }, actions: { label: 'label_17', archive: false, markRead: false, star: true, forward: 'nate.patel@devops.tools', delete: false, neverSpam: true, alwaysImportant: true, neverImportant: false, category: null }, enabled: true, createdAt: '2026-01-20T11:00:00Z' },
    { id: 'filter_11', criteria: { from: '', to: '', subject: '', hasWords: 'confidential', doesntHave: '', hasAttachment: false, size: null, sizeUnit: 'MB', sizeComparison: 'greater' }, actions: { label: 'label_1', archive: false, markRead: false, star: false, forward: null, delete: false, neverSpam: false, alwaysImportant: true, neverImportant: false, category: null }, enabled: true, createdAt: '2026-02-01T10:00:00Z' },
    { id: 'filter_12', criteria: { from: 'notifications@linkedin.com', to: '', subject: '', hasWords: '', doesntHave: '', hasAttachment: false, size: null, sizeUnit: 'MB', sizeComparison: 'greater' }, actions: { label: null, archive: false, markRead: false, star: false, forward: null, delete: false, neverSpam: false, alwaysImportant: false, neverImportant: false, category: 'social' }, enabled: true, createdAt: '2026-02-05T08:00:00Z' },
];

// ---- Settings ----
const SETTINGS = {
    theme: 'default',
    inboxType: 'default',
    conversationView: true,
    density: 'default',
    previewPane: 'none',
    keyboardShortcutsEnabled: true,
    importanceMarkers: true,
    categoriesEnabled: { primary: true, social: true, promotions: true, updates: true, forums: true },
    enabledStars: ['yellow-star','orange-star','red-star','purple-star','blue-star','green-star','yellow-bang','red-bang','purple-question','orange-guillemet','blue-info'],
    dynamicEmail: true,
    hoverActions: true,
    buttonLabels: 'icons',
    desktopNotifications: 'off',
    multipleInboxSections: [
        { query: 'is:starred', name: 'Starred', maxMessages: 25 },
        { query: 'is:snoozed', name: 'Snoozed', maxMessages: 25 },
        { query: 'label:Work', name: 'Work', maxMessages: 25 },
        { query: '', name: 'Section 4', maxMessages: 25 },
        { query: '', name: 'Section 5', maxMessages: 25 }
    ],
    multipleInboxPosition: 'right',
    sendAndArchive: true,
    undoSendDelay: 5,
    defaultReplyBehavior: 'reply',
    nudges: { suggestEmailsToReply: true, suggestEmailsToFollowUp: true },
    autoAdvance: 'newer',
    language: 'English (US)',
    maxPageSize: 50,
};

// ---- Blocked Senders ----
const BLOCKED_SENDERS = [
    { email: 'spam@marketing-blast.com', blockedAt: '2025-11-15T10:00:00Z' },
    { email: 'annoying@daily-deals.biz', blockedAt: '2025-12-20T14:00:00Z' },
    { email: 'noreply@fake-bank-alert.com', blockedAt: '2026-01-10T09:00:00Z' },
    { email: 'offers@shadydeals.xyz', blockedAt: '2026-01-25T16:00:00Z' },
    { email: 'winner@prize-notification.scam', blockedAt: '2026-02-05T11:00:00Z' },
];
