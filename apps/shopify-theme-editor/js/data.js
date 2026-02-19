// ============================================================
// data.js — Rich, realistic mock data for Shopify Theme Editor
// ============================================================

const SEED_DATA_VERSION = 1;

// ---- Theme Architecture Types ----
const ARCHITECTURE_TYPES = {
    VINTAGE: 'vintage',
    ONLINE_STORE_2: 'online_store_2.0',
    THEME_BLOCKS: 'theme_blocks'
};

// ---- Theme Statuses ----
const THEME_STATUS = {
    LIVE: 'live',
    DRAFT: 'draft',
    TRIAL: 'trial'
};

// ---- Visibility / Template Types ----
const TEMPLATE_TYPES = [
    'product', 'collection', 'collections-list', 'page', 'blog',
    'blog-post', 'cart', 'search', 'gift-card', 'password', '404'
];

// ---- Section Areas ----
const SECTION_AREAS = {
    HEADER: 'header',
    TEMPLATE: 'template',
    FOOTER: 'footer'
};

// ---- Cart Display Types ----
const CART_TYPES = {
    DRAWER: 'drawer',
    PAGE: 'page',
    POPUP: 'popup'
};

// ---- Animation Types ----
const HOVER_EFFECTS = {
    NONE: 'none',
    VERTICAL_LIFT: 'vertical-lift',
    THREE_D_LIFT: '3d-lift'
};

// ---- Badge Shapes ----
const BADGE_SHAPES = {
    RECTANGLE: 'rectangle',
    CIRCLE: 'circle'
};

// ---- Badge Positions ----
const BADGE_POSITIONS = {
    TOP_LEFT: 'top-left',
    TOP_RIGHT: 'top-right',
    BOTTOM_LEFT: 'bottom-left',
    BOTTOM_RIGHT: 'bottom-right'
};

// ---- Button Styles ----
const BUTTON_STYLES = {
    ROUNDED: 'rounded',
    SQUARE: 'square',
    PILL: 'pill'
};

// ---- Input Styles ----
const INPUT_STYLES = {
    OUTLINED: 'outlined',
    FILLED: 'filled',
    UNDERLINED: 'underlined'
};

// ---- Current User (Store Owner) ----
const CURRENT_USER = {
    id: 1,
    name: 'Olivia Chen',
    email: 'olivia@northwindtraders.com',
    storeName: 'Northwind Traders',
    storeUrl: 'northwind-traders.myshopify.com',
    plan: 'advanced',
    maxThemes: 20
};

// ---- Color Schemes ----
const DEFAULT_COLOR_SCHEMES = [
    {
        id: 1, name: 'Scheme 1', isDefault: true,
        background: '#ffffff', backgroundGradient: '',
        text: '#121212', solidButtonBg: '#121212',
        solidButtonText: '#ffffff', outlineButton: '#121212',
        shadow: '#121212'
    },
    {
        id: 2, name: 'Scheme 2', isDefault: false,
        background: '#f3f3f3', backgroundGradient: '',
        text: '#1a1a1a', solidButtonBg: '#1a1a1a',
        solidButtonText: '#f3f3f3', outlineButton: '#1a1a1a',
        shadow: '#1a1a1a'
    },
    {
        id: 3, name: 'Accent', isDefault: false,
        background: '#2c5f2d', backgroundGradient: '',
        text: '#ffffff', solidButtonBg: '#97bc62',
        solidButtonText: '#2c5f2d', outlineButton: '#ffffff',
        shadow: '#1a3a1c'
    },
    {
        id: 4, name: 'Dark Mode', isDefault: false,
        background: '#1a1a2e', backgroundGradient: '',
        text: '#e0e0e0', solidButtonBg: '#e94560',
        solidButtonText: '#ffffff', outlineButton: '#e94560',
        shadow: '#0f0f1a'
    },
    {
        id: 5, name: 'Warm Earth', isDefault: false,
        background: '#fdf6ec', backgroundGradient: '',
        text: '#3d2c1e', solidButtonBg: '#c8553d',
        solidButtonText: '#fdf6ec', outlineButton: '#c8553d',
        shadow: '#3d2c1e'
    }
];

// ---- Social Media Links ----
const DEFAULT_SOCIAL_LINKS = {
    instagram: 'https://instagram.com/northwindtraders',
    tiktok: '',
    facebook: 'https://facebook.com/northwindtraders',
    pinterest: 'https://pinterest.com/northwindtraders',
    twitter: 'https://twitter.com/northwindtraders',
    youtube: '',
    linkedin: '',
    snapchat: '',
    tumblr: '',
    vimeo: ''
};

