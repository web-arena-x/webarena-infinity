# RegEx reference for advanced AI agents

Source: https://support.zendesk.com/hc/en-us/articles/8357756811162-RegEx-reference-for-advanced-AI-agents

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **Add-on** | AI agents - Advanced |

The following table provides a list of RegEx values in alphabetical order.

However, note the following limitations:

- Lookahead and lookbehind syntax is not supported. See
  [Why is my customized RegEX not working in AI agents - Advanced?](https://support.zendesk.com/hc/en-us/articles/9546537135514)
- Start-of-line (^) and end-of-line ($) anchors are not supported.

Table 1.

| Value | Description | Format |
| --- | --- | --- |
| Affirmative | Customer enters anything starting with y or Y, five letters to show affirmation | `^[yY].{1,5}\b` |
| credit\_card | Preset in dashboard |  |
| CVV | CVV number | `(CVV|CVV\s)\d{3}` |
| DOB 1 | Date of birth formatted as YYYY-MM-DD, YYYYMMDD | `^\d{4}[.|-|\/]\d{2}[.|-|\/]\d{2}|^\d{8}` |
| DOB 2 | Date of birth formatted as DD/MM/YYYY | `\d{1,2}[.|\-|\/]\d{1,2}[.|\-|\/]\d{2,4}\b` |
| email | Preset in dashboard |  |
| IBAN | Preset in dashboard |  |
| mobileNumber | Mobile number, with or without prefix | `^[+]*[(]{0,1}[0-9]{1,4}[)]{0,1}([-\s.]?[0-9]){4,10}$` |
| Negative | Customer enters anything starting with n or N, five letters to show negation | `^[nN].{1,5}\b` |
| orderNumber | 8 or 16 digits, can include letters or numbers or both | `[0-9a-zA-Z]{8}|[0-9a-zA-Z]{16}` |
| PIN | Four digits, numbers only | `(\s{1})?\d{4}` |
| phoneNumber | Phone number, for example US, CA such as +1 NXX-NXX-XXXX or 01 NXX-NXX-XXXX or 001 NXX-NXX-XXXX | `(\d{0,3})?[ ()]?(?:[- ()]?\d[- ()]?){7}` |
| URL | Universal URL regEx | `((http|https)://)?[a-zA-Z0-9./?:-=#]+.([a-zA-Z]){2,6}([a-zA-Z0-9.&/?:-=#])*` |
| ZIP code | Zip code, for example Canada, such as A2B 3C4 | `(\d{5}([ -]\d{4})?|[A-Z]\d[A-Z][ -]?\d[A-Z]\d)` |