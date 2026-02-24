/* ================================================================
   Shopify Theme Editor — Seed Data
   ================================================================ */

const SEED_DATA_VERSION = 1;

// ── Font Library ──────────────────────────────────────────────────
const FONT_LIBRARY = [
  "Assistant", "Bitter", "Cormorant", "DM Sans", "IBM Plex Sans",
  "Josefin Sans", "Lato", "Montserrat", "Open Sans", "Playfair Display",
  "Roboto", "Source Sans Pro", "Abril Fatface", "Anonymous Pro"
];

// ── Theme Styles (presets) ────────────────────────────────────────
const THEME_STYLES = [
  {
    id: "default", name: "Default",
    settings: {
      typography: { headingFont: "Assistant", headingFontSizeScale: 100, bodyFont: "Assistant", bodyFontSizeScale: 100 },
      colors: { primarySchemeBackground: "#ffffff", primarySchemeText: "#121212" },
      buttons: { borderRadius: 0, shadow: "None" },
      animations: { hoverEffect: "None", revealSectionsOnScroll: false }
    }
  },
  {
    id: "spotlight", name: "Spotlight",
    settings: {
      typography: { headingFont: "Montserrat", headingFontSizeScale: 120, bodyFont: "Open Sans", bodyFontSizeScale: 100 },
      colors: { primarySchemeBackground: "#1a1a2e", primarySchemeText: "#eaeaea" },
      buttons: { borderRadius: 40, shadow: "Small" },
      animations: { hoverEffect: "Vertical lift", revealSectionsOnScroll: true }
    }
  },
  {
    id: "crave", name: "Crave",
    settings: {
      typography: { headingFont: "Playfair Display", headingFontSizeScale: 130, bodyFont: "Lato", bodyFontSizeScale: 105 },
      colors: { primarySchemeBackground: "#fdf6ec", primarySchemeText: "#2d2d2d" },
      buttons: { borderRadius: 8, shadow: "Small" },
      animations: { hoverEffect: "3D lift", revealSectionsOnScroll: true }
    }
  },
  {
    id: "craft", name: "Craft",
    settings: {
      typography: { headingFont: "Cormorant", headingFontSizeScale: 110, bodyFont: "DM Sans", bodyFontSizeScale: 100 },
      colors: { primarySchemeBackground: "#f5f0eb", primarySchemeText: "#3c3c3c" },
      buttons: { borderRadius: 4, shadow: "None" },
      animations: { hoverEffect: "None", revealSectionsOnScroll: false }
    }
  },
  {
    id: "ride", name: "Ride",
    settings: {
      typography: { headingFont: "Josefin Sans", headingFontSizeScale: 115, bodyFont: "Source Sans Pro", bodyFontSizeScale: 100 },
      colors: { primarySchemeBackground: "#0d0d0d", primarySchemeText: "#f0f0f0" },
      buttons: { borderRadius: 20, shadow: "Medium" },
      animations: { hoverEffect: "Vertical lift", revealSectionsOnScroll: true }
    }
  },
  {
    id: "sense", name: "Sense",
    settings: {
      typography: { headingFont: "DM Sans", headingFontSizeScale: 100, bodyFont: "DM Sans", bodyFontSizeScale: 100 },
      colors: { primarySchemeBackground: "#fafafa", primarySchemeText: "#1a1a1a" },
      buttons: { borderRadius: 0, shadow: "None" },
      animations: { hoverEffect: "None", revealSectionsOnScroll: false }
    }
  },
  {
    id: "colorblock", name: "Colorblock",
    settings: {
      typography: { headingFont: "IBM Plex Sans", headingFontSizeScale: 110, bodyFont: "IBM Plex Sans", bodyFontSizeScale: 105 },
      colors: { primarySchemeBackground: "#ffd166", primarySchemeText: "#073b4c" },
      buttons: { borderRadius: 12, shadow: "Small" },
      animations: { hoverEffect: "3D lift", revealSectionsOnScroll: true }
    }
  }
];

