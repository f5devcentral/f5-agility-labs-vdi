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

#. Keep the RDP session open for Task 2

Task 2 – Load Balance Connection Servers
----------------------------------------

Use the F5 iApp for VMware View to configure a load balancing
environment for the Connection Servers. This will increase the number of
Connection Servers available to internal users and load balance access
to these resources (Internal use case with F5 load balancing)

|image5|

Figure 3 - Load balance Connection Servers

**Deploy the iApp**

#. From "corporate-pc".

#. Use browser to access the F5 Admin GUI

   - ``https://f5-bigip1a.demoisfun.net``

     - Username: ``admin``

     - Password: ``password``

#. Create a new Application Service

   - iApps >> Application Services

   - Press the **Create** button

   - Name the Application Service ``VM_LAB_1_LBCS``

   - Select ``f5.vmware_view.v1.5.1`` for the template

#. Review the **Welcome to the iAPP template for VMware Horizon View**

#. Note the **Template Options** (leave these default)

#. **Big-IP Access Policy Manager** (Set this to **No** for this
   exercise)

#. **SSL Encryption** (Certs are preloaded for this exercise)

   +----------------------------------------------------------+------------------------------------------------------------------------+
   | How should the BIG-IP system handle encrypted traffic?   | Terminate SSL for clients, re-encrypt to View servers (SSL-bridging)   |
   +==========================================================+========================================================================+
   | Which SSL certificate do you want to use?                | wild.demoisfun.net.crt                                                 |
   +----------------------------------------------------------+------------------------------------------------------------------------+
   | Which SSL private key do you want to use                 | wild.demoisfun.net.key                                                 |
   +----------------------------------------------------------+------------------------------------------------------------------------+

#. **PC Over IP** (leave these default – No PCoIP connections…)

#. **Virtual Servers and Pools**

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

#. **Client Optimization** (leave these default—Do not compress…)

#. **Application Health**

   - Use the pulldown to select a standard https monitor

#. Press the **Finished** button

View the objects which were created by the iApp
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#. Select the Components tab at the top of the page

   |image6|

#. Is the Virtual server available?

#. Are the pool members available?

#. What is the node status? Why?

#. Note that a persistence profile was created

   - Check Match Across Services

   - Press update

   - Note the error at the top of the page

#. Return to iApp>>Application Services

#. Review the remaining parameters (any questions)

View the properties of the iApp
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#. Select the Properties tab at the top of the page

   |image7|

#. Use the pull down next to Application Service:

#. Select Advanced

#. Note the check in Strict Updates

   - Is this related to the screen when editing the persistence profile?

   - What are the pro’s and con’s of unchecking this parameter?

Test the connection server load balancing using both VMware View client and browser access methods. 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#.  From "corporate-pc"

#.  Open View client and connect to the Virtual Server just created with
    iApp.

    - \+ New Server

      - ``vmw-LB-CS.demoisfun.net``

      - Connect Button

        - IP address will not work—Certificate contains demoisfun.net

#.  When prompted for credentials

    - Username: ``demo01``

    - Password: ``password``

    - Login Button

#.  Double-click Agility icon to launch View desktop

#.  Verify that the Agility desktop functions

#.  Close the View client. (May need to slide the RDP Toolbar out of the
    way)

#.  Open IE and browse to ``https://vmw-LB-CS.demoisfun.net``

#.  Select VMware Horizon View HTML access

#.  Log in

    - Username: ``demo01``

    - Password: ``password``

#.  Double click to launch Agility desktop

#.  At the Cert Warning, click "Continue to this website"

#.  Verify that the Agility desktop functions

#.  Close the IE browser window

Task 3 – Access View Desktop through Security Server
----------------------------------------------------

Test the functional VMware View environment using external Security
Servers. (External use case without F5 integration)

This environment shows a user connecting to a native VMware security
server which is statically mapped to a VMware connection server. This is
a non-redundant external access model

|image8|

Figure 4 - Access external View Desktop

#.  From the "home-pc"

    |image9|

#.  Use the VMware Horizon View client to access the security server

    - \+ New Server

    - Security Server address ``vmw-secursvr1a.demoisfun.net``

    - Press Connect Button

#.  When prompted for credentials

    - Username: ``demo01``

    - Password: ``password``

