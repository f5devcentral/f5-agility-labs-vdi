Task 1 – Access VMware View Desktop environment without F5 
==========================================================

Access the View Desktop using the View Client on the internal network. View Client points directly to a Connection Server. This step is to verify View is working and BIG-IP is not in the path. (Internal use case without F5 integration)


.. figure:: /_static/class1/image_lab1task1.png
   :scale: 100 %
   :align: center
   
   *Accessing Internal View Desktop*


#. From the *"corporate-pc"*.

#. On the desktop, launch the View Client.

   |image4|

#. Click ``New Server``

#. Type in the Connection Server address ``vmw-connsvr1a.demoisfun.net``

#. When prompted for credentials,
   - Username: ``demo01``
   - Password: ``password``

#. After authenticated, double-click the "Agility" icon to launch View Desktop.

#. In the Agility desktop, open Notepad and type in something.

#. Disconnect from Agility desktop by closing View client. (RDP Toolbar
   on top. May need to slide the blue RDP bar to the left in order to
   click the ``X`` in Agility Toolbar)

#. Open View client and try to reconnect to ``vmw-connsvr1a.
   demoisfun.net``

#. Notepad should still be on the desktop with the text you input.

#. Close the View client. (press the ``X`` in Agility Toolbar)

#. Keep the RDP session open for Task 2.


Task 2 – Load Balance Connection Servers
========================================

Use the F5 iApp for VMware View to configure a load balancing environment for the Connection Servers. This will increase the number of
Connection Servers available to internal users and load balance access to these resources (Internal use case with F5 load balancing)


.. figure:: /_static/class1/image_lab1task2.png
   :scale: 100 %
   :align: center

   *Load balance Connection Servers*


Deploy the iApp
---------------

#. From *"corporate-pc"*.

#. Use browser to access the F5 Admin GUI at ``https://f5-bigip1a.demoisfun.net``
     - Username: ``admin``
     - Password: ``password``

#. Create a new Application Service. On the left side menu,
   - iApps -> Application Services
   - Click the ``Create`` button
   - In the *Name* field, type in ``VM_LAB_1_LBCS``
   - In the *Template* pulldown, select ``f5.vmware_view.v1.5.4``

#. Review the *Welcome to the iAPP template for VMware Horizon View*

#. In *Big-IP Access Policy Manager* section

   +----------------------------------------------------------+------------------------------------------------------------------------+
   | Do you want to deploy BIG-IP Access Policy Manager?      | No, do not deploy BIG-IP Access Policy Manager                         |    +----------------------------------------------------------+------------------------------------------------------------------------+

#. In *SSL Encryption* section,
   +----------------------------------------------------------+------------------------------------------------------------------------+
   | How should the BIG-IP system handle encrypted traffic?   | ``Terminate SSL for clients, re-encrypt to View servers (SSL-bridging)`` |
   +----------------------------------------------------------+------------------------------------------------------------------------+
   | Which SSL certificate do you want to use?                | ``wild.demoisfun.net.crt`` (cert preloaded)                            |
   +----------------------------------------------------------+------------------------------------------------------------------------+
   | Which SSL private key do you want to use                 | ``wild.demoisfun.net.key`` (key preloaded)                             |
   +----------------------------------------------------------+------------------------------------------------------------------------+

#. In *Virtual Servers and Pools* section,
   +------------------------------------------------------------------------------------+----------------------------------------------+
   | What virtual server IP address do you want to use for remote, untrusted clients?   | ``192.168.10.150``                           |
   +------------------------------------------------------------------------------------+----------------------------------------------+
   | What FQDN will clients use to access the View environment                          | ``vmw-LB-CS.demoisfun.net``                  |
   +------------------------------------------------------------------------------------+----------------------------------------------+
   | Which Servers should be included in this pool                                      | ``192.168.10.210``                           |
   |                                                                                    | ``192.168.10.211``                           |
   +------------------------------------------------------------------------------------+----------------------------------------------+

#. In *Application Health* section,
   +------------------------------------------------------------------------------------+----------------------------------------------+
   | Create a new health monitor or use existing one                                ?   | ``https``                                    |
   +------------------------------------------------------------------------------------+----------------------------------------------+

