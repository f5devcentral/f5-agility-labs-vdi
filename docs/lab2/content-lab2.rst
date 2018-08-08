Task 1 – Access Horizon Desktop environment without F5 
=============================================================

Access the Horizon Desktop using the Horizon Client on the internal network. Horizon Client points directly to a Connection Server. This step is to verify Horizon is working and BIG-IP is not in the path. (Internal use case without F5 integration)


.. figure:: /_static/class1/image_lab1task1.png
   :scale: 100 %
   :align: center
   
   *Accessing Internal Horizon Desktop*


#. From the *"corporate-pc"*

#. On the desktop, launch the Horizon Client

   |image4|

#. Click **New Server**

#. Type in the Connection Server address ``vmw-connsvr1a.demoisfun.net``

#. When prompted for credentials

   - Username: ``demo01``
   - Password: ``password``
   

#. After authenticated, double-click the **Agility** icon to launch Horizon Desktop

#. In the *Agility* desktop, open Notepad and type in something

#. Disconnect from *Agility* desktop by closing Horizon client. (RDP Toolbar
   on top. May need to slide the blue RDP bar to the left in order to
   click the **X** in Agility Toolbar)

#. Open *Horizon* client again, reconnect to ``vmw-connsvr1a.demoisfun.net`` and open *Agility* desktop

#. *Notepad* should still be on the desktop with the text you input

#. Close the *Horizon* client. (press the **X** in Agility Toolbar)

#. Keep the RDP session open for Task 2


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

#. From *"corporate-pc"*

#. Open IE to access the F5 Admin GUI at ``https://f5-bigip1a.demoisfun.net``
   
   - Username: ``admin``
   - Password: ``password``
   
#. Create a new Application Service. On the left side menu

   - Go to **iApps -> Application Services -> Applications**
   - On the right side of the GUI, click **Create** button
   - In *Name* field, type in ``lab2-lb-cs``
   - In *Template* pulldown, select ``f5.vmware_view.v1.5.4``

   .. NOTE:: The tables for iApp questions list just the values that need to change

   +--------------------------------------------------------------------+----------------------------------------------------+
   | **Welcome to the iAPP template for VMware Horizon**                | Please review                                      |
   +--------------------------------------------------------------------+----------------------------------------------------+
   | **Big-IP Access Policy Manager**                                                                                        |
   +--------------------------------------------------------------------+----------------------------------------------------+
   | Do you want to deploy BIG-IP Access Policy Manager?                | *No, do not deploy BIG-IP Access...*               |
   +--------------------------------------------------------------------+----------------------------------------------------+
   | **SSL Encryption**                                                                                                      |
   +--------------------------------------------------------------------+----------------------------------------------------+
   | How should the BIG-IP system handle encrypted traffic?             | *Terminate SSL for clients, ...(SSL-bridging)*     |
   +--------------------------------------------------------------------+----------------------------------------------------+
   | Which SSL certificate do you want to use?                          | *wild.demoisfun.net.crt* (Cert preloaded)          |
   +--------------------------------------------------------------------+----------------------------------------------------+
   | Which SSL private key do you want to use                           | *wild.demoisfun.net.key* (Key preloaded)           |
   +--------------------------------------------------------------------+----------------------------------------------------+
   | **Virtual Servers and Pools**                                                                                           |
   +--------------------------------------------------------------------+----------------------------------------------------+
   | What virtual server IP address...?                                 | ``192.168.10.150``                                 |
   +--------------------------------------------------------------------+----------------------------------------------------+
   | What FQDN will clients use to access the View environment?         | ``vmw-LB-CS.demoisfun.net``                        |
   +--------------------------------------------------------------------+----------------------------------------------------+
   | Which Servers should be included in this pool                      | ``192.168.10.210``                                 |
   |                                                                    |                                                    |
   |                                                                    | ``192.168.10.211``                                 |
   +--------------------------------------------------------------------+----------------------------------------------------+
   | **Application Health**                                                                                                  |
   +--------------------------------------------------------------------+----------------------------------------------------+
   | Create a new health monitor or use existing one?                   | ``https``                                          |
   +--------------------------------------------------------------------+----------------------------------------------------+

