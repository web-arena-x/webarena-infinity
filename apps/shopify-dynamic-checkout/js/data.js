/* ============================================================
   Shopify Dynamic Checkout – Seed Data
   ============================================================ */

const SEED_DATA_VERSION = 1;

// ---- Current Store Owner ----
const CURRENT_USER = {
    id: 'usr_owner_1',
    name: 'Morgan Rivera',
    email: 'morgan@urbanthread.co',
    storeName: 'Urban Thread Co.',
    storeUrl: 'urbanthread.myshopify.com',
    plan: 'Shopify Plus',
    avatarInitials: 'MR'
};

// ---- Themes ----
const THEMES = [
    {
        id: 'theme_1',
        name: 'Dawn',
        role: 'main',
        version: '15.2.0',
        author: 'Shopify',
        lastUpdated: '2026-02-28T14:32:00Z',
        previewable: true,
        supportLevel: 'full',
        settings: {
            colors: {
                accentButtonBg: '#1A1A1A',
                accentButtonText: '#FFFFFF',
                primaryBg: '#FFFFFF',
                primaryText: '#1A1A1A',
                secondaryBg: '#F6F6F6',
                secondaryText: '#6B7280',
                accentColor: '#4F46E5'
            },
            typography: {
                headingFont: 'Assistant',
                bodyFont: 'Assistant',
                buttonFont: 'Assistant',
                headingScale: 100,
                bodyScale: 100
            }
        }
    },
    {
        id: 'theme_2',
        name: 'Craft',
        role: 'unpublished',
        version: '8.1.0',
        author: 'Shopify',
        lastUpdated: '2026-02-20T09:15:00Z',
        previewable: true,
        supportLevel: 'full',
        settings: {
            colors: {
                accentButtonBg: '#2D5016',
                accentButtonText: '#FFFFFF',
                primaryBg: '#FAF9F6',
                primaryText: '#2D2D2D',
                secondaryBg: '#EDE9E0',
                secondaryText: '#5C5C5C',
                accentColor: '#2D5016'
            },
            typography: {
                headingFont: 'Playfair Display',
                bodyFont: 'Source Sans Pro',
                buttonFont: 'Source Sans Pro',
                headingScale: 110,
                bodyScale: 100
            }
        }
    },
    {
        id: 'theme_3',
        name: 'Sense',
        role: 'unpublished',
        version: '10.0.2',
        author: 'Shopify',
        lastUpdated: '2026-01-12T16:48:00Z',
        previewable: true,
        supportLevel: 'full',
        settings: {
            colors: {
                accentButtonBg: '#C8553D',
                accentButtonText: '#FFFFFF',
                primaryBg: '#FFFCF7',
                primaryText: '#3D3D3D',
                secondaryBg: '#F4EDE4',
                secondaryText: '#7A7A7A',
                accentColor: '#C8553D'
            },
            typography: {
                headingFont: 'DM Serif Display',
                bodyFont: 'DM Sans',
                buttonFont: 'DM Sans',
                headingScale: 120,
                bodyScale: 95
            }
        }
    },
    {
        id: 'theme_4',
        name: 'Ride',
        role: 'unpublished',
        version: '6.3.1',
        author: 'Shopify',
        lastUpdated: '2025-11-05T11:22:00Z',
        previewable: true,
        supportLevel: 'full',
        settings: {
            colors: {
                accentButtonBg: '#0F172A',
                accentButtonText: '#F8FAFC',
                primaryBg: '#F8FAFC',
                primaryText: '#0F172A',
                secondaryBg: '#E2E8F0',
                secondaryText: '#475569',
                accentColor: '#3B82F6'
            },
            typography: {
                headingFont: 'Inter',
                bodyFont: 'Inter',
                buttonFont: 'Inter',
                headingScale: 105,
                bodyScale: 100
            }
        }
    },
    {
        id: 'theme_5',
        name: 'Taste',
        role: 'unpublished',
        version: '12.0.0',
        author: 'Shopify',
        lastUpdated: '2026-02-01T08:45:00Z',
        previewable: true,
        supportLevel: 'full',
        settings: {
            colors: {
                accentButtonBg: '#7C3AED',
                accentButtonText: '#FFFFFF',
                primaryBg: '#FAFAFA',
                primaryText: '#18181B',
                secondaryBg: '#F4F4F5',
                secondaryText: '#52525B',
                accentColor: '#7C3AED'
            },
            typography: {
                headingFont: 'Poppins',
                bodyFont: 'Open Sans',
                buttonFont: 'Poppins',
                headingScale: 100,
                bodyScale: 100
            }
        }
    },
    {
        id: 'theme_6',
        name: 'Vintage Revival',
        role: 'demo',
        version: '3.4.0',
        author: 'Theme Harbor',
        lastUpdated: '2025-09-14T14:00:00Z',
        previewable: true,
        supportLevel: 'limited',
        settings: {
            colors: {
                accentButtonBg: '#8B4513',
                accentButtonText: '#FFF8DC',
                primaryBg: '#FFF8DC',
                primaryText: '#3E2723',
                secondaryBg: '#F5DEB3',
                secondaryText: '#5D4037',
                accentColor: '#8B4513'
            },
            typography: {
                headingFont: 'Merriweather',
                bodyFont: 'Lora',
                buttonFont: 'Merriweather',
                headingScale: 115,
                bodyScale: 95
            }
        }
    }
];

// ---- Product Templates (per theme) ----
const TEMPLATES = [
    // Dawn (theme_1) templates
    {
        id: 'tmpl_1',
        themeId: 'theme_1',
        name: 'Default product',
        handle: 'product',
        isDefault: true,
        isAlternate: false,
        showAcceleratedCheckout: true,
        showQuantitySelector: true,
        buyButtonText: 'Add to cart',
        createdAt: '2025-06-10T08:00:00Z'
    },
    {
        id: 'tmpl_2',
        themeId: 'theme_1',
        name: 'Product - No checkout buttons',
        handle: 'product.no-checkout',
        isDefault: false,
        isAlternate: true,
        showAcceleratedCheckout: false,
        showQuantitySelector: true,
        buyButtonText: 'Add to cart',
        createdAt: '2025-08-22T10:30:00Z'
    },
    {
        id: 'tmpl_3',
        themeId: 'theme_1',
        name: 'Product - Gift cards',
        handle: 'product.gift-card',
        isDefault: false,
        isAlternate: true,
        showAcceleratedCheckout: false,
        showQuantitySelector: false,
        buyButtonText: 'Add to cart',
        createdAt: '2025-09-15T14:20:00Z'
    },
    // Craft (theme_2) templates
    {
        id: 'tmpl_4',
        themeId: 'theme_2',
        name: 'Default product',
        handle: 'product',
        isDefault: true,
        isAlternate: false,
        showAcceleratedCheckout: false,
        showQuantitySelector: true,
        buyButtonText: 'Add to cart',
        createdAt: '2025-07-01T09:00:00Z'
    },
    {
        id: 'tmpl_5',
        themeId: 'theme_2',
        name: 'Product - Featured',
        handle: 'product.featured',
        isDefault: false,
        isAlternate: true,
        showAcceleratedCheckout: true,
        showQuantitySelector: true,
        buyButtonText: 'Buy now',
        createdAt: '2025-10-10T11:15:00Z'
    },
    // Sense (theme_3) templates
    {
        id: 'tmpl_6',
        themeId: 'theme_3',
        name: 'Default product',
        handle: 'product',
        isDefault: true,
        isAlternate: false,
        showAcceleratedCheckout: true,
        showQuantitySelector: true,
        buyButtonText: 'Add to cart',
        createdAt: '2025-06-20T07:45:00Z'
    },
    // Ride (theme_4) templates
    {
        id: 'tmpl_7',
        themeId: 'theme_4',
        name: 'Default product',
        handle: 'product',
        isDefault: true,
        isAlternate: false,
        showAcceleratedCheckout: true,
        showQuantitySelector: false,
        buyButtonText: 'Add to cart',
        createdAt: '2025-05-15T12:00:00Z'
    },
    // Taste (theme_5) templates
    {
        id: 'tmpl_8',
        themeId: 'theme_5',
        name: 'Default product',
        handle: 'product',
        isDefault: true,
        isAlternate: false,
        showAcceleratedCheckout: false,
        showQuantitySelector: true,
        buyButtonText: 'Add to cart',
        createdAt: '2025-08-01T10:00:00Z'
    },
    // Vintage Revival (theme_6) templates
    {
        id: 'tmpl_9',
        themeId: 'theme_6',
        name: 'Default product',
        handle: 'product',
        isDefault: true,
        isAlternate: false,
        showAcceleratedCheckout: false,
        showQuantitySelector: true,
        buyButtonText: 'Add to cart',
        createdAt: '2025-09-14T14:00:00Z'
    }
];

