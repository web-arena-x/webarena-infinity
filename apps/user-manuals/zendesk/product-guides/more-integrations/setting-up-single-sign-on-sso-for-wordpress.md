# Setting up single sign-on (SSO) for WordPress

Source: https://support.zendesk.com/hc/en-us/articles/4408886723994-Setting-up-single-sign-on-SSO-for-WordPress

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

By setting up single sign-on (SSO) for the Zendesk Support for WordPress plugin, your WordPress site users can access Zendesk Support using their WordPress user ID and password. They access Zendesk Support at the usual URL (http://*mycompany*.zendesk.com), but logging in happens through the WordPress login page, which is displayed when they click the login link in Zendesk Support. When they are successfully authenticated by WordPress, they are seamlessly logged in.

Note: This integration requires access to the default Wordpress login mechanisms (WP-LOGIN.php) to work correctly. If any custom code or third-party plugins (Woocommerce, Theme My Login) has been implemented into Wordpress that interferes with this process, we can't guarantee that it will work as expected, and is not supported.

Once you've set up single sign-on, all user management and authentication happens in WordPress.

If you switch to SSO after you've already set up users in Zendesk Support, they will no longer have access to those user accounts (their old login). You can however make sure that their former identity is associated with their WordPress user account, by using the same email address in both user accounts. In other words, if a user's WordPress account uses the same email address as in Zendesk Support, the two accounts will be synced. If a different address is used, a separate user account is created.

**To configure single sign-on for the Zendesk Support for WordPress plugin**

This process is a back and forth between your WordPress site and Zendesk Support.
Sign in to both as an administrator.

Note: You need to have already installed the Zendesk Support for WordPress plugin.
For more information about setting up and using the Zendesk Support for WordPress plugin, see [Setting up and using the Zendesk for WordPress plugin](https://support.zendesk.com/hc/en-us/articles/4408886694810).

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4408838272410), click the **Account** icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_account_icon.png))
   in the sidebar, then select **Security > Single sign-on**.

   Note: You must enable Help Center to set up single sign-on for WordPress. See [Enabling Help Center in setup mode](https://support.zendesk.com/hc/en-us/articles/4408846795674-Getting-started-with-Guide-Setting-up#topic_ndf_fpf_mk).
2. Select the **JSON Web Token** strategy.
3. In WordPress, select **Remote Auth** from the Zendesk panel.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/wp_zendesk_panel.png)
4. Select and copy the **Remote Login URL**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/wp_remote_url.png)
5. Back in the JSON Web Token options you opened in Zendesk Support, copy the URL into the **Remote Login URL** input box.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/wp_sso_jwt_options.png)
6. If you want your users to return to your WordPress site after logging out, copy the **Remote Logout URL** in WordPress and paste it into the **Remote Logout URL** in Zendesk Support.
7. In Wordpress, under **General Settings**, select **JSON Web Token** from the **Remote Auth Strategy** drop-down list.
8. In Zendesk Support, turn on the **Update of external ids?** option.
9. In Zendesk Support, select and copy your **Shared secret** token.

   Note: It's a long number and may exceed the length of the text control that it's displayed in so double-click the number to make sure you've selected it all.
10. In Zendesk Support, click **Save**. You've finished the Zendesk Support part of this set up.
11. In Wordpress, copy the shared secret into **Remote Auth Shared Token**.
12. Click **Save Changes**.

Now all users, including yourself, will be authenticated through your WordPress site when logging in.

Note: If you, as an administrator, need to sign in to Zendesk Support with your user account, you can do so at the following URL:
http://*mycompany*.zendesk.com/access/normal.