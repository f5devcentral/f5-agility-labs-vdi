Lab 1.1: Solutions for VMware View
==================================

Task 1 – Access VMware View Desktop environment without F5 
-----------------------------------------------------------

Test the functional VMware view environment using the internal
Connection Servers (Internal use case without F5 integration)

Access the VDI with a client on the internal network. The workstation
will be preconfigured to initiate the connection through a specific
connection server. Security servers are not used by internal VDI users

|image3|

Figure 2 - Accessing Internal View Desktop

#. From the "corporate-pc".

#. Use the VMware Horizon View client to access the connection server

   |image4|

   - VMware Horizon Client

   - \+ New server

#. Connection Server address "vmw-connsvr1c.demoisfun.net"

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
