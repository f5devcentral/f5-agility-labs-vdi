Lab 3 – Microsoft RDS proxy
===========================

The purpose of this lab is access an internal RDS server from an
external client.

TASK 1 – Access Terminal Server from external
---------------------------------------------

|image19|

**Deploy the iApp**

1. Use the RDP function on your laptop to connect to the “corporate-pc”

2. Connect to the F5 config GUI

   a. https://192.168.10.216

   b. Username: admin

   c. Password: password

3. Create an NTLM Machine Account

   a. Access >>Authentication>>NTLM>>Machine Account

+--------------------------+-------------------------+
| Name                     | AD1-f5-bigip1a          |
+==========================+=========================+
| Machine Account Name     | f5-bigip1a              |
+--------------------------+-------------------------+
| Domain FQDN              | demoisfun.net           |
+--------------------------+-------------------------+
| Domain Controller FQDN   | dif-ad1.demoisfun.net   |
+--------------------------+-------------------------+
| Admin User               | administrator           |
+--------------------------+-------------------------+
| Password                 | password                |
+--------------------------+-------------------------+

1. Us the **JOIN** button to create the machine account

2. Create a new Application Service by selecting iApps -> Application
   Services and selecting Create

   a. iApps >> Application Services

   b. Press the **Create** button

   c. Name the Application Service **VM\_LAB\_3\_RDS**

   d. Select **f5.microsoft\_rds\_remote\_access.v1.0.0** for the
      template

+----+
+----+

iApp Configuration
~~~~~~~~~~~~~~~~~~

1. Review the **Welcome to the iApp template for Remote Desktop
   Gateway**

2. **Template Options**

+-----------------------------------------------------+--------------------------------------------+
| Do you want to deploy BIG-IP APM as an RDP proxy?   | Yes, deploy BIG-IP Access Policy Manager   |
+=====================================================+============================================+
+-----------------------------------------------------+--------------------------------------------+

1. **Access Policy Manager**

+--------------------------------------------------------------------------+------------------+
| Do you want to create a new AAA server, or use an existing AAA server?   | AD1              |
+==========================================================================+==================+
| Which NTLM machine account should be used for Kerberos delegation?       | AD1-f5-bigip1a   |
+--------------------------------------------------------------------------+------------------+

1. **Network (leave defaults)**

2. **SSL Encryption**

+---------------------------------------------+--------------------------+
| Which SSL certificate do you want to use?   | wild.demoisfun.net.crt   |
+=============================================+==========================+
| Which SSL private key do you want to use?   | wild.demoisfun.net.key   |
+---------------------------------------------+--------------------------+

1. **Virtual Servers and Pools **

+-----------------------------------------------------------------+------------------+
| What IP address do you want to use for the virtual server(s)?   | 192.168.3.156    |
+=================================================================+==================+
| How would you like to secure your hosts?                        | Allow any host   |
+-----------------------------------------------------------------+------------------+

1. Press the **Finished** button

Test the RDS proxy functionality using RDS Client
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Use the RDP function on your laptop to connect to the “home-pc”

2. Launch RDS client (on desktop).

   a. Select the “Show Options” Pulldown

      i. Select the “Advanced” tab

         1. Select the Settings button

         2. Note the configuration of the RD Gateway.
            msft-proxy-rds.demoisfun.net resolves to the address
            192.168.3.156 which was configured in the iApp

    |image20|

1. Verify the settings and click the OK button

i.   Under “General” tab, in the “Computer” field, type in the name of
     the host you want to RDP to which is “dif-termsvr.demoisfun.net”

     |image21|

ii.  Clock “Save”

iii. Click “Connect”

a. When prompted for credentials

   i.  Username: demo01

   ii. Password: password

b. Accept Certificate warning

    |image22|

a. You are connected to dif-termsvr.demoisfun.net

1. Use the “Corporate PC” to Connect to the F5 Big IP GUI
   https://192.168.10.216

2. Access>>Overview>>Active Sessions

3. Click on the session to view details

    |image23|

4. Log off using the windows start icon in the lower left corner

.. |image19| image:: /_static/image18.png
   :width: 5.58333in
   :height: 2.96875in
.. |image20| image:: /_static/image19.png
   :width: 2.05729in
   :height: 2.31385in
.. |image21| image:: /_static/image20.png
   :width: 2.06771in
   :height: 2.38695in
.. |image22| image:: /_static/image21.png
   :width: 1.82813in
   :height: 1.68013in
.. |image23| image:: /_static/image22.png
   :width: 5.25486in
   :height: 1.65269in