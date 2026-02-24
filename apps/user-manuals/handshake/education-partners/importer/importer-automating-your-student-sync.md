# Importer: Automating Your Student Sync

Source: https://support.joinhandshake.com/hc/en-us/articles/360012323314-Importer-Automating-Your-Student-Sync

---

*Once you've uploaded your first student file to Handshake using the Importer, you can automate your uploads!*

# Overview

Handshake sets up an isolated location for each school in a designated Amazon S3 bucket for you to transfer your student data files into.

1. University uploads data to Handshake's S3 bucket with their school's specific directory
2. Handshake's Importer tool will analyze your student data and provide any feedback or required formatting modifications via email or in the UI
3. Handshake's Importer tool will upload your student data into Handshake and it will either update your existing student data or create the new students imported

**Note:**

- You only have **write** permissions for your school's folder.
- These S3 directories are **write-only** so any attempts to **GET/LIST** contents will result in '*Access Denied*' Errors.
- We support all standard methods of uploading to AWS S3 that require PUT access.
- We **do not**support **FTP/SFTP** due to the required LIST access. WinSCP requires LIST access to S3 Buckets and therefore cannot be used.
- **Region** must be set to **us-east-1** for your file transfer to work.

# Step 1: Setup & Prerequisites

We recommend using Amazon's CLI tool, as this is the best tool for interacting with AWS S3 for your student uploads. If you cannot use this tool, please contact our Support Team.

If you already have Python, you can install the CLI using the following instructions (see [here](http://docs.aws.amazon.com/cli/latest/userguide/installing.html) for more installation details, based on your operating system):

```
pip install --upgrade --user awscli
```

If you don't have Python, you can install it using the bundled installer [here](http://docs.aws.amazon.com/cli/latest/userguide/awscli-install-bundle.html).

```
curl "https://s3.amazonaws.com/aws-cli/awscli-bundle.zip" -o "awscli-bundle.zip"
unzip awscli-bundle.zip
# with sudo 
sudo ./awscli-bundle/install -i /usr/local/aws -b /usr/local/bin/aws

# without sudo (assumes ~/bin is in your PATH)
./awscli-bundle/install -b ~/bin/aws
```

If you don't have Python and *cannot* install it to use the AWS CLI, alternative options can be found [here](https://docs.google.com/document/d/1LTnyGYMIHhQiua6hgW1CFng4ethg1D9kO6dtfgRbRUU/edit?usp=sharing).

# Step 2: Obtain your Credentials and Configure

**Please contact Handshake's Technical Support team [here](https://support.joinhandshake.com/hc/en-us/requests/new) to receive the AWS credentials for uploading data to Handshake.** Unless otherwise instructed by the Handshake team, you should use “us-east-1” as your region.

Next run the following and enter in your AWS Access Key and Secret Key

```
aws configure
AWS Access Key ID [****************JRTA]:
AWS Secret Access Key [****************RZ7O]:
Default region name [us-east-1]:
Default output format [None]:
```

# Step 3: Upload Your First File

Now you're ready to upload your file to Handshake! Note that you should have received an email giving you the exact AWS S3 Path to upload your file to (if you have not, please reach out to the [Support Team](https://support.joinhandshake.com/hc/en-us/requests/new)).

## Upload Syntax:

```
aws s3 cp [/path/your_local_file] s3://handshake-importer-uploads/[your folder]/[yyyymmdd]_users.csv
```

## Example Upload and Response:

```
aws s3 cp 20140410_users.csv s3://handshake-importer-uploads/importer-production-hudson_university/20140410_users.csv

upload: to s3://handshake-importer-uploads/importer-production-hudson_university/20140410_users.csv
```

The AWS S3 API will respond with the document ID if the file was successfully transferred, otherwise it will respond with an error. You can also check the command exit code to determine whether it was successful.

If you wish to send over a test upload, simply send a file that includes 'test' in the filename. This will send the file to your institution's Importer account and it will be analyzed for any file/formatting errors, but will not be processed.

# Step 4: Validate the File and Enable Autorun

1. Login to the [Importer](https://importer.joinhandshake.com/) and check to see that your file was accepted and passed all analyzer checks.

Here are some common problems you might've encountered if you do not see the file:

The file is not a true CSV  
**Fix**: Double check that the file you are trying to upload can be uploaded manually to the importer and processed successfully

The script you're running isn't successfully uploading the file to your S3 bucket  
**Fix**: Double check your script path and ensure it is returning successfully and giving you back the path of the uploaded object

1. Ensure the data being uploaded passes all the analyzers, if it does not you'll have to make adjustments to your extract script before we can turn on auto run for you.
2. If your file has passed all analyzer checks, **please reach out to our [Technical Support Team](https://support.joinhandshake.com/hc/en-us/requests/new) with the associated Importer job URL** so that we can process it and check for errors. Pending a successful upload, we will enable autorun for your institution!

# Step 5: Scheduling your Regular Upload

After we've enabled autorun for your AWS uploads, we recommend using cron to schedule a recurring upload. Here are instructions on [setting up cron](https://linuxize.com/post/scheduling-cron-jobs-with-crontab/) (for Linux), as well as for [Windows Task Scheduler](https://docs.microsoft.com/en-us/windows/win32/taskschd/task-scheduler-start-page) (if you are not using a Linux server for these uploads).

Pick a weekly, monthly, or semesterly date to do your upload (dependent on your institution's workflow/needs). In general, the format is:

```
 +---------------- minute (0 - 59)
 |  +------------- hour (0 - 23)
 |  |  +---------- day of month (1 - 31)
 |  |  |  +------- month (1 - 12)
 |  |  |  |  +---- day of week (0 - 6) (Sunday=0 or 7)
 |  |  |  |  |
 *  *  *  *  *  command to be executed
```

Example:

```
5 8 * * Sat   aws s3 cp users.csv s3://handshake-importer-uploads/importer-production-hudson_university/`date +"%Y-%m-%d"`_users.csv  >/dev/null 2>&1
```

# Troubleshooting AWS Errors

 If you receive any error messages during your AWS submission, you can refer to [Amazon's CLI error guide](https://docs.aws.amazon.com/AmazonS3/latest/API/ErrorResponses.html) to troubleshoot the error source and its associated resolution. If you need any assistance with this troubleshooting, please reach out to Support for assistance.