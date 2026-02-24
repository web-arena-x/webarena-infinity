# Setting up user authentication for messaging

Source: https://support.zendesk.com/hc/en-us/articles/4411666638746-Setting-up-user-authentication-for-messaging

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

When you provide conversational support, users might try to carry on a conversation across multiple devices and channels. By [authenticating end users](https://support.zendesk.com/hc/en-us/articles/8851239832090), you can make sure all points of contact are associated with the correct end user. This can enhance the quality of support your agents provide and increase the security of sensitive information that might come up while agents assist your end users.

This article contains the following topics:

- [Terminology for messaging authentication](#topic_h1b_5s4_2bc)
- [Overview of implementing messaging authentication for end users](#topic_wby_vs4_2bc)
- [Creating and sharing a signing key](#topic_nyp_qzx_1bc)
- [Authenticating end users with only an external ID](#topic_mty_p5q_1bc)
- [Incorporating email identities into your user authentication](#topic_it5_52r_1bc)
- [Resolving conflicts between external IDs and emails in JWTs](#topic_klx_mpt_3bc)

Related article: [Understanding user authentication for messaging](https://support.zendesk.com/hc/en-us/articles/8851239832090).

## Terminology for messaging authentication

In addition to understanding the user and agent experience with messaging authentication, it's important to understand the following terminology when implementing messaging authentication:

- **JWT**: Zendesk uses signed JSON Web Tokens (JWTs) to authenticate end users for messaging. These tokens contain details that verify the identity of the end users. For more information about JWT, see [jwt.io](https://jwt.io/).
- **Signing key**: A signing key is created by a Zendesk admin in Admin Center and shared with a developer on your team, who then uses it to sign the JWT as necessary.
- **External ID**: An alphanumeric string, such as an ID from an external system, that is unique to each user. This is the primary identification for messaging authentication, even when an email address is included in the JWT.
- **User name**: (Optional) The name of the end user associated with the external ID or email address. If you include the user's name in the JWT, it appears in the Agent Workspace. This information can help agents communicate with end users.
- **Email**: (Optional) The unique email address associated with an end user.

## Overview of implementing messaging authentication for end users

Zendesk uses JSON Web Tokens (JWTs) to authenticate messaging end users, which provides a flexible and stateless way to verify user identities and secure API endpoints.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/messaging_authentication_flow.png)

Implementing end-user authentication for messaging requires collaboration between admins and a developer on your team.

1. The process of messaging authentication begins with an admin generating a signing key and providing it to a developer. Then the developer uses the signing key to implement a back-end service that can create signed JWTs for users as requested.
2. When requested, the back-end service creates and returns signed JWTs to your website or mobile app. The JWTs created by this service must include a unique external ID and, optionally, an email address to identify the end user.
3. Anytime the user is logged in, your website or app needs to call an equivalent [login API](https://developer.zendesk.com/api-reference/widget-messaging/web/authentication/#login) available for Web Widget and mobile SDKs, at which time the JWT is passed to Zendesk to verify the claimed identity of the user.

Note: Optionally, you can [turn on help center authentication](https://support.zendesk.com/hc/en-us/articles/9495852479770) to automatically associate user identities with end users logged in to the help center.

For more information, particularly for the developers on your team, see [Enabling authenticated visitors for messaging with Zendesk SDKs](https://developer.zendesk.com/documentation/zendesk-web-widget-sdks/sdks/web/enabling_auth_visitors) or watch the following video:

*Authenticating end users in web messaging (17:22)*

## Creating and sharing a signing key

Signing keys are used by developers to create JWTs for end users. You must be an admin to create a signing key. You can create a maximum of 10 keys. If you attempt to create a new key after reaching your limit of 10, you are prompted to delete unused keys.

**To create and share a signing key**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_account_icon.png)
   **Account** in the sidebar, then select **Security > End user authentication**.
2. Click the **Messaging** tab, then click **Create key**.

   If you are creating your first key, **Create key** appears at the bottom of the page. Otherwise, it appears in the top-right corner.
3. Enter a **Name** for the key and click **Next**.
4. When prompted, click **Copy** to copy the shared secret.

   The key is saved and an ID is automatically assigned. You can find a key's ID in the list of keys on the Messaging tab of the End user authentication page.
5. Confidentially send the key's ID and the shared secret you copied to your developer.
6. Click **Hide key forever**.

## Authenticating end users with only an external ID

To authenticate an end user, you must supply an external ID in the JWTs you issue to users. Zendesk uses the external ID provided in a JWT as the primary identifier for user authentication for messaging. When performing the user authentication, Zendesk first resolves an existing user with the external ID. If an [email address](#topic_it5_52r_1bc) is included in the JWT, it is used to resolve user identity only when no existing users match the external ID.

### Signing JWTs with an external ID only

After an admin creates a signing key, the developer on your team can use it to create a service that generates JWTs for end users. When your developer creates JWTs using an external ID, the JWT payload needs to include the following information:

- **external\_id**: (Required) This is the unique alphanumeric string that can be used to identify each user. See [Selecting the external ID to use in JWTs issued to users](https://support.zendesk.com/hc/en-us/articles/4411666638746#topic_tdn_zz2_h2c).
- **scope**: (Required) The caller's scope of access. The only valid value is `user`.
- **name**: (Optional) The name of the user. Including the name in the JWT payload allows Zendesk to display the user's name in the Agent Workspace and helps your agents provide more customized support.

For example:

```
{
    "external_id": "12345678",
    "scope": "user",
    "name": "Jane Soap"
}
```

### Selecting the external ID to use in JWTs issued to users

Consider the following requirements and expectations when deciding what to use as external IDs in the JWTs you issue to users:

- An external ID must be an alphanumeric string.
- External IDs can be a maximum of 255 characters.
- Each user's external ID must be globally unique at the account level.

 If your account has [multiple brands](https://support.zendesk.com/hc/en-us/articles/4408829476378), external IDs must be unique across all brands.
- A user's external ID should never change.
- A user can have only one external ID assigned to them.

Some examples of good choices for external IDs include: an incremented or randomized ID assigned at initial contact (example: usr\_12345) or, for multiple brands, a brand-specific identifier combined with an incremented or randomized ID assigned (example: brand1\_a8dedg).

Avoid using the user's email address and phone number because these can change over time and users can have multiple values. Also avoid the user's name, since this may not be unique.

## Incorporating email identities into your user authentication

In addition to the external ID, you can choose to use email identities with authenticated users, unauthenticated users, or both:

- Authenticated users are authenticated through signed JWTs.

 The use of JWTs provides a trustworthy approach because the content of a signed JWT can't be tampered with by end users. If you're concerned about impersonation attacks, you should restrict email identities to authenticated end users. This is the most secure option and is the default configuration for new Zendesk accounts.
- Unauthenticated users are end users who provide an email address in response to a prompt by a Zendesk bot.

 Keep in mind that permitting the use of email identities for unauthenticated users can make you vulnerable to people impersonating other users by providing an email address they don't own.

Tip: **Contributed by community member [Thomas Verschoren](https://internalnote.com/author/verschoren/)** from his blog post [Messaging authentication: Verified email and merging existing users based on email](https://internalnote.com/messaging-authentication-identify-and-merge-existing-users/).

The following flow chart demonstrates how email identities can be used in your messaging authentication:

[View full size](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/messaging_auth_email-identities-flow.pdf)
![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/messaging_auth_email-identities-flow.png)

### Configuring email identities

With the Web Widget or mobile apps, users can provide their email address in response to a form or AI agent prompt. In these scenarios, there's nothing preventing a malicious user from providing someone else's email address in an attempt to impersonate them. However, using JWTs to authenticate users with both external IDs and email identities is a more trustworthy way to assign email addresses to users.

Depending on your settings, agents could see both form-collected and JWT-provided email addresses in user profiles. On new Zendesk accounts, email identities are turned on and configured to use only verified email addresses. This is the most secure option. Older accounts are configured to use both verified and unverified email addresses.

**To turn on email identities**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_channels_icon.png)
   **Channels** in the sidebar, then select **Messaging and social >
   Messaging**.
2. Click **Manage settings**.
3. Click **Email identities**, and then select one of the following options:
   - **[Use only verified emails](#topic_sng_glf_h2c)**: (Default) Email identities are created only for users who are authenticated and have a verified email address included in their issued JWT.
   - **[Use both verified and unverified emails](#topic_xyb_3lf_h2c)**: In addition to the email identities for authenticated users with verified email addresses being visible in user profiles, unverified email addresses provided by users through AI agent flows are also added to the user's profile.
4. (Not recommended) If you want any user, even unauthenticated users, to be able to claim verified email addresses, select **[Unauthenticated user can claim verified emails](#topic_rdc_jlf_h2c)**.
5. Click **Save settings**.

#### Using only verified emails

Email identities are created only for users who are authenticated and have a [verified email address](https://openid.net/specs/openid-connect-core-1_0.html#StandardClaims) included in their issued JWT.

With this option, agents see the email address provided by unauthenticated end users in the conversation history, but they won't see an email identity attached to the user. If an agent needs to follow up with an unauthenticated user over email, they must manually add the email identity to that user record.

Note: Prior to manually adding an email identity or merging two user records, we recommend having your agents perform an identity verification check to prevent social engineering attacks.

#### Using both verified and unverified emails

In addition to the email identities for authenticated users with verified email addresses being visible in user profiles, unverified email addresses provided by users through AI agent flows are also added to the user's profile.

This option is less secure because malicious users could still attempt impersonation attacks. However, agents can inspect the user profiles to determine whether an email address is verified. Unverified email addresses are clearly marked in the Agent Workspace. When agents need to send email follow-ups, they can be instructed to verify end users with security questions to increase confidence that the end user is who they say they are.

In the event of a conflict, verified email identities supersede unverified email identities. This prevents imposters from squatting on unverified email addresses. For example, if an unauthenticated user provides an email address that is later provided by an authenticated user in a JWT as a verified email address, the email identity goes to the verified email.

| Event order | Event | Resulting email identity |
| --- | --- | --- |
| 1 | An unauthenticated user provides a form-collected email. For example, *alice@example.org* | Zendesk creates a new, unauthenticated user (id: 12345) with the unverified email identity (alice@example.org). |
| 2 | An authenticated user is issued a JWT with the following claims: - external\_id: *1A23B* - email: *alice@example.org* - email\_verified: *true* | Zendesk creates a new, authenticated user (id: 22345) with a verified email identity (alice@example.org). The unauthenticated user (id: 12345) loses its unverified email identity because it was superseded by a verified identity. |

#### Allowing unauthenticated users to claim verified emails (not recommended)

In contrast to the other email identity options, this setting allows users to assume the identity of authenticated users simply by providing that user's email address when prompted. When selected, verified emails don't supersede unverified emails.

This option is the least secure and most susceptible to impersonation attacks. However, diligent agents can still detect potential imposters in this scenario by looking for the green check mark icon on the user's profile and next to their messages, which indicates whether the user is authenticated.

When you select this option, the verification state of email identities collected from messaging channels is no longer trustworthy because an imposter can show up after a user is authenticated and take possession of their email status in a later messaging interaction. This means impersonation attacks are more likely to succeed and agents have limited means of knowing whether the end user is who they claim to be. However, verified email identities still supersede unverified email identities and the email identity is removed from the imposter's user record.

### Issuing JWTs with email addresses

If you're using email identities, you must include two additional claims in the [JWTs you issue to end users](#topic_mty_p5q_1bc). That means your JWTs will include the following fields:

- **external\_id**: (Required) This is the unique alphanumeric string that can be used to identify each user. See [Selecting the external ID to use in JWTs issued to users](https://support.zendesk.com/hc/en-us/articles/4411666638746#topic_tdn_zz2_h2c).
- **scope**: (Required) The caller's scope of access. The only valid value is `user`.
- **name**: (Optional) The name of the user. Including the name in the JWT payload allows Zendesk to display the user's name in the Agent Workspace and helps your agents provide more customized support.

- **email**: (Required) The email address of the user being signed in.
 Must be unique to the user.

 Set the email address to the user's primary email address in Agent Workspace. The inclusion of secondary email addresses in JWTs isn't supported.
- **email\_verified**: (Optional) Whether the end user in question has proven ownership of the email address. If you want end users to have verified email identities, the JWTs you issue must contain both `email` and `"email_verified": true` claims.

For example:

```
{
    "external_id": "12345678",
    "email": "janes@soap.com",
    "email_verified": true,
    "name": "Jane Soap",
    "scope": "user"
}
```

## Resolving conflicts between external IDs and emails in JWTs

Zendesk uses the external ID as the primary identifier, with email addresses being used only if no matches are found for the external ID.

It's best to implement messaging authentication with conflict-avoidance in mind. For example, pick your external IDs and email settings in Zendesk to ensure they can't conflict. If, however, an email address presented in a JWT is already associated with a different external ID, Zendesk rejects the JWT and the end user's login attempt fails. When this happens, the conversation begins with the user in an unauthenticated state.

**To resolve conflicts between external IDs and emails in JWTs**

- Update the JWT to use a different `external_id` value or `email` address.

 OR
- Delete the user with the conflicting `external_id`, freeing it up to be used by a different end user. See [Delete User in the Sunshine Conversations API](https://docs.smooch.io/rest/#operation/deleteUser).