.. Cisco NSO documentation master file, created by
   sphinx-quickstart on Mon Dec  2 16:16:50 2019.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to Cisco NSO documentation!
===================================
.. literalinclude:: source_code/maagic_interfaces.py
   :language: python
   :emphasize-lines: 4-5
   :linenos:


Creating and configuring network services is a complex task that often requires multiple configuration changes to all devices participating in the service.

Additionally changes generally need to be made concurrently across all devices with the changes being either completely successful or rolled back to the starting configuration. 

And configuration need to be kept in sync across the system and the network devices. NSO approaches these challenges by acting as interface between people or software that want to configure the network, and the devices in the network.
The key features of NSO that comes into play includes:

#.  Multi-vendor device configuration management using the native protocols of the network devices.

#. A Configuration Database (CDB) managing synchronized configurations for all devices and services in the network domain.

#. A set of northbound interfaces including human interfaces like web UI and a CLI; programmable interfaces including RESTCONF, NETCONF, JSON-RPC; and language bindings including Java, Python and Erlang.

.. image:: images/nso_arch.png
   :scale: 50 %
   :alt: alternate text
   :align: center


Supported Network Operating Systems:
------------------------------------

* Arista EOS
* Cisco IOS
* Cisco IOS-XR
* Cisco NX-OS
* Juniper JunOS

Extras
______

In addition to the core drivers napalm also supports community driven drivers. You can find more information about them here: 

Selecting the right driver
--------------------------

You can select the driver you need by doing the following:

.. code-block:: python

    with ncs.maapi.single_write_trans('admin', 'python') as t:
        root = ncs.maagic.get_root(t)
        device = root.devices.device["ios-netsim-0"].config
        for interface in device.interface["Loopback"]:
            print("This device has interface Loopback {} with a description of {}, and an IP address and mask of {} {}".format(interface.name, interface.description, interface.ip.address.primary.address, interface.ip.address.primary.mask))
    ...
    This device has interface Loopback 0 with a description of None, and an IP address and mask of None None
    This device has interface Loopback 100 with a description of Mgmt IP from NSO, and an IP address and mask of 10.3.3.3 255.255.255.0
    This device has interface Loopback 200 with a description of Also Modified By User, and an IP address and mask of 10.2.2.5 255.255.255.0

Documentation
=============
.. code-block:: bash

    curl -X GET \
    http://127.0.0.1:8080/restconf/data/tailf-ncs:devices/device=ios-netsim-0 \
    -H 'Accept: application/yang-data+json' \
    -H 'Authorization: Basic YWRtaW46YWRtaW4=' \
    -H 'Postman-Token: 4be02b66-7b02-470a-9508-943e40a1bf16' \
    -H 'cache-control: no-cache'

    {
    "tailf-ncs:device": {
        "name": "ios-netsim-0",
        "address": "127.0.0.1",
        "port": 10022,
        ...
            "config": {
            ...
                "community-list": {
                "number-standard": [
                    {
                    "no": 1,
                    "permit": {
                    }
                    },
                    {
            "tailf-ned-cisco-ios:interface": {
                "Loopback": [
                {
                    "name": "0"
                },
                {
                    "name": "100",
                    "description": "Mgmt IP from NSO",
                    "ip": {
                    "address": {
                        "primary": {
                        "address": "10.3.3.3",
                        "mask": "255.255.255.0"
                        }
                    }
                    }
                },
                {
                    "name": "200",
                    "description": "Also Modified By User",
                    "ip": {
                    "address": {
                        "primary": {
                        "address": "10.2.2.5",
                        "mask": "255.255.255.0"
                        }
                    }
                    }
                }
                ],
                "FastEthernet": [
                {
                    "name": "0/0"
                },
                {
                    "name": "1/0"
                },
                {
                    "name": "1/1"
                }
                ]
            },
            "tailf-ned-cisco-ios:spanning-tree": {
                "optimize": {
                "bpdu": {
                    "transmission": false
                }
                }
            },
            "tailf-ned-cisco-ios:router": {
                "bgp": [
                {
                    "as-no": 64512,
                    "aggregate-address": {
                    "address": "10.10.10.1",
                    "mask": "255.255.255.251"
                    }
                }
                ]
            },


.. toctree::
   :maxdepth: 2

   installation/index
   quick_start/index
