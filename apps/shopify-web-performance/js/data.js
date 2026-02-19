// ============================================================================
// Shopify Web Performance Dashboard - Seed Data
// ============================================================================

// Bump this version whenever seed data changes
const SEED_DATA_VERSION = 1;

// ---- Performance Rating Thresholds ----
const METRIC_THRESHOLDS = {
    LCP: { good: 2500, moderate: 4000 },  // milliseconds
    INP: { good: 200, moderate: 500 },     // milliseconds
    CLS: { good: 0.1, moderate: 0.25 }     // unitless
};

// ---- Device Types ----
const DEVICE_TYPES = {
    ALL: 'all',
    DESKTOP: 'desktop',
    MOBILE: 'mobile'
};

// ---- Date Ranges ----
const DATE_RANGES = {
    TODAY: 'today',
    LAST_7_DAYS: 'last_7_days',
    LAST_30_DAYS: 'last_30_days'
};

// ---- Page Types ----
const PAGE_TYPES = ['home', 'product', 'collection', 'cart', 'blog', 'page', 'search', 'account', 'checkout'];

// ---- Event Types ----
const EVENT_TYPES = {
    APP_INSTALL: 'app_installed',
    APP_UNINSTALL: 'app_uninstalled',
    THEME_CHANGE: 'theme_changed',
    THEME_UPDATE: 'theme_updated',
    CODE_CHANGE: 'code_change',
    CUSTOM: 'custom'
};

// ---- Optimization Categories ----
const OPTIMIZATION_CATEGORIES = ['images', 'apps', 'theme', 'scripts', 'fonts', 'videos', 'other'];

// ---- Optimization Statuses ----
const OPTIMIZATION_STATUSES = {
    PENDING: 'pending',
    IN_PROGRESS: 'in_progress',
    COMPLETED: 'completed',
    DISMISSED: 'dismissed'
};

// ---- Optimization Priorities ----
const OPTIMIZATION_PRIORITIES = ['critical', 'high', 'medium', 'low'];

// ---- Alert Conditions ----
const ALERT_CONDITIONS = {
    GREATER_THAN: 'greater_than',
    LESS_THAN: 'less_than'
};

// ---- Report Types ----
const REPORT_TYPES = {
    OVER_TIME: 'over_time',
    BY_PAGE_URL: 'by_page_url',
    BY_PAGE_TYPE: 'by_page_type'
};

// ---- Metrics ----
const METRICS = {
    LCP: { id: 'lcp', name: 'Largest Contentful Paint', shortName: 'LCP', unit: 'ms', description: 'Measures loading speed' },
    INP: { id: 'inp', name: 'Interaction to Next Paint', shortName: 'INP', unit: 'ms', description: 'Measures interactivity' },
    CLS: { id: 'cls', name: 'Cumulative Layout Shift', shortName: 'CLS', unit: '', description: 'Measures visual stability' }
};

// ============================================================================
// Current User
// ============================================================================

const CURRENT_USER = {
    id: 1,
    name: 'Jordan Rivera',
    email: 'jordan@urbanthreads.com',
    role: 'Store Owner',
    avatarColor: '#5c6ac4'
};

// ============================================================================
// Store
// ============================================================================

const STORE = {
    name: 'Urban Threads',
    url: 'urbanthreads.myshopify.com',
    domain: 'urbanthreads.com',
    plan: 'Shopify Plus',
    passwordProtected: false,
    createdAt: '2023-06-15T00:00:00Z',
    currency: 'USD',
    timezone: 'America/New_York'
};

// ============================================================================
// Themes
// ============================================================================

