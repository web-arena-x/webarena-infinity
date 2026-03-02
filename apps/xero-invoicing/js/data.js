const SEED_DATA_VERSION = 1;

const CURRENT_USER = {
  id: 'usr_001',
  name: 'Sarah Mitchell',
  email: 'sarah@democo.com',
  role: 'Advisor',
  organization: {
    name: 'Demo Company (AU)',
    legalName: 'Demo Company Pty Ltd',
    taxNumber: 'ABN 12 345 678 901',
    baseCurrency: 'AUD',
    country: 'Australia',
    address: '100 Queen Street, Melbourne VIC 3000, Australia',
    phone: '+61 3 9000 1234',
    email: 'accounts@democo.com',
    website: 'www.democo.com'
  }
};

const TAX_RATES = [
  { id: 'tax_gst', name: 'GST on Income', rate: 10, isDefault: true, type: 'output' },
  { id: 'tax_gst_free', name: 'GST Free Income', rate: 0, isDefault: false, type: 'output' },
  { id: 'tax_bas_excluded', name: 'BAS Excluded', rate: 0, isDefault: false, type: 'output' },
  { id: 'tax_gst_input', name: 'GST on Expenses', rate: 10, isDefault: true, type: 'input' },
  { id: 'tax_gst_free_exp', name: 'GST Free Expenses', rate: 0, isDefault: false, type: 'input' },
  { id: 'tax_exempt', name: 'Tax Exempt', rate: 0, isDefault: false, type: 'none' }
];

const ACCOUNTS = [
  { id: 'acc_200', code: '200', name: 'Sales', type: 'Revenue' },
  { id: 'acc_210', code: '210', name: 'Interest Income', type: 'Revenue' },
  { id: 'acc_215', code: '215', name: 'Other Revenue', type: 'Revenue' },
  { id: 'acc_260', code: '260', name: 'Consulting & Accounting', type: 'Revenue' },
  { id: 'acc_270', code: '270', name: 'Advertising Revenue', type: 'Revenue' },
  { id: 'acc_300', code: '300', name: 'Purchases', type: 'Direct Costs' },
  { id: 'acc_310', code: '310', name: 'Cost of Goods Sold', type: 'Direct Costs' },
  { id: 'acc_400', code: '400', name: 'Advertising', type: 'Expense' },
  { id: 'acc_404', code: '404', name: 'Bank Fees', type: 'Expense' },
  { id: 'acc_408', code: '408', name: 'Cleaning', type: 'Expense' },
  { id: 'acc_412', code: '412', name: 'Consulting & Accounting', type: 'Expense' },
  { id: 'acc_416', code: '416', name: 'Depreciation', type: 'Expense' },
  { id: 'acc_420', code: '420', name: 'Entertainment', type: 'Expense' },
  { id: 'acc_425', code: '425', name: 'Freight & Courier', type: 'Expense' },
  { id: 'acc_429', code: '429', name: 'General Expenses', type: 'Expense' },
  { id: 'acc_433', code: '433', name: 'Insurance', type: 'Expense' },
  { id: 'acc_437', code: '437', name: 'Interest Expense', type: 'Expense' },
  { id: 'acc_441', code: '441', name: 'Legal Expenses', type: 'Expense' },
  { id: 'acc_445', code: '445', name: 'Light, Power, Heating', type: 'Expense' },
  { id: 'acc_449', code: '449', name: 'Motor Vehicle Expenses', type: 'Expense' },
  { id: 'acc_453', code: '453', name: 'Office Expenses', type: 'Expense' },
  { id: 'acc_461', code: '461', name: 'Printing & Stationery', type: 'Expense' },
  { id: 'acc_469', code: '469', name: 'Rent', type: 'Expense' },
  { id: 'acc_473', code: '473', name: 'Repairs & Maintenance', type: 'Expense' },
  { id: 'acc_477', code: '477', name: 'Wages & Salaries', type: 'Expense' },
  { id: 'acc_800', code: '800', name: 'Accounts Receivable', type: 'Current Asset' },
  { id: 'acc_810', code: '810', name: 'Accounts Payable', type: 'Current Liability' },
  { id: 'acc_820', code: '820', name: 'GST', type: 'Current Liability' },
  { id: 'acc_090', code: '090', name: 'Business Bank Account', type: 'Bank' },
  { id: 'acc_091', code: '091', name: 'Business Savings Account', type: 'Bank' }
];

const TRACKING_CATEGORIES = [
  {
    id: 'track_region',
    name: 'Region',
    options: [
      { id: 'reg_nsw', name: 'New South Wales' },
      { id: 'reg_vic', name: 'Victoria' },
      { id: 'reg_qld', name: 'Queensland' },
      { id: 'reg_wa', name: 'Western Australia' },
      { id: 'reg_sa', name: 'South Australia' }
    ]
  },
  {
    id: 'track_dept',
    name: 'Department',
    options: [
      { id: 'dept_sales', name: 'Sales' },
      { id: 'dept_marketing', name: 'Marketing' },
      { id: 'dept_ops', name: 'Operations' },
      { id: 'dept_support', name: 'Support' },
      { id: 'dept_admin', name: 'Administration' }
    ]
  }
];

const CURRENCIES = [
  { code: 'AUD', name: 'Australian Dollar', symbol: '$' },
  { code: 'USD', name: 'US Dollar', symbol: 'US$' },
  { code: 'GBP', name: 'British Pound', symbol: '£' },
  { code: 'NZD', name: 'New Zealand Dollar', symbol: 'NZ$' },
  { code: 'EUR', name: 'Euro', symbol: '€' },
  { code: 'SGD', name: 'Singapore Dollar', symbol: 'S$' },
  { code: 'JPY', name: 'Japanese Yen', symbol: '¥' },
  { code: 'CAD', name: 'Canadian Dollar', symbol: 'CA$' },
  { code: 'HKD', name: 'Hong Kong Dollar', symbol: 'HK$' }
];

const BRANDING_THEMES = [
  { id: 'theme_standard', name: 'Standard', isDefault: true, logoUrl: '', paymentTerms: 'Payment is due within the specified terms. Please include the invoice number as a reference.', termsAndConditions: 'All amounts are in AUD unless otherwise stated. Late payments may incur interest at 1.5% per month.', showTaxNumber: true, showPaymentAdvice: true },
  { id: 'theme_professional', name: 'Professional Services', isDefault: false, logoUrl: '', paymentTerms: 'Net 30. Please remit payment to the bank account listed below.', termsAndConditions: 'Services are provided subject to our standard terms of engagement. Intellectual property remains with Demo Company until full payment is received.', showTaxNumber: true, showPaymentAdvice: true },
  { id: 'theme_simple', name: 'Simple Clean', isDefault: false, logoUrl: '', paymentTerms: 'Please pay by the due date shown above.', termsAndConditions: '', showTaxNumber: false, showPaymentAdvice: false },
  { id: 'theme_retail', name: 'Retail', isDefault: false, logoUrl: '', paymentTerms: 'Thank you for your purchase. No refunds after 30 days.', termsAndConditions: 'All sales are final unless the item is defective. Returns accepted within 30 days with original receipt.', showTaxNumber: true, showPaymentAdvice: false }
];

const ITEMS = [
  { id: 'item_001', code: 'DEV-HOUR', description: 'Software Development - Hourly Rate', unitPrice: 185.00, accountId: 'acc_200', taxRateId: 'tax_gst', isSold: true, isPurchased: false },
  { id: 'item_002', code: 'CONSULT-HR', description: 'Consulting Services - Per Hour', unitPrice: 250.00, accountId: 'acc_260', taxRateId: 'tax_gst', isSold: true, isPurchased: false },
  { id: 'item_003', code: 'PM-DAY', description: 'Project Management - Day Rate', unitPrice: 1400.00, accountId: 'acc_200', taxRateId: 'tax_gst', isSold: true, isPurchased: false },
  { id: 'item_004', code: 'HOSTING-MO', description: 'Cloud Hosting - Monthly', unitPrice: 299.00, accountId: 'acc_200', taxRateId: 'tax_gst', isSold: true, isPurchased: true },
  { id: 'item_005', code: 'SUPPORT-MO', description: 'Technical Support - Monthly Plan', unitPrice: 450.00, accountId: 'acc_200', taxRateId: 'tax_gst', isSold: true, isPurchased: false },
  { id: 'item_006', code: 'TRAINING', description: 'On-site Training - Per Day', unitPrice: 2200.00, accountId: 'acc_200', taxRateId: 'tax_gst', isSold: true, isPurchased: false },
  { id: 'item_007', code: 'DESIGN-HR', description: 'UI/UX Design - Hourly Rate', unitPrice: 165.00, accountId: 'acc_200', taxRateId: 'tax_gst', isSold: true, isPurchased: false },
  { id: 'item_008', code: 'LICENSE-AN', description: 'Software License - Annual', unitPrice: 1200.00, accountId: 'acc_200', taxRateId: 'tax_gst', isSold: true, isPurchased: false },
  { id: 'item_009', code: 'AUDIT', description: 'Security Audit - Fixed Fee', unitPrice: 5500.00, accountId: 'acc_260', taxRateId: 'tax_gst', isSold: true, isPurchased: false },
  { id: 'item_010', code: 'DATA-MIG', description: 'Data Migration Service', unitPrice: 3800.00, accountId: 'acc_200', taxRateId: 'tax_gst', isSold: true, isPurchased: false },
  { id: 'item_011', code: 'WIDGET-A', description: 'Widget Type A', unitPrice: 24.95, accountId: 'acc_200', taxRateId: 'tax_gst', isSold: true, isPurchased: true },
  { id: 'item_012', code: 'WIDGET-B', description: 'Widget Type B - Premium', unitPrice: 49.95, accountId: 'acc_200', taxRateId: 'tax_gst', isSold: true, isPurchased: true },
  { id: 'item_013', code: 'CABLE-USB', description: 'USB-C Cable 2m', unitPrice: 12.50, accountId: 'acc_200', taxRateId: 'tax_gst', isSold: true, isPurchased: true },
  { id: 'item_014', code: 'SETUP-FEE', description: 'Initial Setup Fee', unitPrice: 500.00, accountId: 'acc_200', taxRateId: 'tax_gst', isSold: true, isPurchased: false },
  { id: 'item_015', code: 'TRAVEL', description: 'Travel Expenses - Reimbursable', unitPrice: 0.00, accountId: 'acc_200', taxRateId: 'tax_gst_free', isSold: true, isPurchased: true }
];

