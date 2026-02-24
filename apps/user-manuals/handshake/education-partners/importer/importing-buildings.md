# Importing Buildings

Source: https://support.joinhandshake.com/hc/en-us/articles/115003775048-Importing-Buildings

---

## Available fields for importing a Buildings file

The fields listed below should be formatted as shown and saved as a CSV. Column headers are case sensitive and should be in all lowercase. If any of your headers differ from the formatting included below, the Importer will not identify it and it will be skipped. We recommend reviewing the example file linked above to ensure correct header formatting.

**Required Fields:** The column headers marked as required are necessary in the file. The column values marked as 'can't be blank' must contain values. Column values that aren't required can be left blank - this will not erase any existing data in that field.

**Optional Fields:** You can leave out any headers or values that are not marked as required - this will not erase any existing data in that field.

| **Column header** | **Column value** |
| --- | --- |
| name **\*Required** | The building name. This field has a 250 character limit. **\*Can't be blank** |
| location\_attributes:name **\*Required** | The location of the building. This must be a *valid address* (GPS coordinates are also accepted). **\*Can't be blank** |

For information on how to upload rooms, please see: [Importing Rooms](https://support.joinhandshake.com/hc/en-us/articles/115003775348)

**When formatting is complete:**

Upload your CSV to the [Importer App](http://importer.joinhandshake.com/). Once it has been successfully analyzed without errors, click **Submit and Request Run**. You will receive a followup email once the file has processed, with any failed row information.