const THEMES = [
    {
        id: 1,
        name: 'Dawn',
        version: '15.0.0',
        author: 'Shopify',
        active: true,
        family: 'horizon',
        os2Compatible: true,
        lastUpdated: '2025-12-01T00:00:00Z',
        settings: {
            pageTransitions: false,
            lazyLoading: true,
            stickyHeader: true,
            predictiveSearch: true,
            cartType: 'drawer',
            paginationLimit: 24,
            animationsEnabled: false
        },
        performanceScore: 92
    },
    {
        id: 2,
        name: 'Refresh',
        version: '3.2.1',
        author: 'Shopify',
        active: false,
        family: 'horizon',
        os2Compatible: true,
        lastUpdated: '2025-11-15T00:00:00Z',
        settings: {
            pageTransitions: true,
            lazyLoading: true,
            stickyHeader: false,
            predictiveSearch: true,
            cartType: 'page',
            paginationLimit: 16,
            animationsEnabled: true
        },
        performanceScore: 88
    },
    {
        id: 3,
        name: 'Craft',
        version: '8.1.0',
        author: 'Shopify',
        active: false,
        family: 'classic',
        os2Compatible: true,
        lastUpdated: '2025-10-20T00:00:00Z',
        settings: {
            pageTransitions: false,
            lazyLoading: true,
            stickyHeader: true,
            predictiveSearch: false,
            cartType: 'drawer',
            paginationLimit: 20,
            animationsEnabled: false
        },
        performanceScore: 85
    },
    {
        id: 4,
        name: 'Prestige',
        version: '10.3.0',
        author: 'Maestrooo',
        active: false,
        family: 'premium',
        os2Compatible: true,
        lastUpdated: '2025-09-10T00:00:00Z',
        settings: {
            pageTransitions: true,
            lazyLoading: true,
            stickyHeader: true,
            predictiveSearch: true,
            cartType: 'drawer',
            paginationLimit: 12,
            animationsEnabled: true
        },
        performanceScore: 78
    },
    {
        id: 5,
        name: 'Impact',
        version: '5.4.2',
        author: 'Maestrooo',
        active: false,
        family: 'premium',
        os2Compatible: true,
        lastUpdated: '2025-08-22T00:00:00Z',
        settings: {
            pageTransitions: true,
            lazyLoading: false,
            stickyHeader: true,
            predictiveSearch: true,
            cartType: 'page',
            paginationLimit: 16,
            animationsEnabled: true
        },
        performanceScore: 72
    },
    {
        id: 6,
        name: 'Debut',
        version: '21.4.0',
        author: 'Shopify',
        active: false,
        family: 'legacy',
        os2Compatible: false,
        lastUpdated: '2024-06-01T00:00:00Z',
        settings: {
            pageTransitions: false,
            lazyLoading: false,
            stickyHeader: false,
            predictiveSearch: false,
            cartType: 'page',
            paginationLimit: 16,
            animationsEnabled: false
        },
        performanceScore: 65
    }
];

// ============================================================================
// Apps
// ============================================================================