#.  Double-click Agility icon to launch desktop

#.  Close the View client

#.  Access the application through your browser 
    ``https://vmw-secursvr1a.demoisfun.net``

#.  Select VMware Horizon View HTML access

    - Username: ``demo01``

    - Password: ``password``

#.  Double-click Agility icon to launch desktop

#.  Accept Cert at warning

#.  Select (Agility)

#.  Verify that the desktop functions

#.  Close the browser window

Task 4 – Load Balance Security Servers
--------------------------------------

Use the F5 iApp for VMware View to configure a load balancing
environment for the Security Servers. This will increase the number of
Security Servers available to internal users and load balance access to
these resources (External use case with F5 load balancing)

This environment load balances 2 external facing Security Servers. These
Security Servers are directly mapped to 2 existing connection servers in
the environment (not the 2 Connections Servers that are load balances in
the steps above)

|image10|

Figure 5 - Load balance Security Servers

**Deploy the iApp**

#. From "corporate-pc"

#. Create a new Application Service by selecting

   - iApps >> Application Services

   - Press the **Create** button

   - Name the Application Service ``VM_LAB_1_LBSS``

   - Select ``f5.vmware_view.v1.5.1`` for the template

#. Review the **Welcome to the iAPP template for VMware Horizon View**

#. Note the **Template Options** (leave these default)

#. **Big-IP Access Policy Manager** (Set this to **No** for this
   exercise)

#. **SSL Encryption** (Certs are preloaded for this exercise)

   +----------------------------------------------------------+--------------------------------------------------------------+
   | How should the BIG-IP system handle encrypted traffic?   | Terminate SSL for clients, re-encrypt…\ **(SSL-Bridging)**   |
   +==========================================================+==============================================================+
   | Which SSL certificate do you want to use?                | wild.demoisfun.net.crt                                       |
   +----------------------------------------------------------+--------------------------------------------------------------+
   | Which SSL private key do you want to use?                | wild.demoisfun.net.key                                       |
   +----------------------------------------------------------+--------------------------------------------------------------+

#. **PC Over IP** (leave these default – No PCoIP connections…)

#. **Virtual Servers and Pools**

   +------------------------------------------------------------------------------------+---------------------------+
   | What virtual server IP address do you want to use for remote, untrusted clients?   | 192.168.3.150             |
   +====================================================================================+===========================+
   | What FQDN will clients use to access the View environment?                         | vmw-LB-SS.demoisfun.net   |
   +------------------------------------------------------------------------------------+---------------------------+
   | Which Servers should be included in this pool?                                     | 192.168.3.214             |
   |                                                                                    |                           |
   |                                                                                    | 192.168.3.215             |
   +------------------------------------------------------------------------------------+---------------------------+

#. **Application Health**

   - Use the pulldown to select a standard https monitor

#. Press the **Finished** button

View the objects which were created by the iApp
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#. Select the Components tab at the top of the page

#. Is the Virtual server available?

#. Are the pool members available?

#. Is the Node Available?

#. Review the remaining parameters (any questions)

Test the Security Server load balancing using both VMware View client and browser access methods
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#.  From "home-pc"

#.  Open View client and connect to the Virtual Server just created with
    iApp.

    - \+ New Server

      - vmw-LB-SS.demoisfun.net (192.168.3.150)

      - Press the Connect button

      - IP address will not work—Certificate contains demoisfun.net

#.  When prompted for credentials

    - Username: ``demo01``

    - Password: ``password``

#.  Double-click Agility icon to launch desktop

#.  Verify the desktop functions

#.  Close the View client

#.  Open IE and browser to

    - ``https://vmw-LB-SS.demoisfun.net``

#.  Select VMware Horizon View HTML access

#.  Enter Credentials

    - Username: ``demo01``

    - Password: ``password``

#.  Select (Agility)

#.  Accept Cert warning

#.  Select (Agility)

#.  Verify that the desktop functions

#.  Close the browser window

Task 5 – Replace Security Servers and leverage APM as a PCOIP proxy
-------------------------------------------------------------------

This environment will utilize Big-IP as a PCOIP Proxy. This eliminates
the requirement for all Security Servers. The Connection Servers will be
load balanced. Authentication is handled by the F5 APM module