// ── Templates ─────────────────────────────────────────────────────
const TEMPLATES = [
  { id: "home", name: "Home page" },
  { id: "products", name: "Products" },
  { id: "collections", name: "Collections" },
  { id: "blog", name: "Blog posts" },
  { id: "cart", name: "Cart" },
  { id: "pages", name: "Pages" },
  { id: "search", name: "Search" },
  { id: "password", name: "Password" },
  { id: "404", name: "404" },
  { id: "gift_card", name: "Gift card" },
  { id: "collection_list", name: "Collection list" },
  { id: "contact", name: "Contact" }
];

// ── Available Section Types ───────────────────────────────────────
const AVAILABLE_SECTION_TYPES = [
  { type: "slideshow",          name: "Slideshow",          category: "Hero" },
  { type: "image_banner",       name: "Image banner",       category: "Hero" },
  { type: "video",              name: "Video",              category: "Media" },
  { type: "rich_text",          name: "Rich text",          category: "Content" },
  { type: "image_with_text",    name: "Image with text",    category: "Content" },
  { type: "multicolumn",        name: "Multicolumn",        category: "Content" },
  { type: "collage",            name: "Collage",            category: "Media" },
  { type: "featured_collection",name: "Featured collection",category: "Collection" },
  { type: "collection_list",    name: "Collection list",    category: "Collection" },
  { type: "featured_product",   name: "Featured product",   category: "Product" },
  { type: "newsletter",         name: "Newsletter",         category: "Engagement" },
  { type: "contact_form",       name: "Contact form",       category: "Engagement" },
  { type: "custom_liquid",      name: "Custom Liquid",      category: "Advanced" },
  { type: "map",                name: "Map",                category: "Advanced" }
];

// ── Block Type Definitions per Section Type ───────────────────────
const BLOCK_TYPES = {
  slideshow:           [{ type: "slide",   name: "Slide" }],
  image_banner:        [{ type: "heading", name: "Heading" }, { type: "button", name: "Button" }, { type: "text", name: "Text" }],
  video:               [{ type: "heading", name: "Heading" }, { type: "text", name: "Text" }],
  rich_text:           [{ type: "heading", name: "Heading" }, { type: "text", name: "Text" }, { type: "button", name: "Button" }],
  image_with_text:     [{ type: "heading", name: "Heading" }, { type: "text", name: "Text" }, { type: "button", name: "Button" }],
  multicolumn:         [{ type: "column",  name: "Column" }],
  collage:             [{ type: "image", name: "Image" }, { type: "product", name: "Product" }, { type: "video", name: "Video" }],
  featured_collection: [{ type: "product_card", name: "Product card" }],
  collection_list:     [{ type: "collection", name: "Collection" }],
  featured_product:    [{ type: "text", name: "Text" }, { type: "variant_picker", name: "Variant picker" }, { type: "buy_buttons", name: "Buy buttons" }],
  newsletter:          [{ type: "heading", name: "Heading" }, { type: "text", name: "Text" }, { type: "email_form", name: "Email form" }],
  contact_form:        [{ type: "heading", name: "Heading" }, { type: "text", name: "Text" }],
  custom_liquid:       [{ type: "liquid", name: "Liquid" }],
  map:                 [{ type: "heading", name: "Heading" }, { type: "text", name: "Text" }],
  header:              [{ type: "mega_menu", name: "Mega menu" }, { type: "nav_link", name: "Navigation link" }],
  announcement_bar:    [{ type: "announcement", name: "Announcement" }],
  footer:              [{ type: "link_list", name: "Link list" }, { type: "text", name: "Text" }, { type: "brand_information", name: "Brand information" }]
};