const APPS = [
    {
        id: 1,
        name: 'Loox Product Reviews',
        developer: 'Loox',
        category: 'Reviews',
        installed: true,
        installedAt: '2024-03-15T00:00:00Z',
        status: 'active',
        performanceImpact: { lcp: 180, inp: 35, cls: 0.02 },
        scriptLoadTime: 245,
        settings: {
            autoPublish: true,
            widgetType: 'popup',
            lazyLoad: true
        },
        description: 'Collect photo reviews and boost social proof'
    },
    {
        id: 2,
        name: 'Klaviyo Email Marketing',
        developer: 'Klaviyo',
        category: 'Marketing',
        installed: true,
        installedAt: '2024-01-20T00:00:00Z',
        status: 'active',
        performanceImpact: { lcp: 120, inp: 80, cls: 0.01 },
        scriptLoadTime: 310,
        settings: {
            popupEnabled: true,
            trackingEnabled: true,
            popupDelay: 5
        },
        description: 'Email marketing automation and segmentation'
    },
    {
        id: 3,
        name: 'Rebuy Personalization',
        developer: 'Rebuy Engine',
        category: 'Conversion',
        installed: true,
        installedAt: '2024-05-10T00:00:00Z',
        status: 'active',
        performanceImpact: { lcp: 250, inp: 60, cls: 0.04 },
        scriptLoadTime: 420,
        settings: {
            widgetPositions: 'product_page',
            maxRecommendations: 8,
            preloadImages: false
        },
        description: 'AI-powered product recommendations and upsells'
    },
    {
        id: 4,
        name: 'Hotjar Behavior Analytics',
        developer: 'Hotjar',
        category: 'Analytics',
        installed: true,
        installedAt: '2024-06-22T00:00:00Z',
        status: 'active',
        performanceImpact: { lcp: 90, inp: 110, cls: 0.00 },
        scriptLoadTime: 380,
        settings: {
            heatmaps: true,
            recordings: true,
            surveys: false
        },
        description: 'Heatmaps, recordings, and user behavior analytics'
    },
    {
        id: 5,
        name: 'Privy Pop Ups',
        developer: 'Privy',
        category: 'Marketing',
        installed: true,
        installedAt: '2024-08-05T00:00:00Z',
        status: 'active',
        performanceImpact: { lcp: 200, inp: 45, cls: 0.08 },
        scriptLoadTime: 290,
        settings: {
            exitIntent: true,
            displayDelay: 3,
            mobileOptimized: true
        },
        description: 'Pop ups, banners, and email capture'
    },
    {
        id: 6,
        name: 'Instafeed Instagram Feed',
        developer: 'Mintt Studio',
        category: 'Social Media',
        installed: true,
        installedAt: '2024-04-18T00:00:00Z',
        status: 'active',
        performanceImpact: { lcp: 320, inp: 25, cls: 0.06 },
        scriptLoadTime: 510,
        settings: {
            postsToShow: 12,
            layout: 'grid',
            lazyLoad: true
        },
        description: 'Display Instagram feed on your store'
    },
    {
        id: 7,
        name: 'Lucky Orange Analytics',
        developer: 'Lucky Orange',
        category: 'Analytics',
        installed: true,
        installedAt: '2025-01-12T00:00:00Z',
        status: 'active',
        performanceImpact: { lcp: 150, inp: 95, cls: 0.01 },
        scriptLoadTime: 350,
        settings: {
            chatEnabled: false,
            surveysEnabled: false,
            dynamicHeatmaps: true
        },
        description: 'Session recordings, heatmaps, and live chat'
    },
    {
        id: 8,
        name: 'PageFly Landing Page Builder',
        developer: 'PageFly',
        category: 'Page Builder',
        installed: true,
        installedAt: '2024-09-30T00:00:00Z',
        status: 'active',
        performanceImpact: { lcp: 280, inp: 70, cls: 0.05 },
        scriptLoadTime: 460,
        settings: {
            preloadPages: false,
            optimizeImages: true,
            lazyLoadSections: true
        },
        description: 'Drag and drop page builder for custom landing pages'
    },
    {
        id: 9,
        name: 'Yotpo Reviews & UGC',
        developer: 'Yotpo',
        category: 'Reviews',
        installed: false,
        installedAt: null,
        status: 'available',
        performanceImpact: { lcp: 160, inp: 40, cls: 0.03 },
        scriptLoadTime: 280,
        settings: {
            autoPublish: false,
            widgetType: 'inline',
            lazyLoad: true
        },
        description: 'Customer reviews, photos, and Q&A'
    },
    {
        id: 10,
        name: 'Google Tag Manager',
        developer: 'Google',
        category: 'Analytics',
        installed: false,
        installedAt: null,
        status: 'available',
        performanceImpact: { lcp: 100, inp: 130, cls: 0.00 },
        scriptLoadTime: 220,
        settings: {
            containerId: '',
            dataLayerName: 'dataLayer',
            deferLoading: true
        },
        description: 'Tag management system for marketing and analytics tags'
    }
];

// ============================================================================
// Monitored Pages
// ============================================================================

const PAGES = [
    { id: 1, path: '/', name: 'Homepage', type: 'home', monitored: true, priority: 'high' },
    { id: 2, path: '/products/classic-cotton-tee', name: 'Classic Cotton Tee', type: 'product', monitored: true, priority: 'high' },
    { id: 3, path: '/products/vintage-denim-jacket', name: 'Vintage Denim Jacket', type: 'product', monitored: true, priority: 'high' },
    { id: 4, path: '/collections/new-arrivals', name: 'New Arrivals', type: 'collection', monitored: true, priority: 'high' },
    { id: 5, path: '/collections/summer-essentials', name: 'Summer Essentials', type: 'collection', monitored: true, priority: 'medium' },
    { id: 6, path: '/cart', name: 'Shopping Cart', type: 'cart', monitored: true, priority: 'high' },
    { id: 7, path: '/blogs/style-guide', name: 'Style Guide Blog', type: 'blog', monitored: true, priority: 'low' },
    { id: 8, path: '/pages/about-us', name: 'About Us', type: 'page', monitored: true, priority: 'low' },
    { id: 9, path: '/products/organic-linen-pants', name: 'Organic Linen Pants', type: 'product', monitored: true, priority: 'medium' },
    { id: 10, path: '/collections/sale', name: 'Sale Collection', type: 'collection', monitored: true, priority: 'medium' },
    { id: 11, path: '/search', name: 'Search Results', type: 'search', monitored: true, priority: 'medium' },
    { id: 12, path: '/pages/size-guide', name: 'Size Guide', type: 'page', monitored: false, priority: 'low' }
];

