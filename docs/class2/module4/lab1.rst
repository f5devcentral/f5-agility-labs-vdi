Lab 1.4: Build a webtop with VMware View and Citrix
==================================
This lab will leverage the APM access policies created in prior labs to build a unified webtop with access to Vmware View and Citrix

Task 1 – Build a VIP and Access Policy 
-----------------------------------------------------------


#. From the "corporate-pc".

#. Connect to the F5 config GUI 

   - https://f5-bigip1a.demosifun.net
   - Username: admin
   - Password: password 

#. Copy the VM_LAB_1_PCOIP access profile to VDI_Combined_webtop
   - Access>>Profiles/Policies>>Access Profiles
   - Click the “Copy” hyperlink on the VM_LAB_1_PCOIP  line
   - Name the profile VDI_Combined_webtop
Press the Copy button (bottom left)


#. When prompted for credentials

   - Username: ``demo01``

   - Password: ``password``

#. Double-click the "Agility" icon to launch virtual desktop.

#. In the Agility virtual desktop, open Notepad and type in something.

#. Disconnect from Agility desktop by closing View client. (RDP Toolbar
   on top. May need to slide the blue RDP bar to the left in order to
   click the X in Agility Toolbar)

#. Open View client and try to reconnect to "vmw-connsvr1c.
   demoisfun.net"

#. Notepad should still be on the desktop with the text you input.

#. Close the View client. (press the X in Agility Toolbar)
