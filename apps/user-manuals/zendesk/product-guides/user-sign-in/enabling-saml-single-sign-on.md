# Enabling SAML single sign-on

Source: https://support.zendesk.com/hc/en-us/articles/4408887505690-Enabling-SAML-single-sign-on

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

Verified AI summary ◀▼

Enable SAML single sign-on (SSO) to streamline user authentication across multiple systems. By setting up SAML SSO, you allow users to sign in once using your company's identity provider, enhancing security and simplifying access management. Ensure you meet the technical requirements and configure the SSO settings to assign them to team members or end users, while managing user data effectively.

Location: Admin Center > Account > Security > Single sign-on

Zendesk supports enterprise single sign-on access to Zendesk accounts via Secure Assertion Markup Language (SAML), [JSON Web Token (JWT)](https://support.zendesk.com/hc/en-us/articles/4408845838874), and [OpenID Connect (IODC)](https://support.zendesk.com/hc/en-us/articles/7957465432474). With SSO, users can sign in once using their company sign-in form to gain access to multiple systems and service providers, including Zendesk products.

As a Zendesk admin, your role consists of enabling the SSO options. This article describes how to enable multiple SAML single sign-on configurations that can be used to authenticate team members (admins and agents, including light agents and contributors), end users, or both.

Important: When you use SSO, you are responsible for verifying your users' identities, including their email addresses. If you don't verify your users and their email addresses, your account is at risk of unauthorized access, and Zendesk cannot guarantee or warrant the security of your account.

This article contains the following topics:

- [How SAML SSO for Zendesk works](#topic_3kj_p23_l3)
- [Requirements for enabling SAML SSO](#topic_u54_wc3_z2b)
- [Enabling SAML SSO](#topic_1ms_gf3_l3)
- [Assigning SAML SSO to users](#topic_b15_1gd_jhb)
- [Managing users in Zendesk after enabling SAML SSO](#topic_f4z_nb4_z2b)
- [Switching authentication methods](#topic_t41_h4b_2lb)

The IT team in a company is usually responsible for setting up and managing the company's SAML authentication system. Their role is to implement SSO for Zendesk on the system. Refer the team to the following topic in this article:

- [Technical implementation worksheet](#topic_ttl_524_z2b)

Related articles:

- [Single sign-on (SSO)
 options in Zendesk](https://support.zendesk.com/hc/en-us/articles/4408883587226)
- [Giving users different ways to sign into Zendesk](https://support.zendesk.com/hc/en-us/articles/5380943678106)
- [Accessing your Zendesk account when your SSO service is down](https://support.zendesk.com/hc/en-us/articles/4408882128666)

## How SAML SSO for Zendesk works

SAML for Zendesk works the way SAML does with all other service providers. A common use case is a company where all user authentication is managed by a corporate authentication system such as Active Directory or LDAP (generically referred to as an *identity provider* or *IdP*). Zendesk establishes a trust relationship with the identity provider and allows it to authenticate and sign in users to Zendesk accounts.

A common use case is a user who signs in to their corporate system at the beginning of the work day. Once signed in, they have access to other corporate applications and services (such as email or Zendesk Support) without having to sign in separately to those services.

If a user attempts to sign in directly to a Zendesk account, they are redirected to your SAML server or service for authentication. Once authenticated, the user is redirected back to your Zendesk account and automatically signed in.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/saml_flow.png)

Another supported workflow is giving users access to Zendesk after they sign in to your company's website. When a user signs in to the website using their website credentials, the website sends a request to the identity provider to validate the user. The website then sends the provider's response to the SAML server, which forwards it to your Zendesk account, which grants a session to the user.

## Requirements for enabling SAML SSO

Meet with the team in your company responsible for the SAML authentication system (usually the IT team) to make sure your company meets the following requirements:

- The company has a SAML server with provisioned users or connected to an identity repository such as Microsoft Active Directory or LDAP. Options include using an in-house SAML server such as OpenAM, or a SAML service such as Okta, OneLogin, or PingIdentity.
- If using an Active Directory Federation Services (ADFS)
 server, forms-based authentication must be enabled.
 Zendesk does not support Windows Integrated Authentication (WIA). For more information, see [Setting up single sign-on using Active Directory with ADFS and SAML](https://support.zendesk.com/hc/en-us/articles/4408834714650).
- Zendesk-bound traffic is over HTTPS, not HTTP.

You'll need the following information to configure a SAML SSO method in Zendesk. Your IT team should be able to provide this to you.

- The remote login URL for your SAML server (sometimes called SAML Single Sign-on URL)
- (Optional) The remote logout URL where Zendesk can redirect users after they sign out of Zendesk
- (Optional) A list of IP ranges to redirect users to the appropriate sign-in option. Users making requests from the specified IP ranges are routed to the remote SAML authentication sign-in form. Users making requests from IP addresses outside the ranges are routed to the normal Zendesk sign-in form. If you don't specify a range, all users are redirected to the remote authentication sign-in form.
- The SHA2 fingerprint of the SAML certificate from your SAML server. X.509 certificates are supported and should be in PEM or DER format, but you'll still need to provide a SHA2 fingerprint for the X.509 certificate. There is no upper limit on the size of the SHA fingerprint.

The IT team may require additional information from Zendesk to configure the SAML implementation. Refer them to the [Technical implementation worksheet](#topic_ttl_524_z2b) in this article.

After you've confirmed that you meet the requirements and have all of the necessary information, you're ready to [enable SAML SSO](#topic_1ms_gf3_l3).

## Enabling SAML SSO

Admins can enable SAML single sign-on only for end users, only for team members (including light agents and contributors), or for both groups. You can create multiple SAML SSO configurations. Before you start, obtain the required information from your company's IT team.
See [Requirements for enabling SAML SSO](#topic_u54_wc3_z2b).

**To enable SAML single sign-on in Zendesk**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_account_icon.png)
   **Account** in the sidebar, then select **Security > Single sign-on**.
2. Click **Create SSO configuration** then select **SAML**.
3. Enter a unique **Configuration name**.
4. For **SAML SSO URL**, enter the remote login URL for your SAML server.
5. Enter the SHA-256 **Certificate fingerprint**. This is required for us to communicate with your SAML server.
6. (Optional) For **Remote logout URL**, enter a logout URL where users should be redirected after they sign out of Zendesk.
7. (Optional) For **IP ranges**, enter a list of IP ranges if you want to redirect users to the appropriate sign-in option.

   Users making requests from the specified IP ranges are routed to the remote SAML authentication sign-in form. Users making requests from IP addresses outside the ranges are routed to the normal Zendesk sign-in form. Don't specify a range if you want all users to be redirected to the remote authentication sign-in form.
8. Select **Show button when users sign in** to add a **Continue with SSO** button to the Zendesk sign-in page.

   You can customize the button label by entering a value in the **Button name** field. Custom button labels are useful if you add multiple SSO buttons to the sign-in page. See [Adding "Continue with SSO" buttons to the Zendesk sign-in page](https://support.zendesk.com/hc/en-us/articles/4408882188570#topic_rqg_yw4_2yb) for more information.
9. Click **Save**.

   By default, enterprise SSO configurations are inactive. You must [assign the SSO configuration to users](#topic_b15_1gd_jhb) to activate it.

## Assigning SAML SSO to users

After creating your SAML SSO configuration, you must activate it by assigning it to end users, team members, or both.

**To assign an SSO configuration to team members or end users**

1. Open the Security settings for team members or end users.
   - In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_account_icon.png)
     **Account** in the sidebar, then select **Security > Team member authentication**.
   - In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_account_icon.png)
     **Account** in the sidebar, then select **Security > End user authentication**.
2. Select **External authentication** to show the authentication options.
3. Select the name(s) of the SSO configuration(s) you want to use.

   Single sign-on might not cover all use cases, so Zendesk authentication remains active by default.
4. Select how you'd like to allow users to sign in.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_security_choose-sign_in.png)

   **Let them choose** allows users to sign in using any active authentication method. See [Giving users different ways to sign into Zendesk](https://support.zendesk.com/hc/en-us/articles/5380943678106).

   **Redirect to SSO** only allows users to authenticate using the [primary SSO configuration](https://support.zendesk.com/hc/en-us/articles/4408882188570#topic_c55_3sf_vsb). Users don’t see additional sign-in options, even if those authentication options are active. When you select **Redirect to SSO**, the **Primary SSO** field appears for you to select the primary SSO configuration.
5. Click **Save**.

## Managing users in Zendesk after enabling SAML SSO

After enabling SAML single sign-on in Zendesk, changes made to users outside Zendesk don't automatically sync to your Zendesk account.
Users are updated in Zendesk at the point of authentication. For example, if a user is added to your internal system, the user is added to your Zendesk account when they sign in to Zendesk. When changes are made to the user's data in your internal system (such as name or email address), any attributes shared in the payload of the SAML are updated in Zendesk. If a user is deleted from your internal system, the user will no longer be able to sign in to Zendesk.
However, their account will still exist in Zendesk.

By default, the only user data stored in Zendesk when single sign-on is enabled is the user's name and email address. Zendesk does not store passwords. As a result, you should turn off any automated email notifications from Zendesk about passwords.

To provide a better customer experience, you might want to store more than just the user's name and email address in Zendesk. See [Obtaining additional user data](#topic_d1r_523_l3).

### Turning off password notification emails from Zendesk

A Zendesk user profile is created for any new user who accesses your Zendesk account through SAML, JWT, or OpenID Connect (OIDC) single sign-on.
Because users are authenticated through an IdP with a non-Zendesk password, the profile is created without a password because they don't need to sign in to Zendesk directly.

Because new users who sign in to Zendesk through SSO are verified through an IdP, they don't receive email notifications to verify their account.
However, it is still recommended to turn off these automated email notifications to prevent them from being sent if the IdP does not successfully verify the user. In the case of SSO, user verification must always occur through the IdP.

**To turn off password notification emails**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_people_icon.png)
   **People** in the sidebar, then select **Configuration > End users**.
2. In the **Account emails** section, deselect **Also send a welcome email when a new user is created by an agent or administrator**.
3. In **Allow users to change their password**, deselect this option.

## Switching authentication methods

If you use a third-party SSO method to create and authenticate users in Zendesk and then switch to Zendesk authentication, these users will not have a password available for login. To gain access, ask these users to reset their passwords from the Zendesk sign-in page.

## Technical implementation worksheet

This section is for the team in the company responsible for the company's SAML authentication system. It provides details about the Zendesk SAML SSO implementation.

Topics covered:

- [Required user data to identify the user being authenticated](#topic_eqz_shy_1fb)
- [Configuring the identity provider for Zendesk](#topic_dzb_qx5_2v)
- [Configuring the SAML server for Zendesk](#topic_hzw_rt4_z2b)
- [Parameters returned to your remote sign-in and sign-out URLs](#topic_s2n_hg1_bfb)
- [Using RelayState to redirect users after authentication](#topic_xx3_ym4_21c)
- [Troubleshooting the SAML configuration for Zendesk](#topic_2dp_mf3_l3)

### Required user data to identify the user being authenticated

When you implement SAML SSO access to Zendesk accounts, you specify certain user data to identify the user being authenticated.

These topics describe the data you need to provide:

- [Specifying the user's email address in the SAML subject's NameID](#topic_dzb_ul5_2v)
- [Specifying two required user attributes in the SAML assertion](#topic_dzb_gl5_2v)

#### Specifying the user's email address in the SAML subject's NameID

Zendesk uses email addresses to uniquely identify users.
You should specify the user's email address in the SAML subject's name ID.

For example:

```
 <saml:Subject>
      <saml:NameID Format="urn:oasis:names:tc:SAML:1.1:nameid-format:unspecified">stevejobs@yourdomain.com</saml:NameID>
      <saml:SubjectConfirmation Method="urn:oasis:names:tc:SAML:2.0:cm:bearer">
        <saml:SubjectConfirmationData NotOnOrAfter="2014-04-23T21:42:47.412Z"/>
      </saml:SubjectConfirmation>
    </saml:Subject>
```

If the givenname and surname attributes aren't provided, Zendesk will use the username of the email address provided in the `<saml:Subject>` `<saml:NameID>` element as the name of the user. The first part of an email address before the '@' symbol is the username.

If the email's username has a period character in it, then we will use it to parse out a first name and last name. If there is no period character, then the whole username becomes the name of the user in Zendesk. For example, if the email address `<saml:Subject><saml:NameID>` is *stanley.yelnats@yourdomain.com*, the user's name in Zendesk would be stored as *Stanley Yelnats*; however, if the email address is *stanleyyelnats@yourdomain.com*, the user name in Zendesk would be stored as *Stanleyyelnats*.

Note: If you're setting up Microsoft Entra SSO, ensure the Name claim points to the field where your users' login email addresses are stored. This value is usually **user.mail**, but your setup may be different.

#### Specifying two required user attributes in the SAML assertion

If you specify the *givenname* and *surname* attributes, you must use the full namespace rather than the friendly names. For example: where the friendly name might be 'surname', the actual value you need to specify for the attribute is *http://schemas.xmlsoap.org/ws/2005/05/identity/claims/surname*

| Concept | Attribute | Description | Example value |
| --- | --- | --- | --- |
| first name | givenname | The given name of this user. You must specify the full namespace for this attribute. | ``` http://schemas.xmlsoap.org/ws/2005/05/identity/claims/givenname ``` |
| last name | surname | The surname of this user. A user in Zendesk is created or updated in accordance with this user's given name and surname. See example below. You must specify the full namespace for this attribute. | ``` http://schemas.xmlsoap.org/ws/2005/05/identity/claims/surname ``` |

Given name and surname example:

```
<saml:Attribute Name="http://schemas.xmlsoap.org/ws/2005/05/identity/claims/givenname">
 <saml:AttributeValue xsi:type="xs:anyType">James</saml:AttributeValue>
 </saml:Attribute>
 <saml:Attribute Name="http://schemas.xmlsoap.org/ws/2005/05/identity/claims/surname">
 <saml:AttributeValue xsi:type="xs:anyType">Dietrich</saml:AttributeValue>
 </saml:Attribute>
```

Zendesk supports [additional user attributes](#topic_d1r_523_l3).
Talk to your Zendesk Support admin about their data requirements in Support.

#### Obtaining additional user data

The only user data required by Zendesk from your authentication system is the user's given name, surname, and email address. The given name and surname are the only attribute names you should use to capture information about a user's name. However, you can get more data by asking your IT team to add user attributes to the SAML assertions the identity provider sends to Zendesk when users sign in.

A [SAML assertion](http://saml.xml.org/assertions) contains one or more statements about the user. One statement is the authorization decision itself – whether or not the user was granted access. Another statement can consist of attributes describing the signed-in user.

Zendesk supports the following additional user attributes for signed-in users. Define your data requirements in Support, then meet with your IT team to discuss adding user attributes to the SAML assertions.

Note the following considerations:

- Zendesk only recognizes these additional user attributes if the attribute names outlined in the table below are used in the assertion's attribute statement. If you try to use the full namespace for these attributes, they'll be ignored.
- Attribute names are case sensitive, so you must match the exact casing shown in the tables below.

| Attribute name | Description |
| --- | --- |
| organization | The name of an organization to add the user to. If the organization doesn't exist in Zendesk, it won't be created. The user will still be created, but they won't be added to any organization. If [**Allow users to belong to multiple organizations**](https://support.zendesk.com/hc/en-us/articles/4408838140314) is turned on, additional organizations append the original organization and are considered secondary organizations. This does not delete the existing memberships. If you'd like to pass multiple organization names at the same time, use the **organizations** attribute instead. Using the organizations attribute overwrites the existing list of organizations. The organization names must be passed in a string, separated by commas. |
| organization\_id | The organization's [external ID](https://developer.zendesk.com/api-reference/ticketing/organizations/organizations/) in the Zendesk API. If both organization and organization\_id are supplied, organization is ignored. If the organization doesn't exist in Zendesk, it won't be created. The user will still be created, but they won't be added to any organization. If [**Allow users to belong to multiple organizations**](https://support.zendesk.com/hc/en-us/articles/4408838140314) is turned on, additional organizations append the original organization and are considered secondary organizations. This does not delete the existing memberships. If you'd like to pass multiple organization IDs at the same time, use the **organization\_ids** attribute instead. Using the organization\_ids attribute overwrites the existing list of organizations. The organization IDs must be passed in a string, separated by commas. |
| phone | A phone number, specified as a string. |
| tags | Tags to set on the user. The tags will replace any other tags that may exist in the user's profile. |
| remote\_photo\_url | URL for a photo to set on the user profile. |
| locale (for agents) locale\_id (for end users) | The locale in Zendesk, specified as a number. To get a list of valid numbers, see [Locales](https://developer.zendesk.com/rest_api/docs/support/locales) in the API docs. |
| role | The user's role. Can be set to **end-user** , **agent**, or **admin**. Default is **end-user**. |
| custom\_role\_id | Applicable only if the value of the **role** attribute above is **agent**. You can get the ids of your custom roles with the [Custom Roles API](https://developer.zendesk.com/rest_api/docs/support/custom_roles). |
| external\_id | A user id from your system if your users are identified by something other than an email address or if their email addresses are subject to change. Specified as a string. When an `external_id` is included in a SAML assertion, it serves as the primary identifier for the user. If a new email address is provided along with an existing `external_id`, the new email replaces the previous primary email address for the user. The user's old primary email address is removed. Secondary email addresses cannot be set through SAML. |
| user\_field\_<key> | A value for a custom user field in Zendesk Support. See [Adding custom fields to users](https://support.zendesk.com/hc/en-us/articles/4408822051866). The <key> is the field key assigned to the custom user field in Zendesk Support. Example: `user_field_employee_number` where `employee_number` is the field key in Zendesk. Sending a null value or an empty string in the attribute value will remove any custom field value set in Zendesk Support. |

Zendesk also supports a series of [InCommon Federation Attributes](https://www.incommon.org/federation/attributes/) to set user attributes as part of the sign in. For Federation attributes, you should specify the full namespace with the attribute name, not the friendly name.
Examples:

| Friendly name | SAML2 formal name |
| --- | --- |
| ou (organization unit) | urn:oid:2.5.4.11 |
| displayName | urn:oid:2.16.840.1.113730.3.1.241 |

### Configuring the identity provider for Zendesk

The following attributes are required to specify the identify provider:

| Attribute | Value |
| --- | --- |
| entityID | https://*yoursubdomain*.zendesk.com |
| AudienceRestriction | *yoursubdomain*.zendesk.com |

For both values, replace *your\_subdomain* with the Zendesk Support subdomain. If you're unsure of the subdomain, ask your Zendesk admin.

Zendesk enforces the `AudienceRestriction` attribute.

Note: If you're setting up [Microsoft Entra SSO](https://learn.microsoft.com/en-us/entra/identity/saas-apps/zendesk-tutorial), you may need to use *https://yoursubdomain*.zendesk.com or *yoursubdomain*.zendesk.com (without the *https://* prefix) as the Entity ID value.

### Configuring the SAML server for Zendesk

Some SAML servers may require the following information when configuring an integration with Zendesk:

- Access Consumer Service (ACS) URL:
 Specify **https://yoursubdomain.zendesk.com/access/saml** (case sensitive), where 'accountname' with your Support subdomain
- Redirects to SAML Single Sign-on URL: Use **HTTP POST**
- Hashing algorithm (ADFS): Zendesk supports the SHA-2 algorithm when using Active Directory Federation Services (ADFS)

### Parameters returned to your remote sign-in and sign-out URLs

When redirecting users to your authentication system, Zendesk appends the following parameters to the remote sign-in and remote sign-out URLs.

**Remote sign-in URL parameters**

| Attribute | Description |
| --- | --- |
| brand\_id | The brand of the Help Center the user was on when they attempted to sign in. For more information, see [Creating a Help Center for one of your brands](https://support.zendesk.com/hc/en-us/articles/4408828794778). |

**Remote sign-out URL parameters**

| Attribute | Description |
| --- | --- |
| email | Email of the user signing out. |
| external\_id | A unique identifier from your system stored in the Zendesk user profile. |
| brand\_id | The brand of the Help Center the user was on when they signed out. For more information, see [Creating a Help Center for one of your brands](https://support.zendesk.com/hc/en-us/articles/4408828794778). |

If you prefer not to receive email and external id information in the sign-out URL, ask your Zendesk admin to specify blank parameters in the **Remote logout URL** field in the admin interface. See [Enabling SAML SSO](#topic_1ms_gf3_l3). For example:
**https://www.yourdomain.com/user/signout/?email=&external\_id=**.

### Using RelayState to redirect users after authentication

`RelayState` is a parameter used to maintain the state of the originating request throughout the SSO process.
It specifies the original URL the user was trying to access before the SSO process started. After completing the SSO process, you can forward the user to the `RelayState` URL to provide a seamless user experience.

The `RelayState` parameter is optional in SAML. If you don’t include it in your request, the user will be directed to the default location based on their user type.

- For agents, the default location is the agent dashboard in Zendesk Support.
- For end users, the default location is the home page of the help center for your default brand.

When a user accesses a Zendesk link that requires signing in, and you are using SAML, Zendesk redirects the user to the SSO configuration you set up and, along with that, sends the URL the user came from in the `RelayState` parameter.

Example:

```
https://zendesk.okta.com/app/zendesk/exladafgzkYLwtYra2r7/sso/saml?RelayState=https%3A%2F%2Fyoursubdomain.zendesk.com%2Fagent%2Ffilters%2F253389123456&brand_id=361234566920&SAMLRequest=[samlloginrequesthere]
```

When constructing the SAML authentication request, add the `RelayState` parameter and set its value to the URL sent from Zendesk in the SAML response.

Example `RelayState` parameter redirecting users to *https://yoursubdomain.zendesk.com/agent/filters/253389123456*:

```
SAMLResponse=[SAMLpayloadhere]&RelayState=https%3A%2F%2Fyoursubdomain.zendesk.com%2Fagent%2Ffilters%2F253389123456
```

### Troubleshooting the SAML configuration for Zendesk

Here is Zendesk's SAML 2.0 metadata:

```
<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<EntityDescriptor entityID="https://yoursubdomain.zendesk.com" xmlns="urn:oasis:names:tc:SAML:2.0:metadata">
    <SPSSODescriptor AuthnRequestsSigned="false" WantAssertionsSigned="true" protocolSupportEnumeration="urn:oasis:names:tc:SAML:2.0:protocol">
        <NameIDFormat>urn:oasis:names:tc:SAML:1.1:nameid-format:emailAddress</NameIDFormat>
        <AssertionConsumerService index="1" Binding="urn:oasis:names:tc:SAML:2.0:bindings:HTTP-POST" Location="https://yoursubdomain.zendesk.com/access/saml"/> <!-- Note: replace 'accountname' with your Zendesk subdomain -->
    </SPSSODescriptor>
</EntityDescriptor>
```

Zendesk expects a SAML assertion that looks as follows:

```
<samlp:Response xmlns:samlp="urn:oasis:names:tc:SAML:2.0:protocol" ID="s2202bbbb
afa9d270d1c15990b738f4ab36139d463" InResponseTo="_e4a78780-35da-012e-8ea7-005056
9200d8" Version="2.0" IssueInstant="2011-03-21T11:22:02Z" Destination="https://yoursubdomain.zendesk.com/access/saml">
    <saml:Issuer xmlns:saml="urn:oasis:names:tc:SAML:2.0:assertion">myidp.entity.id
    </saml:Issuer>
    <samlp:Status xmlns:samlp="urn:oasis:names:tc:SAML:2.0:protocol">
        <samlp:StatusCode  xmlns:samlp="urn:oasis:names:tc:SAML:2.0:protocol"
Value="urn:oasis:names:tc:SAML:2.0:status:Success">
```

**Note**: Replace 'accountname' in the `Destination` attribute with your Zendesk subdomain.

Zendesk expects user attributes to be specified in an assertion's attribute statement (`<saml:AttributeStatement>`)
as in the following example:

```
<saml:AttributeStatement>
 <saml:Attribute Name="organization">
    <saml:AttributeValue xsi:type="xs:string">Acme Rockets</saml:AttributeValue>
 </saml:Attribute>
 <saml:Attribute Name="tags">
    <saml:AttributeValue xsi:type="xs:string">tag1 tag2</saml:AttributeValue>
 </saml:Attribute>
 <saml:Attribute Name="phone">
    <saml:AttributeValue xsi:type="xs:string">555-555-1234</saml:AttributeValue>
 </saml:Attribute>
 <saml:Attribute Name="role">
    <saml:AttributeValue xsi:type="xs:string">agent</saml:AttributeValue>
 </saml:Attribute>
 <saml:Attribute Name="custom_role_id">
    <saml:AttributeValue xsi:type="xs:string">12345</saml:AttributeValue>
 </saml:Attribute>
 </saml:AttributeStatement>
```

For the names and descriptions of the user attributes supported by Zendesk, see the table in [Obtaining additional user data](#topic_d1r_523_l3) above. Note that the full namespace isn't supported for optional user attributes.