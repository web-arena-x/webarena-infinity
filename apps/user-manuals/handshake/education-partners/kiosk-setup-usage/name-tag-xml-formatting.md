# Name Tag XML Formatting

Source: https://support.joinhandshake.com/hc/en-us/articles/360005841133-Name-Tag-XML-Formatting

---

Handshake's name tag printing uses XML (short for Extensible Markup Language) to transport data from student profiles via our check-in kiosk, then format that information on their printed name tag. 

As XML relies on customization, you'll need to ensure the XML you use meets your needs, is compatible with the student profile fields, and is formatted according to the name tag label size you'll be using. 

You can create your own custom XML, or we have some preconfigured XML that we know works well, if you'd prefer to use that to start with (or test with)!

**Note**: DYMO Connect is now supported for 450, 450 Turbo, and 550 printers! However, any XML created within Dymo Connect will not be compatible, instead you can use one of the examples below. If you are using the original DYMO Label Software, you can continue using it or upgrade to the most recent version. For additional details, refer to [Name Tag Printing System Requirements](https://support.joinhandshake.com/hc/en-us/articles/360009369114).

Topics:

- [Supported fields for name tags](#h_01FPX8PC9N838VV4YMD8G61NRV)
- [Format name tag XML](#h_01F6FZ2WNJKCW70T6V2EZHV7VP)
- [Add XML to an event or fair](#h_01FPX6367P34ZGENXRTN3VQTPC)
- Example XMLs   
  - [Label size 1 1/8 x 3 1/2](#label-two)
  - [Label size 2 1/4 x 4](#h_01FPX2V1X847T9XGHWH8EXPPB7)

### Supported fields for name tags

Handshake supports the following fields from the student profile for name tags:

- **FirstName**
  - The FirstName field will pull the student’s preferred name if they have one associated with their account.
- **LastName**
- **Name**
- **Major**
- **GradDate**
- **MajorGradDate**

The fields Major, GradDate, and MajorGradDate all pull data from the student's Education section on their profile. If your institution imports student data, this information should be included in the import.

When printing name tags, if any of this information is missing or inaccurate, we recommend to first double-check the student profile to ensure it's reflected correctly in Handshake.

### Format name tag XML

To customize your XML, open the Dymo software on your computer and follow the steps below.   
**Note:** At this time, only the Dymo Label Writer has the options listed below for customization. If you have Dymo Connect instead, we recommend using one of the below examples and editing the Font Family and Alignment sections directly to adjust the label formatting.

1. You will need to format your label based on the size of your label and the fields you would like to include. To do this, create a text box on your label as shown in the example below:

![dymo_label_box.jpg](https://support.joinhandshake.com/hc/article_attachments/26001342098455)

2. Double click on the text box and select the *Advanced* tab.

![dymo___advanced.jpg](https://support.joinhandshake.com/hc/article_attachments/26001342099863)

3. In the *Reference Name* text field, add one of the following supported fields:

- **FirstName**
- **LastName**
- **Name**
- **Major**
- **GradDate**
- **MajorGradDate**

4. Repeat steps 1-3 until your label is formatted with the information that you would like, then save your label format in a .label file, as you will need this when you add label printing to your event or fair.

You will need to open the .label file with a text editor in order to copy the XML code for Handshake.

![label_file_in_text_editor.jpg](https://support.joinhandshake.com/hc/article_attachments/26001342100887)

### Add XML to an event or fair

1. Navigate to the fair or event in Handshake, then click the **Edit** tab in the upper-right corner of the page.

2. Scroll to the bottom of the page and ensure **Name tag printing** is checked, then paste the XML in the text box below, **Name tag label XML**.

- - **Tip**: expand the Name tag label XML text box by clicking, holding, and dragging downward in the lower-right corner of the box, on the diagonal lines.

3. Make sure to save your updates after pasting!

## Example XMLs

View these common name tag label size XMLs:

- [Label size 1 1/8 x 3 1/2](#label-two)
- [Label size 2 1/4 x 4](#h_01FPX2V1X847T9XGHWH8EXPPB7)

### Label Size:  1 1/8" x  3 1/2"

```
<?xml version="1.0" encoding="UTF-8"?>
<DieCutLabel Version="8.0" Units="twips">
   <PaperOrientation>Landscape</PaperOrientation>
   <Id>Address</Id>
   <PaperName>30252 Address</PaperName>
   <DrawCommands>
      <RoundRectangle X="0" Y="0" Width="1581" Height="5040" Rx="270" Ry="270" />
   </DrawCommands>
    <ObjectInfo>
      <TextObject>
         <Name>FirstName</Name>
         <ForeColor Alpha="255" Red="0" Green="0" Blue="0" />
         <BackColor Alpha="0" Red="255" Green="255" Blue="255" />
         <LinkedObjectName />
         <Rotation>Rotation0</Rotation>
         <IsMirrored>False</IsMirrored>
         <IsVariable>False</IsVariable>
         <HorizontalAlignment>Left</HorizontalAlignment>
         <VerticalAlignment>Middle</VerticalAlignment>
         <TextFitMode>AlwaysFit</TextFitMode>
         <UseFullFontHeight>True</UseFullFontHeight>
         <Verticalized>False</Verticalized>
         <StyledText>
            <Element>
               <String>First Name</String>
               <Attributes>
                  <Font Family="Helvetica" Size="18" Bold="False" Italic="False" Underline="False" Strikeout="False" />
                  <ForeColor Alpha="255" Red="0" Green="0" Blue="0" />
               </Attributes>
            </Element>
         </StyledText>
      </TextObject>
      <Bounds X="331.2" Y="57.59995" Width="4320" Height="600" />
   </ObjectInfo>
   <ObjectInfo>
      <TextObject>
         <Name>LastName</Name>
         <ForeColor Alpha="255" Red="0" Green="0" Blue="0" />
         <BackColor Alpha="0" Red="255" Green="255" Blue="255" />
         <LinkedObjectName />
         <Rotation>Rotation0</Rotation>
         <IsMirrored>False</IsMirrored>
         <IsVariable>False</IsVariable>
         <HorizontalAlignment>Left</HorizontalAlignment>
         <VerticalAlignment>Middle</VerticalAlignment>
         <TextFitMode>AlwaysFit</TextFitMode>
         <UseFullFontHeight>True</UseFullFontHeight>
         <Verticalized>False</Verticalized>
         <StyledText>
            <Element>
               <String>Last Name</String>
               <Attributes>
                  <Font Family="Helvetica" Size="18" Bold="False" Italic="False" Underline="False" Strikeout="False" />
                  <ForeColor Alpha="255" Red="0" Green="0" Blue="0" />
               </Attributes>
            </Element>
         </StyledText>
      </TextObject>
      <Bounds X="345.6" Y="432" Width="4320" Height="600" />
   </ObjectInfo>
   <ObjectInfo>
      <TextObject>
         <Name>MajorGradDate</Name>
         <ForeColor Alpha="255" Red="0" Green="0" Blue="0" />
         <BackColor Alpha="0" Red="255" Green="255" Blue="255" />
         <LinkedObjectName />
         <Rotation>Rotation0</Rotation>
         <IsMirrored>False</IsMirrored>
         <IsVariable>False</IsVariable>
         <HorizontalAlignment>Left</HorizontalAlignment>
         <VerticalAlignment>Middle</VerticalAlignment>
         <TextFitMode>AlwaysFit</TextFitMode>
         <UseFullFontHeight>True</UseFullFontHeight>
         <Verticalized>False</Verticalized>
         <StyledText>
            <Element>
               <String>Major</String>
               <Attributes>
                  <Font Family="Helvetica" Size="18" Bold="False" Italic="False" Underline="False" Strikeout="False" />
                  <ForeColor Alpha="255" Red="0" Green="0" Blue="0" />
               </Attributes>
            </Element>
         </StyledText>
      </TextObject>
      <Bounds X="331.2" Y="864" Width="4320" Height="600" />
   </ObjectInfo>
</DieCutLabel>
```

### 

### Label Size: 2 1/4" x 4"

```
<?xml version="1.0" encoding="UTF-8"?>
<DieCutLabel Version="8.0" Units="twips">
   <PaperOrientation>Landscape</PaperOrientation>
   <Id>NameBadge</Id>
   <PaperName>30256 Shipping</PaperName>
   <DrawCommands>
         <RoundRectangle X="0" Y="0" Width="3331" Height="5760" Rx="180" Ry="180" />
         <RoundRectangle X="2880" Y="2520" Width="180" Height="720" Rx="120" Ry="120" />
   </DrawCommands>
   <ObjectInfo>
      <TextObject>
         <Name>FirstName</Name>
         <ForeColor Alpha="255" Red="0" Green="0" Blue="0" />
         <BackColor Alpha="0" Red="255" Green="255" Blue="255" />
         <LinkedObjectName />
         <Rotation>Rotation0</Rotation>
         <IsMirrored>False</IsMirrored>
         <IsVariable>False</IsVariable>
         <HorizontalAlignment>Center</HorizontalAlignment>
         <VerticalAlignment>Middle</VerticalAlignment>
         <TextFitMode>AlwaysFit</TextFitMode>
         <UseFullFontHeight>True</UseFullFontHeight>
         <Verticalized>False</Verticalized>
         <StyledText>
            <Element>
               <String>FirstName</String>
               <Attributes>
                  <Font Family="Helvetica" Size="23" Bold="False" Italic="False" Underline="False" Strikeout="False" />
                  <ForeColor Alpha="255" Red="0" Green="0" Blue="0" />
               </Attributes>
            </Element>
         </StyledText>
      </TextObject>
      <Bounds X="395.5701" Y="865.2173" Width="5002.188" Height="600" />
   </ObjectInfo>
   <ObjectInfo>
      <TextObject>
         <Name>LastName</Name>
         <ForeColor Alpha="255" Red="0" Green="0" Blue="0" />
         <BackColor Alpha="0" Red="255" Green="255" Blue="255" />
         <LinkedObjectName />
         <Rotation>Rotation0</Rotation>
         <IsMirrored>False</IsMirrored>
         <IsVariable>False</IsVariable>
         <HorizontalAlignment>Center</HorizontalAlignment>
         <VerticalAlignment>Middle</VerticalAlignment>
         <TextFitMode>AlwaysFit</TextFitMode>
         <UseFullFontHeight>True</UseFullFontHeight>
         <Verticalized>False</Verticalized>
         <StyledText>
            <Element>
               <String>LastName</String>
               <Attributes>
                  <Font Family="Helvetica" Size="23" Bold="False" Italic="False" Underline="False" Strikeout="False" />
                  <ForeColor Alpha="255" Red="0" Green="0" Blue="0" />
               </Attributes>
            </Element>
         </StyledText>
      </TextObject>
      <Bounds X="436.4294" Y="1527.131" Width="4932.344" Height="600" />
   </ObjectInfo>
   <ObjectInfo>
      <TextObject>
         <Name>MajorGradDate</Name>
         <ForeColor Alpha="255" Red="0" Green="0" Blue="0" />
         <BackColor Alpha="0" Red="255" Green="255" Blue="255" />
         <LinkedObjectName />
         <Rotation>Rotation0</Rotation>
         <IsMirrored>False</IsMirrored>
         <IsVariable>False</IsVariable>
         <HorizontalAlignment>Center</HorizontalAlignment>
         <VerticalAlignment>Middle</VerticalAlignment>
         <TextFitMode>AlwaysFit</TextFitMode>
         <UseFullFontHeight>True</UseFullFontHeight>
         <Verticalized>False</Verticalized>
         <StyledText>
            <Element>
               <String>MajorGradDate</String>
               <Attributes>
                  <Font Family="Helvetica" Size="23" Bold="False" Italic="False" Underline="False" Strikeout="False" />
                  <ForeColor Alpha="255" Red="0" Green="0" Blue="0" />
               </Attributes>
            </Element>
         </StyledText>
      </TextObject>
      <Bounds X="464.2029" Y="2305.022" Width="4945.391" Height="600" />
   </ObjectInfo>
</DieCutLabel>
```