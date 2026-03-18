/* data.js — Seed data for Xero Invoicing */
/* eslint-disable */

const SEED_DATA_VERSION = 1;

const CONTACTS = [
    { id: 'con_1', name: 'Ridgeway University', email: 'accounts@ridgewayuni.ac.nz', phone: '+64 9 445 7200', billingAddress: { street: '42 Ridgeway Terrace', city: 'Auckland', region: 'Auckland', postalCode: '1010', country: 'New Zealand' }, taxId: 'NZ-98-765-432', contactType: 'customer', createdAt: '2024-06-10T09:00:00Z' },
    { id: 'con_2', name: 'Hamilton Plumbing Services', email: 'invoices@hamiltonplumbing.co.nz', phone: '+64 7 838 1122', billingAddress: { street: '18 Commerce Lane', city: 'Hamilton', region: 'Waikato', postalCode: '3204', country: 'New Zealand' }, taxId: 'NZ-11-222-333', contactType: 'customer', createdAt: '2024-07-15T14:30:00Z' },
    { id: 'con_3', name: 'Coastal Cafe Group', email: 'finance@coastalcafe.co.nz', phone: '+64 3 441 8800', billingAddress: { street: '7 Marine Parade', city: 'Queenstown', region: 'Otago', postalCode: '9300', country: 'New Zealand' }, taxId: 'NZ-44-555-666', contactType: 'customer', createdAt: '2024-08-01T11:00:00Z' },
    { id: 'con_4', name: 'Nexus Technologies Ltd', email: 'ap@nexustech.co.nz', phone: '+64 4 499 3300', billingAddress: { street: '150 Lambton Quay, Level 12', city: 'Wellington', region: 'Wellington', postalCode: '6011', country: 'New Zealand' }, taxId: 'NZ-77-888-999', contactType: 'customer', createdAt: '2024-05-20T08:15:00Z' },
    { id: 'con_5', name: 'Bright Spark Electrical', email: 'admin@brightspark.co.nz', phone: '+64 9 520 4455', billingAddress: { street: '33 Great South Road', city: 'Auckland', region: 'Auckland', postalCode: '1061', country: 'New Zealand' }, taxId: 'NZ-22-333-444', contactType: 'customer', createdAt: '2024-09-12T16:45:00Z' },
    { id: 'con_6', name: 'Summit Financial Advisors', email: 'billing@summitfa.co.nz', phone: '+64 3 379 5500', billingAddress: { street: '88 Cashel Street, Suite 4', city: 'Christchurch', region: 'Canterbury', postalCode: '8011', country: 'New Zealand' }, taxId: 'NZ-55-666-777', contactType: 'customer', createdAt: '2024-04-18T10:20:00Z' },
    { id: 'con_7', name: 'Green Valley Organics', email: 'accounts@greenvalley.co.nz', phone: '+64 6 356 7788', billingAddress: { street: '215 Fitzherbert Avenue', city: 'Palmerston North', region: 'Manawatu-Wanganui', postalCode: '4410', country: 'New Zealand' }, taxId: 'NZ-33-444-555', contactType: 'customer', createdAt: '2024-10-05T13:00:00Z' },
    { id: 'con_8', name: 'Metro Print Solutions', email: 'pay@metroprint.co.nz', phone: '+64 9 307 2200', billingAddress: { street: '5 Federal Street', city: 'Auckland', region: 'Auckland', postalCode: '1010', country: 'New Zealand' }, taxId: 'NZ-66-777-888', contactType: 'customer', createdAt: '2024-03-22T09:30:00Z' },
    { id: 'con_9', name: 'Pinnacle Construction Co', email: 'finance@pinnacleconstruction.co.nz', phone: '+64 7 577 9900', billingAddress: { street: '60 Devonport Road', city: 'Tauranga', region: 'Bay of Plenty', postalCode: '3110', country: 'New Zealand' }, taxId: 'NZ-88-999-000', contactType: 'customer', createdAt: '2024-06-28T15:10:00Z' },
    { id: 'con_10', name: 'Oceanview Resort & Spa', email: 'accounts@oceanviewresort.co.nz', phone: '+64 9 486 6622', billingAddress: { street: '12 Takapuna Beach Road', city: 'Auckland', region: 'Auckland', postalCode: '0622', country: 'New Zealand' }, taxId: 'NZ-99-000-111', contactType: 'customer', createdAt: '2024-07-04T11:45:00Z' },
    { id: 'con_11', name: 'DataFlow Analytics Inc', email: 'invoices@dataflow.io', phone: '+1 415 555 0142', billingAddress: { street: '580 Market Street, Suite 300', city: 'San Francisco', region: 'CA', postalCode: '94104', country: 'United States' }, taxId: 'US-82-1234567', contactType: 'customer', createdAt: '2024-08-19T07:00:00Z' },
    { id: 'con_12', name: 'Swift Courier Services', email: 'billing@swiftcourier.co.nz', phone: '+64 9 366 1100', billingAddress: { street: '29 Hobson Street', city: 'Auckland', region: 'Auckland', postalCode: '1010', country: 'New Zealand' }, taxId: 'NZ-10-111-222', contactType: 'customer', createdAt: '2024-11-01T08:30:00Z' },
    { id: 'con_13', name: 'Harmony Music Academy', email: 'admin@harmonymusic.co.nz', phone: '+64 4 384 2233', billingAddress: { street: '74 Cuba Street', city: 'Wellington', region: 'Wellington', postalCode: '6011', country: 'New Zealand' }, taxId: 'NZ-20-222-333', contactType: 'customer', createdAt: '2024-05-08T12:15:00Z' },
    { id: 'con_14', name: 'Pacific Timber Supplies', email: 'accounts@pactimber.co.nz', phone: '+64 7 347 5566', billingAddress: { street: '180 Te Ngae Road', city: 'Rotorua', region: 'Bay of Plenty', postalCode: '3010', country: 'New Zealand' }, taxId: 'NZ-30-333-444', contactType: 'customer', createdAt: '2024-09-25T14:00:00Z' },
    { id: 'con_15', name: 'Bloom & Branch Florists', email: 'hello@bloombranch.co.nz', phone: '+64 9 623 7744', billingAddress: { street: '103 Ponsonby Road', city: 'Auckland', region: 'Auckland', postalCode: '1011', country: 'New Zealand' }, taxId: 'NZ-40-444-555', contactType: 'customer', createdAt: '2024-10-18T10:00:00Z' },
    { id: 'con_16', name: 'Ironclad Security Systems', email: 'procurement@ironcladsec.co.nz', phone: '+64 9 580 3300', billingAddress: { street: '200 Ellerslie-Panmure Highway', city: 'Auckland', region: 'Auckland', postalCode: '1060', country: 'New Zealand' }, taxId: 'NZ-50-555-666', contactType: 'customer', createdAt: '2024-04-30T16:20:00Z' },
    { id: 'con_17', name: 'Clearwater Environmental', email: 'finance@clearwaterenv.co.nz', phone: '+64 3 548 9900', billingAddress: { street: '45 Halifax Street', city: 'Nelson', region: 'Nelson', postalCode: '7010', country: 'New Zealand' }, taxId: 'NZ-60-666-777', contactType: 'customer', createdAt: '2024-08-14T09:45:00Z' },
    { id: 'con_18', name: 'Apex Legal Partners', email: 'accounts@apexlegal.co.nz', phone: '+64 4 471 1188', billingAddress: { street: '22 The Terrace, Level 8', city: 'Wellington', region: 'Wellington', postalCode: '6011', country: 'New Zealand' }, taxId: 'NZ-70-777-888', contactType: 'customer', createdAt: '2024-06-03T13:30:00Z' },
    { id: 'con_19', name: 'TrueNorth Marketing Agency', email: 'pay@truenorthmarketing.co.nz', phone: '+64 9 302 5500', billingAddress: { street: '15 Shortland Street, Level 3', city: 'Auckland', region: 'Auckland', postalCode: '1010', country: 'New Zealand' }, taxId: 'NZ-80-888-999', contactType: 'customer', createdAt: '2024-07-22T11:15:00Z' },
    { id: 'con_20', name: 'Heritage Craft Brewery', email: 'admin@heritagebrew.co.nz', phone: '+64 3 477 6600', billingAddress: { street: '330 Cumberland Street', city: 'Dunedin', region: 'Otago', postalCode: '9016', country: 'New Zealand' }, taxId: 'NZ-90-999-000', contactType: 'customer', createdAt: '2024-11-15T08:00:00Z' },
    { id: 'con_21', name: 'CloudBridge Software', email: 'ap@cloudbridge.com.au', phone: '+61 2 9876 5432', billingAddress: { street: '100 George Street, Level 20', city: 'Sydney', region: 'NSW', postalCode: '2000', country: 'Australia' }, taxId: 'AU-51-234-567-890', contactType: 'customer', createdAt: '2024-05-15T07:30:00Z' },
    { id: 'con_22', name: 'Meridian Health Clinic', email: 'billing@meridianhealth.co.nz', phone: '+64 9 522 8800', billingAddress: { street: '58 Remuera Road', city: 'Auckland', region: 'Auckland', postalCode: '1050', country: 'New Zealand' }, taxId: 'NZ-12-123-456', contactType: 'customer', createdAt: '2024-09-01T10:30:00Z' },
    { id: 'con_23', name: 'Redwood Property Management', email: 'accounts@redwoodpm.co.nz', phone: '+64 9 415 3300', billingAddress: { street: '8 Fred Thomas Drive', city: 'Auckland', region: 'Auckland', postalCode: '0632', country: 'New Zealand' }, taxId: 'NZ-13-234-567', contactType: 'customer', createdAt: '2024-10-10T14:20:00Z' },
    { id: 'con_24', name: 'Atlas Import/Export Ltd', email: 'finance@atlasimport.co.nz', phone: '+64 9 255 7700', billingAddress: { street: '14 Osterley Way', city: 'Auckland', region: 'Auckland', postalCode: '2104', country: 'New Zealand' }, taxId: 'NZ-14-345-678', contactType: 'customer', createdAt: '2024-06-18T09:00:00Z' },
    { id: 'con_25', name: 'Velocity Sports Equipment', email: 'orders@velocitysports.co.nz', phone: '+64 7 839 4400', billingAddress: { street: '55 Ward Street', city: 'Hamilton', region: 'Waikato', postalCode: '3204', country: 'New Zealand' }, taxId: 'NZ-15-456-789', contactType: 'customer', createdAt: '2024-08-28T11:00:00Z' },
];

