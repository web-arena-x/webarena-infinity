# Automatically redacting credit card numbers from tickets

Source: https://support.zendesk.com/hc/en-us/articles/4408822124314-Automatically-redacting-credit-card-numbers-from-tickets

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Growth, Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support** | Professional or Enterprise |

Users sometimes enter sensitive information such as credit card numbers in tickets
when they shouldn't. In addition to being visible to anybody with access to the
ticket, the credit card number automatically gets stored in a database with the
rest of the ticket.

You can use a feature called Automatic Redaction to redact, or remove digits from
credit card numbers found in ticket comments or custom fields so that the numbers
are no longer useful. The data is redacted when the ticket is created, and on
future comments and internal notes, to prevent the full credit card number from
being stored with Zendesk. This helps keep confidential information out of
Zendesk. Redacting credit card numbers already in the system is not supported.

Note: Due to potential conflicts, this feature shouldn't be
used at the same time as [redaction suggestions](https://support.zendesk.com/hc/en-us/articles/6669399593882).

Related articles:

- [Automatically detecting sensitive
  information for redaction](https://support.zendesk.com/hc/en-us/articles/6669399593882)
- [Redacting ticket content](https://support.zendesk.com/hc/en-us/articles/4408846470170)

Credit card numbers are identified in incoming tickets and comments/internal notes by
using the [Luhn algorithm](http://en.wikipedia.org/wiki/Luhn_algorithm) and by looking for the
prefixes and lengths of common credit card types. The checks don't guarantee that
all credit card numbers will be identified. They also don't guarantee that some
numbers that aren't credit card numbers will be skipped. The system does check for
phone number and URL patterns and skips them. For example, some international
phone numbers may pass the Luhn check -- though if the numbers start with a +,
they won't be redacted.

Numbers that appear to be valid credit card numbers are redacted by replacing some
digits with a replacement character, leaving the first six digits and the last
four digits intact. Example:

- String in incoming ticket: "I want a refund. My card number is 12 345123
  451234 8."
- String stored in Zendesk: "I want a refund. My card number is 12345 1▇▇▇▇
  ▇2348."

  In this example, the string of numbers shown above would not
  be redacted. To be redacted, the number you use must be in a valid
  credit card format.

Numbers are redacted if they're between 12 and 19 digits long. Most bank card numbers
are within this range.

The original credit card number isn't simply masked in the UI but completely redacted
from logs and database entries. It's kept in memory only long enough to check it.
The only exceptions to this are MIME-encoded emails and custom ticket fields in
suspended tickets, but these two exceptions will be removed in the near
future.

A tag is automatically added to tickets with redacted credit card numbers. You can
create a view to see all tickets with this tag in one
place.

**To start redacting credit card numbers**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_account_icon.png)
   **Account** in the sidebar, then select **Security > More settings**.
2. On the **Zendesk Support** tab, select the **Redact credit card
   numbers** checkbox in the **Redaction** section.
3. Click **Save**.

**To list the tickets with redacted credit card numbers**

- Create a view of tickets that contain the tag
  '"system\_credit\_card\_redaction."

  For information about creating
  views, see [Adding views](https://support.zendesk.com/hc/en-us/articles/4408888828570#topic_vcr_xfp_ec).