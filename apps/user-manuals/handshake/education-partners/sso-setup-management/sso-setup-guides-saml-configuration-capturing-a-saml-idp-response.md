# SSO Setup Guides: SAML Configuration: Capturing a SAML IdP Response

Source: https://support.joinhandshake.com/hc/en-us/articles/360012405073-SSO-Setup-Guides-SAML-Configuration-Capturing-a-SAML-IdP-Response

---

If you receive an error and are unsure how to proceed, capturing the SAML IdP response can help decipher the problem. This will only be covered in Google Chrome but can also be done in other browsers.

# 1. Go to your school’s Handshake login page and click the Single Sign On button

[![](https://files.readme.io/448ac76-Screen_Shot_2017-05-12_at_11.39.31_AM.png)](https://files.readme.io/448ac76-Screen_Shot_2017-05-12_at_11.39.31_AM.png)

# 2. Enable developer tools

You can reference the below guide if you are unsure!  
<https://developer.chrome.com/devtools>

You can also change the location of the panel by clicking the 3 dots on the far upper-right corner and then selecting the bottom layout

# 3. Select the Network tab

[![](https://files.readme.io/6877cdd-Screen_Shot_2017-05-12_at_11.41.34_AM.png)](https://files.readme.io/6877cdd-Screen_Shot_2017-05-12_at_11.41.34_AM.png)

# 4. Enable “Preserve log”

[![](https://files.readme.io/7111e2f-Screen_Shot_2017-05-12_at_11.42.45_AM.png)](https://files.readme.io/7111e2f-Screen_Shot_2017-05-12_at_11.42.45_AM.png)

# 5. Login using your credentials

The table will start to fill up and you will be taken back to the Handshake login page

[![](https://files.readme.io/b2f639d-Screen_Shot_2017-05-12_at_11.51.00_AM_-1_1.png)](https://files.readme.io/b2f639d-Screen_Shot_2017-05-12_at_11.51.00_AM_-1_1.png)

# 6. Click on the “saml\_consume” item

A new box will open on the right ( If you have dev tools on the bottom )

[![](https://files.readme.io/f72034b-Screen_Shot_2017-05-12_at_11.51.00_AM.png)](https://files.readme.io/f72034b-Screen_Shot_2017-05-12_at_11.51.00_AM.png)

# 7. Scroll down to the “Form Data” section

Copy the entire “SAMLResponse” This will generally end with “==” because it is base64 encoded, please ensure that you copy the entire response

[![](https://files.readme.io/d31d2c6-Screen_Shot_2017-05-12_at_11.51.30_AM.png)](https://files.readme.io/d31d2c6-Screen_Shot_2017-05-12_at_11.51.30_AM.png)

# 8. Decode

You can copy the SAMLResponse and decode it using an online base64 string decoder to get the response. When creating a ticket for SAML SSO support this can often be helpful.