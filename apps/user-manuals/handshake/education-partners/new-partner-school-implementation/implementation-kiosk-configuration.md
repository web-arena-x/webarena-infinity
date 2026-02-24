# Implementation: Kiosk Configuration

Source: https://support.joinhandshake.com/hc/en-us/articles/232288088-Implementation-Kiosk-Configuration

---

Kiosks are configured in Handshake using the information that you provide in [this form](https://forms.gle/QxgsX51qkznrYwXB6). With that information, our team produces a regex string and substring. The regex string defines the card output formatting that's being used, while the substring defines the actual student's card ID found within the raw output.

**Example:**

**Card output:** !9234708294300==124;

**Regex string:** ^!\d{13}==\d{3};$

**Student's card ID:** 347082

**Regex substring:**^!\d{2}(\d{6})\d{5}==\d{3};$

### Glossary of Regex terms:

- “**^**” = What every regex string will start with
- “**\d**” = the numbers you are wanting to convert in a card output. If there are 4 concurrent numbers in the output, then the regex would be “\d{4}
- “**\D**” = the letters you are wanting to convert in a card output. If there are 5 concurrent letters in an output, then the regex would be “\D{5}

### Rules of Thumb

- Card\_id on student record MUST be contained **within** the Card's output
- We can always shave off information from the output (i.e. if a student's correct card\_id is "1234123", an output of ";001234123400;:" can be submitted without issue, truncating to a card\_id of "1234123")
- We can't add information to the output of a card to make it match the card\_id of a student (i.e. if a student's correct card\_id is "0012341234", an output of ";1234123400;" will not submit successfully. The card\_id will require an update to "12341234")

### What if we have multiple card formats?

Handshake only supports one card format, so you'll need to partner with your team to determine which makes the most sense to add to Handshake for your events, fairs, appointments, interviews, etc.

If you'd like us to configure your kiosks, please fill out the following form: <https://forms.gle/QxgsX51qkznrYwXB6>

- **Note**: we recommend filling out this form at least a week before your first event. This will give your team enough time to test it and allow for any troubleshooting as needed.

### What if we want to configure our own kiosks?

Provided you have the correct permissions, you may go into your school settings and click "**Kiosk Preferences**" on the left menu, then fill out the open fields.

![Kiosk_Preferences_under_school_settings.png](https://support.joinhandshake.com/hc/article_attachments/26001282828439)

### Does Handshake support barcode readers?

It's not officially supported, but if the barcode reader outputs keyboard ([USB Output](http://www.taltech.com/barcodesoftware/articles/which_barcode_scanner_interface#usb)) and the student ID or a unique identifier is contained in the outputted string, then we should be able to support your barcode reader.