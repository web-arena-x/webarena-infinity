# Importer: Preferred Student Name

Source: https://support.joinhandshake.com/hc/en-us/articles/224900247-Importer-Preferred-Student-Name

---

The preferred\_name field is intended to be used if the student goes by a name that differs from their given ***first name***. You cannot include numerical characters (0-9) in this field. If a student has a number in their name (i.e. John the 3rd), you can change the numbers to roman numerals (i.e. John III)

It is strongly advised to not sync in the user's full name in the preferred\_name field, as this will create an undesired (and confusing) effect on the user's profile.

*\*Note: This field needs to be updated in your student system. If not, then any changes made in Handshake manually will be overwritten on the next import.*

**Example 1:**

Student's full name = Christina Thompson

preferred\_name = Tina  
  
Profile will display: Tina Thompson

**Example 2:**

Student's full name = Christina Thompson

preferred\_name = Thompson, Tina

Profile will display: Thompson, Tina Thompson

If you have accidentally processed a file using the student's full name in the preferred\_name field, this can be corrected by either:

- Updating the preferred\_name to include *only* their first name or nickname  
    
  ***OR***
- Inserting **\*\*CLEAR\*\*** (in preferred\_name field) for each student whose name you would like to clear out. When using **\*\*CLEAR\*\***, every letter should be capitalized with two asterisks at the beginning and end of the word.