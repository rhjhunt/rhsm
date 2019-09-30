[![Build Status](https://api.travis-ci.com/rhjhunt/rhsm.svg?branch=master)](https://api.travis-ci.com/rhjhunt/rhsm)

RHSM
=========

Ansible role to use *redhat_subscription* to register a Red Hat Enterprise Linux
(RHEL) system with `subscription-manager`.

Requirements
------------

- Ansible 2.8 or higher
- Red Hat Enterprise Linux (RHEL) 6, 7, or 8
- Valid Red Hat Subscriptions

Role Variables
--------------

The following variables are supported for this role. They directly relate to the
options in the [redhat_subscription](http://docs.ansible.com/ansible/latest/modules/redhat_subscription_module.html) module.

Role Variable | Definition
------------- | ----------
rhsm_activationkey | Activation key to use for registration
rhsm_auto_attach | auto-consume available subscriptions
rhsm_consumer_id | References an existing consumer ID
rhsm_consumer_name | Name of the system to register
rhsm_consumer_type | The type of unit to register
rhsm_environment | Register with a specific environment in Red Hat Satellite 6
rhsm_force_register | Register the system even if it is already registered
rhsm_org_id | Organization ID to use in conjunction with activationkey
rhsm_password | access.redhat.com or Red Hat Satellite 6 password
rhsm_pool | Specify a subscription pool name to consume
rhsm_pool_ids | Specify subscription pool IDs to consume
rhsm_release | Set a release version
rhsm_rhsm_baseurl | Specify CDN baseurl
rhsm_rhsm_repo_ca_cert | Specify an alternative location for a CA
rhsm_server_hostname | Alternative RHSM or Red Hat Satellite 6
rhsm_server_insecure | Enable or disable https server certificate verification
rhsm_server_proxy_hostname | Specify a HTTP proxy hostname
rhsm_server_proxy_password | Specify a password for HTTP proxy
rhsm_server_proxy_port | Specify a HTTP proxy port
rhsm_server_proxy_user | Specify a user for HTTP proxy
rhsm_state | whether to register and subscribe
rhsm_username | access.redhat.com or Red Hat Satellite 6 username

Dependencies
------------

A Red Hat Enterprise Linux 6, 7, or 8 system with `subscription-manager`
installed.

Privilege escalation, `sudo` is required.

Example Playbook
----------------

Example playbook using Organization ID and Activation key.

```yml
---
- hosts: all
  vars:
    rhsm_org_id: '0000000'
    rhsm_activationkey: activation-key
  roles:
    - role: rhsm
```

Example playbook with username, password and pool ID. In order to protect your
password and pool ID it's recommend to put the information in a vault.

```yml
---
- hosts: all
  vars:
    rhsm_password: "{{ vault_password }}"
    rhsm_username: "{{ vault_username }}"
    rhsm_pool_ids:
      - "{{ vault_pool_id }}"
  roles:
    - role: rhsm
```

License
-------

[GPLv3](LICENSE)

Author Information
------------------

Jacob Hunt <jhunt@redhat.com>