// ============================================================================
// Performance Data Generator
// ============================================================================

function generatePerformanceRecords() {
    var records = [];
    var nextId = 1;

    // Simple deterministic pseudo-random based on seed
    function seededRandom(seed) {
        var x = Math.sin(seed) * 10000;
        return x - Math.floor(x);
    }

    // Base performance profiles per page type
    var profiles = {
        'home':       { lcp: [2100, 2800], inp: [150, 220], cls: [0.05, 0.12] },
        'product':    { lcp: [2200, 3000], inp: [160, 230], cls: [0.06, 0.14] },
        'collection': { lcp: [2000, 2600], inp: [140, 200], cls: [0.04, 0.10] },
        'cart':       { lcp: [1800, 2200], inp: [180, 280], cls: [0.03, 0.08] },
        'blog':       { lcp: [1600, 2200], inp: [120, 180], cls: [0.02, 0.06] },
        'page':       { lcp: [1600, 2000], inp: [100, 160], cls: [0.02, 0.05] },
        'search':     { lcp: [1900, 2500], inp: [170, 250], cls: [0.05, 0.10] },
        'account':    { lcp: [1500, 2000], inp: [130, 200], cls: [0.03, 0.07] },
        'checkout':   { lcp: [2000, 2800], inp: [200, 300], cls: [0.04, 0.09] }
    };

    // Generate 30 days of data ending 2026-02-18
    var endDate = new Date('2026-02-18');

    PAGES.forEach(function(page) {
        if (!page.monitored) return;

        var profile = profiles[page.type] || profiles['page'];

        for (var dayOffset = 29; dayOffset >= 0; dayOffset--) {
            var date = new Date(endDate);
            date.setDate(date.getDate() - dayOffset);
            var dateStr = date.toISOString().split('T')[0];

            ['desktop', 'mobile'].forEach(function(device) {
                var seed = page.id * 10000 + dayOffset * 100 + (device === 'mobile' ? 1 : 0);
                var r1 = seededRandom(seed);
                var r2 = seededRandom(seed + 1);
                var r3 = seededRandom(seed + 2);
                var r4 = seededRandom(seed + 3);

                var mobileFactor = device === 'mobile' ? 1.35 : 1.0;
                var mobileClsFactor = device === 'mobile' ? 1.2 : 1.0;

                var lcp = Math.round((profile.lcp[0] + r1 * (profile.lcp[1] - profile.lcp[0])) * mobileFactor);
                var inp = Math.round((profile.inp[0] + r2 * (profile.inp[1] - profile.inp[0])) * mobileFactor);
                var cls = parseFloat(((profile.cls[0] + r3 * (profile.cls[1] - profile.cls[0])) * mobileClsFactor).toFixed(3));

                var fcp = Math.round(lcp * (0.4 + r4 * 0.2));
                var ttfb = Math.round(fcp * (0.3 + seededRandom(seed + 4) * 0.3));

                var sessions = Math.round(50 + seededRandom(seed + 5) * 450);

                // Distribution percentages
                var goodLcp = lcp <= 2500 ? Math.round(75 + seededRandom(seed + 6) * 15) : Math.round(40 + seededRandom(seed + 6) * 25);
                var poorLcp = lcp > 4000 ? Math.round(20 + seededRandom(seed + 7) * 15) : Math.round(2 + seededRandom(seed + 7) * 8);
                var moderateLcp = 100 - goodLcp - poorLcp;

                var goodInp = inp <= 200 ? Math.round(78 + seededRandom(seed + 8) * 15) : Math.round(45 + seededRandom(seed + 8) * 20);
                var poorInp = inp > 500 ? Math.round(15 + seededRandom(seed + 9) * 15) : Math.round(1 + seededRandom(seed + 9) * 6);
                var moderateInp = 100 - goodInp - poorInp;

                var goodCls = cls <= 0.1 ? Math.round(80 + seededRandom(seed + 10) * 15) : Math.round(50 + seededRandom(seed + 10) * 20);
                var poorCls = cls >= 0.25 ? Math.round(15 + seededRandom(seed + 11) * 15) : Math.round(1 + seededRandom(seed + 11) * 5);
                var moderateCls = 100 - goodCls - poorCls;

                records.push({
                    id: nextId++,
                    pageId: page.id,
                    date: dateStr,
                    deviceType: device,
                    lcp: lcp,
                    inp: inp,
                    cls: cls,
                    fcp: fcp,
                    ttfb: ttfb,
                    sessions: sessions,
                    goodLcp: goodLcp,
                    moderateLcp: moderateLcp,
                    poorLcp: poorLcp,
                    goodInp: goodInp,
                    moderateInp: moderateInp,
                    poorInp: poorInp,
                    goodCls: goodCls,
                    moderateCls: moderateCls,
                    poorCls: poorCls
                });
            });
        }
    });

    return records;
}

