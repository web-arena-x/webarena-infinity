# Wordpress: Setting up anonymous ticket submissions with Zendesk Support for Wordpress

Source: https://support.zendesk.com/hc/en-us/articles/4408886063258-Wordpress-Setting-up-anonymous-ticket-submissions-with-Zendesk-Support-for-Wordpress

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

The Zendesk Support for Wordpress plugin includes a comment form that you can add
to the Wordpress administrator dashboard so that your site users can easily submit support
requests (see [Setting up and using the Zendesk for WordPress plugin](https://support.zendesk.com/hc/en-us/articles/4408886694810)). By default, only your
registered Zendesk Support users can submit requests. You can however allow your Wordpress site users
who are not also Zendesk Support users (considered anonymous users) to submit support
requests.

There are several easy steps to set this up:

1. Enable anonymous ticket submissions in the Zendesk Support for Wordpress plugin.
2. Choose an existing administrator or agent who is also a user in your Wordpress
   site to act as the delegator for anonymous requests.
3. Have the assigned agent sign in via the Zendesk Support widget to
   authenticate their account.

This delegator role is simply a means to access your Zendesk Support instance and submit the request on behalf
of the anonymous user. Depending on how you set up Zendesk Support (open or registered users
only), the requester may also be required to register and create a login so
that they can follow up with the ticket.

Note: Anonymous requesters are never aware that their request was submitted via this
delegator; it's all done under the hood via the Zendesk API.

When you're setting the visibility permissions for your Wordpress site users (see [Setting the dashboard widget visibility by user type](https://support.zendesk.com/hc/en-us/articles/4408886694810#topic_rzc_xis_mc)), you
should allow all agent users to see the ticket widget on their Wordpress dashboard so that
they can sign in and be authenticated via the widget, which is required to set
up this delegation.

The delegation agent needs to login here before they can be assigned the delegator role:

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/wp_support_login.png)

**To allow anonymous support requests**

1. Log into Wordpress as an administrator.
2. Select **Settings** from the Zendesk panel.
3. You should have first enabled the contact form for one or more types of users via the
   visibility settings described in [Setting the dashboard widget visibility by user type](https://support.zendesk.com/hc/en-us/articles/4408886694810#topic_rzc_xis_mc).
4. Select the **Anonymous Requests** check box.
5. Select a agent from the **Anonymous Requests By** drop-down list.

   Note: Only agents
   that have logged into Zendesk via the widget are shown in the list.
6. Click **Save Settings**.

Anonymous users can now submit requests using the contact form on the Wordpress administrator
dashboard.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/wp_contact_form.png)

Follow up on requests submitted via this form are handled in Zendesk Support.

Another way to create tickets for anonymous users is to convert blog comments into tickets
(see [Converting a blog post comment into a ticket](https://support.zendesk.com/hc/en-us/articles/4408886694810#topic_hhr_vss_mc)).