const CONTACTS = [
  { id: 'con_001', name: 'Pinnacle Construction Group', email: 'accounts@pinnacleconstruction.com.au', phone: '+61 3 9123 4567', contactPerson: 'James Wright', address: '45 Collins Street, Melbourne VIC 3000', taxNumber: 'ABN 98 765 432 100', defaultThemeId: 'theme_standard', defaultDueDate: { type: 'daysAfterInvoice', days: 30 }, defaultTaxRateId: 'tax_gst', outstandingBalance: 14850.00, overdueBalance: 4950.00, isCustomer: true, isSupplier: false },
  { id: 'con_002', name: 'TechVault Solutions Pty Ltd', email: 'billing@techvault.com.au', phone: '+61 2 8000 5678', contactPerson: 'Mei-Lin Chen', address: '200 George Street, Sydney NSW 2000', taxNumber: 'ABN 11 222 333 444', defaultThemeId: 'theme_professional', defaultDueDate: { type: 'daysAfterInvoice', days: 14 }, defaultTaxRateId: 'tax_gst', outstandingBalance: 28160.00, overdueBalance: 0, isCustomer: true, isSupplier: true },
  { id: 'con_003', name: 'Greenfield Organics', email: 'info@greenfieldorganics.com.au', phone: '+61 7 3456 7890', contactPerson: 'Tom Gallagher', address: '88 Edward Street, Brisbane QLD 4000', taxNumber: 'ABN 55 666 777 888', defaultThemeId: 'theme_standard', defaultDueDate: { type: 'daysAfterInvoice', days: 30 }, defaultTaxRateId: 'tax_gst', outstandingBalance: 2497.50, overdueBalance: 0, isCustomer: true, isSupplier: false },
  { id: 'con_004', name: 'Horizon Media & Advertising', email: 'finance@horizonmedia.com.au', phone: '+61 2 9111 2222', contactPerson: 'Rachel Kumar', address: '15 Darling Drive, Sydney NSW 2000', taxNumber: 'ABN 33 444 555 666', defaultThemeId: 'theme_standard', defaultDueDate: { type: 'endOfFollowingMonth', days: 0 }, defaultTaxRateId: 'tax_gst', outstandingBalance: 0, overdueBalance: 0, isCustomer: true, isSupplier: true },
  { id: 'con_005', name: 'Baxter & Associates Legal', email: 'trust@baxterassociates.com.au', phone: '+61 3 9888 3333', contactPerson: 'David Baxter', address: '300 Bourke Street, Melbourne VIC 3000', taxNumber: 'ABN 22 111 999 888', defaultThemeId: 'theme_professional', defaultDueDate: { type: 'daysAfterInvoice', days: 7 }, defaultTaxRateId: 'tax_gst', outstandingBalance: 6050.00, overdueBalance: 6050.00, isCustomer: true, isSupplier: false },
  { id: 'con_006', name: 'Pacific Freight Lines', email: 'invoices@pacificfreight.com.au', phone: '+61 8 9222 4444', contactPerson: 'Sandra O\'Brien', address: '42 St Georges Terrace, Perth WA 6000', taxNumber: 'ABN 77 888 666 555', defaultThemeId: 'theme_standard', defaultDueDate: { type: 'daysAfterInvoice', days: 30 }, defaultTaxRateId: 'tax_gst', outstandingBalance: 3300.00, overdueBalance: 3300.00, isCustomer: true, isSupplier: true },
  { id: 'con_007', name: 'CloudNine Analytics', email: 'ap@cloudnine.io', phone: '+61 2 7777 8888', contactPerson: 'Aisha Patel', address: '101 Pitt Street, Sydney NSW 2000', taxNumber: 'ABN 44 333 222 111', defaultThemeId: 'theme_standard', defaultDueDate: { type: 'daysAfterInvoice', days: 14 }, defaultTaxRateId: 'tax_gst', outstandingBalance: 18645.00, overdueBalance: 0, isCustomer: true, isSupplier: false },
  { id: 'con_008', name: 'Murray River Winery', email: 'admin@murrayriverwinery.com.au', phone: '+61 3 5000 1111', contactPerson: 'Patrick Flynn', address: '1 Vine Lane, Echuca VIC 3564', taxNumber: 'ABN 99 000 111 222', defaultThemeId: 'theme_retail', defaultDueDate: { type: 'daysAfterInvoice', days: 30 }, defaultTaxRateId: 'tax_gst', outstandingBalance: 687.50, overdueBalance: 0, isCustomer: true, isSupplier: false },
  { id: 'con_009', name: 'Stellar Education Services', email: 'accounts@stellareducation.edu.au', phone: '+61 7 3111 5555', contactPerson: 'Fiona McAllister', address: '55 Ann Street, Brisbane QLD 4000', taxNumber: 'ABN 66 555 444 333', defaultThemeId: 'theme_standard', defaultDueDate: { type: 'daysAfterInvoice', days: 30 }, defaultTaxRateId: 'tax_gst_free', outstandingBalance: 0, overdueBalance: 0, isCustomer: true, isSupplier: false },
  { id: 'con_010', name: 'Redback Mining Supplies', email: 'purchasing@redbackmining.com.au', phone: '+61 8 9333 6666', contactPerson: 'Bruce Henderson', address: '78 Hay Street, Perth WA 6000', taxNumber: 'ABN 88 777 666 555', defaultThemeId: 'theme_standard', defaultDueDate: { type: 'daysAfterInvoice', days: 45 }, defaultTaxRateId: 'tax_gst', outstandingBalance: 0, overdueBalance: 0, isCustomer: true, isSupplier: true },
  { id: 'con_011', name: 'Coastal Living Interiors', email: 'studio@coastalinteriors.com.au', phone: '+61 2 4555 7777', contactPerson: 'Lisa Marchetti', address: '12 Campbell Parade, Bondi Beach NSW 2026', taxNumber: 'ABN 11 999 888 777', defaultThemeId: 'theme_simple', defaultDueDate: { type: 'daysAfterInvoice', days: 14 }, defaultTaxRateId: 'tax_gst', outstandingBalance: 4125.00, overdueBalance: 0, isCustomer: true, isSupplier: false },
  { id: 'con_012', name: 'Alpha Logistics International', email: 'finance@alphalogistics.com', phone: '+61 3 9444 8888', contactPerson: 'Yuki Tanaka', address: '500 Flinders Street, Melbourne VIC 3000', taxNumber: 'ABN 22 888 777 666', defaultThemeId: 'theme_standard', defaultDueDate: { type: 'daysAfterInvoice', days: 30 }, defaultTaxRateId: 'tax_gst', outstandingBalance: 11275.00, overdueBalance: 0, isCustomer: true, isSupplier: true },
  { id: 'con_013', name: 'Bright Spark Electrical', email: 'jobs@brightspark.com.au', phone: '+61 7 3222 9999', contactPerson: 'Danny Kowalski', address: '33 Creek Street, Brisbane QLD 4000', taxNumber: 'ABN 33 666 555 444', defaultThemeId: 'theme_standard', defaultDueDate: { type: 'daysAfterInvoice', days: 30 }, defaultTaxRateId: 'tax_gst', outstandingBalance: 0, overdueBalance: 0, isCustomer: true, isSupplier: true },
  { id: 'con_014', name: 'Summit Health Group', email: 'reception@summithealth.com.au', phone: '+61 2 9666 1111', contactPerson: 'Dr. Anita Sharma', address: '77 Macquarie Street, Sydney NSW 2000', taxNumber: 'ABN 44 555 444 333', defaultThemeId: 'theme_professional', defaultDueDate: { type: 'daysAfterInvoice', days: 14 }, defaultTaxRateId: 'tax_gst_free', outstandingBalance: 7700.00, overdueBalance: 0, isCustomer: true, isSupplier: false },
  { id: 'con_015', name: 'Outback Adventures Tourism', email: 'bookings@outbackadventures.com.au', phone: '+61 8 8555 2222', contactPerson: 'Steve Norris', address: '10 Todd Mall, Alice Springs NT 0870', taxNumber: 'ABN 55 444 333 222', defaultThemeId: 'theme_standard', defaultDueDate: { type: 'daysAfterInvoice', days: 30 }, defaultTaxRateId: 'tax_gst', outstandingBalance: 0, overdueBalance: 0, isCustomer: true, isSupplier: false },
  { id: 'con_016', name: 'Wellington & Partners Accounting', email: 'admin@wellingtonpartners.co.nz', phone: '+64 4 555 6789', contactPerson: 'Rebecca Thornton', address: '25 Lambton Quay, Wellington 6011, NZ', taxNumber: '', defaultThemeId: 'theme_professional', defaultDueDate: { type: 'daysAfterInvoice', days: 30 }, defaultTaxRateId: 'tax_gst_free', outstandingBalance: 0, overdueBalance: 0, isCustomer: true, isSupplier: true },
  { id: 'con_017', name: 'Northern Territory Power Corp', email: 'vendor.payments@ntpower.gov.au', phone: '+61 8 8999 3333', contactPerson: 'Greg Watkins', address: '1 Mitchell Street, Darwin NT 0800', taxNumber: 'ABN 66 333 222 111', defaultThemeId: 'theme_standard', defaultDueDate: { type: 'endOfFollowingMonth', days: 0 }, defaultTaxRateId: 'tax_gst', outstandingBalance: 0, overdueBalance: 0, isCustomer: true, isSupplier: false },
  { id: 'con_018', name: 'Sapphire Bay Resort', email: 'admin@sapphirebay.com.au', phone: '+61 7 4888 4444', contactPerson: 'Karen Whitfield', address: '1 Reef Drive, Cairns QLD 4870', taxNumber: 'ABN 77 222 111 000', defaultThemeId: 'theme_standard', defaultDueDate: { type: 'daysAfterInvoice', days: 30 }, defaultTaxRateId: 'tax_gst', outstandingBalance: 1650.00, overdueBalance: 0, isCustomer: true, isSupplier: false },
  { id: 'con_019', name: 'Metro Fabrication Works', email: 'quotes@metrofab.com.au', phone: '+61 3 9777 5555', contactPerson: 'Ian Drumond', address: '220 Ingles Street, Port Melbourne VIC 3207', taxNumber: 'ABN 88 111 000 999', defaultThemeId: 'theme_standard', defaultDueDate: { type: 'daysAfterInvoice', days: 30 }, defaultTaxRateId: 'tax_gst', outstandingBalance: 0, overdueBalance: 0, isCustomer: true, isSupplier: true },
  { id: 'con_020', name: 'Cascade Software Solutions', email: 'invoices@cascadesoftware.com.au', phone: '+61 2 6111 7777', contactPerson: 'Priya Mehta', address: '18 London Circuit, Canberra ACT 2601', taxNumber: 'ABN 99 888 777 666', defaultThemeId: 'theme_professional', defaultDueDate: { type: 'daysAfterInvoice', days: 14 }, defaultTaxRateId: 'tax_gst', outstandingBalance: 23100.00, overdueBalance: 0, isCustomer: true, isSupplier: false },
  { id: 'con_021', name: 'Harbour City Plumbing', email: 'office@harbourplumbing.com.au', phone: '+61 2 9888 6666', contactPerson: 'Marco Vitale', address: '95 Pyrmont Bridge Road, Pyrmont NSW 2009', taxNumber: 'ABN 10 777 666 555', defaultThemeId: 'theme_simple', defaultDueDate: { type: 'daysAfterInvoice', days: 30 }, defaultTaxRateId: 'tax_gst', outstandingBalance: 0, overdueBalance: 0, isCustomer: false, isSupplier: true },
  { id: 'con_022', name: 'Fresh Start Catering Co', email: 'hello@freshstartcatering.com.au', phone: '+61 3 9000 7777', contactPerson: 'Nicole Tran', address: '8 Hardware Lane, Melbourne VIC 3000', taxNumber: 'ABN 21 666 555 444', defaultThemeId: 'theme_standard', defaultDueDate: { type: 'daysAfterInvoice', days: 7 }, defaultTaxRateId: 'tax_gst', outstandingBalance: 0, overdueBalance: 0, isCustomer: true, isSupplier: false },
  { id: 'con_023', name: 'Vanguard Security Systems', email: 'billing@vanguardsecurity.com.au', phone: '+61 8 9111 8888', contactPerson: 'Robert Chang', address: '60 William Street, Perth WA 6000', taxNumber: 'ABN 32 555 444 333', defaultThemeId: 'theme_standard', defaultDueDate: { type: 'daysAfterInvoice', days: 30 }, defaultTaxRateId: 'tax_gst', outstandingBalance: 4950.00, overdueBalance: 0, isCustomer: true, isSupplier: false },
  { id: 'con_024', name: 'Southern Cross Veterinary', email: 'clinic@southerncrossvet.com.au', phone: '+61 3 9222 9999', contactPerson: 'Dr. Helen Brooks', address: '140 High Street, Kew VIC 3101', taxNumber: 'ABN 43 444 333 222', defaultThemeId: 'theme_standard', defaultDueDate: { type: 'daysAfterInvoice', days: 30 }, defaultTaxRateId: 'tax_gst_free', outstandingBalance: 0, overdueBalance: 0, isCustomer: true, isSupplier: false },
  { id: 'con_025', name: 'Atlas Engineering Consultants', email: 'projects@atlaseng.com.au', phone: '+61 7 3333 1111', contactPerson: 'Owen Stewart', address: '120 Eagle Street, Brisbane QLD 4000', taxNumber: 'ABN 54 333 222 111', defaultThemeId: 'theme_professional', defaultDueDate: { type: 'daysAfterInvoice', days: 30 }, defaultTaxRateId: 'tax_gst', outstandingBalance: 0, overdueBalance: 0, isCustomer: true, isSupplier: true }
];

