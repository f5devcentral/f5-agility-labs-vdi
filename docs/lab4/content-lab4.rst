TASK 1 – Access Terminal Server from external network
=====================================================

.. figure:: /_static/class1/image_lab4task1.png
   :scale: 100 %
   :align: center
   
   *BIG-IP proxy RDP connection*


Create and bind NTLM Machine Account
------------------------------------

#. From "corporate-pc"

#. Open IE to access F5 Admin GUI at,
   ``https://f5-bigip1a.demosifun.net``

   - Username: ``admin``
   - Password: ``password``

#. Create on BIG-IP and bind to an NTLM Machine Account. On the left menu,

   - Click **Access -> Authentication -> NTLM -> Machine Account**
   - Click the **Create** button on the upper right corner

     +--------------------------+-----------------------------+
     | Name                     | ``AD1-f5-bigip1a``          |
     +--------------------------+-----------------------------+
     | Machine Account Name     | ``f5-bigip1a``              |
     +--------------------------+-----------------------------+
     | Domain FQDN              | ``demoisfun.net``           |
     +--------------------------+-----------------------------+
     | Domain Controller FQDN   | ``dif-ad1.demoisfun.net``   |
     +--------------------------+-----------------------------+
     | Admin User               | ``administrator``           |
     +--------------------------+-----------------------------+
     | Password                 | ``password``                |
     +--------------------------+-----------------------------+

#. Click the **JOIN** button to create the machine account


Deploy iApp
-----------

#. Create a new Application Service.

#. **iApps -> Application Services -> Applications**

#. Click the **Create** button

#. In the Name field, type in ``lab4-rds``

#. In the Template pulldown, select ``f5.microsoft_rds_remote_access.v1.0.3``

   +--------------------------------------------------------------------------+--------------------------------------------------------+
   | **Welcome to the iApp template for Remote Desktop Gateway* section**     | *Please review*                                        |
   +--------------------------------------------------------------------------+--------------------------------------------------------+
   | **Template Options**                                                                                                              |
   +--------------------------------------------------------------------------+--------------------------------------------------------+
   | Do you want to deploy BIG-IP APM as an RDP proxy?                        | *Yes, deploy BIG-IP Access Policy...*                  |
   +--------------------------------------------------------------------------+--------------------------------------------------------+
   | **Access Policy Manager**                                                                                                         |
   +--------------------------------------------------------------------------+--------------------------------------------------------+
   | Do you want to create a new AAA server, or use an existing AAA server?   | *AD1*                                                  |
   +--------------------------------------------------------------------------+--------------------------------------------------------+
   | Which NTLM machine account should be used for Kerberos delegation?       | *AD1-f5-bigip1a*                                       |
   +--------------------------------------------------------------------------+--------------------------------------------------------+
   | **SSL Encryption**                                                                                                                |
   +--------------------------------------------------------------------------+--------------------------------------------------------+
   | Which SSL certificate do you want to use?                                | ``wild.demoisfun.net.crt``                             |
   +--------------------------------------------------------------------------+--------------------------------------------------------+
   | Which SSL private key do you want to use?                                | ``wild.demoisfun.net.key``                             |
   +--------------------------------------------------------------------------+--------------------------------------------------------+
   | **Virtual Servers and Pools**                                                                                                     |
   +--------------------------------------------------------------------------+--------------------------------------------------------+
   | What IP address do you want to use for the virtual server(s)?            | ``192.168.3.156``                                      |
   +--------------------------------------------------------------------------+--------------------------------------------------------+
   | How would you like to secure your hosts?                                 | *Allow any host*                                       |
   +--------------------------------------------------------------------------+--------------------------------------------------------+

#. Click **Finished** button


Test the RDS proxy functionality using RDS Client
-------------------------------------------------

#. From *"home-pc"*

#. Launch RDS client (on desktop)

#. Click the **Show Options** pulldown

#. Click the **Advanced** tab

#. Click the **Settings** button

#. In the *"RDS Gateway..."* window,

   - Select **"Use these RD Gateway..."** radio button
   - In *Server name* field, type in ``msft-proxy-rds.demoisfun.net``. Note this address resolves to the address *192.168.3.156* which        was configured in the iApp
   - Select the **"Use my RD Gateway credential..."** checkbox
   - Click **OK**

        |image16|

#. Under *"General"* tab, in the *"Computer"* field, type in the name of the
   host you want to RDP to which is ``dif-termsvr.demoisfun.net``

   - In the *User name* field, type in ``demoisfun\demo01``
   - Click **Save**
   - Click **Connect**
   
          |image17|

#. When prompted for credentials

   - Username: ``demo01``
   - Password: ``password``

#. Click **Yes** to the Certificate warning

   |image18|

#. You are connected to dif-termsvr.demoisfun.net server

#. You can verify this connection through the BIG-IP. From *"corporate-pc"*, open IE to Connect to BIG-IP GUI

#. On the left side menu, click **Access -> Overview -> Active Sessions**

#. Click on the session to view details

   |image19|

#. Log off RDS session by clicking **Start -> Logoff**


.. |image15| image:: /_static/class1/image17.png
.. |image16| image:: /_static/class1/image18.png
.. |image17| image:: /_static/class1/image19.png
.. |image18| image:: /_static/class1/image20.png
.. |image19| image:: /_static/class1/image21.png