// ---- Section Types ----
const SECTION_TYPES = [
    { id: 'announcement-bar', name: 'Announcement bar', area: 'header', icon: 'M' },
    { id: 'header', name: 'Header', area: 'header', icon: 'H' },
    { id: 'image-banner', name: 'Image banner', area: 'template', icon: 'I' },
    { id: 'rich-text', name: 'Rich text', area: 'template', icon: 'T' },
    { id: 'featured-collection', name: 'Featured collection', area: 'template', icon: 'C' },
    { id: 'collage', name: 'Collage', area: 'template', icon: 'G' },
    { id: 'collection-list', name: 'Collection list', area: 'template', icon: 'L' },
    { id: 'image-with-text', name: 'Image with text', area: 'template', icon: 'P' },
    { id: 'multicolumn', name: 'Multicolumn', area: 'template', icon: 'M' },
    { id: 'slideshow', name: 'Slideshow', area: 'template', icon: 'S' },
    { id: 'video', name: 'Video', area: 'template', icon: 'V' },
    { id: 'newsletter', name: 'Email signup', area: 'template', icon: 'E' },
    { id: 'contact-form', name: 'Contact form', area: 'template', icon: 'F' },
    { id: 'map', name: 'Map', area: 'template', icon: 'M' },
    { id: 'custom-liquid', name: 'Custom Liquid', area: 'template', icon: 'L' },
    { id: 'product-grid', name: 'Product grid', area: 'template', icon: 'G' },
    { id: 'related-products', name: 'Related products', area: 'template', icon: 'R' },
    { id: 'blog-posts', name: 'Blog posts', area: 'template', icon: 'B' },
    { id: 'footer', name: 'Footer', area: 'footer', icon: 'F' },
    { id: 'cart-items', name: 'Cart items', area: 'template', icon: 'C' },
    { id: 'cart-subtotal', name: 'Subtotal', area: 'template', icon: 'S' },
    { id: 'search-results', name: 'Search results', area: 'template', icon: 'S' },
    { id: 'password-header', name: 'Password header', area: 'header', icon: 'P' },
    { id: 'password-footer', name: 'Password footer', area: 'footer', icon: 'P' }
];

// ---- Block Types ----
const BLOCK_TYPES = [
    { id: 'heading', name: 'Heading', sections: ['rich-text', 'image-banner', 'image-with-text', 'collage'] },
    { id: 'text', name: 'Text', sections: ['rich-text', 'image-banner', 'image-with-text', 'multicolumn'] },
    { id: 'button', name: 'Button', sections: ['rich-text', 'image-banner', 'image-with-text', 'slideshow'] },
    { id: 'image', name: 'Image', sections: ['collage', 'multicolumn', 'image-with-text', 'slideshow'] },
    { id: 'link', name: 'Link', sections: ['announcement-bar', 'footer'] },
    { id: 'email-form', name: 'Email form', sections: ['newsletter'] },
    { id: 'product-card', name: 'Product card', sections: ['featured-collection', 'product-grid', 'related-products'] },
    { id: 'collection-card', name: 'Collection card', sections: ['collection-list'] },
    { id: 'menu', name: 'Menu column', sections: ['footer'] },
    { id: 'brand-info', name: 'Brand information', sections: ['footer'] },
    { id: 'social-links', name: 'Social links', sections: ['footer'] },
    { id: 'video-block', name: 'Video', sections: ['collage', 'multicolumn'] },
    { id: 'blog-post-card', name: 'Blog post card', sections: ['blog-posts'] },
    { id: 'search-input', name: 'Search input', sections: ['search-results'] },
    { id: 'announcement', name: 'Announcement', sections: ['announcement-bar'] },
    { id: 'mega-menu', name: 'Mega menu', sections: ['header'] },
    { id: 'slide', name: 'Slide', sections: ['slideshow'] },
    { id: 'column', name: 'Column', sections: ['multicolumn'] }
];

