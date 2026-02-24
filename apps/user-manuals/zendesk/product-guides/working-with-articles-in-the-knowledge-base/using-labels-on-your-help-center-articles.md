# Using labels on your help center articles

Source: https://support.zendesk.com/hc/en-us/articles/4408835056154-Using-labels-on-your-help-center-articles

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Growth, Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support with** | Guide Professional or Enterprise |

Labels are a single word or a multiple-word phrase you can add to a specific article in your help center. You can use labels to influence article [search relevance](https://support.zendesk.com/hc/en-us/articles/4408894061338#h_88432433111547663753531) or to [create a list of related articles](https://support.zendesk.com/hc/en-us/articles/4408837776666) based on labels.

You can add and remove labels on individual articles or you can change labels on multiple articles at once.

This article covers the following topics:

- [Adding and removing labels on individual articles](#topic_uqx_5v4_n1b)
- [Changing article labels in bulk on multiple articles](#topic_jq3_lns_y2b)
- [Understanding why to use labels](#topic_ytf_5v4_n1b)
- [Best practices for adding labels](#topic_i4p_vv4_n1b)
- [Using the help center API to filter articles by labels](#topic_slr_sv4_n1b)

## Adding and removing labels on individual articles

Labels are a single word or a multiple-word phrase you can add to an article in your help center. You can add articles labels for multiple purposes, including influencing search and bot results or creating article lists (see [Understanding why to use labels](#topic_ytf_5v4_n1b)).

You can add and remove labels on individual articles or you can [change labels in bulk for multiple articles](#topic_jq3_lns_y2b)
at once.

**To add or remove labels to an article**

1. In [help center](https://support.zendesk.com/hc/en-us/articles/9041943683354#topic_dzz_4wn_s2c) or [Knowledge admin](https://support.zendesk.com/hc/en-us/articles/9041943683354#topic_b5q_nwn_s2c), navigate to the article where you want to change labels, then click **Edit article** in the top menu bar.
2. If the **Article settings** panel is not displayed in the sidebar, click the **Article settings** icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/guide-art-settings-icon.png)) to expand the panel.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/guide-art-settings-panel.png)
3. Click the **Placement** card to expand the Placement panel, then scroll down to the Labels section.
4. In the **Labels** field, start typing the label you want to add, then select **Add as new label** or select the matching label, if it exists.

   Article labels are not case-sensitive. However, be aware that if you filter on labels when searching for articles (for example in the Manage articles view), the filter is case sensitive. See [Best practices for adding labels](#topic_i4p_vv4_n1b), below.

   You can add a maximum of 50 labels. You might have to scroll down to see labels. See [Best practices for adding labels](#topic_i4p_vv4_n1b).

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/hc_article_labels.png)

   Labels live on the default language article and not on translations of the article. If you have translations, you can add labels in multiple languages to the default article.
5. Add multiple labels as needed.
6. If you need to remove a label, click the x beside the label name.
7. Click **Save**.

You must manage labels on each individual article or [using the API](https://developer.zendesk.com/rest_api/docs/help_center/article_labels). There is no global management for article labels.

## Changing article labels in bulk on multiple articles

You can add or remove labels on multiple articles at once.

1. In [Knowledge admin](https://support.zendesk.com/hc/en-us/articles/9041943683354#topic_b5q_nwn_s2c), click **Manage articles** (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/guide_icon_manage_articles.png)) in the sidebar.
2. Find the articles you want to update by browsing, searching, or [using a new or existing articles list.](https://support.zendesk.com/hc/en-us/articles/4408837776666)
3. Select one or more articles to change labels.

   You can select a maximum of 30 articles at a time.

   ![Articles bulk action change labels](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/article_bulk_actions.png)
4. Click the **Article settings** menu at the bottom, then select **Change labels**.
5. Do any of the following:
   - **Add a new label:** Enter the label, then click **Add as a new label**.

     ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/bulk_labels_add_new.png)
   - **Add an existing label:** Search or browse to find the labels you want to add, then select any empty checkbox or any checkbox with a minus.

     The minus sign (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/bulk_labels_minus.png)) indicates that the label appears on some but not all of the selected articles. When you select it, it changes to a checkmark (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/bulk_labels_checkmark.png)), indicating that it will be added to any selected article that doesn't already have that label.

     You can select multiple labels to add to the selected articles.

     ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/bulk_labels_select_existing.png)
   - **Remove an existing label:** Search or browse to find the labels you want to remove, then deselect one or more labels.

     The checkmark (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/bulk_labels_checkmark.png)) indicates that the label appears on all of the selected articles. The minus sign (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/bulk_labels_minus.png)) indicates that the label appears on some but not all of the selected articles. When you select a checkbox with a minus sign, it changes to a checkmark.; click it again to deselect the checkbox.

     You can select multiple labels to add to the selected articles.

     ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/bulk_labels_remove.png)
6. Click **Change**.

   The label changes are applied to the selected articles.

## Understanding why to use labels

Labels have the following uses and impacts:

- **Influence article search relevance**

 Adding labels can make your articles more search friendly. They are not designed to be used for fine-grained control of ranking.
 For example, if I have two articles about making waffles, one with the word "temperature" in the body of the article, one with the label "temperature", the labeled article will be ranked higher if a user searches for the word "temperature".

 Labels are indexed for search with a bit less weight than the article title, but multiple labels with similar words can outweigh the title and body of the article. Use labels carefully as you can significantly impact the relevance of your search results and usefulness. If you are considering using labels to impact search relevance, consider that efforts to do so could end up with inferior ranking performance for your users. The best way to have your article perform well in search is to create a short and focused article, where the title and body include keywords and clearly connect to each other.

 To learn more about search, see [How end-user search works in your help center](https://support.zendesk.com/hc/en-us/articles/4408894061338-About-Help-Center-end-user-search).
- **Influence article recommendations**

 Labels can influence the results for recommended articles. You can define a whitelist of articles that are allowed to be used when looking for relevant matching results.
 You are able to add up to ten labels that serve as an OR filter, allowing you to expand the whitelist to any articles containing any of the defined labels. Keep in mind that if you have an advanced AI agent, that functionality might override the influence of labels on help center articles.

 To learn more, see [Best practices for using labels to optimize your article recommendations](https://support.zendesk.com/hc/en-us/articles/4408883075098).
- **Create article lists** 

 Article lists enable you to get an overview of all your published and unpublished knowledge base content, and then refine that view by using search and applying filters to build article lists. For example, you can find articles that have a specific article label, such as out-of-date.

 To learn more about article lists, see [Using article lists for different views of your knowledge base content](https://support.zendesk.com/hc/en-us/articles/4408837776666).

## Best practices for adding labels

Labels can help boost the search relevance of an article. However, you should use labels carefully and sparingly. It's more important to make sure the article title and body contain the relevant keywords.

- **Use single word labels where possible, instead of multi-word phrases**

 It is possible to add labels as single words or as multiple words or phrases. In general, it's more efficient to use single word labels. If you add a multi-word label, the search engine breaks it into individual words to perform the search. For example, if you have a label of "late delivery," it gets broken down into "late" and "delivery" for search.

 Avoid using long phrases as labels to boost an article's ranking with respect to a query. For example, "Can I return something I ordered online to my local store." Instead, you should modify the article's title or content to make it literally relevant to the query.
- **Do not include variations of the same word, including different tenses or plural forms**

 You do not need to include multiple labels for variations of a word. For example you do not need a label for "return" and "returns" or "update" and "updated." [Fuzzy search](https://support.zendesk.com/hc/en-us/articles/4408894061338#01H8CT7K00NCBBYKZX0EVR1SKX) allows different forms of the same word to match. In particular, the singular and plural forms of a word will generally match.
- **Use a limited number of labels, instead of overloading an article with labels**

 Use labels sparingly. Adding lots of labels might actually diminish any matches on labels. This is because it is assumed that matches with a fewer number of labels beats matches with more labels. And too many labels might outweigh the relevance of the title and body.

 For example, if article 1 has the labels “car,” “automobile,” and “transport” and article 2 has only the label “car,” all other things equal, if the end-user searches for “car,” the article that has only the label “car” will rank higher. That is because, as a general principle, an article that is about one specific thing is more relevant than an article about many things, when a user is looking for that one specific thing.

 Your best bet is to look at the top ranked search queries and make sure that they exist in either (but not both) the title or the labels. You don't give content an extra boost if you match a term across the title, body, labels, and comments.
- **Avoid using variations of the same word with different capitalization**

 In general, labels are case insensitive. This means that you can create the labels "automobile" and "AUTOmobile" and although they will exist as two separate labels, users will be able to do a text search on "automobile" and receive results for articles with either label attached. This is because help center search normalizes the label capitalization prior to searching and delivering results. However, since filters require an exact match, using a label filter in the Manage articles view to locate articles with the "automobile" label will not display articles with the "AUTOmobile" label. Therefore, it is good practice to keep the capitalization of your labels consistent so that users can easily find and filter on the label they need.

## Using the help center API to filter articles by labels

There are two ways you can filter articles by labels using the [Help center API](https://developer.zendesk.com/rest_api/docs/help_center/article_labels):

- [Article](https://developer.zendesk.com/rest_api/docs/help_center/articles#label-names):
 /api/v2/help\_center/en-us/articles.json?label\_names=foo​
- [Search](https://developer.zendesk.com/rest_api/docs/help_center/search#filtering-by-labels):
 /api/v2/help\_center/en-us/articles/search.json?label\_names=foo

These two endpoints behave differently and will return different article results. They are programmatically different and query different data sources for their results. The Articles endpoint queries the Help Center database, whereas the Search endpoint uses native Help Center search. As a result, relevancy matching determines which articles are returned by the label query for the Search endpoint. See [About Help Center end user search](https://support.zendesk.com/hc/en-us/articles/4408894061338-About-Help-Center-end-user-search) for more information about how native Help Center search works.