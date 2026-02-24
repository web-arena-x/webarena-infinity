# Login methods

We offer multiple ways to log in and options to restrict login methods for added security.

> [!NOTE]
> Login restrictions are available to workspaces on our [Business](https://linear.app/pricing) and [Enterprise](https://linear.app/pricing) plans.  
>   
> SAML authentication and IP restrictions are only available to workspaces on our  [Enterprise](https://linear.app/pricing) plan.

![Image of the login options available when opening your Linear app for the first time](https://webassets.linear.app/images/ornj730p/production/9306cc45d0751696c7f04f496ff4934408921c52-1820x1238.png?q=95&auto=format&dpr=2)

## Overview

Linear provides several options for members to log into a workspace and allows for different tiers of restriction methods for added security.

## Login methods

### Google authentication

Members can authenticate with Linear using Google authentication when using a Google supported email address.

### Email login

When selecting **Continue with Email** as the login option, an email will be sent to your inbox containing a login link. You can either use the link to log in or copy the code provided in the email and paste it into the "Enter code" field on the login page.

> [!NOTE]
> We recommend whitelisting notifications@linear.app and/or pm_bounces@pm-bounces.linear.app as trusted senders in your email settings to ensure login emails reach your inbox.

### Passkey

Passkeys allow a secure and fast login without having to rely on passwords. They are supported by all major browsers, mobile operating systems, and many password managers like 1Password. You can register multiple devices to log in via passkey from _[Preferences > Account > Security & Access](https://linear.app/settings/account/security)._

### SAML

Refer to our [SAML](https://linear.app/docs/saml-and-access-control) help docs.

## Restrict login methods

Admins can require specific login methods to allow for all members. This setting can be managed by navigating to [Settings > Administration > Security](https://linear.app/settings/security).   
  
Users with the highest role in the workspace (owners or admins, depending on the workspace) can login through any method to ensure they have access to these settings and prevent lockouts for other users.

### IP restrictions

> [!NOTE]
> IP restrictions are available only on the Enterprise plan.

Workspace access can be restricted to specific IPs to enable an extra security layer for accessing Linear. Once set, all direct user access to the workspace, including web, desktop, mobile, and API access, will be limited to the set of configured IPs. Access can be restricted to one or more IP addresses or ranges, specified using CIDR notation.

To configure IP restrictions, go to [Settings > Administration > Security](https://linear.app/settings/security).

![Ip restrictions setting ](https://webassets.linear.app/images/ornj730p/production/a9e4293f618f19e37be643b36a3051d65de220dc-2502x976.png?q=95&auto=format&dpr=2)

## Switch accounts and workspaces

You can log in to multiple user accounts in Linear, which allows you to switch between workspaces associated with those accounts without re-authenticating. To add a user account:

1. Click on your workspace name in the top left corner to launch a dropdown
2. Hover over **Switch workspace**.
3. Select **Create or join a workspace**.
4. (Optional) Follow the prompts to create a new workspace.
5. If you have an existing workspace under a different email address, click your existing email address in the upper-right corner.
6. Select **Add account**.
7. Log in using a different email.
8. Once authenticated, you will be directed to the last visited workspace for that email address.

If you click the workspace name in the upper left and hover over **Switch workspace**, you will see all the other workspaces associated with the added email in the list of option.

## Logging out

For security purposes, when signing out of a workspace in a given location, you will be signed out of all other sessions, requiring you to log back in next time you access Linear elsewhere.  


## FAQ

<details>
<summary>I can't find my workspace after logging in. Where is it?</summary>
Click on your workspace name in the top left and check that you are logged into all accounts. If you see a number next to _Create or join a workspace_, it's possible you've have a pending workspace invite and can accept this to join. If you're still having difficulty, please reach out to support@linear.app.
</details>
