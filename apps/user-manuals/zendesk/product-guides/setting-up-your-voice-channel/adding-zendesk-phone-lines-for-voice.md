# Adding Zendesk phone lines for voice

Source: https://support.zendesk.com/hc/en-us/articles/4408824192026-Adding-Zendesk-phone-lines-for-voice

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support with** | Talk Team, Professional, or Enterprise |

A Zendesk Suite trial comes complete with a phone number you can start using immediately. After the trial is over, you can buy more phone numbers from Zendesk. If you already have a support phone number, and want to keep using it, you can forward calls from your support number to the Zendesk phone number.

This article covers the following topics:

- [Adding a new line](#topic_lj3_2c5_gv)
- [Adding an external number for outbound calls](#topic_pmh_c5m_j1b)
- [Forwarding incoming calls from an existing number to Zendesk](#topic_tdk_gc5_gv)
- [Adding a local business address](#topic_mqn_mc5_gv)

Related articles:

- [Managing Zendesk phone lines](https://support.zendesk.com/hc/en-us/articles/4408881907994)
- [Adding a digital line](https://support.zendesk.com/hc/en-us/articles/1260805715389)
- [Adding a SIP-IN line](https://support.zendesk.com/hc/en-us/articles/8397091234586)

## Adding a new line

For a detailed list of numbers you can purchase, see [Zendesk phone number availability and pricing](https://support.zendesk.com/hc/en-us/articles/4408846483482). Some countries have specific regulatory requirements and you may be required to verify your business before you can purchase a number. For a full list of requirements see [Zendesk voice and text number regulatory requirements](https://support.zendesk.com/hc/en-us/articles/4408824253978). For more information about how to verify your business for Zendesk phone number purchasing see [Verifying your business for purchasing a Zendesk phone number](https://support.zendesk.com/hc/en-us/articles/4408826639386).

If you have an existing telephone number that you use for support calls, you can forward these calls to your Zendesk phone number. If you have a United States (US) based number, you can port the number to Twilio to use as your Zendesk phone number. For details, see [Porting numbers into Zendesk.](https://support.zendesk.com/hc/en-us/articles/4408834776858-Porting-numbers-into-Zendesk-Voice)

**To add a new line**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_channels_icon.png)
   **Channels** in the sidebar, then select **Talk and email > Talk**.
2. Click the **Lines** tab.
3. Click **Add line > Purchase a new number**.

   ![](http://zen-marketing-documentation.s3.amazonaws.com/docs/en/voice_newnumber.png)
4. Choose a country, and select the number type for example, local or toll free. A list of available numbers is displayed.

   One or more of the following icons appear next to each number to show whether the number is voice, text, or MMS compatible.

   ![](http://zen-marketing-documentation.s3.amazonaws.com/docs/en/Talk_capability_icons.png)
5. If you'd like to refine your list of options, you can search for phone numbers or vanity numbers search for phone numbers or vanity numbers containing specific sequences of letters or numbers.
6. Select a phone number and then click **Next**.

   The phone number is free during a trial, but you cannot change your number during a trial.
7. Review the number you selected and the monthly deduction amount, then click **Next**.
8. If the number requires an approved business verification, select the correct business verification and address, then click **Next**.

   Note: If you don't have an approved business verification for the country and number type, you won't be able to continue purchasing a number. For more information about how to verify your business when purchasing a Zendesk phone number, see [Verifying your business for Zendesk phone number purchasing](https://support.zendesk.com/hc/en-us/articles/4408826639386).
9. Some countries might not require you to have an approved business verification but you might be required to enter a business address. Enter your business address, then click **Next**.
10. Click **Finish**.

    You can now start making and receiving calls with your chosen number.

### About searching for a number

When you add a line, you can search for phone numbers containing specific sequences of letters or numbers. How you search for a phone number depends on whether you are in the US or Canada, or in a country outside of North America.

- **In the US and Canada**: You can enter a specific number combination in your search. For example, searching for 123 will return phone numbers that contain this sequence anywhere in the number, such as 123XXXX, XXXX123, or XX123XX.
- **Outside of North America**: When you search for a specific number combination, the default is to search for a number that starts with that specific number sequence. For example, searching for 123 will only return numbers that start with 123, such as 123XXXX. This is by design to assist you in searching for a number in a specific region or city where your business is located, as is often mandated by local telecom regulators.

 As a workaround to extend your search, you can use the asterisk (\*) as a wildcard character. This will return results that have your number combination match any number. For example, if you search for \*\*\*\* \*\*1234 in the UK, the search will return any number ending in 1234, regardless of the area code. Likewise, if you search for 1234\*\*9876 in the UK, the search will return numbers ending in 9876, in the 1234 area code

## Adding an external number for outbound calls

External numbers for outbound calls is only available on Professional and Enterprise plans.
To add an external number, you must have purchased at least one Zendesk number, plus have international calling activated. To activate international calling, contact [Zendesk customer support](https://support.zendesk.com/hc/en-us/articles/4408843597850). New external numbers are associated with your default brand at the time the number is added.

Note: For regulatory reasons, you cannot add external numbers from Malta.

When agents place outbound calls, the number selected in the call console appears as the caller ID. If you have an outside number that you'd like to appear for caller ID instead, you can add it as an external number. Some countries, such as Japan, do not support adding a phone number to an outgoing call and will display "Anonymous" instead of the number. This does not route incoming calls to the external number into Zendesk. It only allows you to place outbound calls using the external number.

Note: If you enable data locality to move your data to another region, then you'll no longer be able to use external numbers for outbound calling. To overcome this, you can request to have the external number ported into Zendesk. See [Porting numbers into Zendesk](https://support.zendesk.com/hc/en-us/articles/4408834776858).

For details on configuring using an external number for your outbound caller ID, see [Standardizing your outbound caller ID](https://support.zendesk.com/hc/en-us/articles/4408893291930).

**To add an external number**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_channels_icon.png)
   **Channels** in the sidebar, then select **Talk and email > Talk**.
2. Click the **Lines** tab.
3. Click **Add line** > **Add an external number**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/embedded_voice_5.png)
4. Enter the external number in the window that appears and click **Call** to receive a verification code.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/enter_ext_number.png)
5. Enter the verification code from the screen on your phone to verify the external number.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ext_number_verify.png)

The external number now appears in your list of phone lines.

Important: An external number uses your Zendesk number to make outgoing calls.
Because of this, you will be charged the same rate as any other outgoing call.

## Forwarding incoming calls from an existing number to Zendesk

If you want to keep using an existing telephone number for support, you can forward the calls to a Zendesk number. If you have a US-based number with another carrier, you also have the option of porting the number to Twilio (our voice service provider) to use as your Zendesk number.

**To forward calls**

1. Set up a Zendesk number as described in the section above.
2. Ask your telephone service provider to forward calls to the Zendesk number.

Make sure to check with your existing provider about passing the inbound caller ID to your Zendesk number.

**To port an existing number to Zendesk**

Zendesk lets you move or "port" your existing phone number to Zendesk for many countries.
Bear in mind that this process might take some time, so factor that into your plans. To get started, see [Porting numbers into Zendesk](https://support.zendesk.com/hc/en-us/articles/4408834776858).

## Adding a local business address

When adding a new line to Zendesk, for some locales, you'll need to add a local business address.

If you're adding a new number from one of these locales, you'll be prompted to enter the address while purchasing the number (see [Adding a new line](#topic_lj3_2c5_gv)).

If you're using an existing number that requires an address, you can enter it.

For a full list of address and documentation requirements for Zendesk numbers, see [Zendesk voice and text number address requirements](https://support.zendesk.com/hc/en-us/articles/4408824253978).

**To add a local business address for an existing number**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_channels_icon.png)
   **Channels** in the sidebar, then select **Talk and email > Talk**.
2. Click the **Addresses** tab.
3. Click **add address**.
4. Enter your address details.
5. Click **Save**.