#. Click the **Finished** button


View the objects which were created by the iApp
-----------------------------------------------

#. Click **Components** tab at the top of the page

   |image6|

#. Is the Virtual server available?

#. Are the pool members available?

#. What is the node status? Why?

#. Note that a persistence profile was created

   - Click **lab2-lb-cs** to edit the object
   - Check **Match Across Services**
   - Click **Update**
   - Note the error at the top of the page


#. Return to *iApp -> Application Services* -> *lab2-lb-cs*

#. Review the remaining parameters (any questions)


View the properties of the iApp
-------------------------------

#. Select the Properties tab at the top of the page

   |image7|

#. In the *Application Service* pulldown, select **Advanced**

#. Note the *Strict Updates* checkbox is selected
   
   - Is this related to the error observed when editing the persistence profile?
   - What are the pro’s and con’s of unchecking this parameter?
   

Test the connection server load balancing using both VMware View client and browser access methods
--------------------------------------------------------------------------------------------------

#. From *"corporate-pc"*

#. Launch View client and connect to the Virtual Server just created with iApp

#. Click **New Server**

#. Type in the load balanced address ``vmw-LB-CS.demoisfun.net``. (IP address will not work—Certificate contains demoisfun.net)

#. When prompted for credentials
     
   - Username: ``demo01``
   - Password: ``password``


#. Open the **Agility** desktop

#. Verify that the *Agility* desktop functions

#. Close the View client

#. Open a new Tab IE and browse to ``https://vmw-LB-CS.demoisfun.net``

#. Click on **VMware Horizon HTML Access**

#. Log in

   - Username: ``demo01``
   - Password: ``password``


#.  Open **Agility** desktop

#.  At the Cert Warning, click "Continue to this website..."

#.  Verify that the Agility desktop functions

#.  Close the IE *VMWare Horizon* tab


Task 3 – Access Horizon Desktop through the UAG Server
======================================================

Access Horizon Desktop from external network through UAG. (External use case without F5 integration)

.. figure:: /_static/class1/image_lab1task3.png
   :scale: 100 %
   :align: center
   
   *Access Horizon Desktop from external network*

#.  From *"home-pc"*

    |image9|

#.  On the desktop, Launch Horizon client and connect to the UAG

#.  Click **New Server**

#.  Type in the UAG address ``vmw-uag1a.demoisfun.net``

#.  When prompted for credentials

    - Username: ``demo01``
    - Password: ``password``

#.  Open the **Agility** desktop

#.  Close the *Horizon* client

#.  To access *Horizon* desktop in IE, type in URL ``https://vmw-uag1a.demoisfun.net``

#.  Select **VMware Horizon HTML Access**

    - Username: ``demo01``
    - Password: ``password``

#.  Open **Agility** desktop

#.  Verify that the desktop functions

#.  Close the IE *VMware Horizon* tab


Task 4 – Load Balance UAG Servers
======================================

Use the F5 iApp for VMware Horizon to configure a load balancing UAG's. This will increase the number of UAG servers available to external  users and load balance access to these resources (External use case with F5 load balancing)

This environment load balances 2 external facing UAG Servers. UAG's do not require a one-to-one mapping to Connection Servers. The Connection Server LB VIP created in Task 2 enables higher availability to the overall application.

.. figure:: /_static/class1/image_lab1task4.png
   :scale: 100 %
   :align: center
   
   *Load balance UAG's*


Deploy the iApp
---------------
#. From *"corporate-pc"*

#. Open IE to access the F5 Admin GUI at ``https://f5-bigip1a.demoisfun.net``

   - Username: ``admin``
   - Password: ``password``

