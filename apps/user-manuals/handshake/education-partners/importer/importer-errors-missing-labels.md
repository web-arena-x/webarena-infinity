# Importer Errors: Missing Labels

Source: https://support.joinhandshake.com/hc/en-us/articles/225407767-Importer-Errors-Missing-Labels

---

**Reasons a standard label will not show up:**

- "name is already taken"

- If importing a "public" label, *label\_type* must be specified

- defaults to "normal" label - institution only and will fail to import

- Label is already created and "used for" has been specified within Handshake

- If importing contact labels, used for must be adjusted for "All"; they cannot be applied if set to Employers or Appointments, for example

- "unable to find identifiable"

- Generally due to that user or event/appointment not being in the system

- If you can confirm that this is inaccurate and the user is in the system, check the formatting to ensure it meets Handshake requirements

**Please see label formatting requirements [here](http://documentation.joinhandshake.com/en/latest/csv.html#labels).**