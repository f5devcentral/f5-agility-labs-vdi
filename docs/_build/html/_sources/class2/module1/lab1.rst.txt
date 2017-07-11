Lab 1 – Solutions for VMware View
=================================

TASK 1 – Access VMware View Desktop environment without F5 
-----------------------------------------------------------

Test the functional VMware view environment using the internal
Connection Servers (Internal use case without F5 integration)

|image1|

Figure 1 - Accessing internal View Desktop--

Access the VDI with a client on the internal network. The workstation
will be preconfigured to initiate the connection through a specific
connection server. Security servers are not used by internal VDI users

#. Use the RDP function on your laptop to connect to the “corporate-pc“
   RDP server/workstation

 |image2|

#.  When prompted for credentials

    a. Username: Agility

    b. Password: F5Agility

       |image3|

#.  Use the VMware Horizon View client to access the connection server

    a. VMware Horizon Client

    b. + New server

#.  Connection Server address “vmw-connsvr1c.demoisfun.net”

#.  When prompted for credentials

    a. Username: demo01

    b. Password: password

#.  Select the View desktop (Agility—Rt click and Launch)

#.  Scroll down to task bar if needed

#.  Open Notepad and type in something.

#.  Slide the blue RDP indicator to the left

#.  Close the View client. (press the X in Agility Toolbar-was under the
    RDP)

#. Open View client and try to reconnect to “vmw-connsvr1c.
    demoisfun.net”

#. Notepad should still be on the desktop with the test you input

#. Close the View client. (press the X in Agility Toolbar)

#. **Keep the RDP session open for Task 2 **

TASK 2 – Load Balance VMware View connection servers
----------------------------------------------------

Use the F5 iApp for VMware View to configure a load balancing
environment for the Connection Servers. This will increase the number of
Connection Servers available to internal users and load balance access
to these resources (Internal use case with F5 load balancing)

|image4|

Figure 2 - Load balance Connection Servers

**Deploy the iApp**

1. Access the F5 Config GUI from the “corporate-pc” RDP
   server/workstation –

   a. https://f5-bigip1a.demoisfun.net (192.168.10.216)

      i.  Username: admin

      ii. Password: password

2. Create a new Application Service

   a. iApps >> Application Services

   b. Press the **Create** button

   c. Name the Application Service **VM\_LAB\_1\_LBCS**

   d. Select **f5.vmware\_view.v1.5.1** for the template

+----+
+----+

1. Review the **Welcome to the iAPP template for VMware Horizon View**

2. Note the **Template Options** (leave these default)

3. **Big-IP Access Policy Manager** (Set this to **No** for this
   exercise)

4. SSL Encryption (Certs are preloaded for this exercise)

+----------------------------------------------------------+------------------------------------------------------------------------+
| How should the BIG-IP system handle encrypted traffic?   | Terminate SSL for clients, re-encrypt to View servers (SSL-bridging)   |
+==========================================================+========================================================================+
| Which SSL certificate do you want to use?                | wild.demoisfun.net.crt                                                 |
+----------------------------------------------------------+------------------------------------------------------------------------+
| Which SSL private key do you want to use                 | wild.demoisfun.net.key                                                 |
+----------------------------------------------------------+------------------------------------------------------------------------+

1. **PC Over IP** (leave these default – No PCoIP connections…)

2. **Virtual Servers and Pools **

+------------------------------------------------------------------------------------+---------------------------+
| What virtual server IP address do you want to use for remote, untrusted clients?   | 192.168.10.150            |
+====================================================================================+===========================+
| What is the associated service port?                                               | 443                       |
+------------------------------------------------------------------------------------+---------------------------+
| What FQDN will clients use to access the View environment                          | vmw-LB-CS.demoisfun.net   |
+------------------------------------------------------------------------------------+---------------------------+
| Which Servers should be included in this pool                                      | 192.168.10.212            |
|                                                                                    |                           |
|                                                                                    | 192.168.10.213            |
+------------------------------------------------------------------------------------+---------------------------+

1. **Client Optimization** (leave these default—Do not compress…)

2. **Application Health**

   a. Use the pulldown to select a standard https monitor

3. Press the **Finished** button

View the objects which were created by the iApp
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Select the Components tab at the top of the page

    |image5|

1. Is the Virtual server available?

2. Are the pool members available?

3. What is the node status? Why?

4. Note that a persistence profile was created

   a. Check Match Across Services

   b. Press update

   c. Note the error at the top of the page

5. Return to iApp>>Application Services

6. Review the remaining parameters (any questions)

View the properties of the iApp
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Select the Properties tab at the top of the page

2. |image6|

3. Use the pull down next to Application Service:

4. Select Advanced

5. Note the check in Strict Updates

   a. Is this related to the screen when editing the persistence
      profile?

   b. What are the pro’s and con’s of unchecking this parameter?

