Lab 2 – Solutions for Citrix XenDesktop
=======================================

The purpose of this lab is to build out 2 common F5 deployment with
XenDesktop.

Note: The connectivity in this environment is slower than a typical
production environment—please be patient

TASK 1 – Access XenDesktop without F5 
--------------------------------------

|image15|

1. From “corporate-pc”, use IE and browse to Citrix Storefront at
   http://ctx-sf1a.demoisfun.net/Citrix/AgilityStoreWeb/

2. When prompted for credentials

   a. Username: demoisfun\\demo01

   b. Password: password

3. Right Click “Agility” and select “Start” icon to launch XenDesktop.

   a. *Note: This takes a long time due to the Ravello implementation*

4. Citrix “Desktop Viewer” launches and connects to XenDesktop.

5. When the windows Activation Screen Pops up..Press Cancel (windows was
   not activated due to external connectivity limitations)

6. Log off using the windows start icon in the lower left corner

7. Log off the Citrix receiver client using the 01 Demo pulldown in the
   upper right corner

8. Close the browser Window

TASK 2 – Load Balance StoreFront
--------------------------------

|image16|

**Deploy the iApp**

1. Use the RDP function on your laptop to connect to the “corporate-pc”

2. Create a new Application Service by selecting iApps -> Application
   Services and selecting Create

   a. iApps >> Application Services

   b. Press the **Create** button

   c. Name the Application Service **VM\_LAB\_2\_LBSF**

   d. Select **f5.citrix\_vdi.v2.3.0** for the template

+----+
+----+

iApp Configuration
~~~~~~~~~~~~~~~~~~

1. Review the **Welcome to the iApp template for XenDesktop and XenApp**

2. **General**

+------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------+
| Use APM to securely proxy application (ICA) traffic and authenticate users into your Citrix environment?   | Yes, Proxy ICA traffic and authenticate users with BIG\_IP   |
+============================================================================================================+==============================================================+
| What is the Active Directory NetBIOS Domain Name used for your Citrix servers?                             | demoisfun                                                    |
+------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------+

1. **BIG-IP Access Policy Manager**

+---------------------------------------------------------------------------------------------+-------------------------+
| Do you want to replace Citrix Web Interface or StoreFront servers with the BIG-IP system?   | “No, do not replace…”   |
+=============================================================================================+=========================+
| Create a new AAA object or select an existing one?                                          | AD1                     |
+---------------------------------------------------------------------------------------------+-------------------------+

1. **Virtual Server for Web Interface or StoreFront servers **

+---------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------+
| How should the BIG-IP system handle encrypted traffic to Web Interface or StoreFront servers?           | Terminate SSL for Clients, Plaintext to Citrix servers **(SSL offload)**    |
+=========================================================================================================+=============================================================================+
| Which SSL certificate do you want to use?                                                               | wild.demoisfun.net.crt                                                      |
+---------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------+
| Which SSL private key do you want to use?                                                               | wild.demoisfun.net.key                                                      |
+---------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------+
| What IP address will clients use to access the Web Interface or StoreFront servers, or the F5 Webtop?   | 192.168.3.160                                                               |
+---------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------+
| Did you deploy Citrix StoreFront?                                                                       | Yes,…StoreFront 3.0 or 3.6                                                  |
|                                                                                                         |                                                                             |
|                                                                                                         | Note: we are running SF 3.9                                                 |
+---------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------+
| What is the URI used on StoreFront or Web Interface servers for XenApp or XenDesktop?                   | /Citrix/AgilityStoreWeb/                                                    |
|                                                                                                         |                                                                             |
|                                                                                                         | *Note that this is the same URL used to access citrix directly in Task 1*   |
+---------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------+

1. **Web Interface or StoreFront servers**

