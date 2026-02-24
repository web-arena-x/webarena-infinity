# SAML: Updating Your X509 Certificate

Source: https://support.joinhandshake.com/hc/en-us/articles/360057932994-SAML-Updating-Your-X509-Certificate

---

For security reasons, your institution's authentication server may require your public certificate to be updated on a scheduled basis. If you've been notified of an upcoming certificate change, you can update this within Handshake to prevent a lapse in SSO access for your students. 
 
1. Click on your name in the upper-right corner of Handshake, then click on **School Settings**.

![School_Settings_button.png](https://support.joinhandshake.com/hc/article_attachments/13639147252119)

2. From the menu on the left of the page, click on **SSO Preferences**.

![SSO_Preferences_from_School_Settings.png](https://support.joinhandshake.com/hc/article_attachments/25991250506263) 
 
3. From this page, copy/paste a SHA-1 or SHA-256 hash of your updated X509/public cert into the **Fingerprint** text field. To save these changes, click **Update SSO Preferences**.

![mceclip0.png](https://support.joinhandshake.com/hc/article_attachments/25991250504343)

**Note**: Currently we only support SHA-1 and SHA-256 encryption, if your school uses a different form of encryption, please reach out to Support to discuss the best way to move forward: [Contacting Support](https://support.joinhandshake.com/hc/en-us/articles/28656432275863).