Test the connection server load balancing using both VMware View client and browser access methods. 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1.  Use the RDP function on your laptop to connect to the “corporate-pc”
    RDP server/workstation

    i. Same process as Task 1 if you are not still connected

2.  Open View client and connect to the Virtual Server just created with
    iApp.

    a. +New Server

       i.  vmw-LB-CS.demoisfun.net (192.168.10.150)

       ii. IP address will not work—Certificate contains demoisfun.net

3.  When prompted for credentials

    a. Username: demo01

    b. Password: password

4.  Select the View desktop (Agility)

5.  Use connect button to access

6.  Slide the blue RDP indicator to the left

7.  Close the View client. (press the X in Agility Toolbar-was under the
    RDP)

8.  Use a supported browser to access the VDI (IE on the RDP
    workstation)

    |image7|

9.  https://vmw-LB-CS.demoisfun.net

10. Select VMware Horizon View HTML access

11. Log in

    a. Username: demo01

    b. Password: password

12. Select (Agility)

13. Accept Cert Warnings

14. Verify that the desktop functions

15. Close the browser window

TASK 3 – Access View Desktop environment through Security Server
----------------------------------------------------------------

Test the functional VMware View environment using external Security
Servers. (External use case without F5 integration)

Note: This environment shows a user connecting to a native VMware
security server which is statically mapped to a VMware connection
server. This is a non-redundant external access model

|image8|

Figure 3 - Access external View Desktop

Access the VDI using the Security Server from a Windows Server RDP
session

1. Use the RDP function on your laptop to connect to the
   “\ **home-pc**\ ” RDP server/workstation

|image9|

1.  When prompted for credentials

    a. Username: agility

    b. Password: F5Agility

       |image10|

2.  Use the VMware Horizon View client to access the security server

    a. +New Server

    b. Security Server address “vmw-secursvr1a.demoisfun.net”

3.  When prompted for credentials

    a. Username: demo01

    b. Password: password

4.  Select the View desktop (Right Click on Agility - Launch)

5.  Slide the blue RDP indicator to the left

6.  Close the View client. (press the X in Agility Toolbar-was under the
    RD)

    a. vmw-secursvr1a.demoisfun.net

7.  Use a supported browser to access the VDI (IE on the RDP
    workstation)

    |image11|

8.  Access the application through your browser https://
    vmw-secursvr1a.demoisfun.net

    a. vmw-secursvr1a.demoisfun.net

    b. Username: demo01

    c. Password: password

9.  Select VMware Horizon View HTML access

10. Log in

    a. Username: demo01

    b. Password: password

11. Select (Agility)

12. Accept Cert at warning

13. Select (Agility)

14. Verify that the desktop functions

    a. Scroll down to taskbar

15. Close the browser

192.168.3.150

TASK 4 – Load Balance VMware View security servers
---------------------------------------------------------------

Use the F5 iApp for VMware View to configure a load balancing
environment for the Security Servers. This will increase the number of
Security Servers available to internal users and load balance access to
these resources (External use case with F5 load balancing)

Note: This environment load balances 2 external facing Security Servers.
These Security Servers are directly mapped to 2 existing connection
servers in the environment (not the 2 Connections Servers that are load
balances in the steps above)

|image12|

Figure 4 - Load balance Security Servers

\ **Deploy the iApp**

1. Use the RDP function on your laptop to connect to the “corporate-pc”
   RDP server/workstation

   i. Same process as Task 1 if you are not still connected

2. Create a new Application Service by selecting

   a. iApps >> Application Services

   b. Press the **Create** button

   c. Name the Application Service **VM\_LAB\_1\_LBSS**

   d. Select **f5.vmware\_view.v1.5.1** for the template

+----+
+----+

1. Review the **Welcome to the iAPP template for VMware Horizon View**

2. Note the **Template Options** (leave these default)

3. **Big-IP Access Policy Manager** (Set this to **No** for this
   exercise)

4. **SSL Encryption** (Certs are preloaded for this exercise)

+----------------------------------------------------------+--------------------------------------------------------------+
| How should the BIG-IP system handle encrypted traffic?   | Terminate SSL for clients, re-encrypt…\ **(SSL-Bridging)**   |
+==========================================================+==============================================================+
| Which SSL certificate do you want to use?                | wild.demoisfun.net.crt                                       |
+----------------------------------------------------------+--------------------------------------------------------------+
| Which SSL private key do you want to use?                | wild.demoisfun.net.key                                       |
+----------------------------------------------------------+--------------------------------------------------------------+

1. **PC Over IP** (leave these default – No PCoIP connections…)

2. **Virtual Servers and Pools **