// ---- Theme Pages / Sections ----
const THEME_PAGES = [
    { id: 'page_home', themeId: 'theme_1', name: 'Home page', handle: 'index', type: 'home' },
    { id: 'page_products', themeId: 'theme_1', name: 'Products', handle: 'product', type: 'product' },
    { id: 'page_collection', themeId: 'theme_1', name: 'Collections', handle: 'collection', type: 'collection' },
    { id: 'page_cart', themeId: 'theme_1', name: 'Cart', handle: 'cart', type: 'cart' },
    { id: 'page_blog', themeId: 'theme_1', name: 'Blog', handle: 'blog', type: 'blog' },
    { id: 'page_contact', themeId: 'theme_1', name: 'Contact', handle: 'page.contact', type: 'page' },
    { id: 'page_about', themeId: 'theme_1', name: 'About us', handle: 'page.about', type: 'page' }
];

// Sections within pages
const THEME_SECTIONS = [
    // Home page sections
    {
        id: 'sec_1',
        themeId: 'theme_1',
        pageId: 'page_home',
        type: 'featured_product',
        label: 'Featured product',
        productId: 'prod_1',
        showAcceleratedCheckout: true,
        position: 0,
        visible: true
    },
    {
        id: 'sec_2',
        themeId: 'theme_1',
        pageId: 'page_home',
        type: 'featured_collection',
        label: 'Featured collection',
        collectionId: 'col_1',
        position: 1,
        visible: true
    },
    {
        id: 'sec_3',
        themeId: 'theme_1',
        pageId: 'page_home',
        type: 'slideshow',
        label: 'Slideshow',
        position: 2,
        visible: true
    },
    {
        id: 'sec_4',
        themeId: 'theme_1',
        pageId: 'page_home',
        type: 'rich_text',
        label: 'Rich text',
        position: 3,
        visible: true
    },
    {
        id: 'sec_5',
        themeId: 'theme_1',
        pageId: 'page_home',
        type: 'newsletter',
        label: 'Newsletter',
        position: 4,
        visible: true
    },
    // Product page sections
    {
        id: 'sec_6',
        themeId: 'theme_1',
        pageId: 'page_products',
        type: 'product_information',
        label: 'Product information',
        position: 0,
        visible: true,
        blocks: [
            { id: 'blk_1', type: 'title', label: 'Title', visible: true },
            { id: 'blk_2', type: 'price', label: 'Price', visible: true },
            { id: 'blk_3', type: 'variant_picker', label: 'Variant picker', visible: true },
            { id: 'blk_4', type: 'quantity_selector', label: 'Quantity selector', visible: true },
            { id: 'blk_5', type: 'buy_buttons', label: 'Buy buttons', visible: true },
            { id: 'blk_6', type: 'description', label: 'Description', visible: true },
            { id: 'blk_7', type: 'share', label: 'Share', visible: true }
        ]
    },
    {
        id: 'sec_7',
        themeId: 'theme_1',
        pageId: 'page_products',
        type: 'product_recommendations',
        label: 'Product recommendations',
        position: 1,
        visible: true
    }
];

// ---- Payment Methods ----
const PAYMENT_METHODS = [
    {
        id: 'pm_1',
        name: 'Shop Pay',
        provider: 'shopify',
        brand: 'shop_pay',
        type: 'accelerated',
        isActive: true,
        requiresSetup: false,
        browserRestrictions: null,
        regionRestrictions: null,
        debugParam: 'Shop',
        logoColor: '#5A31F4',
        description: 'Shopify\'s accelerated checkout for fast, secure payments.',
        setupUrl: null,
        activatedAt: '2025-03-10T09:00:00Z'
    },
    {
        id: 'pm_2',
        name: 'Apple Pay',
        provider: 'apple',
        brand: 'apple_pay',
        type: 'accelerated',
        isActive: true,
        requiresSetup: false,
        browserRestrictions: 'safari_only',
        regionRestrictions: null,
        debugParam: 'Apple',
        logoColor: '#000000',
        description: 'Accept payments through Apple Pay on Safari browsers.',
        setupUrl: null,
        activatedAt: '2025-04-15T14:30:00Z'
    },
    {
        id: 'pm_3',
        name: 'Google Pay',
        provider: 'google',
        brand: 'google_pay',
        type: 'accelerated',
        isActive: true,
        requiresSetup: false,
        browserRestrictions: null,
        regionRestrictions: null,
        debugParam: 'Google',
        logoColor: '#4285F4',
        description: 'Allow customers to pay with Google Pay from Chrome and other browsers.',
        setupUrl: null,
        activatedAt: '2025-04-15T14:35:00Z'
    },
    {
        id: 'pm_4',
        name: 'PayPal',
        provider: 'paypal',
        brand: 'paypal',
        type: 'accelerated',
        isActive: true,
        requiresSetup: true,
        browserRestrictions: null,
        regionRestrictions: null,
        debugParam: 'PayPal',
        logoColor: '#003087',
        description: 'Accept payments through PayPal and PayPal Credit.',
        setupUrl: 'https://admin.shopify.com/settings/payments/paypal',
        activatedAt: '2025-01-20T10:00:00Z'
    },
    {
        id: 'pm_5',
        name: 'Amazon Pay',
        provider: 'amazon',
        brand: 'amazon_pay',
        type: 'accelerated',
        isActive: false,
        requiresSetup: true,
        browserRestrictions: null,
        regionRestrictions: null,
        debugParam: 'Amazon',
        logoColor: '#FF9900',
        description: 'Let customers check out using their Amazon account.',
        setupUrl: 'https://admin.shopify.com/settings/payments/amazon',
        activatedAt: null
    },
    {
        id: 'pm_6',
        name: 'Venmo',
        provider: 'paypal',
        brand: 'venmo',
        type: 'accelerated',
        isActive: false,
        requiresSetup: true,
        browserRestrictions: null,
        regionRestrictions: ['US'],
        debugParam: 'Venmo',
        logoColor: '#3D95CE',
        description: 'Accept Venmo payments (United States only). Requires PayPal.',
        setupUrl: 'https://admin.shopify.com/settings/payments/paypal',
        activatedAt: null
    },
    {
        id: 'pm_7',
        name: 'Shopify Payments',
        provider: 'shopify',
        brand: 'shopify_payments',
        type: 'primary',
        isActive: true,
        requiresSetup: false,
        browserRestrictions: null,
        regionRestrictions: null,
        debugParam: null,
        logoColor: '#96BF48',
        description: 'Accept credit cards, debit cards, and other payments directly.',
        setupUrl: null,
        activatedAt: '2024-11-01T08:00:00Z'
    },
    {
        id: 'pm_8',
        name: 'Manual payment',
        provider: 'manual',
        brand: 'manual',
        type: 'manual',
        isActive: true,
        requiresSetup: false,
        browserRestrictions: null,
        regionRestrictions: null,
        debugParam: null,
        logoColor: '#6B7280',
        description: 'Bank deposit, money order, or cash on delivery.',
        setupUrl: null,
        activatedAt: '2024-11-01T08:00:00Z'
    }
];

