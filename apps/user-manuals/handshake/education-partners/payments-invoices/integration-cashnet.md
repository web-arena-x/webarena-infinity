# Integration: CASHNet

Source: https://support.joinhandshake.com/hc/en-us/articles/115009783288-Integration-CASHNet

---

**Handshake currently supports a CASHNet Checkout integration.**

## **Handshake Setup**

1. Owner of the school visits the School Settings
2. Click **Payment Preferences**
3. Enter details provided by CASHNet

1. Site URL: CASHNet site URL
2. Site: Merchant ID / Site Name
3. Item: Item Code
4. Whitelisted CashNet ip address: provided by CASHNet (if you receive multiple addresses, you can enter both of them in this box, separated by a comma)

![](https://support.joinhandshake.com/hc/article_attachments/25997610986647)

![](https://support.joinhandshake.com/hc/article_attachments/25997597328535)

**Multiple Item Codes per Career Center**

If you are interested in using different item codes for each career center in Handshake please add the item code for each career center to the Item Code section in the Payment Preferences.

![](https://support.joinhandshake.com/hc/article_attachments/25997597332631)

[What is a career center in Handshake?](https://support.joinhandshake.com/hc/en-us/articles/222083428)

## **CashNet Setup**

1. Setup notifications in CASHNet to send HTTP notifications when transactions succeed or fail
   1. <https://app.joinhandshake.com/omniauth_callbacks/cashnet_webhook_callback>
   2. ![](https://support.joinhandshake.com/hc/article_attachments/25997610983575)
2. Create Reference Type "SESSIONID"
3. Add Reference Type to Item Code
4. Make sure that CASHNet has unblocked \*.joinhandshake.com and app.joinhandshake.com

## **FAQs**

- Can two career centers use the same item code?
  - Yes, you can use the same item code at multiple career centers or different ones at each.
- What fields are sent to CASHNet from Handshake?   
  - Event ID or Fair ID or Interview Schedule ID
  - Event Name or Fair Name or Interview Name
  - Employer ID (if employer payment) or User ID (if student payment)
  - Employer Name
  - Career Center Name
  - Career Center ID