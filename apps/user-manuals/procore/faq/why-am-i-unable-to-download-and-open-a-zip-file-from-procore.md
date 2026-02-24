# Why am I unable to download and open a .ZIP file from Procore? - Procore

Source: https://support.procore.com/faq/why-am-i-unable-to-download-and-open-a-zip-file-from-procore

---

## Background

You may get an error when you try to download and open certain .zip files from Procore. For example, you may encounter ﻿the error after you download documents from Procore in bulk.  
*Note*: This error only affects Windows machines.

## Answer

##### Important

Bid packages containing more than 100,000 files may lead to degraded application performance.

The reason why you may encounter the error is related to how the Windows OS parses the filename and underlying folder structure of a .ZIP file's contents. It is a known limitation across all Windows machines that it cannot open a .ZIP file when it exceeds the 260 character filename limit.  
 
When a .ZIP is created, the included files and the underlying folder structure is maintained to ensure that when its contents are unzipped/unpacked, the files are placed into the correct folder structure that matches the original file path. For example, you may have .ZIP file that contains a folder structure similar to the following:

//Documents/Projects/1234-Parkway-Place/Public/Bid-Documents/Specifications/Manual\_v1.pdf

In the example above, the full path contains 87 characters. If you opened the file, Windows would try to place the folders and files into the default destination path on your local computer, which may be: [C://Windows/Users/John/Downloads/](C://Windows/Users/John/Downloads/ "C://Windows/Users/John/Downloads/")

In this example, the destination path contains 33 characters. When both paths are combined (87 + 33), it yields a total of 120 characters. 
 
Windows machines can properly process ZIP files whose combined original and destination file paths are less than 260 characters in length. If the combined character length exceeds the 260 character limit, Windows will not be able to open the file and you will receive an error or failed event.

## Solution

Users will want to update their Microsoft .NET web framework to 4.6.2 or higher. 
 
Assuming the original file path does not exceed 260 characters, another option is to change the default destination path to a root level path (e.g. C://). The easiest way to change the default destination path is to save an image from a web browser window and select a root level destination (e.g. C://). Then download the .ZIP file from Procore again. (Windows will automatically remember the most recent destination path for unpacking .ZIP files.) Typically, the shorter destination path will allow you to successfully open/unpack the .ZIP file. However, if the .ZIP file itself exceeds the 260 character limit, you will need to contact the person who created and sent you the .ZIP file and request that they change their folder structure and file naming conventions so that the created .ZIP file does not exceed the 260 character limit.﻿ For more information, see Microsoft's documentation: [Maximum Path Length Limitation](https://docs.microsoft.com/en-us/windows/desktop/fileio/naming-a-file#maximum-path-length-limitation "https://docs.microsoft.com/en-us/windows/desktop/fileio/naming-a-file#maximum-path-length-limitation")﻿.