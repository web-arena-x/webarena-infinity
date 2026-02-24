# Enabling and disabling profiles in your help center

Source: https://support.zendesk.com/hc/en-us/articles/4408832453658-Enabling-and-disabling-profiles-in-your-help-center

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Growth, Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support with** | Guide Professional or Enterprise |

Help center profiles display user information, activity, and recent contributions. Help center profiles also enable users to follow one another and get notifications of new articles, posts, and comments for anyone they are following. help center profiles are enabled by default and are available even if you are not using Community in your help center.

This article covers the following topics:

- [About help center profiles](#topic_qf1_dbx_hw)
- [Enabling and disabling help center profiles](#topic_sv1_x1x_hw)

## About help center profiles

Help center profiles can be either *public* or *private*.

- **Public profiles** display user details contributions to everyone.

 ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/hc_profile_public_wes.png)
- **Private profiles** display user details to everyone, but show contributions to only the owner and agents.

 ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/hc_profile_private_oscar.png)

Public profiles become active and visible to all users when the user makes a public contribution, such as a post, community comment, or article comment. Until then, the profile is visible only to the owner and agents.

Help center profiles contain the following user information:

- **Name and optional personal bio**
- **Member since date** - date of the first public contribution
- **Last activity** - date of the last contribution
- **Total activity** - count of all the user's actions
- **Votes** - number of votes the user has given
- **Subscriptions** - number of subscriptions the user has
- **Following and Followed by** - number of users the user is following and being followed by

Public profiles also include an overview of the user's last ten contributions, as well as access to all the user's articles, posts, and comments.

## Enabling and disabling help center profiles

If you are using a [standard help center theme](https://support.zendesk.com/hc/en-us/articles/4408839332250#topic_zkg_rxf_sv), Help center profiles are enabled by default. You can enable or disable profiles as needed in help center settings. If a user's help center profile is disabled, any [badges that are awarded](https://support.zendesk.com/hc/en-us/articles/4408882080026) to that user will be redirected to the admin center profile.

If you are using a [custom help center theme](https://support.zendesk.com/hc/en-us/articles/4408839332250#topic_zkg_rxf_sv) you might need to add code to your custom theme before you can enable help center profiles, see [Adding profiles to your custom help center theme](https://support.zendesk.com/hc/en-us/articles/4408832681626#topic_tq5_fn1_sgb).

You can determine whether you want your help center profiles to be public, for everyone to see, or private, for only the owner and agents to see. Users cannot follow one another with private profiles.

Note: If you are using SSO or the User API and have disabled the “Allow users to view and edit their profile data” setting in Zendesk Support, users will not be able to edit anything other than the description in their help center profile.

**To enable or disable help center profiles**

1. In Guide, click the **Settings** (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/guide_icon_settings.png)) icon in the sidebar.
2. In **Help center settings**, select or deselect **User profiles**.
3. If you are enabling help center profiles, decide whether you want **Public user profiles**, which are visible to everyone, or **Private user profiles**, which are visible to only the user it belongs to and agents.
4. Click **Update**.