#. Create a new Application Service. On the left side menu

   - Go to **iApps -> Application Services -> Applications**
   - On the right side of the GUI, click the **Create** button
   - In the *Name* field, type in ``lab2-lb-uag``
   - In the *Template* pulldown, select ``f5.vmware_view.v1.5.4``
     
   +-----------------------------------------------------------------------------------------------------------------------------------+
   | **Big-IP Access Policy Manager**                                                                                                  |
   +------------------------------------------------------------------------------+----------------------------------------------------+
   | Do you want to deploy BIG-IP Access Policy Manager?                          | *No, do not deploy BIG-IP Access Policy Manager*   |
   +------------------------------------------------------------------------------+----------------------------------------------------+
   | **SSL Encryption**                                                                                                                |
   +------------------------------------------------------------------------------+----------------------------------------------------+
   | How should the BIG-IP system handle encrypted traffic?                       | *Terminate SSL for clients,...(SSL-bridging)*      |
   +------------------------------------------------------------------------------+----------------------------------------------------+
   | Which SSL certificate do you want to use?                                    | *wild.demoisfun.net.crt*                           |
   +------------------------------------------------------------------------------+----------------------------------------------------+
   | Which SSL private key do you want to use                                     | *wild.demoisfun.net.key*                           |
   +------------------------------------------------------------------------------+----------------------------------------------------+
   | **Virtual Servers and Pools**                                                                                                     |
   +------------------------------------------------------------------------------+----------------------------------------------------+
   | What virtual server IP address...for remote, untrusted clients?              | ``192.168.3.150``                                  |
   +------------------------------------------------------------------------------+----------------------------------------------------+
   | What FQDN will clients use to access the View environment                    | ``vmw-LB-UAG.demoisfun.net``                       |
   +------------------------------------------------------------------------------+----------------------------------------------------+
   | Which Servers should be included in this pool                                | ``192.168.3.214``                                  |
   |                                                                              |                                                    |
   |                                                                              | ``192.168.3.215``                                  |
   +------------------------------------------------------------------------------+----------------------------------------------------+
   | **Application Health**                                                                                                            |
   +------------------------------------------------------------------------------+----------------------------------------------------+
   | Create a new health monitor or use existing one?                             | *https*                                            |
   +------------------------------------------------------------------------------+----------------------------------------------------+

#. Click **Finished** button


View the objects which were created by the iApp
-----------------------------------------------

#. Click **Components** tab at the top of the page

#. Is the Virtual server available?

#. Are the pool members available?

#. Is the Node available?

#. Review the remaining parameters (any questions)


Configure UAG to use load balance address
-----------------------------------------

#. From *"corporate-pc"*

#. Open new tab in IE and go to *vmw-uag1a* administrative interface at
   ``https://192.168.10.214:9443/admin``

#. Log in as

   - Username: ``admin``
   - Password: ``F5@gility``
   
#. On the right side, under *Configure Manually*, click **Select**

#. In *General Settings -> Edge Service Settings*, click the **Show** button

   |image_uaggear|

#. Next to *Horizon Settings*, click the **Gear**

#. In the *Blast External URL* field, type in ``https://vmw-lb-uag.demoisfun.net:443``

#. In the *Tunnel External URL* field, type in ``https://vmw-lb-uag.demoisfun.net:443``

   |image_uagsetting|

#. Click **Save**

#. Make same changes for the other UAG *vmw-uag1b* at ``https://192.168.10.215:9443/admin``


Test the UAG load balancing using Horizon and HTML5 client access methods
-------------------------------------------------------------------------

#. From *"home-pc"*

#. Launch View client and connect to the Virtual Server just created with iApp.

#. Click **New Server**

#. Type in the load balance address ``vmw-LB-UAG.demoisfun.net``

#. When prompted for credentials

   - Username: ``demo01``
   - Password: ``password``
     
#. Open the **Agility** desktop

#. Verify that the *Agility* desktop functions

#. Close the View client

#. Open IE and browse to ``https://vmw-LB-UAG.demoisfun.net``

#. Select **VMware Horizon HTML Access**

#. Log in

   - Username: ``demo01``
   - Password: ``password``
     
#.  Open **Agility** desktop

#.  Verify that *Agility* desktop functions

#.  Close IE *VMware Horizon* tab



Task 5 – BIG-IP proxy View traffic in place of UAG
==================================================

In this configuration, we will consolidate authentication, load balance and proxy View traffic on a single BIG-IP. This can bypass the UAG's to access View desktop from external network. 

.. figure:: /_static/class1/image_lab1task5.png
   :scale: 100 %
   :align: center
   
   *Consolidating authentication, load balance and proxy View on a single BIG-IP*


Deploy the iApp
---------------