// ---- Shop Promise ----
const SHOP_PROMISE = {
    isActive: false,
    prioritizesShopPay: false,
    estimatedDeliveryDays: { min: 3, max: 5 },
    freeShippingThreshold: 75.00
};

// ---- Products ----
const PRODUCTS = [
    {
        id: 'prod_1',
        title: 'Classic Cotton T-Shirt',
        description: 'Premium 100% organic cotton t-shirt with a relaxed fit. Pre-shrunk and enzyme-washed for exceptional softness.',
        vendor: 'Urban Thread Co.',
        productType: 'Apparel',
        status: 'active',
        templateId: 'tmpl_1',
        hasGiftCardRecipientFields: false,
        createdAt: '2025-03-15T10:30:00Z',
        updatedAt: '2026-02-20T08:15:00Z',
        tags: ['cotton', 'casual', 'bestseller', 'organic'],
        variants: [
            { id: 'var_1', title: 'Small / Black', price: '29.99', compareAtPrice: null, sku: 'CT-SM-BK', inventoryQty: 145, weight: 200 },
            { id: 'var_2', title: 'Small / White', price: '29.99', compareAtPrice: null, sku: 'CT-SM-WH', inventoryQty: 98, weight: 200 },
            { id: 'var_3', title: 'Small / Navy', price: '29.99', compareAtPrice: null, sku: 'CT-SM-NV', inventoryQty: 67, weight: 200 },
            { id: 'var_4', title: 'Medium / Black', price: '29.99', compareAtPrice: null, sku: 'CT-MD-BK', inventoryQty: 210, weight: 220 },
            { id: 'var_5', title: 'Medium / White', price: '29.99', compareAtPrice: null, sku: 'CT-MD-WH', inventoryQty: 155, weight: 220 },
            { id: 'var_6', title: 'Medium / Navy', price: '29.99', compareAtPrice: null, sku: 'CT-MD-NV', inventoryQty: 89, weight: 220 },
            { id: 'var_7', title: 'Large / Black', price: '29.99', compareAtPrice: null, sku: 'CT-LG-BK', inventoryQty: 178, weight: 240 },
            { id: 'var_8', title: 'Large / White', price: '29.99', compareAtPrice: null, sku: 'CT-LG-WH', inventoryQty: 132, weight: 240 },
            { id: 'var_9', title: 'Large / Navy', price: '29.99', compareAtPrice: null, sku: 'CT-LG-NV', inventoryQty: 75, weight: 240 },
            { id: 'var_10', title: 'XL / Black', price: '31.99', compareAtPrice: null, sku: 'CT-XL-BK', inventoryQty: 62, weight: 260 },
            { id: 'var_11', title: 'XL / White', price: '31.99', compareAtPrice: null, sku: 'CT-XL-WH', inventoryQty: 43, weight: 260 }
        ],
        images: [{ alt: 'Classic Cotton T-Shirt front view' }]
    },
    {
        id: 'prod_2',
        title: 'Merino Wool Sweater',
        description: 'Ultra-fine merino wool sweater with ribbed cuffs and hem. Temperature regulating and moisture-wicking.',
        vendor: 'Urban Thread Co.',
        productType: 'Apparel',
        status: 'active',
        templateId: 'tmpl_1',
        hasGiftCardRecipientFields: false,
        createdAt: '2025-04-20T09:00:00Z',
        updatedAt: '2026-02-18T11:20:00Z',
        tags: ['wool', 'merino', 'premium', 'winter'],
        variants: [
            { id: 'var_12', title: 'Small / Charcoal', price: '89.99', compareAtPrice: '119.99', sku: 'MW-SM-CH', inventoryQty: 34, weight: 380 },
            { id: 'var_13', title: 'Small / Cream', price: '89.99', compareAtPrice: '119.99', sku: 'MW-SM-CR', inventoryQty: 28, weight: 380 },
            { id: 'var_14', title: 'Medium / Charcoal', price: '89.99', compareAtPrice: '119.99', sku: 'MW-MD-CH', inventoryQty: 52, weight: 420 },
            { id: 'var_15', title: 'Medium / Cream', price: '89.99', compareAtPrice: '119.99', sku: 'MW-MD-CR', inventoryQty: 41, weight: 420 },
            { id: 'var_16', title: 'Large / Charcoal', price: '89.99', compareAtPrice: '119.99', sku: 'MW-LG-CH', inventoryQty: 37, weight: 460 },
            { id: 'var_17', title: 'Large / Cream', price: '89.99', compareAtPrice: '119.99', sku: 'MW-LG-CR', inventoryQty: 19, weight: 460 }
        ],
        images: [{ alt: 'Merino Wool Sweater in charcoal' }]
    },
    {
        id: 'prod_3',
        title: 'Slim Fit Chinos',
        description: 'Modern slim fit chinos with stretch cotton blend. Features a hidden coin pocket and reinforced seams.',
        vendor: 'Urban Thread Co.',
        productType: 'Apparel',
        status: 'active',
        templateId: 'tmpl_1',
        hasGiftCardRecipientFields: false,
        createdAt: '2025-05-10T08:30:00Z',
        updatedAt: '2026-01-28T15:45:00Z',
        tags: ['chinos', 'slim-fit', 'business-casual'],
        variants: [
            { id: 'var_18', title: '30x30 / Khaki', price: '64.99', compareAtPrice: null, sku: 'CH-30-KH', inventoryQty: 88, weight: 450 },
            { id: 'var_19', title: '30x30 / Olive', price: '64.99', compareAtPrice: null, sku: 'CH-30-OL', inventoryQty: 72, weight: 450 },
            { id: 'var_20', title: '32x32 / Khaki', price: '64.99', compareAtPrice: null, sku: 'CH-32-KH', inventoryQty: 134, weight: 480 },
            { id: 'var_21', title: '32x32 / Olive', price: '64.99', compareAtPrice: null, sku: 'CH-32-OL', inventoryQty: 95, weight: 480 },
            { id: 'var_22', title: '32x32 / Navy', price: '64.99', compareAtPrice: null, sku: 'CH-32-NV', inventoryQty: 108, weight: 480 },
            { id: 'var_23', title: '34x32 / Khaki', price: '64.99', compareAtPrice: null, sku: 'CH-34-KH', inventoryQty: 121, weight: 500 },
            { id: 'var_24', title: '34x32 / Navy', price: '64.99', compareAtPrice: null, sku: 'CH-34-NV', inventoryQty: 76, weight: 500 },
            { id: 'var_25', title: '36x32 / Khaki', price: '64.99', compareAtPrice: null, sku: 'CH-36-KH', inventoryQty: 54, weight: 520 }
        ],
        images: [{ alt: 'Slim Fit Chinos front' }]
    },
    {
        id: 'prod_4',
        title: 'Leather Crossbody Bag',
        description: 'Full-grain leather crossbody bag with adjustable strap and brass hardware. Interior zip pocket and card slots.',
        vendor: 'Atelier Goods',
        productType: 'Accessories',
        status: 'active',
        templateId: 'tmpl_2',
        hasGiftCardRecipientFields: false,
        createdAt: '2025-06-01T12:00:00Z',
        updatedAt: '2026-02-10T09:30:00Z',
        tags: ['leather', 'bag', 'accessories', 'handmade'],
        variants: [
            { id: 'var_26', title: 'Tan', price: '149.99', compareAtPrice: null, sku: 'LCB-TAN', inventoryQty: 23, weight: 650 },
            { id: 'var_27', title: 'Black', price: '149.99', compareAtPrice: null, sku: 'LCB-BLK', inventoryQty: 31, weight: 650 },
            { id: 'var_28', title: 'Cognac', price: '149.99', compareAtPrice: null, sku: 'LCB-COG', inventoryQty: 15, weight: 650 }
        ],
        images: [{ alt: 'Leather Crossbody Bag' }]
    },
    {
        id: 'prod_5',
        title: 'Digital Gift Card',
        description: 'Send an Urban Thread Co. digital gift card to someone special. Available in multiple denominations.',
        vendor: 'Urban Thread Co.',
        productType: 'Gift Cards',
        status: 'active',
        templateId: 'tmpl_3',
        hasGiftCardRecipientFields: true,
        createdAt: '2025-02-01T10:00:00Z',
        updatedAt: '2026-02-28T16:00:00Z',
        tags: ['gift-card', 'digital'],
        variants: [
            { id: 'var_29', title: '$25', price: '25.00', compareAtPrice: null, sku: 'GC-025', inventoryQty: null, weight: 0 },
            { id: 'var_30', title: '$50', price: '50.00', compareAtPrice: null, sku: 'GC-050', inventoryQty: null, weight: 0 },
            { id: 'var_31', title: '$75', price: '75.00', compareAtPrice: null, sku: 'GC-075', inventoryQty: null, weight: 0 },
            { id: 'var_32', title: '$100', price: '100.00', compareAtPrice: null, sku: 'GC-100', inventoryQty: null, weight: 0 },
            { id: 'var_33', title: '$200', price: '200.00', compareAtPrice: null, sku: 'GC-200', inventoryQty: null, weight: 0 }
        ],
        images: [{ alt: 'Digital Gift Card' }]
    },
    {
        id: 'prod_6',
        title: 'Recycled Polyester Windbreaker',
        description: 'Lightweight windbreaker made from 100% recycled polyester. Packable design with reflective detailing.',
        vendor: 'Urban Thread Co.',
        productType: 'Outerwear',
        status: 'active',
        templateId: 'tmpl_1',
        hasGiftCardRecipientFields: false,
        createdAt: '2025-07-20T09:00:00Z',
        updatedAt: '2026-02-25T10:10:00Z',
        tags: ['sustainable', 'recycled', 'windbreaker', 'outerwear'],
        variants: [
            { id: 'var_34', title: 'Small / Forest', price: '79.99', compareAtPrice: null, sku: 'WB-SM-FO', inventoryQty: 45, weight: 300 },
            { id: 'var_35', title: 'Small / Slate', price: '79.99', compareAtPrice: null, sku: 'WB-SM-SL', inventoryQty: 38, weight: 300 },
            { id: 'var_36', title: 'Medium / Forest', price: '79.99', compareAtPrice: null, sku: 'WB-MD-FO', inventoryQty: 67, weight: 330 },
            { id: 'var_37', title: 'Medium / Slate', price: '79.99', compareAtPrice: null, sku: 'WB-MD-SL', inventoryQty: 54, weight: 330 },
            { id: 'var_38', title: 'Large / Forest', price: '79.99', compareAtPrice: null, sku: 'WB-LG-FO', inventoryQty: 42, weight: 360 },
            { id: 'var_39', title: 'Large / Slate', price: '79.99', compareAtPrice: null, sku: 'WB-LG-SL', inventoryQty: 29, weight: 360 }
        ],
        images: [{ alt: 'Recycled Polyester Windbreaker' }]
    },
    {
        id: 'prod_7',
        title: 'Silk Blend Scarf',
        description: 'Luxurious silk-cashmere blend scarf with hand-rolled edges. Limited edition print by artist Yuki Tanaka.',
        vendor: 'Atelier Goods',
        productType: 'Accessories',
        status: 'active',
        templateId: 'tmpl_2',
        hasGiftCardRecipientFields: false,
        createdAt: '2025-09-01T11:00:00Z',
        updatedAt: '2026-01-15T13:25:00Z',
        tags: ['silk', 'scarf', 'limited-edition', 'luxury'],
        variants: [
            { id: 'var_40', title: 'Midnight Garden', price: '124.99', compareAtPrice: null, sku: 'SC-MG', inventoryQty: 8, weight: 120 },
            { id: 'var_41', title: 'Ocean Wave', price: '124.99', compareAtPrice: null, sku: 'SC-OW', inventoryQty: 12, weight: 120 },
            { id: 'var_42', title: 'Sunset Bloom', price: '124.99', compareAtPrice: null, sku: 'SC-SB', inventoryQty: 5, weight: 120 }
        ],
        images: [{ alt: 'Silk Blend Scarf Midnight Garden' }]
    },
    {
        id: 'prod_8',
        title: 'Canvas Sneakers',
        description: 'Casual canvas sneakers with vulcanized rubber sole. Vegan-friendly and machine washable.',
        vendor: 'Stride Lab',
        productType: 'Footwear',
        status: 'active',
        templateId: 'tmpl_1',
        hasGiftCardRecipientFields: false,
        createdAt: '2025-08-10T10:00:00Z',
        updatedAt: '2026-02-22T14:00:00Z',
        tags: ['sneakers', 'vegan', 'casual', 'footwear'],
        variants: [
            { id: 'var_43', title: 'US 7 / White', price: '54.99', compareAtPrice: null, sku: 'CS-07-WH', inventoryQty: 33, weight: 450 },
            { id: 'var_44', title: 'US 8 / White', price: '54.99', compareAtPrice: null, sku: 'CS-08-WH', inventoryQty: 48, weight: 470 },
            { id: 'var_45', title: 'US 9 / White', price: '54.99', compareAtPrice: null, sku: 'CS-09-WH', inventoryQty: 62, weight: 490 },
            { id: 'var_46', title: 'US 10 / White', price: '54.99', compareAtPrice: null, sku: 'CS-10-WH', inventoryQty: 55, weight: 510 },
            { id: 'var_47', title: 'US 7 / Black', price: '54.99', compareAtPrice: null, sku: 'CS-07-BK', inventoryQty: 41, weight: 450 },
            { id: 'var_48', title: 'US 8 / Black', price: '54.99', compareAtPrice: null, sku: 'CS-08-BK', inventoryQty: 57, weight: 470 },
            { id: 'var_49', title: 'US 9 / Black', price: '54.99', compareAtPrice: null, sku: 'CS-09-BK', inventoryQty: 69, weight: 490 },
            { id: 'var_50', title: 'US 10 / Black', price: '54.99', compareAtPrice: null, sku: 'CS-10-BK', inventoryQty: 44, weight: 510 },
            { id: 'var_51', title: 'US 11 / Black', price: '54.99', compareAtPrice: null, sku: 'CS-11-BK', inventoryQty: 22, weight: 530 }
        ],
        images: [{ alt: 'Canvas Sneakers White' }]
    },
    {
        id: 'prod_9',
        title: 'Linen Blend Blazer',
        description: 'Unstructured linen-cotton blazer with patch pockets. Perfect for warm-weather dressing.',
        vendor: 'Urban Thread Co.',
        productType: 'Apparel',
        status: 'active',
        templateId: 'tmpl_1',
        hasGiftCardRecipientFields: false,
        createdAt: '2025-10-05T08:45:00Z',
        updatedAt: '2026-02-14T12:30:00Z',
        tags: ['linen', 'blazer', 'summer', 'business-casual'],
        variants: [
            { id: 'var_52', title: 'Small / Sand', price: '139.99', compareAtPrice: '179.99', sku: 'BL-SM-SA', inventoryQty: 18, weight: 500 },
            { id: 'var_53', title: 'Medium / Sand', price: '139.99', compareAtPrice: '179.99', sku: 'BL-MD-SA', inventoryQty: 27, weight: 540 },
            { id: 'var_54', title: 'Large / Sand', price: '139.99', compareAtPrice: '179.99', sku: 'BL-LG-SA', inventoryQty: 21, weight: 580 },
            { id: 'var_55', title: 'Small / Slate Blue', price: '139.99', compareAtPrice: '179.99', sku: 'BL-SM-SB', inventoryQty: 14, weight: 500 },
            { id: 'var_56', title: 'Medium / Slate Blue', price: '139.99', compareAtPrice: '179.99', sku: 'BL-MD-SB', inventoryQty: 32, weight: 540 },
            { id: 'var_57', title: 'Large / Slate Blue', price: '139.99', compareAtPrice: '179.99', sku: 'BL-LG-SB', inventoryQty: 16, weight: 580 }
        ],
        images: [{ alt: 'Linen Blend Blazer in sand' }]
    },
    {
        id: 'prod_10',
        title: 'Organic Denim Jacket',
        description: 'Classic trucker jacket in organic selvedge denim. Raw indigo with natural fade potential.',
        vendor: 'Urban Thread Co.',
        productType: 'Outerwear',
        status: 'active',
        templateId: 'tmpl_1',
        hasGiftCardRecipientFields: false,
        createdAt: '2025-11-01T07:30:00Z',
        updatedAt: '2026-02-26T09:50:00Z',
        tags: ['denim', 'organic', 'jacket', 'selvedge'],
        variants: [
            { id: 'var_58', title: 'Small / Raw Indigo', price: '129.99', compareAtPrice: null, sku: 'DJ-SM-RI', inventoryQty: 35, weight: 750 },
            { id: 'var_59', title: 'Medium / Raw Indigo', price: '129.99', compareAtPrice: null, sku: 'DJ-MD-RI', inventoryQty: 48, weight: 800 },
            { id: 'var_60', title: 'Large / Raw Indigo', price: '129.99', compareAtPrice: null, sku: 'DJ-LG-RI', inventoryQty: 29, weight: 850 },
            { id: 'var_61', title: 'XL / Raw Indigo', price: '129.99', compareAtPrice: null, sku: 'DJ-XL-RI', inventoryQty: 17, weight: 900 }
        ],
        images: [{ alt: 'Organic Denim Jacket' }]
    },
    {
        id: 'prod_11',
        title: 'Titanium Watch – Miyota Movement',
        description: 'Minimalist titanium watch with Japanese Miyota automatic movement. Sapphire crystal, 100m water resistance.',
        vendor: 'Stride Lab',
        productType: 'Accessories',
        status: 'active',
        templateId: 'tmpl_1',
        hasGiftCardRecipientFields: false,
        createdAt: '2025-12-01T14:00:00Z',
        updatedAt: '2026-02-27T11:40:00Z',
        tags: ['watch', 'titanium', 'automatic', 'premium'],
        variants: [
            { id: 'var_62', title: 'Brushed Silver / 40mm', price: '349.99', compareAtPrice: null, sku: 'TW-SV-40', inventoryQty: 11, weight: 95 },
            { id: 'var_63', title: 'Matte Black / 40mm', price: '349.99', compareAtPrice: null, sku: 'TW-BK-40', inventoryQty: 8, weight: 95 },
            { id: 'var_64', title: 'Brushed Silver / 42mm', price: '369.99', compareAtPrice: null, sku: 'TW-SV-42', inventoryQty: 6, weight: 105 },
            { id: 'var_65', title: 'Matte Black / 42mm', price: '369.99', compareAtPrice: null, sku: 'TW-BK-42', inventoryQty: 4, weight: 105 }
        ],
        images: [{ alt: 'Titanium Watch Brushed Silver' }]
    },
    {
        id: 'prod_12',
        title: 'Bamboo Fiber Socks – 6 Pack',
        description: 'Breathable bamboo fiber crew socks with arch support. Antimicrobial and hypoallergenic.',
        vendor: 'Urban Thread Co.',
        productType: 'Apparel',
        status: 'active',
        templateId: 'tmpl_1',
        hasGiftCardRecipientFields: false,
        createdAt: '2025-05-20T09:15:00Z',
        updatedAt: '2026-01-30T10:00:00Z',
        tags: ['socks', 'bamboo', 'sustainable', 'basics'],
        variants: [
            { id: 'var_66', title: 'S-M / Mixed Earth', price: '34.99', compareAtPrice: null, sku: 'BS-SM-ME', inventoryQty: 220, weight: 200 },
            { id: 'var_67', title: 'M-L / Mixed Earth', price: '34.99', compareAtPrice: null, sku: 'BS-ML-ME', inventoryQty: 315, weight: 220 },
            { id: 'var_68', title: 'L-XL / Mixed Earth', price: '34.99', compareAtPrice: null, sku: 'BS-LX-ME', inventoryQty: 189, weight: 240 },
            { id: 'var_69', title: 'S-M / All Black', price: '34.99', compareAtPrice: null, sku: 'BS-SM-BK', inventoryQty: 278, weight: 200 },
            { id: 'var_70', title: 'M-L / All Black', price: '34.99', compareAtPrice: null, sku: 'BS-ML-BK', inventoryQty: 412, weight: 220 },
            { id: 'var_71', title: 'L-XL / All Black', price: '34.99', compareAtPrice: null, sku: 'BS-LX-BK', inventoryQty: 198, weight: 240 }
        ],
        images: [{ alt: 'Bamboo Fiber Socks 6 Pack' }]
    },
    {
        id: 'prod_13',
        title: 'Cashmere Beanie',
        description: 'Pure cashmere ribbed beanie with a fold-over brim. Lightweight warmth for cold days.',
        vendor: 'Atelier Goods',
        productType: 'Accessories',
        status: 'draft',
        templateId: 'tmpl_1',
        hasGiftCardRecipientFields: false,
        createdAt: '2026-01-10T08:00:00Z',
        updatedAt: '2026-02-28T16:30:00Z',
        tags: ['cashmere', 'beanie', 'winter', 'luxury'],
        variants: [
            { id: 'var_72', title: 'Oatmeal', price: '69.99', compareAtPrice: null, sku: 'CB-OAT', inventoryQty: 25, weight: 80 },
            { id: 'var_73', title: 'Charcoal', price: '69.99', compareAtPrice: null, sku: 'CB-CHR', inventoryQty: 30, weight: 80 },
            { id: 'var_74', title: 'Burgundy', price: '69.99', compareAtPrice: null, sku: 'CB-BUR', inventoryQty: 18, weight: 80 }
        ],
        images: [{ alt: 'Cashmere Beanie' }]
    },
    {
        id: 'prod_14',
        title: 'Stretch Yoga Pants',
        description: 'Four-way stretch yoga pants with hidden waistband pocket. Moisture-wicking and squat-proof.',
        vendor: 'Stride Lab',
        productType: 'Activewear',
        status: 'active',
        templateId: 'tmpl_1',
        hasGiftCardRecipientFields: false,
        createdAt: '2025-07-15T11:30:00Z',
        updatedAt: '2026-02-19T08:45:00Z',
        tags: ['yoga', 'activewear', 'stretch', 'athleisure'],
        variants: [
            { id: 'var_75', title: 'XS / Obsidian', price: '58.99', compareAtPrice: null, sku: 'YP-XS-OB', inventoryQty: 56, weight: 250 },
            { id: 'var_76', title: 'Small / Obsidian', price: '58.99', compareAtPrice: null, sku: 'YP-SM-OB', inventoryQty: 89, weight: 260 },
            { id: 'var_77', title: 'Medium / Obsidian', price: '58.99', compareAtPrice: null, sku: 'YP-MD-OB', inventoryQty: 112, weight: 280 },
            { id: 'var_78', title: 'Large / Obsidian', price: '58.99', compareAtPrice: null, sku: 'YP-LG-OB', inventoryQty: 67, weight: 300 },
            { id: 'var_79', title: 'Small / Sage', price: '58.99', compareAtPrice: null, sku: 'YP-SM-SG', inventoryQty: 74, weight: 260 },
            { id: 'var_80', title: 'Medium / Sage', price: '58.99', compareAtPrice: null, sku: 'YP-MD-SG', inventoryQty: 95, weight: 280 }
        ],
        images: [{ alt: 'Stretch Yoga Pants Obsidian' }]
    },
    {
        id: 'prod_15',
        title: 'Waxed Canvas Backpack',
        description: 'Heritage waxed canvas backpack with leather trim. Padded laptop compartment fits up to 15" devices.',
        vendor: 'Atelier Goods',
        productType: 'Bags',
        status: 'active',
        templateId: 'tmpl_2',
        hasGiftCardRecipientFields: false,
        createdAt: '2025-04-08T14:20:00Z',
        updatedAt: '2026-02-12T10:15:00Z',
        tags: ['backpack', 'canvas', 'waxed', 'laptop'],
        variants: [
            { id: 'var_81', title: 'Olive', price: '189.99', compareAtPrice: null, sku: 'WCB-OLV', inventoryQty: 19, weight: 1200 },
            { id: 'var_82', title: 'Navy', price: '189.99', compareAtPrice: null, sku: 'WCB-NVY', inventoryQty: 14, weight: 1200 }
        ],
        images: [{ alt: 'Waxed Canvas Backpack' }]
    },
    {
        id: 'prod_16',
        title: 'Performance Running Shorts',
        description: 'Ultralight running shorts with built-in liner. Side zip pocket for keys, reflective logo.',
        vendor: 'Stride Lab',
        productType: 'Activewear',
        status: 'active',
        templateId: 'tmpl_1',
        hasGiftCardRecipientFields: false,
        createdAt: '2025-06-25T13:00:00Z',
        updatedAt: '2026-02-21T09:20:00Z',
        tags: ['running', 'shorts', 'performance', 'activewear'],
        variants: [
            { id: 'var_83', title: 'Small / Carbon', price: '44.99', compareAtPrice: null, sku: 'RS-SM-CB', inventoryQty: 83, weight: 120 },
            { id: 'var_84', title: 'Medium / Carbon', price: '44.99', compareAtPrice: null, sku: 'RS-MD-CB', inventoryQty: 107, weight: 130 },
            { id: 'var_85', title: 'Large / Carbon', price: '44.99', compareAtPrice: null, sku: 'RS-LG-CB', inventoryQty: 91, weight: 140 },
            { id: 'var_86', title: 'Small / Electric Blue', price: '44.99', compareAtPrice: null, sku: 'RS-SM-EB', inventoryQty: 64, weight: 120 },
            { id: 'var_87', title: 'Medium / Electric Blue', price: '44.99', compareAtPrice: null, sku: 'RS-MD-EB', inventoryQty: 78, weight: 130 }
        ],
        images: [{ alt: 'Performance Running Shorts' }]
    },
    {
        id: 'prod_17',
        title: 'Hand-Poured Soy Candle Set',
        description: 'Set of 3 hand-poured soy candles with cotton wicks. Scents: Cedar & Sage, Lavender Fields, Citrus Grove. 40hr burn time each.',
        vendor: 'Home & Gather',
        productType: 'Home',
        status: 'active',
        templateId: 'tmpl_1',
        hasGiftCardRecipientFields: false,
        createdAt: '2025-09-18T10:45:00Z',
        updatedAt: '2026-02-15T14:00:00Z',
        tags: ['candles', 'home', 'soy', 'gift-set'],
        variants: [
            { id: 'var_88', title: 'Classic Collection', price: '42.99', compareAtPrice: null, sku: 'CND-CLC', inventoryQty: 156, weight: 900 },
            { id: 'var_89', title: 'Seasonal Collection', price: '44.99', compareAtPrice: null, sku: 'CND-SSN', inventoryQty: 89, weight: 900 }
        ],
        images: [{ alt: 'Soy Candle Set' }]
    },
    {
        id: 'prod_18',
        title: 'Heavyweight Hoodie – Oversized Fit',
        description: '400gsm heavyweight french terry hoodie. Double-lined hood, kangaroo pocket, ribbed cuffs. Intentionally oversized.',
        vendor: 'Urban Thread Co.',
        productType: 'Apparel',
        status: 'archived',
        templateId: 'tmpl_1',
        hasGiftCardRecipientFields: false,
        createdAt: '2024-10-01T08:00:00Z',
        updatedAt: '2025-12-15T09:30:00Z',
        tags: ['hoodie', 'heavyweight', 'oversized', 'streetwear'],
        variants: [
            { id: 'var_90', title: 'M / Washed Black', price: '89.99', compareAtPrice: null, sku: 'HH-MD-WB', inventoryQty: 0, weight: 700 },
            { id: 'var_91', title: 'L / Washed Black', price: '89.99', compareAtPrice: null, sku: 'HH-LG-WB', inventoryQty: 0, weight: 750 },
            { id: 'var_92', title: 'XL / Washed Black', price: '89.99', compareAtPrice: null, sku: 'HH-XL-WB', inventoryQty: 2, weight: 800 }
        ],
        images: [{ alt: 'Heavyweight Hoodie' }]
    },
    {
        id: 'prod_19',
        title: 'Ceramic Pour-Over Coffee Set',
        description: 'Handmade ceramic pour-over dripper with matching carafe. Includes 100 paper filters.',
        vendor: 'Home & Gather',
        productType: 'Home',
        status: 'active',
        templateId: 'tmpl_1',
        hasGiftCardRecipientFields: false,
        createdAt: '2025-08-28T09:30:00Z',
        updatedAt: '2026-02-23T11:00:00Z',
        tags: ['coffee', 'ceramic', 'pour-over', 'kitchen'],
        variants: [
            { id: 'var_93', title: 'Matte White', price: '68.99', compareAtPrice: null, sku: 'PO-WHT', inventoryQty: 42, weight: 1100 },
            { id: 'var_94', title: 'Speckled Grey', price: '68.99', compareAtPrice: null, sku: 'PO-GRY', inventoryQty: 31, weight: 1100 },
            { id: 'var_95', title: 'Midnight Blue', price: '72.99', compareAtPrice: null, sku: 'PO-BLU', inventoryQty: 24, weight: 1100 }
        ],
        images: [{ alt: 'Pour-Over Coffee Set' }]
    },
    {
        id: 'prod_20',
        title: 'Merino Wool Base Layer – Long Sleeve',
        description: '180gsm merino wool base layer. Flatlock seams, thumbhole cuffs, odor-resistant. For hiking, skiing, and everyday wear.',
        vendor: 'Stride Lab',
        productType: 'Activewear',
        status: 'active',
        templateId: 'tmpl_1',
        hasGiftCardRecipientFields: false,
        createdAt: '2025-10-20T08:00:00Z',
        updatedAt: '2026-02-24T15:30:00Z',
        tags: ['merino', 'base-layer', 'outdoor', 'thermal'],
        variants: [
            { id: 'var_96', title: 'Small / Black', price: '79.99', compareAtPrice: null, sku: 'BL-SM-BK', inventoryQty: 53, weight: 200 },
            { id: 'var_97', title: 'Medium / Black', price: '79.99', compareAtPrice: null, sku: 'BL-MD-BK', inventoryQty: 78, weight: 220 },
            { id: 'var_98', title: 'Large / Black', price: '79.99', compareAtPrice: null, sku: 'BL-LG-BK', inventoryQty: 61, weight: 240 },
            { id: 'var_99', title: 'Small / Deep Ocean', price: '79.99', compareAtPrice: null, sku: 'BL-SM-DO', inventoryQty: 44, weight: 200 },
            { id: 'var_100', title: 'Medium / Deep Ocean', price: '79.99', compareAtPrice: null, sku: 'BL-MD-DO', inventoryQty: 59, weight: 220 }
        ],
        images: [{ alt: 'Merino Wool Base Layer' }]
    }
];

