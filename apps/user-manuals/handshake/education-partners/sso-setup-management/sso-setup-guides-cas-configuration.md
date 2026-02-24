# SSO Setup Guides: CAS Configuration

Source: https://support.joinhandshake.com/hc/en-us/articles/360012361773-SSO-Setup-Guides-CAS-Configuration

---

# Step 1. Setup Handshake on your CAS Server

Handshake uses the following URLs, please add both of them in your local CAS settings:

```
app.joinhandshake.com/
yourschooldomain.joinhandshake.com/
```

***`NOTE: yourschooldomain` should be substituted with your school's sub-domain, this is normally the first part of your email (i.e. mtu if your email is mtu.edu)***

**\*\*\*Depending on how you have CAS configured, it may be required to add in https:// to Handshake's URLs to successfully authorize them on your end. If you receive an '*application not authorized to use CAS*' error, please try adjusting your URLs to include https:// to resolve this issue.**

# Step 2: Login to Handshake to Setup SSO

Setting SSO up on Handshake is self-service! After your career services admin has added you to Handshake you can begin [SSO Setup and Testing](sso-setup-guides-in-app-setup-and-testing.md).

# More Questions?

See our [Frequently Asked Questions](https://documentation.joinhandshake.com/docs/frequently-asked-questions) or reach out to our [support](https://support.joinhandshake.com/hc/en-us/requests/new).