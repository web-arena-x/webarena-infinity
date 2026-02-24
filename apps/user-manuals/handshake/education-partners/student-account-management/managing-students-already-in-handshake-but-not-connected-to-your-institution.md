# Managing Students Already in Handshake but Not Connected to Your Institution

Source: https://support.joinhandshake.com/hc/en-us/articles/115013134948-Managing-Students-Already-in-Handshake-but-Not-Connected-to-Your-Institution

---

There may be instances where a student has an account in Handshake, but they are not connected to your institution. This is due to:

- the student creating an account and not requesting to connect
- the student request to connect being rejected (denied) or left in pending by career services
- the student being connected to another institution

## Student has an account but they are not connected

When a student manually creates a new Handshake account, they can request to connect with your institution. If they are not connected, their profile remains active, but they can not explore your institutions offerings. To learn more about this process, refer to [How Students & Alumni Can Request to Access Handshake](https://support.joinhandshake.com/hc/en-us/articles/360006170614-How-Alumni-Can-Request-to-Access-Handshake).

If they are not connected to an institution, students *can* still access different parts of Handshake. To learn more about the access that students can have when they are not connected to an institution, refer to [EDU: Understanding the Job Seeker Experience - Connected vs. Not Connected](https://support.joinhandshake.com/hc/en-us/articles/33904911962903)

If a student creates an account and requests to connect, and they are declined, this will not delete the account but leave them unconnected. 

There are two possible indications a student already has an account in Handshake: 

- when you import the student's information through the importer and they appear on the failed rows download with the error **{"success":false,"errors":{"email\_address":["has already been taken"]}**
  - for more information on this, refer to [Importer Error: Email Address Has Already Been Taken](https://support.joinhandshake.com/hc/en-us/articles/4421092998295).
- when you manually create a student account in Handshake and receive a message that the email address is already in use

If the student is *not* already connected to another institution, there are two ways to resolve this and connect them:

- [manually add the student individually](#h_01FTGJGSVXB59XVZ7C9DX5X0B4)
- [reload the failed rows via the importer](#h_01FTGJH2DM1YK65G5VT3PN07WB)

**Note:** If the student has an account that's already connected to your institution and has another account that is not connected to your institution, they have a duplicate account. Refer to [Managing and Merging Duplicate Student Accounts](https://support.joinhandshake.com/hc/en-us/articles/115002657968) for more information on how to manage and *possibly* merge duplicate student accounts.

### Manually add the student individually

You can add students to your institution directly by email address on the Manage Students page. This is only recommended when connecting less than 25 students at a time, as it can be a time consuming process. To do this, follow the steps outlined in [Add an Existing Student Account to Your Institution](https://support.joinhandshake.com/hc/en-us/articles/360009480274).

**Note**: if the student's account is connected to another institution, you will receive an error message when attempting this workflow. Skip to the section below, titled [Student is connected to a different institution](#h_01FTECVHTJHW7T5FYZC4PYTVDT), for more information on this process.

### Reload the failed rows into Importer

If you need to connect several students to your institution, we recommend re-uploading the failed rows file into Importer. For detailed information on why this error is occurring and how to resolve , refer to [Importer Error: Email Address Has Already Been Taken](https://support.joinhandshake.com/hc/en-us/articles/4421092998295).

## Student is connected to a different institution

- If their email address is the **email domain for your institution**:
  - Confirm that they want to switch to your institution and then contact Handshake Support with the email address, name, and institution this student wants to be switched to.

- If their email address is the **email domain for a different institution**:
  - You will need to create a new student account for them with their current email address for your institution. The student will then have two email addresses and logins into Handshake, one for each institution they are connected to. Follow the steps outlined in [Create a Student Account Associated with Your Career Services Account](https://support.joinhandshake.com/hc/en-us/articles/219132677), using the student's information.

- If their email address **is a generic (gmail, yahoo, etc.) address**:
  - Confirm that they want to switch to your institution and then contact Handshake Support with the email address, name, and institution this student wants to be switched to.
  - Once they are connected to your institution, if they would like to update their email address, you can update their email address to their .edu address for your school. For information on this, refer to [Career Services User Settings: Email Change Request Process](https://support.joinhandshake.com/hc/en-us/articles/235760768-Email-Change-Request-Process).