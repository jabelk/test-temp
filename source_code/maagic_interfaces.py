with ncs.maapi.single_write_trans('admin', 'python') as t:
    root = ncs.maagic.get_root(t)
    device = root.devices.device["ios-netsim-0"].config
    for interface in device.interface["Loopback"]:
        print("This device has interface Loopback {} with a description of {}, and an IP address and mask of {} {}".format(interface.name, interface.description, interface.ip.address.primary.address, interface.ip.address.primary.mask))
