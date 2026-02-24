# Setting up and using the Zendesk Support for WordPress plugin

Source: https://support.zendesk.com/hc/en-us/articles/4408886694810-Setting-up-and-using-the-Zendesk-Support-for-WordPress-plugin

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

Using the Zendesk Support for WordPress plugin, you can connect your WordPress
site and its users. The plugin lets you do the following in WordPress:

- Enable your registered or unregistered (anonymous) Zendesk
  Support users to submit support requests from within the
  WordPress administrator dashboard (see [Setting up anonymous ticket
  submissions with Zendesk Support for
  WordPress](https://support.zendesk.com/hc/en-us/articles/4408886063258)).
- Convert blog comments into tickets and add a public comment that
  can also be posted as a reply in the blog post.
- View all of the tickets in the tickets widget, which is added to
  the administrator dashboard.
- View details for each ticket and then open them in Zendesk
  Support to make updates.
- Add a contact form to the administrator dashboard so that your
  site users can quickly make support requests.
- Set the visibility permissions for each type of registered
  WordPress site user (administrators, editors, authors,
  contributors, subscribers), allowing them to either see the
  tickets widget or the contact form.
- Add Web Widget (Classic) to your WordPress site.
- Enable your users to sign in to Zendesk Support using single
  sign-on (SSO) (see [Setting up single sign-on (SSO) for
  WordPress](https://support.zendesk.com/hc/en-us/articles/4408886723994)).

This article includes the following topics:

- [Installing the Zendesk Support for WordPress plugin](#topic_wem_sen_lc)
- [Uninstalling the Zendesk Support for WordPress plugin](#topic_cwq_2yv_jbc)
- [Configuring the plugin settings](#topic_fbv_mln_lc)
- [Setting the dashboard widget visibility by user type](#topic_rzc_xis_mc)
- [Customizing the contact form](#topic_ckr_ajs_mc)
- [Adding Web Widget (Classic) to your WordPress site](#topic_spa_djs_mc)
- [Submitting a request from the dashboard](#topic_fvt_ass_mc)
- [Using the ticket widget](#topic_anc_dss_mc)
- [Converting a blog post comment into a ticket](#topic_hhr_vss_mc)

## Installing the Zendesk Support for WordPress plugin

You can add the Zendesk Support for WordPress plugin to your WordPress
site just like any other plugin. Plugins are only supported in
self-hosted WordPress sites (wordpress.org), not free-hosted sites
on wordpress.com.

To log into the WordPress plugin in your account, make sure you enable
password access in Zendesk Support.

**To enable password access in Zendesk Support**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_apps_integrations_icon.png)
   **Apps and integrations** in the sidebar, then select **APIs > Zendesk API**.
2. On the Settings tab, enable **Password access**.

**To install the Zendesk Support for WordPress plugin**

1. Download the plugin at <https://wordpress.org/plugins/zendesk/>.
2. Log in to your WordPress site as an administrator.

   Note: If you installed a beta version of the
   Zendesk Support for WordPress plugin, delete it in
   WordPress before installing the new version.
3. In the dashboard, select **Plugin > Add New**.
4. Select **Upload**.
5. Click **Browse** to select the file you downloaded
   (zendesk.zip).
6. Click **Install Now**.
7. After the file is uploaded and installed, click
   **Activate**.

The next step is to configure the plugin with your account information
and select the features you want to enable.

## Uninstalling the Zendesk Support for WordPress plugin

You must log in as a WordPress site administrator to uninstall plugins
from your site.

**To uninstall the plugin**

1. Log in to your WordPress site as an administrator.
2. In the left menu bar, go to **Plugins** > **Installed
   Plugins**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/wordpress_installed_plugins.png)
3. Find Zendesk Support for WordPress in the list of installed
   plugins, then click **Deactivate**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/wordpress_deactivate.png)
4. Click **Delete**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/wordpress_delete.png)

## Configuring the plugin settings

Activating the plugin adds a new panel to the WordPress administrator
dashboard, as shown here:

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/wp_setup_admin.png)

You need to configure your subdomain to access Zendesk Support in
WordPress.

**To configure your Zendesk Support instance in WordPress**

1. Click the set up link and you'll be prompted to enter
   your subdomain.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/wp_enter_zd_subdomain.png)
2. Enter your subdomain.

   Note: If you use host mapping, this
   is automatically detected when you save the
   account settings.
3. Click **Save Settings**.

You will next be prompted to optionally set the visibility permissions
for your registered site users, customize the contact form, allow
support requests from unregistered (anonymous) users, and add Web
Widget (Classic) to your WordPress site.

For information about allowing anonymous users to submit requests, see
[Setting up anonymous ticket submissions
with Zendesk Support for WordPress](https://support.zendesk.com/hc/en-us/articles/4408886063258).

You can set these options immediately or later by selecting the Zendesk
Support settings from the Zendesk Support for WordPress panel, as
shown here:

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/wp_zendesk_panel.png)

### Setting the dashboard widget visibility by user type

You can add either the contact form or the Zendesk Support widget
to the dashboards of the registered users (administrators,
editors, authors, contributors, subscribers) of your
WordPress site. The contact form allows them to submit
support requests directly from WordPress and the ticket
widget allows users who are also Zendesk Support agents to
view tickets and quickly access Zendesk Support to make
ticket updates. In other words, the contact form is for
users who need to submit support requests, and the tickets
widget is for agents to manage tickets.

**To set the dashboard visibility**

1. When you initially set up the plugin, the
   settings page is displayed after you've configured
   Zendesk Support. You can otherwise access this
   page by selecting **Settings** from the Zendesk
   panel. Visibility permissions are set in the
   **Dashboard Widget Visibility** section.
2. For each type of registered site user, you can
   specify the following:
   - Don't display anything
   - Show a contact form
   - Show the tickets widget
3. Choose a visibility setting for all user
   types:
   - Administrators
   - Editors
   - Authors
   - Contributors
   - Subscribers
4. Click **Save Changes**.

### Customizing the contact form

Using the contact form, your registered site users can submit
support requests.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/wp_contact_form.png)

The contact form is added to the WordPress dashboard when enabled
for the types of users described above. You can modify the
wording of each element of the form (title, summary,
description, and the button label) on the **Settings**
page.

Note: You cannot currently add custom fields or modify
this form.

**To customize the contact form**

1. Select **Settings** from the Zendesk Support
   panel.
2. In the **Contact Form Settings** section,
   enter text for the form title, summary label,
   details label, and submit button label.
3. Click **Save Settings**.

### Adding Web Widget (Classic) to your WordPress site

Using the Zendesk Support for WordPress plugin, you can easily
add Web Widget (Classic) to your WordPress site. After
integrating your WordPress site with Zendesk Support, the
Web Widget code is automatically pulled into WordPress.

**To add Web Widget (Classic) to your WordPress site**

1. If you haven't already done so, set up Zendesk
   Support Web Widget (Classic) (see [Using Web Widget (Classic) to
   embed customer service in your
   website](https://support.zendesk.com/hc/en-us/articles/4408836216218)).
2. In WordPress, select **Settings** from the
   Zendesk panel.
3. Select one of the following widget display
   settings:
   - Do not display the Web Widget anywhere (this
     is the default)
   - Display the Web Widget on all posts and
     pages
   - I will decide where the Web Widget displays
     using a template tag
4. If you selected to use a template tag, you can
   then place the widget where you would like it on
   your site using the following template tag:

   ```
   <?php if ( function_exists( 'the_zendesk_webwidget' ) ) the_zendesk_webwidget(); ?>
   ```
5. Click **Save Settings**.

Web Widget (Classic) behaves as it would when added to any other
website. For example, you can configure it to also allow
users to chat with agents and search your knowledge
base.

## Submitting a request from the dashboard

Registered site users who have been granted permission to see the Zendesk
Support contact form (shown above) on their dashboards may submit
support requests. These users can either be registered users in
Zendesk Support or you can allow unregistered (anonymous) users to
submit requests (see [Setting up anonymous ticket submissions
with Zendesk Support for WordPress](https://support.zendesk.com/hc/en-us/articles/4408886063258)).

Users fill out the contact form and click **Submit**. If you've
configured the plugin to allow anonymous submissions, then the
requester is not prompted to sign in to Zendesk Support; an agent
acts as the delegate for anonymous requests. If not, all your users
must sign in before submitting requests. After a request is
submitted, the requester receives the usual email notification.

## Using the ticket widget

Using the tickets widget, agents can view tickets using all of the shared
views in Zendesk Support.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/wp_ticket_widget.png)

By selecting **Change View** you see and can switch to any of the
shared views in Zendesk Support.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/wp_change_view.png)

By clicking on a ticket, you see summary information about the ticket and
make updates.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/wp_ticket_detail.png)

## Converting a blog post comment into a ticket

You can convert blog comments into tickets in the dashboard. Only
comments that have been submitted along with an email address can be
converted into a ticket. The commenter's email address is used to
add them to your instance of Zendesk Support and enable follow-up
communication about the ticket.

**To convert a comment into a ticket**

1. Sign in to the WordPress administrator dashboard, and
   select **Comments**.
2. Locate the comment you want to convert to a ticket and
   click **Convert to Zendesk Ticket**.
3. You'll be prompted to enter a comment, which can be
   posted as a response in the post. Enter your comment
   and then optionally select either or both of these
   two options:
   - Make this a public comment in the ticket
   - Post as a reply on this blog post
4. Click **Create Ticket**.

All follow up on the ticket occurs within Zendesk Support.