// ---- Collections ----
const COLLECTIONS = [
    { id: 'col_1', title: 'New Arrivals', handle: 'new-arrivals', productIds: ['prod_11', 'prod_13', 'prod_19', 'prod_20'] },
    { id: 'col_2', title: 'Bestsellers', handle: 'bestsellers', productIds: ['prod_1', 'prod_3', 'prod_8', 'prod_12', 'prod_14'] },
    { id: 'col_3', title: 'Apparel', handle: 'apparel', productIds: ['prod_1', 'prod_2', 'prod_3', 'prod_9', 'prod_10', 'prod_12', 'prod_13', 'prod_18'] },
    { id: 'col_4', title: 'Accessories', handle: 'accessories', productIds: ['prod_4', 'prod_7', 'prod_11', 'prod_15'] },
    { id: 'col_5', title: 'Activewear', handle: 'activewear', productIds: ['prod_14', 'prod_16', 'prod_20'] },
    { id: 'col_6', title: 'Outerwear', handle: 'outerwear', productIds: ['prod_6', 'prod_10'] },
    { id: 'col_7', title: 'Home & Living', handle: 'home-living', productIds: ['prod_17', 'prod_19'] },
    { id: 'col_8', title: 'Footwear', handle: 'footwear', productIds: ['prod_8'] },
    { id: 'col_9', title: 'Gift Ideas', handle: 'gift-ideas', productIds: ['prod_5', 'prod_7', 'prod_17'] },
    { id: 'col_10', title: 'Sale', handle: 'sale', productIds: ['prod_2', 'prod_9'] },
    { id: 'col_11', title: 'Sustainable', handle: 'sustainable', productIds: ['prod_1', 'prod_6', 'prod_10', 'prod_12'] }
];

