# Integration: TouchNet

Source: https://support.joinhandshake.com/hc/en-us/articles/115009782928-Integration-TouchNet

---

TouchNet is a third-party Global Payments company that can be integrated into Handshake for payment processing. This article will provide the steps necessary to complete the integration. 

Topics: 

- [Getting Started](#h_01FYY6FH117AT00Q5NMV4FG328)
- [TouchNet Project Plan](#h_01FYY6G5ZPVX7GRQ2W2QNKWF1N)
- [Setup in Handshake](#h_01FYY9JWDS36E28KC2QYJX5FJ9)
- [Test your TouchNet integration](#h_01FYYA3W6YPJHE83G120BBYDC1)
- [FAQ's](#h_01FYYAQ0DR665FD1M2V3TXKKE8)

### Getting Started

*What are the first steps to get your TouchNet account setup in Handshake?* 

1. Contact your TouchNet administrator/account manager to start the integration process!
   - You can also reach out to touchnetready@touchnet.com if you don't know who your contact is.
2. TouchNet can provide you with the following information that you'll enter in Handshake:
   - uPay URL
   - Site ID

### TouchNet Project Plan

Once connected with TouchNet to integrate their service into Handshake, the below actions occur before setup: 

- Institutions are required to sign an addendum.
  - Fees vary based on other projects that they have.
- A request is submitted to the legal team and the addendum is sent for signature.
  - The timeline varies widely, from school to school.

TouchNet will then coordinate the following with your institution:  

- A list of contacts for the project
- A timeline for the project
- A scheduled kick-off call with the contacts

Kick-off calls are usually 30 minutes long with the following information provided:

- - Action items for integration
  - URLs and items we know will apply
  - **Upay site ID** (which Handshake needs for integration)

### Setup in Handshake

To ensure payments are received, the **Touchnet admin** will need to ensure the following IP addresses are unblocked in Touchnet.

- - - Primary IP: 54.88.136.216
    - Secondary IP: 54.84.188.199

*To setup Touchnet in Handshake, one must have the Manage Payment Preferences role at your institution. To find out which users have this access at your institution, navigate to School Settings > Staff Management, then filter on the role "Manage Payment Preferences". Alternatively, you can contact the Handshake administrator at your campus.*

1. Click your name in the upper-right corner of the screen, then click School Settings. 

2. Click **Payment Preferences** from the menu on the left of the page, then click the **Touchnet** tab.

3. Enter the details provided by TouchNet on the tracking guide. This includes the uPay URL, uPay Site ID, and the T-Link URL.

**Note**: the below screenshot is an example — in the T-Link URL, the word TEST shouldn't be present. If it is present, then the link won't work and payment attempts will fail. 

![](https://support.joinhandshake.com/hc/article_attachments/25991250130199)

If you have multiple career centers in Handshake you can set up the uPay URL and Site per career center. We'll use the default that you set if you don't add them individually.

![](https://support.joinhandshake.com/hc/article_attachments/25991264351639)

### Test your TouchNet Integration

1. Create a test Career Fair, or use an existing one in Handshake, and select **Credit Card** under *Employer payment methods* in the Career Fair settings.

2. In that fair, create a test registration for your On-Campus Employer account:

- Select **Credit Card**as the *Payment Method* in the registration
- Save and Approve the registration
  - *Create an invoice if you like, but do not mark the registration as paid.*

3. Test a Payment:

- While viewing from your on-campus employer account, open the registration and click **Pay Now** on the left side of the page.
  - **Note**: the registration *must* be marked as Unpaid or Invoiced
- Enter the credit card information and make a payment. Typically, the amount must be at least $1.

4. Verify Payment Status in the Registration:

- Open the registration and navigate to Payment History where you confirm the charge
  - If there isn't a charge, double-check the integration credentials in your **Payment Preferences** and contact our Support team for assistance.

### FAQs

- **Is Handshake a TouchNet Ready partner?**
  - Yes! Handshake is a TouchNet Ready partner and we can provide documentation upon request.
- **Is the application hosted on your servers or hosted on campus?**
  - The Handshake application is hosted on Amazon cloud servers. 
    - Primary IP: 54.88.136.216
    - Secondary IP: 54.84.188.199
- **Does the application pass the: Success/Cancel/Error URLs or do they need to configure this in UPay application on the TouchNet side?**
  - Yes, the Handshake application passes these three URLs.
- **Should the IP addresses listed be unblocked on our campus servers or the TouchNet servers?**
  - These should be unblocked on TouchNet servers.
- **Are there additional parameters that are being passed in a payments call?**
  - Yes, we pass the following information to TouchNet when a payment is created. You'll want to work with TouchNet to have these exposed in your TouchNet instance:
    - **user\_name**
      - The name on the Handshake account of the person making the payment.
    - **user\_id**
      - This is the employer user’s Handshake account ID.
    - **user\_institution\_id**
      - This is the employer company profile’s Handshake ID.
    - **user\_institution\_name**
      - This is the name of the employer Company.
    - **chargeable\_id**
      - This is an ID for the object being charged, it will be the registration ID in Handshake for employers paying for a Career Fair registration.
    - **chargeable\_type**
      - This will be the type of object being charged for, i.e. “Registration”.
    - **charge\_name**
      - This will be a description of the Employer and Event the charge is for.
    - **charging\_institution\_id**
      - This will be your institution’s account ID on Handshake.
    - **charging\_institution\_name**
      - Your institution’s name on Handshake.
    - **charge\_event\_name**
      - The name of the event, i.e. the Career Fair name.
    - **charging\_career\_center\_name**
      - The Career Center associated with the event on Handshake.
    - **charging\_career\_center\_id**
      - Handshake ID number of that same Career Center.
- **What fields are sent to TouchNet from Handshake?**   
  - Event ID or Fair ID or Interview Schedule ID
  - Event Name or Fair Name or Interview Name
  - Employer ID (if employer payment) or User ID (if student payment)
  - Employer Name
  - Career Center Name
  - Career Center ID