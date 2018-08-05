
Task 1 – Build a VIP with an Access Policy allowing access to VMware and Citrix
===============================================================================

#. From *"corporate-pc"*

#. Connect to the F5 config GUI

#. Disable *Stict Updates* for the *lab1-proxy* Application

   - iApps>>Application Services
   - Select VMW_LAB_1_PROXY 
   - Select the Properties Tab
   - Use the pulldown to select Advanced from Application Service 
   - Uncheck Strict Updates
   - Click the “Update” button


#. Copy the VM_LAB_1_PCOIP access profile to VDI_Combined_webtop

   - **Access -> Profiles/Policies -> "Access Profiles..."**
   - Click the “Copy” hyperlink on the *lab1-proxy* line
   - Name the profile VDI_Combined_webtop
   - Press the "Copy" button (bottom left)

#. View the characteristics of the *VDI_Combined_webtop* and *lab3-lb-sf* access policies

   - View the VM_LAB_2_LB_SF Access profile. The subsequent steps will integrate the required components from that Citrix  policy with the copy of the VM_LAB_1_PCOIP we created (VDI_Combined_webtop- Access>>Profiles/Policies>>Access Profiles
   - Click the “Edit” hyperlink on the VM_LAB_2_LB_SF

#. Open the VDI-Combined_webtop to add the required objects and parameters

   - Access>>Profiles/Policies>>Access Profiles
   - Click the “Edit” hyperlink on the VDI_Combined_webtop
   - Review the existing VPE configuration 
 
#. Add Citrix to the Browser Resource assign on the Full or Mobile Browser branch
 
   - Click on the Browser Resource Assign object on the right end or the branch
   - Click on the “Add/Delete” link in the Browser Resource Assign pop up window
   - Select the Remote Desktop tab 
   - Add /Common/VM_LAB_2_LBSF.app/VM_LAB_2_LBSF_remote_desktop_1
   - Press the “Update” button
   - Pres the “Save” button
   
.. image:: /_static/class1/image41.png
   :scale: 75 %
   :align: center

#. Add a branch  for the Citrix Receiver to the Client type decision Box

   - Click on the “Client Type” object
   - Select the “Branch Rules” Tab
   - Click the “Add Branch Rule” button
   - Name: Citrix Receiver
   - Press the “change” link in the section
   - Click on the “Add Expression”
   - Agent Sel: UI Mode
   - Condition: UI Mode
   - UI Mode is: Citrix Reciever
   - Click on “Add Expression”
   - Click the “Finished” button
   - Click on the “Save” button (this takes a while) 
 
#. Add a Logon Page object to the Citrix Receiver branch
 
   - Click the “+” to the right of Citrix Reciever branch of the Client Type Object
   - Select the “Logon” tab
   - Select Logon Page
   - Click the “Add Item” button
   - Review the default settings
   - Click the “Save” button
 
#. Add a Domain Variable Assign object to the Citrix Receiver branch
 
   - Click the “+” to the right of the Logon Page
   - Select the “Assignment” tab
   - Select “Variable Assign”
   - Click the “Add Item” button
   - Click the “Add new entry” button
   - Click the “change” link
   - Custom Variable, Unsecure, Enter **session.logon.last.domain** in the left panel
   - Custom Expression, Enter **expr {"demoisfun"}** in the right panel
   - Click the “Finished” Button
   - Click the “Save” button

.. image:: /_static/class1/image42.png
   :scale: 75 %
   :align: center
   
#. Add an *AD Auth* object to the Citrix Receiver branch

   - Click the **“+”** to the right of Variable Assign
   - Click the **Authentication** tab
   - Select **AD Auth**
   - Click the **Add Item** button
   - In the *Server* pulldown, select **/Common/AD1**
   - Click the **Save** button

#. Add an *Advanced Resource Assign* object to the Citrix Receiver branch

   - To the right of *AD Auth, Successfull* branch, click the **“+”**
   - Click **Assignment** tab
   - Select **Advanced Resource  Assign** radio button
   - Click **Add Item** button
   - Click **Add new entry** button
   - Click **Add/Delete** link
   - Click **Remote Desktop...** tab
   - Select **/Common/lab2-lb-sf.app/lab2-lb-sf_remote_desktop_1** check box
   - Click **Webtop...** tab
   - Select **Common/lab2-lb-sf.app/lap2-lb-sf_webtop** radio button
   - Click **Update** button
   - Click **Save** button
   - To the right of *Advanced Resource Assign, fallback* branch, click **Deny**
   - Select **Allow** radio button
   - Click **Save** button
   - On the upper right corner, click **Close** the VPE. Click **YES** on the IE pop-up

.. image:: /_static/class1/image43.png
   :scale: 75 %
   :align: center

#. Apply the access policy

   - On the upper left corner of the main F5 GUI, click **Apply Access Policy** 
   - **Access -> Profiles/Policies -> "Access Profiles..."**
   - Verify that all Access policies status is Green (refresh browser if necessary) 

.. image:: /_static/class1/image45.png
   :scale: 75 %
   :align: center

#. Create a VIP for PCOIP UDP traffic 

   - Go to **Local Traffic -> Virtual Servers -> Virtual Server List**
   - View the configuration of the *lab2-proxy_pcoip_udp* VS. We will replicate this configuration using the IP of the new VIP we created for VDI access (Hint—Open an additional browser window connected to F5-bigip1a.demoisfun.net. This will allow you to display different VIPs in the same device)
   - Go to **Local Traffic -> Virtual Servers -> Virtual Server List**
   - Click **Create** button in the upper right section of the GUI
   - Configure the VIP with the variables below

   +--------------------------------------------+-----------------------------+
   |General Properties                                                        |
   +--------------------------------------------+-----------------------------+
   |Name                                        | Combined_VDI_PROXY          |
   +--------------------------------------------+-----------------------------+
   |Destination Address/Mask                    | 192.168.3.157               |
   +--------------------------------------------+-----------------------------+
   |Service Port                                | 4172                        +
   +--------------------------------------------+-----------------------------+
   |Configuration                                                             |
   +--------------------------------------------+-----------------------------+
   |Protocol                                    | UDP                         |
   +--------------------------------------------+-----------------------------+
   |Source Address Translation                  | Auto Map                    |
   +--------------------------------------------+-----------------------------+
   |Access Policy                                                             |
   +--------------------------------------------+-----------------------------+
   |Application Tunnels (Jave & Per-App VPN)    | Enabled - Checked           |
   +--------------------------------------------+-----------------------------+

   - Click “Finished” at the bottom of the screen

#. Create a Combined VIP for the Citrix and VMware connectivity

   - Go to **Local Traffic -> Virtual Servers -> Virtual Server List**
   - Click **Create** button in the upper right section of the GUI
   - Configure the VIP with the variables below
   
#. VIP Config Parameters 

   +--------------------------------------------+----------------------------+
   |General Properties                                                       |
   +--------------------------------------------+----------------------------+
   |Name                                        | Combined_VDI_Desktop       |
   +--------------------------------------------+----------------------------+
   |Destination Address/Mask                    | 192.168.3.157              |
   +--------------------------------------------+----------------------------+
   |Service Port                                | 443                        +
   +--------------------------------------------+----------------------------+
   |Configuration                                                            |
   +--------------------------------------------+----------------------------+
   |HTTP Profile                                | http                       |
   +--------------------------------------------+----------------------------+
   |SSL Profile (Client)                        | VM_LAB_1_PROXY_client_SSL  |
   +--------------------------------------------+----------------------------+
   |SSL Profile (Server)                        | serverssl                  |
   +--------------------------------------------+----------------------------+
   |Source Address Translatio                   | Auto Map                   |
   +--------------------------------------------+----------------------------+
   |Access Policy                                                            |
   +--------------------------------------------+----------------------------+
   |Access Profile                              | VDI_Combined_webtop        |
   +--------------------------------------------+----------------------------+
   |Connectivity Profile                        | VM_LAB_1_PROXY_connect     |
   +--------------------------------------------+----------------------------+
   |VDI Profile                                 | vdi                        |
   +--------------------------------------------+----------------------------+

#. Click “Finished” at the bottom of the screen


Test Connectivity
-----------------

Verify connectivity to VMware ad Citrix
=======================================

#. From *“home-pc”*

#. Open IE and browse to ``https://vdi.demoisfun.net``. Note this address has been configured in DNS to resolve to the VIP 192.168.3.157

#. When prompted for credentials

   - Username: demo01
   - Password: password

#. APM webtop is displayed with
   - Agility - Vmware View Desktop
   - Agility - Agility VDI Class (Citrix)
   
#. Click **Agility - Agility VDI Class** to launch XenDesktop

#. In *Select client** pop-up, click **Citrix Receiver** button

#. Verify that desktop is functional

#. In Citrix Agility desktop, click **Start -> Disconnect**. This will return you to APM webtop

#. Click **Agility - Vmware View Desktop**

#. In *Select client* pop-up, click **VMware Horizon** button

# Verify that the VMware desktop functions

# Close *View* client

.. image:: /_static/class1/image44.png
   :scale: 75 %
   :align: center
