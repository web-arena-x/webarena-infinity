# Manage device drivers for your EC2 instance

Source: apps/user-manuals/aws/ec2-ug.pdf

---

5. Configure you export properties, delivery location, and tags (optional).
6. Choose Create.
AWS CLI To create a data export Use the following command to create a data export with the specified configuration: aws ec2 create-capacity-manager-data-export \ --s3-bucket-name my-exports-bucket \ --s3-bucket-prefix capacity-data-exports \ --schedule hourly \ --output-format parquet/CSV \ --tag-specifications 'ResourceType=capacity-manager-data- export,Tags=[{Key=environment,Value=production}]'

# Manage device drivers for your EC2 instance Device drivers are software components that communicate with the virtualized hardware for your Amazon EC2 instance. To prevent system errors, performance issues, and other unexpected behavior, it's important to keep your drivers up-to-date. That's especially true for drivers that can have a strong impact on system performance depending on your usage, such as networking, graphics, and storage device drivers. New driver releases can include defect fixes or introduce expanded functionality that you might want to take advantage of for instances that are currently running.
## Network drivers Linux distributions can incorporate networking features like Elastic Network Adapter (ENA) or Elastic Fabric Adapter (EFA) within the kernel. However, the timing may vary for implementation of kernel driver features within the different distributions.
ENA and EFA Linux kernel drivers are available from the Amazon Drivers GitHub repository. For more information and links to the available drivers, see Amazon Drivers on GitHub.

For more information about ENA drivers, see Enable enhanced networking with ENA on your EC2 instances. For more information about EFA drivers, see Getting started topics in the Elastic Fabric Adapter for AI/ML and HPC workloads on Amazon EC2 section of this guide.
To install or update networking drivers on Windows instances, see the following topics:
- Install the ENA driver on Windows
- Install the latest AWS PV drivers For more information, see Paravirtual drivers for Windows instances.
Note EFA is not supported on Windows instances.
## Graphics drivers To install or update graphics drivers, see the following topics:
- AMD drivers for your EC2 instance
- NVIDIA drivers for your Amazon EC2 instance
## Storage device drivers To install or update storage drivers, see the following topics:
- For Linux instances, see Install or upgrade the NVMe driver in the Amazon EBS User Guide.
- For Windows instances, see AWS NVMe drivers.
## AMD drivers for your EC2 instance An instance with an attached AMD GPU, such as a G4ad instance, must have the appropriate AMD driver installed. Depending on your requirements, you can either use an AMI with the driver preinstalled or download a driver from Amazon S3.
To install NVIDIA drivers on an instance with an attached NVIDIA GPU, such as a G4dn instance, see NVIDIA drivers instead.

Contents
- AMD Radeon Pro Software for Enterprise Driver
- AMIs with the AMD driver installed
- AMD driver download
### AMD Radeon Pro Software for Enterprise Driver The AMD Radeon Pro Software for Enterprise Driver is built to deliver support for professional- grade graphics use cases. Using the driver, you can configure your instances with two 4K displays per GPU.
Supported APIs
- OpenGL, OpenCL
- Vulkan
- AMD Advanced Media Framework
- Video Acceleration API
- DirectX 9 and later
- Microsoft Hardware Media Foundation Transform
### AMIs with the AMD driver installed AWS offers different Amazon Machine Images (AMIs) that come with the AMD drivers installed.
Open Marketplace offerings with the AMD driver.
### AMD driver download If you aren't using an AMI with the AMD driver installed, you can download the AMD driver and install it on your instance. Only the following operating system versions support AMD drivers:
- Amazon Linux 2 with kernel version 5.4
- Ubuntu 20.04
- Ubuntu 22.04
- Ubuntu 24.04
- Windows Server 2016

- Windows Server 2019
- Windows Server 2022 These downloads are available to AWS customers only. By downloading, you agree to use the downloaded software only to develop AMIs for use with the AMD Radeon Pro V520 hardware.
Upon installation of the software, you are bound by the terms of the AMD End User License Agreement.
#### Install the AMD driver on your Amazon Linux 2 Linux instance
1. Connect to your Linux instance.
2. Install the AWS CLI on your Linux instance and configure default credentials. For more information, see Installing the AWS CLI in the AWS Command Line Interface User Guide.
Important Your user or role must have the permissions granted that contains the AmazonS3ReadOnlyAccess policy. For more information, see AWS managed policy:
AmazonS3ReadOnlyAccess in the Amazon Simple Storage Service User Guide.
3. Install kernel 5.4 $ sudo amazon-linux-extras disable kernel-5.10 $ sudo amazon-linux-extras enable kernel-5.4 $ sudo yum install -y kernel
4. Install gcc and make, if they are not already installed.
$ sudo yum install gcc make
5. Update your package cache and get the package updates for your instance.
$ sudo amazon-linux-extras install epel -y $ sudo yum update -y
6. Reboot the instance.
$ sudo reboot

7. Reconnect to the instance after it reboots.
8. Download the latest AMD driver.
$ aws s3 cp --recursive s3://ec2-amd-linux-drivers/latest/ .
9. Extract the file.
$ tar -xf amdgpu-pro-*rhel*.tar.xz
10. Change to the folder for the extracted driver.
11. Run the self install script to install the full graphics stack.
$ ./amdgpu-pro-install -y --opencl=pal,legacy
12. Reboot the instance.
$ sudo reboot
13. Confirm that the driver is functional.
$ sudo dmesg | grep amdgpu The response should look like the following:
Initialized amdgpu
#### Install the AMD driver on your Ubuntu Linux instance
1. Connect to your Linux instance.
2. Update your package cache and get the package updates for your instance.
$ sudo apt-get update --fix-missing && sudo apt-get upgrade -y
3. Install gcc and make, if they are not already installed.
$ sudo apt install build-essential -y
4. Install Linux firmware and kernel modules

$ sudo apt install linux-firmware linux-modules-extra-aws -y
5. Reboot instance $ sudo reboot
6. Reconnect to the instance after it reboots.
7. Install the AMD Linux driver package
- For Ubuntu 20.04:
$ wget https://repo.radeon.com/.preview/afe3e25b8f1beff0bb312e27924d63b5/amdgpu- install/5.4.02.01/ubuntu/focal/amdgpu-install_5.4.02.01.50402-1_all.deb $ sudo dpkg --add-architecture i386 $ sudo apt install ./amdgpu-install_5.4.02.01.50402-1_all.deb
- For later Ubuntu versions go to Linux® Drivers for AMD Radeon™ Graphics and download the latest Ubuntu package and install it.
$ sudo apt install ./amdgpu-install_{version-you-downloaded}.deb
8. Run the self install script to install the full graphics stack.
$ amdgpu-install --usecase=workstation --vulkan=pro -y
9. Reboot the instance.
$ sudo reboot
10. Confirm that the driver is functional.
$ sudo dmesg | grep amdgpu The response should look like the following:
Initialized amdgpu

#### Install the AMD driver on your Windows instance
1. Connect to your Windows instance and open a PowerShell window.
2. Configure default credentials for the AWS Tools for Windows PowerShell on your Windows instance. For more information, see Getting Started with the AWS Tools for Windows PowerShell in the AWS Tools for PowerShell User Guide.
Important Your user or role must have the permissions granted that contains the AmazonS3ReadOnlyAccess policy. For more information, see AWS managed policy:
AmazonS3ReadOnlyAccess in the Amazon Simple Storage Service User Guide.
3. Set the key prefix according to your version of Windows:
- Windows 10 and Windows 11 $KeyPrefix = "latest/AMD_GPU_WINDOWS10"
- Windows Server 2016 $KeyPrefix = "archives"
- Windows Server 2019 $KeyPrefix = "latest/AMD_GPU_WINDOWS_2K19" # use "archives" for Windows Server 2016
- Windows Server 2022 $KeyPrefix = "latest/AMD_GPU_WINDOWS_2K22"
4. Download the drivers from Amazon S3 to your desktop using the following PowerShell commands.
$Bucket = "ec2-amd-windows-drivers"
$LocalPath = "$home\Desktop\AMD"
$Objects = Get-S3Object -BucketName $Bucket -KeyPrefix $KeyPrefix -Region us-east-1 foreach ($Object in $Objects) { $LocalFileName = $Object.Key if ($LocalFileName -ne '' -and $Object.Size -ne 0) {

    $LocalFilePath = Join-Path $LocalPath $LocalFileName Copy-S3Object -BucketName $Bucket -Key $Object.Key -LocalFile $LocalFilePath - Region us-east-1 } }
5. Unzip the downloaded driver file and run the installer using the following PowerShell commands.
Expand-Archive $LocalFilePath -DestinationPath "$home\Desktop\AMD\$KeyPrefix" - Verbose Now, check the content of the new directory. The directory name can be retrieved using the Get-ChildItem PowerShell command.
Get-ChildItem "$home\Desktop\AMD\$KeyPrefix"
The output should be similar to the following:
Directory: C:\Users\Administrator\Desktop\AMD\latest Mode                LastWriteTime         Length Name ----                -------------         ------ ---- d-----       10/13/2021  12:52 AM                210414a-365562C-Retail_End_User.2 Install the drivers: pnputil /add-driver $home\Desktop\AMD\$KeyPrefix\*.inf /install /subdirs
6. Follow the instructions to install the driver and reboot your instance as required.
7. To verify that the GPU is working properly, check Device Manager. You should see "AMD Radeon Pro V520 MxGPU" listed as a display adapter.
8. To help take advantage of the four displays of up to 4K resolution, set up the high- performance display protocol, Amazon DCV.

## NVIDIA drivers for your Amazon EC2 instance An instance with an attached NVIDIA GPU, such as a P- or G- series instance types, must have the appropriate NVIDIA driver installed. Depending on the instance type, you can either download a public NVIDIA driver, download a driver from Amazon S3 that is available only to AWS customers, or use an AWS AMI with the driver pre-installed.
To install AMD drivers on an instance with an attached AMD GPU, such as a G4ad instance, see AMD drivers instead.
Topics
- Types of NVIDIA drivers
- Available drivers by instance type
- Installation options
- Use AMIs that include NVIDIA drivers
- Install NVIDIA public drivers
- Install NVIDIA GRID drivers (G7e, G6, Gr6, G6e, G6f, Gr6f, G5, G4dn, and G3 instances)
- Install NVIDIA gaming drivers (G7e, G6, G6e, G5, and G4dn instances)
### Types of NVIDIA drivers The following are the main types of NVIDIA drivers that can be used with GPU-based instances.
Tesla drivers These drivers are intended primarily for compute workloads, which use GPUs for computational tasks such as parallelized floating-point calculations for machine learning and fast Fourier transforms for high performance computing applications.
GRID drivers These drivers are certified to provide optimal performance for professional visualization applications that render content such as 3D models or high-resolution videos. You can configure GRID drivers to support two modes. Quadro Virtual Workstations provide access to four 4K displays per GPU. GRID vApps provide RDSH App hosting capabilities.

Gaming drivers These drivers contain optimizations for gaming and are updated frequently to provide performance enhancements. They support a single 4K display per GPU.
Configured mode On Windows, the Tesla drivers are configured to run in Tesla Compute Cluster (TCC) mode. The GRID and gaming drivers are configured to run in Windows Display Driver Model (WDDM) mode. In TCC mode, the card is dedicated to compute workloads. In WDDM mode, the card supports both compute and graphics workloads.
NVIDIA control panel The NVIDIA control panel is supported with GRID and Gaming drivers. It is not supported with Tesla drivers.
Supported APIs for Tesla, GRID, and gaming drivers
- OpenCL, OpenGL, and Vulkan
- NVIDIA CUDA and related libraries (for example, cuDNN, TensorRT, nvJPEG, and cuBLAS)
- NVENC for video encoding and NVDEC for video decoding
- Windows-only APIs: DirectX, Direct2D, DirectX Video Acceleration, DirectX Raytracing
### Available drivers by instance type The following table summarizes the supported NVIDIA drivers for each GPU instance type.
Instance type Tesla driver GRID driver Gaming driver G3 Yes Yes No G4dn Yes Yes Yes G5 Yes Yes Yes G5g Yes ¹ No No

Instance type Tesla driver GRID driver Gaming driver G6 Yes Yes Yes G6e Yes Yes Yes G6f No Yes No Gr6 Yes Yes No Gr6f No Yes No G7e Yes Yes Yes P2 Yes No No P3 Yes No No P4d Yes No No P4de Yes No No P5 Yes No No P5e Yes No No P5en Yes No No P6-B200 Yes No No P6e-GB200 Yes No No P6-B300 Yes No No ¹ This Tesla driver also supports optimized graphics applications specific to the ARM64 platform
### Installation options Use one of the following options to get the NVIDIA drivers required for your GPU instance.
Options

1. Use AMIs that include NVIDIA drivers
2. Install NVIDIA public drivers
3. Install NVIDIA GRID drivers (G7e, G6, Gr6, G6e, G6f, Gr6f, G5, G4dn, and G3 instances)
4. Install NVIDIA gaming drivers (G7e, G6, G6e, G5, and G4dn instances)
### Use AMIs that include NVIDIA drivers AWS and NVIDIA offer different Amazon Machine Images (AMIs) that come with the NVIDIA drivers installed.
- Marketplace offerings with the Tesla public driver
- Marketplace offerings with the GRID driver
- Marketplace offerings with the Gaming driver To review considerations that are dependent on your operating system (OS) platform, choose the tab that applies to your AMI.
Linux To update the driver version installed using one of these AMIs, you must uninstall the NVIDIA packages from your instance to avoid version conflicts. Use this command to uninstall the NVIDIA packages:
[ec2-user ~]$ sudo yum erase nvidia cuda The CUDA toolkit package has dependencies on the NVIDIA drivers. Uninstalling the NVIDIA packages erases the CUDA toolkit. You must reinstall the CUDA toolkit after installing the NVIDIA driver.
Windows If you create a custom Windows AMI using one of the AWS Marketplace offerings, the AMI must be a standardized image created with Windows Sysprep to ensure that the GRID driver works.
For more information, see Create an Amazon EC2 AMI using Windows Sysprep.

### Install NVIDIA public drivers If the AWS Marketplace AMIs described in Use AMIs that include NVIDIA drivers don't fit your use case, you can install the public drivers and bring your own license. Installation options include the following:
- Option 1: Driver-only install
- Option 2: Install with the CUDA toolkit (recommended for Linux distributions)

P6-B200 and P6-B300 instance type considerations The P6-B200 and P6-B300 platforms are unique in that they expose Mellanox ConnectX network interface cards (NICs) to the instance as PCIe devices. These NICs do not act as typical network interfaces but instead function as NVSwitch bridges providing a control path to initialize and configure the NVFabric, which is the NVLink topology of the GPU interconnect.
To fully initialize the system, the NVIDIA Fabric Manager must configure NVFabric and establish the NVSwitch topology. This enables InfiniBand kernel modules to communicate with the Mellanox ConnectX NICs.
NVIDIA Fabric Manager is included in the CUDA toolkit. We recommend Option 2: Install with the CUDA toolkit for this instance type.
#### Option 1: Driver-only install To install a specific driver, log on to your instance and download the 64-bit NVIDIA public driver for the instance type from  http://www.nvidia.com/Download/Find.aspx. For Product Type, Product Series, and Product, use the options shown in the following table.
Then follow the Local Repository Installation instructions in the  NVIDIA Driver Installation Guide.
Note P6-B200 and P6-B300 instance types require installation and configuration of additional packages that come bundled with the NVIDIA CUDA Toolkit. For more information, see instructions for your Linux distribution in Option 2: Install with the CUDA toolkit.

Instance Product type Product series Product Minimum driver version G3 Tesla M-Class M60 -- G4dn Tesla T-Series T4 -- G5 Tesla A-Series A10 470.00 or later G5g1 Tesla T-Series T4G 470.82.01 or later G6 Tesla L-Series L4 525.0 or later G6e Tesla L-Series L40S 535.0 or later Gr6 Tesla L-Series L4 525.0 or later G7e Tesla RTX series RTX PRO 6000 Blackwell 575.0 or later P2 Tesla K-Series K80 -- P3 Tesla V-Series V100 -- P4d Tesla A-Series A100 -- P4de Tesla A-Series A100 -- P5 Tesla H-Series H100 530 or later P5e Tesla H-Series H200 550 or later P5en Tesla H-Series H200 550 or later P6-B2002 Tesla HGX-Series B200 570 or later P6e-GB200 Tesla HGX-Series B200 570 or later P6-B3002 Tesla HGX-Series B300 580 or later

1 The operating system for G5g instances is Linux aarch64.
2 For P6-B200 and P6-B300 instance types, there are additional installation requirements to configure NVIDIA Fabric Manager.
#### Option 2: Install with the CUDA toolkit Install instructions vary slightly by operating system. To install public drivers on your instance with the NVIDIA CUDA toolkit, follow the instructions for your instance operating system. For instance operating systems that aren't shown here, follow the instructions for your operating system and instance type architecture on the NVIDIA Developer website. For more information, see CUDA Toolkit Downloads.
For instance type architecture or other specifications, see the Accelerated computing specifications in the Amazon EC2 Instance Types reference.
##### Amazon Linux 2023 This section covers an NVIDIA CUDA toolkit install on an Amazon Linux 2023 instance. The command examples in this section are based on an x86_64 architecture.
For arm64-sbsa commands, see CUDA Toolkit Downloads and select the options that apply to your distribution. Instructions appear after you've made your final selection.
Prerequisite Before installing the toolkit and drivers, run the following command to ensure that you have the correct version of the kernel headers and development packages.
[ec2-user ~]$ sudo dnf install kernel-devel-$(uname -r) kernel-headers-$(uname -r) -y Download the toolkit and drivers Choose the type of installation to use for your instance, and follow the associated steps.
RPM local installation You can follow these instructions to download the CUDA toolkit installer repository bundle to your instance, then extract and register the specified bundle.
To view instructions on the NVIDIA developer website, see CUDA Toolkit Downloads.