#. From *"corporate-pc"*

#. Open IE to access the F5 Admin GUI at ``https://f5-bigip1a.demoisfun.net``

   - Username: ``admin``
   - Password: ``password``

#. Create a new Application Service. On the left side menu

   - Go to **iApps -> Application Services -> Applications**
   - On the right side of the GUI, click the **Create** button
   - In the *Name* field, type in ``lab2-proxy``
   - In the *Template* pulldown, select ``f5.vmware_view.v1.5.4``
   
   +-----------------------------------------------------------------------------------------------------------------------------------+
   | **BIG-IP Access Policy Manager**                                                                                                  |
   +------------------------------------------------------------------------------+----------------------------------------------------+
   | Do you want to deploy BIG-IP Access Policy Manager?                          | *Yes, deploy BIG-IP Access Policy Manager*         |
   +------------------------------------------------------------------------------+----------------------------------------------------+
   | Do you want to support browser based connections...HTML5 client?             | *Yes, support HTML 5 view clientless browser*      |
   +------------------------------------------------------------------------------+----------------------------------------------------+
   | What is the NetBIOS domain name for your environment?                        | ``demoisfun``                                      |
   +------------------------------------------------------------------------------+----------------------------------------------------+
   | Create a new AAA Server object or select an existing one                     | *AD1*                                              |
   +------------------------------------------------------------------------------+----------------------------------------------------+
   | **SSL Encryption* section**                                                                                                       |
   +------------------------------------------------------------------------------+----------------------------------------------------+
   | How should the BIG-IP system handle encrypted traffic?                       | *Terminate SSL for clients,...(SSL-Bridging)*      |
   +------------------------------------------------------------------------------+----------------------------------------------------+
   | Which SSL certificate do you want to use?                                    | ``wild.demoisfun.net.crt``                         |
   +------------------------------------------------------------------------------+----------------------------------------------------+
   | Which SSL private key do you want to use?                                    | ``wild.demoisfun.net.key``                         |
   +------------------------------------------------------------------------------+----------------------------------------------------+
   | **Virtual Servers and Pools**                                                                                                     |
   +------------------------------------------------------------------------------+----------------------------------------------------+
   | What virtual server IP address...for remote, untrusted clients?              | ``192.168.3.152``                                  |
   +------------------------------------------------------------------------------+----------------------------------------------------+
   | What FQDN will clients use to access the View environment?                   | ``vmw-PROXY-VIEW.demoisfun.net``                   |
   +------------------------------------------------------------------------------+----------------------------------------------------+
   | Which Servers should be included in this pool?                               | ``192.168.10.210``                                 |
   |                                                                              |                                                    |
   |                                                                              | ``192.168.10.211``                                 |
   +------------------------------------------------------------------------------+----------------------------------------------------+
   | **Application Health**                                                                                                            |
   +------------------------------------------------------------------------------+----------------------------------------------------+
   | Create a new health monitor or use existing one?                             | *https*                                            |
   +------------------------------------------------------------------------------+----------------------------------------------------+

#. Click **Finished** button


View the objects which were created by the iApp
-----------------------------------------------

#. Click **Components** tab at the top of the page

#. Note the increase in objects compared to Task 2 and Task 4

#. Are the pool members available?

#. Note the APM objects which were not present in the prior exercises

#. Review the remaining parameters (any questions)


Test the APM webtop using Horizon and HTML5 client access methods
-----------------------------------------------------------------

#. From *"home-pc"*

#. Launch **View Client**

   - Click **New Server** 
   - Type in proxy address ``vmw-PROXY-VIEW.demoisfun.net``
   
#. When prompted for credentials

   - Username: ``demo01``
   - Password: ``password``
   
   
#. Click **Agility** icon

#. Close the session by clicking the X in the upper  toolbar

#. Open IE and browse to ``https://vmw-PROXY-VIEW.demoisfun.net``

#. Select **VMware Horizon View HTML Access**

#. Enter credential

   - Username: ``demo01``
   - Password: ``password``

#. Click **Agility** to launch desktop

#. With APM Webtop, user has the option to choose client at launch time. Select **HTML5 Client**

#. Verify that the desktop functions

#. Close IE

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
