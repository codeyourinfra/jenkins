import os
import re
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_oracle_java8_is_installed(host):
    oracle_java8 = host.package("oracle-java8-installer")
    assert oracle_java8.is_installed
    assert oracle_java8.version.startswith("8u")


def test_jenkins_is_installed(host):
    cmd = host.run("java -jar /usr/share/jenkins/jenkins.war --version")
    assert cmd.rc == 0
    pattern = re.compile("^[\\d.]+$")
    assert pattern.match(cmd.stdout)