[ec2-user ~]$ wget https://developer.download.nvidia.com/compute/cuda/13.0.0/ local_installers/cuda-repo-amzn2023-13-0-local-13.0.0_580.65.06-1.x86_64.rpm [ec2-user ~]$ sudo rpm -i cuda-repo-amzn2023-13-0- local-13.0.0_580.65.06-1.x86_64.rpm RPM network installation You can follow these instructions to register the CUDA repository with the package manager on your instance. When you run the install steps, the package manager downloads only the packages that are required.
To view instructions on the NVIDIA developer website, see CUDA Toolkit Downloads.
[ec2-user ~]$ wget https://developer.download.nvidia.com/compute/cuda/ repos/ubuntu2404/x86_64/cuda-keyring_1.1-1_all.deb [ec2-user ~]$ sudo dpkg -i cuda-keyring_1.1-1_all.deb Remaining steps are the same for both local and network installation.
1. Complete the CUDA toolkit install [ec2-user ~]$ sudo dnf clean all [ec2-user ~]$ sudo dnf install cuda-toolkit -y
2. Install the open kernel module variant of the driver [ec2-user ~]$ sudo dnf module install nvidia-driver:open-dkms -y
3. Install GPUDirect Storage and Fabric Manager [ec2-user ~]$ sudo dnf install nvidia-gds -y [ec2-user ~]$ sudo dnf install nvidia-fabric-manager -y
4. Enable Fabric Manager and driver persistence [ec2-user ~]$ sudo systemctl enable nvidia-fabricmanager [ec2-user ~]$ sudo systemctl enable nvidia-persistenced
5. (P6-B200 and P6-B300 only) These instance types require installation and configuration of additional packages that come bundled with the NVIDIA CUDA Toolkit.

1. Install NVIDIA Link Subnet Manager and ibstat.
[ec2-user ~]$ sudo dnf install nvlink5
2. Enable automatic loading of the Infiniband module on startup.
[ec2-user ~]$ echo "ib_umad" | sudo tee -a /etc/modules-load.d/modules.conf
6. Reboot the instance [ec2-user ~]$ sudo reboot
##### Ubuntu 24.04 This section covers an NVIDIA CUDA toolkit install on an Ubuntu 24.04 instance. The command examples in this section are based on an x86_64 architecture.
For arm64-sbsa commands, see CUDA Toolkit Downloads and select the options that apply to your distribution. Instructions appear after you've made your final selection.
Prerequisite Before installing the toolkit and drivers, run the following command to ensure that you have the correct version of the kernel headers and development packages.
$ apt install linux-headers-$(uname -r)
Download the toolkit and drivers Choose the type of installation to use for your instance, and follow the associated steps.
RPM local installation You can follow these instructions to download the CUDA toolkit installer repository bundle to your instance, then extract and register the specified bundle.
To view instructions on the NVIDIA developer website, see CUDA Toolkit Downloads.
$ wget https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2404/ x86_64/cuda-ubuntu2404.pin $ sudo mv cuda-ubuntu2404.pin /etc/apt/preferences.d/cuda-repository-pin-600

$ wget https://developer.download.nvidia.com/compute/cuda/13.0.0/ local_installers/cuda-repo-ubuntu2404-13-0-local_13.0.0-580.65.06-1_amd64.deb $ sudo dpkg -i cuda-repo-ubuntu2404-13-0-local_13.0.0-580.65.06-1_amd64.deb $ sudo cp /var/cuda-repo-ubuntu2404-13-0-local/cuda-*-keyring.gpg /usr/share/ keyrings/ RPM network installation You can follow these instructions to register the CUDA repository with the package manager on your instance. When you run the install steps, the package manager downloads only the packages that are required.
To view instructions on the NVIDIA developer website, see CUDA Toolkit Downloads.
$ wget https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2404/x86_64/ cuda-keyring_1.1-1_all.deb $ sudo dpkg -i cuda-keyring_1.1-1_all.deb Remaining steps are the same for both local and network installation.
1. Complete the CUDA toolkit install $ sudo apt update $ sudo apt install cuda-toolkit -y
2. Install the open kernel module variant of the driver $ sudo apt install nvidia-open -y
3. Install GPUDirect Storage and Fabric Manager $ sudo apt install nvidia-gds -y $ sudo apt install nvidia-fabricmanager -y
4. Enable Fabric Manager and driver persistence $ sudo systemctl enable nvidia-fabricmanager $ sudo systemctl enable nvidia-persistenced
5. (P6-B200 and P6-B300 only) These instance types require installation and configuration of additional packages that come bundled with the NVIDIA CUDA Toolkit.

1. Install the latest InfiniBand-specific device driver and diagnostic utilities.
$ sudo apt install linux-modules-extra-$(uname -r) -y $ sudo apt install infiniband-diags -y
2. Install NVIDIA Link Subnet Manager.
$ sudo apt install nvlsm -y
6. Reboot the instance sudo reboot
7. Update your path and add the following environment variable.
$ export PATH=${PATH}:/usr/local/cuda-13.0/bin $ export LD_LIBRARY_PATH=${LD_LIBRARY_PATH}:/usr/local/cuda-13.0/lib64
##### Windows operating systems To install the NVIDIA driver on Windows, follow these steps:
1. Open the folder where you downloaded the driver and launch the installation file. Follow the instructions to install the driver and reboot your instance as required.
2. Disable the display adapter named Microsoft Basic Display Adapter that is marked with a warning icon using Device Manager. Install these Windows features: Media Foundation and Quality Windows Audio Video Experience.
Important Don't disable the display adapter named Microsoft Remote Display Adapter. If Microsoft Remote Display Adapter is disabled your connection might be interrupted and attempts to connect to the instance after it has rebooted might fail.
3. Check Device Manager to verify that the GPU is working correctly.
4. To achieve the best performance from your GPU, complete the optimization steps in Optimize GPU settings on Amazon EC2 instances.

### Install NVIDIA GRID drivers (G7e, G6, Gr6, G6e, G6f, Gr6f, G5, G4dn, and G3 instances) instances)
These downloads are available to AWS customers only. By downloading, in order to adhere to requirements of the AWS solution referred to in the NVIDIA GRID Cloud End User License Agreement (EULA), you agree to use the downloaded software only to develop AMIs for use with the NVIDIA L4, NVIDIA L40S, NVIDIA A10G, NVIDIA Tesla T4, or NVIDIA Tesla M60 hardware.
You can use the GRID drivers to both create and use AMIs within the AWS environment. Upon installation of the software, you are bound by the terms of the NVIDIA GRID Cloud End User License Agreement. For information about the version of the NVIDIA GRID driver for your operating system, see the NVIDIA Virtual GPU (vGPU) Software on the NVIDIA website.
Considerations
- G7e instances require GRID 19.1 or later for Linux and 19.3 (581.192) or later for Windows.
- G6f and Gr6f instances require GRID 18.4 or later.
- G6e instances require GRID 17.4 or later.
- G6 and Gr6 instances require GRID 17.1 or later.
- G5 instances require GRID 13.1 or later (or GRID 12.4 or later).
- G3 instances require AWS provided DNS resolution for GRID licensing to work.
- IMDSv2 is only supported with NVIDIA driver version 14.0 or greater.
- For Windows instances, if you launch your instance from a custom Windows AMI, the AMI must be a standardized image created with Windows Sysprep to ensure that the GRID driver works. For more information, see Create an Amazon EC2 AMI using Windows Sysprep.
- GRID 17.0 and later do not support Windows Server 2019.
- GRID 14.2 and later do not support Windows Server 2016.
- GRID 17.0 and later is not supported with G3 instances.
- For Linux instances, you might need to install or update packages, such as gcc, if the NVIDIA installer fails with an error message. The specifics depend on the versions of the operating system and the kernel. For more information, see the NVIDIA Enterprise Support Portal.

### Prerequisites
- (Linux) Verify that the AWS CLI is installed on your instance and configured with default credentials. For more information, see Installing the AWS CLI in the AWS Command Line Interface User Guide.
- (Windows) Configure default credentials for the AWS Tools for Windows PowerShell on your instance. For more information, see Getting started with the AWS Tools for Windows PowerShell in the AWS Tools for PowerShell User Guide.
- Your user or role must have the permissions granted that contains the AmazonS3ReadOnlyAccess policy.
#### Amazon Linux 2023 To install the NVIDIA GRID driver on your instance
1. Connect to your instance. Update your package cache and get the package updates for your instance.
[ec2-user ~]$ sudo dnf update -y
2. Install gcc and make, if they are not already installed.
[ec2-user ~]$ sudo dnf install gcc make
3. Reboot your instance to load the latest kernel version.
[ec2-user ~]$ sudo reboot
4. Reconnect to your instance after it has rebooted.
5. Install the kernel headers packages.
[ec2-user ~]$ sudo dnf install -y kernel-devel kernel-modules-extra
6. Download the GRID driver installation utility using the following command:
[ec2-user ~]$ aws s3 cp --recursive s3://ec2-linux-nvidia-drivers/latest/ .
Multiple versions of the GRID driver are stored in this bucket. You can see all of the available versions using the following command.

[ec2-user ~]$ aws s3 ls --recursive s3://ec2-linux-nvidia-drivers/
7. Add permissions to run the driver installation utility using the following command.
[ec2-user ~]$ chmod +x NVIDIA-Linux-x86_64*.run
8. Run the self-install script as follows to install the GRID driver that you downloaded. For example:
[ec2-user ~]$ sudo /bin/sh ./NVIDIA-Linux-x86_64*.run When prompted, accept the license agreement and specify the installation options as required (you can accept the default options).
9. Confirm that the driver is functional. The response for the following command lists the installed version of the NVIDIA driver and details about the GPUs.
[ec2-user ~]$ nvidia-smi -q | head
10. If you are using NVIDIA vGPU software version 14.x or greater on the G4dn, G5, or G5g instances, disable GSP with the following commands. For more information about why this is required, see the NVIDIA documentation.
[ec2-user ~]$ sudo touch /etc/modprobe.d/nvidia.conf [ec2-user ~]$ echo "options nvidia NVreg_EnableGpuFirmware=0" | sudo tee --append / etc/modprobe.d/nvidia.conf
11. Reboot the instance.
[ec2-user ~]$ sudo reboot
12. (Optional) Depending on your use case, you might complete the following optional steps. If you do not require this functionality, do not complete these steps. a.
To help take advantage of the four displays of up to 4K resolution, set up the high- performance display protocol Amazon DCV. b.
NVIDIA Quadro Virtual Workstation mode is enabled by default. To activate GRID Virtual Applications for RDSH Application hosting capabilities, complete the GRID Virtual

Application activation steps in Activate NVIDIA GRID Virtual Applications on your Amazon EC2 GPU-based instances.
#### Amazon Linux 2 To install the NVIDIA GRID driver on your instance
1. Connect to your instance. Update your package cache and get the package updates for your instance.
[ec2-user ~]$ sudo yum update -y
2. Install gcc and make, if they are not already installed.
[ec2-user ~]$ sudo yum install gcc make
3. Reboot your instance to load the latest kernel version.
[ec2-user ~]$ sudo reboot
4. Reconnect to your instance after it has rebooted.
5. Install the kernel headers package for the version of the kernel that is running.
[ec2-user ~]$ sudo yum install -y kernel-devel-$(uname -r)
6. Download the GRID driver installation utility using the following command:
[ec2-user ~]$ aws s3 cp --recursive s3://ec2-linux-nvidia-drivers/latest/ .
Multiple versions of the GRID driver are stored in this bucket. You can see all of the available versions using the following command.
[ec2-user ~]$ aws s3 ls --recursive s3://ec2-linux-nvidia-drivers/
7. Add permissions to run the driver installation utility using the following command.
[ec2-user ~]$ chmod +x NVIDIA-Linux-x86_64*.run
8. Run the self-install script as follows to install the GRID driver that you downloaded. For example:

[ec2-user ~]$ sudo /bin/sh ./NVIDIA-Linux-x86_64*.run If you are using Amazon Linux 2 with kernel version 5.10, use the following command to install the GRID driver.
[ec2-user ~]$ sudo CC=/usr/bin/gcc10-cc ./NVIDIA-Linux-x86_64*.run When prompted, accept the license agreement and specify the installation options as required (you can accept the default options).
9. Confirm that the driver is functional. The response for the following command lists the installed version of the NVIDIA driver and details about the GPUs.
[ec2-user ~]$ nvidia-smi -q | head
10. If you are using NVIDIA vGPU software version 14.x or greater on the G4dn, G5, or G5g instances, disable GSP with the following commands. For more information about why this is required, see the NVIDIA documentation.
[ec2-user ~]$ sudo touch /etc/modprobe.d/nvidia.conf [ec2-user ~]$ echo "options nvidia NVreg_EnableGpuFirmware=0" | sudo tee --append / etc/modprobe.d/nvidia.conf
11. Reboot the instance.
[ec2-user ~]$ sudo reboot
12. (Optional) Depending on your use case, you might complete the following optional steps. If you do not require this functionality, do not complete these steps. a.
To help take advantage of the four displays of up to 4K resolution, set up the high- performance display protocol Amazon DCV. b.
NVIDIA Quadro Virtual Workstation mode is enabled by default. To activate GRID Virtual Applications for RDSH Application hosting capabilities, complete the GRID Virtual Application activation steps in Activate NVIDIA GRID Virtual Applications on your Amazon EC2 GPU-based instances.

#### CentOS 7 and Red Hat Enterprise Linux 7 To install the NVIDIA GRID driver on your instance
1. Connect to your instance. Update your package cache and get the package updates for your instance.
[ec2-user ~]$ sudo yum update -y
2. Install gcc and make, if they are not already installed.
[ec2-user ~]$ sudo yum install -y gcc make
3. Reboot your instance to load the latest kernel version.
[ec2-user ~]$ sudo reboot
4. Reconnect to your instance after it has rebooted.
5. Install the kernel headers package for the version of the kernel that you are running.
[ec2-user ~]$ sudo yum install -y kernel-devel-$(uname -r)
6. Disable the nouveau open source driver for NVIDIA graphics cards. a.
Add nouveau to the /etc/modprobe.d/blacklist.conf blacklist file. Copy the following code block and paste it into a terminal.
[ec2-user ~]$ cat << EOF | sudo tee --append /etc/modprobe.d/blacklist.conf blacklist vga16fb blacklist nouveau blacklist rivafb blacklist nvidiafb blacklist rivatv EOF b.
Edit the /etc/default/grub file and add the following line:
GRUB_CMDLINE_LINUX="rdblacklist=nouveau" c.
Rebuild the Grub configuration.

[ec2-user ~]$ sudo grub2-mkconfig -o /boot/grub2/grub.cfg
7. Download the GRID driver installation utility using the following command:
[ec2-user ~]$ aws s3 cp --recursive s3://ec2-linux-nvidia-drivers/latest/ .
Multiple versions of the GRID driver are stored in this bucket. You can see all of the available versions using the following command.
[ec2-user ~]$ aws s3 ls --recursive s3://ec2-linux-nvidia-drivers/
8. Add permissions to run the driver installation utility using the following command.
[ec2-user ~]$ chmod +x NVIDIA-Linux-x86_64*.run
9. Run the self-install script as follows to install the GRID driver that you downloaded. For example:
[ec2-user ~]$ sudo /bin/sh ./NVIDIA-Linux-x86_64*.run When prompted, accept the license agreement and specify the installation options as required (you can accept the default options).
10. Confirm that the driver is functional. The response for the following command lists the installed version of the NVIDIA driver and details about the GPUs.
[ec2-user ~]$ nvidia-smi -q | head
11. If you are using NVIDIA vGPU software version 14.x or greater on the G4dn, G5, or G5g instances, disable GSP with the following commands. For more information about why this is required, see the NVIDIA documentation.
[ec2-user ~]$ sudo touch /etc/modprobe.d/nvidia.conf [ec2-user ~]$ echo "options nvidia NVreg_EnableGpuFirmware=0" | sudo tee --append / etc/modprobe.d/nvidia.conf
12. Reboot the instance.

[ec2-user ~]$ sudo reboot
13. (Optional) Depending on your use case, you might complete the following optional steps. If you do not require this functionality, do not complete these steps. a.
To help take advantage of the four displays of up to 4K resolution, set up the high- performance display protocol Amazon DCV. b.
NVIDIA Quadro Virtual Workstation mode is enabled by default. To activate GRID Virtual Applications for RDSH Application hosting capabilities, complete the GRID Virtual Application activation steps in Activate NVIDIA GRID Virtual Applications on your Amazon EC2 GPU-based instances. c.
Install the GUI desktop/workstation package.
[ec2-user ~]$ sudo yum groupinstall -y "Server with GUI"
#### CentOS Stream 8 and Red Hat Enterprise Linux 8 To install the NVIDIA GRID driver on your instance
1. Connect to your instance. Update your package cache and get the package updates for your instance.
[ec2-user ~]$ sudo yum update -y
2. Install gcc and make, if they are not already installed.
[ec2-user ~]$ sudo yum install -y gcc make
3. Reboot your instance to load the latest kernel version.
[ec2-user ~]$ sudo reboot
4. Reconnect to your instance after it has rebooted.
5. Install the kernel headers package for the version of the kernel that you are running.
[ec2-user ~]$ sudo dnf install -y elfutils-libelf-devel libglvnd-devel kernel- devel-$(uname -r)

6. Download the GRID driver installation utility using the following command:
[ec2-user ~]$ aws s3 cp --recursive s3://ec2-linux-nvidia-drivers/latest/ .
Multiple versions of the GRID driver are stored in this bucket. You can see all of the available versions using the following command.
[ec2-user ~]$ aws s3 ls --recursive s3://ec2-linux-nvidia-drivers/
7. Add permissions to run the driver installation utility using the following command.
[ec2-user ~]$ chmod +x NVIDIA-Linux-x86_64*.run
8. Run the self-install script as follows to install the GRID driver that you downloaded. For example:
[ec2-user ~]$ sudo /bin/sh ./NVIDIA-Linux-x86_64*.run When prompted, accept the license agreement and specify the installation options as required (you can accept the default options).
9. Confirm that the driver is functional. The response for the following command lists the installed version of the NVIDIA driver and details about the GPUs.
[ec2-user ~]$ nvidia-smi -q | head
10. If you are using NVIDIA vGPU software version 14.x or greater on the G4dn, G5, or G5g instances, disable GSP with the following commands. For more information about why this is required, see the NVIDIA documentation.
[ec2-user ~]$ sudo touch /etc/modprobe.d/nvidia.conf [ec2-user ~]$ echo "options nvidia NVreg_EnableGpuFirmware=0" | sudo tee --append / etc/modprobe.d/nvidia.conf
11. Reboot the instance.
[ec2-user ~]$ sudo reboot

