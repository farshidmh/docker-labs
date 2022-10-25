<link rel='stylesheet' href='../assets/css/main.css'/>

# Install Docker on Windows

## Step 1: Ensure Compatibility

Docker for Windows works **ONLY** on the following Windows Operating Systems:

1. Windows 10 Professional 64-Bit
2. Windows Server 2016

It does **NOT** work on:

1. Any version of Windows earlier than Windows 10
2. Any home version of windows (rather than Professional)
3. Any 32 Bit version of Windows.
4. Windows on ARM, Tablets, Windows RT, etc. etc. 

If you are unsure what version of Windows you are running, you can check like this:

Select the Start button > Settings  > System  > About.


## Step 2: Ensure Virtualization is Enabled

Open up the Task Manager -> Performance Tab. Click on CPU (if not already selected).

On the lower right you should see Something that says `Virtualization:`.  It will be 
rigth abouve the L1 Cache:

If it says "Enabled", then you are good.

If it says, "Disabled" then you need to turn Virtualization on in your BIOS.

You will need to reboot your PC and get into your PCs BIOS software.  Every PC BIOS
is different.  You will need to find and enable Virtualization, which may also be called
VT-x or AMD-V.

Most PC Motherboards will have Virtualization disabled by default.  So, it is likely
you will need to turn it on in the bios if you have never turned it on before.


## Step 3: Ensure that Hyper-V is enabled in Windows

Open Powershell as Administrator.  To do this, go to the Start Menu -> Select Powershell, and right 
Click "Run as Administrator"


Type the following:

```console
Enable-WindowsOptionalFeature -Online -FeatureName Microsoft-Hyper-V -All
```

You will need to restart your computer after this.

## Step 4: Open up powershell as Administrator

 * Click Start and type “powershell“
 * Right-click Windows Powershell and choose “Run as Administrator“

## Step 5: Install Chocolatey

 * Paste the following command into Powershell and press enter.


```console
Set-ExecutionPolicy Bypass -Scope Process -Force; `
  iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))
```
 * Answer Yes when prompted
 * Close Powershell


## Step 6: Open a new Powershell as Administrator

 * Click Start and type “powershell“
 * Right-click Windows Powershell and choose “Run as Administrator“


## Step 7: Install Chocolatey

 * Paste the following command into Powershell and press enter.

```console

choco search docker-desktop
choco install docker-desktop

```

 * Close Powershell

## Step 8: Run Hello world container

Open a Windows Command Prompt (NOT As administrator)

Run the following hello world container

```bash
docker run hello-world
```

```console
Unable to find image 'hello-world:latest' locally
latest: Pulling from library/hello-world
9bb5a5d4561a: Pull complete
Digest: sha256:f5233545e43561214ca4891fd1157e1c3c563316ed8e237750d59bde73361e77
Status: Downloaded newer image for hello-world:latest

Hello from Docker!
This message shows that your installation appears to be working correctly.
```

Seems to be going ok.  Let's see what images that got.

```bash
docker images
```

```console
REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE
hello-world         latest              e38bc07ac18e        5 weeks ago         1.85kB
```

Looks like things are working!