const TAX_RATES = [
    { id: 'tax_1', name: 'GST on Income (15%)', rate: 15, isDefault: true },
    { id: 'tax_2', name: 'GST on Expenses (15%)', rate: 15, isDefault: false },
    { id: 'tax_3', name: 'No GST (0%)', rate: 0, isDefault: false },
    { id: 'tax_4', name: 'GST on Imports (15%)', rate: 0, isDefault: false },
    { id: 'tax_5', name: 'Zero Rated (0%)', rate: 0, isDefault: false },
    { id: 'tax_6', name: 'Exempt (0%)', rate: 0, isDefault: false },
    { id: 'tax_7', name: 'AU GST on Income (10%)', rate: 10, isDefault: false },
    { id: 'tax_8', name: 'US Sales Tax (8.5%)', rate: 8.5, isDefault: false },
];

const ACCOUNT_CODES = [
    { id: 'acc_1', code: '200', name: 'Sales', type: 'Revenue' },
    { id: 'acc_2', code: '210', name: 'Interest Income', type: 'Revenue' },
    { id: 'acc_3', code: '260', name: 'Other Revenue', type: 'Revenue' },
    { id: 'acc_4', code: '270', name: 'Consulting Revenue', type: 'Revenue' },
    { id: 'acc_5', code: '280', name: 'Service Revenue', type: 'Revenue' },
    { id: 'acc_6', code: '290', name: 'Subscription Revenue', type: 'Revenue' },
    { id: 'acc_7', code: '300', name: 'Licensing Revenue', type: 'Revenue' },
    { id: 'acc_8', code: '310', name: 'Training Revenue', type: 'Revenue' },
    { id: 'acc_9', code: '320', name: 'Rental Revenue', type: 'Revenue' },
    { id: 'acc_10', code: '400', name: 'Advertising', type: 'Expense' },
    { id: 'acc_11', code: '410', name: 'Bank Fees', type: 'Expense' },
    { id: 'acc_12', code: '420', name: 'Cleaning', type: 'Expense' },
    { id: 'acc_13', code: '460', name: 'Printing & Stationery', type: 'Expense' },
    { id: 'acc_14', code: '470', name: 'Rent', type: 'Expense' },
    { id: 'acc_15', code: '489', name: 'Software Licenses', type: 'Expense' },
];

