Task 1 – Access XenDesktop without F5
=====================================

.. figure:: /_static/class1/image_lab2task1.png
   :scale: 100 %
   :align: center
   
   *Access XenDesktop through StoreFront*

#. From *corporate-pc*

#. Open IE and browse to Citrix Storefront at,
   ``http://ctx-sf1a.demoisfun.net/Citrix/AgilityStoreWeb/``

.. NOTE:: Storefront first launch takes a bit of time

#. When prompted for credentials

   - Username: ``demoisfun\demo01``
   - Password: ``password``

#. Click **Agility** to launch XenDesktop

#. Citrix *Desktop Viewer* launches and connects to XenDesktop

#. Verify virtual desktop function

#. In *Citrix Agility* desktop, click Start and Logoff

#. Log off the Citrix receiver client using the **01 Demo** pulldown in the
   upper right corner

#. Close IE


Task 2 – Load Balance StoreFront
================================

.. figure:: /_static/class1/image_lab2task2.png
   :scale: 100 %
   :align: center
   
   *Load balance StoreFront*


Deploy the iApp
---------------

#. From *"corporate-pc"*

#. Create a new Application Service.

   - **iApps -> Application Services -> Applications**
   - Click the **Create** button
   - In the *Name* field, type in ``lab3-lb-sf``
   - In the *Template* pulldown, select **f5.citrix_vdi.v2.4.4**


   +---------------------------------------------------------------------------+-------------------------------------------------------+
   | **Welcome to the iApp template for XenDesktop and XenApp**                | *Review this section*                                 |
   +---------------------------------------------------------------------------+-------------------------------------------------------+
   | **General**                                                                                                                       |
   +---------------------------------------------------------------------------+-------------------------------------------------------+
   | Use APM to securely proxy application (ICA)...Citrix environment?         | *Yes, Proxy ICA traffic...with BIG-IP*                |
   +---------------------------------------------------------------------------+-------------------------------------------------------+
   | What is the Active Directory NetBIOS Domain Name...Citrix servers?        | demoisfun                                             |
   +---------------------------------------------------------------------------+-------------------------------------------------------+
   | **BIG-IP Access Policy Manager**                                                                                                  |
   +---------------------------------------------------------------------------+-------------------------------------------------------+
   | Do you want to replace Citrix Web Interface...with the BIG-IP system?     | *No, do not replace…*                                 |
   +---------------------------------------------------------------------------+-------------------------------------------------------+
   | Create a new AAA object or select an existing one?                        | *AD1*                                                 |
   +---------------------------------------------------------------------------+-------------------------------------------------------+
   | **Virtual Server for Web Interface or StoreFront servers**                                                                        |
   +---------------------------------------------------------------------------+-------------------------------------------------------+
   | How should the BIG-IP system handle encrypted traffic to...servers?       | *Terminate SSL for Clients...*(SSL offload)*          |
   +---------------------------------------------------------------------------+-------------------------------------------------------+
   | Which SSL certificate do you want to use?                                 | *wild.demoisfun.net.crt*                              |
   +---------------------------------------------------------------------------+-------------------------------------------------------+
   | Which SSL private key do you want to use?                                 | *wild.demoisfun.net.key*                              |
   +---------------------------------------------------------------------------+-------------------------------------------------------+
   | What IP address will clients use to access...or the F5 Webtop?            | ``192.168.3.160``                                     |
   +---------------------------------------------------------------------------+-------------------------------------------------------+
   | Did you deploy Citrix StoreFront?                                         | *Yes, ...StoreFront 3.0 or above*                     |
   +---------------------------------------------------------------------------+-------------------------------------------------------+
   | What is the URI used on StoreFront...for XenApp or XenDesktop?            | ``/Citrix/AgilityStoreWeb/``                          |
   +---------------------------------------------------------------------------+-------------------------------------------------------+
   | **Web Interface or StoreFront servers**                                                                                           |
   +---------------------------------------------------------------------------+-------------------------------------------------------+
   | What DNS name will clients use to reach the...StoreFront servers?         | ``ctx-LB-SF.demoisfun.net``                           |
   +---------------------------------------------------------------------------+-------------------------------------------------------+
   | Which port...for Web Interface or StoreFront HTTP traffic?                | ``80``                                                |
   +---------------------------------------------------------------------------+-------------------------------------------------------+
   | What are the IP addresses of your Web Interface or StoreFront servers?    | ``192.168.10.220``                                    |
   |                                                                           |                                                       |
   |                                                                           | ``192.168.10.221``                                    |
   +---------------------------------------------------------------------------+-------------------------------------------------------+
   | Which Monitor do you want to use                                          | *http*                                                |
   +---------------------------------------------------------------------------+-------------------------------------------------------+
   | **Virtual Server for XML Broker or Desktop Delivery Controller (DDC) Servers**                                                    |
   +---------------------------------------------------------------------------+-------------------------------------------------------+
   | What IP address do you want to use for the...DDC farm virtual server?     | ``192.168.10.161``                                    |
   +---------------------------------------------------------------------------+-------------------------------------------------------+
   | How will requests from the Web Interface or StoreFront servers arrive?    | *XML Broker...requests will arrive unencrypted (HTTP)*|
   +---------------------------------------------------------------------------+-------------------------------------------------------+
   | **XML Broker or DDC Servers**                                                                                                     |
   +---------------------------------------------------------------------------+-------------------------------------------------------+
   | What are the IP addresses of your XML Broker or DDC servers?              | ``192.168.10.222``                                    |
   |                                                                           |                                                       |
   |                                                                           | ``192.168.10.223``                                    |
   +---------------------------------------------------------------------------+-------------------------------------------------------+
   | Which monitor do you want to use?                                         | *http*                                                |
   +---------------------------------------------------------------------------+-------------------------------------------------------+

