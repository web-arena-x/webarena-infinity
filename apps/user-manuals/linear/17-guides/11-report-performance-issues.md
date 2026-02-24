# Report performance issues

Linear is engineered to be a highly performant application. If you're experiencing performance issues with the app, we’d like know about it. Follow the steps outlined below so we can investigate and resolve the issue as quickly as possible.

## What to include in your performance report

To help us diagnose and fix performance issues effectively, please include the following information in your report:

* **Short written description:** Briefly describe the performance problem you're experiencing (e.g., "The app becomes unresponsive when loading the projects list").
* **Screen recording:** A video recording showing the issue in action helps us see exactly what you're experiencing. You can use the built in screen recording tool on [MacOS](https://support.apple.com/guide/mac-help/take-a-screenshot-mh26782/mac) or [Windows](https://support.microsoft.com/en-us/windows/use-snipping-tool-to-capture-screenshots-00246869-1843-655f-f220-97299b865f6b) or a 3rd party tool like [Loom](https://www.loom.com/).
* **Performance snapshot:** A Chrome performance profile captured while the issue occurs provides technical data we can analyze.
* **Confirm workspace data access:** Please confirm in writing if you consent to our team accessing obfuscated data from your workspace to help diagnose the issue. All sensitive data is anonymized, so we will never be able to see issue details etc.

## How to record a performance snapshot

Follow these steps to capture a performance snapshot in Google Chrome:

### 1. Open Chrome DevTools

Right-click anywhere on the Linear app page and select **Inspect**, or press `Cmd`+`Option`+`I` (Mac) or `Ctrl`+`Shift`+`I` (Windows/Linux).

![1. Open Chrome DevTools](https://webassets.linear.app/images/ornj730p/production/2b188bb6cab20de70e379dc017babc1e1ee547d2-1203x1024.png?q=95&auto=format&dpr=2)

### 2. Navigate to the Performance tab

In the DevTools panel, click on the **Performance** tab at the top.

![2. Navigate to the Performance tab](https://webassets.linear.app/images/ornj730p/production/64c757c41f4e4ec8da92dc9f24b6ad45d3bb6a37-1203x1024.png?q=95&auto=format&dpr=2)

### 3. Start recording

Click the **Record** button (circular icon) in the Performance tab to begin capturing performance data.

* Uncheck the Screenshots option
* Check the Memory option

![3. Start recording](https://webassets.linear.app/images/ornj730p/production/b7bccb5d215b1f89a12751d17466c667063e73f4-1203x1024.png?q=95&auto=format&dpr=2)

### 4. Reproduce the issue

Perform the actions that trigger the performance problem. Try to keep the recording focused on demonstrating the specific issue.

![4. Reproduce the performance issue](https://webassets.linear.app/images/ornj730p/production/328dfb618f277b08a965a5ea8ea0ed6b732e4df9-1203x1024.png?q=95&auto=format&dpr=2)

### 5. Save the performance profile

Stop the recording and click the **Download** icon (downward arrow) in the Performance tab to save the performance profile as a `.json` file.

* Check all three options in the popover.

![5. Save the performance profile](https://webassets.linear.app/images/ornj730p/production/0ac6a6d99a73d29822bc510fbecaceb93c9c64fc-1203x1024.png?q=95&auto=format&dpr=2)

### 6. Send everything to support

Email [**support@linear.app**](mailto:support@linear.app?subject=Performance%20issue%20report&body=%5BShort%20written%20description%20of%20the%20issue%5D%0D%0A%5BAttach%20screen%20recording%20video%5D%0D%0A%5BAttach%20.json%20performance%20profile%5D%0D%0A%0D%0AI%20confirm%20that%20the%20Linear%20team%20can%20access%20obfuscated%20(anonymized)%20workspace%20data%20to%20help%20diagnose%20the%20issue) with:

* Your short written description of the issue
* The screen recording video file
* The performance profile `.json` file
* Confirmation of consent for the Linear team to access obfuscated workspace data



## FAQ

<details>
<summary>Which browser should I use?</summary>
Google Chrome is preferred. If you’re experiencing performance problems in a different browser like Safari or Firefox, they typically also offer performance recordings in a similar manner. Reach out to us if you need guidance.
</details>

<details>
<summary>What if I am using the desktop app?</summary>
The desktop app runs on Chromium, so the steps above will work there too.
</details>