var PERFORMANCE_RECORDS = generatePerformanceRecords();

// ============================================================================
// Events
// ============================================================================

const EVENTS = [
    { id: 1, date: '2026-01-22T00:00:00Z', type: 'app_installed', title: 'Installed Lucky Orange Analytics', description: 'Added behavior analytics tracking', metric: 'all', impact: 'negative' },
    { id: 2, date: '2026-01-28T00:00:00Z', type: 'theme_updated', title: 'Updated Dawn theme to v15.0', description: 'Theme update with performance improvements', metric: 'lcp', impact: 'positive' },
    { id: 3, date: '2026-02-03T00:00:00Z', type: 'code_change', title: 'Added hero video to homepage', description: 'Embedded promotional video above the fold', metric: 'lcp', impact: 'negative' },
    { id: 4, date: '2026-02-05T00:00:00Z', type: 'app_uninstalled', title: 'Removed TrustBadge app', description: 'Uninstalled unused trust badge app', metric: 'cls', impact: 'positive' },
    { id: 5, date: '2026-02-08T00:00:00Z', type: 'theme_changed', title: 'Tested Prestige theme (reverted)', description: 'Briefly activated Prestige theme for testing', metric: 'all', impact: 'neutral' },
    { id: 6, date: '2026-02-10T00:00:00Z', type: 'code_change', title: 'Optimized collection page images', description: 'Compressed and resized collection hero images', metric: 'lcp', impact: 'positive' },
    { id: 7, date: '2026-02-14T00:00:00Z', type: 'app_installed', title: 'Installed PageFly Builder', description: 'Added landing page builder for campaigns', metric: 'lcp', impact: 'negative' },
    { id: 8, date: '2026-02-17T00:00:00Z', type: 'custom', title: 'Valentines Day sale ended', description: 'High traffic period concluded', metric: 'all', impact: 'neutral' }
];

// ============================================================================
// Performance Budgets
// ============================================================================

const PERFORMANCE_BUDGETS = {
    lcp: { target: 2500, warning: 3500 },
    inp: { target: 200, warning: 400 },
    cls: { target: 0.1, warning: 0.2 }
};

// ============================================================================
// Alert Rules
// ============================================================================

const ALERT_RULES = [
    { id: 1, name: 'LCP Budget Exceeded', metric: 'lcp', condition: 'greater_than', threshold: 2500, pageType: 'all', deviceType: 'all', enabled: true, notifyEmail: true, createdAt: '2025-10-01T00:00:00Z' },
    { id: 2, name: 'Mobile INP Warning', metric: 'inp', condition: 'greater_than', threshold: 300, pageType: 'all', deviceType: 'mobile', enabled: true, notifyEmail: true, createdAt: '2025-10-15T00:00:00Z' },
    { id: 3, name: 'CLS Regression Alert', metric: 'cls', condition: 'greater_than', threshold: 0.15, pageType: 'all', deviceType: 'all', enabled: true, notifyEmail: false, createdAt: '2025-11-01T00:00:00Z' },
    { id: 4, name: 'Homepage LCP Monitor', metric: 'lcp', condition: 'greater_than', threshold: 2000, pageType: 'home', deviceType: 'all', enabled: true, notifyEmail: true, createdAt: '2025-11-20T00:00:00Z' },
    { id: 5, name: 'Product Page CLS', metric: 'cls', condition: 'greater_than', threshold: 0.1, pageType: 'product', deviceType: 'mobile', enabled: false, notifyEmail: false, createdAt: '2025-12-01T00:00:00Z' },
    { id: 6, name: 'Desktop INP Check', metric: 'inp', condition: 'greater_than', threshold: 150, pageType: 'all', deviceType: 'desktop', enabled: true, notifyEmail: true, createdAt: '2026-01-10T00:00:00Z' }
];

