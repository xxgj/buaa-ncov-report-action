# buaa-ncov-report-action

[![GitHub stars](https://img.shields.io/github/stars/kevinchen147/buaa-ncov-report-action)](https://github.com/kevinchen147/buaa-ncov-report-action/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/kevinchen147/buaa-ncov-report-action)](https://github.com/kevinchen147/buaa-ncov-report-action/network)
![GitHub commit activity](https://img.shields.io/github/commit-activity/m/kevinchen147/buaa-ncov-report-action)
[![GitHub issues](https://img.shields.io/github/issues/kevinchen147/buaa-ncov-report-action)](https://github.com/kevinchen147/buaa-ncov-report-action/issues)
[![GitHub pulls](https://img.shields.io/github/issues-pr/kevinchen147/buaa-ncov-report-action)](https://github.com/kevinchen147/buaa-ncov-report-action/pulls)
[![Contributors](https://img.shields.io/github/contributors/kevinchen147/buaa-ncov-report-action)](https://github.com/kevinchen147/buaa-ncov-report-action/graphs/contributors)
[![GitHub license](https://img.shields.io/github/license/kevinchen147/buaa-ncov-report-action)](https://github.com/kevinchen147/buaa-ncov-report-action/blob/master/LICENSE)


Minimal GitHub action for BUAA NCOV daily report.

## Quick Start

There are only two steps needed for BUAA NCOV daily report: 

### Step One: Creating a repository

> See [Creating a repository from a template](https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-repository-from-a-template#creating-a-repository-from-a-template) for details.

### Step Two: Creating encrypted secrets

> See [Creating encrypted secrets for a repository](https://docs.github.com/en/actions/security-guides/encrypted-secrets#creating-encrypted-secrets-for-a-repository) for details.

You should create two secrets for daily report:

- `USERNAME`: your BUAA SSO username
- `PASSWORD`: your BUAA SSO password

## How It Works

- [GitHub Action](https://github.com/features/actions)
- [Python Requests](https://docs.python-requests.org/en/latest/)

## License

`buaa-ncov-report-action` released under the MIT license.