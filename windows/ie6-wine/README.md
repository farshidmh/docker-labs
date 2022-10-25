## Lab: Run IE6 in Container

Here we are going to try a useful case:  Browser testing.   

Like the zombie that just refuses to die, Internet Explorer 6 lives on, wreaking a trail of devastation in its wake.  One would hope that nobody would be foolish enough to run IE6 unprotected  on their computer, but we still may want to test with IE6 for various reasons.  Unbelievably, many enterprises continue to use IE6 to run legacy webapps, despite Microsoft's pleas to remove it once and for all.j

A Docker container is a great way to run IE6. That data is immutable means that any malware captured by IE6 would be removed the second the browser closes.

Unfortunately, windows containers do not allow for GUI apps of any kind.  So we need to use a Linux container.   So, there are two ways we can run this.

1. Virtualization inside the container.  Unfortuantely, we will need to handle licensing a windows VM guest from Microsoft.  If only MS made this easier!  And it is somewhat dubious that this approach is any better than just running a Windows VM in the first place with Virtualbox or VMWare Desktop.
2. WINE.  WINE is a translation layer for the Win32 and Win64 API on top of Linux.  As IE itself is freeware, we can run this without any restrictions. The only problem is that WINE is not perfect and so IE6 will probably be even
more flaky than it would be on a Windows host.


We're goin to try the second approach.  We'll see that it will work (somewhat), but it also will be prone to errors and browser crashes.


## STEP 1:

Log into your linux host, which needs to have X11 installed.  This approach will work on Linux only.  In theory, it will work on any machine with an X-server installed (such as Mac with Quartz, or VcXsrv on Windows), but that's out of the scope of this lab.  


## Step 2:
```bash
cd ie6
docker build . -t elephantscale/ie6
```

## Step 3: Run Browser

```bash
cd ..
./run-docker.sh elephantscale/ie6
```

## Step 4: Test Browser

You should be able to test IE6 by going to various sites, etc. 