const INVOICES = [
  { id: 'inv_001', number: 'INV-0042', contactId: 'con_001', status: 'paid', date: '2025-12-15', dueDate: '2026-01-14', reference: 'PO-8834', currency: 'AUD', brandingThemeId: 'theme_standard', taxMode: 'exclusive', lineItems: [
    { id: 'li_001', itemId: 'item_003', description: 'Project Management - Day Rate', quantity: 5, unitPrice: 1400.00, discountPercent: 0, accountId: 'acc_200', taxRateId: 'tax_gst', trackingRegion: 'reg_vic', trackingDept: 'dept_ops' },
    { id: 'li_002', itemId: 'item_001', description: 'Software Development - Hourly Rate', quantity: 40, unitPrice: 185.00, discountPercent: 0, accountId: 'acc_200', taxRateId: 'tax_gst', trackingRegion: 'reg_vic', trackingDept: 'dept_ops' }
  ], subtotal: 14400.00, taxTotal: 1440.00, total: 15840.00, amountDue: 0, amountPaid: 15840.00, payments: [{ id: 'pay_001', date: '2026-01-10', amount: 15840.00, reference: 'EFT-9920', accountId: 'acc_090' }], notes: [{ date: '2025-12-15T09:00:00Z', text: 'Invoice created', user: 'Sarah Mitchell' }, { date: '2025-12-15T09:05:00Z', text: 'Approved and sent to client', user: 'Sarah Mitchell' }, { date: '2026-01-10T14:30:00Z', text: 'Payment received via EFT', user: 'Sarah Mitchell' }], sentAt: '2025-12-15T09:05:00Z', title: '', summary: '' },

  { id: 'inv_002', number: 'INV-0043', contactId: 'con_002', status: 'paid', date: '2025-12-20', dueDate: '2026-01-03', reference: '', currency: 'AUD', brandingThemeId: 'theme_professional', taxMode: 'exclusive', lineItems: [
    { id: 'li_003', itemId: 'item_002', description: 'Consulting Services - Q4 Strategy Review', quantity: 16, unitPrice: 250.00, discountPercent: 0, accountId: 'acc_260', taxRateId: 'tax_gst', trackingRegion: 'reg_nsw', trackingDept: 'dept_sales' },
    { id: 'li_004', itemId: 'item_006', description: 'On-site Training - CRM System', quantity: 2, unitPrice: 2200.00, discountPercent: 10, accountId: 'acc_200', taxRateId: 'tax_gst', trackingRegion: 'reg_nsw', trackingDept: 'dept_sales' }
  ], subtotal: 7960.00, taxTotal: 796.00, total: 8756.00, amountDue: 0, amountPaid: 8756.00, payments: [{ id: 'pay_002', date: '2026-01-02', amount: 8756.00, reference: 'CHQ-4412', accountId: 'acc_090' }], notes: [{ date: '2025-12-20T11:00:00Z', text: 'Created from quote QU-0018', user: 'Sarah Mitchell' }], sentAt: '2025-12-20T11:30:00Z', title: '', summary: '' },

  { id: 'inv_003', number: 'INV-0044', contactId: 'con_003', status: 'paid', date: '2026-01-05', dueDate: '2026-02-04', reference: 'GF-2026-001', currency: 'AUD', brandingThemeId: 'theme_standard', taxMode: 'inclusive', lineItems: [
    { id: 'li_005', itemId: 'item_004', description: 'Cloud Hosting - January 2026', quantity: 1, unitPrice: 299.00, discountPercent: 0, accountId: 'acc_200', taxRateId: 'tax_gst', trackingRegion: 'reg_qld', trackingDept: '' },
    { id: 'li_006', itemId: 'item_005', description: 'Technical Support - January 2026', quantity: 1, unitPrice: 450.00, discountPercent: 0, accountId: 'acc_200', taxRateId: 'tax_gst', trackingRegion: 'reg_qld', trackingDept: '' }
  ], subtotal: 680.91, taxTotal: 68.09, total: 749.00, amountDue: 0, amountPaid: 749.00, payments: [{ id: 'pay_003', date: '2026-01-28', amount: 749.00, reference: 'DD-Auto', accountId: 'acc_090' }], notes: [], sentAt: '2026-01-05T08:00:00Z', title: '', summary: '' },

  { id: 'inv_004', number: 'INV-0045', contactId: 'con_001', status: 'awaiting_payment', date: '2026-01-20', dueDate: '2026-02-19', reference: 'PO-9012', currency: 'AUD', brandingThemeId: 'theme_standard', taxMode: 'exclusive', lineItems: [
    { id: 'li_007', itemId: 'item_001', description: 'Software Development - API Integration', quantity: 60, unitPrice: 185.00, discountPercent: 0, accountId: 'acc_200', taxRateId: 'tax_gst', trackingRegion: 'reg_vic', trackingDept: 'dept_ops' },
    { id: 'li_008', itemId: 'item_007', description: 'UI/UX Design - Dashboard Redesign', quantity: 20, unitPrice: 165.00, discountPercent: 0, accountId: 'acc_200', taxRateId: 'tax_gst', trackingRegion: 'reg_vic', trackingDept: 'dept_ops' }
  ], subtotal: 14400.00, taxTotal: 1440.00, total: 15840.00, amountDue: 10890.00, amountPaid: 4950.00, payments: [{ id: 'pay_004', date: '2026-02-10', amount: 4950.00, reference: 'EFT-0044', accountId: 'acc_090' }], notes: [{ date: '2026-01-20T10:00:00Z', text: 'Sent to client', user: 'Sarah Mitchell' }, { date: '2026-02-10T09:15:00Z', text: 'Partial payment received - $4,950', user: 'Sarah Mitchell' }], sentAt: '2026-01-20T10:00:00Z', title: '', summary: '' },

  { id: 'inv_005', number: 'INV-0046', contactId: 'con_005', status: 'awaiting_payment', date: '2026-01-25', dueDate: '2026-02-01', reference: '', currency: 'AUD', brandingThemeId: 'theme_professional', taxMode: 'exclusive', lineItems: [
    { id: 'li_009', itemId: 'item_009', description: 'Security Audit - Network Infrastructure', quantity: 1, unitPrice: 5500.00, discountPercent: 0, accountId: 'acc_260', taxRateId: 'tax_gst', trackingRegion: 'reg_vic', trackingDept: 'dept_ops' },
    { id: 'li_010', itemId: null, description: 'Travel & Accommodation - Site Visit', quantity: 1, unitPrice: 550.00, discountPercent: 0, accountId: 'acc_200', taxRateId: 'tax_gst', trackingRegion: 'reg_vic', trackingDept: 'dept_ops' }
  ], subtotal: 6050.00, taxTotal: 605.00, total: 6655.00, amountDue: 6655.00, amountPaid: 0, payments: [], notes: [], sentAt: '2026-01-25T14:00:00Z', title: '', summary: '' },

  { id: 'inv_006', number: 'INV-0047', contactId: 'con_007', status: 'awaiting_payment', date: '2026-02-01', dueDate: '2026-02-15', reference: 'CN-PROJ-2026-Q1', currency: 'AUD', brandingThemeId: 'theme_standard', taxMode: 'exclusive', lineItems: [
    { id: 'li_011', itemId: 'item_001', description: 'Software Development - Data Pipeline', quantity: 80, unitPrice: 185.00, discountPercent: 5, accountId: 'acc_200', taxRateId: 'tax_gst', trackingRegion: 'reg_nsw', trackingDept: 'dept_ops' },
    { id: 'li_012', itemId: 'item_002', description: 'Consulting - Architecture Review', quantity: 8, unitPrice: 250.00, discountPercent: 0, accountId: 'acc_260', taxRateId: 'tax_gst', trackingRegion: 'reg_nsw', trackingDept: 'dept_sales' },
    { id: 'li_013', itemId: 'item_004', description: 'Cloud Hosting - Feb 2026', quantity: 3, unitPrice: 299.00, discountPercent: 0, accountId: 'acc_200', taxRateId: 'tax_gst', trackingRegion: '', trackingDept: '' }
  ], subtotal: 16957.00, taxTotal: 1695.70, total: 18652.70, amountDue: 18652.70, amountPaid: 0, payments: [], notes: [{ date: '2026-02-01T08:30:00Z', text: 'Q1 project billing', user: 'Sarah Mitchell' }], sentAt: '2026-02-01T09:00:00Z', title: 'Q1 2026 Data Pipeline Project', summary: 'Development and consulting services for CloudNine data pipeline project, including hosting.' },

  { id: 'inv_007', number: 'INV-0048', contactId: 'con_006', status: 'awaiting_payment', date: '2026-02-05', dueDate: '2026-03-07', reference: 'PF-WO-3301', currency: 'AUD', brandingThemeId: 'theme_standard', taxMode: 'exclusive', lineItems: [
    { id: 'li_014', itemId: 'item_010', description: 'Data Migration - Legacy System to Cloud', quantity: 1, unitPrice: 3800.00, discountPercent: 0, accountId: 'acc_200', taxRateId: 'tax_gst', trackingRegion: 'reg_wa', trackingDept: 'dept_ops' }
  ], subtotal: 3800.00, taxTotal: 380.00, total: 4180.00, amountDue: 4180.00, amountPaid: 0, payments: [], notes: [], sentAt: '2026-02-05T11:00:00Z', title: '', summary: '' },

  { id: 'inv_008', number: 'INV-0049', contactId: 'con_011', status: 'awaiting_payment', date: '2026-02-10', dueDate: '2026-02-24', reference: '', currency: 'AUD', brandingThemeId: 'theme_simple', taxMode: 'inclusive', lineItems: [
    { id: 'li_015', itemId: 'item_011', description: 'Widget Type A', quantity: 50, unitPrice: 24.95, discountPercent: 0, accountId: 'acc_200', taxRateId: 'tax_gst', trackingRegion: 'reg_nsw', trackingDept: 'dept_sales' },
    { id: 'li_016', itemId: 'item_012', description: 'Widget Type B - Premium', quantity: 30, unitPrice: 49.95, discountPercent: 0, accountId: 'acc_200', taxRateId: 'tax_gst', trackingRegion: 'reg_nsw', trackingDept: 'dept_sales' },
    { id: 'li_017', itemId: 'item_013', description: 'USB-C Cable 2m', quantity: 20, unitPrice: 12.50, discountPercent: 0, accountId: 'acc_200', taxRateId: 'tax_gst', trackingRegion: 'reg_nsw', trackingDept: 'dept_sales' }
  ], subtotal: 3377.27, taxTotal: 337.73, total: 3715.00, amountDue: 3715.00, amountPaid: 0, payments: [], notes: [], sentAt: '2026-02-10T15:00:00Z', title: '', summary: '' },

  { id: 'inv_009', number: 'INV-0050', contactId: 'con_012', status: 'awaiting_payment', date: '2026-02-12', dueDate: '2026-03-14', reference: 'ALI-2026-Q1', currency: 'AUD', brandingThemeId: 'theme_standard', taxMode: 'exclusive', lineItems: [
    { id: 'li_018', itemId: 'item_002', description: 'Consulting - Supply Chain Optimization', quantity: 24, unitPrice: 250.00, discountPercent: 0, accountId: 'acc_260', taxRateId: 'tax_gst', trackingRegion: 'reg_vic', trackingDept: 'dept_sales' },
    { id: 'li_019', itemId: 'item_001', description: 'Software Development - Tracking Module', quantity: 30, unitPrice: 185.00, discountPercent: 0, accountId: 'acc_200', taxRateId: 'tax_gst', trackingRegion: 'reg_vic', trackingDept: 'dept_ops' },
    { id: 'li_020', itemId: 'item_014', description: 'Initial Setup Fee', quantity: 1, unitPrice: 500.00, discountPercent: 0, accountId: 'acc_200', taxRateId: 'tax_gst', trackingRegion: '', trackingDept: '' }
  ], subtotal: 12050.00, taxTotal: 1205.00, total: 13255.00, amountDue: 13255.00, amountPaid: 0, payments: [], notes: [], sentAt: '2026-02-12T10:00:00Z', title: 'Supply Chain Optimization Project', summary: '' },

  { id: 'inv_010', number: 'INV-0051', contactId: 'con_014', status: 'awaiting_payment', date: '2026-02-15', dueDate: '2026-03-01', reference: 'SHG-IT-2026', currency: 'AUD', brandingThemeId: 'theme_professional', taxMode: 'exclusive', lineItems: [
    { id: 'li_021', itemId: 'item_008', description: 'Software License - Practice Management System - Annual', quantity: 1, unitPrice: 1200.00, discountPercent: 0, accountId: 'acc_200', taxRateId: 'tax_gst_free', trackingRegion: 'reg_nsw', trackingDept: 'dept_sales' },
    { id: 'li_022', itemId: 'item_005', description: 'Technical Support - Annual Plan', quantity: 12, unitPrice: 450.00, discountPercent: 10, accountId: 'acc_200', taxRateId: 'tax_gst_free', trackingRegion: 'reg_nsw', trackingDept: 'dept_support' }
  ], subtotal: 6060.00, taxTotal: 0, total: 6060.00, amountDue: 6060.00, amountPaid: 0, payments: [], notes: [], sentAt: '2026-02-15T13:00:00Z', title: '', summary: '' },

  { id: 'inv_011', number: 'INV-0052', contactId: 'con_020', status: 'awaiting_payment', date: '2026-02-18', dueDate: '2026-03-04', reference: 'CSS-DEV-FEB', currency: 'AUD', brandingThemeId: 'theme_professional', taxMode: 'exclusive', lineItems: [
    { id: 'li_023', itemId: 'item_001', description: 'Software Development - Mobile App Features', quantity: 120, unitPrice: 185.00, discountPercent: 0, accountId: 'acc_200', taxRateId: 'tax_gst', trackingRegion: '', trackingDept: 'dept_ops' },
    { id: 'li_024', itemId: 'item_007', description: 'UI/UX Design - Mobile Screens', quantity: 16, unitPrice: 165.00, discountPercent: 0, accountId: 'acc_200', taxRateId: 'tax_gst', trackingRegion: '', trackingDept: 'dept_ops' }
  ], subtotal: 24840.00, taxTotal: 2484.00, total: 27324.00, amountDue: 27324.00, amountPaid: 0, payments: [], notes: [{ date: '2026-02-18T09:00:00Z', text: 'February development sprint billing', user: 'Sarah Mitchell' }], sentAt: '2026-02-18T09:30:00Z', title: 'February 2026 Development Sprint', summary: 'Mobile app feature development and UX design for Cascade Software.' },

  { id: 'inv_012', number: 'INV-0053', contactId: 'con_023', status: 'awaiting_payment', date: '2026-02-20', dueDate: '2026-03-22', reference: '', currency: 'AUD', brandingThemeId: 'theme_standard', taxMode: 'exclusive', lineItems: [
    { id: 'li_025', itemId: 'item_004', description: 'Cloud Hosting - February 2026', quantity: 1, unitPrice: 299.00, discountPercent: 0, accountId: 'acc_200', taxRateId: 'tax_gst', trackingRegion: 'reg_wa', trackingDept: '' },
    { id: 'li_026', itemId: 'item_005', description: 'Technical Support - February 2026', quantity: 1, unitPrice: 450.00, discountPercent: 0, accountId: 'acc_200', taxRateId: 'tax_gst', trackingRegion: 'reg_wa', trackingDept: 'dept_support' }
  ], subtotal: 749.00, taxTotal: 74.90, total: 823.90, amountDue: 823.90, amountPaid: 0, payments: [], notes: [], sentAt: '2026-02-20T16:00:00Z', title: '', summary: '' },

  { id: 'inv_013', number: 'INV-0054', contactId: 'con_018', status: 'awaiting_payment', date: '2026-02-22', dueDate: '2026-03-24', reference: 'SBR-WEB', currency: 'AUD', brandingThemeId: 'theme_standard', taxMode: 'exclusive', lineItems: [
    { id: 'li_027', itemId: 'item_001', description: 'Website Development - Booking System', quantity: 8, unitPrice: 185.00, discountPercent: 0, accountId: 'acc_200', taxRateId: 'tax_gst', trackingRegion: 'reg_qld', trackingDept: 'dept_ops' },
    { id: 'li_028', itemId: 'item_014', description: 'Initial Setup Fee', quantity: 1, unitPrice: 500.00, discountPercent: 0, accountId: 'acc_200', taxRateId: 'tax_gst', trackingRegion: 'reg_qld', trackingDept: '' }
  ], subtotal: 1980.00, taxTotal: 198.00, total: 2178.00, amountDue: 2178.00, amountPaid: 0, payments: [], notes: [], sentAt: '2026-02-22T10:00:00Z', title: '', summary: '' },

  { id: 'inv_014', number: 'INV-0055', contactId: 'con_002', status: 'awaiting_payment', date: '2026-02-25', dueDate: '2026-03-11', reference: 'TV-Q1-2026', currency: 'AUD', brandingThemeId: 'theme_professional', taxMode: 'exclusive', lineItems: [
    { id: 'li_029', itemId: 'item_001', description: 'Software Development - Cloud Migration Phase 2', quantity: 100, unitPrice: 185.00, discountPercent: 0, accountId: 'acc_200', taxRateId: 'tax_gst', trackingRegion: 'reg_nsw', trackingDept: 'dept_ops' },
    { id: 'li_030', itemId: 'item_003', description: 'Project Management - Migration Oversight', quantity: 10, unitPrice: 1400.00, discountPercent: 0, accountId: 'acc_200', taxRateId: 'tax_gst', trackingRegion: 'reg_nsw', trackingDept: 'dept_ops' },
    { id: 'li_031', itemId: 'item_009', description: 'Security Audit - Post-Migration', quantity: 1, unitPrice: 5500.00, discountPercent: 0, accountId: 'acc_260', taxRateId: 'tax_gst', trackingRegion: 'reg_nsw', trackingDept: 'dept_ops' }
  ], subtotal: 38000.00, taxTotal: 3800.00, total: 41800.00, amountDue: 41800.00, amountPaid: 0, payments: [], notes: [], sentAt: '2026-02-25T08:00:00Z', title: 'Cloud Migration Phase 2', summary: 'Complete cloud migration including development, project management, and security audit.' },

  { id: 'inv_015', number: 'INV-0056', contactId: 'con_004', status: 'awaiting_approval', date: '2026-02-27', dueDate: '2026-03-31', reference: 'HM-DIGITAL-Q1', currency: 'AUD', brandingThemeId: 'theme_standard', taxMode: 'exclusive', lineItems: [
    { id: 'li_032', itemId: 'item_007', description: 'UI/UX Design - Campaign Landing Pages', quantity: 32, unitPrice: 165.00, discountPercent: 0, accountId: 'acc_200', taxRateId: 'tax_gst', trackingRegion: 'reg_nsw', trackingDept: 'dept_ops' },
    { id: 'li_033', itemId: 'item_001', description: 'Software Development - Analytics Dashboard', quantity: 24, unitPrice: 185.00, discountPercent: 0, accountId: 'acc_200', taxRateId: 'tax_gst', trackingRegion: 'reg_nsw', trackingDept: 'dept_ops' }
  ], subtotal: 9720.00, taxTotal: 972.00, total: 10692.00, amountDue: 10692.00, amountPaid: 0, payments: [], notes: [{ date: '2026-02-27T14:00:00Z', text: 'Submitted for manager approval', user: 'Sarah Mitchell' }], sentAt: null, title: 'Q1 Digital Campaign Work', summary: '' },

  { id: 'inv_016', number: 'INV-0057', contactId: 'con_009', status: 'awaiting_approval', date: '2026-02-28', dueDate: '2026-03-30', reference: '', currency: 'AUD', brandingThemeId: 'theme_standard', taxMode: 'exclusive', lineItems: [
    { id: 'li_034', itemId: 'item_006', description: 'On-site Training - LMS Platform', quantity: 3, unitPrice: 2200.00, discountPercent: 0, accountId: 'acc_200', taxRateId: 'tax_gst_free', trackingRegion: 'reg_qld', trackingDept: 'dept_support' }
  ], subtotal: 6600.00, taxTotal: 0, total: 6600.00, amountDue: 6600.00, amountPaid: 0, payments: [], notes: [], sentAt: null, title: '', summary: '' },

  { id: 'inv_017', number: 'INV-0058', contactId: 'con_008', status: 'draft', date: '2026-03-01', dueDate: '2026-03-31', reference: 'MRW-WEBSITE', currency: 'AUD', brandingThemeId: 'theme_retail', taxMode: 'inclusive', lineItems: [
    { id: 'li_035', itemId: 'item_001', description: 'Website Redesign - Homepage & Product Pages', quantity: 16, unitPrice: 185.00, discountPercent: 0, accountId: 'acc_200', taxRateId: 'tax_gst', trackingRegion: 'reg_vic', trackingDept: 'dept_ops' },
    { id: 'li_036', itemId: 'item_007', description: 'UI/UX Design - Brand Refresh', quantity: 8, unitPrice: 165.00, discountPercent: 0, accountId: 'acc_200', taxRateId: 'tax_gst', trackingRegion: 'reg_vic', trackingDept: 'dept_ops' }
  ], subtotal: 3890.91, taxTotal: 389.09, total: 4280.00, amountDue: 4280.00, amountPaid: 0, payments: [], notes: [], sentAt: null, title: 'Website Redesign', summary: '' },

  { id: 'inv_018', number: 'INV-0059', contactId: 'con_013', status: 'draft', date: '2026-03-01', dueDate: '2026-03-31', reference: '', currency: 'AUD', brandingThemeId: 'theme_standard', taxMode: 'exclusive', lineItems: [
    { id: 'li_037', itemId: 'item_004', description: 'Cloud Hosting - March 2026', quantity: 1, unitPrice: 299.00, discountPercent: 0, accountId: 'acc_200', taxRateId: 'tax_gst', trackingRegion: 'reg_qld', trackingDept: '' }
  ], subtotal: 299.00, taxTotal: 29.90, total: 328.90, amountDue: 328.90, amountPaid: 0, payments: [], notes: [], sentAt: null, title: '', summary: '' },

  { id: 'inv_019', number: 'INV-0060', contactId: 'con_010', status: 'draft', date: '2026-03-02', dueDate: '2026-04-16', reference: 'RB-CONSULT', currency: 'AUD', brandingThemeId: 'theme_standard', taxMode: 'exclusive', lineItems: [
    { id: 'li_038', itemId: 'item_002', description: 'Consulting - Mining Software Assessment', quantity: 8, unitPrice: 250.00, discountPercent: 0, accountId: 'acc_260', taxRateId: 'tax_gst', trackingRegion: 'reg_wa', trackingDept: 'dept_sales' },
    { id: 'li_039', itemId: 'item_015', description: 'Travel Expenses - Perth Site Visit', quantity: 1, unitPrice: 1250.00, discountPercent: 0, accountId: 'acc_200', taxRateId: 'tax_gst_free', trackingRegion: 'reg_wa', trackingDept: '' }
  ], subtotal: 3250.00, taxTotal: 200.00, total: 3450.00, amountDue: 3450.00, amountPaid: 0, payments: [], notes: [], sentAt: null, title: '', summary: '' },

  { id: 'inv_020', number: 'INV-0061', contactId: 'con_003', status: 'awaiting_payment', date: '2026-02-05', dueDate: '2026-03-07', reference: 'GF-2026-002', currency: 'AUD', brandingThemeId: 'theme_standard', taxMode: 'inclusive', lineItems: [
    { id: 'li_040', itemId: 'item_004', description: 'Cloud Hosting - February 2026', quantity: 1, unitPrice: 299.00, discountPercent: 0, accountId: 'acc_200', taxRateId: 'tax_gst', trackingRegion: 'reg_qld', trackingDept: '' },
    { id: 'li_041', itemId: 'item_005', description: 'Technical Support - February 2026', quantity: 1, unitPrice: 450.00, discountPercent: 0, accountId: 'acc_200', taxRateId: 'tax_gst', trackingRegion: 'reg_qld', trackingDept: '' },
    { id: 'li_042', itemId: 'item_001', description: 'Software Development - E-commerce Module', quantity: 8, unitPrice: 185.00, discountPercent: 0, accountId: 'acc_200', taxRateId: 'tax_gst', trackingRegion: 'reg_qld', trackingDept: 'dept_ops' }
  ], subtotal: 2226.36, taxTotal: 222.64, total: 2449.00, amountDue: 2449.00, amountPaid: 0, payments: [], notes: [], sentAt: '2026-02-05T10:00:00Z', title: '', summary: '' },

  { id: 'inv_021', number: 'INV-0062', contactId: 'con_007', status: 'awaiting_payment', date: '2026-02-20', dueDate: '2026-03-06', reference: 'CN-HOSTING-FEB', currency: 'AUD', brandingThemeId: 'theme_standard', taxMode: 'exclusive', lineItems: [
    { id: 'li_043', itemId: 'item_004', description: 'Cloud Hosting - Premium Tier - Feb 2026', quantity: 5, unitPrice: 299.00, discountPercent: 0, accountId: 'acc_200', taxRateId: 'tax_gst', trackingRegion: 'reg_nsw', trackingDept: '' },
    { id: 'li_044', itemId: 'item_005', description: 'Technical Support - Priority - Feb 2026', quantity: 1, unitPrice: 450.00, discountPercent: 0, accountId: 'acc_200', taxRateId: 'tax_gst', trackingRegion: 'reg_nsw', trackingDept: 'dept_support' }
  ], subtotal: 1945.00, taxTotal: 194.50, total: 2139.50, amountDue: 2139.50, amountPaid: 0, payments: [], notes: [], sentAt: '2026-02-20T11:00:00Z', title: '', summary: '' },

  { id: 'inv_022', number: 'INV-0063', contactId: 'con_011', status: 'paid', date: '2025-11-10', dueDate: '2025-11-24', reference: '', currency: 'AUD', brandingThemeId: 'theme_simple', taxMode: 'inclusive', lineItems: [
    { id: 'li_045', itemId: 'item_011', description: 'Widget Type A', quantity: 100, unitPrice: 24.95, discountPercent: 5, accountId: 'acc_200', taxRateId: 'tax_gst', trackingRegion: 'reg_nsw', trackingDept: 'dept_sales' }
  ], subtotal: 2154.09, taxTotal: 215.41, total: 2370.25, amountDue: 0, amountPaid: 2370.25, payments: [{ id: 'pay_005', date: '2025-11-22', amount: 2370.25, reference: 'PayPal-8843', accountId: 'acc_090' }], notes: [], sentAt: '2025-11-10T09:00:00Z', title: '', summary: '' },

  { id: 'inv_023', number: 'INV-0064', contactId: 'con_017', status: 'paid', date: '2025-10-01', dueDate: '2025-11-30', reference: 'NTP-2025-IT-004', currency: 'AUD', brandingThemeId: 'theme_standard', taxMode: 'exclusive', lineItems: [
    { id: 'li_046', itemId: 'item_002', description: 'Consulting Services - SCADA System Review', quantity: 40, unitPrice: 250.00, discountPercent: 0, accountId: 'acc_260', taxRateId: 'tax_gst', trackingRegion: '', trackingDept: 'dept_sales' },
    { id: 'li_047', itemId: 'item_009', description: 'Security Audit - SCADA Infrastructure', quantity: 2, unitPrice: 5500.00, discountPercent: 0, accountId: 'acc_260', taxRateId: 'tax_gst', trackingRegion: '', trackingDept: 'dept_ops' }
  ], subtotal: 21000.00, taxTotal: 2100.00, total: 23100.00, amountDue: 0, amountPaid: 23100.00, payments: [{ id: 'pay_006', date: '2025-11-28', amount: 23100.00, reference: 'EFT-GOV-2025-112', accountId: 'acc_090' }], notes: [], sentAt: '2025-10-01T08:00:00Z', title: 'SCADA System Review & Audit', summary: '' },

  { id: 'inv_024', number: 'INV-0065', contactId: 'con_015', status: 'voided', date: '2025-09-15', dueDate: '2025-10-15', reference: 'OAT-CAMP-01', currency: 'AUD', brandingThemeId: 'theme_standard', taxMode: 'exclusive', lineItems: [
    { id: 'li_048', itemId: 'item_001', description: 'Website Development - Booking Portal', quantity: 40, unitPrice: 185.00, discountPercent: 0, accountId: 'acc_200', taxRateId: 'tax_gst', trackingRegion: '', trackingDept: 'dept_ops' }
  ], subtotal: 7400.00, taxTotal: 740.00, total: 8140.00, amountDue: 0, amountPaid: 0, payments: [], notes: [{ date: '2025-10-20T10:00:00Z', text: 'Voided - project cancelled by client', user: 'Sarah Mitchell' }], sentAt: '2025-09-15T10:00:00Z', title: '', summary: '' },

  { id: 'inv_025', number: 'INV-0066', contactId: 'con_016', status: 'paid', date: '2025-11-01', dueDate: '2025-12-01', reference: 'WP-NZ-2025-Q4', currency: 'NZD', brandingThemeId: 'theme_professional', taxMode: 'exclusive', lineItems: [
    { id: 'li_049', itemId: 'item_002', description: 'Consulting - Tax Compliance Software Review', quantity: 12, unitPrice: 250.00, discountPercent: 0, accountId: 'acc_260', taxRateId: 'tax_gst_free', trackingRegion: '', trackingDept: 'dept_sales' }
  ], subtotal: 3000.00, taxTotal: 0, total: 3000.00, amountDue: 0, amountPaid: 3000.00, payments: [{ id: 'pay_007', date: '2025-11-25', amount: 3000.00, reference: 'NZEFT-4421', accountId: 'acc_090' }], notes: [], sentAt: '2025-11-01T08:00:00Z', title: '', summary: '' }
];

