Jump Host
=========

Please follow the instructions provided by the instructor to start your lab and access your jump host.

.. NOTE:: All work for this lab will be performed exclusively from the Windows jumphost. No installation or interaction with your local system is required.


Lab Network Setup
=================

In the interest of focusing as much time as possible on this solution,
we have provided some resources and basic setup ahead of time. These
are:

-  The system has been licensed and provisioned for LTM and APM

-  A Microsoft Active Directory environment has been configured for
   authentication

-  A VMware Horizon View environment has already been configured

-  A Citrix XenDesktop environment has already been configured

-  A Microsoft RDS has already been configured

-  Windows desktops with Citrix and View clients will be accessed using
   RDP to demonstrate functionality

.. figure:: /_static/class1/image_overview.png
   :scale: 100 %
   :align: center
   
   *Complete lab setup*
  

Connect to Lab Environment 
==========================

Please refer to *Fig 1.1*. We are simulating internal and external access
to VDI with 2 Windows desktops. When viewing the *“corporate-pc”* session,
imagine you are sitting at your office desk. Likewise, viewing the
*“home-pc”* session is like you are sitting at home, or anywhere outside
of the company network.

The lab is hosted in our cloud provider: Ravello. Lab instructors will
provide a URL and a unique student number to access the environment.
Each attendee is expected to have a computer with a modern browser and an
RDP client.

To connect to jump hosts,

#. Open browser and go to the URL provided by instructor.

#. Scroll down and find *“corporate-pc”*. Choose to connect with RDP.
   Leave this connection for entire lab duration.

   +------------+--------------------------------------------------------------------+
   | |image1|   | Username: ``agility`` (*Student Agility*)                          |
   |            |                                                                    |
   |            | Password: ``F5Agility``                                            |
   +------------+--------------------------------------------------------------------+

#. Scroll down and find *“home-pc”*. Choose to connect with RDP. Leave
   this connection for entire lab duration.

   +------------+--------------------------------------------------------------------+
   | |image2|   | Username: ``agility`` (*Student Agility*)                          |
   |            |                                                                    |
   |            | Password: ``F5Agility``                                            |
   +------------+--------------------------------------------------------------------+

.. |image1| image:: /_static/class1/image3.png
   :width: 1.86762in
   :height: 2.56604in
.. |image2| image:: /_static/class1/image4.png
   :width: 1.82075in
   :height: 2.56895in   