+------------------------------------------------------------------------------------+---------------------------+
| What virtual server IP address do you want to use for remote, untrusted clients?   | 192.168.3.150             |
+====================================================================================+===========================+
| What is the associated service port?                                               | 443                       |
+------------------------------------------------------------------------------------+---------------------------+
| What FQDN will clients use to access the View environment?                         | vmw-LB-SS.demoisfun.net   |
+------------------------------------------------------------------------------------+---------------------------+
| Which Servers should be included in this pool?                                     | 192.168.3.214             |
|                                                                                    |                           |
|                                                                                    | 192.168.3.215             |
+------------------------------------------------------------------------------------+---------------------------+

1. **Client Optimization** (leave these default—Do not compress…)

2. **Application Health**

   a. Use the pulldown to select a standard https monitor

3. Press the **Finished** button

View the objects which were created by the iApp
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Select the Components tab at the top of the page

2. Is the Virtual server available?

3. Are the pool members available?

4. Is the Node Available?

5. Review the remaining parameters (any questions)

Test the Security Server load balancing using both VMware View client and browser access methods
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1.  Use the RDP function on your laptop to connect to the “home-pc” RDP
    server/workstation

2.  Open View client and connect to the Virtual Server just created with
    iApp.

    a. +New Server

       i.  vmw-LB-SS.demoisfun.net (192.168.3.150)

       ii. IP address will not work—Certificate contains demoisfun.net

3.  When prompted for credentials

    a. Username: demo01

    b. Password: password

4.  Select the View desktop (Agility)

5.  Use connect button to access

6.  Slide the blue RDP indicator to the left

7.  Close the View client. (press the X in Agility Toolbar-was under the
    RD)

8.  Use a supported browser to access the VDI (IE on the RDP
    workstation)

    |image13|

9.  https://vmw-LB-SS.demoisfun.net

10. Select VMware Horizon View HTML access

11. Enter Credentials

    a. Username: demo01

    b. Password: password

12. Select (Agility)

13. Accept Cert warning

14. Select (Agility)

15. Verify that the desktop functions

16. Close the browser

TASK 5 – Replace Security Servers and leverage APM as a PCOIP proxy
-------------------------------------------------------------------

**Use the VMware View iApp to replace Security Server to proxy PCoIP
traffic**

Note: This environment will utilize Big-IP as a PCOIP Proxy. This
eliminates the requirement for all Security Servers. The Connection
Servers will be load balanced. Authentication is handled by the F5 APM
module

|image14|

Figure 5 - Replace Security Servers

**Deploy the iApp**

1. Use the RDP function on your laptop to connect to the “corporate-pc”
   RDP server/workstation

   i. Same process as Task 1 if you are not still connected

2. Create a new Application Service by selecting iApps -> Application
   Services and selecting Create

   a. iApps >> Application Services

   b. Press the **Create** button

   c. Name the Application Service **VM\_LAB\_1\_PCOIP**

   d. Select **f5.vmware\_view.v1.5.1** for the template

+----+
+----+

iApp Configuration
~~~~~~~~~~~~~~~~~~

1. Review the **Welcome to the iAPP template for VMware Horizon View**

2. Note the **Template Options** (leave these default)

3. **Big-IP Access Policy Manager**

+--------------------------------------------------------------------------------------+-------------------------------------------------------------+
| Do you want to deploy BIG-IP Access Policy Manager?                                  | Yes, deploy BIG-IP Access Policy Manager                    |
+======================================================================================+=============================================================+
|                                                                                      |                                                             |
+--------------------------------------------------------------------------------------+-------------------------------------------------------------+
| Do you want to support browser based connections, including the View HTML5 client?   | Yes, support HTML 5 view clientless browser connections     |
+--------------------------------------------------------------------------------------+-------------------------------------------------------------+
| Should the BIG-IP system support RSA SecureID two-factor authentication              | NO, do not support RSA SecureID two-factor authentication   |
+--------------------------------------------------------------------------------------+-------------------------------------------------------------+
| Should the BIG\_IP system show a message to View users during logon                  | No, do not add a message during logon                       |
+--------------------------------------------------------------------------------------+-------------------------------------------------------------+
| What is the NetBIOS domain name for your environment                                 | demoisfun                                                   |
+--------------------------------------------------------------------------------------+-------------------------------------------------------------+
| Create a new AAA Server object **or select an existing one **                        | AD1                                                         |
+--------------------------------------------------------------------------------------+-------------------------------------------------------------+

1. SSL Encryption (Certs are preloaded for this exercise)

+----------------------------------------------------------+--------------------------------------------------------------+
| How should the BIG-IP system handle encrypted traffic?   | Terminate SSL for clients, re-encrypt…\ **(SSL-Bridging)**   |
+==========================================================+==============================================================+
| Which SSL certificate do you want to use?                | wild.demoisfun.net.crt                                       |
+----------------------------------------------------------+--------------------------------------------------------------+
| Which SSL private key do you want to use?                | wild.demoisfun.net.key                                       |
+----------------------------------------------------------+--------------------------------------------------------------+