const QUOTES = [
  { id: 'quo_001', number: 'QU-0022', contactId: 'con_001', status: 'accepted', date: '2026-01-10', expiryDate: '2026-02-10', reference: 'PO-PENDING-9088', currency: 'AUD', brandingThemeId: 'theme_standard', taxMode: 'exclusive', lineItems: [
    { id: 'qli_001', itemId: 'item_001', description: 'Software Development - Phase 3 CRM Integration', quantity: 120, unitPrice: 185.00, discountPercent: 0, accountId: 'acc_200', taxRateId: 'tax_gst', trackingRegion: 'reg_vic', trackingDept: 'dept_ops' },
    { id: 'qli_002', itemId: 'item_003', description: 'Project Management', quantity: 15, unitPrice: 1400.00, discountPercent: 0, accountId: 'acc_200', taxRateId: 'tax_gst', trackingRegion: 'reg_vic', trackingDept: 'dept_ops' },
    { id: 'qli_003', itemId: 'item_006', description: 'On-site Training - CRM for Sales Team', quantity: 2, unitPrice: 2200.00, discountPercent: 0, accountId: 'acc_200', taxRateId: 'tax_gst', trackingRegion: 'reg_vic', trackingDept: '' }
  ], subtotal: 47600.00, taxTotal: 4760.00, total: 52360.00, title: 'CRM Integration - Phase 3', summary: 'Complete CRM integration including development, project management, and staff training.', terms: 'Payment terms: 50% upfront, 50% on completion. Pricing valid for 30 days.', notes: [{ date: '2026-01-15T09:00:00Z', text: 'Client accepted via online quote', user: 'System' }], sentAt: '2026-01-10T10:00:00Z', isInvoiced: false },

  { id: 'quo_002', number: 'QU-0023', contactId: 'con_010', status: 'sent', date: '2026-02-20', expiryDate: '2026-03-22', reference: '', currency: 'AUD', brandingThemeId: 'theme_standard', taxMode: 'exclusive', lineItems: [
    { id: 'qli_004', itemId: 'item_010', description: 'Data Migration - Mining Operations Database', quantity: 2, unitPrice: 3800.00, discountPercent: 0, accountId: 'acc_200', taxRateId: 'tax_gst', trackingRegion: 'reg_wa', trackingDept: 'dept_ops' },
    { id: 'qli_005', itemId: 'item_002', description: 'Consulting - Requirements Analysis', quantity: 16, unitPrice: 250.00, discountPercent: 0, accountId: 'acc_260', taxRateId: 'tax_gst', trackingRegion: 'reg_wa', trackingDept: 'dept_sales' },
    { id: 'qli_006', itemId: 'item_006', description: 'On-site Training - Data Systems', quantity: 1, unitPrice: 2200.00, discountPercent: 0, accountId: 'acc_200', taxRateId: 'tax_gst', trackingRegion: 'reg_wa', trackingDept: '' },
    { id: 'qli_007', itemId: 'item_015', description: 'Travel - Perth (2 trips)', quantity: 2, unitPrice: 1800.00, discountPercent: 0, accountId: 'acc_200', taxRateId: 'tax_gst_free', trackingRegion: 'reg_wa', trackingDept: '' }
  ], subtotal: 17400.00, taxTotal: 1380.00, total: 18780.00, title: 'Mining Operations Data Migration', summary: 'Comprehensive data migration from legacy systems to modern cloud infrastructure, including training and travel.', terms: '', notes: [], sentAt: '2026-02-20T14:00:00Z', isInvoiced: false },

  { id: 'quo_003', number: 'QU-0024', contactId: 'con_025', status: 'sent', date: '2026-02-25', expiryDate: '2026-03-27', reference: 'AEC-COLLAB', currency: 'AUD', brandingThemeId: 'theme_professional', taxMode: 'exclusive', lineItems: [
    { id: 'qli_008', itemId: 'item_001', description: 'Software Development - Collaboration Platform', quantity: 200, unitPrice: 185.00, discountPercent: 5, accountId: 'acc_200', taxRateId: 'tax_gst', trackingRegion: 'reg_qld', trackingDept: 'dept_ops' },
    { id: 'qli_009', itemId: 'item_007', description: 'UI/UX Design - Platform Interface', quantity: 40, unitPrice: 165.00, discountPercent: 0, accountId: 'acc_200', taxRateId: 'tax_gst', trackingRegion: 'reg_qld', trackingDept: 'dept_ops' },
    { id: 'qli_010', itemId: 'item_003', description: 'Project Management', quantity: 20, unitPrice: 1400.00, discountPercent: 0, accountId: 'acc_200', taxRateId: 'tax_gst', trackingRegion: 'reg_qld', trackingDept: 'dept_ops' }
  ], subtotal: 69750.00, taxTotal: 6975.00, total: 76725.00, title: 'Engineering Collaboration Platform', summary: 'Custom collaboration platform development for engineering teams.', terms: 'Milestone-based billing: 25% on kickoff, 25% at midpoint, 25% on UAT, 25% on go-live.', notes: [], sentAt: '2026-02-25T16:00:00Z', isInvoiced: false },

  { id: 'quo_004', number: 'QU-0025', contactId: 'con_022', status: 'draft', date: '2026-03-01', expiryDate: '2026-03-31', reference: '', currency: 'AUD', brandingThemeId: 'theme_standard', taxMode: 'inclusive', lineItems: [
    { id: 'qli_011', itemId: 'item_001', description: 'Website Development - Online Ordering System', quantity: 24, unitPrice: 185.00, discountPercent: 0, accountId: 'acc_200', taxRateId: 'tax_gst', trackingRegion: 'reg_vic', trackingDept: 'dept_ops' },
    { id: 'qli_012', itemId: 'item_014', description: 'Initial Setup Fee', quantity: 1, unitPrice: 500.00, discountPercent: 0, accountId: 'acc_200', taxRateId: 'tax_gst', trackingRegion: 'reg_vic', trackingDept: '' }
  ], subtotal: 4594.55, taxTotal: 459.45, total: 4940.00, title: 'Online Ordering System', summary: '', terms: '', notes: [], sentAt: null, isInvoiced: false },

  { id: 'quo_005', number: 'QU-0026', contactId: 'con_004', status: 'declined', date: '2026-01-15', expiryDate: '2026-02-14', reference: 'HM-VID-2026', currency: 'AUD', brandingThemeId: 'theme_standard', taxMode: 'exclusive', lineItems: [
    { id: 'qli_013', itemId: 'item_001', description: 'Video Streaming Platform Development', quantity: 160, unitPrice: 185.00, discountPercent: 0, accountId: 'acc_200', taxRateId: 'tax_gst', trackingRegion: 'reg_nsw', trackingDept: 'dept_ops' },
    { id: 'qli_014', itemId: 'item_004', description: 'Cloud Hosting - Video CDN - Monthly', quantity: 12, unitPrice: 299.00, discountPercent: 0, accountId: 'acc_200', taxRateId: 'tax_gst', trackingRegion: '', trackingDept: '' }
  ], subtotal: 33188.00, taxTotal: 3318.80, total: 36506.80, title: 'Video Streaming Platform', summary: '', terms: '', notes: [{ date: '2026-02-01T10:00:00Z', text: 'Declined - budget constraints', user: 'System' }], sentAt: '2026-01-15T11:00:00Z', isInvoiced: false },

  { id: 'quo_006', number: 'QU-0027', contactId: 'con_009', status: 'accepted', date: '2025-12-01', expiryDate: '2025-12-31', reference: 'SES-LMS', currency: 'AUD', brandingThemeId: 'theme_standard', taxMode: 'exclusive', lineItems: [
    { id: 'qli_015', itemId: 'item_006', description: 'On-site Training - LMS Platform (3 days)', quantity: 3, unitPrice: 2200.00, discountPercent: 0, accountId: 'acc_200', taxRateId: 'tax_gst_free', trackingRegion: 'reg_qld', trackingDept: 'dept_support' }
  ], subtotal: 6600.00, taxTotal: 0, total: 6600.00, title: 'LMS Training Program', summary: 'Three-day on-site training program for LMS administrators and content creators.', terms: '', notes: [{ date: '2025-12-10T14:00:00Z', text: 'Accepted by Fiona McAllister', user: 'System' }], sentAt: '2025-12-01T10:00:00Z', isInvoiced: true },

  { id: 'quo_007', number: 'QU-0028', contactId: 'con_019', status: 'sent', date: '2026-02-28', expiryDate: '2026-03-30', reference: 'MF-AUTO', currency: 'AUD', brandingThemeId: 'theme_standard', taxMode: 'exclusive', lineItems: [
    { id: 'qli_016', itemId: 'item_001', description: 'Automation Software Development', quantity: 60, unitPrice: 185.00, discountPercent: 0, accountId: 'acc_200', taxRateId: 'tax_gst', trackingRegion: 'reg_vic', trackingDept: 'dept_ops' },
    { id: 'qli_017', itemId: 'item_002', description: 'Consulting - Process Analysis', quantity: 8, unitPrice: 250.00, discountPercent: 0, accountId: 'acc_260', taxRateId: 'tax_gst', trackingRegion: 'reg_vic', trackingDept: 'dept_sales' }
  ], subtotal: 13100.00, taxTotal: 1310.00, total: 14410.00, title: 'Factory Automation Software', summary: '', terms: 'Net 30 from acceptance.', notes: [], sentAt: '2026-02-28T09:00:00Z', isInvoiced: false },

  { id: 'quo_008', number: 'QU-0029', contactId: 'con_012', status: 'accepted', date: '2026-02-10', expiryDate: '2026-03-10', reference: 'ALI-PHASE2', currency: 'AUD', brandingThemeId: 'theme_standard', taxMode: 'exclusive', lineItems: [
    { id: 'qli_018', itemId: 'item_001', description: 'Software Dev - Logistics Tracking Enhancement', quantity: 80, unitPrice: 185.00, discountPercent: 0, accountId: 'acc_200', taxRateId: 'tax_gst', trackingRegion: 'reg_vic', trackingDept: 'dept_ops' },
    { id: 'qli_019', itemId: 'item_008', description: 'Software License - Logistics Module - Annual', quantity: 1, unitPrice: 1200.00, discountPercent: 0, accountId: 'acc_200', taxRateId: 'tax_gst', trackingRegion: '', trackingDept: '' }
  ], subtotal: 16000.00, taxTotal: 1600.00, total: 17600.00, title: 'Logistics Tracking Phase 2', summary: '', terms: '', notes: [{ date: '2026-02-18T10:00:00Z', text: 'Accepted by Yuki Tanaka', user: 'System' }], sentAt: '2026-02-10T09:00:00Z', isInvoiced: false }
];

