# Troubleshoot impaired Amazon EC2 Linux instance using EC2Rescue

Source: apps/user-manuals/aws/ec2-ug.pdf

---

[HKEY_LOCAL_MACHINE\Software\Microsoft\Windows NT\CurrentVersion \ProfileList\ Option 2
1. Edit the relevant file, as follows:
- Windows Server 2012 R2 and earlier – Edit the EC2Config answer file (C:\Program Files \Amazon\Ec2ConfigService\sysprep2008.xml).
- Windows Server 2016 and 2019 – Edit the unattend.xml answer file (C:\ProgramData \Amazon\EC2-Windows\Launch\Sysprep\Unattend.xml).
- Windows Server 2022 – Edit the unattend.xml answer file (C:\ProgramData\Amazon \EC2Launch\sysprep\unattend.xml).
2. Change <CopyProfile>true</CopyProfile> to <CopyProfile>false</ CopyProfile>.
3. Run Sysprep again. Note that this configuration change will delete the built-in administrator user profile after Sysprep completes.
# Troubleshoot impaired Amazon EC2 Linux instance using EC2Rescue EC2Rescue EC2Rescue for Linux is an easy-to-use, open-source tool that can be run on an Amazon EC2 Linux instance to diagnose, troubleshoot, and remediate common issues using its library of over 100 modules. Modules are YAML files that contain either a BASH or a Python script and the necessary metadata.
Some generalized use cases for EC2Rescue for Linux instances include:
- Gathering syslog and package manager logs
- Collecting resource utilization data
- Diagnosing and remediating known problematic kernel parameters and common OpenSSH issues

Note The AWSSupport-TroubleshootSSH AWS Systems Manager Automation runbook installs EC2Rescue for Linux and then uses the tool to check or attempt to fix common issues that prevent an SSH connection to a Linux instance. For more information, see AWSSupport- TroubleshootSSH.
If you are using a Windows instance, see the section called "EC2Rescue for Windows instances".
Topics
- Install EC2Rescue on an Amazon EC2 Linux instance
- Run EC2Rescue commands on an Amazon EC2 Linux instance
- Develop EC2Rescue modules for Amazon EC2 Linux instances
## Install EC2Rescue on an Amazon EC2 Linux instance The EC2Rescue for Linux tool can be installed on an Amazon EC2 Linux instance that meets the following prerequisites.
Prerequisites
- Supported operating systems:
- Amazon Linux 2
- Amazon Linux 2016.09+
- SUSE Linux Enterprise Server 12+
- RHEL 7+
- Ubuntu 16.04+
- Software requirements:
- Python 2.7.9+ or 3.2+

### Install EC2Rescue The AWSSupport-TroubleshootSSH runbook installs EC2Rescue for Linux and then uses the tool to check or attempt to fix common issues that prevent a remote connection to a Linux machine via SSH. For more information, and to run this automation, see Support-TroubleshootSSH.
If your system has the required Python version, you can install the standard build. Otherwise, you can install the bundled build, which includes a minimal copy of Python.
To install the standard build
1. From a working Linux instance, download the EC2Rescue for Linux tool: curl -O https://s3.amazonaws.com/ec2rescuelinux/ec2rl.tgz
2. (Optional) Verify the signature of the EC2Rescue for Linux installation file. For more information, see (Optional) Verify the signature of EC2Rescue for Linux.
3. Download the sha256 hash file: curl -O https://s3.amazonaws.com/ec2rescuelinux/ec2rl.tgz.sha256
4. Verify the integrity of the tarball: sha256sum -c ec2rl.tgz.sha256
5. Unpack the tarball: tar -xzvf ec2rl.tgz
6. Verify the installation by listing out the help file: cd ec2rl-<version_number>
./ec2rl help To install the bundled build For a link to the download and a list of limitations, see EC2Rescue for Linux on github.

### (Optional) Verify the signature of EC2Rescue for Linux The following is the recommended process of verifying the validity of the EC2Rescue for Linux package for Linux-based operating systems.
When you download an application from the internet, we recommend that you authenticate the identity of the software publisher and check that the application has not been altered or corrupted after it was published. This protects you from installing a version of the application that contains a virus or other malicious code.
If, after running the steps in this topic, you determine that the software for EC2Rescue for Linux is altered or corrupted, do not run the installation file. Instead, contact Amazon Web Services.
EC2Rescue for Linux files for Linux-based operating systems are signed using GnuPG, an open- source implementation of the Pretty Good Privacy (OpenPGP) standard for secure digital signatures. GnuPG (also known as GPG) provides authentication and integrity checking through a digital signature. AWS publishes a public key and signatures that you can use to verify the downloaded EC2Rescue for Linux package. For more information about PGP and GnuPG (GPG), see https://www.gnupg.org/.
The first step is to establish trust with the software publisher. Download the public key of the software publisher, check that the owner of the public key is who they claim to be, and then add the public key to your keyring. Your keyring is a collection of known public keys. After you establish the authenticity of the public key, you can use it to verify the signature of the application.
Tasks
- Authenticate and import the public key
- Verify the signature of the package
#### Authenticate and import the public key The next step in the process is to authenticate the EC2Rescue for Linux public key and add it as a trusted key in your GPG keyring.
To authenticate and import the EC2Rescue for Linux public key
1. At a command prompt, use the following command to obtain a copy of our public GPG build key:

curl -O https://s3.amazonaws.com/ec2rescuelinux/ec2rl.key
2. At a command prompt in the directory where you saved ec2rl.key, use the following command to import the EC2Rescue for Linux public key into your keyring: gpg2 --import ec2rl.key The command returns results similar to the following: gpg: /home/ec2-user/.gnupg/trustdb.gpg: trustdb created gpg: key 2FAE2A1C: public key "ec2autodiag@amazon.com <EC2 Rescue for Linux>" imported gpg: Total number processed: 1 gpg:               imported: 1  (RSA: 1)
Tip If you see an error stating that the command cannot be found, install the GnuPG utility with apt-get install gnupg2 (Debian-based Linux) or yum install gnupg2 (Red Hat- based Linux).
#### Verify the signature of the package After you've installed the GPG tools, authenticated and imported the EC2Rescue for Linux public key, and verified that the EC2Rescue for Linux public key is trusted, you are ready to verify the signature of the EC2Rescue for Linux installation script.
To verify the EC2Rescue for Linux installation script signature
1. At a command prompt, run the following command to download the signature file for the installation script: curl -O https://s3.amazonaws.com/ec2rescuelinux/ec2rl.tgz.sig
2. Verify the signature by running the following command at a command prompt in the directory where you saved ec2rl.tgz.sig and the EC2Rescue for Linux installation file. Both files must be present.

gpg2 --verify ./ec2rl.tgz.sig The output should look something like the following: gpg: Signature made Thu 12 Jul 2018 01:57:51 AM UTC using RSA key ID 6991ED45 gpg: Good signature from "ec2autodiag@amazon.com <EC2 Rescue for Linux>" gpg: WARNING: This key is not certified with a trusted signature! gpg:          There is no indication that the signature belongs to the owner.
Primary key fingerprint: E528 BCC9 0DBF 5AFA 0F6C  C36A F780 4843 2FAE 2A1C Subkey fingerprint: 966B 0D27 85E9 AEEC 1146  7A9D 8851 1153 6991 ED45 If the output contains the phrase Good signature from "ec2autodiag@amazon.com <EC2 Rescue for Linux>", it means that the signature has successfully been verified, and you can proceed to run the EC2Rescue for Linux installation script.
If the output includes the phrase BAD signature, check whether you performed the procedure correctly. If you continue to get this response, contact Amazon Web Services and do not run the installation file that you downloaded previously.
The following are details about the warnings that you might see:
- WARNING: This key is not certified with a trusted signature! There is no indication that the signature belongs to the owner. This refers to your personal level of trust in your belief that you possess an authentic public key for EC2Rescue for Linux. In an ideal world, you would visit an Amazon Web Services office and receive the key in person. However, more often you download it from a website. In this case, the website is an Amazon Web Services website.
- gpg2: no ultimately trusted keys found. This means that the specific key is not "ultimately trusted" by you (or by other people whom you trust).
For more information, see https://www.gnupg.org/.
## Run EC2Rescue commands on an Amazon EC2 Linux instance EC2Rescue is a command line tool. After you have installed EC2Rescue on your Linux instance, you can get general help on how to use the tool by running ./ec2rl help. You can view the available modules by running ./ec2rl list, and you can get help on a specific module by running ./ ec2rl help module_name.

The following are common tasks you can perform to get started using this tool.
Tasks
- Run EC2Rescue modules
- Upload the EC2Rescue module results
- Create backups of an Amazon EC2 Linux instance
### Run EC2Rescue modules To run all EC2Rescue modules Use the ./ec2rl run command without specifying any additional parameters. Some modules require root access. If you are not a root user, use sudo when you run the command.
./ec2rl run To run a specific EC2Rescue module Use the ./ec2rl run command and for --only-modules, specify the name of the module to run.
Some modules require arguments to use them.
./ec2rl run --only-modules=module_name --arguments For example, to run the dig module to query the amazon.com domain, use the following command.
./ec2rl run --only-modules=dig --domain=amazon.com To view the results of an EC2Rescue module Run the module then view the log file in cat /var/tmp/ec2rl/logfile_location. For example, the log file for the dig module can be found in the following location: cat /var/tmp/ec2rl/timestamp/mod_out/run/dig.log

### Upload the EC2Rescue module results If Support has requested the results for a EC2Rescue module, you can upload the log file using the EC2Rescue tool. You can upload the results either to a location provided by Support or to an Amazon S3 bucket that you own.
To upload results to a location provided by Support Use the ./ec2rl upload command. For --upload-directory, specify the location of the log file.
For --support-url, specify the URL provided by Support.
./ec2rl upload --upload-directory=/var/tmp/ec2rl/logfile_location --support- url="url_provided_by_aws_support"
To upload results to an Amazon S3 bucket Use the ./ec2rl upload command. For --upload-directory, specify the location of the log file.
For --presigned-url, specify a presigned URL for the S3 bucket. For more information about generating pre-signed URLs for Amazon S3, see Uploading Objects Using Pre-Signed URLs.
./ec2rl upload --upload-directory=/var/tmp/ec2rl/logfile_location --presigned- url="presigned_s3_url"
### Create backups of an Amazon EC2 Linux instance You can use EC2Rescue to backup your Linux instance by creating an AMI or by creating snapshots of it's attached volumes.
To create an AMI Use the ./ec2rl run command and for --backup, specify ami.
./ec2rl run --backup=ami To create multi-volume snapshots of all attached volumes Use the ./ec2rl run command and for --backup, specify allvolumes.
./ec2rl run --backup=allvolumes To create a snapshot of a specific attached volume

Use the ./ec2rl run command and for --backup, specify the ID of the volume to back up.
./ec2rl run --backup=vol-01234567890abcdef
## Develop EC2Rescue modules for Amazon EC2 Linux instances Modules are written in YAML, a data serialization standard. A module's YAML file consists of a single document, representing the module and its attributes.
### Add module attributes The following table lists the available module attributes.
Attribute Description name The name of the module. The name should be less than or equal to 18 characters in length. version The version number of the module. title A short, descriptive title for the module.
This value should be less than or equal to 50 characters in length. helptext The extended description of the module.
Each line should be less than or equal to 75 characters in length. If the module consumes arguments, required or optional, include them in the helptext value.
For example: helptext: !!str | Collect output from ps for system analysis Consumes --times= for number of times to repeat Consumes --period= for time period between repetition

Attribute Description placement The stage in which the module should be run.
Supported values:
- prediagnostic
- run
- postdiagnostic language The language that the module code is written in. Supported values:
- bash
- python Note Python code must be compatible with both Python 2.7.9+ and Python 3.2+. remediation Indicates whether the module supports remediation. Supported values are True or False.
The module defaults to False if this is absent, making it an optional attribute for those modules that do not support remediation. content The entirety of the script code. constraint The name of the object containing the constraint values.

Attribute Description domain A descriptor of how the module is grouped or classified. The set of included modules uses the following domains:
- application
- net
- os
- performance class A descriptor of the type of task performed by the module. The set of included modules uses the following classes:
- collect (collects output from programs)
- diagnose (pass/fail based on a set of criteria)
- gather (copies files and writes to specific file) distro The list of Linux distributions that this module supports. The set of included modules uses the following distributions:
- alami (Amazon Linux)
- rhel
- ubuntu
- suse required The required arguments that the module is consuming from the CLI options. optional The optional arguments that the module can use.

Attribute Description software The software executables used in the module.
This attribute is intended to specify software that is not installed by default. The EC2Rescue for Linux logic ensures that these programs are present and executable before running the module. package The source software package for an executabl e. This attribute is intended to provide extended details on the package with the software, including a URL for downloading or getting further information. sudo Indicates whether root access is required to run the module.
You do not need to implement sudo checks in the module script. If the value is true, then the EC2Rescue for Linux logic only runs the module when the executing user has root access. perfimpact Indicates whether the module can have significant performance impact upon the environment in which it is run. If the value is true and the --perfimpact=true argument is not present, then the module is skipped. parallelexclusive Specifies a program that requires mutual exclusivity. For example, all modules specifyin g "bpf" run in a serial manner.
### Add environment variables The following table lists the available environment variables.

Environment Variable Description EC2RL_CALLPATH The path to ec2rl.py. This path can be used to locate the lib directory and use vendored Python modules.
EC2RL_WORKDIR The main tmp directory for the diagnostic tool.
Default value: /var/tmp/ec2rl .
EC2RL_RUNDIR The directory where all output is stored.
Default value: /var/tmp/ec2rl/<da te&timestamp>
.
EC2RL_GATHEREDDIR The root directory for placing gathered module data.
Default value:/var/tmp/ec2rl/<da te&timestamp>/mod_out/gathe red/ .
EC2RL_NET_DRIVER The driver in use for the first, alphabetically ordered, non-virtual network interface on the instance.
Examples:
- xen_netfront
- ixgbevf
- ena EC2RL_SUDO True if EC2Rescue for Linux is running as root; otherwise, false.
EC2RL_VIRT_TYPE The virtualization type as provided by the instance metadata.
Examples:

Environment Variable Description
- default-hvm
- default-paravirtual EC2RL_INTERFACES An enumerated list of interfaces on the system. The value is a string containing names, such as eth0, eth1, etc. This is generated via the functions.bash  and is only available for modules that have sourced it.
### Use YAML syntax The following should be noted when constructing your module YAML files:
- The triple hyphen (---) denotes the explicit start of a document.
- The !ec2rlcore.module.Module tag tells the YAML parser which constructor to call when creating the object from the data stream. You can find the constructor inside the module.py file.
- The !!str tag tells the YAML parser to not attempt to determine the type of data, and instead interpret the content as a string literal.
- The pipe character (|) tells the YAML parser that the value is a literal-style scalar. In this case, the parser includes all whitespace. This is important for modules because indentation and newline characters are kept.
- The YAML standard indent is two spaces, which can be seen in the following examples. Ensure that you maintain standard indentation (for example, four spaces for Python) for your script and then indent the entire content two spaces inside the module file.
### Example modules Example one (mod.d/ps.yaml):
--- !ec2rlcore.module.Module
# Module document. Translates directly into an almost-complete Module object name: !!str ps path: !!str

version: !!str 1.0 title: !!str Collect output from ps for system analysis helptext: !!str | Collect output from ps for system analysis Requires --times= for number of times to repeat Requires --period= for time period between repetition placement: !!str run package:
  - !!str language: !!str bash content: !!str |
  #!/bin/bash error_trap()
  { printf "%0.s=" {1..80} echo -e "\nERROR: "$BASH_COMMAND" exited with an error on line ${BASH_LINENO[0]}" exit 0 } trap error_trap ERR
  # read-in shared function source functions.bash echo "I will collect ps output from this $EC2RL_DISTRO box for $times times every $period seconds." for i in $(seq 1 $times); do ps auxww sleep $period done constraint: requires_ec2: !!str False domain: !!str performance class: !!str collect distro: !!str alami ubuntu rhel suse required: !!str period times optional: !!str software: !!str sudo: !!str False perfimpact: !!str False parallelexclusive: !!str
