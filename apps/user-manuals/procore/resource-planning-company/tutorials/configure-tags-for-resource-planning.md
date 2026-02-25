# Configure Tags for Resource Planning

Source: https://v2.support.procore.com/product-manuals/resource-planning-company/tutorials/configure-tags-for-resource-planning

---

## Background

Tags are specific criteria that can be added to both people and projects in Resource Planning. Tags can be filtered to help you organize and quickly find people and projects that match that criteria.

## Things to Consider

- [Required User](/product-manuals/resource-planning-company/permissions) [Permissions](/product-manuals/resource-planning-company/permissions)
- Tags can be categorized.
- Tags can be assigned to people, projects, or requests.
- Tags for people and projects can appear when their [QR Codes](/product-manuals/resource-planning-company/tutorials/configure-qr-codes-for-resource-planning) are scanned.
- Expiration dates, and warnings for upcoming expiration dates, can be configured with tags to alert when items such as certifications may be expiring. See [How do I use tags with expiration dates in Resource Planning?](/faq-how-do-i-use-tags-with-expiration-dates-in-resource-planning)

  - Expiration dates are only tracked for people, not projects.
  - For users to receive alerts about expiring tags, you must configure a notification profile and assign the profile to the user.

##### Example

Create tags for qualifications that people and projects need on a job site, such as an health and safety certifications or badging access. They are easy to see when scheduling and can be viewed when a QR code is scanned on a job site.

**Example: Tracking Certifications**

- Create a certification tag that employees must have on a job site.
- Configure the tag with expiration dates to track people's certifications so that they're always current.
- Attach documents, like their certificate, to tag to maintain a record of the certification.

**Example: Badging**

- Create the badging tag needed for a project (Airport, School District, etc.) and assign it to the project and to the people who are authorized to work on the project.
- When filling requests for the project, filter your available people by the project's badging tag.

## Steps

1. Navigate to the Company level **Resource Planning** tool.
2. Click the **Configure Settings**  icon.
3. Click **Tags**.
4. *Optional:* To group tags in categories, click the **Group Tags in Categories?** toggle **ON**.

   1. To create a new tag Category, click **New** in the 'Categories' section.
   2. Enter the **Category Name**.
   3. Click **Save**.
5. In the Tags section, click **New**.
6. Configure your tag with the following properties:

   1. **Name**\*. Enter the name of the tag.
   2. **Color**. Enter the color of the tag.
   3. **Require Expiration Date**. Mark this checkbox if the tag requires an expiration date.  
      *Note:* If requiring an expiration date, the expiration date needs to be added when adding the tag to a person's profile. This is commonly used to track a person's certifications. For more information, see [How do I use tags with expiration dates?](/faq-how-do-i-use-tags-with-expiration-dates-in-resource-planning)
   4. **# Days Warning Ahead of Expiration**. Enter the number of days in advance the person will be notified when their tag is expiring.
   5. **Globally Accessible to All Groups**. Mark this checkbox if you want to make this tag available in all groups. See [Configure Groups for Resource Planning](/product-manuals/resource-planning-company/tutorials/configure-groups-for-resource-planning).
   6. **Groups**\*. If you choose not to make the tag available to all groups, select which groups should have access to the tag.
   7. **Abbreviations (5 Characters)**. Enter the tag's abbreviation.
   8. **Categories.** If you chose to categorize your tags, select the categories in which the tag should appear.
7. Click **Save**.