const CREDIT_NOTES = [
  { id: 'cn_001', number: 'CN-0008', contactId: 'con_001', status: 'paid', date: '2026-01-15', reference: 'Discount adjustment', currency: 'AUD', brandingThemeId: 'theme_standard', taxMode: 'exclusive', lineItems: [
    { id: 'cnli_001', itemId: null, description: 'Agreed volume discount - Q4 2025 project work', quantity: 1, unitPrice: 1000.00, discountPercent: 0, accountId: 'acc_200', taxRateId: 'tax_gst', trackingRegion: 'reg_vic', trackingDept: '' }
  ], subtotal: 1000.00, taxTotal: 100.00, total: 1100.00, remainingCredit: 0, allocations: [{ invoiceId: 'inv_004', invoiceNumber: 'INV-0045', amount: 1100.00, date: '2026-01-20' }], refunds: [], notes: [] },

  { id: 'cn_002', number: 'CN-0009', contactId: 'con_011', status: 'awaiting_payment', date: '2026-02-12', reference: 'Damaged goods return', currency: 'AUD', brandingThemeId: 'theme_simple', taxMode: 'inclusive', lineItems: [
    { id: 'cnli_002', itemId: 'item_012', description: 'Widget Type B - Premium (defective batch return)', quantity: 5, unitPrice: 49.95, discountPercent: 0, accountId: 'acc_200', taxRateId: 'tax_gst', trackingRegion: 'reg_nsw', trackingDept: 'dept_sales' }
  ], subtotal: 227.05, taxTotal: 22.70, total: 249.75, remainingCredit: 249.75, allocations: [], refunds: [], notes: [{ date: '2026-02-12T11:00:00Z', text: '5 units returned due to manufacturing defect', user: 'Sarah Mitchell' }] },

  { id: 'cn_003', number: 'CN-0010', contactId: 'con_002', status: 'paid', date: '2025-12-22', reference: 'Overcharge correction', currency: 'AUD', brandingThemeId: 'theme_professional', taxMode: 'exclusive', lineItems: [
    { id: 'cnli_003', itemId: 'item_002', description: 'Consulting rate correction - billed at $275 instead of $250', quantity: 8, unitPrice: 25.00, discountPercent: 0, accountId: 'acc_260', taxRateId: 'tax_gst', trackingRegion: 'reg_nsw', trackingDept: 'dept_sales' }
  ], subtotal: 200.00, taxTotal: 20.00, total: 220.00, remainingCredit: 0, allocations: [{ invoiceId: 'inv_002', invoiceNumber: 'INV-0043', amount: 220.00, date: '2025-12-22' }], refunds: [], notes: [] },

  { id: 'cn_004', number: 'CN-0011', contactId: 'con_006', status: 'draft', date: '2026-03-01', reference: '', currency: 'AUD', brandingThemeId: 'theme_standard', taxMode: 'exclusive', lineItems: [
    { id: 'cnli_004', itemId: null, description: 'Service credit for extended downtime - Feb 2026', quantity: 1, unitPrice: 880.00, discountPercent: 0, accountId: 'acc_200', taxRateId: 'tax_gst', trackingRegion: 'reg_wa', trackingDept: 'dept_support' }
  ], subtotal: 880.00, taxTotal: 88.00, total: 968.00, remainingCredit: 968.00, allocations: [], refunds: [], notes: [] },

  { id: 'cn_005', number: 'CN-0012', contactId: 'con_007', status: 'awaiting_payment', date: '2026-02-22', reference: 'Scope reduction', currency: 'AUD', brandingThemeId: 'theme_standard', taxMode: 'exclusive', lineItems: [
    { id: 'cnli_005', itemId: 'item_001', description: 'Scope reduction - removed reporting module from Q1 project', quantity: 10, unitPrice: 185.00, discountPercent: 0, accountId: 'acc_200', taxRateId: 'tax_gst', trackingRegion: 'reg_nsw', trackingDept: 'dept_ops' }
  ], subtotal: 1850.00, taxTotal: 185.00, total: 2035.00, remainingCredit: 2035.00, allocations: [], refunds: [], notes: [] }
];