// ---- Themes ----
const THEMES = [
    {
        id: 1,
        name: 'Dawn',
        status: 'live',
        version: '15.0',
        architecture: ARCHITECTURE_TYPES.ONLINE_STORE_2,
        source: 'shopify',
        price: 0,
        lastSaved: '2026-02-18T14:22:00Z',
        createdAt: '2025-06-10T09:00:00Z',
        updatedAt: '2026-02-18T14:22:00Z',
        updateAvailable: true,
        updateVersion: '16.0',
        previewUrl: 'https://northwind-traders.myshopify.com/?preview_theme_id=1',
        customCss: '',
        themeStyle: 'default'
    },
    {
        id: 2,
        name: 'Craft',
        status: 'draft',
        version: '8.0',
        architecture: ARCHITECTURE_TYPES.ONLINE_STORE_2,
        source: 'shopify',
        price: 0,
        lastSaved: '2026-01-28T10:15:00Z',
        createdAt: '2025-08-20T11:00:00Z',
        updatedAt: '2026-01-28T10:15:00Z',
        updateAvailable: false,
        updateVersion: null,
        previewUrl: 'https://northwind-traders.myshopify.com/?preview_theme_id=2',
        customCss: '.hero-section { padding: 60px 0; }',
        themeStyle: 'default'
    },
    {
        id: 3,
        name: 'Sense',
        status: 'draft',
        version: '12.0',
        architecture: ARCHITECTURE_TYPES.ONLINE_STORE_2,
        source: 'shopify',
        price: 0,
        lastSaved: '2025-12-05T16:30:00Z',
        createdAt: '2025-04-15T08:00:00Z',
        updatedAt: '2025-12-05T16:30:00Z',
        updateAvailable: true,
        updateVersion: '13.2',
        previewUrl: 'https://northwind-traders.myshopify.com/?preview_theme_id=3',
        customCss: '',
        themeStyle: 'bold'
    },
    {
        id: 4,
        name: 'Ride',
        status: 'trial',
        version: '4.0',
        architecture: ARCHITECTURE_TYPES.THEME_BLOCKS,
        source: 'theme-store',
        price: 350,
        lastSaved: '2026-02-10T09:45:00Z',
        createdAt: '2026-01-15T14:00:00Z',
        updatedAt: '2026-02-10T09:45:00Z',
        updateAvailable: false,
        updateVersion: null,
        previewUrl: 'https://northwind-traders.myshopify.com/?preview_theme_id=4',
        customCss: '',
        themeStyle: 'sporty'
    },
    {
        id: 5,
        name: 'Impact',
        status: 'draft',
        version: '6.2',
        architecture: ARCHITECTURE_TYPES.THEME_BLOCKS,
        source: 'theme-store',
        price: 320,
        lastSaved: '2026-02-14T11:20:00Z',
        createdAt: '2025-11-01T10:00:00Z',
        updatedAt: '2026-02-14T11:20:00Z',
        updateAvailable: false,
        updateVersion: null,
        previewUrl: 'https://northwind-traders.myshopify.com/?preview_theme_id=5',
        customCss: '.product-title { font-weight: 900; }',
        themeStyle: 'bold'
    },
    {
        id: 6,
        name: 'Crave',
        status: 'draft',
        version: '3.1',
        architecture: ARCHITECTURE_TYPES.ONLINE_STORE_2,
        source: 'shopify',
        price: 0,
        lastSaved: '2025-09-18T08:30:00Z',
        createdAt: '2025-07-05T12:00:00Z',
        updatedAt: '2025-09-18T08:30:00Z',
        updateAvailable: true,
        updateVersion: '4.0',
        previewUrl: 'https://northwind-traders.myshopify.com/?preview_theme_id=6',
        customCss: '',
        themeStyle: 'default'
    },
    {
        id: 7,
        name: 'Copy of Dawn',
        status: 'draft',
        version: '15.0',
        architecture: ARCHITECTURE_TYPES.ONLINE_STORE_2,
        source: 'shopify',
        price: 0,
        lastSaved: '2026-02-01T13:00:00Z',
        createdAt: '2026-02-01T13:00:00Z',
        updatedAt: '2026-02-01T13:00:00Z',
        updateAvailable: false,
        updateVersion: null,
        previewUrl: 'https://northwind-traders.myshopify.com/?preview_theme_id=7',
        customCss: '',
        themeStyle: 'default'
    }
];