+------------------------------------------------------------------------------------+---------------------------+
| What DNS name will clients use to reach the Web Interface or StoreFront servers?   | ctx-LB-SF.demoisfun.net   |
+====================================================================================+===========================+
| Which port have you configured for Web Interface or StoreFront HTTP traffic?       | 80                        |
+------------------------------------------------------------------------------------+---------------------------+
| What are the IP addresses of your Web Interface or StoreFront servers?             | 192.168.10.220            |
|                                                                                    |                           |
|                                                                                    | 192.168.10.221            |
+------------------------------------------------------------------------------------+---------------------------+
| Which Monitor do you want to use                                                   | http                      |
+------------------------------------------------------------------------------------+---------------------------+

1. **Virtual Server for XML Broker or Desktop Delivery Controller (DDC)
   Servers**

+-------------------------------------------------------------------------------------+-------------------------------------------------------------+
| What IP address do you want to use for the XML Broker or DDC farm virtual server?   | 192.168.10.161                                              |
+=====================================================================================+=============================================================+
| How will requests from the Web Interface or StoreFront servers arrive?              | XML Broker or DCC requests will arrive unencrypted (HTTP)   |
+-------------------------------------------------------------------------------------+-------------------------------------------------------------+

1. **XML Broker or DDC Servers **

+----------------------------------------------------------------+------------------+
| What are the IP addresses of your XML Broker or DDC servers?   | 192.168.10.222   |
|                                                                |                  |
|                                                                | 192.168.10.223   |
+================================================================+==================+
| Which monitor do you want to use?                              | http             |
+----------------------------------------------------------------+------------------+

1. Press the **Finished** button

Test connectivity
~~~~~~~~~~~~~~~~~

1. Use the RDP function on your laptop to connect to the “home-pc”

2. Launch IE and browse to http://ctx-lb-sf.demoisfun.net

3. When prompted for credentials

   a. Username: demo01

   b. Password: password

4. Storefront is displayed with Agility icon.

5. Right Click on “Agility” and select “Start” icon to launch
   XenDesktop.

   a. *Note: This takes a long time due to the Ravello implementation*

6. Log off using the windows start icon in the lower left corner

7. Log off the Citrix receiver client using the 01 Demo pulldown in the
   upper right corner

8. Close the browser Window

TASK 3 – Reconfigure the iApp to Replace StoreFront
---------------------------------------------------

|image17|

**Deploy the iApp**

1. Use the RDP function on your laptop to connect to the “corporate-pc”

2. Create a new Application Service by selecting iApps -> Application
   Services and selecting Create

   a. iApps >> Application Services

   b. Click on **VM\_LAB\_2\_LBSF**

   c. Click the **Reconfigure** link near the top

+----+
+----+

iApp Configuration
~~~~~~~~~~~~~~~~~~

1. **BIG-IP Access Policy Manager**

+---------------------------------------------------------------------------------------------+--------------------------+
| Do you want to replace Citrix Web Interface or StoreFront servers with the BIG-IP system?   | “Yes, replace Citrix…”   |
+=============================================================================================+==========================+
+---------------------------------------------------------------------------------------------+--------------------------+

1. Scroll through the template and note that the storefront pool members
   are no longer present

2. Press the **Finished** button

Test connectivity
~~~~~~~~~~~~~~~~~

1. Use the RDP function on your laptop to connect to the “home-pc”

2. Launch IE and browse to http://ctx-lb-sf.demoisfun.net

3. When prompted for credentials

   a. Username: demo01

   b. Password: password

4. APM webtop is displayed with Agility icon.

5. Click on Agility icon to launch XenDesktop.

6. When the windows Activation Screen Pops up..Press Cancel (windows was
   not activated due to external connectivity limitations)

7. Log off using the windows start icon in the lower left
   corner\ |image18|

8. Logout using the Logout button in the upper right corner of the
   screen

9. Close the broiwser window

.. |image15| image:: /_static/image14.png
   :width: 5.14583in
   :height: 3.45833in
.. |image16| image:: /_static/image15.png
   :width: 5.30208in
   :height: 2.98958in
.. |image17| image:: /_static/image16.png
   :width: 5.39583in
   :height: 3.21875in
.. |image18| image:: /_static/image17.png
   :width: 4.53125in
   :height: 2.03125in
.. |image19| image:: /_static/image18.png
   :width: 5.58333in
   :height: 2.96875in