const REPEATING_INVOICES = [
  { id: 'rep_001', contactId: 'con_003', status: 'active', frequency: 'monthly', startDate: '2025-06-01', nextDate: '2026-04-01', endDate: '', currency: 'AUD', brandingThemeId: 'theme_standard', taxMode: 'inclusive', saveAs: 'approved_for_sending', lineItems: [
    { id: 'rli_001', itemId: 'item_004', description: 'Cloud Hosting - Monthly', quantity: 1, unitPrice: 299.00, accountId: 'acc_200', taxRateId: 'tax_gst' },
    { id: 'rli_002', itemId: 'item_005', description: 'Technical Support - Monthly Plan', quantity: 1, unitPrice: 450.00, accountId: 'acc_200', taxRateId: 'tax_gst' }
  ], dueDate: { type: 'daysAfterInvoice', days: 30 }, reference: 'Monthly hosting & support', emailSubject: 'Invoice from Demo Company - Monthly Services', emailBody: 'Hi [Contact.FirstName],\n\nPlease find attached your monthly invoice for hosting and support services.\n\nKind regards,\nDemo Company' },

  { id: 'rep_002', contactId: 'con_007', status: 'active', frequency: 'monthly', startDate: '2025-09-01', nextDate: '2026-04-01', endDate: '2026-12-31', currency: 'AUD', brandingThemeId: 'theme_standard', taxMode: 'exclusive', saveAs: 'draft', lineItems: [
    { id: 'rli_003', itemId: 'item_004', description: 'Cloud Hosting - Premium Tier', quantity: 5, unitPrice: 299.00, accountId: 'acc_200', taxRateId: 'tax_gst' },
    { id: 'rli_004', itemId: 'item_005', description: 'Technical Support - Priority Plan', quantity: 1, unitPrice: 450.00, accountId: 'acc_200', taxRateId: 'tax_gst' }
  ], dueDate: { type: 'daysAfterInvoice', days: 14 }, reference: 'CloudNine monthly services', emailSubject: '', emailBody: '' },

  { id: 'rep_003', contactId: 'con_020', status: 'active', frequency: 'monthly', startDate: '2026-01-01', nextDate: '2026-04-01', endDate: '', currency: 'AUD', brandingThemeId: 'theme_professional', taxMode: 'exclusive', saveAs: 'approved_for_sending', lineItems: [
    { id: 'rli_005', itemId: 'item_008', description: 'Software License - Monthly', quantity: 1, unitPrice: 100.00, accountId: 'acc_200', taxRateId: 'tax_gst' }
  ], dueDate: { type: 'daysAfterInvoice', days: 14 }, reference: 'Cascade license fee', emailSubject: 'Demo Company - Monthly License Fee', emailBody: 'Dear Priya,\n\nAttached is your monthly software license invoice.\n\nBest regards,\nDemo Company' },

  { id: 'rep_004', contactId: 'con_023', status: 'active', frequency: 'monthly', startDate: '2025-11-01', nextDate: '2026-04-01', endDate: '', currency: 'AUD', brandingThemeId: 'theme_standard', taxMode: 'exclusive', saveAs: 'approved', lineItems: [
    { id: 'rli_006', itemId: 'item_004', description: 'Cloud Hosting - Standard', quantity: 1, unitPrice: 299.00, accountId: 'acc_200', taxRateId: 'tax_gst' },
    { id: 'rli_007', itemId: 'item_005', description: 'Technical Support - Standard', quantity: 1, unitPrice: 450.00, accountId: 'acc_200', taxRateId: 'tax_gst' }
  ], dueDate: { type: 'daysAfterInvoice', days: 30 }, reference: 'Monthly services', emailSubject: '', emailBody: '' },

  { id: 'rep_005', contactId: 'con_014', status: 'draft', frequency: 'quarterly', startDate: '2026-04-01', nextDate: '2026-04-01', endDate: '', currency: 'AUD', brandingThemeId: 'theme_professional', taxMode: 'exclusive', saveAs: 'draft', lineItems: [
    { id: 'rli_008', itemId: 'item_005', description: 'Technical Support - Quarterly Plan', quantity: 3, unitPrice: 450.00, accountId: 'acc_200', taxRateId: 'tax_gst_free' }
  ], dueDate: { type: 'daysAfterInvoice', days: 14 }, reference: 'Summit Health quarterly support', emailSubject: '', emailBody: '' }
];

