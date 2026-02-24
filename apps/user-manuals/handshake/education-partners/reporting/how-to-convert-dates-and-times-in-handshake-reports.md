# How to Convert Dates and Times in Handshake Reports

Source: https://support.joinhandshake.com/hc/en-us/articles/218693588-How-to-Convert-Dates-and-Times-in-Handshake-Reports

---

Would you like to convert the dates in a report that you have downloaded in Handshake? All dates that are pulled from Handshake are in UTC time which is Coordinated Universal Time.

If your download includes the text "UTC" at the end of your date/time cell, you will first have to remove that text from each cell. To do this, highlight the cells with your dates/times and utilize the Find and Replace feature within Excel to find the "UTC" text and replace it with nothing:

![mceclip0.png](https://support.joinhandshake.com/hc/article_attachments/25998877079063)

Next, format those cells in the Date / Time format of your choice:

![59589620160503-3-1ngaej7](https://support.joinhandshake.com/hc/article_attachments/25998866522775)

Finally, use the Excel formulas listed below to converting your dates (ST = Standard Time / DT = Daylight Savings):

**EST** =*CellName* - (5/24)

**EDT** =CellName - (4/24)

**CST** =*CellName* - (6/24)

**CDT** =*CellName* - (5/24)

**PST** =*CellName* - (8/24)

**PDT** =*CellName* - (7/24)

**MST** =*CellName* - (7/24)

**MDT** =*CellName* - (6/24)