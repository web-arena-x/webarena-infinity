# SSO Setup Guides: LDAP Configuration

Source: https://support.joinhandshake.com/hc/en-us/articles/360012362193-SSO-Setup-Guides-LDAP-Configuration

---

# Step 1: Login to Handshake to Setup LDAP

Setting SSO up on Handshake is self-service! After your career services admin has added you to Handshake you can begin the [SSO Setup and Testing](sso-setup-guides-in-app-setup-and-testing.md).

### **Contact support to have your team's LDAP server IP unblocked**

\*This step must be done before proceeding to test or logins will fail. At this time we only support a single Hostname (or IP) in your SSO Preferences, but can unblock all IP's associated with that host on the backend. You can contact our Support Team and ask to have your team's LDAP server IP(s) unblocked.

\*\*This process can take up to 5-7 days from time of request, so please submit this request as soon as you've confirmed your LDAP server host.

**Additional Notes:** -We can unblock multiple IP's on the backend if necessary, but these must align with the single "Host" value in your Handshake SSO Preferences (Screenshot below).

-If you have multiple IP's for your LDAP server, please provide a hostname that uses all of these, or narrow down your configuration to a **single IP**.

**LDAP Host Field Found in Your Handshake SSO Preferences:**

[![](https://files.readme.io/1f87c38-LDAP-host.png)](https://files.readme.io/1f87c38-LDAP-host.png)

### 

### You should also unblock both of Handshake's IPs on your end for this to align:

**54.88.136.216** **54.84.188.199**

# More Questions?

Refer to our [Frequently Asked Questions](https://documentation.joinhandshake.com/docs/frequently-asked-questions) or reach out to our Support.