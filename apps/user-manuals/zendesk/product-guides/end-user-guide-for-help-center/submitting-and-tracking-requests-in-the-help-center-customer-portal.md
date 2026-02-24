# Submitting and tracking requests in the help center Customer Portal

Source: https://support.zendesk.com/hc/en-us/articles/4408846805530-Submitting-and-tracking-requests-in-the-help-center-Customer-Portal

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Growth, Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support with** | Guide Professional or Enterprise |

The help center offers the option for end users to submit requests by default. End users who submit requests can also manage their support requests in the [customer portal](https://www.zendesk.com/guide/features/customer-portal-software/). Depending on your account configuration, end users can either view their requests [across all brands](https://support.zendesk.com/hc/en-us/articles/9319604460826) in the Customer Portal or only requests associated with the brand's help center they're currently logged into.

The help center may not offer the option to submit support requests depending on how it's set up. This article describes the default options for submitting and tracking requests in the customer portal without any customization.

Topics covered in this article:

- [Submitting a support request](#topic_hgd_mqd_yy)
- [Updating your support requests](#topic_afk_cfk_cgc)
- [Viewing and tracking your support and service requests](#topic_zhh_w2k_cgc)
- [Marking a request as solved](#topic_bhd_mqd_yy)
- [Creating a follow-up to a solved request](#topic_dhd_mqd_yy)
- [Submitting CSAT for your ticket](#topic_rpc_ygy_ycc)
- [Viewing the service catalog and submitting service requests](#topic_ijj_s2k_cgc)

## Submitting a support request

You can submit requests using the *support request form* (or *web form*) on your help center. Depending on how your help center is set up, users may or may not be required to sign in to submit support requests in your help center.

The support request form may contain more fields than those described in this section. It depends on how the help center is set up. You can't remove any of the default fields on the submit request form; however, you can set up single sign-on (SSO), so users will automatically be signed-in to your help center and will not have to enter their email in the form. See [Single sign-on options in Zendesk](https://support.zendesk.com/hc/en-us/articles/4408883587226) for more information on SSO.

To submit a service request in the service catalog, instead of a support request, see [Viewing the service catalog and submitting service requests](#topic_ijj_s2k_cgc).

**To submit a support request in the help center**

1. In [help center](https://support.zendesk.com/hc/en-us/articles/9041943683354#topic_dzz_4wn_s2c), click **Submit a request** at the top of the page.
2. If the [**CC** option is enabled](https://support.zendesk.com/hc/en-us/articles/4408843795482#topic_x3t_4p5_cq) for the help center and you are signed in, you can add an email address to copy a user on the ticket.

   To copy multiple users, use a comma to separate each email address.
3. Enter a subject and description of the problem.

   As you enter a subject, a list of suggested articles in the knowledge base appears. You can click one of the articles instead of submitting the request. Encouraging end users to look for answers in the knowledge base can deflect tickets.
4. If you belong to multiple organizations, select the organization for this support request.
5. Add any attachments.

   The file size limit is 50 MB.
6. Click **Submit**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/hc_request_form.png)

## Updating your support requests

There are two ways you can update your support requests:

- [Updating a support request by email](#topic_kgd_mqd_yy)
- [Updating a support request in the customer portal](#topic_ngd_mqd_yy)

### Updating a support request by email

You can update an existing support request ticket with a comment by email.

Your email must reference an existing ticket ID, using the proper syntax, in plain text.
You must have permission to update the ticket, either as the ticket requester, a CC on the ticket, or a member of a shared organization for the ticket.

**To update an existing support request by email**

1. In your email client, create a new email message or forward an existing email.

   The email is sent to the support team. The subject can be anything you want.
2. At the top of body of the email, enter the ticket ID for an existing support request using the following syntax:

   ```
   #id ticketnumber
   ```

   For example:

   ```
   #id 123456
   ```
3. Leave one blank line after the ticket ID.
4. Enter the comment you want to add to the ticket after the blank line.

   Your email should look something like this:

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/email_update_ticket_enduser.png)
5. Send the email.

### Updating a support request in the customer portal

You can update any existing support request that is not closed with a comment.

You can also add CCs (if enabled in the help center) to an existing support request. If you belong to multiple organizations, you can also change the organization for a support request when you view it in the help center.

**To update an existing support request**

1. Click your profile icon on the upper-right side of any help center page and then click **Requests**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/guide-profile-menu-24.png)

   By default, the page displays all requests that you have submitted.

   Note: If you are using an older version of the Copenhagen theme, this menu may look different.
2. Click the link for the request you want to update.
3. Add a comment to update the request.
4. (Optional) If the [**CC** option is enabled](https://support.zendesk.com/hc/en-us/articles/4408843795482#topic_x3t_4p5_cq) for the help center and you are signed in, you can add an email address to copy a user on the ticket

   When you add a CC to an existing ticket, you must also add a comment.
5. (Optional) If you belong to multiple organizations, you can change the organization for the support request.
6. Click **Submit**.

## Viewing and tracking your support and service requests

You can track support requests, as well as any service catalog requests in help center, as described in these sections:

- [Tracking your support and service requests](#topic_qgd_mqd_yy)
- [Tracking your organization's support requests](#topic_vgd_mqd_yy)
- [Filter options and behavior by field type](#topic_il4_r4s_4hc)

Note: AI-generated replies from AI agents on email, API, and web form channels aren't visible to the customer when checking the request from the help center.

### Tracking your support requests and service requests

You can use the help center to track your support requests and service catalog requests. Depending on the account [configuration](https://support.zendesk.com/hc/en-us/articles/9319604460826), the list of your requests could reflect all requests for all brands or only those associated with the brand of the help center you're currently logged into.

**To track your support requests and service requests**

1. Click your profile icon on the upper-right side of any help center page and then click **Requests**.

   Note: All of your email addresses must be verified in order to display the Requests page. If you have an unverified email address, you'll be prompted to verify it before you can continue.

   ![](https://zen-marketing-documentation.s3.us-west-1.amazonaws.com/docs/en/Guide-UserProfileLogin.png)

   By default, the page displays all requests that you have submitted with the following columns:

   Subject, ID, Created date, Updated date, Status, and Requester.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/knw-requests.png)

   To show or hide columns on the page, click the option button ( ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/options-menu-icon-small.png)) and then either select or deselect the system and custom fields you want to view or hide, or click **See more columns** to open a separate window where you can show more columns. All columns that are displayed in the list of requests are also shown in the drop down menu together with the six system field columns.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/show+hide+req.png)

   To show custom fields to end users in the new request list, the field permissions must be set to either **Customers can edit** or **Customers can view**. See [Adding custom fields to your ticket and support request form](https://support.zendesk.com/hc/en-us/articles/4408883152794#topic_ubz_ynk_xj).[Team members](https://support.zendesk.com/hc/en-us/articles/4408883763866-Understanding-Zendesk-Support-user-roles#topic_nqx_cbp_cc) will be able to see fields that have the [Agents can edit permission](https://support.zendesk.com/hc/en-us/articles/4408883152794-Adding-custom-fields-to-your-tickets-and-support-request-form#topic_ubz_ynk_xj) as they would have access to those fields in Agent workspace. This is also the case if you are an Admin assuming an end user account.
2. To filter your requests, you can select the **Filter** drop down, then either select the filter and sub filter you want to apply, or select **See all filters** to open the Filters window shown below, where you can select and apply filters and sub filters.

   ![](https://zen-marketing-documentation.s3.us-west-1.amazonaws.com/docs/en/Req+List+Filter+Modal+Jan+2023.png)

   You can select multiple filters to further refine your search criteria. You can also filter on values in fields where you have hidden the column.

   When you select more than one filter, the filters act as an "AND" search criteria, meaning that requests must meet all filter criteria in order to display. When you select multiple filter options within a single filter, they act as an "OR" search criteria, meaning that tickets must meet one or more criteria in order to display. For example, if you select both "Awaiting reply" and "Open" within the Status filter, tickets can have either an "Awaiting reply" or an "Open" status to display.Filters that you apply appear beneath the search field and can be cleared at any time by clicking **Clear filters**.
3. To search your requests, enter a search term in the **Search Requests** box.

   You can optionally use [ticket property keywords](https://support.zendesk.com/hc/en-us/articles/4408886879258#topic_crj_yev_uc) in your search.
4. To see details about a request, click the request title.

   If you belong to multiple organizations, you can change the organization for a request when you view details for that request.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Guide-Request-EU-View.png)

### Tracking your organization's support requests

As an end user, you can be a member of one organization or multiple organizations. If you're a member of a shared organization, you can see tickets for all members of that organization.

Note: A shared organization must be set up by an administrator. See [Setting up a shared organization for end users](https://support.zendesk.com/hc/en-us/articles/4408882246298#topic_nat_vgn_bc).

**To track your organization's support requests**

1. Click your profile icon on the upper-right side of any page and then click **Requests**.

   ![](https://zen-marketing-documentation.s3.us-west-1.amazonaws.com/docs/en/Guide-UserProfileLogin.png)
2. Click the **Organization requests** link on the My requests page to see all the requests in your organizations. The link appears only if you're a member of a shared organization.

   To show or hide columns on the page, click the option button (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/options-menu-icon-small.png)) and then select or deselect the system and custom fields you want to view or hide.
3. To filter the requests, click **Organization** to select the organization that you want to view tickets for, then click the **Filter** drop down to select the filter and sub filter you want to apply. You can select multiple filters to further refine your search criteria.

   When you select more than one filter, the filters act as an "AND" search criteria, meaning that requests must meet all filter criteria in order to display. When you select multiple filter options within a single filter, they act as an "OR" search criteria, meaning that tickets must meet one or more criteria in order to display. For example, if you select both "Awaiting reply" and "Open" within the Status filter, tickets can have either an "Awaiting reply" or an "Open" status to display.
4. To see details about a request, click the request subject.

   You can add comments to a request if an administrator has set it up. See [Setting up a shared organization for end users](https://support.zendesk.com/hc/en-us/articles/4408882246298#topic_nat_vgn_bc).

**To subscribe to requests for a shared organization**

1. Click your profile icon on the upper-right side of any page and then click **Requests**.
2. Click the **Organization Requests** link on the My requests page to see all the requests in your organizations.

   The link appears only if you're a member of a shared organization in Zendesk.
3. Click **Follow organization**.

   If the Follow organization button is not available, ask your administrator to add it to your help center theme (see [Add Follow/Unfollow for users in a shared organization](https://support.zendesk.com/hc/en-us/articles/4408832681626#topic_ccb_5g1_qw)).

   You will now receive notifications for new and updated request in your shared organization.
4. Select the organization that you want to follow, then click **Save**. You will receive updates about tickets in each of your selected organizations.

### Filter options and behavior by field type

Zendesk provides [custom field types](https://support.zendesk.com/hc/en-us/articles/4408838961562) for tickets, users, and organizations. Although the fields displayed in the request form and request list are custom field types, they often have unique names that reflect their purpose. For example, the request list may display a field named “Store location” that is a drop-down field type designed to let users select from a list of store locations. In this case, the request list will display the field name “Store location,” even though it is a drop-down custom field type.

For a list of custom field types that you can filter on, see [About custom field types](https://support.zendesk.com/hc/en-us/articles/4408838961562-About-custom-field-types).

## Marking a request as solved

You can withdraw a request by marking it as solved. The request must be assigned to an agent before you can mark it as solved.

**To mark a request as solved**

1. Click your profile icon in the upper-right side of any page and then click **Requests**.
2. Click the title of an open request to open it.
3. Select the option on the lower side of the request to mark it as solved.

   The request must be assigned to an agent. Otherwise, you do not have the option to mark it as solved.
4. Enter any comment you want in the reply and click **Add Reply**.

## Creating a follow-up to a solved request

You can reopen a solved request by creating a follow-up ticket.

**To create a follow-up to a solved request**

1. Click your profile icon in the upper-right side of any page and then click **Requests**.Click **All my requests** in the sidebar.
2. Click the title of a solved request to open it.

   Tip: If you have a long list of requests, you can filter the view by selecting Solved from the Status menu.
3. Click the link on the lower side of the request to create a follow-up request.
4. Complete the follow-up request and click **Submit**.

## Submitting CSAT for your ticket

If CSAT is on, you can submit your customer satisfaction rating and feedback for a solved ticket. By default, the CSAT survey is open for 28 days after the ticket is solved, but this might vary depending on how CSAT is configured. Alternatively, you can submit CSAT through the email, if you received one.

**To submit CSAT for a ticket**

1. Click your profile icon on the upper-right of any help center page, then click **Requests**.
2. Open any solved ticket.
3. Click **Add feedback** to open the CSAT survey, then enter and submit your feedback. Once submitted, you can click **Edit feedback** in the ticket if you want to change your feedback. Depending on how much time has passed, you might not be able to edit your feedback. In that case, you can click **View feedback** to review your feedback for the ticket.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/guide-review-csat-feedback-2024.png)

## Accessing the service catalog and submitting service requests

If a service catalog has been published, the service catalog is populated with services and assets users commonly need. For example, an employee might submit a request for an asset from their IT department.

You can access the service catalog and submit requests, as described in these sections:

- [Access the service catalog](#topic_v2c_gfk_cgc)
- [Submitting a service request](#topic_y2c_gfk_cgc)

To submit a support request, instead of a service request, see [Submitting support requests](#topic_hgd_mqd_yy).

### Accessing the service catalog

You can access and view the service catalog in help center.

**To access the service catalog**

- In the help center, click **Services** in the navigation bar at the top of any page.

 ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/guide-serv-cat-search-field.png)

### Submitting a service request

You can submit service requests using the service catalog in the help center. When you submit a service request, a ticket is automatically generated with the unique combination of ticket fields, and agents assigned to the ticket can work to resolve it.

For the fastest resolution, complete as many of the fields as possible.

**To request a service in the service catalog**

1. In the help center, click **Services** in the navigation bar at the top of any page.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/guide-serv-cat-search-field.png)
2. Select the service or asset you're requesting.

   Optionally, you can use the search bar to find the service more quickly.
3. Enter the requested details about your service request in the available fields.
   Required fields are indicated by an asterisk (\*).

   The more fields you complete, the easier it is for internal support specialists to resolve your request.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/guide-serv-cat-request-page-submit.png)
4. Click **Submit request**.

   A ticket is automatically created and can be [tracked](#topic_qgd_mqd_yy) with your other requests.