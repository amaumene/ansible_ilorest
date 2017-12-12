# ansible_ilorest
Ansible role and module to manage HP iLO through the RESTful API

## Components

### The module
The module is based on [python-ilorest-library](https://github.com/HewlettPackard/python-ilorest-library) by HP.

### The role
The role is more a PoC at this stage. I've just implemented the features I needed.

## How-to

### Requirements
This module has only been tested with Ansible 2.4

You need to install python-ilorest-library:
```pip install python-ilorest-library```

### Inventory
The inventory is describing the IP of the IPMI of the servers. The username and password are passed as variables:
```compute00 ilo_ip=10.0.0.1
compute01 ilo_ip=10.0.0.2
controller00 ilo_ip=10.0.0.3
controller01 ilo_ip=10.0.0.4
controller02 ilo_ip=10.0.0.5
cephosd00 ilo_ip=10.0.0.6
cephosd01 ilo_ip=10.0.0.7
cephosd02 ilo_ip=10.0.0.8

[all:vars]
ilo_user=username
ilo_pass=password
ansible_python_interpreter=python
```

### Playbook
A example playbook will look like this:
```---
- name: iLO and BIOS configuration through RestAPI
  hosts: all
  connection: local
  gather_facts: False

  vars:
    - bios_revert_default: False
    - bios_boot_mode: LegacyBios
    - bios_power_profile: MaxPerf
    - bios_power_regulator: StaticHighPerf
    - reset_server: False

  roles:
    - ilorest
```
This example will set the boot mode to legacy instead of UEFI but won't reset the defaults parameters.

/!\ The server is restart at the end of the role so the changes are saved.
