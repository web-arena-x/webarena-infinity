# Setting Up Automated Source Codes for Handshake

Source: https://support.joinhandshake.com/hc/en-us/articles/27540400245271-Setting-Up-Automated-Source-Codes-for-Handshake

---

Setting up automated source codes ensures that Handshake is consistently tracked as the candidate source in your Applicant Tracking System (ATS).

Follow the steps below to configure your ATS to automatically recognize Handshake as a source, so every candidate from Handshake is reliably captured in your system.

*Premium features are for Handshake Premium accounts only. For more information, please check out this* [*resource*](https://www.joinhandshake.com/employers-premium/). 

### Set up automated source codes

#### **Step 1: Identify the source parameter in your ATS**

Before setting up automated source codes, identify which parameter your ATS uses to track candidate sources. Common parameter names include:

- utm\_source
- source
- ref
- tracking\_source

To locate the parameter:

1. Log into your ATS.
2. Navigate to the settings or integrations section where candidate sources are configured.
3. Confirm the parameter your ATS uses to track sources.

After identifying the parameter, confirm that it matches one of Handshake’s supported parameters:

- gh\_src
- iisn
- iis
- src
- source
- ref
- utm\_medium
- referral
- utm\_source
- \_jvst
- \_jvsd
- sourceDetails
- trid
- lever-source%5B%5D
- Source
- rb
- jobBoardSource
- channel
- rcid

**Note**: If your ATS uses a parameter not supported by Handshake, please note that an automated solution is currently unavailable. In this case, you will need to manually add source tracking to your job URLs when posting jobs. For additional guidance, please refer to your ATS documentation or contact your integration’s support team.

### 

#### Step 2: Register "Handshake" as a candidate source in your ATS

Now, configure "Handshake" as a candidate source in your ATS:

1. Access the ATS settings where global candidate sources are configured.
2. Add "Handshake" as a new source, using the parameter name identified in Step 1. For example, if your ATS uses utm\_source, enter "Handshake" as the value for utm\_source.

**Note**: Ensure "Handshake" is entered exactly as shown. If your ATS alters it into a different string or characters, it may not function correctly.

### 

#### Step 3: Test the source configuration

After setting up "Handshake" as a source, it’s important to test the configuration to ensure it works.

You can do this yourself by:

1. Create a test job URL that includes the source parameter, e.g., www.yourcompanyname.com/job/123445/product-manager?source=Handshake.
2. Submit a test application through this link.
3. Check your ATS to confirm that the candidate's source is listed as "Handshake."

If everything appears to be correct, proceed to the next step. If not, revisit the configuration or consult your ATS support.

### 

#### Step 4: Request activation of source code automation

After completing steps 1–3, contact Support to request activation of source code automation. Handshake will then automatically add the correct source parameter and code to your job URLs.

This ensures you won’t need to manually include the source when posting jobs on Handshake—just ensure that no one on your team removes the "Handshake" source setting configured in Step 2.