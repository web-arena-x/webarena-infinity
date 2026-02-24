# Adding a Contact Center admin user

Source: https://support.zendesk.com/hc/en-us/articles/9829255826074-Adding-a-Contact-Center-admin-user

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **Add-on** | Zendesk for Contact Center |

Verified AI summary ◀▼

To grant admin privileges in Contact Center, add users to the LMAdmin group in the Amazon Cognito user pool. This allows them to configure settings and access dashboards. For SSO users, ensure they sign in at least once before adding them. This setup enhances user management and access control within your contact center.

By default, newly created users are regular users. If a user has admin privileges in Contact Center (meaning they can configure Contact Center settings, view dashboards, and so on), they must be added to the LMAdmin user pool group that was created with the CloudFormation stack.

**To add a Contact Center admin user**

1. In the Amazon Cognito user pool, go to Groups. You'll see a group named LMAdmin.
2. Click the LMAdmin group and add your new user to the group.

.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/cc_gd_117.png)

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/cc_gd_118.png)

If you use SSO, the users available to add to this group are only created after they have successfully signed into Contact Center at least once. Once added, the user will gain access to the settings and dashboard pages in Contact Center.

Note: Connect provides the core contact center capabilities that Contact Center builds on.