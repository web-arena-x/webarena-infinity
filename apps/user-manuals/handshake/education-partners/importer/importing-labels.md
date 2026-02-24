# Importing Labels

Source: https://support.joinhandshake.com/hc/en-us/articles/229507687-Importing-Labels

---

Labels are tags that can be applied to data in Handshake to help you classify and organize that data within the system. Labels can be applied to students, contacts, employers, and jobs. There are three types of labels in Handshake: normal, public, and system.

This article will highlight the process of bulk importing a *normal or public* label onto data in Handshake via the Importer.

You can only import *10 unique labels per file***.** If you have more than 10 different labels in the file, you'll need to split your existing file into multiple separate CSV files.

### Prerequisites

1. Make sure you have access to the [Importer Tool](https://support.joinhandshake.com/hc/en-us/articles/360016070934).
2. Understand how to manually add/edit a label in Handshake - refer to [School Settings: Labels](https://support.joinhandshake.com/hc/en-us/articles/218692998) for more information.

**Best Practice**: to ensure your label is connected to the appropriate **Used For** type, we recommend manually creating the label in Handshake first, then adding the label via the Importer.

### High Level Workflow

1. Format your CSV file according to the specifications below.
2. Upload the CSV file to the Importer with the file-type **Labels**.
3. Review any error messages or file warnings once analysis completes.
4. Choose the button to **Run Job**.

## **Available fields for importing a Labels file**

### **Download an** [**example Labels CSV file**](https://support.joinhandshake.com/hc/article_attachments/25291209715351)

The fields listed below should be formatted as shown and saved as a CSV. Column headers are case sensitive and should be in all lowercase. If any of your headers differ from the formatting included below, the Importer will not identify it and it will be skipped. We recommend reviewing the example file linked above to ensure correct header formatting.

**Required Fields:** The column headers marked as required are necessary in the file. The column values marked as 'can't be blank' must contain values. Column values that aren't required can be left blank - this will not erase any existing data in that field.

**Optional Fields:** You can leave out any headers or values that are not marked as required - this will not erase any existing data in that field.

| **Column header** | **Column value** |
| --- | --- |
| identifiable\_type **\*Required** | The object type you are attaching a label to. Must use one of the following (case sensitive):   ``` User Contact Employer Job ```   **\*Can't be blank** |
| user\_type **\*Required** | The user type you are attaching a label to.  Must use one of the following (case sensitive):   ``` Students Career Services ```   *Only used when uploading a label to a User. If you are uploading a label to a Contact, Employer, or Job, leave this field blank but still include the header.* |
| identifier **\*Required** | - For a User, this is their email address in Handshake. - For a Contact, this is their email address in Handshake.   - **Note**: if the email addresses aren't found in Handshake, the labels won't be applied. - For an Employer, this is the Employer ID  *Only used when uploading a label to a User, Contact, or Employer. If you are uploading a label to a Job, leave this field blank but still include the header.* |
| identifiable\_id **\*Required** | - For a Job, this is the Job ID  *Only used when uploading a label to a Job. If you are uploading a label to a User, Contact, or Employer, leave this field blank but still include the header.* |
| name **\*Required** | This is the name of the label you want to use. Only one label name can be inserted into a row. |
| label\_type | Must be on of the following:   ``` normal public ```   For more information regarding label types, see [Handshake's Guide to Using Labels](https://support.joinhandshake.com/hc/en-us/articles/360047541253) |

### Example Image of File

![Screen_Shot_2020-04-01_at_4.31.01_PM.png](https://support.joinhandshake.com/hc/article_attachments/25997636150551)