const BANK_ACCOUNTS = [
    { id: 'bank_1', name: 'Business Cheque Account', accountNumber: '12-3456-0012345-00', currency: 'NZD' },
    { id: 'bank_2', name: 'Business Savings Account', accountNumber: '12-3456-0012345-01', currency: 'NZD' },
    { id: 'bank_3', name: 'USD Holding Account', accountNumber: '12-3456-0012345-02', currency: 'USD' },
    { id: 'bank_4', name: 'AUD Holding Account', accountNumber: '12-3456-0012345-03', currency: 'AUD' },
    { id: 'bank_5', name: 'Credit Card - Visa', accountNumber: '****-****-****-4532', currency: 'NZD' },
];

const CURRENCIES = [
    { code: 'NZD', name: 'New Zealand Dollar', symbol: '$' },
    { code: 'AUD', name: 'Australian Dollar', symbol: 'A$' },
    { code: 'USD', name: 'United States Dollar', symbol: 'US$' },
    { code: 'GBP', name: 'British Pound', symbol: '\u00a3' },
    { code: 'EUR', name: 'Euro', symbol: '\u20ac' },
    { code: 'CAD', name: 'Canadian Dollar', symbol: 'C$' },
    { code: 'JPY', name: 'Japanese Yen', symbol: '\u00a5' },
    { code: 'SGD', name: 'Singapore Dollar', symbol: 'S$' },
    { code: 'HKD', name: 'Hong Kong Dollar', symbol: 'HK$' },
    { code: 'CNY', name: 'Chinese Yuan', symbol: '\u00a5' },
    { code: 'FJD', name: 'Fijian Dollar', symbol: 'FJ$' },
];