// ---- Installed Apps ----
const INSTALLED_APPS = [
    {
        id: 'app_1',
        name: 'Currency Converter Plus',
        appType: 'currency_converter',
        isActive: true,
        developer: 'Mlveda',
        description: 'Auto-detect visitor location and show prices in local currency.',
        installedAt: '2025-06-15T10:00:00Z',
        conflictsWithCheckout: true,
        conflictReason: 'Currency converters may interfere with accelerated checkout pricing.'
    },
    {
        id: 'app_2',
        name: 'CartHook Post Purchase Offers',
        appType: 'cart_interaction',
        isActive: false,
        developer: 'CartHook',
        description: 'Add post-purchase upsell offers after checkout.',
        installedAt: '2025-08-20T14:30:00Z',
        conflictsWithCheckout: true,
        conflictReason: 'Apps that interact with the cart may conflict with accelerated checkout.'
    },
    {
        id: 'app_3',
        name: 'Judge.me Product Reviews',
        appType: 'reviews',
        isActive: true,
        developer: 'Judge.me',
        description: 'Collect and display product reviews with photos.',
        installedAt: '2025-03-01T09:00:00Z',
        conflictsWithCheckout: false,
        conflictReason: null
    },
    {
        id: 'app_4',
        name: 'Oberlo Dropshipping',
        appType: 'external_checkout',
        isActive: true,
        developer: 'Oberlo',
        description: 'Source and ship products directly from suppliers.',
        installedAt: '2025-01-10T11:45:00Z',
        conflictsWithCheckout: true,
        conflictReason: 'Apps that take customers to an external checkout may conflict.'
    },
    {
        id: 'app_5',
        name: 'Klaviyo Email Marketing',
        appType: 'marketing',
        isActive: true,
        developer: 'Klaviyo',
        description: 'Email and SMS marketing automation.',
        installedAt: '2025-02-28T16:00:00Z',
        conflictsWithCheckout: false,
        conflictReason: null
    },
    {
        id: 'app_6',
        name: 'ReConvert Upsell & Cross Sell',
        appType: 'cart_interaction',
        isActive: true,
        developer: 'StilyoApps',
        description: 'Customize thank you page and add upsell funnels.',
        installedAt: '2025-07-05T08:15:00Z',
        conflictsWithCheckout: true,
        conflictReason: 'Apps that interact with the cart may conflict with accelerated checkout.'
    },
    {
        id: 'app_7',
        name: 'Shopify Inbox',
        appType: 'messaging',
        isActive: true,
        developer: 'Shopify',
        description: 'Chat with customers directly from your admin.',
        installedAt: '2024-12-01T10:00:00Z',
        conflictsWithCheckout: false,
        conflictReason: null
    },
    {
        id: 'app_8',
        name: 'Privy Pop Ups & Email',
        appType: 'marketing',
        isActive: false,
        developer: 'Privy',
        description: 'Email capture pop ups, banners, and flyouts.',
        installedAt: '2025-04-12T09:30:00Z',
        conflictsWithCheckout: false,
        conflictReason: null
    }
];

