# Managing file sending in live chat

Source: https://support.zendesk.com/hc/en-us/articles/4408886202394-Managing-file-sending-in-live-chat

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **Support with** | Live chat and messaging Team, Professional, or Enterprise |

Agents and visitors can share screenshots, PDFs, and other relevant files during a chat session directly from the dashboard or widget.

For information about how to share files in a chat session, see [Sending files in a chat](https://support.zendesk.com/hc/en-us/articles/4408828723738).

This article includes the following topics:

- [About file sharing in live chat](#topic_ukc_tjj_rvb)
- [Disabling file sharing](#topic_w53_tjj_rvb)
- [Adding additional file types](#topic_izp_tjj_rvb)

## About file sharing in live chat

By default, sharing is enabled for the following file types:

- PDF (.pdf)
- PNG (.png)
- JPEG (.jpeg)
- GIF (.gif)
- Text (.txt)

If needed, you can add more file types to the allowed list. See [Adding additional file types](#topic_izp_tjj_rvb) for more information.

Note: If you're using the [Mobile Chat SDK](https://support.zendesk.com/hc/en-us/articles/4408886121626), file types other than those listed above might not open when an agent sends them to a visitor, depending on the mobile operating system and the way the customer's app is configured.

The file extension and the MIME type of the file must match for a successful upload. For example, if you change the extension on a file from a *.jpg* to *.png* without doing an explicit conversion/export, the extension becomes *.png* but the mime type stays *.jpg*. Mismatched files are considered "malformed" and are blocked.

## Disabling file sharing

If you don't want agents and visitors to share any file types, you can disable file sharing completely.

**To turn off file sending**

1. From the dashboard, select **Settings** > **Account** > **File Sending** tab.
2. Click **Off** in the upper right-hand side.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/zopim_filesendingoff.png)
3. Click **Save Changes**.

## Adding additional file types

You can also choose to allow additional file types by adding them to the allowed file types list. Keep in mind that certain file types, such as executable (.exe), might not be safe, so exercise caution when allowing additional file types. Also note that if you allow compressed file types, such as ZIP (.zip), you're also allowing any file types the compressed file might include.

**To allow additional file types**

1. From the dashboard, select **Settings** > **Account** > **File Sending** tab.
2. Select the option to allow additional file types.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/zopim_addlfiletypes.png)
3. Enter the extensions of the additional file types you want to allow separated by a comma.
4. Select the check box to accept the risk associated with file types you choose to accept. ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/zopim_filesendingagreebox.png)
5. Click **Save Changes**.