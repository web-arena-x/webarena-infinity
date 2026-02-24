# Search behavior in your online store

Source: https://help.shopify.com/en/manual/online-store/storefront-search/search-behavior

---

# Search behavior in your online store

The online store search uses different factors in and several built-in behaviors for handling search terms to return accurate and relevant results from your products, pages, and blog posts.

## On this page

* [Considerations for online store search](search-behavior.md#considerations-for-online-store-search)
* [Singular and plural search terms](search-behavior.md#singular-and-plural)
* [Typo tolerance](search-behavior.md#typo-tolerance)
* [Search limitations](search-behavior.md#search-limitations)
* [Search syntax](search-behavior.md#search-syntax)
* [Trigram](search-behavior.md#trigram)
* [Search types and features](search-behavior.md#search-types-and-features)
* [Advanced search behaviors](search-behavior.md#advanced-search-behaviors)

## Considerations for online store search

Review the following considerations and requirements for search behavior on your online store.

### Apps

Apps that modify your theme or that have search capabilities might impact the built-in online store search:

* If you're using a third-party search app to generate search results, then the search behaviors and capabilities of Shopify's built-in search might not apply to search results on your online store. To learn more about how your third-party search app works, contact the app's developer.
* Third-party apps that modify your theme's search template might impact search results on your online store.
* You can manage and improve your search results by managing the visibility of products, pages and blog posts, and by customizing your online store search results with the [Shopify Search & Discovery](https://apps.shopify.com/search-and-discovery) app. Learn more about [managing searchability](managing-searchability.md) and [using the Search & Discovery](../storefront-search.md#search-and-discovery) app.

### Search syntax

The following search behaviors don't apply to searches that use [search syntax](search-behavior.md#search-syntax):

* Typo tolerance
* Predictive search
* [Semantic understanding](search-and-discovery-modify-search.md#semantics)

### Supported languages

Your store's [primary locale](https://shopify.dev/docs/liquid/reference/objects/shop-locale#shop_locale-primary) affects which search behaviors you get.

List of supported search languages and whether each language supports typo tolerance, search stemming, and trigram.

| Language | Typo tolerance | Search stemming | Trigram |
| --- | --- | --- | --- |
| English | ✔ | ✔ |  |
| French | ✔ |  |  |
| Spanish | ✔ |  |  |
| Portuguese (Brazil) | ✔ |  |  |
| German | ✔ |  |  |
| Dutch | ✔ |  |  |
| Italian | ✔ |  |  |
| Japanese |  | ✔ | ✔ Can support [Katakana, hiragana, and kanji.](search-behavior.md#trigram) |
| Danish | ✔ |  |  |
| Swedish | ✔ |  |  |
| Portuguese (Portugal) | ✔ |  |  |
| Finnish | ✔ |  |  |
| Norwegian (Bokmål) | ✔ |  |  |
| Turkish | ✔ |  |  |
| Romanian | ✔ |  |  |
| Hungarian | ✔ |  |  |
| Russian | ✔ |  |  |
| Polish | ✔ |  |  |
| Czech | ✔ |  |  |
| Greek | ✔ |  |  |
| Icelandic | ✔ |  |  |
| Lithuanian | ✔ |  |  |
| Slovenian | ✔ |  |  |
| Slovak | ✔ |  |  |
| Bulgarian | ✔ |  |  |
| Vietnamese | ✔ |  |  |
| Croatian | ✔ |  |  |
| Indonesian | ✔ |  |  |
| Latvian | ✔ |  |  |
| Estonian | ✔ |  |  |
| Serbian | ✔ |  |  |
| Ukrainian | ✔ |  |  |
| Catalan | ✔ |  |  |
| Norwegian (Nynorsk) | ✔ |  |  |
| Faroese | ✔ |  |  |
| Portuguese | ✔ |  |  |
| Albanian | ✔ |  |  |
| Bosnian | ✔ |  |  |
| Afrikaans | ✔ |  |  |
| Macedonian | ✔ |  |  |
| Armenian | ✔ |  |  |
| Serbo-Croatian | ✔ |  |  |
| Latin | ✔ |  |  |
| Welsh | ✔ |  |  |
| Gaelic | ✔ |  |  |
| Moldovan | ✔ |  |  |

### Unlisted product status

You can prevent products from being found in your online store search by using [**Unlisted** product status](https://help.shopify.com/en/manual/products/details/product-details-page#unlisted-products).

## Singular and plural search terms

The online store search tries to match terms in both their singular and plural forms.

Searching for `puppies` matches results containing "puppy" or "puppies".

Treating singular and plural terms as equivalent is an example of stemming, where a word is mapped to its common lemma (stem). Shopify's stemming also takes into account the common stem of different words.

Searching for `body:leggings` matches results containing "leg" or "leggings".

If you want to search for a word based on partial pattern matching, then use [prefix search](search-behavior.md#prefix-search).

## Typo tolerance

The online store search includes typo tolerance, which finds correct matches for search terms that contain typos.

Search results include matches that differ from the search term by one letter or that have two letters in a different order. The first four letters of a search term need to be entered correctly for typo tolerance to take effect.

For example, search for `chocollate`, will return results that have `chocolate` or `chocolates` in the title or description.

Typo tolerance isn't applied on all fields when creating search results. For example, `chocollate` wouldn't match on any product tags of blog post tags of `chocolate`. The following resource fields support typo tolerance:

List of resource fields on products, pages, and blog posts that support typo tolerance.

| Resource type | Supported fields |
| --- | --- |
| Products | * title * product\_type * variants.title * vendor |
| Pages | * author * title |
| Blog posts | * author * title |

## Search limitations

### Stopwords in search

#### What are stopwords

Common words in any language are classified as "stopwords" and are not indexed for search. This includes words like "and", "or", "the", "a", "an", and "for" in English, as well as equivalent words in other supported languages.

Stopwords are excluded from search indexing because they are too common to provide meaningful search signals and would make the search index much larger and slower. If you search for stopwords alone, then you won't get any results.

#### Impact on search behavior

This behavior applies to both admin search and storefront search across all supported languages.

## Search syntax

Search syntax determines how search terms are treated when Shopify searches for results.

### Using AND, OR and NOT operators

**AND**

Searching for results with the `AND` operator between search terms returns results when all search
terms are in the result.

By default, all search terms are treated as having `AND` between them. Searching for `artichoke hearts` or
`artichoke AND hearts` both yield results containing both "artichoke" and "hearts". Joining operators aren't necessary.

**OR**

Searching for results with the `OR` operator between search terms returns results when any search
term is a result.

Searching for `artichoke OR hearts` yields results containing at least one of "artichoke" or "hearts".

**NOT**

Searching for results without a term can be done by prefixing the term with a minus sign (`-`).

Searching for `artichoke -heart` matches terms with "artichoke", but not "heart".

### Prefix search

Prefix search will return results where the search term matches the beginning of other terms in results. Prefix search occurs automatically on all searches.

Searching for `artich` matches terms that begin with "artich", like "artichoke". This also works on the last term of a search. Searching for `artichoke hea` matches terms that begin with "artichoke hea".

### Phrase search

Placing a search term between double quotes (`""`) searches for that exact word or phrase in one of the searchable fields.

Searching `"artichoke hearts"` matches a product with the title "Can of artichoke hearts", but not a product with the title "Canned hearts of artichoke".

### Searching specific fields

Add a field name with a colon to your search term to narrow your search for that term to the specified field.

For example, searching for `title:artichoke` searches for titles that include the term "artichoke".

Searching for a misspelt word won't work when searching specific fields, since search looks for an exact match. For example, searching for `title:artichoqe` doesn't yield any results.

Depending on the resource you're searching for (product, page, blog post), results can be based on different searchable properties.

List of searchable properties on products, pages, and blog posts.

| Resource | Searchable properties |
| --- | --- |
| Products | * body * product\_type * tag * title * variants.barcode * variants.sku * variants.title * vendor |
| Pages | * author * body * title |
| Blog posts | * author * body * tag * title |

## Trigram

Trigram search matches any consecutive sequence of at least three characters in katakana, hiragana, and kanji. You can also search kanji in pairs. For example, you can search for "アップルグリーンラップドレス" by entering any of the following terms:

* `ップル`
* `アップル`
* `ップルグリーンラ`

## Search types and features

Your online store uses different types of search functionality depending on how customers interact with the search interface:

* **Regular search**: Results that appear on the search results page after customers enter a search term and press Enter.
* **Predictive search**: Autocomplete functionality that suggests results as customers type in the search box, before they press Enter. Learn more about [predictive search](predictive-search.md).

### Search ranking and relevance

Search results are ordered by relevance, which is determined by several factors:

* **Keyword frequency**: How many times the search term appears in the product, page, or article.
* **Field importance**: Terms found in titles are ranked higher than terms found in descriptions or other fields.
* **Field length**: Shorter fields with matching terms are ranked higher than longer fields.
* **Popularity signals**: Recent sales and customer interactions may influence ranking to optimize for conversions.

### Query relaxation

When a search returns no results, the search system automatically relaxes the search criteria to find potential matches:

* **Typo tolerance**: For words with 3-5 characters, one typo is allowed. For words with 6 or more characters, up to two typos are allowed.
* **Field matching**: Relaxed search only applies to `product_type` and `title` fields for an exact match on other fields.

For example, if "care bears" returns no direct results, the system might match products containing "card years" because each word differs by only one character.

## Advanced search behaviors

### Partial word matching

Search supports partial word matching (prefix search) on the last term of a search query. For example:

* Searching for `winter sno` matches `winter snowboard` and `winter snowshoes`
* The previous terms must match exactly for prefix search to work

### Out-of-stock product handling

By default, products that are completely out of stock (all variants unavailable) appear at the end of search results. This behavior can be customized in your theme settings to:

* **Show**: Display out-of-stock products in normal ranking order
* **Last**: Show out-of-stock products at the end of results (default)
* **Hide**: Completely hide out-of-stock products from results

### Search result limitations

**Maximum expansions for prefix search**: When using prefix search across all stores, results are limited to 50 matches maximum. This limitation may cause some relevant products to not appear in results for very common prefixes.

**Pages in unexpected results**: Older pages may show in search results that don't seem relevant because of hidden author information from legacy page creation processes.