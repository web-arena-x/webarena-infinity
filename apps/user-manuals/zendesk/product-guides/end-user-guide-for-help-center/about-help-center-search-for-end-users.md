# About help center search for end users

Source: https://support.zendesk.com/hc/en-us/articles/4408894061338-About-help-center-search-for-end-users

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support with** | Guide Professional or Enterprise |

Your help center performs a full-text search of your knowledge base articles, community
posts, and if federated search is enabled and configured, [external content](https://support.zendesk.com/hc/en-us/articles/4593607942298) such as blogs or websites.

When a user enters a search query in the help center, the search algorithms get to work,
looking for indicators of the most relevant results and ranking them. The relevant snippet
from the content of your knowledge base article, community post, or external content is
created and the search results and relevant search filters are displayed on the search results
page.

[Generative search](https://support.zendesk.com/hc/en-us/articles/8888178335898) is available with all Zendesk Suite and Knowledge
plans, and provides AI-generated answers to users' search queries in your help center based on
your content. When generative search is activated, users can view generated answers without
clicking through search results or scanning related articles. However, users can still easily
click into the articles for more information.

Help center search is just one way to search for content in your help center. For information
about other search methods, see [Understanding help center search methods](https://support.zendesk.com/hc/en-us/articles/4408834595738-Understanding-help-center-search-methods-instant-search-native-search-article-suggestions-KC-app).

Note: If your help center is [configured to support multiple languages](https://support.zendesk.com/hc/en-us/articles/4408827609882), your [help center locale](https://support.zendesk.com/hc/en-us/articles/4408834328090) must match the article translation. For example,
if your help center locale is set to en-gb (English - United Kingdom), but the article
translation itself is written in Japanese, search will not work as intended and described in
this article.

This article contains the following sections:

- [Which content is included and excluded in search results](#topic_zmf_y4s_3fc)
- [Understanding the relevance score in search results](#topic_sxm_z4s_3fc)
- [Understanding boosts in search results](#topic_asy_1ps_3fc)
- [Other relevance features](#topic_zjy_bps_3fc)
- [Improving the search experience for end users](#topic_syt_cps_3fc)

## Which content is included and excluded in search results

When you search the help center, you're searching all knowledge base articles (first 10,000
characters of each article) in your native help center. Your search can also include the
following:

- Articles and community posts from other help centers in your account, if multiple help
  centers are enabled and search has been configured to include results from those help
  centers. See [Enabling search across multiple help centers](../using-help-center-search/enabling-search-across-multiple-help-centers.md).
- Content from external sources, if federated search is enabled and search has been
  configured to include results from external content. See [About help center federated search](https://support.zendesk.com/hc/en-us/articles/4408830243482).

### Articles and community posts

When an article, post, or external content is returned, the search engine attempts to
find a snippet from the document body that matches the search. If there is no match in the
document body or comments, an extract from the start of the document body is returned. If
there is a match, the search engine divides the article or post into sentences and ranks
each sentence based on the number of matches. The score is then normalized by the fragment
length to ensure that fragments are not too small.

The default snippet size for a search result is 120 characters, although results can vary
slightly because the snippet engine will always try to return a fragment that includes a
complete sentence.

These items might also be included in the search:

- **Restricted content -** Only users with permission to access restricted content
  will see in search results.
- **New content -** When you add or update content it usually takes only a few
  minutes before the content is indexed and can be searched.
- **Comments** - Article and post comments are included in the help center search
  results. Comments will show up in the search results as long as the search result
  snippet is matched in the comment. If there are multiple comment matches within one
  community post, the algorithm will pick the most relevant comment snippet.
- **Hyperlinks -** URLs within the document body and linked text are included in help
  center search results.

These items are not included in the search:

- **Attachments -** Content within article attachments isn't included in help center
  search.
- **My Activities -** Search in My Activities is limited to tickets and,
  specifically, tickets you have access to. It does not include articles.

### External Content

If external content is available, the title of the external content is displayed along
with a link to open the content in a new browser tab and a snippet from the document body
that matches the search. If there is no match in the document body, an extract from the
start of the document body is returned.

External content source types and filters are defined during search crawler setup or
during federated search API configuration. See [About help center federated search](https://support.zendesk.com/hc/en-us/articles/4408830243482).

## Understanding the relevance score in search results

The ranked search results are based on [relevance scores](https://www.elastic.co/guide/en/elasticsearch/guide/master/relevance-intro.html) and are displayed to users in
descending order of their scores.

Relevance scores are indicated by a weighted average per field score. A field is a part of
a record, representing an item of data. The following are some examples of relevance
scoring:

- Matches in an article or post title field score higher than matches in other
  fields.
- Matches in article labels score higher than matches in the body field.

The following table lists the current field weights:

| Field | Weight for KB articles | Weight for community posts | Weight for external content |
| --- | --- | --- | --- |
| Title | 3 | 3 | 3 |
| Details (Body of a community post) | N/A | 1 | N/A |
| Body | 1 | N/A | 1 |
| Labels | 2.8 | N/A | N/A |
| Comment | 1 | 1 | N/A |
| Section title | 1.5 | N/A | N/A |

Relevance scores are also impacted by a text analysis process that considers the following
factors:

- **Exact match** - Results that exactly match a word in the search string. This scores
  higher than a stemmed match.
- **Stemmed match** - Results where a word matches after [stemming](https://www.elastic.co/guide/en/elasticsearch/guide/master/stemming.html). For example, the plural form of a word
  generally matches the singular form.
- **Term frequency** - Number of matches returned in a single field. Higher term
  frequency increases the score.
- **Field length** - Matches in shorter fields score higher than results in longer
  fields. For example, if you have a single word search that matches a one-word title, that
  will score higher than a hit in a long article title with many words.
- **Proximity boost** - The score is boosted when all the search terms are close
  together in the same field. For example if all the search terms are included in an
  article title, this puts them in close proximity and gives the result higher
  relevance.
- **Phrase boost** - In multiple term queries, exact word order is preferred. For
  example, when searching for “car park”, results containing “car park” are ranked higher
  than results containing “park car.”
- **Query length** - For one- and two-word queries, the algorithm returns only
  documents that match all the search words. For longer queries, 40% of the query terms must
  be present in a document for it to become a search result.
- **Overall quantity and quality** of relevant results.
- **Semantic search** - Knowledge uses semantic search as a way to improve the ranking
  and generate the most accurate search results possible based on the intent and context of
  user search queries. See [About semantic search and how it works](https://support.zendesk.com/hc/en-us/articles/5633225532826).

Note: Suggested articles are what users see when they type the subject
of a request in the Submit a request form in their help center. Suggested posts are what
users see when they create the title of a community post. The search relevance used for
suggested articles and posts is the same as the rest of the help center.

## Understanding boosts in search results

In addition to text analysis, we give extra weight to certain features of articles and
posts. These include:

- **Article votes** - End users can rate articles as “helpful” or “unhelpful” so that
  over time an article may develop a score such as “10 of 50 users found this article
  helpful.” Articles with a higher percentage of positive votes receive a boost so that they
  show up a higher in results than they otherwise would. The more overall votes an article
  has weighs in too; for example, an article with a rating of 10 out of 50 gets more weight
  than one with 10 out of 100.
- **Community post votes** (requires Knowledge Professional or Enterprise) - End users
  can rate community posts as “helpful” or “unhelpful,” just as they can for articles. The
  percentage of positive votes functions as a boost and makes a certain post rank higher
  than it otherwise would.
- **Labels** (requires Knowledge Professional or Enterprise) - Labels are elements you
  can use to influence the relevance score of your articles in search results. Consider
  using labels carefully to balance your Knowledge base search results.

## Other relevance features

### Fuzzy search

Fuzzy search is a process where an article or post is deemed to be relevant to a search
query, even when there is not an exact match to the search terms in any of its fields.
Fuzzy search is used to protect users from spelling mistakes.

Unlike stemming (which removes suffixes and prefixes to get to the root of a search term)
fuzzy search uses [edit distance](https://en.wikipedia.org/wiki/Edit_distance) to identify search results that contain terms
close to the query terms. For example, if you search for “user segmemt” the search engine
will also return results containing “user segment”.

The current rule for finding approximate matches is:

- Terms containing a maximum of two characters must match exactly
- Terms containing three to five characters are allowed one typo
- Terms longer than five characters are allowed two typos

Fuzzy search is not available in Japanese, Korean, and Chinese help center languages.

### Optimized language support

For content written in certain languages, we apply specific optimizations.

Stemming is language specific. In English, the search engine knows that if you search for
the term “films” you also want results that contain the singular form “film.” Similar
rules apply to all languages.

Stop words are another language-specific factor. Stop words are the most common words in
a language that are usually excluded from the search query to avoid returning too many
results. For example, in English, “the” is a stop word.

Help center search is aware of the stemming rules and the stop words for a number of
languages that together make up up to 99% of all searches performed by end users.

Searches are optimized in the following languages: Arabic, Bulgarian, Burmese, Chinese,
Danish, Dutch, English, French, German, Greek, Hindi, Indonesian, Italian, Japanese,
Khmer, Korean, Norwegian, Persian, Portuguese, Romanian, Russian, Spanish, Swedish, and
Thai.

All other languages benefit from basic search support.

## Improving the search experience for end users

There are a number of ways that you can improve a user's search experience. Consider
changing the color of search results highlighting in your custom theme, or use CSS to [change the appearance of your search results keyword
highlighting](https://support.zendesk.com/hc/en-us/articles/4408842914714-Help-Center-CSS-cookbook#topic_ocg_xdp_h5).

You can also use the search analytics dashboard to review search terms from the last 30
days. For each search term, you can see the number of searches for that term, number and
type of search results returned (if any), click-through, and the next action taken.

Note: This requires Knowledge Professional or Enterprise.

Search analytics gives you insight into what your customers are looking for and where they
are failing to find answers. To make end users more successful, you can analyze search data,
then take actions to improve search results and your knowledge base content. See [Analyzing help center search results](https://support.zendesk.com/hc/en-us/articles/4408818465562).

**To access the Zendesk Knowledge dashboard**

1. In the Zendesk product tray, click **Analytics**.
2. From the list of dashboards, select the **Zendesk Knowledge**
   dashboard.
3. Click the **Search** tab.

### Providing tips for your end users to find content more easily

There are a number of operands you can recommend to help end users locate content in
search.

Note: When you search, any comments associated with an
article and post are also searched. Therefore, the search term might not be in an
article or post itself, but in a linked comment. Exact matches with doubles quotes (")
are not supported on comments.

- **Find multiple words:** Use double quotes (") around each word to find content
  that contains all those words.

  For example, `"article" "title" "section" "author"` retrieves content
  that contains all four words, in any order. Make sure you put spaces between the
  search words, otherwise the search handles the text as one string.

  You'll get results if there is a [stemmed](https://www.elastic.co/guide/en/elasticsearch/guide/master/stemming.html) version of a word (e.g.
  *articles*). You won't get results where content contains only the words
  *title* and *section*, for example.

  If you use single quotes (') around a word, the single quotes are ignored. If you
  search for `'article' 'title' 'section' 'author'`, you'll see results
  for all content that contains any of the words *title* or *article* or
  *section* or *author* (exactly as if you had searched without the single
  quotes).
- **Find a phrase:** Use double quotes (") around a phrase to find content that
  contains all the words in that phrase.

  For example, `"article title"` retrieves all content that contains the
  words *article* and *title*, in that order. You'll also get results if there
  is a [stemmed](https://www.elastic.co/guide/en/elasticsearch/guide/master/stemming.html) version of the word (e.g.
  *articles*). You won't get results where content contains only the word
  *title*, for example.

  If you use single quotes (') around a phrase, the single quotes are ignored.
- **Exclude results containing certain words**: Use the minus operator (-) in front
  of the search term to find content that does not include that word or phrase.

  For example, *reporting bugs -support* returns content containing the words
  *reporting* and *bugs*, but excludes those that contain the word
  *support* from the result set.

  Note: Do not repeat the same word after a minus operator (-). For
  example, the search `"cannot send -cannot set"` repeats the word
  “cannot” and therefore won’t return any results. Instead, search for `"cannot
  send -set"` so that the search returns results excluding the articles that
  contain the phrase “cannot set”.
- **Combine operands for advanced search**: you can combine the operands above to
  find a very specific set of results.

  For example, *"reporting bugs" -support* returns hits for content that contains
  both the words *reporting* and *bugs*, but does not contain the word
  *support.*