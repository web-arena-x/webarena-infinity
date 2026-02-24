# Accessibility and VPAT

Source: https://support.joinhandshake.com/hc/en-us/articles/115012476208-Accessibility-and-VPAT

---

At Handshake, we are committed to fostering an environment where all users can access and benefit from our platform's features and resources. Our team dedicates time regularly to reviewing and improving accessibility on an ongoing basis, with the updates included in this resource.

*We want to help enable all users on Handshake. If you have any feedback, please reach out to us at [accessibility@joinhandshake.com](mailto:accessibility@joinhandshake.com).*

**Past Updates**

- Avoid unnecessary use of heading elements
- Ensure heading level matches the heading’s visual importance/level
- Avoid the use of implicit headings
- Provide visual or instructions for user input
- Provide alternative text for images
- Provide visual labels or instructions for user input
- Provide alternative text for images
- Ensure text and images of text provide sufficient contrast
- Provide error prevention for legal commitments, financial transactions, test responses, and data changes
- Ensure that instructive text is placed at the beginning of a form
- Ensure implicit row header cells use elements with row scope
- Ensure alternative text for image links is informative
- Ensure CSS background images that convey meaning have textual and visible equivalents
- Ensure charts and graphs provide an informative and visible alternative description
- Ensure keyboard focus returns properly when menus are closed
- Ensure link text is meaningful within context
- Ensure Javascript functionality is accessible from the keyboard
- Ensure markup documents contain well-formed elements
- Ensure related links are grouped
- Ensure headings and labels are descriptive and unique
- Ensure text can be resized
- Avoid use of placeholder values or explain input
- Ensure content is visible to assistive technologies
- Ensure error messages are explicitly indicated at the beginning of a form after submit
- Provide a clear indication of fields in error for information that is submitted
- Complete work for: Ensure page tabs provide state and role
- Ensure custom controls are keyboard accessible
- Ensure page tabs provide state and role
- Inform assistive technologies of changes in content
- Ensure custom controls provide proper textual name, role, and state information
- Provide fieldsets for groups of form controls
- Ensure that keyboard focus remains within modal dialogs
- Avoid inappropriate use of ARIA roles, states, and properties
- Ensure color is not used as the sole method of indicating selection
- Ensure dialogs use proper structure
- Ensure ARIA roles, states, and properties are valid
- Provide fieldsets for groups of form controls - all of our common form components, specifically RadioButtonList, CheckboxList, MonthYearSelect, and Pills, are properly grouped within fieldsets. This will allow us to keep our form components accessible moving forward.
- Apply aria-live regions for favorite buttons (falls within Ensure custom controls provide proper textual name in the accessibility audit)
  - If a job shows up multiple times on a page, and the job is favorited in one area, an announcement will now be made to users with screen readers that the other parts of the UI are updated.
  - Along with this change, we were able to standardize how announcements are being made, which should make it easier to avoid this violation moving forward
- Provide fieldsets for groups of form controls
  - Postings
  - Profile
  - Reviews
  - First destination response
- Ensure form field constraints and errors are associated with their corresponding field
  - Profile
  - Appointments
  - First destination
- Inform assistive technologies of changes in content
  - Documents
  - Employers
  - Appointments
  - Peer messaging
- Ensure color is not the sole means of indicating error messages
  - Appointments
  - First Destination Surveys
- Ensure custom controls are keyboard accessible
  - Documents
  - Employers
  - Job roles
  - Notifications
  - Interview Schedules
- Ensure the reading order of content and elements are correct when viewed without style sheets
  - Employers
- Ensure page tabs provide state and role
  - Postings
  - Employers
  - Career fairs
  - Q&A
  - Search
  - Experiences
- Provide an informative, context-sensitive page title - 60% of our page titles did not have accurate titles. Highly used workflows below:
  - Login
  - Register
  - Homepage
  - Job search
  - Employers
  - Q&A
  - Review
  - Appointments
  - Messages
  - Notifications
  - Articles
  - Surveys
- Provide a valid label for form fields - 27% occurrence rate
  - Login
  - Profile
  - Job search
  - Reviews
  - Surveys
- Ensure custom controls provide proper textual name, role, and state information - 33% occurrence rate
  - Homepage
  - Profile
  - Employers
  - Jobs
  - Interests
  - Reviews
  - Notifications
- Ensure containing elements allow text resize without loss of functionality. 23% occurrence rate.
  - Jobs
  - First Destination Surveys
  - Appointments
  - Messages
- Provide an accessible alert method for content changes that occur without explicit user knowledge. 10% occurrence rate.
  - Interests
  - Articles
  - Surveys

**In Progress Updates**

- Ensure calendar components are keyboard accessible
- Ensure that non-modal calendars are rendered inline with the controls that activate them
- Ensure that calendar components do not use color alone to convey selection/meaning

Read more about our commitment, efforts, and software conformance reports in Handshake's [Accessibility Statement](https://joinhandshake.com/accessibility/).

### Handshake Web Content Accessibility Guidelines and VPAT

*Mobile versions (iOS and Android) updated May 2023*

*Web version updated June 2022*