# Providing agents with more information using the Iframe app

Source: https://support.zendesk.com/hc/en-us/articles/4408894151962-Providing-agents-with-more-information-using-the-Iframe-app

---

The Iframe app lets agents access additional information from the Zendesk agent interface. This article describes the app and how to install it.

## Using the Iframe app

An *iframe* is an HTML element that lets you nest one web page in another web page. The Iframe app is designed to let Zendesk agents quickly flip to a web page in the agent interface and then flip back to their tickets without interrupting their workflow. This can be especially useful if agents use a page to look up things like orders or other data.

You can embed a lot of different web pages in the Zendesk agent interface with the Iframe app. However, not all pages will be displayed properly and some might be displayed but then exhibit strange behavior. A rule of thumb is to choose web pages that are very simple.

Also, some sites actively prevent other web sites from loading their content in this way. They do this for security reasons so hackers can't pretend to be those companies. When this happens, you’ll see the Iframe app but there won’t be any content when you click it.

**Important**: The latest versions of Firefox or Chrome browsers may block web pages from being loaded into Zendesk. To view the pages, agents must click the shield icon in the browser's Address bar and agree to load an unsafe script (Chrome) or to disable protection on the page (Firefox).

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/zat_chrome_script.png)

**To install the Iframe app**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_apps_integrations_icon.png) **Apps and integrations** in the sidebar, then select **Apps > Channel apps**.
2. Click **Zendesk Marketplace** and search for "Iframe."
3. Click the **Iframe** app icon.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sidebar_icon_app.png)
4. Click **Install App** in the upper right of the page.
5. Configure the app:
   - **Iframe URL:** Required. Put the link to the page you want to display when agents click on the Iframe app.
   - **Inactive Icon URL**: An image to be displayed when you're not interacting with the app. Pick something that contrasts with the grey color of the Zendesk panel for visibility.
   - **Hover Icon URL**: An image to be swapped in when an agent hovers the mouse over the image but hasn’t clicked or done anything yet.
   - **Selected Icon URL**: An image to be displayed when an agent has clicked on and activated the Iframe app.
   - **Title**: Required. A title differentiating the app from other apps.
6. Click **Install**.

**Examples**

Is your business X (formerly Twitter) focused? You can embed X’s status page into your Zendesk. Here are the Iframe app settings for the X status page.

- Title: X Status
- Iframe URL: https://api.twitterstat.us
- Inactive Icon URL: https://twitter.com/images/resources/twitter-bird-light-bgs.png
- Hover Icon URL: https://twitter.com/images/resources/twitter-bird-dark-bgs.png
- Selected Icon URL: https://twitter.com/images/resources/twitter-bird-light-bgs.png

Make sure your agents know how to set their browser to allow the page to load. See the note in the introduction for more information.

Here are other examples of web pages that can be loaded into the Iframe app:

- Twilio status: <http://status.twilio.com/>
- Salesforce.com status: <http://trust.salesforce.com/trust/status/>
- Google App Engine: <http://code.google.com/status/appengine>
- Skype: <http://heartbeat.skype.com>
- Google Analytics: <http://www.google.com/analytics/status#hl=en>