// ── Products ──────────────────────────────────────────────────────
const PRODUCTS = [
  {
    id: 1, title: "Classic Cotton T-Shirt", vendor: "GreenLeaf Apparel", type: "Apparel",
    price: 29.99, compareAtPrice: 39.99, tags: ["cotton", "casual", "bestseller"],
    variants: [
      { id: 101, title: "Small / White", price: 29.99, sku: "TSHIRT-S-W", inventory: 45 },
      { id: 102, title: "Medium / White", price: 29.99, sku: "TSHIRT-M-W", inventory: 62 },
      { id: 103, title: "Large / Black", price: 29.99, sku: "TSHIRT-L-B", inventory: 38 }
    ],
    image: null, collection_ids: [1, 2]
  },
  {
    id: 2, title: "Organic Linen Dress", vendor: "GreenLeaf Apparel", type: "Apparel",
    price: 89.99, compareAtPrice: null, tags: ["linen", "organic", "summer"],
    variants: [
      { id: 201, title: "Small / Natural", price: 89.99, sku: "DRESS-S-N", inventory: 20 },
      { id: 202, title: "Medium / Natural", price: 89.99, sku: "DRESS-M-N", inventory: 15 }
    ],
    image: null, collection_ids: [1, 3]
  },
  {
    id: 3, title: "Bamboo Cutting Board Set", vendor: "EcoHome Goods", type: "Home & Garden",
    price: 44.99, compareAtPrice: 54.99, tags: ["bamboo", "kitchen", "eco-friendly"],
    variants: [
      { id: 301, title: "3-Piece Set", price: 44.99, sku: "BOARD-3PC", inventory: 80 },
      { id: 302, title: "5-Piece Set", price: 64.99, sku: "BOARD-5PC", inventory: 35 }
    ],
    image: null, collection_ids: [4, 9]
  },
  {
    id: 4, title: "Wireless Bluetooth Earbuds", vendor: "TechWave", type: "Electronics",
    price: 79.99, compareAtPrice: 99.99, tags: ["wireless", "bluetooth", "audio"],
    variants: [
      { id: 401, title: "Black", price: 79.99, sku: "EARBUDS-BLK", inventory: 120 },
      { id: 402, title: "White", price: 79.99, sku: "EARBUDS-WHT", inventory: 95 }
    ],
    image: null, collection_ids: [2, 5]
  },
  {
    id: 5, title: "Handmade Ceramic Mug", vendor: "ArtisanCraft", type: "Home & Garden",
    price: 24.99, compareAtPrice: null, tags: ["ceramic", "handmade", "gift"],
    variants: [
      { id: 501, title: "Ocean Blue", price: 24.99, sku: "MUG-BLUE", inventory: 55 },
      { id: 502, title: "Forest Green", price: 24.99, sku: "MUG-GREEN", inventory: 42 },
      { id: 503, title: "Sunset Orange", price: 24.99, sku: "MUG-ORANGE", inventory: 30 }
    ],
    image: null, collection_ids: [4, 6, 8]
  },
  {
    id: 6, title: "Leather Crossbody Bag", vendor: "UrbanStyle Co", type: "Accessories",
    price: 129.99, compareAtPrice: 159.99, tags: ["leather", "crossbody", "premium"],
    variants: [
      { id: 601, title: "Tan", price: 129.99, sku: "BAG-TAN", inventory: 25 },
      { id: 602, title: "Black", price: 129.99, sku: "BAG-BLK", inventory: 30 }
    ],
    image: null, collection_ids: [2, 8]
  },
  {
    id: 7, title: "Natural Face Serum", vendor: "PureGlow Beauty", type: "Beauty",
    price: 49.99, compareAtPrice: null, tags: ["natural", "skincare", "serum"],
    variants: [
      { id: 701, title: "30ml", price: 49.99, sku: "SERUM-30", inventory: 70 },
      { id: 702, title: "50ml", price: 69.99, sku: "SERUM-50", inventory: 40 }
    ],
    image: null, collection_ids: [3, 9]
  },
  {
    id: 8, title: "Smart Home Speaker", vendor: "TechWave", type: "Electronics",
    price: 149.99, compareAtPrice: 179.99, tags: ["smart-home", "speaker", "voice-assistant"],
    variants: [
      { id: 801, title: "Charcoal", price: 149.99, sku: "SPEAKER-CHAR", inventory: 60 },
      { id: 802, title: "Cream", price: 149.99, sku: "SPEAKER-CRM", inventory: 45 }
    ],
    image: null, collection_ids: [5, 8]
  },
  {
    id: 9, title: "Yoga Mat Premium", vendor: "ZenFit", type: "Accessories",
    price: 59.99, compareAtPrice: 74.99, tags: ["yoga", "fitness", "eco-friendly"],
    variants: [
      { id: 901, title: "Lavender", price: 59.99, sku: "YOGA-LAV", inventory: 90 },
      { id: 902, title: "Midnight Blue", price: 59.99, sku: "YOGA-BLUE", inventory: 75 }
    ],
    image: null, collection_ids: [3, 9]
  },
  {
    id: 10, title: "Stainless Steel Water Bottle", vendor: "EcoHome Goods", type: "Accessories",
    price: 34.99, compareAtPrice: null, tags: ["stainless-steel", "reusable", "eco-friendly"],
    variants: [
      { id: 1001, title: "500ml / Silver", price: 34.99, sku: "BOTTLE-500-S", inventory: 150 },
      { id: 1002, title: "750ml / Silver", price: 39.99, sku: "BOTTLE-750-S", inventory: 100 },
      { id: 1003, title: "500ml / Matte Black", price: 36.99, sku: "BOTTLE-500-B", inventory: 80 }
    ],
    image: null, collection_ids: [2, 9]
  },
  {
    id: 11, title: "Wool Blend Scarf", vendor: "GreenLeaf Apparel", type: "Apparel",
    price: 45.99, compareAtPrice: 59.99, tags: ["wool", "winter", "warm"],
    variants: [
      { id: 1101, title: "Heather Grey", price: 45.99, sku: "SCARF-GREY", inventory: 35 },
      { id: 1102, title: "Burgundy", price: 45.99, sku: "SCARF-BURG", inventory: 28 }
    ],
    image: null, collection_ids: [7, 10]
  },
  {
    id: 12, title: "Portable Phone Charger", vendor: "TechWave", type: "Electronics",
    price: 39.99, compareAtPrice: 49.99, tags: ["portable", "charger", "travel"],
    variants: [
      { id: 1201, title: "10000mAh", price: 39.99, sku: "CHARGER-10K", inventory: 200 },
      { id: 1202, title: "20000mAh", price: 59.99, sku: "CHARGER-20K", inventory: 120 }
    ],
    image: null, collection_ids: [5, 7]
  }
];