#. Click the **Finished** button.


View the objects which were created by the iApp
-----------------------------------------------

#. Select the Components tab at the top of the page

   |image6|

#. Is the Virtual server available?

#. Are the pool members available?

#. What is the node status? Why?

#. Note that a persistence profile was created

   - Check Match Across Services

   - Press update

   - Note the error at the top of the page

#. Return to iApp -> Application Services

#. Review the remaining parameters (any questions)


View the properties of the iApp
-------------------------------

#. Select the Properties tab at the top of the page

   |image7|

#. In the *Application Service* pulldown, select ``Advanced``.

#. Select Advanced

#. Note the check in *Strict Updates* checkbox,

   - Is this related to the screen when editing the persistence profile?

   - What are the pro’s and con’s of unchecking this parameter?
   

Test the connection server load balancing using both VMware View client and browser access methods
--------------------------------------------------------------------------------------------------

#. From *"corporate-pc"*

#. Launch View client and connect to the Virtual Server just created with iApp.

#. Click ``New Server``

#. Type in the load balance address ``vmw-LB-CS.demoisfun.net``. (IP address will not work—Certificate contains demoisfun.net)

#. When prompted for credentials,
   - Username: ``demo01``
   - Password: ``password``

#. After authenticated, double-click the "Agility" icon to launch View Desktop.

#.  Verify that the Agility desktop functions

#.  Close the View client. (May need to slide the RDP Toolbar out of the way)

#.  Open IE and browse to ``https://vmw-LB-CS.demoisfun.net``

#.  Select ``VMware Horizon View HTML access``

#.  Log in
    - Username: ``demo01``
    - Password: ``password``

#.  Double click to launch Agility desktop

#.  At the Cert Warning, click "Continue to this website"

#.  Verify that the Agility desktop functions

#.  Close the IE browser window


Task 3 – Access View Desktop through the UAG Server
====================================================

Access View Desktop from external network through UAG. (External use case without F5 integration)

.. figure:: /_static/class1/image_lab1task3.png
   :scale: 100 %
   :align: center
   
   *Access View Desktop from external network*

#.  From the *"home-pc"*

    |image9|

#.  Launch View client and connect to the UAG.

#.  Click ``New Server``

#.  Type in the UAG address ``vmw-uag1a.demoisfun.net``.

#.  When prompted for credentials,
      - Username: ``demo01``
      - Password: ``password``

#.  After authenticated, double-click the "Agility" icon to launch View Desktop.

#.  Close the View client

#.  To access View desktop in browser, type in URL ``https://vmw-uag1a.demoisfun.net``

#.  Select ``VMware Horizon View HTML Access``
    - Username: ``demo01``
    - Password: ``password``

#.  Double-click Agility icon to launch desktop

#.  Accept Cert Warning

#.  Select ``Agility``

#.  Verify that the desktop functions

#.  Close the browser window


Task 4 – Load Balance UAG Servers
======================================

Use the F5 iApp for VMware View to configure a load balancing UAG's. This will increase the number of UAG servers available to external  users and load balance access to these resources (External use case with F5 load balancing)

This environment load balances 2 external facing UAG Servers. UAG's do not require a one-to-one mapping to Connection Servers. The Connection Server LB VIP created in Task 2 enables higher availability to the overall application.

.. figure:: /_static/class1/image_lab1task4.png
   :scale: 100 %
   :align: center
   
   *Load balance UAG's*


Deploy the iApp
---------------
#. From *"corporate-pc"*.

#. Use browser to access the F5 Admin GUI at ``https://f5-bigip1a.demoisfun.net``
     - Username: ``admin``
     - Password: ``password``

#. Create a new Application Service. On the left side menu,
   - iApps -> Application Services
   - Click the ``Create`` button
   - In the *Name* field, type in ``VM_LAB_1_LBUAG``
   - In the *Template* pulldown, select ``f5.vmware_view.v1.5.4``

#. Review the *Welcome to the iAPP template for VMware Horizon View*

