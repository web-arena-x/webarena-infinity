# Importer: Primary Education Start/End Dates and Currently Attending for Students

Source: https://support.joinhandshake.com/hc/en-us/articles/224905027-Importer-Primary-Education-Start-End-Dates-and-Currently-Attending-for-Students

---

Education start and end dates do **\*not\*** automatically adjust the currently attending field, and conflicts can cause a user's record to fail to sync.

**primary\_education:start\_date, primary\_education:end\_date, and primary\_education:currently attending:**

- Not required fields
- One can exist without the other
- Must not conflict with each other

**Some examples of conflicts that will cause a record to fail:**

- **primary\_education:start\_date** is after the **primary\_education:end\_date**
- **primary\_education:end\_date** has expired (student has graduated) but **primary\_education:currently\_attending** is being passed as TRUE

- **primary\_education:currently\_attending** set to TRUE
- **primary\_education:end\_date** set to 2015-05-01

Please note that if a student has adjusted data in their profile (that is not being passed in the student sync) that conflicts with the data contained in your student sync file, this will cause the record to fail.

**Example:**

- School is only uploading **primary\_education:end\_date**
- The student has adjusted their profile to have a start date after the end date included in your student upload