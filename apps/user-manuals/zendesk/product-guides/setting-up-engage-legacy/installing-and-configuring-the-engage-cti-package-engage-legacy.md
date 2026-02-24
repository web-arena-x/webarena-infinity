# Installing and Configuring the Engage CTI package (Engage Legacy)

Source: https://support.zendesk.com/hc/en-us/articles/9731463294362-Installing-and-Configuring-the-Engage-CTI-package-Engage-Legacy

---

Overview of high-level steps to install the CTI package:

1. Install the Salesforce Package
2. Get the VisualForce page URL
3. Configure the Call Center Settings
4. Configure Approved Origins in Engage Settings and Connect
5. Add the Softphone Utility to the Lightning Console App
6. Add users to the Call Center
7. Permission sets

## Install the Salesforce Package

Visit this link and follow the prompts: [Engage CTI](https://appexchange.salesforce.com/listingDetail?listingId=a0N4V00000Hhh1bUAB)

**Choose the appropriate permissions - Recommended: Choose Specific Profiles**

Then apply the EngageCTI Agent option to the Profiles your agents will use.

![](https://support.zendesk.com/hc/article_attachments/9731467036442)

If you don't do this at install time, or want to add roles to extra users later, there is a Permission Set included with the package. See more info below.

## Get VisualForce page URL

Find the VisualForce Pages sections by searching in the Quick Search in Setup.

![](https://support.zendesk.com/hc/article_attachments/9731499905178)

Click on the LMVisualForcePage.

![](https://support.zendesk.com/hc/article_attachments/9731439074330)

Then click Preview.

![](https://support.zendesk.com/hc/article_attachments/9731499927066)

This will open in a new window. You need to copy the URL.

Save this URL because you will need it in the following step.

![](https://support.zendesk.com/hc/article_attachments/9731499938842)

## Configure Call Center Settings

You can find the Call Center Settings by searching in the Quick Search in Setup.

![](https://support.zendesk.com/hc/article_attachments/9731439115290)

The package installs **"Local Measure Engage CTI Adapter"** (Display name) - "lmCallCenter" (Internal name).

![](https://support.zendesk.com/hc/article_attachments/9731450591130)

View the call center and click Edit.

![](https://support.zendesk.com/hc/article_attachments/9731439132186)

- Set CTI Adaptor URL to the URL you got from step 2.
- Set the Engage URL to the region-specific URL for your Engage Instance (new pattern with workspace name as a subdomain) - eg. <https://demo.syd.localmeasure.com>
- Set the Merchant Name to your workspace name - eg. “demo” is workspace name in  <https://demo.syd.localmeasure.com>

![](https://support.zendesk.com/hc/article_attachments/9731439141402)

## Configure Approved Origins in Engage Settings and Connect

You will need to add two URLs to the Approved Origins in Engage Settings and Connect

- Salesforce organisation URL. The URL after you log in to SalesForce. It is in the browser address bar. (eg. [localmeasure2-dev-ed.lightning.force.com](http://localmeasure2-dev-ed.lightning.force.com/))

![](https://support.zendesk.com/hc/article_attachments/9731467146906)

- VisualForce Page URL (see step 2).

‍

### Adding to Engage Settings

Log in to Engage, under “Settings > General Settings > Local Measure Connection”, click on Edit Approved Origins, and add the above URLs.

![](https://support.zendesk.com/hc/article_attachments/9731500013210)

Your Engage user must be assigned to “LM-Admin” group to see the Engage Settings. To add your user to this group, go to “AWS Console > Cognito” and select the User pool for Engage instance. Under the User tab, select the user and add it to LM-Admin group. Then refresh the Engage page.

![](https://support.zendesk.com/hc/article_attachments/9731450642458)

### Add Approved Origins in AWS Connect Console

Follow the instructions [here](https://docs.aws.amazon.com/connect/latest/adminguide/app-integration.html) to add Approved Origins to Amazon Connect.

![](https://support.zendesk.com/hc/article_attachments/9731476031514)

## Add the Softphone Utility to the Lightning Console App

The Open CTI Softphone can be added to any Lightning Console App.

Go to App Manager in Setup.

![](https://support.zendesk.com/hc/article_attachments/9731439205530)

Select the App you want to update and choose Edit.

![](https://support.zendesk.com/hc/article_attachments/9731463512090)

In Utility Items, choose **Add Utility Item** then **Open CTI Softphone.**

![](https://support.zendesk.com/hc/article_attachments/9731467248026)

Update these fields - you can set them to what makes sense to you. The width and height in the screenshot below will give agents the smoothest experience.

![](https://support.zendesk.com/hc/article_attachments/9731500140186)

## Adding Call Center Users

We recommend you add one user first to test that everything is working. Before enabling more users.

Go to the Call Center Settings and click Manage Call Center Users.

![](https://support.zendesk.com/hc/article_attachments/9731463592858)

From here you can add or remove users.

![](https://support.zendesk.com/hc/article_attachments/9731463605786)

Any users added will be able to access the Utility Bar from the Lightning Console App you configured earlier.

![](https://support.zendesk.com/hc/article_attachments/9731500238746)

You can also add or update the Call Center from the individual User Settings.

![](https://support.zendesk.com/hc/article_attachments/9731467395610)

## Permission Sets - adding necessary access level after installation

During installation, admins can choose to apply permissions to specific profiles. If you want to change or add more users after installation, then you use Permission Sets.

In Setup, find Permission Sets and choose EngageCTI agent.

![](https://support.zendesk.com/hc/article_attachments/9731439445658)

You can then Manage Assignments to add assignment rules for users.

![](https://support.zendesk.com/hc/article_attachments/9731439477658)

For more info on Permission Sets refer to Salesforce Help: [Help and Training](https://help.salesforce.com/s/articleView?id=sf.perm_sets_overview.htm&type=5)