const INVOICE_SETTINGS = {
  invoicePrefix: 'INV-',
  invoiceNextNumber: 67,
  creditNotePrefix: 'CN-',
  creditNoteNextNumber: 13,
  quotePrefix: 'QU-',
  quoteNextNumber: 30,
  defaultDueDate: { type: 'daysAfterInvoice', days: 30 },
  defaultQuoteExpiry: { type: 'daysAfterQuote', days: 30 },
  defaultTaxMode: 'exclusive',
  showTaxColumn: true,
  showDiscountColumn: true,
  showItemCode: true
};

const INVOICE_REMINDERS = [
  { id: 'rem_001', enabled: true, timing: 'before', days: 7, subject: 'Upcoming invoice due - {InvoiceNumber}', body: 'Hi {ContactName},\n\nThis is a friendly reminder that invoice {InvoiceNumber} for {AmountDue} is due on {DueDate}.\n\nPlease let us know if you have any questions.\n\nKind regards,\nDemo Company', includeInvoicePdf: true, includeSummary: true },
  { id: 'rem_002', enabled: true, timing: 'after', days: 1, subject: 'Invoice overdue - {InvoiceNumber}', body: 'Hi {ContactName},\n\nInvoice {InvoiceNumber} for {AmountDue} was due on {DueDate} and is now overdue.\n\nPlease arrange payment at your earliest convenience.\n\nKind regards,\nDemo Company', includeInvoicePdf: true, includeSummary: true },
  { id: 'rem_003', enabled: true, timing: 'after', days: 14, subject: 'Second reminder: Invoice overdue - {InvoiceNumber}', body: 'Hi {ContactName},\n\nThis is a second reminder that invoice {InvoiceNumber} for {AmountDue} is now 14 days overdue.\n\nIf payment has already been made, please disregard this message.\n\nKind regards,\nDemo Company', includeInvoicePdf: true, includeSummary: false },
  { id: 'rem_004', enabled: false, timing: 'after', days: 30, subject: 'Final notice: Invoice overdue - {InvoiceNumber}', body: 'Hi {ContactName},\n\nThis is a final notice regarding invoice {InvoiceNumber} for {AmountDue}, which is now 30 days overdue.\n\nPlease arrange payment immediately to avoid further action.\n\nKind regards,\nDemo Company', includeInvoicePdf: true, includeSummary: true }
];

const DUE_DATE_OPTIONS = [
  { value: 'daysAfterInvoice', label: 'day(s) after invoice date' },
  { value: 'daysAfterEndOfMonth', label: 'day(s) after end of invoice month' },
  { value: 'endOfFollowingMonth', label: 'of the following month' },
  { value: 'endOfCurrentMonth', label: 'of the current month' }
];
