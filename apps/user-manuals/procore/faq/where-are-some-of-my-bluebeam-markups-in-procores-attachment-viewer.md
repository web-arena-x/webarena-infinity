# Where are some of my Bluebeam markups in Procore's attachment viewer? - Procore

Source: https://support.procore.com/faq/where-are-some-of-my-bluebeam-markups-in-procores-attachment-viewer

---

##### In Beta

This integration is currently available through a beta program. If you would like to participate in the beta, please reach out to your Procore point of contact.

## Answer

A past change to Bluebeam's software resulted in a known issue when viewing markup detail in Procore's attachment viewer. This issue was resolved on Thursday, October 26, 2017. It impacted users who completing their markup in Bluebeam or users who had deployed the Procore + Bluebeam integration with the Project level Submittals tool.

### If Your Markup Files Were Affected by this Issue

If any of your uploaded files were affected by the issue prior to the fix being deployed, simply review your file a Bluebeam Studio session (see [Create a Bluebeam Studio Session](https://support.procore.com/integrations/bluebeam/tutorials/create-a-bluebeam-studio-session "Create a Bluebeam Studio Session")) and then finalize the session (see Finalize a Bluebeam Studio Session) in order to re-upload it to the Submittals tool.

---

The information below is a historical description of the markup issue that impacted the attachment viewer:

#### Historical Description of Issue

After uploading a file containing Bluebeam markup into Procore's Submittals tool, not all of the markup details appear when viewing the file in Procore's attachment viewer. Procore's initial investigation has discovered that this issue typically affects (but is not limited to) the following Bluebeam markup types: *Arrows*, *Highlight*, *Boxes*, *Lines*, and some *Stamps*.

The illustrations below show an example of the known issue in closer detail.

##### Bluebeam Studio Session: Example Bluebeam Markup

The following illustration shows you an example of a file that has been marked up in a Bluebeam studio session. Note that in this example, three markup items are highlighted by the ORANGE arrows.

![bb-markup.png](https://support.procore.com/@api/deki/files/42318/bb-markup.png?revision=1&size=bestfit&width=537&height=662)

##### Procore Attachment Viewer: Example of Historical Issue

After uploading the file to Procore's attachment viewer (e.g., this the **Attach File(s)** area of a submittal), you will notice that the highlighted markup detail are NOT displaying as expected.  
 
![procore-missing-markup.png](https://support.procore.com/@api/deki/files/42319/procore-missing-markup.png?revision=1&size=bestfit&width=531&height=637)

##### Historical Workaround

If you want your project team members with access to the Submittals tool to view the Bluebeam markup, you may opt to flatten the image in Bluebeam prior to uploading it to Procore. However, it is important to note, that when you flatten an image you will not be able to view the original, unflattened drawing that maintains the vector layers or elements when you download that drawing back out of Procore.

To learn how to flatten images in Bluebeam, see this [Bluebeam Support Article](http://support.bluebeam.com/online-help/revu2017/Content/RevuHelp/04--Document/08--Flatten/Flatten-Markups--MT.htm "http://support.bluebeam.com/online-help/revu2017/Content/RevuHelp/04--Document/08--Flatten/Flatten-Markups--MT.htm").

## See Also

- [Bluebeam](https://support.procore.com/integrations/bluebeam "Bluebeam")
- [Sign in to Bluebeam from Procore](https://support.procore.com/integrations/bluebeam/tutorials/sign-in-to-bluebeam-from-procore "Sign into Bluebeam from Procore")