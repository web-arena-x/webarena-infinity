# Set up eFiling for VAT in Xero

Source: https://central.xero.com/s/article/Set-up-eFiling-for-VAT-in-Xero

---

## Overview

- Before you set up eFiling, activate eFiling within SARS and connect Xero to our app partner CloudConvert.
- Set up eFiling in Xero to file VAT201 returns directly with the South African Revenue Service (SARS).

## How eFiling works

eFiling allows you to submit VAT201 returns to SARS directly from Xero. This filing process replaces other methods, including filing through SARS VAT online services.

Before you can use eFiling, you need to set up Xero as an Independent Software Vendor (ISV) in the SARS portal. This generates an ISV login name and key. You can use the same ISV login name and key to file returns from multiple Xero organisations.

To file a return from Xero, you need the advisor or standard + reports user role.

## Before you start

- Ensure you have a [SARS eFiling profile](https://secure.sarsefiling.co.za/app/login) (SARS website).
- Check the VAT details in your [financial settings](/s/article/Set-up-your-organisation-s-financial-details-SA) are correct.
- Set the [VAT201 return start date](The-VAT-201-return.md).
- Set up Xero as an ISV in SARS eFiling using the steps below.

## Set up Xero as an ISV in SARS

In order for Xero to submit VAT201 returns to SARS, you need to activate Xero as an ISV through SARS eFiling. To do this:

1. Log in to the [SARS eFiling portal](https://secure.sarsefiling.co.za/app/login) (SARS website).
2. Click **Organisations** at the top of the page.
3. On the left hand side, click **Organisation**, then select **ISV Activation**.
4. Next to **ISV Application**, select **Xero**.
5. Click **Activate**.

SARS generates a SARS ISV login name and SARS ISV login key, which you need to enter when you file a VAT201 return from Xero.

If you're authorised to submit a VAT201 return on behalf of another organisation, such as a client, you enter the same login name and login key for each Xero organisation.

Tip

If your access to the Xero organisation or your user configuration within SARS changes, you might need to set up Xero as an ISV again to generate a new ISV login name and login key.

## Set up eFiling in Xero

1. In the **Reporting** menu, select **All reports**.
2. Under **Tax**, click **VAT201 Report**.
3. Click **Settings**.
4. Select **VAT settings**, then review your financial settings, VAT201 return start date and customs code.
5. (Optional) To update any of the financial details, click **Edit in financial settings**, then make the changes.
6. Select **CloudConvert authorisation**, then click **Set up connection**.
7. Review the information on the screen, then click **Allow access**.
8. Select **Return details**, then complete the sections:
   - **The declarant** – Enter your personal information in this section. You need to enter at least one phone number.
   - **Voluntary Disclosure Programme (VDP)** – If you have a VDP agreement with SARS, select **YES**, then enter your **VDP application number**.
   - (Optional) **Tax practitioner** – If you’re an accountant or bookkeeper filing tax returns on behalf of a client, enter both your **Tax practitioner registration number** and **Tax practitioner telephone number**.
9. Click **Save**.

## What's next?

Once you've set up the connection with SARS, you can [file a VAT201 return from Xero](File-a-VAT201-return-with-SARS.md).