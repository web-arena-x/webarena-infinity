# Configure a Prefix and Starting Number for RFIs

Source: https://v2.support.procore.com/product-manuals/rfi-project/tutorials/configure-a-prefix-and-starting-number-for-rfis

---

## Background

For best results, a user with âAdminâ level permission should always configure the RFIs tool at the start of a project. To help with that configuration step, its important to understand the different options that are available.

### Configuration Options

RFI numbers in Procore must always be configured to use a starting number. Depending on the needs of your environment, a user with 'Admin' level permission can also configure the RFIs tool on your project to use either a custom prefix or a manual prefix. The table below describes your options:

| **RFI Configuration Option** | **Prefix** | **Starting Number** | **Example** |
| --- | --- | --- | --- |
| Default Starting Number | None | 1 | 1, 2â¦ |
| Custom Starting Number of Consistent Length | None | User Defined (e.g., 0001 or 1001) | 0001, 0002â¦ 1001, 1002â¦ |
| Manual Prefix and Default Starting Number | User Defined (e.g., RFI-) | 1 | RFI-1, RFI-2â¦ |
| Manual Prefix and Custom Starting Number of Consistent Length | User Defined (e.g. RFI-) | User Defined (e.g. 001 or 101) | RFI-001, RFI-002â¦ RFI-101, RFI-102â¦ |
| Project Stage Prefix and Default Starting Number | Custom Stage (e.g., BID, PRE, RFI, PST, WAR) | 1 | BID-1, BID-2â¦ |
| Project Stage Prefix and Custom Starting Number of Consistent Length | Custom Stage (e.g., BID, PRE, RFI, PST, WAR) | User Defined (e.g., 0001 or 1001) | BID-0001, BID-0002â¦ BID-1001, BID-1002â¦ |

#### Best Practices

For best results when configuring your RFI prefixes and/or numbering on a project, Procore recommends using these guidelines:

- The starting number must always be greater than zero (0). Always starting with one (1) is recommended (e.g., 1, 01, 001, 0001, 00001, 000001, and so on).
- The prefix should use a meaningful name that clearly communicates the project stage or usage intent. For example, Bidding (BID).
- The prefix must be between one (1) character and 30 characters in length. One (1) to three (3) characters is recommended.
- The prefix can contain any UTF-8 character. The most common UTF-8 characters to use with numbering are the hyphen (-) and the underscore (\_).

#### Limitations

Please be aware of the following prefix and numbering limitations:

- To ensure RFI prefixes function as intended, the **Project Stage** field must remain enabled on any RFI fieldset applied to the project.
- **Duplicate prefixes are NOT permitted**  
  For example, you cannot use "PCST" or "P-CST" to represent both Pre-Construction and Post-Construction. Instead, Procore recommends using the default prefixes of Pre-Constructions (PRE) and Post-Construction (PST) or creating a unique prefix for each stage.
- **Duplicate numbers are NOT permitted**  
  For example, you cannot have two RFIs with the same number.
- **Deleted RFI numbers are NEVER reused**  
  The system does NOT reuse numbers from deleted RFIs.

If your project has been configured to use RFI Prefixes, be aware of the following:

- Procore always separates the prefix from the RFI number with a hyphen (e.g., BID-1, BID-001, and so on). This hyphen cannot be removed.

##### Â Tip

If an authorized user enables the RFI Prefix by Project Stage option AFTER your project's RFIs have been created, automatic prefix will be applied to existing numbers that have manually entered prefixes. This can sometimes result in some numbers having two prefixes. To address this known limitation, see [Why do some of our project's RFI numbers have two prefixes?](/faq-why-do-some-of-our-projects-rfi-numbers-have-two-prefixes)

## Steps

- Configure a Manual Prefix and Starting Number  
  **OR**
- Configure a Project Stage Prefix and Starting Number

### Configure a Manual Prefix and Starting Number

Do the following when creating the first RFI for your project. For step-by-step instructions, see [Create an RFI](/product-manuals/rfi-project/tutorials/create-an-rfi).

1. Navigate to the project's **RFIs** tool.
2. Click **Create RFI**.
3. In the **Number** field, type the desired start number in the custom sequence.   
   *Examples*:

   - *To configure a starting number of consistent length*, tâââââype: 0001 or 1001
   - *To configure a manual prefix followed a starting number*, type: RFI0001 or RFI-1001
4. Continue to create the RFI as described in [Create an RFI](/product-manuals/rfi-project/tutorials/create-an-rfi).  
   The next time you create an RFI, the system will use your custom format to assign the next number to an RFI. You can change the numbering scheme at anytime, although it is NOT recommended.

### Configure a Project Stage Prefix and Starting Number

You must have 'Admin' level permission to perform the following steps:

1. Navigate to the project's **RFIs** tool.
2. Click **Configure Settings**.
3. Next to the **RFI Prefix Number: Prefix by Stage** area, place a checkmark in the **Once Enabled and In Use, this Configuration Cannot be Disabled** box.   
   ***Note*****:** Your Procore Administrator can configure Procore to use the default project stages and/or create custom project stages in the Company level Admin tool. See [Add a Custom Project Stage](/product-manuals/admin-company/tutorials/add-a-custom-project-stage).
4. Mark the 'Prefix Stage Enabled' checkbox for each stage you want to use for prefixing the RFI numbers.
5. Enter a prefix for each project stage selected.
6. Scroll to the bottom of the page and click **Update** to save your changes.