// ---- Cart Attributes ----
const CART_ATTRIBUTES = [
    {
        id: 'cattr_1',
        name: 'Gift wrapping',
        type: 'checkbox',
        isActive: true,
        description: 'Offer gift wrapping for an additional $5.00',
        conflictsWithCheckout: true
    },
    {
        id: 'cattr_2',
        name: 'Delivery date',
        type: 'date_picker',
        isActive: true,
        description: 'Let customers choose a preferred delivery date',
        conflictsWithCheckout: true
    },
    {
        id: 'cattr_3',
        name: 'Order notes',
        type: 'text',
        isActive: true,
        description: 'Free-form text field for special instructions',
        conflictsWithCheckout: false
    },
    {
        id: 'cattr_4',
        name: 'Terms and conditions',
        type: 'checkbox',
        isActive: false,
        description: 'Require customers to accept terms before checkout',
        conflictsWithCheckout: true
    }
];

// ---- Activity Log ----
const ACTIVITY_LOG = [
    { id: 'log_1', action: 'theme_published', themeId: 'theme_1', themeName: 'Dawn', userId: 'usr_owner_1', timestamp: '2026-02-28T14:32:00Z', details: 'Published Dawn v15.2.0' },
    { id: 'log_2', action: 'checkout_buttons_enabled', themeId: 'theme_1', templateId: 'tmpl_1', userId: 'usr_owner_1', timestamp: '2026-02-28T14:35:00Z', details: 'Enabled accelerated checkout on Default product template' },
    { id: 'log_3', action: 'payment_method_activated', paymentMethodId: 'pm_3', userId: 'usr_owner_1', timestamp: '2026-02-25T10:00:00Z', details: 'Activated Google Pay' },
    { id: 'log_4', action: 'template_created', themeId: 'theme_1', templateId: 'tmpl_2', userId: 'usr_owner_1', timestamp: '2025-08-22T10:30:00Z', details: 'Created alternate template: Product - No checkout buttons' },
    { id: 'log_5', action: 'product_template_changed', productId: 'prod_4', templateId: 'tmpl_2', userId: 'usr_owner_1', timestamp: '2025-08-23T09:15:00Z', details: 'Assigned Leather Crossbody Bag to alternate template' },
    { id: 'log_6', action: 'theme_color_changed', themeId: 'theme_1', userId: 'usr_owner_1', timestamp: '2026-02-20T11:00:00Z', details: 'Updated accelerated checkout button colors' },
    { id: 'log_7', action: 'checkout_buttons_disabled', themeId: 'theme_2', templateId: 'tmpl_4', userId: 'usr_owner_1', timestamp: '2026-02-18T14:20:00Z', details: 'Disabled accelerated checkout on Craft default template' },
    { id: 'log_8', action: 'payment_method_deactivated', paymentMethodId: 'pm_5', userId: 'usr_owner_1', timestamp: '2025-11-10T16:45:00Z', details: 'Deactivated Amazon Pay' },
    { id: 'log_9', action: 'shop_promise_disabled', userId: 'usr_owner_1', timestamp: '2026-01-05T09:30:00Z', details: 'Disabled Shop Promise' },
    { id: 'log_10', action: 'template_created', themeId: 'theme_1', templateId: 'tmpl_3', userId: 'usr_owner_1', timestamp: '2025-09-15T14:20:00Z', details: 'Created alternate template: Product - Gift cards' },
    { id: 'log_11', action: 'font_changed', themeId: 'theme_1', userId: 'usr_owner_1', timestamp: '2026-02-10T13:40:00Z', details: 'Changed button font to Assistant' },
    { id: 'log_12', action: 'featured_product_section_added', themeId: 'theme_1', sectionId: 'sec_1', userId: 'usr_owner_1', timestamp: '2026-01-15T10:20:00Z', details: 'Added Featured product section to Home page' },
    { id: 'log_13', action: 'product_template_changed', productId: 'prod_7', templateId: 'tmpl_2', userId: 'usr_owner_1', timestamp: '2025-09-05T11:30:00Z', details: 'Assigned Silk Blend Scarf to No checkout buttons template' },
    { id: 'log_14', action: 'product_template_changed', productId: 'prod_15', templateId: 'tmpl_2', userId: 'usr_owner_1', timestamp: '2025-09-06T08:45:00Z', details: 'Assigned Waxed Canvas Backpack to No checkout buttons template' },
    { id: 'log_15', action: 'section_checkout_toggled', themeId: 'theme_1', sectionId: 'sec_1', userId: 'usr_owner_1', timestamp: '2026-02-01T14:15:00Z', details: 'Enabled accelerated checkout on Home page featured product' }
];

