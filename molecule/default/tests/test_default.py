"""Test suite to verify that a system is properly subscribed."""

import os
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('all')


def test_os_release(host):
    """Verify the system is a RHEL system."""
    assert host.file("/etc/os-release").contains("rhel")


def test_rhsm_package(host):
    """Verify subscription-manager is installed."""
    assert host.package("subscription-manager").is_installed


def test_pool_id(host):
    """Verify that a pool id is attached to the host."""
    with host.sudo():
        assert host.check_output(
            'subscription-manager list --consumed --pool-only')


def test_status(host):
    """Verify the system is registered."""
    with host.sudo():
        assert host.check_output('subscription-manager status')
