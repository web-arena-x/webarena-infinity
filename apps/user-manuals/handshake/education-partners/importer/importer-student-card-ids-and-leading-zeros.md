# Importer: Student Card IDs and Leading Zeros

Source: https://support.joinhandshake.com/hc/en-us/articles/115001027207-Importer-Student-Card-IDs-and-Leading-Zeros

---

Sometimes when handling data, especially in Excel, the leading 0's are not preserved. This can cause complications when uploading your student data. 

**Help! Why is my user not able to check in to the kiosk? ("User not found") Their card ID is swiping a lot of 0's that aren't on their user profile!**

If you have access to the [Importer App](https://support.joinhandshake.com/hc/en-us/sections/206357347-Data-Importer-App), please start by including the **card\_id** field in your next student upload. If there should not be any leading zeros in this field, remove these before saving your CSV file.

**How can I check that the original file has lost the leading 0's, since Excel removes them upon opening the file?**

Using a text editor, or right-clicking the file and "open with" notepad or a comparable program, you can take a look at the raw text, to ensure that the card\_id's have the leading 0's.

**Ways to avoid losing your leading 0's:**

- Try opening in a program other than Excel, if possible
- If opening in Excel, remember to reformat the card\_id column before saving

- Right click column> Format Cells > Custom Format > Add the number of characters in 0's

- E.g. if all card ID's are 16-digits, add 16 0's: 
 ![](https://support.joinhandshake.com/hc/article_attachments/25997597219351)
- This will prefix any ID number that does not meet the 16-digit specification

- If a card id reads: 123456789

- Adding the above customization will cause it to read: 0000000123456789