// ---- Templates ----
const TEMPLATES = [
    // Dawn (theme 1) templates
    { id: 1, themeId: 1, name: 'Default product', type: 'product', handle: 'product', isDefault: true },
    { id: 2, themeId: 1, name: 'Default collection', type: 'collection', handle: 'collection', isDefault: true },
    { id: 3, themeId: 1, name: 'Collections list', type: 'collections-list', handle: 'list-collections', isDefault: true },
    { id: 4, themeId: 1, name: 'Default page', type: 'page', handle: 'page', isDefault: true },
    { id: 5, themeId: 1, name: 'Contact', type: 'page', handle: 'contact', isDefault: false },
    { id: 6, themeId: 1, name: 'About', type: 'page', handle: 'about', isDefault: false },
    { id: 7, themeId: 1, name: 'Default blog', type: 'blog', handle: 'blog', isDefault: true },
    { id: 8, themeId: 1, name: 'Default blog post', type: 'blog-post', handle: 'article', isDefault: true },
    { id: 9, themeId: 1, name: 'Cart', type: 'cart', handle: 'cart', isDefault: true },
    { id: 10, themeId: 1, name: 'Search', type: 'search', handle: 'search', isDefault: true },
    { id: 11, themeId: 1, name: 'Gift card', type: 'gift-card', handle: 'gift_card', isDefault: true },
    { id: 12, themeId: 1, name: 'Password', type: 'password', handle: 'password', isDefault: true },
    { id: 13, themeId: 1, name: '404', type: '404', handle: '404', isDefault: true },
    { id: 14, themeId: 1, name: 'Featured product', type: 'product', handle: 'product.featured', isDefault: false },
    // Craft (theme 2) templates
    { id: 15, themeId: 2, name: 'Default product', type: 'product', handle: 'product', isDefault: true },
    { id: 16, themeId: 2, name: 'Default collection', type: 'collection', handle: 'collection', isDefault: true },
    { id: 17, themeId: 2, name: 'Default page', type: 'page', handle: 'page', isDefault: true },
    { id: 18, themeId: 2, name: 'Default blog', type: 'blog', handle: 'blog', isDefault: true },
    { id: 19, themeId: 2, name: 'Cart', type: 'cart', handle: 'cart', isDefault: true },
    { id: 20, themeId: 2, name: 'Search', type: 'search', handle: 'search', isDefault: true },
    { id: 21, themeId: 2, name: 'FAQ', type: 'page', handle: 'page.faq', isDefault: false },
    // Minimal templates for other themes
    { id: 22, themeId: 3, name: 'Default product', type: 'product', handle: 'product', isDefault: true },
    { id: 23, themeId: 3, name: 'Default collection', type: 'collection', handle: 'collection', isDefault: true },
    { id: 24, themeId: 3, name: 'Default page', type: 'page', handle: 'page', isDefault: true },
    { id: 25, themeId: 4, name: 'Default product', type: 'product', handle: 'product', isDefault: true },
    { id: 26, themeId: 4, name: 'Default collection', type: 'collection', handle: 'collection', isDefault: true },
    { id: 27, themeId: 5, name: 'Default product', type: 'product', handle: 'product', isDefault: true },
    { id: 28, themeId: 5, name: 'Default collection', type: 'collection', handle: 'collection', isDefault: true },
    { id: 29, themeId: 6, name: 'Default product', type: 'product', handle: 'product', isDefault: true },
    { id: 30, themeId: 6, name: 'Default page', type: 'page', handle: 'page', isDefault: true },
    { id: 31, themeId: 7, name: 'Default product', type: 'product', handle: 'product', isDefault: true },
    { id: 32, themeId: 7, name: 'Default collection', type: 'collection', handle: 'collection', isDefault: true }
];

