# Creating a help center for one of your Support brands 

Source: https://support.zendesk.com/hc/en-us/articles/4408828794778-Creating-a-help-center-for-one-of-your-Support-brands

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Growth, Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support** | Enterprise |

Note: This feature has the following plan restrictions:

- Suite Growth or Professional: Five brands, Five help centers
- Suite Enterprise or Enterprise Plus: 300 brands, 300 help centers
- Support Enterprise with Guide Professional: Five brands, one help center
- Support Enterprise with Guide Enterprise: Five brands, five help centers

When you add [multiple Support brands](https://support.zendesk.com/hc/en-us/articles/4408829476378) to your account, you can also create a separate help center for each brand with each its own articles and community. If you want articles or community posts from one help center to appear in search results for another help center in the same account, you can configure your search settings to enable multiple help center search. See [Enabling search across multiple help centers](../using-help-center-search/enabling-search-across-multiple-help-centers.md).

End users who visit the help center for a specific brand only see tickets for that brand. If you have multiple brands and you're using ticket forms, all ticket forms will be available in all of your help centers.

This article contains the following sections:

- [Creating a help center for a brand](#topic_nm5_dbj_yx)
- [Understanding user authentication with multiple help centers](#topic_bqr_2bj_yx)

## Creating a help center for a brand

You can create additional help centers if you have set up multiple brands. The following plan restrictions apply:

- Suite Growth or Professional: Five brands, Five help centers
- Suite Enterprise or Enterprise Plus: 300 brands, 300 help centers
- Support Enterprise with Guide Professional: Five brands, one help center
- Support Enterprise with Guide Enterprise: Five brands, five help centers

**To create a help center for a brand**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_account_icon.png)
   **Account** in the sidebar, then select **Brand management > Brands**.
2. If you haven't already done so, click **Create brand** to create your brand (see [Creating multiple brands](https://support.zendesk.com/hc/en-us/articles/4408829476378#topic_bp3_gby_wp)).
   If you're adding a help center to an existing brand, make sure that brand is active.
3. On the Brands page, click the brand you want to set up a help center for.
4. Click the **Actions** menu, then click **Turn on Knowledge**.
5. Select one of the available options to create your help center:
   - **Generate a new help center**:
     Automatically create a help center with up to 40 articles using your ticket data and generative AI.
     See [Creating help center content using ticket data and generative AI](https://support.zendesk.com/hc/en-us/articles/9935599563930).
   - **Start from scratch**: Create a help center manually, including building your content architecture and writing your articles. See [Getting started with your help center](https://support.zendesk.com/hc/en-us/articles/4408846795674).
   - ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/KBuilder-brand-genai.png)

To access a branded help center, see [Viewing a help center for one of your brands](https://support.zendesk.com/hc/en-us/articles/4408832814362).

## Understanding user authentication with multiple help centers

When you have multiple help centers to support multiple brands, you cannot restrict users to a specific help center. All of your help centers are accessible to all of your end users, although you can [restrict help center access to signed-in users](https://support.zendesk.com/hc/en-us/articles/4408842656154). However, when end users change from one brand help center to another, they need to click **Sign in**again. They don't need to enter their email address and password again; they are automatically signed in with their credentials.

If you are using remote authentication or SSO, each help center will redirect users to the same single sign-in protocol and database. This is because users belong to the account, not to a specific brand.

When users receive a welcome email, password reset email, or identity verification email, it will include a list of all of your help centers. This ensures that users understand that any changes to their account affect their access to these multiple help centers.