#. Click **Finished** button


Test Connectivity
-----------------

#. From *"home-pc"*
   
#. OpenIE and go to the StoreFront load balanced address,
   ``http://ctx-lb-sf.demoisfun.net``

#. When prompted for credentials

   - Username: ``demo01``
   - Password: ``password``

#. Click **Agility** to launch XenDesktop

#. In the *Citrix Agility* desktop, click **Start -> Disconnect**

#. Log off StoreFront using the **01 Demo** pulldown in the upper right corner


Task 3 – BIG-IP Replaces StoreFront
===================================

.. figure:: /_static/class1/image_lab2task3.png
   :scale: 100 %
   :align: center
   
   *BIG-IP replaces StoreFront*


Deploy the iApp
---------------

#. From *"corporate-pc"*

#. Create a new Application Service.

   - **iApps -> Application Services -> Applications**
   - Click **lab3-lb-sf**
   - Click **Reconfigure** link near the top
   
   +-------------------------------------------------------------------------+--------------------------+
   | **BIG-IP Access Policy Manager**                                                                   |
   +-------------------------------------------------------------------------+--------------------------+
   | Do you want to replace Citrix Web Interface...with the BIG-IP system?   | *Yes, replace Citrix…*   |
   +-------------------------------------------------------------------------+--------------------------+

#. Scroll through the template and note that the storefront pool members are no longer present (not needed)

#. Press the **Finished** button


Test Connectivity
-----------------

#.  From *"home-pc"*

#.  If IE is still open, close to clear cache.

#.  Open IE and browse to ``http://ctx-lb-sf.demoisfun.net``

#.  When prompted for credentials

    - Username: ``demo01``
    - Password: ``password``

#.  APM webtop is displayed with *Agility* icon

#.  Click on **Agility** to launch XenDesktop

#.  On the bottom pop-up, click **Citrix Receiver** to launch the Citrix ICA client

#.  Verify that desktop is functional

#.  In Citrix Agility desktop, click on Start and Disconnect

#.  Logout of APM Webtop using the *Logout* button in the upper right corner

#.  Close the browser window

.. |image12| image:: /_static/class1/image14.png
   :width: 5.14583in
   :height: 3.45833in
.. |image13| image:: /_static/class1/image15.png
   :width: 5.30208in
   :height: 2.98958in
.. |image14| image:: /_static/class1/image16.png
   :width: 5.39583in
   :height: 3.21875in
