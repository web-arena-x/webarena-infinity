# WeChat (Engage Legacy)

Source: https://support.zendesk.com/hc/en-us/articles/9731476677786-WeChat-Engage-Legacy

---

## About WeChat

WeChat is China's most popular messaging app with a monthly user base of more than 1 billion people.

### What kind of WeChat account does a client need to talk to their customers?

You will need to have a **verified** **WeChat** **Service Account** to use the Engage WeChat integration**.** If you do not currently have this type of account, you will need to apply for one (See **Setup an Official WeChat Service Account** below).

### What does the Engage WeChat integration support?

- One-to-one messaging
- Incoming image attachments
- GIFs
- Emojis

Features not supported:

- Stickers
- Location sharing
- Contact sharing
- Voice input
- Videos

## Setup an Official WeChat Service Account

**Please note that WeChat webpages are displayed in Mandarin, we recommend using a browser-based translator to help guide you through the process. We recommend the** [**Google Translate browser extension for Chrome.**](http://translate/aapbdbdomjkkjkaonfhkkikfgjllcleb/RK%3D2/RS%3DBBFW_pnWkPY0xPMYsAZI5xOgQEE-)

- Go to <https://mp.weixin.qq.com/?lang=en_US&token=>
- Click on '[Register Now](https://mp.weixin.qq.com/cgi-bin/registermidpage?action=index&lang=en_US&token=)'
- There are four types of accounts - you will need to set-up a Service Account in order to use this with Engage for Amazon Connect.

![__wf_reserved_inherit](https://support.zendesk.com/hc/article_attachments/9731476684698)

- Once you’ve created your account, you will need to go through the account verification process.
- To review this process, in your WeChat Dashboard navigate down to 'Settings' and click on 'WeChat Verification'.
- For more information on verification, view the [Tencent Verification Guide](https://kf.qq.com/product/weixinmp.html#hid=97).

## Configure your WeChat Account

Once the account has been verified, you will need to complete the following steps to configure your WeChat account for use with Engage for Amazon Connect.

- In the WeChat Dashboard, navigate to 'Developer' then click on 'Basic Configuration'.
- The dashboard will instruct you to turn on 2FA (WeChat Protect). Follow the steps to set this up.

- You will need to go to IP Whitelist and add these two IP addresses to the text box:
- If your instance is in AU-Sydney region, enter these IP addresses:   
  52.63.123.104 13.54.69.253 54.153.142.150
- If your instance is in EU-London region, enter these IP addresses:   
  18.168.27.72 18.134.77.8 35.178.165.248
- If your instance is in US region, enter these IP addresses:   
  3.86.171.108 54.158.103.106 54.166.29.108

- Under Server Configuration, add the Local Measure server URL:   
  <https://webhook-proxy.getlocalmeasure.com/wechat>
- Under Token, add the token:   
  **WidgetsRUs**
- Under Message encryption and decryption key, add the key: **lpcKK6P5PIa5IcnxOxgGcYdHtmiGOrLUaoGPrXetUG3**
- Under Message encryption and decryption, click 'Plaintext Mode'.
- Click 'Save'.
- Click 'Enable' in the server configuration settings.

## Adding WeChat to Engage

You will need the following details in order to add WeChat to Engage:

- Developer ID
- Developer Password
- Original ID

To obtain these details:

- In the WeChat Dashboard, navigate to 'Developer' then click on 'Basic Configuration'.
- Under 'Public Account Development Information', you can obtain a new **Developer ID** (App ID) if you don't already have one. Please record these details so they can be added to Engage.
- Under 'Public Account Development Information', you can generate a new **Developer Password** (App Secret) if you have not already set one up. Please record these details so they can be added to Engage.
- To obtain your **Original ID,** click on the account icon in the top right hand corner and select 'Account Details'. Scroll down to 'Registration Message' to find your Original ID. Please record these details so they can be added to Engage.

Now you are ready to add the WeChat account to Engage.

- Click 'Add New'.
- You will be presented with the following modal where you will need to input:
- Account Name (this is can be the same name as your WeChat account)
- Developer ID
- Original ID
- Developer Password - This information can be [found in your WeChat account](https://www.notion.so/WeChat-0eb414a27f19467e83b230981a248242)

![](https://support.zendesk.com/hc/article_attachments/9731476699290)

- Click **Save.**
- Your WeChat account will be listed under Accounts.

Once added, your WeChat account will be integrated with Engage for Amazon Connect.

Don't forget to reverify your account every 12 months to keep your integration active.