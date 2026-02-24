# Single Sign-On

Source: https://help.clio.com/hc/en-us/articles/41135505613339-Single-Sign-On

---

To streamline user authentication and/or to comply with security policies applicable to your firm you can integrate Clio with your Identity Provider (IdP).

## Set up SAML-based SSO

**Note:** Administrators can set up SAML-based Single Sign-On (SSO) for their firm’s Clio account.

#### Verify your domain(s)

1. Go to **Settings** > **Security & Compliance** > **Firm Security**.
2. Click **Update single sign-on**.
3. Click **Add domain**.
4. In the modal, type your domain, then click **Verify domain**.
5. Follow the set of instructions provided in Clio to verify domain ownership.

   **Tip:** You can ask your IT team to help you with these instructions. If you use a web hosting service, refer to their documentation about how to navigate to the DNS settings and where to input the relevant information.

   **Note:** Domain verification usually takes about 20 minutes, but may take as long as 72 hours. You can return to this page at any time to view the status of the verification. If you are unable to verify domain ownership, reach out to your DNS service provider or web hosting service if they provide DNS services as part of their hosting package.
6. Click **Done**.

#### Add configuration for your Identity Provider

**Note:** In addition to being a Clio administrator, you will need to be an administrator for your Identity Provider service to add the configuration. Or, you can work alongside an administrator for your Identity Provider to add the configuration.

Okta Azure Custom

1. Go to **Settings** > **Security & Compliance** > **Firm Security**.
2. Click **Update single sign-on**.
3. Click **Add configuration**.
4. Select Okta, then click **Create configuration**.  
   You will be provided with a step-by-step instruction set to guide you through this.
   1. **Step 1: Create the SAML integration:** The steps provided are to be completed in Okta’s administrator console. When you have completed these steps, click **Continue** in Clio to see the next instructions.
   2. **Step 2: Configure SAML attributes:** The steps provided are to be completed in Okta’s administrator console. When you have completed these steps, click **Continue** in Clio to see the next instructions.
   3. **Step 3: Add metadata URL to Clio:** In this step, you add information that you find in your Okta’s administrator console to Clio.
      1. You can use “Okta” for the **Configuration name**.
      2. Paste the Metadata URL found in Okta into the **Identity Provider metadata URL** field in Clio.
      3. Click **Continue** to see the next instructions.
   4. **Step 4: Assign users and groups:** The steps provided are to be completed in Okta’s administrator console. When you have completed these steps, click **Continue** in Clio to see the next instructions.
   5. **Step 5: Add and exclude domains and email:**
      1. Add domains and emails.

         1. Select **Email** or **Domain**, then type to search or use the down arrow to find and select the email or domain to add.
         2. Select the relevant email or domain to add to the list of added emails and domains.

         **Note:** If you choose **Domain**, but have not set up a domain yet, you can type the domain you want to set up, then click **Add “[your typed domain]”** to set up your domain. Then you can return to your configuration to finish setting it up.

         Repeat this until you are satisfied with your list of domains and/or emails.
      2. *Optional:* Add any applicable exceptions.

         1. Select **Email** or **Domain**, then type to search or use the down arrow to find and select the email or domain to exclude.
         2. Select the relevant email or domain to add to the list of excluded emails and domains.

         Repeat this until you are satisfied with your list of excluded domains and/or emails.
      3. Click **Continue**.
   6. **Step 6: Check configuration:** In the final page of this setup process, you can review your configuration. When satisfied with the configuration details, toggle the status toggle to **On** to enable the configuration. You can also set this configuration as the default SSO by checking **Set as default Single Sign-On**.

      **Note:** Your domain must be verified to enable the configuration.
5. Click **Save and exit**.

