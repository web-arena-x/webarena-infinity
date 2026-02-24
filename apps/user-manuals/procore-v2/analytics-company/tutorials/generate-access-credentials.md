# Generate Access Credentials

Source: https://v2.support.procore.com/product-manuals/analytics-company/tutorials/generate-access-credentials

---

To start accessing your Procore data, there are two options for generating your data access credentials: the Databricks direct connection method or the Delta Share Token method. The access token is a string of digits you will enter in your applicable data connector to access data.

## Considerations

- You must have the Analytics tool enabled at the Company level for your company's Procore account.
- By default, all Company Admins have 'Admin' level access to Analytics in the Directory.
- Anyone with 'Admin' level access to the Analytics tool can grant additional users access to the Analytics tool.
- Users must have 'Admin' level access to the Analytics tool to generate an access token.

## Steps

1. Log in to Procore.
2. Click the **Account & Profile** icon in the top-right area of the navigation bar.
3. Click **My Profile Settings**.
4. Under **Choose Your Connection with Analytics**, you have two options to generate credentials:

   - Databricks direct connect OR generate a personal access token with Delta Share.
5. Enter your **Databricks Sharing Identifier** for the Databricks direct connection method, then click **Connect**. See [Connect Your Procore Data to a Databricks Workspace](/process-guides/getting-started-with-analytics/connect-to-databricks) to learn more.
6. For the token method, select **Delta Share Token**.
7. Make sure to choose an expiration date.
8. Click **Generate Tokens**.

   - **Important!** It's recommended that you copy and store your token for future reference since Procore does not store tokens for users.
9. You will use your Bearer Token, Share Name, Delta sharing server URL, and your Share Credentials Version to begin accessing and integrating your data.
10. Explore the additional sections of the Getting Started Guide for next steps on connecting your data based on your desired data connection method.

##### Â Note

- The token will disappear after one hour or it will also disappear if you navigate away from the page. To generate a new token, return to Step 1.
- It may take up to 24 hours for the data to become visible.
- Please do not regenerate your token during this processing time as doing so may cause issues with your token.