// ---- Available Fonts ----
const AVAILABLE_FONTS = [
    'Assistant', 'Inter', 'Roboto', 'Open Sans', 'Lato', 'Montserrat',
    'Poppins', 'Source Sans Pro', 'Playfair Display', 'DM Serif Display',
    'DM Sans', 'Merriweather', 'Lora', 'Nunito', 'Raleway', 'Work Sans',
    'Oswald', 'PT Sans', 'Cabin', 'Libre Baskerville'
];

// ---- ID Counters ----
const INITIAL_NEXT_IDS = {
    _nextThemeId: 7,
    _nextTemplateId: 10,
    _nextSectionId: 8,
    _nextProductId: 21,
    _nextAppId: 9,
    _nextLogId: 16,
    _nextCartAttrId: 5,
    _nextCollectionId: 12
};

// Export for use by state.js
const SeedData = {
    SEED_DATA_VERSION,
    CURRENT_USER,
    THEMES,
    TEMPLATES,
    THEME_PAGES,
    THEME_SECTIONS,
    PAYMENT_METHODS,
    SHOP_PROMISE,
    PRODUCTS,
    COLLECTIONS,
    INSTALLED_APPS,
    CART_ATTRIBUTES,
    ACTIVITY_LOG,
    AVAILABLE_FONTS,
    INITIAL_NEXT_IDS
};
