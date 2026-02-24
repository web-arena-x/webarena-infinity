# Rendering URIs in comments as links automatically

Source: https://support.zendesk.com/hc/en-us/articles/4408830863130-Rendering-URIs-in-comments-as-links-automatically

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

Location: Admin Center > Objects and rules > Tickets > Settings

Administrators can make certain uniform resource identifiers (URIs) in agent comments render as links automatically. The URI must be specified in your admin settings in order for this to happen, and the comment must come from an agent, not an end user. It doesn’t matter whether the comment is private or public, or was added by replying to an email notification or from the Support interface.

You may want to do this if you agents frequently copy links from an app on their mobile device into comments.

This article includes these sections:

- [Entering your custom URI schemes](#topic_nxk_yc1_5kb)
- [When URLs automatically become links](#topic_ktk_2d1_5kb)

## Entering your custom URI schemes

A URI can be an address for a specific location in a mobile app. URIs in comments from end users cannot be rendered as links automatically. All URLs and URIs include a *scheme*. For example, let’s say that you want this URI to be rendered as a link automatically in agent comments:

```
chrome://version/
```

This URI includes a custom scheme. The scheme is *chrome*. You need to enter *chrome* into the **Render URIs as hyperlinks** field.

**To render URIs in comments as links automatically**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_objects_rules_icon.png) **Objects and rules** in the sidebar, then select **Tickets > Settings**.
2. Click **Comment options for agents** to expand it.
3. In the **Render custom URIs as hyperlinks** field, type the the custom URI *schemes*.

   URIs in comments by agents that include these schemes will become links automatically. URIs in end-user comments will remain plain text.

   Make sure that you enter the correct names. Zendesk cannot verify that the names are correct for you. Check with the administrator of the app, if needed, for verification.
4. Click **Save**.

## When URLs automatically become links

When an agent or end user replies to a ticket, URLs that include the following schemes will automatically becomes active links:

- http
- https
- mailto
- tel
- ftp
- aim
- jabber
- facetime
- gtalk
- im
- irc
- rtsp
- skype
- webcal
- chrome-extension