// ── Collections ───────────────────────────────────────────────────
const COLLECTIONS = [
  { id: 1,  title: "Summer Collection",   description: "Light and breezy styles for the warm season",         productCount: 3 },
  { id: 2,  title: "Best Sellers",         description: "Our most popular products loved by customers",        productCount: 4 },
  { id: 3,  title: "New Arrivals",         description: "Fresh picks just added to our store",                 productCount: 3 },
  { id: 4,  title: "Home Essentials",      description: "Everything you need to make your house a home",       productCount: 2 },
  { id: 5,  title: "Tech Accessories",     description: "Cutting-edge gadgets and tech gear",                  productCount: 3 },
  { id: 6,  title: "Gift Ideas",           description: "Perfect presents for every occasion",                 productCount: 1 },
  { id: 7,  title: "Sale Items",           description: "Great deals and discounts on selected products",      productCount: 2 },
  { id: 8,  title: "Premium Collection",   description: "Luxury products crafted with the finest materials",   productCount: 3 },
  { id: 9,  title: "Eco-Friendly",         description: "Sustainable products that are good for the planet",   productCount: 4 },
  { id: 10, title: "Winter Warmers",       description: "Cozy products to keep you warm all winter long",      productCount: 1 }
];

// ── Markets ───────────────────────────────────────────────────────
const MARKETS = [
  { id: 1, name: "United States",  currency: "USD", locale: "en-US", primary: true },
  { id: 2, name: "European Union", currency: "EUR", locale: "en-EU", primary: false },
  { id: 3, name: "United Kingdom", currency: "GBP", locale: "en-GB", primary: false },
  { id: 4, name: "Canada",         currency: "CAD", locale: "en-CA", primary: false },
  { id: 5, name: "Japan",          currency: "JPY", locale: "ja-JP", primary: false }
];