1. **PC Over IP** (leave these default)

2. **Virtual Servers and Pools **

+------------------------------------------------------------------------------------+--------------------------------+
| What virtual server IP address do you want to use for remote, untrusted clients?   | 192.168.3.152                  |
+====================================================================================+================================+
| What is the associated service port?                                               | 443                            |
+------------------------------------------------------------------------------------+--------------------------------+
| What FQDN will clients use to access the View environment?                         | vmw-PROXY-VIEW.demoisfun.net   |
+------------------------------------------------------------------------------------+--------------------------------+
| Which Servers should be included in this pool?                                     | 192.168.10.212                 |
|                                                                                    |                                |
|                                                                                    | 192.168.10.213                 |
+------------------------------------------------------------------------------------+--------------------------------+

1. **Application Health**

   a. Use the pull down to select a standard https monitor

2. Press the **Finished** button

View the objects which were created by the iApp
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Select the Components tab at the top of the page

2. Note the increase in objects compared to Task 2 and Task 4

3. Are the pool members available?

4. Note the APM objects which were not present in the prior exercises

5. Review the remaining parameters (any questions)

Test the APM (PCoIP) functionality using both VMware View client and browser access methods
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Use the RDP function on your laptop to connect to the “home-pc” or use
the browser / local view client on your laptop to access
vmw-PROXY-VIEW.demoisfun.net

1.  Open View client and connect to the Virtual Server just created with
    iApp.

    i.  vmw-PROXY-VIEW.demoisfun.net (192.168.3.152)

    ii. IP address will not work—Certificate contains demoisfun.net

2.  When prompted for credentials

    a. Username: demo01

    b. Password: password

3.  If authentication fails

    a. Access Policy>>Manage Sessions

    b. Look at the entire session log

       i. More detail can be captured by enabling debug

    c. Note the clock skew error

    d. Use the “Corporate PC” to Connect to the F5 Big IP GUI
       https://192.168.10.216

    e. Set the time on the big IP to match the time on the corporate-pc

       i. date MMDDhhmm Keep in mind—the big IP uses military time 1:25
          PM = 13:25

    f. Return to step 1

4.  Select the View desktop (Agility)

5.  Use connect button to access

6.  Close the View client. (press the X in the upper right corner of the
    screen)

7.  https://192.168.3.152

    a. Username: demo01

    b. Password: password

8.  Select (Agility) from the webtop

9.  Select VMware View Client on the desktop

10. Note the error and inspect the certificate

11. Close the error box and cert view boxes

12. Open VMware View Client

    a. `vmw-PROXY-VIEW.demoisfun.net <https://vmw-PROXY-VIEW.demoisfun.net>`__

    b. Username:demo01

    c. Password: password

13. Select (Agility) from the webtop

14. Select VMware View client

15. When the desktop opens, open Notepad and enter some text (leave this
    on the screen)

16. Slide the blue RDP indicator to the left

17. Close the View client. (press the X in Agility Toolbar-was under the
    RD)

18. Use a supported browser to access the VDI (IE on the RDP
    workstation)

19. https://vmw-PROXY-VIEW.demoisfun.net

20. Select VMware Horizon View HTML access

21. Enter Credentials

    a. Username: demo01

    b. Password: password

22. Select (Agility)

23. Select HTML5 Client

24. Verify that the desktop functions

25. Close the browser

.. |image1| image:: /_static/image3.png
   :width: 5.40625in
   :height: 3.04167in
.. |image2| image:: /_static/image4.png
   :width: 2.04303in
   :height: 1.41146in
.. |image3| image:: /_static/image5.png
   :width: 1.48020in
   :height: 2.12500in
.. |image4| image:: /_static/image6.png
   :width: 4.94792in
   :height: 3.20833in
.. |image5| image:: /_static/image7.png
   :width: 3.32292in
   :height: 1.05208in
.. |image6| image:: /_static/image8.png
   :width: 3.15625in
   :height: 1.29167in
.. |image7| image:: /_static/image9.png
   :width: 4.37500in
   :height: 1.28125in
.. |image8| image:: /_static/image10.png
   :width: 5.25000in
   :height: 3.18750in
.. |image9| image:: /_static/image4.png
   :width: 2.04236in
   :height: 1.41111in
.. |image10| image:: /_static/image11.png
   :width: 1.32738in
   :height: 2.22370in
.. |image11| image:: /_static/image9.png
   :width: 4.37500in
   :height: 1.28125in
.. |image12| image:: /_static/image12.png
   :width: 4.63542in
   :height: 3.06250in
.. |image13| image:: /_static/image9.png
   :width: 4.37500in
   :height: 1.28125in
.. |image14| image:: /_static/image13.png
   :width: 5.67708in
   :height: 3.35417in
