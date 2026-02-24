# How are submittals numbered in Procore? - Procore

Source: https://support.procore.com/faq/how-are-submittals-numbered-in-procore

---

## Answer

Each submittal in Procore must have a submittal number. A submittal's default number is assigned automatically when the submittal is created in the project's Submittals tool, but the number can be changed manually when creating or editing the submittal. How submittals are numbered by default depends upon whether or not the 'Number Submittals By Spec Section' setting is turned ON or OFF on your project. See [Configure Settings: Submittals Tool](https://support.procore.com/products/online/user-guide/project-level/submittals/tutorials/configure-settings-submittals-tool "Configure Settings: Submittals Tool").

- ****If the 'Number Submittals By Spec Section' configuration setting is turned ON****: The default submittal numbers are based on the number of submittals created under the spec section selected when each submittal is created. For example, the first submittal created under the spec section 03-3000 Concrete would be given the number "03-3000-1.0" by default (with "1" representing the number of submittals in that spec section and ".0" representing the revision number of the submittal). The next submittal created under the spec section 03-3000 Concrete will be numbered "03-3000-2.0" by default.
- ****If the 'Number Submittals By Spec Section' configuration setting is turned OFF****: The default submittal numbers are based on the total number of submittals created in the project. Regardless of which spec section the submittals is created under, the first submittal created on a project will given the number "1.0" by default (with ".0" representing the revision number of the submittal). The next submittal created will given the number "2.0" by default.  
    
  **Note**: If the 'Number Submittals by Spec Section' configuration setting is turned OFF, spec section numbers will still be included in the submittal's information and PDF exports, but will not be included in project extracts for the Submittals tool. See [Which tools can I extract project data from using the Procore Extracts application?](https://support.procore.com/faq/which-tools-can-i-extract-project-data-from-using-the-procore-extracts-application "Which tools can I extract project data from using the Procore Extracts application?")

## See Also

- [Configure Settings: Submittals Tool](https://support.procore.com/products/online/user-guide/project-level/submittals/tutorials/configure-settings-submittals-tool "Configure Settings: Submittals Tool")

## 

If you would like to learn more about Procore's submittals management software and how it can help your business, please visit our [construction submittals software product page ![icon-external-link.png](https://support.procore.com/@api/deki/files/186764/icon-external-link.png?revision=2&size=bestfit&width=14&height=14)](https://www.procore.com/project-management/submittals "https://www.procore.com/project-management/submittals").