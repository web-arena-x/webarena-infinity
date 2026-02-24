# Candidate Analysis

Source: https://support.joinhandshake.com/hc/en-us/articles/360052523873-Candidate-Analysis

---

Candidate Analysis is a feature that helps employers gain insights into how candidates engage with their company on the Handshake platform. By uploading a list of external candidates from your ATS, employers can identify and attribute candidate interactions and applications, both within Handshake and through external systems.

With Candidate Analysis, employers can better understand the impact of their recruitment strategies and showcase the return on investment (ROI) from their talent acquisition efforts on Handshake.

> If you haven’t already, please reach out to your Handshake CSM before using this tool.

*This feature is available to Premium partners only. For more information, check out this* [*resource*](https://www.joinhandshake.com/employers-premium/)*!*

**Topics:**

- [Access Candidate analysis](#h_01HQ9HC8A63AWS3FJN9167PWV1)
- [Upload candidate lists](#h_01HQ9HSJAREFB65TYNJECJ21PK)
- [How Handshake anonymizes candidate data](#h_01ERG4P7F5MY0NN8VPMPHJ0MYA)
- [What happens to your hashed data after it is uploaded?](#h_01ERG4PJX176MZ3YP02V0M8ACE)

### Access Candidate analysis

Click **Analytics** from the left navigation bar, then select **Candidate analysis** from the **Applicants** tab. 

- Handshake anonymizes the information imported to preserve your data privacy.
- Candidate accounts will only be displayed if the candidate has an active, public student or alumni account. Accounts that aren't activated or are set to private will not be included.

![Candidate analysis tab .png](https://support.joinhandshake.com/hc/article_attachments/26001457134999)

## 

### Upload candidate lists

#### Step 1: Prepare your file

The headers noted below are mandatory and must be present in your file.

Create a spreadsheet in a CSV format with the following headers: 

- **First Name**
- **Last Name**
- **Email Address**

| | | |
| --- | --- | --- |
| First Name | Last Name | Email Address |

**Note**: the file *cannot* exceed more than 150,000 candidate records. If you need to analyze more records, you'll need to separate the file into multiple uploads.

**Tips**:

- Before preparing your list, discuss with your Customer Success Manager which categories of candidate data to analyze:
 - Interns, Full-Time Early Talent Roles
 - Stage in the recruitment funnel:
    - Candidate leads
    - Applicants
    - Qualified applicants
    - Applicants who received offers
    - Hires
- We recommend uploading files based on the most recent hiring season, typically 4 months to a year. For example: All Summer 2024 Intern Applicants.
- Upload candidates that graduated from an academic institution in the past year or are currently enrolled in an academic institution.
- Only include candidates for US-based roles, i.e., no global or international candidates.
- Be as descriptive in your file-naming as possible (e.g., ‘Handshake\_2023\_fulltime\_offers.csv’).

#### Step 2: Upload your file

1. Click the blue button **Get started**.

![Get started button .png](https://support.joinhandshake.com/hc/article_attachments/26001457127191)

2. A pop-up will appear with our Data Privacy Policy. Click the blue button **I understand** in the lower-right corner to proceed. 

- To stop receiving this message, check the box for **Don't show this again**.

![Data_privacy_for_your_import_.png](https://support.joinhandshake.com/hc/article_attachments/26001429364631)

3. Choose your file.

- Max file size: 20 MB
- To obtain a sample file, click **Download sample file**.

After selecting your file, complete the following fields:

- **Candidate status**
 - Hired
 - Offered
 - Applied
 - Interviewed
 - Other
- **Starting and ending dates**
- **Role type**
 - Full-time
 - Internship
 - Part-time
 - Co-op
 - Management trainee
 - Other
- **Information about candidates** (*optional*)
 - e.g., Accounting candidates, candidates within our e-commerce division only, etc.

Once all fields are completed, click the black button **Continue** in the lower-right corner.

![Let's start form .png](https://support.joinhandshake.com/hc/article_attachments/26001457138199)

4. After clicking **Continue**, the data will be hashed. The hashing process might take up to 20 seconds.

![Hashing data.png](https://support.joinhandshake.com/hc/article_attachments/26001429376279)

5. Once the hashing process is complete, a message is displayed on the page indicating that the data has been hashed. A sample of the file is also provided. 

6. To import this data into Handshake for analysis, click the black button **Import & launch analysis**. 

![Data has been hashed.png](https://support.joinhandshake.com/hc/article_attachments/26001429380375)

7. Handshake will begin to search for candidates with matching hashed values.

- - First, Handshake will search using the hashed candidate email against its own database of hashed user emails.
 - Next, all remaining records not found by email are searched using hashed names.

8. Handshake will retrieve details on your historical interactions in the last 24 months with these matched candidates. Results will be shared with you through your Customer Success Manager. 

- Handshake does not report on candidates that you have not interacted with in the last 24 months.
- Because of limitations inherent in the matching process, the results may be incomplete.

To ensure that employer-provided hashed data is not stored in perpetuity, Handshake regularly deletes all uploaded files.

![Upload confirmation .png](https://support.joinhandshake.com/hc/article_attachments/26001429369623)

### How Handshake anonymizes candidate data

Once you have prepared a file with a list of candidates and have validated its format, Handshake will anonymize all fields in the file that could be used to identify the exact candidate. Specifically, Handshake will run an SHA-256 hashing algorithm on the First Name, Last Name, and Email fields in the file. This process will transform plaintext names and emails into 64-character hexadecimal values that are functionally impossible to decrypt.

As an example, “John Doe” would read as “6cea57c2fb6cbc2a40411135005760f241fffc3e5e67ab99882726431037f908” after hashing. You will be able to view a preview of these hashed values for verification before any data is transferred to Handshake.

File validation and hashing take place in your browser on your computer. Handshake does not receive any data from your local system until after hashing and you explicitly click the button to upload. 

### What happens to your hashed data after it is uploaded?

Handshake will start matching student/alumni accounts with the hashed fields. Handshake will identify the matching values produced by the hashing algorithm against its own set of hashed data, in the same way that web passwords are securely validated.

Handshake compiles an output report summarizing your historical interactions with the matched Handshake accounts in the past 24 months. This output report is emailed to your Handshake success team.

Once the above process is complete, the original hashed file is deleted from Handshake’s system. Handshake keeps the original file for *only* as long as needed to match Handshake accounts. Unmatched records are never shared or stored.