12. (Optional) Depending on your use case, you might complete the following optional steps. If you do not require this functionality, do not complete these steps. a.
To help take advantage of the four displays of up to 4K resolution, set up the high- performance display protocol Amazon DCV. b.
NVIDIA Quadro Virtual Workstation mode is enabled by default. To activate GRID Virtual Applications for RDSH Application hosting capabilities, complete the GRID Virtual Application activation steps in Activate NVIDIA GRID Virtual Applications on your Amazon EC2 GPU-based instances. c.
Install the GUI workstation package.
[ec2-user ~]$ sudo dnf groupinstall -y workstation
#### Rocky Linux 8 To install the NVIDIA GRID driver on your Linux instance
1. Connect to your instance. Update your package cache and get the package updates for your instance.
[ec2-user ~]$ sudo yum update -y
2. Install gcc and make, if they are not already installed.
[ec2-user ~]$ sudo yum install -y gcc make
3. Reboot your instance to load the latest kernel version.
[ec2-user ~]$ sudo reboot
4. Reconnect to your instance after it has rebooted.
5. Install the kernel headers package for the version of the kernel that you are running.
[ec2-user ~]$ sudo dnf install -y elfutils-libelf-devel libglvnd-devel kernel- devel-$(uname -r)
6. Download the GRID driver installation utility using the following command:

[ec2-user ~]$ aws s3 cp --recursive s3://ec2-linux-nvidia-drivers/latest/ .
Multiple versions of the GRID driver are stored in this bucket. You can see all of the available versions using the following command.
[ec2-user ~]$ aws s3 ls --recursive s3://ec2-linux-nvidia-drivers/
7. Add permissions to run the driver installation utility using the following command.
[ec2-user ~]$ chmod +x NVIDIA-Linux-x86_64*.run
8. Run the self-install script as follows to install the GRID driver that you downloaded. For example:
[ec2-user ~]$ sudo /bin/sh ./NVIDIA-Linux-x86_64*.run When prompted, accept the license agreement and specify the installation options as required (you can accept the default options).
9. Confirm that the driver is functional. The response for the following command lists the installed version of the NVIDIA driver and details about the GPUs.
[ec2-user ~]$ nvidia-smi -q | head
10. If you are using NVIDIA vGPU software version 14.x or greater on the G4dn, G5, or G5g instances, disable GSP with the following commands. For more information about why this is required, see the NVIDIA documentation.
[ec2-user ~]$ sudo touch /etc/modprobe.d/nvidia.conf [ec2-user ~]$ echo "options nvidia NVreg_EnableGpuFirmware=0" | sudo tee --append / etc/modprobe.d/nvidia.conf
11. Reboot the instance.
[ec2-user ~]$ sudo reboot
12. (Optional) Depending on your use case, you might complete the following optional steps. If you do not require this functionality, do not complete these steps.

a.
To help take advantage of the four displays of up to 4K resolution, set up the high- performance display protocol Amazon DCV. b.
NVIDIA Quadro Virtual Workstation mode is enabled by default. To activate GRID Virtual Applications for RDSH Application hosting capabilities, complete the GRID Virtual Application activation steps in Activate NVIDIA GRID Virtual Applications on your Amazon EC2 GPU-based instances.
#### Ubuntu and Debian To install the NVIDIA GRID driver on your instance
1. Connect to your instance. Update your package cache and get the package updates for your instance.
$ sudo apt-get update -y
2. Install gcc and make, if they are not already installed.
$ sudo apt-get install -y gcc make
3. (Ubuntu) Upgrade the linux-aws package to receive the latest version.
$ sudo apt-get upgrade -y linux-aws (Debian) Upgrade package to receive the latest version.
$ sudo apt-get upgrade -y
4. Reboot your instance to load the latest kernel version.
$ sudo reboot
5. Reconnect to your instance after it has rebooted.
6. Install the kernel headers package for the version of the kernel you are currently running.
$ sudo apt-get install -y linux-headers-$(uname -r) linux-modules-extra-$(uname -r)
7. Disable the nouveau open source driver for NVIDIA graphics cards.

a.
Add nouveau to the /etc/modprobe.d/blacklist.conf blacklist file. Copy the following code block and paste it into a terminal.
$ cat << EOF | sudo tee --append /etc/modprobe.d/blacklist.conf blacklist vga16fb blacklist nouveau blacklist rivafb blacklist nvidiafb blacklist rivatv EOF b.
Edit the /etc/default/grub file and add the following line:
GRUB_CMDLINE_LINUX="rdblacklist=nouveau" c.
Rebuild the Grub configuration.
$ sudo update-grub
8. Download the GRID driver installation utility using the following command:
$ aws s3 cp --recursive s3://ec2-linux-nvidia-drivers/latest/ .
Multiple versions of the GRID driver are stored in this bucket. You can see all of the available versions using the following command.
$ aws s3 ls --recursive s3://ec2-linux-nvidia-drivers/
9. Add permissions to run the driver installation utility using the following command.
$ chmod +x NVIDIA-Linux-x86_64*.run
10. Run the self-install script as follows to install the GRID driver that you downloaded. For example:
$ sudo /bin/sh ./NVIDIA-Linux-x86_64*.run When prompted, accept the license agreement and specify the installation options as required (you can accept the default options).

11. Confirm that the driver is functional. The response for the following command lists the installed version of the NVIDIA driver and details about the GPUs.
$ nvidia-smi -q | head
12. If you are using NVIDIA vGPU software version 14.x or greater on the G4dn, G5, or G5g instances, disable GSP with the following commands. For more information about why this is required, see the NVIDIA documentation.
$ sudo touch /etc/modprobe.d/nvidia.conf $ echo "options nvidia NVreg_EnableGpuFirmware=0" | sudo tee --append /etc/ modprobe.d/nvidia.conf
13. Reboot the instance.
$ sudo reboot
14. (Optional) Depending on your use case, you might complete the following optional steps. If you do not require this functionality, do not complete these steps. a.
To help take advantage of the four displays of up to 4K resolution, set up the high- performance display protocol Amazon DCV. b.
NVIDIA Quadro Virtual Workstation mode is enabled by default. To activate GRID Virtual Applications for RDSH Application hosting capabilities, complete the GRID Virtual Application activation steps in Activate NVIDIA GRID Virtual Applications on your Amazon EC2 GPU-based instances. c.
Install the GUI desktop/workstation package.
$ sudo apt-get install -y lightdm ubuntu-desktop
#### Windows operating systems To install the NVIDIA GRID driver on your Windows instance
1. Connect to your Windows instance and open a PowerShell window.
2. Download the drivers and the NVIDIA GRID Cloud End User License Agreement from Amazon S3 to your desktop using the following PowerShell commands.

$Bucket = "ec2-windows-nvidia-drivers"
$KeyPrefix = "latest"
$LocalPath = "$home\Desktop\NVIDIA"
$Objects = Get-S3Object -BucketName $Bucket -KeyPrefix $KeyPrefix -Region us-east-1 foreach ($Object in $Objects) { $LocalFileName = $Object.Key if ($LocalFileName -ne '' -and $Object.Size -ne 0) { $LocalFilePath = Join-Path $LocalPath $LocalFileName Copy-S3Object -BucketName $Bucket -Key $Object.Key -LocalFile $LocalFilePath - Region us-east-1 } } Multiple versions of the NVIDIA GRID driver are stored in this bucket. You can download all of the available Windows versions in the bucket by removing the -KeyPrefix $KeyPrefix option. For information about the version of the NVIDIA GRID driver for your operating system, see the NVIDIA Virtual GPU (vGPU) Software on the NVIDIA website.
Starting with GRID version 11.0, you can use the drivers under latest for both G3 and G4dn instances. We will not add versions later than 11.0 to g4/latest, but will keep version 11.0 and the earlier versions specific to G4dn under g4/latest.
G5 instances require GRID 13.1 or later (or GRID 12.4 or later).
3. Navigate to the desktop and double-click the installation file to launch it (choose the driver version that corresponds to your instance OS version). Follow the instructions to install the driver and reboot your instance as required. To verify that the GPU is working properly, check Device Manager.
4. (Optional) Use the following command to disable the licensing page in the control panel to prevent users from accidentally changing the product type (NVIDIA GRID Virtual Workstation is enabled by default). For more information, see the GRID Licensing User Guide.
PowerShell Run the following PowerShell commands to create the registry value to disable the licensing page in the control panel. The AWS Tools for PowerShell in AWS Windows AMIs defaults to the 32-bit version and this command fails. Instead, use the 64-bit version of PowerShell included with the operating system.

New-Item -Path "HKLM:\SOFTWARE\NVIDIA Corporation\Global" -Name GridLicensing New-ItemProperty -Path "HKLM:\SOFTWARE\NVIDIA Corporation\Global\GridLicensing" - Name "NvCplDisableManageLicensePage" -PropertyType "DWord" -Value "1"
Command Prompt Run the following registry command to create the registry value to disable the licensing page in the control panel. You can run it using the Command Prompt window or a 64-bit version of PowerShell. reg add "HKLM\SOFTWARE\NVIDIA Corporation\Global\GridLicensing" /v NvCplDisableManageLicensePage /t REG_DWORD /d 1
5. (Optional) Depending on your use case, you might complete the following optional steps. If you do not require this functionality, do not complete these steps. a.
To help take advantage of the four displays of up to 4K resolution, set up the high- performance display protocol, Amazon DCV. b.
NVIDIA Quadro Virtual Workstation mode is enabled by default. To activate GRID Virtual Applications for RDSH Application hosting capabilities, complete the GRID Virtual Application activation steps in Activate NVIDIA GRID Virtual Applications on your Amazon EC2 GPU-based instances.
### Install NVIDIA gaming drivers (G7e, G6, G6e, G5, and G4dn instances)
These drivers are available to AWS customers only. By downloading them, you agree to use the downloaded software only to develop AMIs for use with the RTX PRO 6000 Blackwell, NVIDIA L4, NVIDIA L40S, NVIDIA A10G, NVIDIA Tesla T4, or NVIDIA Tesla M60 hardware. You can use the GRID drivers to both create and use AMIs within the AWS environment. Upon installation of the software, you are bound by the terms of the NVIDIA GRID Cloud End User License Agreement.
Considerations
- G3 instances require AWS provided DNS resolution for GRID licensing to work.
- IMDSv2 is only supported with NVIDIA driver version 495.x or greater.

Prerequisites
- (Linux) Verify that the AWS CLI is installed on your instance and configured with default credentials. For more information, see Installing the AWS CLI in the AWS Command Line Interface User Guide.
- Your user or role must have the permissions granted that contains the AmazonS3ReadOnlyAccess policy.
#### Amazon Linux 2023 To install the NVIDIA gaming driver on your instance
1. Connect to your instance. Update your package cache and get the package updates for your instance.
[ec2-user ~]$ sudo dnf update -y
2. Install gcc and make, if they are not already installed.
[ec2-user ~]$ sudo dnf install gcc make
3. Reboot your instance to load the latest kernel version.
[ec2-user ~]$ sudo reboot
4. Reconnect to your instance after it is rebooted.
5. Install the kernel headers packages.
[ec2-user ~]$ sudo dnf install -y kernel-devel kernel-modules-extra kernel-devel- $(uname -r) kernel-headers-$(uname -r) dkms
6. Download the gaming driver installation utility using the following command:
[ec2-user ~]$ aws s3 cp --recursive s3://nvidia-gaming/linux/latest/ .
Multiple versions of the gaming driver are stored in this bucket. You can see all of the available versions using the following command:
[ec2-user ~]$ aws s3 ls --recursive s3://nvidia-gaming/linux/

7. Extract the gaming driver installation utility from the downloaded .zip archive.
[ec2-user ~]$ unzip latest-driver-name.zip -d nvidia-drivers
8. Add permissions to run the driver installation utility using the following command:
[ec2-user ~]$ chmod +x nvidia-drivers/NVIDIA-Linux-x86_64*-grid.run
9. Run the installer using the following command:
[ec2-user ~]$ sudo ./nvidia-drivers/NVIDIA-Linux-x86_64*.run When prompted, accept the license agreement and specify the installation options as required (you can accept the default options).
10. Use the following command to create the required configuration file.
[ec2-user ~]$ cat << EOF | sudo tee -a /etc/nvidia/gridd.conf vGamingMarketplace=2 EOF
11. Use the following command to download and rename the certification file.
- For version 460.39 or later:
[ec2-user ~]$ sudo curl -o /etc/nvidia/GridSwCert.txt "https://nvidia- gaming.s3.amazonaws.com/GridSwCert-Archive/GridSwCertLinux_2024_02_22.cert"
- For version 440.68 to 445.48:
[ec2-user ~]$ sudo curl -o /etc/nvidia/GridSwCert.txt "https://nvidia- gaming.s3.amazonaws.com/GridSwCert-Archive/GridSwCert-Linux_2020_04.cert"
- For earlier versions:
[ec2-user ~]$ sudo curl -o /etc/nvidia/GridSwCert.txt "https://nvidia- gaming.s3.amazonaws.com/GridSwCert-Archive/GridSwCert-Linux_2019_09.cert"
12. If you are using NVIDIA driver version 510.x or greater on the G4dn, G5, or G5g instances, disable GSP with the following commands. For more information about why this is required, see the NVIDIA documentation.

[ec2-user ~]$ sudo touch /etc/modprobe.d/nvidia.conf [ec2-user ~]$ echo "options nvidia NVreg_EnableGpuFirmware=0" | sudo tee --append / etc/modprobe.d/nvidia.conf
13. Reboot the instance.
[ec2-user ~]$ sudo reboot
14. Verify the NVIDIA Gaming license using the following command.
[ec2-user ~]$ nvidia-smi.exe -q In the output, search for vGPU Software Licensed Product.
15. (Optional) To help take advantage of a single display of up to 4K resolution, set up the high- performance display protocol Amazon DCV.
#### Amazon Linux 2 To install the NVIDIA gaming driver on your instance
1. Connect to your instance. Update your package cache and get the package updates for your instance.
[ec2-user ~]$ sudo yum update -y
2. Install gcc and make, if they are not already installed.
[ec2-user ~]$ sudo yum install gcc make
3. Reboot your instance to load the latest kernel version.
[ec2-user ~]$ sudo reboot
4. Reconnect to your instance after it is rebooted.
5. Install the kernel headers package for the version of the kernel you are currently running.

[ec2-user ~]$ sudo yum install -y kernel-devel-$(uname -r)
6. Download the gaming driver installation utility using the following command:
[ec2-user ~]$ aws s3 cp --recursive s3://nvidia-gaming/linux/latest/ .
Multiple versions of the gaming driver are stored in this bucket. You can see all of the available versions using the following command:
[ec2-user ~]$ aws s3 ls --recursive s3://nvidia-gaming/linux/
7. Extract the gaming driver installation utility from the downloaded .zip archive.
[ec2-user ~]$ unzip latest-driver-name.zip -d nvidia-drivers
8. Add permissions to run the driver installation utility using the following command:
[ec2-user ~]$ chmod +x nvidia-drivers/NVIDIA-Linux-x86_64*-grid.run
9. Run the installer using the following command:
[ec2-user ~]$ sudo ./nvidia-drivers/NVIDIA-Linux-x86_64*.run If you are using Amazon Linux 2 with kernel version 5.10, use the following command to install the NVIDIA gaming drivers.
[ec2-user ~]$ sudo CC=/usr/bin/gcc10-cc ./NVIDIA-Linux-x86_64*.run When prompted, accept the license agreement and specify the installation options as required (you can accept the default options).
10. Use the following command to create the required configuration file.
[ec2-user ~]$ cat << EOF | sudo tee -a /etc/nvidia/gridd.conf vGamingMarketplace=2 EOF
11. Use the following command to download and rename the certification file.
- For version 460.39 or later:

[ec2-user ~]$ sudo curl -o /etc/nvidia/GridSwCert.txt "https://nvidia- gaming.s3.amazonaws.com/GridSwCert-Archive/GridSwCertLinux_2024_02_22.cert"
- For version 440.68 to 445.48:
[ec2-user ~]$ sudo curl -o /etc/nvidia/GridSwCert.txt "https://nvidia- gaming.s3.amazonaws.com/GridSwCert-Archive/GridSwCert-Linux_2020_04.cert"
- For earlier versions:
[ec2-user ~]$ sudo curl -o /etc/nvidia/GridSwCert.txt "https://nvidia- gaming.s3.amazonaws.com/GridSwCert-Archive/GridSwCert-Linux_2019_09.cert"
12. If you are using NVIDIA driver version 510.x or greater on the G4dn, G5, or G5g instances, disable GSP with the following commands. For more information about why this is required, see the NVIDIA documentation.
[ec2-user ~]$ sudo touch /etc/modprobe.d/nvidia.conf [ec2-user ~]$ echo "options nvidia NVreg_EnableGpuFirmware=0" | sudo tee --append / etc/modprobe.d/nvidia.conf
13. Reboot the instance.
[ec2-user ~]$ sudo reboot
14. Verify the NVIDIA Gaming license using the following command.
[ec2-user ~]$ nvidia-smi.exe -q In the output, search for vGPU Software Licensed Product.
15. (Optional) To help take advantage of a single display of up to 4K resolution, set up the high- performance display protocol Amazon DCV.