// ---- Sections (instances within templates) ----
const SECTIONS = [
    // Dawn default product template (template 1)
    { id: 1, templateId: 1, themeId: 1, type: 'header', name: 'Header', area: 'header', position: 0, hidden: false, customCss: '', colorSchemeId: 1 },
    { id: 2, templateId: 1, themeId: 1, type: 'announcement-bar', name: 'Announcement bar', area: 'header', position: 1, hidden: false, customCss: '', colorSchemeId: 3 },
    { id: 3, templateId: 1, themeId: 1, type: 'image-banner', name: 'Image banner', area: 'template', position: 0, hidden: false, customCss: '', colorSchemeId: 1 },
    { id: 4, templateId: 1, themeId: 1, type: 'rich-text', name: 'Rich text', area: 'template', position: 1, hidden: false, customCss: '', colorSchemeId: 1 },
    { id: 5, templateId: 1, themeId: 1, type: 'featured-collection', name: 'Featured collection', area: 'template', position: 2, hidden: false, customCss: '', colorSchemeId: 2 },
    { id: 6, templateId: 1, themeId: 1, type: 'related-products', name: 'Related products', area: 'template', position: 3, hidden: true, customCss: '', colorSchemeId: 1 },
    { id: 7, templateId: 1, themeId: 1, type: 'newsletter', name: 'Email signup', area: 'template', position: 4, hidden: false, customCss: '', colorSchemeId: 4 },
    { id: 8, templateId: 1, themeId: 1, type: 'footer', name: 'Footer', area: 'footer', position: 0, hidden: false, customCss: '', colorSchemeId: 1 },

    // Dawn default collection template (template 2)
    { id: 9, templateId: 2, themeId: 1, type: 'header', name: 'Header', area: 'header', position: 0, hidden: false, customCss: '', colorSchemeId: 1 },
    { id: 10, templateId: 2, themeId: 1, type: 'product-grid', name: 'Product grid', area: 'template', position: 0, hidden: false, customCss: '', colorSchemeId: 1 },
    { id: 11, templateId: 2, themeId: 1, type: 'newsletter', name: 'Email signup', area: 'template', position: 1, hidden: false, customCss: '', colorSchemeId: 4 },
    { id: 12, templateId: 2, themeId: 1, type: 'footer', name: 'Footer', area: 'footer', position: 0, hidden: false, customCss: '', colorSchemeId: 1 },

    // Dawn default page template (template 4)
    { id: 13, templateId: 4, themeId: 1, type: 'header', name: 'Header', area: 'header', position: 0, hidden: false, customCss: '', colorSchemeId: 1 },
    { id: 14, templateId: 4, themeId: 1, type: 'rich-text', name: 'Rich text', area: 'template', position: 0, hidden: false, customCss: '', colorSchemeId: 1 },
    { id: 15, templateId: 4, themeId: 1, type: 'image-with-text', name: 'Image with text', area: 'template', position: 1, hidden: false, customCss: '', colorSchemeId: 2 },
    { id: 16, templateId: 4, themeId: 1, type: 'footer', name: 'Footer', area: 'footer', position: 0, hidden: false, customCss: '', colorSchemeId: 1 },

    // Dawn Contact template (template 5)
    { id: 17, templateId: 5, themeId: 1, type: 'header', name: 'Header', area: 'header', position: 0, hidden: false, customCss: '', colorSchemeId: 1 },
    { id: 18, templateId: 5, themeId: 1, type: 'contact-form', name: 'Contact form', area: 'template', position: 0, hidden: false, customCss: '', colorSchemeId: 1 },
    { id: 19, templateId: 5, themeId: 1, type: 'map', name: 'Map', area: 'template', position: 1, hidden: true, customCss: '', colorSchemeId: 1 },
    { id: 20, templateId: 5, themeId: 1, type: 'footer', name: 'Footer', area: 'footer', position: 0, hidden: false, customCss: '', colorSchemeId: 1 },

    // Dawn About template (template 6)
    { id: 21, templateId: 6, themeId: 1, type: 'header', name: 'Header', area: 'header', position: 0, hidden: false, customCss: '', colorSchemeId: 1 },
    { id: 22, templateId: 6, themeId: 1, type: 'image-banner', name: 'Hero banner', area: 'template', position: 0, hidden: false, customCss: '', colorSchemeId: 3 },
    { id: 23, templateId: 6, themeId: 1, type: 'rich-text', name: 'Our story', area: 'template', position: 1, hidden: false, customCss: '', colorSchemeId: 1 },
    { id: 24, templateId: 6, themeId: 1, type: 'multicolumn', name: 'Team members', area: 'template', position: 2, hidden: false, customCss: '', colorSchemeId: 2 },
    { id: 25, templateId: 6, themeId: 1, type: 'image-with-text', name: 'Mission statement', area: 'template', position: 3, hidden: false, customCss: '', colorSchemeId: 5 },
    { id: 26, templateId: 6, themeId: 1, type: 'footer', name: 'Footer', area: 'footer', position: 0, hidden: false, customCss: '', colorSchemeId: 1 },

    // Dawn Cart template (template 9)
    { id: 27, templateId: 9, themeId: 1, type: 'header', name: 'Header', area: 'header', position: 0, hidden: false, customCss: '', colorSchemeId: 1 },
    { id: 28, templateId: 9, themeId: 1, type: 'cart-items', name: 'Cart items', area: 'template', position: 0, hidden: false, customCss: '', colorSchemeId: 1 },
    { id: 29, templateId: 9, themeId: 1, type: 'cart-subtotal', name: 'Subtotal', area: 'template', position: 1, hidden: false, customCss: '', colorSchemeId: 1 },
    { id: 30, templateId: 9, themeId: 1, type: 'featured-collection', name: 'You may also like', area: 'template', position: 2, hidden: false, customCss: '', colorSchemeId: 2 },
    { id: 31, templateId: 9, themeId: 1, type: 'footer', name: 'Footer', area: 'footer', position: 0, hidden: false, customCss: '', colorSchemeId: 1 },

    // Dawn Blog template (template 7)
    { id: 32, templateId: 7, themeId: 1, type: 'header', name: 'Header', area: 'header', position: 0, hidden: false, customCss: '', colorSchemeId: 1 },
    { id: 33, templateId: 7, themeId: 1, type: 'blog-posts', name: 'Blog posts', area: 'template', position: 0, hidden: false, customCss: '', colorSchemeId: 1 },
    { id: 34, templateId: 7, themeId: 1, type: 'footer', name: 'Footer', area: 'footer', position: 0, hidden: false, customCss: '', colorSchemeId: 1 },

    // Dawn Password template (template 12)
    { id: 35, templateId: 12, themeId: 1, type: 'password-header', name: 'Password header', area: 'header', position: 0, hidden: false, customCss: '', colorSchemeId: 1 },
    { id: 36, templateId: 12, themeId: 1, type: 'newsletter', name: 'Email signup banner', area: 'template', position: 0, hidden: false, customCss: '', colorSchemeId: 4 },
    { id: 37, templateId: 12, themeId: 1, type: 'password-footer', name: 'Password footer', area: 'footer', position: 0, hidden: false, customCss: '', colorSchemeId: 1 },

    // Craft default product template (template 15)
    { id: 38, templateId: 15, themeId: 2, type: 'header', name: 'Header', area: 'header', position: 0, hidden: false, customCss: '', colorSchemeId: 1 },
    { id: 39, templateId: 15, themeId: 2, type: 'image-banner', name: 'Image banner', area: 'template', position: 0, hidden: false, customCss: '', colorSchemeId: 1 },
    { id: 40, templateId: 15, themeId: 2, type: 'featured-collection', name: 'Featured collection', area: 'template', position: 1, hidden: false, customCss: '', colorSchemeId: 2 },
    { id: 41, templateId: 15, themeId: 2, type: 'footer', name: 'Footer', area: 'footer', position: 0, hidden: false, customCss: '', colorSchemeId: 1 }
];

