import os
import re
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('ubuntu')


def test_java8_is_installed(host):
    java8 = host.package("openjdk-8-jdk")
    assert java8.is_installed
    assert java8.version.startswith("8u")


def test_jenkins_is_installed(host):
    cmd = host.run("java -jar /usr/share/jenkins/jenkins.war --version")
    assert cmd.rc == 0
    pattern = re.compile("^[\\d.]+$")
    assert pattern.match(cmd.stdout)
