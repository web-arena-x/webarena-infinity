# Email Address Verification Limitations

Source: https://support.joinhandshake.com/hc/en-us/articles/360006245813-Email-Address-Verification-Limitations

---

We frequently receive questions around how email addresses are verified or handled if invalid. We will provide more information about this here.

*Neither Handshake, nor anyone else, can catch all invalid email addresses*. Most of the invalid addresses are manually-entered or are an invalid inbox (the part before the "@") at a valid domain. 

We attempt to verify the validity of email addresses that are supplied to us, as a part of our effort to reduce the amount of inaccurate data in our system. Handshake uses the following methods to verify emails:

- *Briteverify* - Only used when importing contacts
- *Built-in validation* - All emails saved in our app
- *Pre-send filter* - All emails when sent out

Unfortunately, it is *impossible* to tell for certain that an email address is valid. This is due to how email, as a technology, was designed and built.

## Limitations of All Email Validators

All email validators will have certain limitations, due to how the email standard is laid out in [RFC 822](https://tools.ietf.org/html/rfc822); the published standard for the format of email addresses.

Email address format validation is often inaccurate because writing software to verify all possible email addresses can be very error-prone. Instead, most providers either take a too-strict approach, which rejects some valid addresses, or a lenient approach, which will accept some invalid addresses.

Below are examples of email addresses, some are valid and some are not.

1. john.doe@example.com
2. john..doe@example.com
3. x@example.com
4. user@[2001:DB8::1]
5. "()<>[]:,;@\\\"!#$%&'-/=?^\_`{}| ~.a"@example.org
6. a"b(c)d,e:f;g<h>i[j\k]l@example.com
7. example@s.example

Two and six are the only invalid ones. The rest are perfectly acceptable. Many webmail providers, such as Gmail (or the related G Suite for Education), will often reject examples four and five as well.

## Mail Server Downtimes

Mail servers can experience temporary downtimes which will influence whether the email address is recognized as valid or not. An email address may work one day, and not the other. Similarly, an email address may appear as invalid one day, and the next day it may be valid. 

## Does the Mailbox Exist?

This question is impossible to answer for anyone outside of the organization that controls the mail server. This is for two reasons:

- There is no public directory of email addresses
- There is no way to ask a mail server if an address exists

The reason behind both of these is spam. If either of these were possible, it would be easy for spammers to harvest email addresses and send more targeted campaigns.

In the first case, spammers would download the whole directory and use it as a mailing list. In the second instance, they'd ask the target mail server about all possible email addresses, using a series of requests; "Does a@example.com exist? ... Does b@example.com exist? ... etc."

## Was the Email Marked as Spam?

No email server will tell you this, for similar reasons to the above; spammers would know their tactics have been discovered, and they'd be able to change them in order to bypass spam filters more regularly.

## Limitations of Specific Email Validators

In addition to the limitations laid out above, different validation tools will have their own nuances.

### Briteverify

Briteverify can (mostly) consistently validate the following:

- Address is properly-formatted
- Domain is valid (ex: joinhandshake.com is valid, but -adomain.com will never be valid.)
- Known email provider restrictions (ex: Gmail does not allow single-letter mailboxes, so "a@gmail.com" will never be valid.)

However, it incorrectly responds that emails are valid in the following cases:

- Domain is valid, but has no listed email server. (ex: "user@googleusercontent.com" is marked as valid, but googleusercontent.com has no listed email server.)
- Mailbox does not exist. (ex: "not-a-user@joinhandshake.com" is marked as valid, but does not exist.)

#### *Where Briteverify is Used*

We only use Briteverify for contact import jobs through the importer. We can't use Briteverify everywhere because we are limited on the number of emails we can check per day.

### Built-in Validation

The software we use to run our services has some basic email address validation built in. We use this when we store email addresses, regardless of whether they came in through the importer, web interface, or elsewhere.

This validation is fairly basic. It uses simple checks to approximately gauge if an email address is valid. Due to its construction, it will mark some valid addresses as invalid and vice-versa. It will, for example, correctly determine that "how\_is\_this\_an\_email???\/\/\/\/.com" is invalid, but incorrectly mark "student@example.eud" (a common typo) valid.

### Pre-Send Filter

This is only used immediately before actually trying to send an email. It prevents email send attempts if the top-level domain (e.g. .com, .net, .edu) is invalid.

This catches email addresses like "student@example.eud" or "recruter@example.comq" before they are sent. It would also (correctly) allow valid-but-unusual top-level domains, such as in "croupier@example.casino" and "meow@i.am.a.cat". (or "woof@i.am.a.dog", if you're more of a dog-person).

However, this is *all* it does, since it is intended to be used in combination with Briteverify and the built-in validation. If used alone, it would consider "how\_is\_this\_an\_email???\/\/\/\/.com" to be ok.