// ---- Blocks (within sections) ----
const BLOCKS = [
    // Announcement bar blocks (section 2)
    { id: 1, sectionId: 2, themeId: 1, type: 'announcement', name: 'Announcement', position: 0, hidden: false, settings: { text: 'Free shipping on orders over $75', link: '/collections/all' } },
    { id: 2, sectionId: 2, themeId: 1, type: 'announcement', name: 'Sale announcement', position: 1, hidden: false, settings: { text: 'Winter Sale - Up to 40% off selected items', link: '/collections/sale' } },

    // Image banner blocks (section 3)
    { id: 3, sectionId: 3, themeId: 1, type: 'heading', name: 'Heading', position: 0, hidden: false, settings: { text: 'Welcome to Northwind Traders', size: 'h1' } },
    { id: 4, sectionId: 3, themeId: 1, type: 'text', name: 'Subheading', position: 1, hidden: false, settings: { text: 'Discover our curated collection of premium goods' } },
    { id: 5, sectionId: 3, themeId: 1, type: 'button', name: 'Shop now button', position: 2, hidden: false, settings: { text: 'Shop now', link: '/collections/all', style: 'solid' } },

    // Rich text blocks (section 4)
    { id: 6, sectionId: 4, themeId: 1, type: 'heading', name: 'Heading', position: 0, hidden: false, settings: { text: 'About Our Collection', size: 'h2' } },
    { id: 7, sectionId: 4, themeId: 1, type: 'text', name: 'Description', position: 1, hidden: false, settings: { text: 'Each product in our store is thoughtfully sourced from artisans around the world.' } },
    { id: 8, sectionId: 4, themeId: 1, type: 'button', name: 'Learn more', position: 2, hidden: false, settings: { text: 'Learn more', link: '/pages/about', style: 'outline' } },

    // Email signup blocks (section 7)
    { id: 9, sectionId: 7, themeId: 1, type: 'heading', name: 'Heading', position: 0, hidden: false, settings: { text: 'Subscribe to our newsletter', size: 'h2' } },
    { id: 10, sectionId: 7, themeId: 1, type: 'text', name: 'Description', position: 1, hidden: false, settings: { text: 'Be the first to know about new collections and exclusive offers.' } },
    { id: 11, sectionId: 7, themeId: 1, type: 'email-form', name: 'Email form', position: 2, hidden: false, settings: {} },

    // Footer blocks (section 8)
    { id: 12, sectionId: 8, themeId: 1, type: 'menu', name: 'Quick links', position: 0, hidden: false, settings: { title: 'Quick links', menu: 'main-menu' } },
    { id: 13, sectionId: 8, themeId: 1, type: 'menu', name: 'Customer service', position: 1, hidden: false, settings: { title: 'Customer Service', menu: 'footer' } },
    { id: 14, sectionId: 8, themeId: 1, type: 'brand-info', name: 'Brand information', position: 2, hidden: false, settings: {} },
    { id: 15, sectionId: 8, themeId: 1, type: 'social-links', name: 'Social links', position: 3, hidden: false, settings: {} },

    // About page blocks (template 6)
    // Hero banner blocks (section 22)
    { id: 16, sectionId: 22, themeId: 1, type: 'heading', name: 'Heading', position: 0, hidden: false, settings: { text: 'Our Story', size: 'h1' } },
    { id: 17, sectionId: 22, themeId: 1, type: 'text', name: 'Subtitle', position: 1, hidden: false, settings: { text: 'Crafting excellence since 2018' } },

    // Our story blocks (section 23)
    { id: 18, sectionId: 23, themeId: 1, type: 'heading', name: 'Heading', position: 0, hidden: false, settings: { text: 'What We Believe', size: 'h2' } },
    { id: 19, sectionId: 23, themeId: 1, type: 'text', name: 'Content', position: 1, hidden: false, settings: { text: 'At Northwind Traders, we believe in sustainable sourcing and fair trade practices.' } },

    // Team members blocks (section 24)
    { id: 20, sectionId: 24, themeId: 1, type: 'column', name: 'Olivia Chen', position: 0, hidden: false, settings: { title: 'Olivia Chen', text: 'Founder & CEO' } },
    { id: 21, sectionId: 24, themeId: 1, type: 'column', name: 'Marcus Rivera', position: 1, hidden: false, settings: { title: 'Marcus Rivera', text: 'Head of Design' } },
    { id: 22, sectionId: 24, themeId: 1, type: 'column', name: 'Aisha Patel', position: 2, hidden: false, settings: { title: 'Aisha Patel', text: 'Operations Manager' } },

    // Mission statement blocks (section 25)
    { id: 23, sectionId: 25, themeId: 1, type: 'heading', name: 'Heading', position: 0, hidden: false, settings: { text: 'Our Mission', size: 'h2' } },
    { id: 24, sectionId: 25, themeId: 1, type: 'text', name: 'Mission text', position: 1, hidden: false, settings: { text: 'To connect customers with products that tell a story and make a positive impact on communities worldwide.' } },
    { id: 25, sectionId: 25, themeId: 1, type: 'button', name: 'CTA button', position: 2, hidden: false, settings: { text: 'Meet our artisans', link: '/pages/artisans', style: 'solid' } },

    // Contact form section blocks (section 18)
    { id: 26, sectionId: 18, themeId: 1, type: 'heading', name: 'Heading', position: 0, hidden: false, settings: { text: 'Get in Touch', size: 'h1' } },
    { id: 27, sectionId: 18, themeId: 1, type: 'text', name: 'Description', position: 1, hidden: false, settings: { text: 'We would love to hear from you. Send us a message and we will respond within 24 hours.' } },

    // Blog posts blocks (section 33)
    { id: 28, sectionId: 33, themeId: 1, type: 'heading', name: 'Blog title', position: 0, hidden: false, settings: { text: 'From the Blog', size: 'h1' } },

    // Cart featured collection blocks (section 30)
    { id: 29, sectionId: 30, themeId: 1, type: 'heading', name: 'Heading', position: 0, hidden: false, settings: { text: 'You may also like', size: 'h2' } },

    // Password page blocks (section 36)
    { id: 30, sectionId: 36, themeId: 1, type: 'heading', name: 'Heading', position: 0, hidden: false, settings: { text: 'Coming Soon', size: 'h1' } },
    { id: 31, sectionId: 36, themeId: 1, type: 'text', name: 'Description', position: 1, hidden: false, settings: { text: 'We are working on something exciting. Enter your email to be notified when we launch.' } },
    { id: 32, sectionId: 36, themeId: 1, type: 'email-form', name: 'Email form', position: 2, hidden: false, settings: {} }
];