#. In *Big-IP Access Policy Manager* section,
   +----------------------------------------------------------+------------------------------------------------------------------------+
   | Do you want to deploy BIG-IP Access Policy Manager?      | ``No, do not deploy BIG-IP Access Policy Manager``                     |    +----------------------------------------------------------+------------------------------------------------------------------------+

#. In *SSL Encryption* section,
   +----------------------------------------------------------+------------------------------------------------------------------------+
   | How should the BIG-IP system handle encrypted traffic?   | ``Terminate SSL for clients, re-encrypt to View servers (SSL-bridging)`` |
   +----------------------------------------------------------+------------------------------------------------------------------------+
   | Which SSL certificate do you want to use?                | ``wild.demoisfun.net.crt`` (cert preloaded)                            |
   +----------------------------------------------------------+------------------------------------------------------------------------+
   | Which SSL private key do you want to use                 | ``wild.demoisfun.net.key`` (key preloaded)                             |
   +----------------------------------------------------------+------------------------------------------------------------------------+

#. In *Virtual Servers and Pools* section,
   +------------------------------------------------------------------------------------+----------------------------------------------+
   | What virtual server IP address do you want to use for remote, untrusted clients?   | ``192.168.3.150``                            |
   +------------------------------------------------------------------------------------+----------------------------------------------+
   | What FQDN will clients use to access the View environment                          | ``vmw-LB-UAG.demoisfun.net``                 |
   +------------------------------------------------------------------------------------+----------------------------------------------+
   | Which Servers should be included in this pool                                      | ``192.168.3.214``                            |
   |                                                                                    | ``192.168.3.215``                            |
   +------------------------------------------------------------------------------------+----------------------------------------------+

#. In *Application Health* section,
   +------------------------------------------------------------------------------------+----------------------------------------------+
   | Create a new health monitor or use existing one?                                   | ``https``                                    |
   +------------------------------------------------------------------------------------+----------------------------------------------+

#. Click the **Finished** button.


View the objects which were created by the iApp
-----------------------------------------------

#. Select the Components tab at the top of the page

#. Is the Virtual server available?

#. Are the pool members available?

#. Is the Node Available?

#. Review the remaining parameters (any questions)


Configure UAG to use load balance address
-----------------------------------------

#. From *"corporate-pc"*

#. Open browser and go to *vmw-uag1a* administrative interface at ``https://192.168.10.214:9443/admin``

#. Log in as,
   - Username: ``admin``
   - Password: ``F5@gility``
   
#. On the right side, under *Configure Manually*, click ``Select``

#. In *General Settings -> Edge Service Settings*, click the ``Show`` button.

   |image_uaggear|

#. Next to *Horizon Settings*, click the ``Gear``

#. In the *Blast External URL* field, type in ``https://vmw-lb-uag.demoisfun.net:443``

#. In the *Tunnel External URL* field, type in ``https://vmw-lb-uag.demoisfun.net:443``

   |image_uagsettings|

#. Click ``Save``


Test the UAG Server load balancing using both VMware View client and browser access methods
-------------------------------------------------------------------------------------------

#. From *"home-pc"*

#. Launch View client and connect to the Virtual Server just created with iApp.

#. Click ``New Server``

#. Type in the load balance address ``vmw-LB-UAG.demoisfun.net``. (IP address will not work—Certificate contains demoisfun.net)

#. When prompted for credentials,
   - Username: ``demo01``
   - Password: ``password``

#. After authenticated, double-click the "Agility" icon to launch View Desktop.

#.  Verify that the Agility desktop functions

#.  Close the View client. (May need to slide the RDP Toolbar out of the way)

#.  Open IE and browse to ``https://vmw-LB-UAG.demoisfun.net``

#.  Select ``VMware Horizon View HTML access``

#.  Log in
    - Username: ``demo01``
    - Password: ``password``

#.  Double click to launch Agility desktop

#.  At the Cert Warning, click "Continue to this website"

#.  Verify that the Agility desktop functions

#.  Close the IE browser window



Task 5 – BIG-IP proxy View traffic in place of UAG
==================================================

In this configuration, we will consolidate authentication, load balance and proxy View traffic on a single BIG-IP. This can bypass the UAG's to access View desktop from external network. 