const BRANDING_THEMES = [
    { id: 'theme_1', name: 'Standard', isDefault: true },
    { id: 'theme_2', name: 'Professional Blue', isDefault: false },
    { id: 'theme_3', name: 'Minimal Clean', isDefault: false },
    { id: 'theme_4', name: 'Bold Corporate', isDefault: false },
];

const DEFAULT_SETTINGS = {
    defaultDueDateTerms: '20',
    defaultDueDateTermsType: 'days_after_invoice',
    defaultTaxRateId: 'tax_1',
    invoiceNumberPrefix: 'INV-',
    invoiceNumberNextNumber: 121,
    invoiceNumberPadding: 4,
    defaultBrandingThemeId: 'theme_1',
    defaultEmailSubject: 'Invoice {InvoiceNumber} from Kiwi Consulting Ltd',
    defaultEmailBody: 'Hi {ContactName},\n\nPlease find attached invoice {InvoiceNumber} for {Total} due on {DueDate}.\n\nIf you have any questions, please get in touch.\n\nKind regards,\nKiwi Consulting Ltd',
    latePenaltyEnabled: false,
    latePenaltyRate: 1.5,
    latePenaltyFrequency: 'monthly',
    companyName: 'Kiwi Consulting Ltd',
    companyEmail: 'accounts@kiwiconsulting.co.nz',
    companyPhone: '+64 9 555 0100',
    companyAddress: '25 Queen Street, Level 5, Auckland 1010, New Zealand',
    companyTaxId: 'NZ-12-345-678',
};

