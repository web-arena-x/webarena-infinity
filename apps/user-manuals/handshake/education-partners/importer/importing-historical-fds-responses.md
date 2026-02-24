# Importing Historical FDS Responses

Source: https://support.joinhandshake.com/hc/en-us/articles/360000697048-Importing-Historical-FDS-Responses

---

Your school may be interested in adding FDS responses into Handshake en masse. This article will explain what data you need, and what fields are required to import these responses into Handshake.

Topics:

- [What data do I need to import historical FDS responses?](#h_01HXJ0BP7FZNSKQ7MDJZ343QNF)
- [Import a graduation group from the past: Workflow 1](#h_01JWEHANW8SZRN65NHTX5WNNJQ)
- [Import a graduation group from the past: Workflow 2](#h_01JWEJ0HYXHMZPHPXC0VMPF0QP)
 - [Additional Considerations](#h_01JWEJ41EMK3HAP8QT0RTR2HMN)
- [Available fields for importing a Historical FDS Responses file](#h_01J3KEAP0F65YWNTEGZXHG9RX0)
 - [Download an example Historical FDS Responses CSV file](#h_01J42CP9PKSTCG8WTK7GB14MM7)

## What data do I need to import historical FDS responses?

- Student email

- The student *must* exist in Handshake in order to add a first destination response

- Education level name (one of the following - *case sensitive*):
 - High School
 - Associates
 - Certificate
 - Advanced Certificate
 - Bachelors
 - Masters
 - Doctorate
 - Postdoctoral Studies

- Outcome (one of the following - *case sensitive*):
 - Continuing Education
 - Military
 - Not Seeking
 - Still Looking
 - Volunteering
 - Working

For each response type, you'll need the following information:

- **If Working** - Employer name, employment category name, and employment type name
- **If Continuing Education** - School Name
- **If Military** - Military Branch Name
- **If Not Seeking** - Not Seeking Option Name (one of the following - *case sensitive*):

- Other
- Taking a gap year
- Taking time off
- Traveling

- **If Still Looking** - Seeking Option Name (one of the following - *case sensitive*):

- Continuing Education
- Employment

### Import a graduation group from the past: Workflow 1

To import a graduation group from the past, you can **deselect** the option to send recipient emails then select a future date for the graduation group date while using the group name field to indicate the real date.

Example:

![Set a future graduation date with the title of the actual date.png](https://support.joinhandshake.com/hc/article_attachments/32456668916759)

### Import a graduation group from the past: Workflow 2

Another way to upload historical FDS data and keep the graduation group dates and names accurately in the past is to instead adjust the email delivery timeline to be all future dates, then **save** the FDS, go back to edit it, then **deselect** the option to send recipient emails.

As long as you are importing responses, none of the emails will get sent. That and disabling the sending of emails will allow the date validation logic to work correctly, too.

#### Additional considerations

- When importing responses, please note that importing a Knowledge Response will prevent additional reminder emails from being sent to the student. If you want those emails to be sent, then we advise to wait till after the final reminder email is sent to upload responses.
- Grad Group *cannot* be included in the import, so we recommend adding students to the correct Grad Group *first*, then uploading responses afterward.
- At this time, no additional response data can be uploaded outside of the fields listed in this article. If you need to enter in knowledge responses for custom questions, this must be done manually in Handshake. Learn more about this here: [Enter a FDS Response for a Student (Knowledge Response)](https://support.joinhandshake.com/hc/en-us/articles/115010804328).

## Available fields for importing a Historical FDS Responses file

### Download an [example Historical FDS Responses CSV file](https://support.joinhandshake.com/hc/article_attachments/13489479124247)

The fields listed below should be formatted as displayed and saved as a CSV. Column headers are case sensitive and should be in all lowercase. If any of your headers differ from the formatting included below, the Importer will not identify it and it will be skipped. We recommend reviewing the example file linked above to ensure correct header formatting.

**Required Fields:** The column headers marked as required are necessary in the file. The column values marked as 'can't be blank' must contain values. Column values that aren't required can be left blank - this will not erase any existing data in that field.

**Optional Fields:** You can leave out any headers or values that are not marked as required - this will not erase any existing data in that field.

| **Column header** | **Column value** |
| --- | --- |
| student\_email **\*Required** | The student's account email in Handshake. **\*Can't be blank** |
| first\_destination\_response\_type\_name **\*Required** | One of the following options must be included:   ``` Continuing Education Military Not Seeking Still Looking Volunteering Working ```   **\*Can't be blank** |
| email\_address **\*Required** | Personal email address for the student (if you don’t know this you can import their university email address) **\*Can't be blank** |
| import\_identifier **\*Required** | This is an identifier (of your creation) and is unique to each student's responses. The import\_identifier can be anything, but it *has to be unique*. Examples of recommended identifiers are as follows: schoolhistoricalFDS100 schoolhistoricalFDS101 schoolhistoricalFDS102 schoolhistoricalFDS103 This field has a 250 character limit **\*Can't be blank** |
| education\_level\_name **\*Required** | One of the following options must be included:   ``` High School Associates Certificate Advanced Certificate Bachelors Masters Doctorate Postdoctoral Studies ``` **\*Can't be blank** |
| first\_destination\_survey\_id **\*Required** | ID number of the survey you will be importing data into (which can be found at the end of the URL of the survey's main page). If you haven't created this yet, please follow the instructions outlined [here](https://support.joinhandshake.com/hc/en-us/articles/219133387). **\*Can't be blank** |
| status **\*Required** | The status of the student's FDS response, with one of the following options (case sensitive): ``` in_progress submitted unsubmitted ``` **\*Can't be blank** |
| employment\_category\_name | **Required** if 'Working' or 'Volunteering' is selected under first\_destination\_response\_type\_name with one of the following options:   ``` Entrepreneur Faculty Non-Tenure Faculty Tenure Fellowship Freelancer Organization Other Temporary/Contract Work Assignment ``` |
| employer\_name | **Required** if 'Working' or 'Volunteering' options are selected under first\_destination\_response\_type\_name. This field has a 250 character limit |
| continuing\_education\_school\_name | **Required** if 'Continuing Education' option is selected under first\_destination\_response\_type\_name. This field has a 250 character limit |
| military\_branch\_name | **Required** if 'Military' option is selected under first\_destination\_response\_type\_name, with one of the following options:   ``` Air Force Army Coast Guard Marine Corps Navy ``` |
| not\_seeking\_option\_name | **Required** if 'Not Seeking' option is selected under first\_destination\_response\_type\_name, with one of the following options:   ``` Other Taking a gap year Taking time off Traveling ``` |
| seeking\_option\_name | **Required** if 'Still Looking' option is selected under first\_destination\_response\_type\_name, with one of the following options:   ``` Continuing Education Employment ``` |
| pay\_schedule\_name | **Required** if there is a value under 'Salary', with one of the following options:   ``` Hourly Wage Annual Salary Monthly Stipend ``` |
| primary\_major\_name | The Primary Major for the student. Must be an existing major under your school settings (under the Majors tab) |
| graduation\_date | The Graduation Date for the student. Dates ***must*** be in the following formatting:   ``` yyyy-mm-dd ``` |
| employment\_type\_name | **Required** if 'Working' option is selected under first\_destination\_response\_type\_name, with one of the following options:   ``` Full-Time Part-Time Seasonal ``` |
| location\_name | The student's location (all string values are accepted). This field has a 250 character limit |
| bonus\_amount | Student's sign-on bonus, if applicable. Must be a numerical value, without any decimals or special characters. |
| salary | Student's salary. Must be a numerical value, without any decimals or special characters. |
| found\_through\_handshake | Whether or not the student found this job through Handshake. Must use boolean values (case sensitive):   ``` TRUE FALSE ``` |
| job\_position\_name | The student's job position/title. This field has a 250 character limit |
| job\_function\_name | The function(s) of the student's job. Must be one of the following options:   ``` Accounting Actuary Administration Advertising, Media & PR Architecture & Planning Business Development Community & Social Services Construction / Contracting Consulting Counseling Customer/Technical Support Data & Analytics Design / Art Education / Teaching / Training Engineering - Civil / Mechanical / Other Engineering - Web / Software Entrepreneurship Environmental / Sustainability Mgmt Finance Fundraising & Event Management General Management Healthcare Services Hotel / Restaurant / Hospitality Human Resources Information Technology Legal Logistics & Supply Chain Marketing - Brand Management Marketing - General Military & Protective Services Operations / Production Other Political Organizing / Lobbying Product / Project Management Purchasing Quality Assurance Real Estate Research Sales Veterinary / Animal Care Writing / Editing ``` |
| start\_date | Start date of the student's job.  Dates ***must*** be in the following formatting: yyyy-mm-dd Must be after offer\_date and accept\_date |
| offer\_date | Date that the student was offered their job. Dates ***must*** be in the following formatting: yyyy-mm-dd Must be before accept\_date and start\_date |
| accept\_date | Date the student accepted their job offer. Dates **must** be in the following formatting: yyyy-mm-dd Must be after offer\_date and before start\_date |
| fellowship\_name | **Required** if 'TRUE' is selected under is\_fellowship If the student received a fellowship, the fellowship's name. This field has a 250 character limit |
| military\_rank\_name | Military rank if Military, with the options:   ``` Warrant Officer Enlisted Officer ``` |
| continuing\_education\_major\_name | If the student is pursuing additional education, their relevant major. This field has a 250 character limit |
| other\_compensation\_amount | Any additional compensation the student is receiving. Must be a numerical value, without any decimals or special characters. |
| employer\_industry\_name | The employer's associated industry for the job the student has accepted. Must be one of the following options:   ``` Accounting Advertising, PR & Marketing Aerospace Animal & Wildlife Architecture and Planning Automotive Biotech & Life Sciences Civil Engineering Commercial Banking & Credit Computer Networking Construction CPG - Consumer Packaged Goods Defense Design Electronic & Computer Hardware Energy Engineering & Construction Environmental Services Farming, Ranching and Fishing Fashion Financial Services Food & Beverage Forestry Government - Consulting Government - Intelligence Government - Local, State & Federal Healthcare Higher Education Hotels & Accommodation Human Resources Information Technology Insurance Interior Design International Affairs Internet & Software Investment Banking Investment / Portfolio Management Journalism, Media & Publishing K-12 Education Landscaping Legal & Law Enforcement Library Services Management Consulting Manufacturing Medical Devices Movies, TV, Music Natural Resources NGO Non-Profit - Other Oil & Gas Agriculture Other Education Other Industries Performing and Fine Arts Pharmaceuticals Politics Real Estate Religious Work Research Restaurants & Food Service Retail Stores Sales & Marketing Scientific and Technical Consulting Social Assistance Sports & Leisure Staffing & Recruiting Summer Camps/Outdoor Recreation Telecommunications Tourism Transportation & Logistics Utilities and Renewable Energy Veterinary Wholesale Trade ``` |
| specialization | Student's specialization, if any. This field has a 250 character limit |
| is\_fellowship | Whether or not the student accepted a fellowship. Must use boolean values (case sensitive):   ``` TRUE FALSE ``` |
| continuing\_education\_education\_level\_name | The additional education the student is pursuing, if any. Must be one of the following options:   ``` High School Associates Certificate Advanced Certificate Bachelors Masters Doctorate Postdoctoral Studies ``` |
| other\_employment\_category\_name | Can include the student's employment category here if it wasn't listed under employment\_category\_name. This field has a 250 character limit |
| employed\_during\_education | Whether or not the student was employed during their education at your institution. Must use boolean values (case sensitive):   ``` TRUE FALSE ``` |
| knowledge\_source | Where you obtained the FDS responses from (i.e. LinkedIn, Family, Phone Call, etc). This field has a 250 character limit |
| knowledge\_response | Whether or not these responses were entered on behalf of the student. Must use boolean values (case sensitive):   ``` TRUE FALSE ``` |
| authorized\_to\_work\_in\_us | Whether or not the student is authorized to work in the U.S. Must use boolean values (case sensitive):   ``` TRUE FALSE ``` |
| latest\_response | Whether this is the student's latest response/data. Must use boolean values (case sensitive):   ``` TRUE FALSE ``` |

You can also download the attached file below as a reference guide for your FDS responses.