.. figure:: /_static/class1/image_lab1task5.png
   :scale: 100 %
   :align: center
   
   *Consolidating authentication, load balance and proxy View on a single BIG-IP*


Deploy the iApp
---------------

#. From *"corporate-pc"*.

#. Use browser to access the F5 Admin GUI at ``https://f5-bigip1a.demoisfun.net``
     - Username: ``admin``
     - Password: ``password``

#. Create a new Application Service. On the left side menu,
   - iApps -> Application Services
   - Click the ``Create`` button
   - In the *Name* field, type in ``VM_LAB_1_PROXY``
   - In the *Template* pulldown, select ``f5.vmware_view.v1.5.4``

#. Review the *Welcome to the iAPP template for VMware Horizon View*

#. In *BIG-IP Access Policy Manager* section,

   +---------------------------------------------------------------------+-------------------------------------------------------------+
   | Do you want to deploy BIG-IP Access Policy Manager?                 | ``Yes, deploy BIG-IP Access Policy Manager``                |
   +---------------------------------------------------------------------+-------------------------------------------------------------+
   | Do you want to support browser based connections,                   |                                                             |
   |including the View HTML5 client?                                     | ``Yes, support HTML 5 view clientless browser connections``    |
   +---------------------------------------------------------------------+-------------------------------------------------------------+
   | Should the BIG-IP system support RSA SecureID two-factor            |                                                             |
   |authentication                                                       | ``NO, do not support RSA SecureID two-factor authentication``   |
   +---------------------------------------------------------------------+-------------------------------------------------------------+
   | Should the BIG\_IP system show a message to View users during logon | ``No, do not add a message during logon``                   |
   +---------------------------------------------------------------------+-------------------------------------------------------------+
   | What is the NetBIOS domain name for your environment                | ``demoisfun``                                               |
   +---------------------------------------------------------------------+-------------------------------------------------------------+
   | Create a new AAA Server object **or select an existing one**        | ``AD1``                                                     |
   +---------------------------------------------------------------------+-------------------------------------------------------------+

#. **SSL Encryption (Certs are preloaded for this exercise)**

   +----------------------------------------------------------+--------------------------------------------------------------+
   | How should the BIG-IP system handle encrypted traffic?   | ``Terminate SSL for clients, re-encrypt…\ *(SSL-Bridging)*`` |
   +----------------------------------------------------------+--------------------------------------------------------------+
   | Which SSL certificate do you want to use?                | ``wild.demoisfun.net.crt``                                   |
   +----------------------------------------------------------+--------------------------------------------------------------+
   | Which SSL private key do you want to use?                | ``wild.demoisfun.net.key``                                   |
   +----------------------------------------------------------+--------------------------------------------------------------+

#. **Virtual Servers and Pools**

   +------------------------------------------------------------------------------------+------------------------------------+
   | What virtual server IP address do you want to use for remote, untrusted clients?   | ``192.168.3.152``                  |
   +------------------------------------------------------------------------------------+------------------------------------+
   | What FQDN will clients use to access the View environment?                         | ``vmw-PROXY-VIEW.demoisfun.net``   |
   +------------------------------------------------------------------------------------+------------------------------------+
   | Which Servers should be included in this pool?                                     | ``192.168.10.210``                 |
   |                                                                                    | ``192.168.10.211``                 |
   +------------------------------------------------------------------------------------+------------------------------------+

#. In *Application Health* section,
   +------------------------------------------------------------------------------------+----------------------------------------------+
   | Create a new health monitor or use existing one?                                   | ``https``                                    |
   +------------------------------------------------------------------------------------+----------------------------------------------+

#. Click the **Finished** button.


View the objects which were created by the iApp
-----------------------------------------------

#. Select the Components tab at the top of the page

#. Note the increase in objects compared to Task 2 and Task 4

#. Are the pool members available?

#. Note the APM objects which were not present in the prior exercises

#. Review the remaining parameters (any questions)


Test the APM (PCoIP) functionality using both VMware View client and browser access methods
-------------------------------------------------------------------------------------------

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
.. |image_uaggear| image:: /_static/class1/image_uaggear.png
   :scale: 100 %
.. |image_uagsetting| image:: /_static/class1/image_uagsetting.png
   :scale: 100 %