// ── Theme Settings ────────────────────────────────────────────────
const THEME_SETTINGS = {
  logo: {
    image: null,
    altText: "",
    desktopLogoWidth: 120,
    faviconImage: null,
    faviconAltText: ""
  },
  colors: {
    schemes: [
      {
        id: "scheme_1", name: "Scheme 1",
        background: "#ffffff", backgroundGradient: "",
        text: "#121212",
        solidButtonBackground: "#121212", solidButtonLabel: "#ffffff",
        outlineButton: "#121212", shadow: "#121212"
      },
      {
        id: "scheme_2", name: "Scheme 2",
        background: "#f3f3f3", backgroundGradient: "",
        text: "#1a1a1a",
        solidButtonBackground: "#1a1a1a", solidButtonLabel: "#ffffff",
        outlineButton: "#1a1a1a", shadow: "#1a1a1a"
      },
      {
        id: "scheme_3", name: "Accent 1",
        background: "#1a1a2e", backgroundGradient: "",
        text: "#eaeaea",
        solidButtonBackground: "#e94560", solidButtonLabel: "#ffffff",
        outlineButton: "#eaeaea", shadow: "#0f0f1a"
      },
      {
        id: "scheme_4", name: "Accent 2",
        background: "#fdf6ec", backgroundGradient: "",
        text: "#2d2d2d",
        solidButtonBackground: "#c8553d", solidButtonLabel: "#ffffff",
        outlineButton: "#2d2d2d", shadow: "#c8b99a"
      },
      {
        id: "scheme_5", name: "Inverse",
        background: "#121212", backgroundGradient: "",
        text: "#ffffff",
        solidButtonBackground: "#ffffff", solidButtonLabel: "#121212",
        outlineButton: "#ffffff", shadow: "#000000"
      }
    ]
  },
  typography: {
    headingFont: "Assistant",
    headingFontSizeScale: 100,
    bodyFont: "Assistant",
    bodyFontSizeScale: 100
  },
  layout: {
    pageWidth: 1600,
    sectionSpacing: 0,
    gridHorizontalSpace: 8,
    gridVerticalSpace: 8
  },
  animations: {
    revealSectionsOnScroll: false,
    hoverEffect: "None"
  },
  buttons: {
    borderRadius: 0,
    shadow: "None",
    border: "None",
    shadowOpacity: 0,
    horizontalOffset: 0,
    verticalOffset: 4,
    blur: 5
  },
  variantPills: {
    shape: "Rectangle",
    border: "Outline",
    shadow: "None"
  },
  inputs: {
    shape: "Rectangle",
    border: "Outline",
    shadow: "None"
  },
  productCards: {
    style: "Standard",
    imageRatio: "Adapt",
    showSecondImageOnHover: false,
    showVendor: false,
    showRating: false,
    colorSchemeId: "scheme_1"
  },
  collectionCards: {
    style: "Standard",
    imageRatio: "Adapt",
    colorSchemeId: "scheme_1"
  },
  blogCards: {
    style: "Standard",
    imageRatio: "Adapt",
    showDate: true,
    showAuthor: false,
    colorSchemeId: "scheme_1"
  },
  contentContainers: {
    borderRadius: 0,
    shadow: "None",
    border: "None"
  },
  media: {
    borderRadius: 0,
    shadow: "None",
    border: "None"
  },
  dropdownsAndPopups: {
    borderRadius: 0,
    shadow: "Small",
    border: "Outline"
  },
  drawers: {
    borderRadius: 0,
    shadow: "None",
    border: "None"
  },
  badges: {
    salePosition: "Bottom left",
    saleShape: "Rectangle",
    saleColor: "#e94560",
    soldOutPosition: "Bottom left",
    soldOutShape: "Rectangle",
    soldOutColor: "#6b7280"
  },
  brandInformation: {
    showBrandImage: false,
    showBrandDescription: false,
    showSocialMediaLinks: true
  },
  socialMedia: {
    facebook: "",
    instagram: "",
    twitter: "",
    tiktok: "",
    snapchat: "",
    pinterest: "",
    tumblr: "",
    youtube: "",
    vimeo: "",
    linkedin: ""
  },
  searchBehavior: {
    enableSuggestions: true,
    showVendor: false,
    showPrice: false
  },
  currencyFormat: {
    showCurrencyCodes: false
  },
  cart: {
    type: "Drawer",
    showVendor: false,
    enableCartNote: false,
    drawerCollection: "",
    drawerColorSchemeId: "scheme_1"
  },
  customCSS: "",
  activeThemeStyle: "default"
};

