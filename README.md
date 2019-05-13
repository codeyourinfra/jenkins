# jenkins

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT) [![GitHub release](https://img.shields.io/github/release/codeyourinfra/jenkins.svg)](https://github.com/codeyourinfra/jenkins/releases/latest) [![Build status](https://travis-ci.org/codeyourinfra/jenkins.svg?branch=master)](https://travis-ci.org/codeyourinfra/jenkins) [![Ansible Role](https://img.shields.io/ansible/role/29218.svg)](https://galaxy.ansible.com/codeyourinfra/jenkins) [![Ansible Role downloads](https://img.shields.io/ansible/role/d/29218.svg)](https://galaxy.ansible.com/codeyourinfra/jenkins)

Ansible role to install [Jenkins](https://jenkins.io).

## Example Playbook

```yml
---
- hosts: servers
  roles:
    - codeyourinfra.jenkins
```

## Dependencies

The role is dependent of [Codeyourinfra's Java 8 Ansible role](https://github.com/codeyourinfra/java8/tree/v1.0), once we need Java to run Jenkins. Java is so installed before the Jenkins installation.

## Build process

The build process is performed by [Travis CI](https://travis-ci.org/codeyourinfra/jenkins). During the build, [Molecule](https://molecule.readthedocs.io) is used to test the role.

## Test yourself

Inside your [Python virtual environment](https://docs.python.org/3/tutorial/venv.html), run:

`pip install -r requirements.txt`

And then:

`molecule test`

## Author Information

[@gustavomcarmo](https://github.com/gustavomcarmo) is a contributor of [Codeyourinfra](https://github.com/codeyourinfra). Get on board too! :)