#### CentOS 7 and Red Hat Enterprise Linux 7 To install the NVIDIA gaming driver on your instance
1. Connect to your Linux instance. Install gcc and make, if they are not already installed.
[ec2-user ~]$ sudo yum install -y gcc make
2. Update your package cache and get the package updates for your instance.
[ec2-user ~]$ sudo yum update -y
3. Reboot your instance to load the latest kernel version.
[ec2-user ~]$ sudo reboot
4. Reconnect to your instance after it has rebooted.
5. Install the kernel headers package for the version of the kernel you are currently running.
[ec2-user ~]$ sudo yum install -y unzip kernel-devel-$(uname -r)
6. Disable the nouveau open source driver for NVIDIA graphics cards. a.
Add nouveau to the /etc/modprobe.d/blacklist.conf blacklist file. Copy the following code block and paste it into a terminal.
[ec2-user ~]$ cat << EOF | sudo tee --append /etc/modprobe.d/blacklist.conf blacklist vga16fb blacklist nouveau blacklist rivafb blacklist nvidiafb blacklist rivatv EOF b.
Edit the /etc/default/grub file and add the following line:
GRUB_CMDLINE_LINUX="rdblacklist=nouveau" c.
Rebuild the Grub configuration.
[ec2-user ~]$ sudo grub2-mkconfig -o /boot/grub2/grub.cfg

7. Download the gaming driver installation utility using the following command:
[ec2-user ~]$ aws s3 cp --recursive s3://nvidia-gaming/linux/latest/ .
Multiple versions of the gaming driver are stored in this bucket. You can see all of the available versions using the following command:
[ec2-user ~]$ aws s3 ls --recursive s3://nvidia-gaming/linux/
8. Extract the gaming driver installation utility from the downloaded .zip archive.
[ec2-user ~]$ unzip *Gaming-Linux-Guest-Drivers.zip -d nvidia-drivers
9. Add permissions to run the driver installation utility using the following command:
[ec2-user ~]$ chmod +x nvidia-drivers/NVIDIA-Linux-x86_64*-grid.run
10. Run the installer using the following command:
[ec2-user ~]$ sudo nvidia-drivers/NVIDIA-Linux-x86_64*.run When prompted, accept the license agreement and specify the installation options as required (you can accept the default options).
11. Use the following command to create the required configuration file.
[ec2-user ~]$ cat << EOF | sudo tee -a /etc/nvidia/gridd.conf vGamingMarketplace=2 EOF
12. Use the following command to download and rename the certification file.
- For version 460.39 or later:
[ec2-user ~]$ sudo curl -o /etc/nvidia/GridSwCert.txt "https://nvidia- gaming.s3.amazonaws.com/GridSwCert-Archive/GridSwCertLinux_2024_02_22.cert"
- For version 440.68 to 445.48:
[ec2-user ~]$ sudo curl -o /etc/nvidia/GridSwCert.txt "https://nvidia- gaming.s3.amazonaws.com/GridSwCert-Archive/GridSwCert-Linux_2020_04.cert"

- For earlier versions:
[ec2-user ~]$ sudo curl -o /etc/nvidia/GridSwCert.txt "https://nvidia- gaming.s3.amazonaws.com/GridSwCert-Archive/GridSwCert-Linux_2019_09.cert"
13. If you are using NVIDIA driver version 510.x or greater on the G4dn, G5, or G5g instances, disable GSP with the following commands. For more information about why this is required, see the NVIDIA documentation.
[ec2-user ~]$ sudo touch /etc/modprobe.d/nvidia.conf [ec2-user ~]$ echo "options nvidia NVreg_EnableGpuFirmware=0" | sudo tee --append / etc/modprobe.d/nvidia.conf
14. Reboot the instance.
[ec2-user ~]$ sudo reboot
15. (Optional) To help take advantage of a single display of up to 4K resolution, set up the high- performance display protocol Amazon DCV. If you do not require this functionality, do not complete this step.
#### CentOS Stream 8 and Red Hat Enterprise Linux 8 To install the NVIDIA gaming driver on your instance
1. Connect to your Linux instance. Install gcc and make, if they are not already installed.
[ec2-user ~]$ sudo yum install -y gcc make
2. Update your package cache and get the package updates for your instance.
[ec2-user ~]$ sudo yum update -y
3. Reboot your instance to load the latest kernel version.
[ec2-user ~]$ sudo reboot
4. Reconnect to your instance after it has rebooted.

5. Install the kernel headers package for the version of the kernel you are currently running.
[ec2-user ~]$ sudo yum install -y unzip kernel-devel-$(uname -r)
6. Download the gaming driver installation utility using the following command:
[ec2-user ~]$ aws s3 cp --recursive s3://nvidia-gaming/linux/latest/ .
Multiple versions of the gaming driver are stored in this bucket. You can see all of the available versions using the following command:
[ec2-user ~]$ aws s3 ls --recursive s3://nvidia-gaming/linux/
7. Extract the gaming driver installation utility from the downloaded .zip archive.
[ec2-user ~]$ unzip *Gaming-Linux-Guest-Drivers.zip -d nvidia-drivers
8. Add permissions to run the driver installation utility using the following command:
[ec2-user ~]$ chmod +x nvidia-drivers/NVIDIA-Linux-x86_64*-grid.run
9. Run the installer using the following command:
[ec2-user ~]$ sudo nvidia-drivers/NVIDIA-Linux-x86_64*.run When prompted, accept the license agreement and specify the installation options as required (you can accept the default options).
10. Use the following command to create the required configuration file.
[ec2-user ~]$ cat << EOF | sudo tee -a /etc/nvidia/gridd.conf vGamingMarketplace=2 EOF
11. Use the following command to download and rename the certification file.
- For version 460.39 or later:
[ec2-user ~]$ sudo curl -o /etc/nvidia/GridSwCert.txt "https://nvidia- gaming.s3.amazonaws.com/GridSwCert-Archive/GridSwCertLinux_2024_02_22.cert"
- For version 440.68 to 445.48:

[ec2-user ~]$ sudo curl -o /etc/nvidia/GridSwCert.txt "https://nvidia- gaming.s3.amazonaws.com/GridSwCert-Archive/GridSwCert-Linux_2020_04.cert"
- For earlier versions:
[ec2-user ~]$ sudo curl -o /etc/nvidia/GridSwCert.txt "https://nvidia- gaming.s3.amazonaws.com/GridSwCert-Archive/GridSwCert-Linux_2019_09.cert"
12. If you are using NVIDIA driver version 510.x or greater on the G4dn, G5, or G5g instances, disable GSP with the following commands. For more information about why this is required, see the NVIDIA documentation.
[ec2-user ~]$ sudo touch /etc/modprobe.d/nvidia.conf [ec2-user ~]$ echo "options nvidia NVreg_EnableGpuFirmware=0" | sudo tee --append / etc/modprobe.d/nvidia.conf
13. Reboot the instance.
[ec2-user ~]$ sudo reboot
14. (Optional) To help take advantage of a single display of up to 4K resolution, set up the high- performance display protocol Amazon DCV.
#### Rocky Linux 8 To install the NVIDIA gaming driver on your instance
1. Connect to your Linux instance. Install gcc and make, if they are not already installed.
[ec2-user ~]$ sudo yum install -y gcc make
2. Update your package cache and get the package updates for your instance.
[ec2-user ~]$ sudo yum update -y
3. Reboot your instance to load the latest kernel version.
[ec2-user ~]$ sudo reboot

4. Reconnect to your instance after it has rebooted.
5. Install the kernel headers package for the version of the kernel you are currently running.
[ec2-user ~]$ sudo dnf install -y unzip elfutils-libelf-devel libglvnd-devel kernel-devel-$(uname -r)
6. Download the gaming driver installation utility using the following command:
[ec2-user ~]$ aws s3 cp --recursive s3://nvidia-gaming/linux/latest/ .
Multiple versions of the gaming driver are stored in this bucket. You can see all of the available versions using the following command:
[ec2-user ~]$ aws s3 ls --recursive s3://nvidia-gaming/linux/
7. Extract the gaming driver installation utility from the downloaded .zip archive.
[ec2-user ~]$ unzip *Gaming-Linux-Guest-Drivers.zip -d nvidia-drivers
8. Add permissions to run the driver installation utility using the following command:
[ec2-user ~]$ chmod +x nvidia-drivers/NVIDIA-Linux-x86_64*-grid.run
9. Run the installer using the following command:
[ec2-user ~]$ sudo nvidia-drivers/NVIDIA-Linux-x86_64*.run When prompted, accept the license agreement and specify the installation options as required (you can accept the default options).
10. Use the following command to create the required configuration file.
[ec2-user ~]$ cat << EOF | sudo tee -a /etc/nvidia/gridd.conf vGamingMarketplace=2 EOF
11. Use the following command to download and rename the certification file.
- For version 460.39 or later:

[ec2-user ~]$ sudo curl -o /etc/nvidia/GridSwCert.txt "https://nvidia- gaming.s3.amazonaws.com/GridSwCert-Archive/GridSwCertLinux_2024_02_22.cert"
- For version 440.68 to 445.48:
[ec2-user ~]$ sudo curl -o /etc/nvidia/GridSwCert.txt "https://nvidia- gaming.s3.amazonaws.com/GridSwCert-Archive/GridSwCert-Linux_2020_04.cert"
- For earlier versions:
[ec2-user ~]$ sudo curl -o /etc/nvidia/GridSwCert.txt "https://nvidia- gaming.s3.amazonaws.com/GridSwCert-Archive/GridSwCert-Linux_2019_09.cert"
12. If you are using NVIDIA driver version 510.x or greater on the G4dn, G5, or G5g instances, disable GSP with the following commands. For more information about why this is required, see the NVIDIA documentation.
[ec2-user ~]$ sudo touch /etc/modprobe.d/nvidia.conf [ec2-user ~]$ echo "options nvidia NVreg_EnableGpuFirmware=0" | sudo tee --append / etc/modprobe.d/nvidia.conf
13. Reboot the instance.
[ec2-user ~]$ sudo reboot
14. (Optional) To help take advantage of a single display of up to 4K resolution, set up the high- performance display protocol Amazon DCV.
#### Ubuntu and Debian To install the NVIDIA gaming driver on your instance
1. Connect to your Linux instance. Install gcc and make, if they are not already installed.
$ sudo apt-get install -y gcc make build-essential
2. Update your package cache and get the package updates for your instance.

$ sudo apt-get update -y
3. Upgrade the linux-aws package to receive the latest version.
$ sudo apt-get upgrade -y linux-aws
4. Reboot your instance to load the latest kernel version.
$ sudo reboot
5. Reconnect to your instance after it has rebooted.
6. Install the kernel headers package for the version of the kernel you are currently running.
$ sudo apt install -y unzip dkms linux-headers-$(uname -r)
7. Disable the nouveau open source driver for NVIDIA graphics cards. a.
Add nouveau to the /etc/modprobe.d/blacklist.conf blacklist file. Copy the following code block and paste it into a terminal.
$ cat << EOF | sudo tee --append /etc/modprobe.d/blacklist.conf blacklist vga16fb blacklist nouveau blacklist rivafb blacklist nvidiafb blacklist rivatv EOF b.
Edit the /etc/default/grub file and add the following line:
GRUB_CMDLINE_LINUX="rdblacklist=nouveau" c.
Rebuild the Grub configuration.
$ sudo update-grub
8. Download the gaming driver installation utility using the following command:
$ aws s3 cp --recursive s3://nvidia-gaming/linux/latest/ .

Multiple versions of the gaming driver are stored in this bucket. You can see all of the available versions using the following command:
$ aws s3 ls --recursive s3://nvidia-gaming/linux/
9. Extract the gaming driver installation utility from the downloaded .zip archive.
$ unzip *Gaming-Linux-Guest-Drivers.zip -d nvidia-drivers
10. Add permissions to run the driver installation utility using the following command:
$ chmod +x nvidia-drivers/NVIDIA-Linux-x86_64*-grid.run
11. Run the installer using the following command:
$ sudo nvidia-drivers/NVIDIA-Linux-x86_64*.run When prompted, accept the license agreement and specify the installation options as required (you can accept the default options).
12. Use the following command to create the required configuration file.
$ cat << EOF | sudo tee -a /etc/nvidia/gridd.conf vGamingMarketplace=2 EOF
13. Use the following command to download and rename the certification file.
- For version 460.39 or later:
$ sudo curl -o /etc/nvidia/GridSwCert.txt "https://nvidia- gaming.s3.amazonaws.com/GridSwCert-Archive/GridSwCertLinux_2024_02_22.cert"
- For version 440.68 to 445.48:
$ sudo curl -o /etc/nvidia/GridSwCert.txt "https://nvidia- gaming.s3.amazonaws.com/GridSwCert-Archive/GridSwCert-Linux_2020_04.cert"
- For earlier versions:

$ sudo curl -o /etc/nvidia/GridSwCert.txt "https://nvidia- gaming.s3.amazonaws.com/GridSwCert-Archive/GridSwCert-Linux_2019_09.cert"
14. If you are using NVIDIA driver version 510.x or greater on the G4dn, G5, or G5g instances, disable GSP with the following commands. For more information about why this is required, see the NVIDIA documentation.
$ sudo touch /etc/modprobe.d/nvidia.conf $ echo "options nvidia NVreg_EnableGpuFirmware=0" | sudo tee --append /etc/ modprobe.d/nvidia.conf
15. Reboot the instance.
$ sudo reboot
16. (Optional) To help take advantage of a single display of up to 4K resolution, set up the high- performance display protocol Amazon DCV. If you do not require this functionality, do not complete this step.
#### Windows operating systems Before you install an NVIDIA gaming driver on your instance, you must ensure that the following prerequisites are met in addition to the considerations mentioned for all gaming drivers.
- If you launch your Windows instance using a custom Windows AMI, the AMI must be a standardized image created with Windows Sysprep to ensure that the gaming driver works. For more information, see Create an Amazon EC2 AMI using Windows Sysprep.
- Configure default credentials for the AWS Tools for Windows PowerShell on your Windows instance. For more information, see Getting Started with the AWS Tools for Windows PowerShell in the AWS Tools for PowerShell User Guide.
To install the NVIDIA gaming driver on your Windows instance
1. Connect to your Windows instance and open a PowerShell window.
2. Download and install the gaming driver using the following PowerShell commands.

$Bucket = "nvidia-gaming"
$KeyPrefix = "windows/latest"
$LocalPath = "$home\Desktop\NVIDIA"
$Objects = Get-S3Object -BucketName $Bucket -KeyPrefix $KeyPrefix -Region us-east-1 foreach ($Object in $Objects) { $LocalFileName = $Object.Key if ($LocalFileName -ne '' -and $Object.Size -ne 0) { $LocalFilePath = Join-Path $LocalPath $LocalFileName Copy-S3Object -BucketName $Bucket -Key $Object.Key -LocalFile $LocalFilePath - Region us-east-1 } } Multiple versions of the NVIDIA GRID driver are stored in this S3 bucket. You can download all of the available versions in the bucket if you change the value of the $KeyPrefix variable from "windows/latest" to "windows".
3. Navigate to the desktop and double-click the installation file to launch it (choose the driver version that corresponds to your instance OS version). Follow the instructions to install the driver and reboot your instance as required. To verify that the GPU is working properly, check Device Manager.
4. Use one of the following methods to register the driver.
Version 527.27 or above Create the following registry key with the 64-bit version of PowerShell, or the Command Prompt window. key: HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\nvlddmkm \Global name: vGamingMarketplace type: DWord value: 2 PowerShell

Run the following PowerShell command to create this registry value. The AWS Tools for PowerShell in AWS Windows AMIs defaults to the 32-bit version and this command fails.
Instead, use the 64-bit version of PowerShell included with the operating system.
New-ItemProperty -Path "HKLM:\SYSTEM\CurrentControlSet\Services\nvlddmkm\Global"
 -Name "vGamingMarketplace" -PropertyType "DWord" -Value "2"
Command Prompt Run the following registry command to create this registry value. You can run it using the Command Prompt window or a 64-bit version of PowerShell. reg add "HKLM\SYSTEM\CurrentControlSet\Services\nvlddmkm\Global" /v vGamingMarketplace /t REG_DWORD /d 2 Earlier versions Create the following registry key with the 64-bit version of PowerShell, or the Command Prompt window. key: HKEY_LOCAL_MACHINE\SOFTWARE\NVIDIA Corporation\Global name: vGamingMarketplace type: DWord value: 2 PowerShell Run the following PowerShell command to create this registry value. The AWS Tools for PowerShell in AWS Windows AMIs defaults to the 32-bit version and this command fails.
Instead, use the 64-bit version of PowerShell included with the operating system.
New-ItemProperty -Path "HKLM:\SOFTWARE\NVIDIA Corporation\Global" -Name "vGamingMarketplace" -PropertyType "DWord" -Value "2"
Command Prompt