|image11|

Figure 6 - Replace Security Servers

**Deploy the iApp**

#. From "corporate-pc"

#. Create a new Application Service by selecting iApps -> Application
   Services and selecting Create

   - iApps >> Application Services

   - Press the **Create** button

   - Name the Application Service ``VM_LAB_1_PCOIP``

   - Select ``f5.vmware_view.v1.5.1`` for the template

iApp Configuration
~~~~~~~~~~~~~~~~~~

#. Review the **Welcome to the iAPP template for VMware Horizon View**

#. Note the **Template Options** (leave these default)

#. **BIG-IP Access Policy Manager**

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
   | Create a new AAA Server object **or select an existing one**                         | AD1                                                         |
   +--------------------------------------------------------------------------------------+-------------------------------------------------------------+

#. **SSL Encryption (Certs are preloaded for this exercise)**

   +----------------------------------------------------------+--------------------------------------------------------------+
   | How should the BIG-IP system handle encrypted traffic?   | Terminate SSL for clients, re-encrypt…\ **(SSL-Bridging)**   |
   +==========================================================+==============================================================+
   | Which SSL certificate do you want to use?                | wild.demoisfun.net.crt                                       |
   +----------------------------------------------------------+--------------------------------------------------------------+
   | Which SSL private key do you want to use?                | wild.demoisfun.net.key                                       |
   +----------------------------------------------------------+--------------------------------------------------------------+

#. **PC Over IP** (leave these default)

#. **Virtual Servers and Pools**

   +------------------------------------------------------------------------------------+--------------------------------+
   | What virtual server IP address do you want to use for remote, untrusted clients?   | 192.168.3.152                  |
   +====================================================================================+================================+
   | What FQDN will clients use to access the View environment?                         | vmw-PROXY-VIEW.demoisfun.net   |
   +------------------------------------------------------------------------------------+--------------------------------+
   | Which Servers should be included in this pool?                                     | 192.168.10.212                 |
   |                                                                                    |                                |
   |                                                                                    | 192.168.10.213                 |
   +------------------------------------------------------------------------------------+--------------------------------+

#. **Application Health**

   - Use the pull down to select a standard https monitor

#. Press the **Finished** button

View the objects which were created by the iApp
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#. Select the Components tab at the top of the page

#. Note the increase in objects compared to Task 2 and Task 4

#. Are the pool members available?

#. Note the APM objects which were not present in the prior exercises

#. Review the remaining parameters (any questions)

Test the APM (PCoIP) functionality using both VMware View client and browser access methods
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#.  From "home-pc"

#.  Open IE and browse to ``https://vmw-PROXY-VIEW.demoisfun.net``

    - Username: ``demo01``

    - Password: ``password``

#.  Click Agility on APM webtop

#.  Select VMware View Client

#.  Note the error and inspect the certificate

#.  Close the error box and cert view boxes

#.  Close the View client

#.  Open IE and browse to

    - ``https://vmw-PROXY-VIEW.demoisfun.net``

#.  Select VMware Horizon View HTML access

#.  Enter Credentials

    - Username: ``demo01``

    - Password: ``password``

#.  Click Agility

#.  Select HTML5 Client

#.  Verify that the desktop functions

#.  Close the browser

.. |image3| image:: /_static/class1/image5.png
   :width: 5.40625in
   :height: 3.04167in
.. |image4| image:: /_static/class1/image6.png
   :width: 2.47015in
   :height: 1.73397in
.. |image5| image:: /_static/class1/image7.png
   :width: 4.94792in
   :height: 3.20833in
.. |image6| image:: /_static/class1/image8.png
   :width: 3.32292in
   :height: 1.05208in
.. |image7| image:: /_static/class1/image9.png
   :width: 3.15625in
   :height: 1.29167in
.. |image8| image:: /_static/class1/image10.png
   :width: 5.25000in
   :height: 3.18750in
.. |image9| image:: /_static/class1/image11.png
   :width: 1.29861in
   :height: 1.88819in
.. |image10| image:: /_static/class1/image12.png
   :width: 4.63542in
   :height: 3.06250in
.. |image11| image:: /_static/class1/image13.png
   :width: 5.67708in
   :height: 3.35417in