1. Go to **Settings** > **Security & Compliance** > **Firm Security**.
2. Click **Update single sign-on**.
3. Click **Add configuration**.
4. Select Azure, then click **Create configuration**.  
   You will be provided with a step-by-step instruction set to guide you through this.
   1. **Step 1: Create the SAML integration:** The steps provided are to be completed in Azure’s administrator console. When you have completed these steps, click **Continue** in Clio to see the next instructions.
   2. **Step 2: Configure SAML attributes:** The steps provided are to be completed in Azure’s administrator console. When you have completed these steps, click **Continue** in Clio to see the next instructions.
   3. **Step 3: Add metadata URL to Clio:** In this step, you add information that you find in your Azure’s administrator console to Clio.
      1. You can use “Azure” for the **Configuration name**.
      2. Paste the Metadata URL found in Azure into the **Identity Provider metadata URL** field in Clio.
      3. Click **Continue** to see the next instructions.
   4. **Step 4: Assign users and groups:** The steps provided are to be completed in Azure’s administrator console. When you have completed these steps, click **Continue** in Clio to see the next instructions.
   5. **Step 5: Add and exclude domains and email:**
      1. Add domains and emails.

         1. Select **Email** or **Domain**, then type to search or use the down arrow to find and select the email or domain to add.
         2. Select the relevant email or domain to add to the list of added emails and domains.

         **Note:** If you choose **Domain**, but have not set up a domain yet, you can type the domain you want to set up, then click **Add “[your typed domain]”** to set up your domain. Then you can return to your configuration to finish setting it up.

         Repeat this until you are satisfied with your list of domains and/or emails.
      2. *Optional:* Add any applicable exceptions.

         1. Select **Email** or **Domain**, then type to search or use the down arrow to find and select the email or domain to exclude.
         2. Select the relevant email or domain to add to the list of excluded emails and domains.

         Repeat this until you are satisfied with your list of excluded domains and/or emails.
      3. Click **Continue**.
   6. **Step 6: Check configuration:** In the final page of this setup process, you can review your configuration. When satisfied with the configuration details, toggle the status toggle to **On** to enable the configuration. You can also set this configuration as the default SSO by checking **Set as default Single Sign-On**.

      **Note:** Your domain must be verified to enable the configuration.
5. Click **Save and exit**.

If you use an identity provider other than Okta or Azure, you can use the custom configuration option to set up SSO. You will need to refer to your identity provider’s documentation to understand how to create the SAML integration and configure its attributes.

1. Go to **Settings** > **Security & Compliance** > **Firm Security**.
2. Click **Update single sign-on**.
3. Click **Add configuration**.
4. Select **Custom**, then click **Create configuration**.
   1. **Step 1: Create the SAML application:**
      1. Use the information provided on screen to create a SAML application with your Identity Provider and configure your attributes.

         **Note:** Refer to your Identity Provider’s documentation for instructions.
      2. Add a configuration name. You can use the name of your identity provider to easily identify your configuration.
      3. In your identity provider app, find the metadata URL and paste this information in the **Identity prover metadata URL** field in Clio.
      4. Click **Continue**.
   2. **Step 2: Add and exclude domains and email:**
      1. Add domains and emails.

         1. Select **Email** or **Domain**, then type to search or use the down arrow to find and select the email or domain to add.
         2. Select the relevant email or domain to add to the list of added emails and domains.

         **Note:** If you choose **Domain**, but have not set up a domain yet, you can type the domain you want to set up, then click **Add “[your typed domain]”** to set up your domain. Then you can return to your configuration to finish setting it up.

         Repeat this until you are satisfied with your list of domains and/or emails.
      2. *Optional:* Add any applicable exceptions.

         1. Select **Email** or **Domain**, then type to search or use the down arrow to find and select the email or domain to exclude.
         2. Select the relevant email or domain to add to the list of excluded emails and domains.

         Repeat this until you are satisfied with your list of excluded domains and/or emails.
      3. Click **Continue**.
   3. **Step 3: Check configuration:** In the final page of this setup process, you can review your configuration. When satisfied with the configuration details, toggle the status toggle to **On** to enable the configuration. You can also set this configuration as the default SSO by checking **Set as default Single Sign-On**.

      **Note:** Your domain must be verified to enable the configuration.
5. Click **Save and exit**.