Run the following registry command to create this registry key with the Command Prompt window. You can also use this command in the 64-bit version of PowerShell. reg add "HKLM\SOFTWARE\NVIDIA Corporation\Global" /v vGamingMarketplace /t REG_DWORD /d 2
5. Run the following command in PowerShell. This downloads the certification file, renames the file GridSwCert.txt, and moves the file to the Public Documents folder on your system drive. Typically, the folder path is C:\Users\Public\Documents.
- For version 460.39 or later:
Invoke-WebRequest -Uri "https://nvidia-gaming.s3.amazonaws.com/GridSwCert- Archive/GridSwCertWindows_2024_02_22.cert" -OutFile "$Env:PUBLIC\Documents \GridSwCert.txt"
- For version 445.87:
Invoke-WebRequest -Uri "https://nvidia-gaming.s3.amazonaws.com/GridSwCert- Archive/GridSwCert-Windows_2020_04.cert" -OutFile "$Env:PUBLIC\Documents \GridSwCert.txt"
- For earlier versions:
Invoke-WebRequest -Uri "https://nvidia-gaming.s3.amazonaws.com/GridSwCert- Archive/GridSwCert-Windows_2019_09.cert" -OutFile "$Env:PUBLIC\Documents \GridSwCert.txt"
If you receive an error when downloading the file, and you are using Windows Server 2016 or earlier, TLS 1.2 might need to be enabled for your PowerShell terminal. You can enable TLS 1.2 for the current PowerShell session with the following command and then try again:
[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12
6. Reboot your instance.
7. Locate the nvidia-smi.exe file on the instance.
Get-ChildItem -Path C:\ -Recurse -Filter "nvidia-smi.exe"

Verify the NVIDIA Gaming license using the following command. Replace path with the name of the folder in the output from the previous command.
C:\Windows\System32\DriverStore\FileRepository\path\nvidia-smi.exe -q The output should be similar to the following. vGPU Software Licensed Product Product Name              : NVIDIA Cloud Gaming License Status            : Licensed (Expiry: N/A)
8. (Optional) To help take advantage of the single display of up to 4K resolution, set up the high- performance display protocol Amazon DCV. If you do not require this functionality, do not complete this step.
## Install the ENA driver on EC2 Windows instances If your instance isn't based on one of the latest Windows Amazon Machine Images (AMIs) that Amazon provides, use the following procedure to install the current ENA driver on your instance.
You should perform this update at a time when it's convenient to reboot your instance. If the install script doesn't automatically reboot your instance, we recommend that you reboot the instance as the final step.
If you use an instance store volume to store data while the instance is running, that data is erased when you stop the instance. Before you stop your instance, verify that you've copied any data that you need from your instance store volumes to persistent storage, such as Amazon EBS or Amazon S3.
Prerequisites To install or upgrade the ENA driver, your Windows instance must meet the following prerequisites:
- PowerShell version 3.0 or later is installed.
- The commands shown in this section must run in the 64-bit version of PowerShell. Do not use the x86 version of PowerShell. That is the 32-bit version of the shell, and is not supported for these commands.

### Step 1: Back up your data We recommend that you create a backup AMI, in case you're not able to roll back your changes through the Device Manager. To create a backup AMI with the AWS Management Console, follow these steps:
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. In the navigation pane, choose Instances.
3. Select the instance that requires the driver upgrade, and choose Stop instance from the Instance state menu.
4. After the instance is stopped, select the instance again. To create your backup, choose Image and templates from the Actions menu, then choose Create image.
5. To restart your instance, choose Start instance from the Instance state menu.
### Step 2: Install or upgrade your ENA driver You can install or upgrade your ENA driver with AWS Systems Manager Distributor, or with PowerShell cmdlets. For further instructions, select the tab that matches the method that you want to use.
Systems Manager Distributor You can use the Systems Manager Distributor feature to deploy packages to your Systems Manager managed nodes. With Systems Manager Distributor, you can install the ENA driver package once, or with scheduled updates. For more information about how to install the ENA driver package (AwsEnaNetworkDriver) with Systems Manager Distributor, see Install or update packages in the AWS Systems Manager User Guide.
PowerShell This section covers how to download and install ENA driver packages on your instance with PowerShell cmdlets.
Option 1: Download and extract the latest version
1. Connect to your instance and log in as the local administrator.
2. Use the invoke-webrequest cmdlet to download the latest driver package:

PS C:\> invoke-webrequest https://ec2-windows-drivers- downloads.s3.amazonaws.com/ENA/Latest/AwsEnaNetworkDriver.zip - outfile $env:USERPROFILE\AwsEnaNetworkDriver.zip Note If you receive an error when downloading the file, and you are using Windows Server 2016 or earlier, TLS 1.2 might need to be enabled for your PowerShell terminal. You can enable TLS 1.2 for the current PowerShell session with the following command and then try again:
[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12 Alternatively, you can download the latest driver package from a browser window on your instance.
3. Use the expand-archive cmdlet to extract the zip archive that you downloaded to your instance:
PS C:\> expand-archive $env:userprofile\AwsEnaNetworkDriver.zip - DestinationPath $env:userprofile\AwsEnaNetworkDriver Option 2: Download and extract a specific version
1. Connect to your instance and log in as the local administrator.
2. Download the ENA driver package for the specific version you want from the version link in the ENA Windows driver version history table.
3. Extract the zip archive to your instance.
Install the ENA driver with PowerShell The install steps are the same whether you've downloaded the latest driver or a specific version.
To install the ENA driver, follow these steps.

1. To install the driver, run the install.ps1 PowerShell script from the AwsEnaNetworkDriver directory on your instance. If you get an error, make sure that you're using PowerShell 3.0 or later.
2. If the installer doesn't automatically reboot your instance, run the Restart-Computer PowerShell cmdlet.
PS C:\> Restart-Computer
### Step 3 (optional): Verify the ENA driver version after installation To ensure that the ENA driver package was successfully installed on your instance, you can verify the new version as follows:
1. Connect to your instance and log in as the local administrator.
2. To open the Windows Device Manager, enter devmgmt.msc in the Run box.
3. Choose OK. This opens the Device Manager window.
4. Select the arrow to the left of Network adapters to expand the list.
5. Choose the name, or open the context menu for the Amazon Elastic Network Adapter, and then choose Properties. This opens the Amazon Elastic Network Adapter Properties dialog.
Note ENA adapters all use the same driver. If you have multiple ENA adapters, you can select any one of them to update the driver for all of the ENA adapters.
6. To verify the current version that's installed, open the Driver tab and check the Driver Version.
If the current version doesn't match your target version, see Troubleshoot the Elastic Network Adapter Windows driver.
### Roll back an ENA driver installation If anything goes wrong with the installation, you might need to roll back the driver. Follow these steps to roll back to the previous version of the ENA driver that was installed on your instance.
1. Connect to your instance and log in as the local administrator.
2. To open the Windows Device Manager, enter devmgmt.msc in the Run box.

3. Choose OK. This opens the Device Manager window.
4. Select the arrow to the left of Network adapters to expand the list.
5. Choose the name, or open the context menu for the Amazon Elastic Network Adapter, and then choose Properties. This opens the Amazon Elastic Network Adapter Properties dialog.
Note ENA adapters all use the same driver. If you have multiple ENA adapters, you can select any one of them to update the driver for all of the ENA adapters.
6. To roll back the driver, open the Driver tab and choose Roll Back Driver. This opens the Driver Package rollback window.
Note If the Driver tab doesn't show the Roll Back Driver action, or if the action is unavailable, it means that the Driver Store on your instance doesn't contain the previously installed driver package. To troubleshoot this issue, see Troubleshooting scenarios, and expand the Unexpected ENA driver version installed section. For more information about the device driver package selection process, see How Windows selects a driver package for a device on the Microsoft documentation website.
### Track ENA Windows driver version releases Windows AMIs include the ENA Windows driver to enable enhanced networking.
For Windows Server versions 2016 and above, we recommend that you use the latest driver version. For earlier versions of Windows Server, refer to the following table to determine which ENA driver version to use.
Windows Server version ENA driver version Windows Server 2012 R2 2.6.0 and earlier Windows Server 2012 2.6.0 and earlier Windows Server 2008 R2 2.2.3 and earlier

#### ENA Windows driver version history The following table summarizes the changes for each release.
Driver version Details Release date 2.11.0

New features
- Added support for dynamic queue allocation with scaling up to 64 I/O queues, subject to instance type limits.
Bug fixes
- Fixed missing handling of error conditions when retrieving the physical DMA address width from the device.
August 1, 2025 2.10.0

Bug fixes
- Fixed improper handling of memory allocation failures   during queue initialization to prevent unexpected  reboots.
- Fixed possible misconfiguration of network offloads where device capabilities were ignored.
June 24, 2025 2.9.0

New features
- Added support for asynchronous reset requests initiated by the device.
- Added support for handling the maximum large LLQ depth value provided  by the device.
December 12, 2024

Driver version Details Release date
- Added Event ID 58001 in the Windows Event Viewer to enhance  visibility into unexpected power state transitions caused by device  misconfiguration.
Bug fixes
- Fixed improper handling of memory allocation failures during device  initialization to prevent unexpected reboots.
- Fixed an issue in the interrupt service routine that could enqueue a  DPC during device stop, preventing unexpected reboots.
2.8.0

Bug fixes
- Fixed a race condition in the complete flow of egress network  buffer list (NBL) processing, which could lead to memory corruption  caused by attempting to release an NBL that was already released.
- Fixed misdetection of L3 protocol when disabling all LSO and checksum  offloads that could lead to unexpected behavior.
September 30, 2024

Driver version Details Release date 2.7.0

New features
- Removed support for Windows Server 2012 (Windows
8) and Windows Server 2012 R2 (Windows 8.1). These operating system versions have reached the end of support from AWS. Driver install will fail on Windows Server 2012 and earlier.
- Added support for offloading IPv6 Tx checksum calculation to the device.
- Added wide Low Latency Queuing (LLQ) support. This is dynamically enabled based on device recommend ation.  You can override this setting with the new "WideLLQ" registry key.
- Added reporting for packet drops resulting from Rx overrun, which indicates insufficient space in the  Rx ring for incoming packets.
- Added support for suboptimal configuration notificat ions from the device. See event ID 59000  in the Windows event viewer.
Bug fixes
- Avoid unnecessary device reset caused by Tx packets with headers that exceed the maximum Low Latency Queuing (LLQ)  header size.
May 1, 2024

Driver version Details Release date 2.6.0

New features
- Adds the following network performance metrics for instance  types that support ENA Express.
- ena_srd_mode
- ena_srd_tx_pkts
- ena_srd_eligible_tx_pkts
- ena_srd_rx_pkts
- ena_srd_resource_utilization
- Adds conntrack_allowance_available network  performance metric for Nitro based instance types.
- Adds new adapter reset reason due to detection of RX data  corruption.
- Updates driver logging infrastructure.
Bug fixes
- Prevents adapter reset in the event that CPU starvatio n causes  a network performance metrics update to fail.
- Prevents false detection of an interruption to the device  heartbeat.
- June 20, 2023

Driver version Details Release date Fixes driver installation script to support downgrade operation.
- Fixes the receive error count statistic.
2.5.0 Announcement ENA Windows driver version 2.5.0 has been rolled back due to failure to initialize  on the Windows domain controller. Windows Client and Windows Server are unaffected.
February 17, 2023

Driver version Details Release date 2.4.0

New features
- Adds support for Windows Server 2022.
- Removes support for Windows Server 2008 R2.
- Sets Low Latency Queuing (LLQ) to always on to improve   performance on sixth generation Amazon EC2 instances.
Bug fixes
- Fixes a failure to publish network performance metrics   to the Performance Counters for Windows (PCW)  system.
- Fixes a memory leak during the registry key reading operation.
- Prevents an infinite reset loop in the event of an  unre coverable error during the adapter reset  process.
April 28, 2022

Driver version Details Release date 2.2.4 Announcement ENA Windows driver version 2.2.4 has been rolled back due to potential performance  degradation on the sixth generation EC2 instances. We recommend that you downgrade  the driver, using one of the following methods:
- Install the previous version
1. Download the previous version package from the link in this table (version 2.2.3).
2. Run the install.ps1 PowerShell installation script.
For more details for pre- and post-installation steps see   Enable enhanced networking on Windows.
- Use Amazon EC2 Systems Manager for a bulk update
- Perform a bulk update via SSM document AWS- ConfigureAWSPackage , with the following parameters:
- Name: AwsEnaNetworkDriver
- Version: 2.2.3 October 26, 2021

Driver version Details Release date 2.2.3

New features
- Adds support for new Nitro cards with up to 400 Gbps  instance networking.
Bug fixes
- Fixes race condition between system time change and system time query by the ENA driver, which causes false-positive detection of HW unresponsiveness.
 Announcement Windows ENA driver version 2.2.3 is the final version that  supports Windows Server 2008 R2. Currently available instance   types that use ENA will continue to be supported on Windows  Server 2008 R2, and the drivers are available by download. No  future instance types will support Windows Server 2008 R2, and  you cannot launch, import, or migrate Windows Server 2008 R2  images to future instance types.
March 25, 2021

Driver version Details Release date 2.2.2

New features
- Adds support to query network adapter performan ce  metrics with CloudWatch and the Performance Counters for  Windows consumers.
Bug fixes
- Fixes performance issues on bare metal  instances.
December 21, 2020 2.2.1

New features
- Adds a method to allow the host to query the Elastic Network Adapter for network performance metrics.
October 1, 2020

Driver version Details Release date 2.2.0

New features
- Adds support for next generation hardware   types.
- Improves instance start time after resuming from  st op-hibernate, and eliminates false positive ENA error messages.
Performance optimizations
- Optimizes processing of inbound traffic.
- Improves shared memory management in low resource   environment.
Bug fixes
- Avoids system crash upon ENA device removal in rare scenario where driver fails to reset.
August 12, 2020 2.1.5

Bug fixes
- Fixes occasional network adapter initialization  failure on bare metal instances.
June 23, 2020

Driver version Details Release date 2.1.4

Bug fixes
- Prevent connectivity issues caused by corrupted LSO packet metadata arriving from the network stack.
- Prevent system crash caused by a rare race condition that results in accessing an already released packet memory.
November 25, 2019 2.1.2

New features
- Added support for vendor ID report to allow OS to generate MAC-based UUIDs.
Bug fixes
- Improved DHCP network configuration performance during  initialization.
- Properly calculate L4 checksum on inbound IPv6 traffic   when the maximum transmission unit (MTU) exceeds   4K.
- General improvements to driver stability and minor bug  fixes.
November 4, 2019

Driver version Details Release date 2.1.1

Bug fixes
- Prevent drops of highly fragmented TCP LSO packets arriving from operating system.
- Properly handle Encapsulating Security Payload (ESP) protocol within the IPSec in IPv6 networks.
September 16, 2019

Driver version Details Release date 2.1.0

ENA Windows driver v2.1 introduces new ENA device capabilities,  provides a performance boost, adds new features, and includes  multiple stability improvements.
New features
- Use standardized Windows registry key for  Jumbo frames configuration.
- Allow VLAN ID setting via the ENA driver   properties GUI.
- Improved Recovery flows
- Improved failure identification  mechanism.
- Added support for tunable recovery   parameters.
- Support up to 32 I/O queues for newer EC2  instances that have more than 8 vCPUs.
- ~90% reduction of driver memory   footprint.
Performance optimizations
- Reduced transmit path latency.
- Support for receive checksum offload.
- Performance optimization for heavily loaded   system (optimized usage of locking   mechanisms).
- Further enhancements to reduce CPU utilization  and improve system responsiveness under  load.
July 1, 2019

Driver version Details Release date Bug fixes
- Fix crash due to invalid parsing of  non-contiguous Tx headers.
- Fix driver v1.5 crash during the elastic network  inte rface detach on Bare Metal instances.
- Fix LSO pseudo-header checksum calculation  error over IPv6.
- Fix potential memory resource leak upon  initialization failure.
- Disable TCP/UDP checksum offload for IPv4 fragments.
- Fix for VLAN configuration. VLAN was  incorrectly disabled when only VLAN priority   should have been disabled.
- Enable correct parsing of custom driver   messages by the event viewer.
- Fix failure to initialize driver due to  invalid timestamp handling.
- Fix race condition between data processing and  ENA device disabling.

Driver version Details Release date 1.5.0

Updates
- Improved stability and performance fixes.
- Receive Buffers can now be configured up to a value of  8192 in Advanced Properties of the ENA NIC.
- Default Receive Buffers of 1k.
October 4, 2018 1.2.3

Includes reliability fixes and unifies support for Windows  Server 2008 R2 through Windows Server
2016. February 13, 2018 1.0.8

The initial release. Included in AMIs for Windows Server 2008  R2, Windows Server 2012 RTM, Windows Server 2012 R2, and Windows  Server 2016.
July 2016
#### Subscribe to ENA Windows driver release notifications from Amazon SNS Amazon SNS can notify you when new versions of EC2 Windows Drivers are released. Use the following procedure to subscribe to these notifications.
Subscribe to EC2 notifications
1. Open the Amazon SNS console at https://console.aws.amazon.com/sns/v3/home.
2. In the navigation bar, change the Region to US East (N. Virginia), if necessary. You must select this Region because the SNS notifications that you are subscribing to are in this Region.
3. In the navigation pane, choose Subscriptions.
4. Choose Create subscription.
5. In the Create subscription dialog box, do the following: a.
For TopicARN, copy the following Amazon Resource Name (ARN):

arn:aws:sns:us-east-1:801119661308:ec2-windows-drivers b.
For Protocol, choose Email. c.
For Endpoint, enter an email address where you want notifications sent. d.
Choose Create subscription.
6. You'll receive a confirmation email. Open the email and follow the directions to complete your subscription.
Whenever new EC2 Windows drivers are released, we send notifications to subscribers. If you no longer want to receive these notifications, use the following procedure to unsubscribe.
Unsubscribe from Amazon EC2 Windows driver notification
1. Open the Amazon SNS console at https://console.aws.amazon.com/sns/v3/home.
2. In the navigation pane, choose Subscriptions.
3. Select the checkbox for the subscription and then choose Actions, Delete subscriptions. When prompted for confirmation, choose Delete.
## Paravirtual drivers for Windows instances Windows AMIs contain a set of drivers to permit access to virtualized hardware. These drivers are used by Amazon EC2 to map instance store and Amazon EBS volumes to their devices. The following table shows key differences between the different drivers.

Red Hat PV Citrix PV AWS PV Instance type Not supported for all instance types. If you specify an unsupported instance type, the instance is impaired.
Supported for Xen instance types.
Supported for Xen instance types.
Attached volumes Supports up to 16 attached volumes.
Supports more than 16 attached volumes.
Supports more than 16 attached volumes.

Red Hat PV Citrix PV AWS PV Network The driver has known issues where the network connectio n resets under high loads; for example, fast FTP file transfers.
The driver automatic ally configure s jumbo frames on the network adapter when on a compatibl e instance type. When the instance is in a cluster placement group, this offers better network performan ce between instances that are in the cluster placement group.
For more informati on, see Placement groups for your Amazon EC2 instances.

The following table shows which PV drivers you should run on each version of Windows Server on Amazon EC2.
Windows Server version PV driver version Windows Server 2025 Not supported Windows Server 2022 AWS PV latest version Windows Server 2019 AWS PV latest version Windows Server 2016 AWS PV latest version Windows Server 2012 R2 AWS PV version 8.4.3 Windows Server 2012 AWS PV version 8.4.3 Windows Server 2008 R2 AWS PV version 8.3.5 Windows Server 2008 Citrix PV 5.9 Windows Server 2003 Citrix PV 5.9 Contents
- AWS PV drivers
- Citrix PV drivers
- Red Hat PV drivers
- Subscribe to notifications
- Upgrade PV drivers on EC2 Windows instances
- Troubleshoot PV drivers on Windows instances
### AWS PV drivers The AWS PV drivers are stored in the %ProgramFiles%\Amazon\Xentools directory. This directory also contains public symbols and a command line tool, xenstore_client.exe, that enables you to access entries in XenStore. For example, the following PowerShell command returns the current time from the Hypervisor:

PS C:\> [DateTime]::FromFileTimeUTC((gwmi -n root\wmi -cl AWSXenStoreBase).XenTime).ToString("hh:mm:ss")
11:17:00 The AWS PV driver components are listed in the Windows registry under HKEY_LOCAL_MACHINE \SYSTEM\CurrentControlSet\Services. These driver components are as follows: xenbus, xeniface, xennet, xenvbd, and xenvif.
AWS PV drivers also have a Windows service named LiteAgent, which runs in user-mode. It handles tasks such as shutdown and restart events from AWS APIs on Xen generation instances. You can access and manage services by running Services.msc from the command line. When running on Nitro generation instances, the AWS PV drivers are not used and the LiteAgent service will self-stop starting with driver version 8.2.4. Updating to the latest AWS PV driver also updates the LiteAgent and improves reliability on all instance generations.
#### Install the latest AWS PV drivers Amazon Windows AMIs contain a set of drivers to permit access to virtualized hardware. These drivers are used by Amazon EC2 to map instance store and Amazon EBS volumes to their devices.
We recommend that you install the latest drivers to improve stability and performance of your EC2 Windows instances.
Installation options
- Use AWS Systems Manager to automatically update the PV drivers. For more information, see Walkthrough: Automatically Update PV Drivers on EC2 Windows Instances in the AWS Systems Manager User Guide.
- Download the driver package and run the install program manually. Be sure to check the readme.txt file for system requirements. For information about downloading and installing the AWS PV drivers, or upgrading a domain controller, see Upgrade Windows Server instances (AWS PV upgrade) manually.
#### AWS PV driver package history The following table shows the changes to AWS PV drivers for each driver release.

Package version Details Release date 8.6.0
- Stability fixes to XenStore interactions.
27 May 2025 8.5.0
- Stability fixes to address rare cases of crashes during network device detachment.
- Stability fixes to address rare cases of crashes during EBS volume detachment.
- Fixed bugs in the package installer.
- Updated the PV installer to use Pnputil.
31 October 2024 8.4.3 Fixed bugs in the package installer to improve the upgrade experience. This is the last version that can run on Windows Server 2012 and 2012 R2. This version is available for download, however it is no longer supported since Windows Server 2012 and 2012 R2 have reached end of support.
24 January 2023 8.4.2 Stability fixes to address race condition.
13 April 2022 8.4.1 Improved package installer.
7 January 2022 8.4.0
- Stability fixes to address rare cases of stuck disk IO.
- Stability fixes to address rare cases of crashes during EBS volume detachment.
- Added feature to distribute load across multiple cores for workloads that leverage more than 20,000 IOPS and experience degradation due to bottlenecks. To enable this feature, see Workloads that leverage more than 20,000 disk IOPS experience degradation due to CPU bottlenecks.
2 March 2021 8.3.5 Improved package installer.
This is the last version that can run on Windows Server 2008 R2. This version is available for download but no longer 7 January 2022

Package version Details Release date supported. Windows Server 2008 R2 has reached end-of-life, and is no longer supported by Microsoft.
8.3.4 Improved reliability of network device attachment.
4 August 2020 8.3.3
- Update to XenStore-facing component to prevent bug check during error-handling paths.
- Update to storage component to avoid crashes when an invalid SRB is submitted.
To update this driver on Windows Server 2008 R2 instances, you must first verify that the appropriate patches are installed to address the following Microsoft Security Advisory: Microsoft Security Advisory 3033929.
4 February 2020 8.3.2 Enhanced reliability of networking components.
30 July 2019 8.3.1 Improved performance and robustness of storage component.
12 June 2019 8.2.7 Improved efficiency to support migrating to latest generation instance types.
20 May 2019 8.2.6 Improved efficiency of crash dump path.
15 January 2019 8.2.5 Additional security enhancements.
PowerShell installer now available in package.
12 December 2018 8.2.4 Reliability improvements.
2 October 2018

Package version Details Release date 8.2.3 Bug fixes and performance improvements.
Report EBS volume ID as disk serial number for EBS volumes.
This enables cluster scenarios such as S2D.
29 May 2018 8.2.1 Network and storage performance improvements plus multiple robustness fixes.
To verify that this version has been installed, refer to the following Windows registry value: HKLM\Software\Amaz on\PVDriver\Version 8.2.1 .
8 March 2018 7.4.3 Added support for Windows Server 2016.
Stability fixes for all supported Windows OS versions.
*AWS PV driver version 7.4.3's signature expires on March 29,
2019. We recommend updating to the latest AWS PV driver.
18 Nov 2016 7.4.2 Stability fixes for support of X1 instance type.
2 Aug 2016 7.4.1
- Performance improvement in AWS PV Storage driver.
- Stability fixes in AWS PV Storage driver: Fixed an issue where the instances were hitting a system crash with bug check code 0x0000DEAD.
- Stability fixes in AWS PV Network driver.
- Added support for Windows Server 2008R2.
12 July 2016 7.3.2
- Improved logging and diagnostics.
- Stability fix in AWS PV Storage driver. In some cases disks may not surface in Windows after reattaching the disk to the instance.
- Added support for Windows Server 2012.
24 June 2015

Package version Details Release date 7.3.1 TRIM update: Fix related to TRIM requests. This fix stabilizes instances and improves instance performance when managing large numbers of TRIM requests.

7.3.0 TRIM support: The AWS PV driver now sends TRIM requests to the hypervisor. Ephemeral disks will properly process TRIM requests given the underlying storage supports TRIM (SSD).
Note that EBS-based storage does not support TRIM as of March 2015.

7.2.5
- Stability fix in AWS PV Storage drivers: In some cases the AWS PV driver could dereference invalid memory and cause a system failure.
- Stability fix while generating a crash dump: In some cases the AWS PV driver could get stuck in a race condition when writing a crash dump. Before this release, the issue could only be resolved by forcing the driver to stop and restart which lost the memory dump.

7.2.4 Device ID persistence: This driver fix masks the platform PCI device ID and forces the system to always surface the same device ID, even if the instance is moved. More generally, the fix affects how the hypervisor surfaces virtual devices. The fix also includes modifications to the co-installer for the AWS PV drivers so the system persists mapped virtual devices.

7.2.2
- Load the AWS PV drivers in Directory Services Restore Mode (DSRM) mode: Directory Services Restore Mode is a safe mode boot option for Windows Server domain controllers.
- Persist device ID when virtual network adapter device is reattached: This fix forces the system to check the MAC address mapping and persist the device ID. This fix ensures that adapters retain their static settings if the adapters are reattached.


Package version Details Release date 7.2.1
- Run in safe mode: Fixed an issue where the driver would not load in safe mode. Previously the AWS PV Drivers would only instantiate in normal running systems.
- Add disks to Microsoft Windows Storage Pools: Previously we synthesized page 83 queries. The fix disabled page 83 support. Note this does not affect storage pools that are used in a cluster environment because PV disks are not valid cluster disks.

7.2.0 Base: The AWS PV base version.

### Citrix PV drivers The Citrix PV drivers are stored in the %ProgramFiles%\Citrix\XenTools (32-bit instances) or %ProgramFiles(x86)%\Citrix\XenTools (64-bit instances) directory.
The Citrix PV driver components are listed in the Windows registry under HKEY_LOCAL_MACHINE \SYSTEM\CurrentControlSet\services. These driver components are as follows: xenevtchn, xeniface, xennet, Xennet6, xensvc, xenvbd, and xenvif.
Citrix also has a driver component named XenGuestAgent, which runs as a Windows service. It handles tasks such as shutdown and restart events from the API. You can access and manage services by running Services.msc from the command line.
If you are encountering networking errors while performing certain workloads, you may need to disable the TCP offloading feature for the Citrix PV driver. For more information, see TCP offloading.
### Red Hat PV drivers Red Hat drivers are supported for legacy instances, but are not recommended on newer instances with more than 12GB of RAM due to driver limitations. Instances with more than 12GB of RAM running Red Hat drivers can fail to boot and become inaccessible. We recommend upgrading Red Hat drivers to Citrix PV drivers, and then upgrade Citrix PV drivers to AWS PV drivers.

The source files for the Red Hat drivers are in the %ProgramFiles%\RedHat (32-bit instances) or %ProgramFiles(x86)%\RedHat (64-bit instances) directory. The two drivers are rhelnet, the Red Hat Paravirtualized network driver, and rhelscsi, the Red Hat SCSI miniport driver.
### Subscribe to notifications Amazon SNS can notify you when new versions of EC2 Windows Drivers are released. You can subscribe to these notifications.
Note You must specify the Region in which the SNS topic was created.
Whenever new EC2 Windows drivers are released, we send notifications to subscribers. If you no longer want to receive these notifications, you can unsubscribe. For more information, see Delete an SNS topic and subscription.
Console To subscribe to notifications
1. Open the Amazon SNS console at https://console.aws.amazon.com/sns/v3/home.
2. In the navigation bar, change the Region to US East (N. Virginia), if necessary. You must select this Region because the SNS notifications that you are subscribing to are in this Region.
3. In the navigation pane, choose Subscriptions.
4. Choose Create subscription.
5. In the Create subscription dialog box, do the following: a.
For TopicARN, copy the following Amazon Resource Name (ARN): arn:aws:sns:us-east-1:801119661308:ec2-windows-drivers b.
For Protocol, choose Email. c.
For Endpoint, type an email address that you can use to receive the notifications. d.
Choose Create subscription.
6. You'll receive a confirmation email. Open the email and follow the directions to complete your subscription.

AWS CLI To subscribe to notifications Use the following command. aws sns subscribe \ --topic-arn arn:aws:sns:us-east-1:801119661308:ec2-windows-drivers \ --region us-east-1 \ --protocol email \ --notification-endpoint YourUserName@YourDomainName.ext PowerShell To subscribe to notifications Use the following command.
Connect-SNSNotification `
    -TopicArn 'arn:aws:sns:us-east-1:801119661308:ec2-windows-drivers' `
    -Region us-east-1 `
    -Protocol email `
    -Endpoint "YourUserName@YourDomainName.ext"
### Upgrade PV drivers on EC2 Windows instances We recommend that you install the latest PV drivers to improve the stability and performance of your EC2 Windows instances. The directions on this page help you download the driver package and run the install program.
To verify which driver your Windows instance uses Open Device Manager and view Network Adapters. Check whether the PV driver is one of the following:
- AWS PV Network Device
- Citrix PV Ethernet Adapter
- Red Hat PV NIC Driver System requirements

Be sure to check the readme.txt file in the download for system requirements.
Contents
- Upgrade Windows Server instances (AWS PV upgrade) with Distributor
- Upgrade Windows Server instances (AWS PV upgrade) manually
- Upgrade a domain controller (AWS PV upgrade)
- Upgrade Windows Server 2008 and 2008 R2 instances (Red Hat to Citrix PV upgrade)
- Upgrade your Citrix Xen guest agent service
#### Upgrade Windows Server instances (AWS PV upgrade) with Distributor You can use Distributor, a capability of AWS Systems Manager, to install or upgrade the AWS PV driver package. The installation or upgrade can be performed one time, or you can install or update it on a schedule. The In-place update option for Installation Type isn't supported for this Distributor package.
Important If your instance is a domain controller, see Upgrade a domain controller (AWS PV upgrade).
The upgrade process for domain controller instances is different than standard editions of Windows.
1. We recommend that you create a backup in case you need to roll back your changes.
Tip Instead of creating the AMI from the Amazon EC2 console, you can use Systems Manager Automation to create the AMI using the AWS-CreateImage runbook. For more information, see AWS-CreateImage in the AWS Systems Manager Automation runbook reference User Guide. a.
When you stop an instance, the data on any instance store volumes is erased. Before you stop an instance, verify that you've copied any data that you need from your instance store volumes to persistent storage, such as Amazon EBS or Amazon S3.

b.
In the navigation pane, choose Instances. c.
Select the instance that requires the driver upgrade, and choose Instance state, Stop instance. d.
After the instance is stopped, select the instance, choose Actions, then Image and templates, and then choose Create image. e.
Choose Instance state, Start instance.
2. Connect to the instance using Remote Desktop. For more information, see the section called "Connect using an RDP client".
3. We recommend that you take all non-system disks offline and note any drive letter mappings to the secondary disks in Disk Management before you perform this upgrade. This step is not required if you are performing an in-place update of AWS PV drivers. We also recommend setting non-essential services to Manual start-up in the Services console.
4. For the instructions for how to install or upgrade the AWS PV driver package using Distributor, see the procedures in Install or update packages in the AWS Systems Manager User Guide.
5. For Name, choose AWSPVDriver.
6. For Installation type, select Uninstall and reinstall.
7. Configure the other parameters for the package as necessary and run installation or upgrade using the referenced procedure in Step 4.
After running the Distributor package, the instance automatically reboots and then upgrades the driver. The instance will not be available for up to 15 minutes.
8. After the upgrade is complete, and the instance passes both health checks in the Amazon EC2 console, verify that the new driver was installed by connecting to the instance using Remote Desktop.
9. After you are connected, run the following PowerShell command:
Get-ItemProperty HKLM:\SOFTWARE\Amazon\PVDriver
10. Verify that the driver version is the same as the latest version listed in the Driver Version History table. For more information, see AWS PV driver package history Open Disk Management to review any offline secondary volumes and bring them online corresponding to the drive letters noted in Step 3.
If you previously disabled TCP offloading using Netsh for Citrix PV drivers we recommend that you re-enable this feature after upgrading to AWS PV drivers. TCP Offloading issues with Citrix drivers

are not present in the AWS PV drivers. As a result, TCP Offloading provides better performance with AWS PV drivers.
If you previously applied a static IP address or DNS configuration to the network interface, you might need to reapply the static IP address or DNS configuration after upgrading AWS PV drivers.
#### Upgrade Windows Server instances (AWS PV upgrade) manually Use the following procedure to perform an in-place upgrade of AWS PV drivers, or to upgrade from Citrix PV drivers to AWS PV drivers on Windows Server 2008 R2, Windows Server 2012, Windows Server 2012 R2, Windows Server 2016, Windows Server 2019, or Windows Server 2022. This upgrade is not available for Red Hat drivers, or for other versions of Windows Server.
Some older versions of Windows Server can't use the latest drivers. To verify which driver version to use for your operating system, see the driver version table in the Paravirtual drivers for Windows instances page.
Important If your instance is a domain controller, see Upgrade a domain controller (AWS PV upgrade).
The upgrade process for domain controller instances is different than standard editions of Windows.
To upgrade AWS PV drivers manually
1. We recommend that you create a backup in case you need to roll back your changes.
Tip Instead of creating the AMI from the Amazon EC2 console, you can use Systems Manager Automation to create the AMI using the AWS-CreateImage runbook. For more information, see AWS-CreateImage in the AWS Systems Manager Automation runbook reference User Guide. a.
When you stop an instance, the data on any instance store volumes is erased. Before you stop an instance, verify that you've copied any data that you need from your instance store volumes to persistent storage, such as Amazon EBS or Amazon S3.

b.
In the navigation pane, choose Instances. c.
Select the instance that requires the driver upgrade, and choose Instance state, Stop instance. d.
After the instance is stopped, select the instance, choose Actions, then Image and templates, and then choose Create image. e.
Choose Instance state, Start instance.
2. Connect to the instance using Remote Desktop.
3. We recommend that you take all non-system disks offline and note any drive letter mappings to the secondary disks in Disk Management before you perform this upgrade. This step is not required if you are performing an in-place update of AWS PV drivers. We also recommend setting non-essential services to Manual start-up in the Services console.
4. Download the drivers to your instance using one of the following options:
- Browser – Download the latest driver package to the instance and extract the zip archive.
- PowerShell – Run the following commands:
Invoke-WebRequest https://s3.amazonaws.com/ec2-windows-drivers-downloads/AWSPV/ Latest/AWSPVDriver.zip -outfile $env:USERPROFILE\pv_driver.zip Expand-Archive $env:userprofile\pv_driver.zip -DestinationPath $env:userprofile \pv_drivers If you receive an error when downloading the file, and you are using Windows Server 2016 or earlier, TLS 1.2 might need to be enabled for your PowerShell terminal. You can enable TLS 1.2 for the current PowerShell session with the following command and then try again:
[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12
5. Run AWSPVDriverSetup.msi.
After running the MSI, the instance automatically reboots and then upgrades the driver. The instance will not be available for up to 15 minutes. After the upgrade is complete and the instance passes both health checks in the Amazon EC2 console, you can verify that the new driver was installed by connecting to the instance using Remote Desktop and then running the following PowerShell command:

Get-ItemProperty HKLM:\SOFTWARE\Amazon\PVDriver Verify that the driver version is the same as the latest version listed in the Driver Version History table. For more information, see AWS PV driver package history Open Disk Management to review any offline secondary volumes and bring them online corresponding to the drive letters noted in Step 3.
If you previously disabled TCP offloading using Netsh for Citrix PV drivers we recommend that you re-enable this feature after upgrading to AWS PV drivers. TCP Offloading issues with Citrix drivers are not present in the AWS PV drivers. As a result, TCP Offloading provides better performance with AWS PV drivers.
If you previously applied a static IP address or DNS configuration to the network interface, you might need to reapply the static IP address or DNS configuration after upgrading AWS PV drivers.
#### Upgrade a domain controller (AWS PV upgrade)
Use the following procedure on a domain controller to perform either an in-place upgrade of AWS PV drivers, or to upgrade from Citrix PV drivers to AWS PV drivers. To ensure that your FSMO roles remain operational during the upgrade, we recommend that you transfer those roles to other domain controllers before you start the upgrade. For more information, see How to view and transfer FSMO roles on the Microsoft Learn website.
To upgrade a domain controller
1. We recommend that you create a backup of your domain controller in case you need to roll back your changes. Using an AMI as a backup is not supported. For more information, see Backup and restore considerations in the Microsoft documentation.
2. Run the following command to configure Windows to boot into Directory Services Restore Mode (DSRM).
Warning Before running this command, confirm that you know the DSRM password. You'll need this information so that you can log in to your instance after the upgrade is complete and the instance automatically reboots.

bcdedit /set {default} safeboot dsrepair PowerShell:
PS C:\> bcdedit /set "{default}" safeboot dsrepair The system must boot into DSRM because the upgrade utility removes Citrix PV storage drivers so it can install AWS PV drivers. Therefore we recommend noting any drive letter and folder mappings to the secondary disks in Disk Management. When Citrix PV storage drivers are not present, secondary drives are not detected. Domain controllers that use an NTDS folder on secondary drives will not boot because the secondary disk is not detected.
Warning After you run this command do not manually reboot the system. The system will be unreachable because Citrix PV drivers do not support DSRM.
3. Run the following command to add DisableDCCheck to the registry: reg add HKLM\SOFTWARE\Wow6432Node\Amazon\AWSPVDriverSetup /v DisableDCCheck /t REG_SZ /d true
4. Download the latest driver package to the instance and extract the zip archive.
5. Run AWSPVDriverSetup.msi.
After running the MSI, the instance automatically reboots and then upgrades the driver. The instance will not be available for up to 15 minutes.
6. After the upgrade is complete and the instance passes both health checks in the Amazon EC2 console, connect to the instance using Remote Desktop. Open Disk Management to review any offline secondary volumes and bring them online corresponding to the drive letters and folder mappings noted earlier.
You must connect to the instance by specifying the username in the following format hostname\administrator. For example, Win2k12TestBox\administrator.
7. Run the following command to remove the DSRM boot configuration:

bcdedit /deletevalue safeboot
8. Reboot the instance.
9. To complete the upgrade process, verify that the new driver was installed. In Device Manager, under Storage Controllers, locate AWS PV Storage Host Adapter. Verify that the driver version is the same as the latest version listed in the Driver Version History table. For more information, see AWS PV driver package history.
10. Run the following command to delete DisableDCCheck from the registry: reg delete HKLM\SOFTWARE\Wow6432Node\Amazon\AWSPVDriverSetup /v DisableDCCheck Note If you previously disabled TCP offloading using Netsh for Citrix PV drivers we recommend that you re-enable this feature after upgrading to AWS PV Drivers. TCP Offloading issues with Citrix drivers are not present in the AWS PV drivers. As a result, TCP Offloading provides better performance with AWS PV drivers.
#### Upgrade Windows Server 2008 and 2008 R2 instances (Red Hat to Citrix PV upgrade)
Before you start upgrading your Red Hat drivers to Citrix PV drivers, make sure you do the following:
- Install the latest version of the EC2Config service. For more information, see Install the latest version of EC2Config.
- Verify that you have Windows PowerShell 3.0 installed. To verify the version that you have installed, run the following command in a PowerShell window:
PS C:\> $PSVersionTable.PSVersion Windows PowerShell 3.0 is bundled in the Windows Management Framework (WMF) version 3.0 install package. If you need to install Windows PowerShell 3.0, see Windows Management Framework 3.0 in the Microsoft Download Center.

- Back up your important information on the instance, or create an AMI from the instance. For more information about creating an AMI, see Create an Amazon EBS-backed AMI.
Tip Instead of creating the AMI from the Amazon EC2 console, you can use Systems Manager Automation to create the AMI using the AWS-CreateImage runbook. For more information, see AWS-CreateImage in the AWS Systems Manager Automation runbook reference User Guide.
If you create an AMI, make sure that you do the following:
- Write down your password.
- Do not run the Sysprep tool manually or using the EC2Config service.
- Set your Ethernet adapter to obtain an IP address automatically using DHCP.
To upgrade Red Hat drivers
1. Connect to your instance and log in as the local administrator. For more information about connecting to your instance, see Connect to your Windows instance using RDP.
2. In your instance, download the Citrix PV upgrade package.
3. Extract the contents of the upgrade package to a location of your choice.
4. Double-click the Upgrade.bat file. If you get a security warning, choose Run.
5. In the Upgrade Drivers dialog box, review the information and choose Yes if you are ready to start the upgrade.
6. In the Red Hat Paravirtualized Xen Drivers for Windows uninstaller dialog box, choose Yes to remove the Red Hat software. Your instance will be rebooted.
Note If you do not see the uninstaller dialog box, choose Red Hat Paravirtualize in the Windows taskbar.

7. Check that the instance has rebooted and is ready to be used. a.
Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/. b.
On the Instances page, select Actions, then Monitor and troubleshoot, and then choose Get system log. c.
The upgrade operations should have restarted the server 3 or 4 times. You can see this in the log file by the number of times Windows is Ready to use is displayed.
8. Connect to your instance and log in as the local administrator.
9. Close the Red Hat Paravirtualized Xen Drivers for Windows uninstaller dialog box.
10. Confirm that the installation is complete. Navigate to the Citrix-WIN_PV folder that you extracted earlier, open the PVUpgrade.log file, and then check for the text INSTALLATION IS COMPLETE.

#### Upgrade your Citrix Xen guest agent service If you are using Citrix PV drivers on Windows Server, you can upgrade the Citrix Xen guest agent service. This Windows service handles tasks such as shutdown and restart events from the API. You can run this upgrade package on any version of Windows Server, as long as the instance is running Citrix PV drivers.
Important For Windows Server 2008 R2 and later, we recommend you upgrade to AWS PV drivers that include the Guest Agent update.
Before you start upgrading your drivers, make sure you back up your important information on the instance, or create an AMI from the instance. For more information about creating an AMI, see Create an Amazon EBS-backed AMI.
Tip Instead of creating the AMI from the Amazon EC2 console, you can use Systems Manager Automation to create the AMI using the AWS-CreateImage runbook. For more

information, see AWS-CreateImage in the AWS Systems Manager Automation runbook reference User Guide.
If you create an AMI, make sure you do the following:
- Do not enable the Sysprep tool in the EC2Config service.
- Write down your password.
- Set your Ethernet adapter to DHCP.
To upgrade your Citrix Xen guest agent service
1. Connect to your instance and log in as the local administrator. For more information about connecting to your instance, see Connect to your Windows instance using RDP.
2. On your instance, download the Citrix upgrade package.
3. Extract the contents of the upgrade package to a location of your choice.
4. Double-click the Upgrade.bat file. If you get a security warning, choose Run.
5. In the Upgrade Drivers dialog box, review the information and choose Yes if you are ready to start the upgrade.
6. When the upgrade is complete, the PVUpgrade.log file will open and contain the text UPGRADE IS COMPLETE.
7. Reboot your instance.
### Troubleshoot PV drivers on Windows instances The following are solutions to issues that you might encounter with older Amazon EC2 images and PV drivers.
Contents
- Windows Server 2012 R2 loses network and storage connectivity after an instance reboot
- TCP offloading
- Time synchronization
- Workloads that leverage more than 20,000 disk IOPS experience degradation due to CPU bottlenecks

#### Windows Server 2012 R2 loses network and storage connectivity after an instance reboot Important This issue occurs only with AMIs made available before September 2014.
Windows Server 2012 R2 Amazon Machine Images (AMIs) made available before September 10, 2014 can lose network and storage connectivity after an instance reboot. The error in the AWS Management Console system log states: "Difficulty detecting PV driver details for Console Output."
The connectivity loss is caused by the Plug and Play Cleanup feature. This features scans for and disables inactive system devices every 30 days. The feature incorrectly identifies the EC2 network device as inactive and removes it from the system. When this happens, the instance loses network connectivity after a reboot.
For systems that you suspect could be affected by this issue, you can download and run an in- place driver upgrade. If you are unable to perform the in-place driver upgrade, you can run a helper script. The script determines if your instance is affected. If it is affected, and the Amazon EC2 network device has not been removed, the script disables the Plug and Play Cleanup scan. If the network device was removed, the script repairs the device, disables the Plug and Play Cleanup scan, and enables your instance to reboot with network connectivity enabled.
Contents
- Choose how to fix problems
- Method 1 - Enhanced networking
- Method 2 - Registry configuration
- Run the remediation script
##### Choose how to fix problems There are two methods for restoring network and storage connectivity to an instance affected by this issue. Choose one of the following methods:
Method Prerequisites Procedure Overview Method 1 - Enhanced networking Enhanced networking is only available in a virtual private You change the server instance type to a C3

Method Prerequisites Procedure Overview cloud (VPC) which requires a C3 instance type. If the server does not currently use the C3 instance type, then you must temporarily change it. instance. Enhanced networkin g then enables you to connect to the affected instance and fix the problem. After you fix the problem, you change the instance back to the original instance type. This method is typically faster than Method 2 and less likely to result in user error. You will incur additiona l charges as long as the C3 instance is running.
Method 2 - Registry configura tion Ability to create or access a second server. Ability to change Registry settings.
You detach the root volume from the affected instance, attach it to a different instance, connect, and make changes in the Registry.
You will incur additiona l charges as long as the additional server is running.
This method is slower than Method 1, but this method has worked in situations where Method 1 failed to resolve the problem.
##### Method 1 - Enhanced networking
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. In the navigation pane, choose Instances.
3. Locate the affected instance. Select the instance and choose Instance state, and then choose Stop instance.

Warning When you stop an instance, the data on any instance store volumes is erased. To keep data from instance store volumes, be sure to back it up to persistent storage.
4. After the instance is stopped, create a backup. Select the instance and choose Actions, then Image and templates, and then choose Create image.
5. Change the instance type to any C3 instance type.
6. Start the instance.
7. Connect to the instance using Remote Desktop and then download the AWS PV Drivers Upgrade package to the instance.
8. Extract the contents of the folder and run AWSPVDriverSetup.msi.
After running the MSI, the instance automatically reboots and then upgrades the drivers. The instance will not be available for up to 15 minutes.
9. After the upgrade is complete and the instance passes both health checks in the Amazon EC2 console, connect to the instance using Remote Desktop and verify that the new drivers were installed. In Device Manager, under Storage Controllers, locate AWS PV Storage Host Adapter. Verify that the driver version is the same as the latest version listed in the Driver Version History table. For more information, see AWS PV driver package history.
10. Stop the instance and change the instance back to its original instance type.
11. Start the instance and resume normal use.
##### Method 2 - Registry configuration
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. In the navigation pane, choose Instances.
3. Locate the affected instance. Select the instance, choose Instance state, and then choose Stop instance.
Warning When you stop an instance, the data on any instance store volumes is erased. To keep data from instance store volumes, be sure to back it up to persistent storage.

4. Choose Launch instances and create a temporary Windows Server 2008 or Windows Server 2012 instance in the same Availability Zone as the affected instance. Do not create a Windows Server 2012 R2 instance.
Important If you do not create the instance in the same Availability Zone as the affected instance you will not be able to attach the root volume of the affected instance to the new instance.
5. In the navigation pane, choose Volumes.
6. Locate the root volume of the affected instance. Detach the volume and then attach the volume to the temporary instance that you created earlier. Attach it with the default device name (xvdf).
7. Use Remote Desktop to connect to the temporary instance, and then use the Disk Management utility to make the volume available for use.
8. On the temporary instance, open the Run dialog box, type regedit, and press Enter.
9. In the Registry Editor navigation pane, choose HKEY_Local_Machine, and then from the File menu choose Load Hive.
10. In the Load Hive dialog box, navigate to Affected Volume\Windows\System32\config\System and type a temporary name in the Key Name dialog box. For example, enter OldSys.
11. In the navigation pane of the Registry Editor, locate the following keys:
HKEY_LOCAL_MACHINE\your_temporary_key_name\ControlSet001\Control\Class \4d36e97d-e325-11ce-bfc1-08002be10318 HKEY_LOCAL_MACHINE\your_temporary_key_name\ControlSet001\Control\Class \4d36e96a-e325-11ce-bfc1-08002be10318
12. For each key, double-click UpperFilters, enter a value of XENFILT, and then choose OK.

13. Locate the following key:
HKEY_LOCAL_MACHINE\your_temporary_key_name\ControlSet001\Services\XENBUS \Parameters
14. Create a new string (REG_SZ) with the name ActiveDevice and the following value:
PCI\VEN_5853&DEV_0001&SUBSYS_00015853&REV_01
15. Locate the following key:
HKEY_LOCAL_MACHINE\your_temporary_key_name\ControlSet001\Services\XENBUS
16. Change the Count from 0 to 1.
17. Locate and delete the following keys:
HKEY_LOCAL_MACHINE\your_temporary_key_name\ControlSet001\Services\xenvbd \StartOverride HKEY_LOCAL_MACHINE \your_temporary_key_name\ControlSet001\Services\xenfilt \StartOverride
18. In the Registry Editor navigation pane, choose the temporary key that you created when you first opened the Registry Editor.

19. From the File menu, choose Unload Hive.
20. In the Disk Management Utility, choose the drive you attached earlier, open the context (right- click) menu, and choose Offline.
21. In the Amazon EC2 console, detach the affected volume from the temporary instance and reattach it to your Windows Server 2012 R2 instance with the device name /dev/sda1. You must specify this device name to designate the volume as a root volume.
22. Start the instance.
23. Connect to the instance using Remote Desktop and then download the AWS PV Drivers Upgrade package to the instance.
24. Extract the contents of the folder and run AWSPVDriverSetup.msi.
After running the MSI, the instance automatically reboots and then upgrades the drivers. The instance will not be available for up to 15 minutes.
25. After the upgrade is complete and the instance passes both health checks in the Amazon EC2 console, connect to the instance using Remote Desktop and verify that the new drivers were installed. In Device Manager, under Storage Controllers, locate AWS PV Storage Host Adapter. Verify that the driver version is the same as the latest version listed in the Driver Version History table. For more information, see AWS PV driver package history.
26. Delete or stop the temporary instance you created in this procedure.
##### Run the remediation script If you are unable to perform an in-place driver upgrade or migrate to a newer instance you can run the remediation script to fix the problems caused by the Plug and Play Cleanup task.
To run the remediation script
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. In the navigation pane, choose Instances.
3. Select the instance for which you want to run the remediation script. Choose Instance state, and then choose Stop instance.

Warning When you stop an instance, the data on any instance store volumes is erased. To keep data from instance store volumes, be sure to back it up to persistent storage.
4. After the instance is stopped, create a backup. Select the instance, choose Actions, then Image and templates, and then choose Create image.
5. Choose Instance state, and then choose Start instance.
6. Connect to the instance by using Remote Desktop and then download the RemediateDriverIssue.zip folder to the instance.
7. Extract the contents of the folder.
8. Run the remediation script according to the instructions in the Readme.txt file. The file is located in the folder where you extracted RemediateDriverIssue.zip.
#### TCP offloading Important This issue does not apply to instances running AWS PV or Intel network drivers.
By default, TCP offloading is enabled for the Citrix PV drivers in Windows AMIs. If you encounter transport-level errors or packet transmission errors (as visible on the Windows Performance Monitor)—for example, when you're running certain SQL workloads—you may need to disable this feature.
Warning Disabling TCP offloading may reduce the network performance of your instance.
To disable TCP offloading for Windows Server 2012 and 2008
1. Connect to your instance and log in as the local administrator.

2. If you're using Windows Server 2012, press Ctrl+Esc to access the Start screen, and then choose Control Panel. If you're using Windows Server 2008, choose Start and select Control Panel.
3. Choose Network and Internet, then Network and Sharing Center.
4. Choose Change adapter settings.
5. Right-click Citrix PV Ethernet Adapter #0 and select Properties.
6. In the Local Area Connection Properties dialog box, choose Configure to open the Citrix PV Ethernet Adapter #0 Properties dialog box.
7. On the Advanced tab, disable each of the properties, except for Correct TCP/UDP Checksum Value. To disable a property, select it from Property and choose Disabled from Value.
8. Choose OK.
9. Run the following commands from a Command Prompt window. netsh int ip set global taskoffload=disabled netsh int tcp set global chimney=disabled netsh int tcp set global rss=disabled netsh int tcp set global netdma=disabled
10. Reboot the instance.
#### Time synchronization Prior to the release of the 2013.02.13 Windows AMI, the Citrix Xen guest agent could set the system time incorrectly. This can cause your DHCP lease to expire. If you have issues connecting to your instance, you might need to update the agent.
To determine whether you have the updated Citrix Xen guest agent, check whether the C:
\Program Files\Citrix\XenGuestAgent.exe file is from March 2013. If the date on this file

is earlier than that, update the Citrix Xen guest agent service. For more information, see Upgrade your Citrix Xen guest agent service.
#### Workloads that leverage more than 20,000 disk IOPS experience degradation due to CPU bottlenecks bottlenecks You can be affected by this issue if you are using Windows instances running AWS PV drivers that leverage more than 20,000 IOPS, and you experience bug check code 0x9E:
USER_MODE_HEALTH_MONITOR.
Disk reads and writes (IOs) in the AWS PV drivers occur in two phases: IO preparation and IO completion. By default, the preparation phase runs on a single arbitrary core. The completion phase runs on core 0. The amount of computation required to process an IO varies based on it size and other properties. Some IOs use more computation in the preparation phase, and others in the completion phase. When an instance drives more than 20,000 IOPS, the preparation or completion phase may result in a bottleneck, where the CPU upon which it runs is at 100% capacity. Whether or not the preparation or completion phase becomes a bottleneck depends on the properties of the IOs used by the application.
Starting with AWS PV drivers 8.4.0, the load of the preparation phase and the completion phase can be distributed across multiple cores, eliminating bottlenecks. Each application uses different IO properties. Therefore, applying one of the following configurations may raise, lower, or not impact the performance of your application. After you apply any of these configurations, monitor the application to verify that it is meeting your desired performance.
1. Prerequisites Before you begin this troubleshooting procedure, verify the following prerequisites:
- Your instance uses AWS PV drivers version 8.4.0 or later. To upgrade, see Upgrade PV drivers on EC2 Windows instances.
- You have RDP access to the instance. For steps to connect to your Windows instance using RDP, see Connect to your Windows instance using an RDP client.
- You have administrator access on the instance.
2. Observe CPU load on your instance You can use Windows Task Manager to view the load on each CPU to determine potential bottlenecks to disk IO.

1. Verify that your application is running and handling traffic similar to your production workload.
2. Connect to your instance using RDP.
3. Choose the Start menu on your instance.
4. Enter Task Manager in the Start menu to open Task Manager.
5. If Task Manager displays the Summary View, choose More details to expand the detailed view.
6. Choose the Performance tab.
7. Select CPU in the left pane.
8. Right-click on the graph in the main pane and select Change graph to>Logical processors to display each individual core.
9. Depending on how many cores are on your instance, you may see lines displaying CPU load over time, or you may just see a number.
- If you see graphs displaying load over time, look for CPUs where the box is almost entirely shaded.
- If you see a number on each core, look for cores that consistently show 95% or greater.
10.Note whether core 0 or a different core is experiencing a heavy load.
3. Choose which configuration to apply Configuration name When to apply this configuration Notes Default configuration Workload is driving less than 20,000 IOPS, or other configurations did not improve performance or stability.
For this configuration, IO occurs on a few cores, which may benefit smaller workloads by increasing cache locality and reducing context switching.
Allow driver to choose whether to distribute completion Workload is driving more than 20,000 IOPS and moderate or high load is observed on core 0.
This configuration is recommended for all Xen instances using PV 8.4.0 or later and leveraging more than 20,000 IOPS,

Configuration name When to apply this configuration Notes whether or not problems are encountered.
Distribute both preparation and completion Workload is driving more than 20,000 IOPS, and either allowing the driver to choose the distribution did not improve performan ce, or a core other than 0 is experiencing a high load.
This configuration enables distribution of both IO preparation and IO completion.
Note We recommend that you do not distribute IO preparation without also distributing IO completion (setting DpcRedirection without setting NotifierDistributed) because the completion phase is sensitive to overload by the preparation phase when the preparation phase is running in parallel.
Registry key values
- NotifierDistributed Value 0 or not present — The completion phase will run on core 0.
Value 1 — The driver chooses to run the completion phase or core 0 or one additional core per attached disk.
Value 2 — The driver runs the completion phase on one additional core per attached disk.
- DpcRedirection Value 0 or not present — The preparation phase will run on a single, arbitrary core.
Value 1 — The preparation phase is distributed across multiple cores.

Default configuration Apply the default configuration with AWS PV driver versions prior to 8.4.0, or if performance or stability degradation is observed after applying one of the other configurations in this section.
1. Connect to your instance using RDP.
2. Open a new PowerShell command prompt as an administrator.
3. Run the following commands to remove the NotifierDistributed and DpcRedirection registry keys.
Remove-ItemProperty -Path HKLM:\System\CurrentControlSet\Services\xenvbd \Parameters -Name NotifierDistributed Remove-ItemProperty -Path HKLM:\System\CurrentControlSet\Services\xenvbd \Parameters -Name DpcRedirection
4. Reboot your instance.
Allow driver to choose whether to distribute completion Set NotiferDistributed registry key to allow the PV storage driver to choose whether or not to distribute IO completion.
1. Connect to your instance using RDP.
2. Open a new PowerShell command prompt as an administrator.
3. Run the following command to set the NotiferDistributed registry key.
Set-ItemProperty -Type DWORD -Path HKLM:\System\CurrentControlSet\Services\xenvbd \Parameters -Value 0x00000001 -Name NotifierDistributed
4. Reboot your instance.

Distribute both preparation and completion Set NotifierDistributed and DpcRedirection registry keys to always distribute both the preparation and completion phases.
1. Connect to your instance using RDP.
2. Open a new PowerShell command prompt as an administrator.
3. Run the following commands to set the NotifierDistributed and DpcRedirection registry keys.
Set-ItemProperty -Type DWORD -Path HKLM:\System\CurrentControlSet\Services\xenvbd \Parameters -Value 0x00000002 -Name NotifierDistributed Set-ItemProperty -Type DWORD -Path HKLM:\System\CurrentControlSet\Services\xenvbd \Parameters -Value 0x00000001 -Name DpcRedirection
4. Reboot your instance.
## AWS NVMe drivers Amazon EBS volumes and instance store volumes are exposed as NVMe block devices on Nitro- based instances. To fully utilize the performance and capabilities of Amazon EBS features for volumes exposed as NVMe block devices, the instance must have the AWS NVMe driver installed.
All current generation AWS Windows AMIs come with the AWS NVMe driver installed by default.
For more information about EBS and NVMe, see Amazon EBS and NVMe in the Amazon EBS User Guide. For more information about SSD instance store and NVMe, see SSD instance store volumes for EC2 instances.
### Linux instances The following AMIs include the required NVMe drivers:
- Amazon Linux 2
- Amazon Linux AMI 2018.03
- Ubuntu 14.04 or later with linux-aws kernel

Note AWS Graviton-based instance types require Ubuntu 18.04 or later with linux-aws kernel
- Red Hat Enterprise Linux 7.4 or later
- SUSE Linux Enterprise Server 12 SP2 or later
- CentOS 7.4.1708 or later
- FreeBSD 11.1 or later
- Debian GNU/Linux 9 or later To confirm that your instance has the NVMe driver You can confirm that your instance has the NVMe driver using the following command.
- Amazon Linux, RHEL, CentOS, and SUSE Linux Enterprise Server $ modinfo nvme If the instance has the NVMe driver, the command returns information about the driver.
- Amazon Linux 2 and Ubuntu $ ls /sys/module/ | grep nvme If the instance has the NVMe driver, the command returns the installed drivers.
To update the NVMe driver If your instance has the NVMe driver, you can update the driver to the latest version using the following procedure.
1. Connect to your instance.
2. Update your package cache to get necessary package updates as follows.
- For Amazon Linux 2, Amazon Linux, CentOS, and Red Hat Enterprise Linux:

[ec2-user ~]$ sudo yum update -y
- For Ubuntu and Debian:
[ec2-user ~]$ sudo apt-get update -y
3. Ubuntu 16.04 and later include the linux-aws package, which contains the NVMe and ENA drivers required by Nitro-based instances. Upgrade the linux-aws package to receive the latest version as follows:
[ec2-user ~]$ sudo apt-get install --only-upgrade -y linux-aws For Ubuntu 14.04, you can install the latest linux-aws package as follows:
[ec2-user ~]$ sudo apt-get install linux-aws
4. Reboot your instance to load the latest kernel version. sudo reboot
5. Reconnect to your instance after it has rebooted.
### Windows instances PowerShell If you did not launch your instance from one of the latest AWS Windows AMIs provided by Amazon, use the following procedure to install the current AWS NVMe driver on your instance.
Reboot is required for this install. Either the install script will reboot your instance or you must reboot it as the final step.
Prerequisites
- PowerShell version 3.0 or later is installed.
- The commands shown in this section must run in the 64-bit version of PowerShell. Do not use the x86 version of PowerShell. That is the 32-bit version of the shell, and is not supported for these commands.

To download and install the latest AWS NVMe driver
1. We recommend that you create an AMI as a backup as follows, in case you need to roll back your changes. a.
When you stop an instance, the data on any instance store volumes is erased. Before you stop an instance, verify that you've copied any data that you need from your instance store volumes to persistent storage, such as Amazon EBS or Amazon S3. b.
In the navigation pane, choose Instances. c.
Select the instance that requires the driver upgrade, and choose Instance state, Stop instance. d.
After the instance is stopped, select the instance, choose Actions, then Image and templates, and then choose Create image. e.
Choose Instance state, Start instance.
2. Connect to your instance and log in as the local administrator.
3. Download the drivers to your instance using one of the following options:
- Browser – Download the latest driver package to the instance and extract the zip archive.
- PowerShell – Run the following commands:
Invoke-WebRequest https://s3.amazonaws.com/ec2-windows-drivers-downloads/ NVMe/Latest/AWSNVMe.zip -outfile $env:USERPROFILE\nvme_driver.zip Expand-Archive $env:userprofile\nvme_driver.zip -DestinationPath $env:userprofile\nvme_driver If you receive an error when downloading the file, and you are using Windows Server 2016 or earlier, TLS 1.2 might need to be enabled for your PowerShell terminal. You can enable TLS 1.2 for the current PowerShell session with the following command and then try again:
[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12
4. Install the driver to your instance by running the install.ps1 PowerShell script from the nvme_driver directory (.\install.ps1). If you get an error, make sure you are using PowerShell 3.0 or later.

a.
(Optional) Starting with AWS NVMe version 1.5.0, Small Computer System Interface (SCSI) persistent reservations are supported for Windows Server 2016 and later. This feature adds support for Windows Server Failover Clustering with shared Amazon EBS storage. By default, this feature isn't enabled during installation.
You can enable the feature when running the install.ps1 script to install the driver by specifying the EnableSCSIPersistentReservations parameter with a value of $true.
PS C:\> .\install.ps1 -EnableSCSIPersistentReservations $true You can disable the feature when running the install.ps1 script to install the driver by specifying the EnableSCSIPersistentReservations parameter with a value of $false.
PS C:\> .\install.ps1 -EnableSCSIPersistentReservations $false b.
Starting with AWS NVMe 1.5.0, the install.ps1 script always installs the ebsnvme-id tool with the driver.
(Optional) For versions 1.4.0, 1.4.1, and 1.4.2, the install.ps1 script allows you to specify whether the ebsnvme-id tool should be installed with the driver. i.
To install the ebsnvme-id tool, specify InstallEBSNVMeIdTool 'Yes'. ii.
If you don't want to install the tool, specify InstallEBSNVMeIdTool 'No'.
If you don't specify InstallEBSNVMeIdTool, and the tool is already present at C:\ProgramData\Amazon\Tools, the package will upgrade the tool by default.
If the tool is not present, install.ps1 will not upgrade the tool by default.
If you don't want to install the tool as part of the package, and want to install it later, you can find the latest version or the tool in the driver package.
Alternatively, you can download version 1.0.0 from Amazon S3:
Download the ebsnvme-id tool.
5. If the installer does not reboot your instance, reboot the instance.

Distributor You can use Distributor, a capability of AWS Systems Manager, to install the NVMe driver package one time or with scheduled updates.
To install the latest AWS NVMe driver
1. For the instructions for how to install the NVMe driver package using Distributor, see the procedures in Install or update packages in the Amazon EC2 Systems Manager User Guide.
2. For Installation Type, select Uninstall and reinstall.
3. For Name, choose AWSNVMe.
4. (Optional) For Additional Arguments, you can customize the installation by specifying values. The values must be formatted using valid JSON syntax. For examples of how to pass additional arguments for the aws configure package, see the Command document plugin reference. a.
Starting with AWS NVMe 1.5.0, the driver supports SCSI persistent reservations for Windows Server 2016 and later. By default, this feature isn't enabled during installation.
- To enable this feature, specify {"SSM_EnableSCSIPersistentReservations":
"true"}.
- If you don't want to enable this feature, specify {"SSM_EnableSCSIPersistentReservations": "false"}. b.
Starting with AWS NVMe 1.5.0, the install.ps1 script will always install the ebsnvme-id tool.
(Optional) For versions 1.4.0, 1.4.1, and 1.4.2, the install.ps1 script allows you to specify whether the ebsnvme-id tool should be installed with the driver.
- To install the ebsnvme-id tool, specify {"SSM_InstallEBSNVMeIdTool":
"Yes"}.
- If you don't want to install the tool, specify {"SSM_InstallEBSNVMeIdTool":
"No"}.
If SSM_InstallEBSNVMeIdTool is not specified for Additional Arguments, and the tool is already present at C:\ProgramData\Amazon\Tools, the package will

upgrade the tool by default. If the tool is not present, the package will not upgrade the tool by default.
If you don't want to install the tool as part of the package, and want to install it later, you can find the latest version of the tool in the driver package. Alternatively, you can download version 1.0.0 from Amazon S3:
Download the ebsnvme-id tool.
5. If the installer does not reboot your instance, reboot the instance.
### Configure SCSI persistent reservations for Windows instances After AWS NVMe driver version 1.5.0 or later has been installed, you can enable or disable SCSI persistent reservations using the Windows registry for Windows Server 2016 and later. You must reboot the instance for these registry changes to take effect.
You can enable SCSI persistent reservations with the following command which sets the EnableSCSIPersistentReservations to a value of 1.
PS C:\> $registryPath = "HKLM:\SYSTEM\CurrentControlSet\Services\AWSNVMe\Parameters \Device"
Set-ItemProperty -Path $registryPath -Name EnableSCSIPersistentReservations -Value 1 You can disable SCSI persistent reservations with the following command which sets the EnableSCSIPersistentReservations to a value of 0.
PS C:\> $registryPath = "HKLM:\SYSTEM\CurrentControlSet\Services\AWSNVMe\Parameters \Device"
Set-ItemProperty -Path $registryPath -Name EnableSCSIPersistentReservations -Value 0
### AWS NVMe Windows driver version history The following table shows which AWS NVMe drivers run on each version of Windows Server on Amazon EC2.
Windows Server version AWS NVMe driver version Windows Server 2025 latest version

Windows Server version AWS NVMe driver version Windows Server 2022 latest version Windows Server 2019 latest version Windows Server 2016 latest version Windows Server 2012 R2 version 1.5.1 and earlier Windows Server 2012 version 1.5.1 and earlier Windows Server 2008 R2 version 1.3.2 and earlier Windows Server 2008 version 1.3.2 and earlier The following table describes the released versions of the AWS NVMe driver.
Package version Driver version Details Release date 1.8.0 1.8.0
- Added support for IOCTLs to operate with devices that implement dynamic  namespace managemen t. For more information, see IOCTL_SCSI_MINIPORT IOCTL in the Microsoft documentation.
- Bug fixes in the Get Log Page command and serial number generation.
16 January 2026 1.7.0 1.7.0
- Added support for NVMe Get Log Page Command.
- Added support for detailed performance statistics for EBS and EC2 instance  store volumes.
- Bug fixes for the Identify Namespace command.
17 September 2025

Package version Driver version Details Release date 1.6.0 1.6.0
- Updated the install script to use PnPUtil.
- Updated ebsnvme-id.exe to use NVMe IOCTL.
25 October 2024 1.5.1 1.5.0 Fixed the install script to create a folder for the ebsnvme-id  tool if it is not  present.
17 November 2023 1.5.0 1.5.0 Added support for Small Computer System Interface (SCSI)  persistent reservations for instances running Windows Server 2016  and later. The ebsnvme-id tool (ebsnvme-id.exe )  is now installed by default.
31 August 2023 1.4.2 1.4.2 Fixed a bug where the AWS NVMe driver did not support instance store  volumes on D3 instances.
16 March 2023 1.4.1 1.4.1 Reports Namespace Preferred Write Granularity (NPGW) for EBS  volumes that support this optional NVMe feature. For more  information, see section 8.25, "Improving Performance through I/O  Size and Alignment Adherence," in the NVMe Base Specifica tion, version 1.4.
20 May 2022

Package version Driver version Details Release date 1.4.0 1.4.0
- Added support for IOCTLs that allow applications to  interact with NVMe devices. This support allows applications  to get IdentifyController , IdentifyNamespace , and   NameSpace  list from the NVMe device. For  more information, see Protocol-specific queries in the Microsoft  documen tation.
- The 1.4.0 driver version and the latest   ebsnvme- id  tool  (ebsnvme-id.exe ) are combined in a single  package. This combination allows you to install both driver  and tool from a single package.
For more details, see AWS NVMe drivers.
- Bug fixes and reliability improvements.
23 November 2021 1.3.2 1.3.2 Fixed issue with modifying EBS volumes actively processing IO, which  may result in data corruption.
Customers who do not modify online EBS  volume s (for example, resizing or changing type) are not impacted.
This is the last version that can run on Windows Server 2008 and 2008 R2.  This version is available for download but no longer supported.  Windows Server 2008 and 2008 R2 has reached end-of-life, and is no longer supported by Microsoft.
10 September 2019 1.3.1 1.3.1 Reliability Improvements.
21 May 2019 1.3.0 1.3.0 Device optimization improvements.
31 August 2018

Package version Driver version Details Release date 1.2.0 1.2.0 Performance and reliability improvements for AWS NVMe devices on  all supported instances, including bare metal instances.
13 June 2018
>1.0.0
>1.0.0 AWS NVMe driver for supported instance types running Windows  Server.
12 February 2018
#### Subscribe to notifications Amazon SNS can notify you when new versions of EC2 Windows Drivers are released. Use the following procedure to subscribe to these notifications.
To subscribe to EC2 notifications from the console
1. Open the Amazon SNS console at https://console.aws.amazon.com/sns/v3/home.
2. In the navigation bar, change the Region to US East (N. Virginia), if necessary. You must select this Region because the SNS notifications that you are subscribing to are in this Region.
3. In the navigation pane, choose Subscriptions.
4. Choose Create subscription.
5. In the Create subscription dialog box, do the following: a.
For TopicARN, copy the following Amazon Resource Name (ARN): arn:aws:sns:us-east-1:801119661308:ec2-windows-drivers b.
For Protocol, choose Email. c.
For Endpoint, type an email address that you can use to receive the notifications. d.
Choose Create subscription.
6. You'll receive a confirmation email. Open the email and follow the directions to complete your subscription.
Whenever new EC2 Windows drivers are released, we send notifications to subscribers. If you no longer want to receive these notifications, use the following procedure to unsubscribe.