// ── Sections (Home page seed data) ────────────────────────────────

const SECTIONS = [
  // --- Header group ---
  {
    id: "section_1", type: "announcement_bar", name: "Announcement bar",
    templateId: "home", group: "header", order: 0, visible: true, collapsed: false,
    settings: { colorSchemeId: "scheme_3", autoRotate: true, rotateInterval: 5 },
    blocks: [
      { id: "block_1", type: "announcement", name: "Announcement", sectionId: "section_1", order: 0, visible: true,
        settings: { text: "Free shipping on orders over $50!", link: "/collections/all" } },
      { id: "block_2", type: "announcement", name: "Announcement", sectionId: "section_1", order: 1, visible: true,
        settings: { text: "Summer Sale — Up to 40% off selected items", link: "/collections/sale-items" } }
    ]
  },
  {
    id: "section_2", type: "header", name: "Header",
    templateId: "home", group: "header", order: 1, visible: true, collapsed: false,
    settings: { logoWidth: 120, stickyHeader: true, showSearchIcon: true, menuType: "Dropdown", colorSchemeId: "scheme_1" },
    blocks: [
      { id: "block_3", type: "mega_menu", name: "Mega menu", sectionId: "section_2", order: 0, visible: true,
        settings: { label: "Shop", collectionId: 2 } },
      { id: "block_4", type: "nav_link", name: "Navigation link", sectionId: "section_2", order: 1, visible: true,
        settings: { label: "About", url: "/pages/about" } }
    ]
  },

  // --- Template group ---
  {
    id: "section_3", type: "slideshow", name: "Slideshow",
    templateId: "home", group: "template", order: 0, visible: true, collapsed: false,
    settings: { autoPlay: true, slideInterval: 5, height: "Large", colorSchemeId: "scheme_1" },
    blocks: [
      { id: "block_5", type: "slide", name: "Slide", sectionId: "section_3", order: 0, visible: true,
        settings: { heading: "Welcome to GreenLeaf", subheading: "Sustainable style for modern living", buttonLabel: "Shop Now", buttonLink: "/collections/all", image: null } },
      { id: "block_6", type: "slide", name: "Slide", sectionId: "section_3", order: 1, visible: true,
        settings: { heading: "Summer Collection 2025", subheading: "Light fabrics, bold colors", buttonLabel: "Explore", buttonLink: "/collections/summer-collection", image: null } },
      { id: "block_7", type: "slide", name: "Slide", sectionId: "section_3", order: 2, visible: true,
        settings: { heading: "Eco-Friendly Products", subheading: "Good for you, good for the planet", buttonLabel: "Learn More", buttonLink: "/pages/sustainability", image: null } }
    ]
  },
  {
    id: "section_4", type: "rich_text", name: "Rich text",
    templateId: "home", group: "template", order: 1, visible: true, collapsed: false,
    settings: { colorSchemeId: "scheme_1", fullWidth: false },
    blocks: [
      { id: "block_8", type: "heading", name: "Heading", sectionId: "section_4", order: 0, visible: true,
        settings: { text: "Welcome to Our Store", size: "Large" } },
      { id: "block_9", type: "text", name: "Text", sectionId: "section_4", order: 1, visible: true,
        settings: { text: "Discover our curated collection of sustainable and stylish products designed for modern living." } }
    ]
  },
  {
    id: "section_5", type: "featured_collection", name: "Featured collection",
    templateId: "home", group: "template", order: 2, visible: true, collapsed: false,
    settings: { collectionId: 2, title: "Best Sellers", productsToShow: 8, showViewAll: true, colorSchemeId: "scheme_1", columnsDesktop: 4 },
    blocks: []
  },
  {
    id: "section_6", type: "image_banner", name: "Image banner",
    templateId: "home", group: "template", order: 3, visible: true, collapsed: false,
    settings: { image: null, height: "Medium", desktopContentPosition: "Center", colorSchemeId: "scheme_3" },
    blocks: [
      { id: "block_10", type: "heading", name: "Heading", sectionId: "section_6", order: 0, visible: true,
        settings: { text: "New Season Arrivals", size: "Large" } },
      { id: "block_11", type: "button", name: "Button", sectionId: "section_6", order: 1, visible: true,
        settings: { label: "Shop New Arrivals", link: "/collections/new-arrivals", style: "Primary" } }
    ]
  },
  {
    id: "section_7", type: "image_with_text", name: "Image with text",
    templateId: "home", group: "template", order: 4, visible: true, collapsed: false,
    settings: { image: null, imageWidth: "Medium", desktopImagePlacement: "Left", desktopContentAlignment: "Left", colorSchemeId: "scheme_1" },
    blocks: [
      { id: "block_12", type: "heading", name: "Heading", sectionId: "section_7", order: 0, visible: true,
        settings: { text: "Our Story", size: "Medium" } },
      { id: "block_13", type: "text", name: "Text", sectionId: "section_7", order: 1, visible: true,
        settings: { text: "Founded in 2020, GreenLeaf is committed to bringing you sustainable products that don't compromise on style or quality." } },
      { id: "block_14", type: "button", name: "Button", sectionId: "section_7", order: 2, visible: true,
        settings: { label: "Read More", link: "/pages/about", style: "Secondary" } }
    ]
  },
  {
    id: "section_8", type: "collage", name: "Collage",
    templateId: "home", group: "template", order: 5, visible: true, collapsed: false,
    settings: { desktopLayout: "Left large", mobileLayout: "Collage", colorSchemeId: "scheme_1" },
    blocks: [
      { id: "block_15", type: "image", name: "Image", sectionId: "section_8", order: 0, visible: true,
        settings: { image: null, altText: "Sustainable Living" } },
      { id: "block_16", type: "product", name: "Product", sectionId: "section_8", order: 1, visible: true,
        settings: { productId: 5 } },
      { id: "block_17", type: "video", name: "Video", sectionId: "section_8", order: 2, visible: true,
        settings: { videoUrl: "https://www.youtube.com/watch?v=example", altText: "Brand story" } }
    ]
  },
  {
    id: "section_9", type: "collection_list", name: "Collection list",
    templateId: "home", group: "template", order: 6, visible: true, collapsed: false,
    settings: { title: "Shop by Category", imageRatio: "Square", columnsDesktop: 4, colorSchemeId: "scheme_1" },
    blocks: [
      { id: "block_18", type: "collection", name: "Collection", sectionId: "section_9", order: 0, visible: true,
        settings: { collectionId: 1 } },
      { id: "block_19", type: "collection", name: "Collection", sectionId: "section_9", order: 1, visible: true,
        settings: { collectionId: 4 } },
      { id: "block_20", type: "collection", name: "Collection", sectionId: "section_9", order: 2, visible: true,
        settings: { collectionId: 5 } },
      { id: "block_21", type: "collection", name: "Collection", sectionId: "section_9", order: 3, visible: true,
        settings: { collectionId: 9 } }
    ]
  },
  {
    id: "section_10", type: "featured_product", name: "Featured product",
    templateId: "home", group: "template", order: 7, visible: true, collapsed: false,
    settings: { productId: 7, showDynamicCheckout: true, colorSchemeId: "scheme_4" },
    blocks: [
      { id: "block_22", type: "text", name: "Text", sectionId: "section_10", order: 0, visible: true,
        settings: { text: "Our most popular face serum — 100% natural ingredients." } },
      { id: "block_23", type: "variant_picker", name: "Variant picker", sectionId: "section_10", order: 1, visible: true,
        settings: { style: "Pills" } },
      { id: "block_24", type: "buy_buttons", name: "Buy buttons", sectionId: "section_10", order: 2, visible: true,
        settings: { showDynamicCheckout: true } }
    ]
  },
  {
    id: "section_11", type: "newsletter", name: "Newsletter",
    templateId: "home", group: "template", order: 8, visible: true, collapsed: false,
    settings: { colorSchemeId: "scheme_5", fullWidth: true },
    blocks: [
      { id: "block_25", type: "heading", name: "Heading", sectionId: "section_11", order: 0, visible: true,
        settings: { text: "Subscribe to Our Newsletter", size: "Medium" } },
      { id: "block_26", type: "text", name: "Text", sectionId: "section_11", order: 1, visible: true,
        settings: { text: "Stay updated with new products, exclusive offers, and sustainability tips." } },
      { id: "block_27", type: "email_form", name: "Email form", sectionId: "section_11", order: 2, visible: true,
        settings: { buttonLabel: "Subscribe", placeholder: "Enter your email" } }
    ]
  },
  {
    id: "section_12", type: "video", name: "Video",
    templateId: "home", group: "template", order: 9, visible: true, collapsed: false,
    settings: { videoUrl: "https://www.youtube.com/watch?v=example", coverImage: null, autoplay: false, colorSchemeId: "scheme_1" },
    blocks: []
  },
  {
    id: "section_13", type: "multicolumn", name: "Multicolumn",
    templateId: "home", group: "template", order: 10, visible: true, collapsed: false,
    settings: { title: "Why Choose GreenLeaf?", imageRatio: "Circle", columnsDesktop: 3, colorSchemeId: "scheme_2" },
    blocks: [
      { id: "block_28", type: "column", name: "Column", sectionId: "section_13", order: 0, visible: true,
        settings: { title: "Sustainable", text: "All our products are ethically sourced and eco-friendly.", image: null, linkLabel: "", linkUrl: "" } },
      { id: "block_29", type: "column", name: "Column", sectionId: "section_13", order: 1, visible: true,
        settings: { title: "Quality First", text: "We never compromise on quality — every product is tested and approved.", image: null, linkLabel: "", linkUrl: "" } },
      { id: "block_30", type: "column", name: "Column", sectionId: "section_13", order: 2, visible: true,
        settings: { title: "Fast Shipping", text: "Free shipping on orders over $50, delivered to your door.", image: null, linkLabel: "", linkUrl: "" } }
    ]
  },

  // --- Footer group ---
  {
    id: "section_14", type: "footer", name: "Footer",
    templateId: "home", group: "footer", order: 0, visible: true, collapsed: false,
    settings: { colorSchemeId: "scheme_5", showPaymentIcons: true, showCountrySelector: false, showLanguageSelector: false },
    blocks: [
      { id: "block_31", type: "link_list", name: "Link list", sectionId: "section_14", order: 0, visible: true,
        settings: { heading: "Quick Links", links: [
          { label: "Search", url: "/search" },
          { label: "About Us", url: "/pages/about" },
          { label: "Contact", url: "/pages/contact" },
          { label: "FAQ", url: "/pages/faq" }
        ] } },
      { id: "block_32", type: "link_list", name: "Link list", sectionId: "section_14", order: 1, visible: true,
        settings: { heading: "Policies", links: [
          { label: "Shipping Policy", url: "/policies/shipping-policy" },
          { label: "Refund Policy", url: "/policies/refund-policy" },
          { label: "Privacy Policy", url: "/policies/privacy-policy" },
          { label: "Terms of Service", url: "/policies/terms-of-service" }
        ] } },
      { id: "block_33", type: "text", name: "Text", sectionId: "section_14", order: 2, visible: true,
        settings: { heading: "Our Mission", text: "GreenLeaf is dedicated to making sustainable living accessible and stylish for everyone." } }
    ]
  }
];

// ── ID Counters ───────────────────────────────────────────────────
var _nextSectionId = 15;
var _nextBlockId = 34;
var _nextColorSchemeId = 6;
