import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_consul_group_exists(host):
    consul_group = host.group("consul")
    assert consul_group.exists


def test_consul_user_exists(host):
    consul_user = host.user("consul")
    assert consul_user.exists


def test_consul_is_installed(host):
    consul_app = host.file("/opt/consul/bin/consul")
    assert consul_app.exists
    assert consul_app.user == 'consul'
    assert consul_app.group == 'consul'
    assert consul_app.mode == 0o750
    assert not consul_app.is_directory


def test_consul_config_is_installed(host):
    consul_config = host.file("/etc/consul.d/config.json")
    assert consul_config.exists
    assert consul_config.user == 'consul'
    assert consul_config.group == 'consul'
    assert consul_config.mode == 0o640
    assert not consul_config.is_directory


def test_consul_is_running(host):
    consul_service = host.service('consul')
    assert consul_service.is_running
    assert consul_service.is_enabled


def test_consul_data_directory(host):
    consul_data_dir = host.file("/var/consul")
    assert consul_data_dir.exists
    assert consul_data_dir.user == 'consul'
    assert consul_data_dir.group == 'consul'
    assert consul_data_dir.is_directory


def test_consul_log_directory(host):
    consul_log_dir = host.file("/var/log/consul")
    assert consul_log_dir.exists
    assert consul_log_dir.user == 'consul'
    assert consul_log_dir.group == 'consul'
    assert consul_log_dir.is_directory
