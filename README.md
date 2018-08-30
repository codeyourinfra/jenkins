# jenkins

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT) [![GitHub release](https://img.shields.io/github/release/codeyourinfra/jenkins.svg)]() [![Build status](https://travis-ci.org/codeyourinfra/jenkins.svg?branch=master)](https://travis-ci.org/codeyourinfra/jenkins)

Ansible role to install Jenkins.

## Example Playbook

```yml
---
- hosts: servers
  roles:
    - codeyourinfra.jenkins
```

## Dependencies

The role is dependent of [Codeyourinfra Oracle Java 8 Ansible role](https://galaxy.ansible.com/codeyourinfra/oracle_java8), once we need Java to run Jenkins. Java is so installed before the Jenkins installation.

## Build process

The build process is performed in [Travis CI](https://travis-ci.org/codeyourinfra/jenkins). During the build, the role is tested by using [Ubuntu Docker images with Python 3](https://hub.docker.com/r/codeyourinfra/python3).

The build is also triggered if any change is made in the `codeyourinfra.oracle_java8` role. After all, nobody wants some issue introduced by a change made in the upstream code :)

## Author Information

[@gustavomcarmo](https://github.com/gustavomcarmo) is a contributor of [Codeyourinfra](https://github.com/codeyourinfra). Get on board too! :)