/* ---- Deterministic invoice generation ---- */
function _buildSeedInvoices() {
    const _descriptions = [
        ['Website design and development', 'UX/UI consultation session', 'SEO audit and optimization report', 'Content management system setup', 'Monthly hosting and maintenance'],
        ['IT infrastructure assessment', 'Network security audit', 'Cloud migration services', 'Database optimization', 'Help desk support - monthly retainer'],
        ['Annual accounting software license', 'Quarterly bookkeeping services', 'Financial year-end preparation', 'Payroll processing - monthly', 'Tax compliance review'],
        ['Marketing strategy consultation', 'Social media campaign management', 'Brand identity design package', 'Email marketing setup', 'Google Ads management - monthly'],
        ['Staff training workshop - 2 days', 'Leadership development program', 'Health & safety certification course', 'Software onboarding training', 'Team building event coordination'],
        ['Office fit-out consultation', 'Interior design services', 'Furniture supply and installation', 'Project management - Phase 1', 'Site inspection and reporting'],
        ['Legal document review', 'Contract drafting services', 'Compliance advisory - quarterly', 'Intellectual property registration', 'Employment agreement preparation'],
        ['Environmental impact assessment', 'Waste management consultation', 'Carbon footprint audit', 'Sustainability report preparation', 'Water quality testing services'],
        ['Equipment rental - excavator (5 days)', 'Safety equipment supply', 'Vehicle fleet maintenance', 'Warehouse storage - monthly', 'Freight and logistics services'],
        ['Catering services - corporate event', 'Event planning and coordination', 'Venue hire - conference room', 'Photography services - half day', 'Audio/visual equipment rental'],
    ];
    const _unitPrices = [75, 95, 120, 150, 180, 200, 250, 300, 350, 450, 500, 750, 1000, 1200, 1500, 2000, 2500, 45, 60, 85];
    const _quantities = [1, 1, 1, 2, 2, 3, 4, 5, 8, 10, 12, 15, 20, 0.5, 1.5, 2.5, 24, 40, 100, 6];
    const _references = ['PO-2025-001', 'PO-2025-002', 'PO-2025-003', 'REF-88421', 'REF-77302', 'QUO-2026-015', 'QUO-2026-018', 'JOB-4455', 'JOB-4460', 'WO-12340', 'WO-12355', 'PROJ-ALPHA', 'PROJ-BETA', 'PROJ-GAMMA', 'SO-99001', 'SO-99015', '', '', '', '', '', '', '', '', ''];

    // Deterministic seeded random
    let _seed = 42;
    function rand() { _seed = (_seed * 1664525 + 1013904223) & 0x7FFFFFFF; return _seed / 0x7FFFFFFF; }
    function pick(arr) { return arr[Math.floor(rand() * arr.length)]; }
    function pickIdx(arr) { return Math.floor(rand() * arr.length); }
    function dateStr(y, m, d) { return y + '-' + String(m).padStart(2,'0') + '-' + String(d).padStart(2,'0'); }
    function isoStr(y, m, d, h, mi) { return dateStr(y,m,d) + 'T' + String(h||9).padStart(2,'0') + ':' + String(mi||0).padStart(2,'0') + ':00Z'; }

    const invoices = [];
    const payments = [];
    let liCounter = 1;
    let payCounter = 1;

    // Status distribution: 12 draft, 10 awaiting_approval, 30 awaiting_payment, 42 paid, 14 overdue, 5 voided, 7 partially paid (awaiting_payment with partial)
    const statusPool = [];
    for (let i = 0; i < 12; i++) statusPool.push('draft');
    for (let i = 0; i < 10; i++) statusPool.push('awaiting_approval');
    for (let i = 0; i < 30; i++) statusPool.push('awaiting_payment');
    for (let i = 0; i < 42; i++) statusPool.push('paid');
    for (let i = 0; i < 14; i++) statusPool.push('overdue');
    for (let i = 0; i < 5; i++) statusPool.push('voided');
    // Shuffle
    for (let i = statusPool.length - 1; i > 0; i--) {
        const j = Math.floor(rand() * (i + 1));
        [statusPool[i], statusPool[j]] = [statusPool[j], statusPool[i]];
    }

    for (let idx = 0; idx < 113; idx++) {
        const invNum = 'INV-' + String(idx + 1).padStart(4, '0');
        const status = statusPool[idx % statusPool.length];
        const contactId = CONTACTS[idx % CONTACTS.length].id;

        // Dates: spread over Oct 2025 to Mar 2026
        const monthOffset = Math.floor(rand() * 6); // 0-5 months back from March 2026
        const baseMonth = 3 - monthOffset; // March=3 back to Oct=-2
        let issueYear = 2026;
        let issueMonth = baseMonth;
        if (issueMonth <= 0) { issueMonth += 12; issueYear = 2025; }
        const issueDay = 1 + Math.floor(rand() * 28);
        const issueDate = dateStr(issueYear, issueMonth, issueDay);
        const issueISO = isoStr(issueYear, issueMonth, issueDay, 8 + Math.floor(rand() * 10), Math.floor(rand() * 60));

        // Due date: 7, 14, 20, or 30 days after issue
        const dueDays = [7, 14, 20, 30][Math.floor(rand() * 4)];
        const dueD = new Date(issueYear, issueMonth - 1, issueDay + dueDays);
        const dueDate = dateStr(dueD.getFullYear(), dueD.getMonth() + 1, dueD.getDate());

        // Currency: mostly NZD, some AUD/USD
        const currRand = rand();
        let currency = 'NZD';
        if (currRand > 0.85) currency = 'AUD';
        else if (currRand > 0.78) currency = 'USD';

        // Line items: 1-5
        const numLines = 1 + Math.floor(rand() * 4);
        const descGroup = _descriptions[pickIdx(_descriptions)];
        const lineItems = [];
        let subtotal = 0;
        for (let li = 0; li < numLines; li++) {
            const desc = descGroup[li % descGroup.length];
            const qty = _quantities[pickIdx(_quantities)];
            const price = _unitPrices[pickIdx(_unitPrices)];
            const lineTotal = Math.round(qty * price * 100) / 100;
            subtotal += lineTotal;
            const taxRateId = rand() > 0.15 ? 'tax_1' : 'tax_3';
            const accountIdx = Math.floor(rand() * 9); // first 9 are revenue
            lineItems.push({
                id: 'li_' + liCounter++,
                description: desc,
                quantity: qty,
                unitPrice: price,
                taxRateId: taxRateId,
                accountCode: ACCOUNT_CODES[accountIdx].code,
                lineTotal: lineTotal
            });
        }
        subtotal = Math.round(subtotal * 100) / 100;

        // Calculate tax
        let taxTotal = 0;
        lineItems.forEach(li => {
            const rate = TAX_RATES.find(t => t.id === li.taxRateId);
            if (rate) taxTotal += li.lineTotal * (rate.rate / 100);
        });
        taxTotal = Math.round(taxTotal * 100) / 100;
        const total = Math.round((subtotal + taxTotal) * 100) / 100;

        // Reference
        const reference = _references[idx % _references.length];

        // Notes
        const noteOptions = ['', '', '', '', 'Payment due within stated terms.', 'Please reference invoice number on all payments.', 'Thank you for your business.', 'Prices are exclusive of GST unless stated.', ''];
        const notes = pick(noteOptions);

        // Activity
        const activity = [{ type: 'created', date: issueISO, user: 'System', detail: 'Invoice created' }];

        let sentAt = null;
        let paidAt = null;
        let voidedAt = null;
        let amountPaid = 0;

        if (status === 'awaiting_approval') {
            // No additional activity
        } else if (status === 'awaiting_payment') {
            const sentDate = new Date(issueYear, issueMonth - 1, issueDay + 1 + Math.floor(rand() * 3));
            sentAt = isoStr(sentDate.getFullYear(), sentDate.getMonth() + 1, sentDate.getDate(), 10, 30);
            activity.push({ type: 'approved', date: sentAt, user: 'System', detail: 'Invoice approved' });
            activity.push({ type: 'sent', date: sentAt, user: 'System', detail: 'Email sent to ' + CONTACTS.find(c => c.id === contactId).email });

            // Some have partial payments
            if (rand() > 0.75) {
                const partialAmt = Math.round(total * (0.2 + rand() * 0.5) * 100) / 100;
                amountPaid = partialAmt;
                const payDate = new Date(sentDate.getTime() + (3 + Math.floor(rand() * 10)) * 86400000);
                const payISO = isoStr(payDate.getFullYear(), payDate.getMonth() + 1, payDate.getDate(), 14, 0);
                payments.push({
                    id: 'pay_' + payCounter++,
                    invoiceId: 'inv_' + (idx + 1),
                    date: dateStr(payDate.getFullYear(), payDate.getMonth() + 1, payDate.getDate()),
                    amount: partialAmt,
                    bankAccountId: 'bank_1',
                    reference: 'PARTIAL-' + invNum,
                    note: 'Partial payment received',
                    exchangeRate: currency === 'NZD' ? 1 : (currency === 'AUD' ? 1.08 : 1.58)
                });
                activity.push({ type: 'payment', date: payISO, user: 'System', detail: 'Payment of $' + partialAmt.toFixed(2) + ' received' });
            }
        } else if (status === 'paid') {
            const sentDate = new Date(issueYear, issueMonth - 1, issueDay + 1);
            sentAt = isoStr(sentDate.getFullYear(), sentDate.getMonth() + 1, sentDate.getDate(), 9, 15);
            activity.push({ type: 'approved', date: sentAt, user: 'System', detail: 'Invoice approved' });
            activity.push({ type: 'sent', date: sentAt, user: 'System', detail: 'Email sent to ' + CONTACTS.find(c => c.id === contactId).email });

            const payDate = new Date(sentDate.getTime() + (2 + Math.floor(rand() * 15)) * 86400000);
            paidAt = isoStr(payDate.getFullYear(), payDate.getMonth() + 1, payDate.getDate(), 11, 0);
            amountPaid = total;
            payments.push({
                id: 'pay_' + payCounter++,
                invoiceId: 'inv_' + (idx + 1),
                date: dateStr(payDate.getFullYear(), payDate.getMonth() + 1, payDate.getDate()),
                amount: total,
                bankAccountId: currency === 'AUD' ? 'bank_4' : (currency === 'USD' ? 'bank_3' : 'bank_1'),
                reference: invNum,
                note: '',
                exchangeRate: currency === 'NZD' ? 1 : (currency === 'AUD' ? 1.08 : 1.58)
            });
            activity.push({ type: 'payment', date: paidAt, user: 'System', detail: 'Full payment of $' + total.toFixed(2) + ' received' });
        } else if (status === 'overdue') {
            const sentDate = new Date(issueYear, issueMonth - 1, issueDay + 1);
            sentAt = isoStr(sentDate.getFullYear(), sentDate.getMonth() + 1, sentDate.getDate(), 10, 0);
            activity.push({ type: 'approved', date: sentAt, user: 'System', detail: 'Invoice approved' });
            activity.push({ type: 'sent', date: sentAt, user: 'System', detail: 'Email sent to ' + CONTACTS.find(c => c.id === contactId).email });
        } else if (status === 'voided') {
            const voidDate = new Date(issueYear, issueMonth - 1, issueDay + 5 + Math.floor(rand() * 10));
            voidedAt = isoStr(voidDate.getFullYear(), voidDate.getMonth() + 1, voidDate.getDate(), 14, 30);
            activity.push({ type: 'voided', date: voidedAt, user: 'System', detail: 'Invoice voided' });
        }

        const amountDue = Math.round((total - amountPaid) * 100) / 100;

        invoices.push({
            id: 'inv_' + (idx + 1),
            invoiceNumber: invNum,
            reference: reference,
            contactId: contactId,
            status: status,
            issueDate: issueDate,
            dueDate: dueDate,
            currency: currency,
            lineItems: lineItems,
            subtotal: subtotal,
            taxTotal: taxTotal,
            total: total,
            amountPaid: amountPaid,
            amountDue: amountDue,
            notes: notes,
            brandingThemeId: pick(BRANDING_THEMES).id,
            createdAt: issueISO,
            updatedAt: issueISO,
            sentAt: sentAt,
            paidAt: paidAt,
            voidedAt: voidedAt,
            activity: activity
        });
    }

    return { invoices, payments };
}

const _seedResult = _buildSeedInvoices();
const INVOICES = _seedResult.invoices;
const PAYMENTS = _seedResult.payments;
