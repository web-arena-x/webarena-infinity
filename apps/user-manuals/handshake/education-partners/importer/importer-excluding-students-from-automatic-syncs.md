# Importer: Excluding Students from Automatic Syncs

Source: https://support.joinhandshake.com/hc/en-us/articles/115013032627-Importer-Excluding-Students-from-Automatic-Syncs

---

The '*Exclude from Automatic Sync*' setting prevents student accounts from being updated through the Importer (either by manual uploads or automated files sent to your institution's S3 bucket). This option can be found under each student's account settings, and can only be modified by Career Services staff.

One might exclude a student from syncs if the students data keeps getting changed to incorrect values via imports, or for an alumni user whose account should no longer be updated.

![](https://support.joinhandshake.com/hc/article_attachments/25998877224087)

**Note**: this field must be manually selected and deselected in-app; it cannot be bulk updated through the Importer with a student sync file.

If a student has '*Exclude from Automatic Sync*' enabled on their account, and a Career Services user uploads a file with the student included on it via import, the information will *not* update and an error message will generate stating "**exclude\_from\_sync**".