// ============================================================================
// Optimizations
// ============================================================================

const OPTIMIZATIONS = [
    { id: 1, title: 'Compress hero banner image on homepage', description: 'The homepage hero image is 2.4MB. Compress to under 200KB using WebP format.', metric: 'lcp', priority: 'critical', status: 'pending', estimatedImpact: '300-500ms LCP improvement', category: 'images', pageAffected: '/', createdAt: '2025-12-01T00:00:00Z' },
    { id: 2, title: 'Remove unused Instafeed scripts from product pages', description: 'The Instagram feed widget loads on all pages but only displays on the homepage.', metric: 'lcp', priority: 'high', status: 'in_progress', estimatedImpact: '200ms LCP improvement', category: 'apps', pageAffected: '/products/*', createdAt: '2025-12-10T00:00:00Z' },
    { id: 3, title: 'Defer Klaviyo popup script loading', description: 'The email signup popup script blocks rendering. Defer loading until after page interaction.', metric: 'inp', priority: 'high', status: 'pending', estimatedImpact: '50-80ms INP improvement', category: 'scripts', pageAffected: '*', createdAt: '2025-12-15T00:00:00Z' },
    { id: 4, title: 'Set explicit image dimensions in collection grid', description: 'Product images in collection pages lack width/height attributes causing layout shifts.', metric: 'cls', priority: 'medium', status: 'completed', estimatedImpact: '0.05 CLS improvement', category: 'images', pageAffected: '/collections/*', createdAt: '2025-11-20T00:00:00Z' },
    { id: 5, title: 'Lazy load below-fold product reviews', description: 'Loox review widgets load immediately. Configure lazy loading for reviews below the fold.', metric: 'lcp', priority: 'medium', status: 'pending', estimatedImpact: '150ms LCP improvement', category: 'apps', pageAffected: '/products/*', createdAt: '2026-01-05T00:00:00Z' },
    { id: 6, title: 'Optimize web fonts loading strategy', description: 'Custom fonts are render-blocking. Switch to font-display: swap and preload critical fonts.', metric: 'lcp', priority: 'high', status: 'pending', estimatedImpact: '200-400ms LCP improvement', category: 'fonts', pageAffected: '*', createdAt: '2026-01-10T00:00:00Z' },
    { id: 7, title: 'Reduce Privy popup CLS impact', description: 'Email popup causes layout shift when it appears. Use fixed positioning instead.', metric: 'cls', priority: 'medium', status: 'dismissed', estimatedImpact: '0.04 CLS improvement', category: 'apps', pageAffected: '*', createdAt: '2026-01-15T00:00:00Z' },
    { id: 8, title: 'Enable pagination on large collections', description: 'The Sale collection loads 200+ products at once. Enable pagination to limit to 24 per page.', metric: 'lcp', priority: 'high', status: 'pending', estimatedImpact: '500ms+ LCP improvement', category: 'theme', pageAffected: '/collections/sale', createdAt: '2026-01-20T00:00:00Z' }
];

// ============================================================================
// Saved Reports
// ============================================================================

const SAVED_REPORTS = [
    { id: 1, name: 'Mobile LCP Weekly', metric: 'lcp', reportType: 'over_time', filters: { deviceType: 'mobile', dateRange: 'last_7_days', pageType: 'all' }, createdAt: '2025-10-15T00:00:00Z' },
    { id: 2, name: 'Product Page CLS Report', metric: 'cls', reportType: 'by_page_url', filters: { deviceType: 'all', dateRange: 'last_30_days', pageType: 'product' }, createdAt: '2025-11-01T00:00:00Z' },
    { id: 3, name: 'Desktop INP by Page Type', metric: 'inp', reportType: 'by_page_type', filters: { deviceType: 'desktop', dateRange: 'last_30_days', pageType: 'all' }, createdAt: '2025-12-01T00:00:00Z' },
    { id: 4, name: 'Homepage Performance Trend', metric: 'lcp', reportType: 'over_time', filters: { deviceType: 'all', dateRange: 'last_30_days', pageType: 'home' }, createdAt: '2026-01-05T00:00:00Z' }
];