// ---- Theme Settings (per theme) ----
const THEME_SETTINGS = [
    {
        themeId: 1,
        logo: { url: '', altText: '', width: 120 },
        favicon: { url: '' },
        colors: JSON.parse(JSON.stringify(DEFAULT_COLOR_SCHEMES)),
        typography: {
            headingFont: 'Assistant',
            bodyFont: 'Assistant',
            fontSizeScale: 100
        },
        layout: {
            pageWidth: 1200,
            sectionSpacing: 36,
            gridHorizontalSpacing: 12,
            gridVerticalSpacing: 12
        },
        animations: {
            revealOnScroll: true,
            hoverEffect: HOVER_EFFECTS.VERTICAL_LIFT
        },
        buttons: {
            style: BUTTON_STYLES.ROUNDED,
            borderRadius: 4
        },
        variantPills: {
            style: BUTTON_STYLES.ROUNDED
        },
        inputs: {
            style: INPUT_STYLES.OUTLINED,
            borderRadius: 4
        },
        badges: {
            salePosition: BADGE_POSITIONS.TOP_LEFT,
            saleShape: BADGE_SHAPES.RECTANGLE,
            soldOutPosition: BADGE_POSITIONS.BOTTOM_LEFT,
            soldOutShape: BADGE_SHAPES.RECTANGLE
        },
        socialLinks: JSON.parse(JSON.stringify(DEFAULT_SOCIAL_LINKS)),
        searchBehavior: {
            enableSuggestions: true,
            showVendor: true,
            showPrice: true
        },
        currencyFormat: {
            showCurrencyCode: false
        },
        cart: {
            type: CART_TYPES.DRAWER,
            showVendor: false,
            enableNote: true,
            emptyDrawerCollection: '',
            cartColorSchemeId: 1
        },
        customCss: ''
    },
    {
        themeId: 2,
        logo: { url: '', altText: '', width: 150 },
        favicon: { url: '' },
        colors: JSON.parse(JSON.stringify(DEFAULT_COLOR_SCHEMES)),
        typography: {
            headingFont: 'Playfair Display',
            bodyFont: 'Roboto',
            fontSizeScale: 110
        },
        layout: {
            pageWidth: 1400,
            sectionSpacing: 48,
            gridHorizontalSpacing: 16,
            gridVerticalSpacing: 16
        },
        animations: {
            revealOnScroll: false,
            hoverEffect: HOVER_EFFECTS.THREE_D_LIFT
        },
        buttons: {
            style: BUTTON_STYLES.PILL,
            borderRadius: 24
        },
        variantPills: {
            style: BUTTON_STYLES.PILL
        },
        inputs: {
            style: INPUT_STYLES.FILLED,
            borderRadius: 8
        },
        badges: {
            salePosition: BADGE_POSITIONS.TOP_RIGHT,
            saleShape: BADGE_SHAPES.CIRCLE,
            soldOutPosition: BADGE_POSITIONS.BOTTOM_RIGHT,
            soldOutShape: BADGE_SHAPES.RECTANGLE
        },
        socialLinks: JSON.parse(JSON.stringify(DEFAULT_SOCIAL_LINKS)),
        searchBehavior: {
            enableSuggestions: true,
            showVendor: false,
            showPrice: true
        },
        currencyFormat: {
            showCurrencyCode: true
        },
        cart: {
            type: CART_TYPES.PAGE,
            showVendor: true,
            enableNote: false,
            emptyDrawerCollection: '',
            cartColorSchemeId: 1
        },
        customCss: '.hero-section { padding: 60px 0; }'
    }
];

// ---- Font Library ----
const FONT_LIBRARY = [
    'Abril Fatface', 'Alegreya', 'Alegreya Sans', 'Anonymous Pro', 'Arvo',
    'Assistant', 'Bitter', 'Cormorant', 'DM Sans', 'EB Garamond',
    'Fira Code', 'IBM Plex Sans', 'IBM Plex Serif', 'Inter', 'Josefin Sans',
    'Lato', 'Libre Baskerville', 'Lora', 'Merriweather', 'Montserrat',
    'Mulish', 'Nunito', 'Nunito Sans', 'Open Sans', 'Oswald',
    'Poppins', 'PT Sans', 'PT Serif', 'Playfair Display', 'Quicksand',
    'Raleway', 'Roboto', 'Roboto Condensed', 'Roboto Slab', 'Rubik',
    'Source Sans Pro', 'Source Serif Pro', 'Space Grotesk', 'Space Mono', 'Work Sans'
];

// ---- System Fonts ----
const SYSTEM_FONTS = [
    'Arial', 'Courier New', 'Georgia', 'Helvetica', 'Times New Roman', 'Verdana'
];
