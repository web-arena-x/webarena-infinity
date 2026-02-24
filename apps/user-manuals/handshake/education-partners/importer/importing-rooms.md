# Importing Rooms

Source: https://support.joinhandshake.com/hc/en-us/articles/115003775348-Importing-Rooms

---

If you'd like to import multiple rooms at once, you can do so using the steps in this article. To learn more about rooms, refer to [School Settings: Campus Information](https://support.joinhandshake.com/hc/en-us/articles/218692968).

**Note:** Your school must have Buildings configured in order to import Rooms. Refer to the [School Settings: Campus Information](https://support.joinhandshake.com/hc/en-us/articles/218692968) article or import Buildings by referring to [Importing Buildings](https://support.joinhandshake.com/hc/en-us/articles/115003775048).

## Fields for importing a rooms file

The following headers should be formatted as listed, and saved as a CSV. Column headers are case sensitive and should be in all lowercase. If any of your headers differ from the formatting below, the Importer will not identify it and it will likely be skipped.

**Required Fields:** The headers marked as required are necessary in the file. The fields marked as 'Can't be blank' must contain values. Fields that aren't required can be left blank - this will not erase any existing data in that field.

**Optional Fields:** You can leave out fields or values that are not marked as required - this will not erase any existing data in that field.

| **Column header** | **Column value** |
| --- | --- |
| name **\*Required** | The name of the room. *\****Can't be blank** |
| building\_name **\*Required** | The name of the building. Must be a building already existing at the school. **\*Can't be blank** |
| capacity **\*Required** | The room's capacity (integer).  Must be >1 and <10,000. **\*Can't be blank** |
| available\_start | When the room becomes available. |
| available\_end | When the room is no longer available. |

**Note:** The system assumes UTC for the date/time. Please see our date formatting guide for assistance with the date and time formatting: [Importer: Date Formatting](https://support.joinhandshake.com/hc/en-us/articles/231942648)

#### When you've finished formatting the CSV

Upload the file to the Importer App. After it's finished analyzing the file, correct any errors and re-upload if needed, then click **Submit and Request Run**.

One of our technical support specialists will process the file within 24 hours of submission.