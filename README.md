[![PyPI version](https://img.shields.io/pypi/v/ansiblelint-custom-rules-zjleblanc.svg)](https://pypi.org/project/ansiblelint-custom-rules-zjleblanc)
[![CI/CD](https://github.com/zjleblanc/ansible-lint-rules/actions/workflows/master.yml/badge.svg?branch=master&event=push)](https://github.com/zjleblanc/ansible-lint-rules/actions/workflows/master.yml)

# Ansible Lint Custom Rules

This python library contains a few custom lint rules based on practices I have found useful when implementing Ansible in an enterprise environment. For general ansible-lint usage, please refer to the [documentation](https://ansible-lint.readthedocs.io/)

## Installation

`pip install ansiblelint-custom-rules-zjleblanc`

The package will be installed into the ansible lint rules library and immdeiately available for use in the installation environment. If you are using plugins to an IDE, then you may have to close and re-open to see the effects.

## Extend

**Please** add your own custom rules. Merge requests are welcome or fork the repo and use it as a base for building custom rules for your organization.

## Rules

| Id | Description | Tags |
| --- | --- | --- |
| task_module_last | Enforces defining the module (and it's corresponding vars) at the end of a task block | `readability` `formatting` |
| when_follows_name | Enforces the use of when conditionals directly following the task name |  `readability` `formatting` | 

To see examples of how the rule is enforced, refer to the test playbooks which can be found at: `tests/playbooks/{rule-id}`