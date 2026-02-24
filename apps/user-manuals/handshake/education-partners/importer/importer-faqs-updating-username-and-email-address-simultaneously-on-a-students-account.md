# Importer FAQs: Updating Username and Email Address Simultaneously on a Student's Account

Source: https://support.joinhandshake.com/hc/en-us/articles/360048150594-Importer-FAQs-Updating-Username-and-Email-Address-Simultaneously-on-a-Student-s-Account

---

The primary account identifier used for a student in all Importer uploads is their **username** field - this is why we recommend you set this value to something that is *unique and unchanging* for the student throughout their educational career (such as part or all of their email address, or card ID - which can be subject to change with name changes or lost ID cards, etc). If you would like further information on our recommendations for what values to associate with each field in your student upload file, please refer to our [Student Upload Guide](https://support.joinhandshake.com/hc/en-us/articles/233086688).

With that being said, we understand that this cannot always be achieved for every institution on Handshake (there may not be a unique identifier for each student that isn't subject to change under certain circumstances). For this reason, we do allow for updates to be made to the **username** field through the Importer, as long as you have *sensitive fields enabled* for the job you are submitting with these changes. More information on updating sensitive fields on a student's account can be found [here](https://support.joinhandshake.com/hc/en-us/articles/223411787).

For these uploads, the backup account identifier that will be used for student account updates is the **email\_address** field. This field will only be used as the account identifier in uploads where the **username** field is changing (and thus, cannot be used as the account identifier). For this reason, you *cannot* submit an upload file that will update a student's **username** *and* **email\_address** values simultaneously. This will leave the Importer's analyzer with no account identifier to utilize in correctly attaching the associated information to an account in Handshake. If you've attempted to submit an upload file that updates both of these fields, you will see the following failed row messages:

**{"auth\_identifier":["has already been taken"]}}**

**{"card\_id":["has already been taken"]}}**

For situations where both of these fields must be updated for a student, you'll need to submit two separate upload files:

-One that will update the **email\_address** field (holding the **username** field constant - i.e. the existing value on the student's account)

-One that will update the **username** field with sensitive fields enabled on the Importer job (now including the updated **email\_address** value)

More information on our Student Data best practices can be found [here](https://support.joinhandshake.com/hc/en-us/articles/360045679113). If you need assistance with your student upload file, or resolving any failed rows, please reach out to our Support Team.