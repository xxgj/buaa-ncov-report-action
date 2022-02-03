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

**Only 2 steps needed:**

1. Creating a repository by `Use this template`: See [Creating a repository from a template](https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-repository-from-a-template#creating-a-repository-from-a-template) for details.

2. Creating encrypted secrets: See [Creating encrypted secrets for a repository](https://docs.github.com/en/actions/security-guides/encrypted-secrets#creating-encrypted-secrets-for-a-repository) for details.

    You should create two secrets:

    - `USERNAME`: your BUAA SSO username
    - `PASSWORD`: your BUAA SSO password

## How It Works

### `report.py`

`buaa-ncov-report-action` use [python-requests](https://docs.python-requests.org/en/latest/) to report.

1. Login

```python
# login
login = s.post(url='https://app.buaa.edu.cn/uc/wap/login/check',
                data={
                    'username': os.environ['USERNAME'],
                    'password': os.environ['PASSWORD']
                },
                headers=header)
```

2. Getting yesterday's info

```python
# get info
info = s.get(url='https://app.buaa.edu.cn/buaaxsncov/wap/default/get-info',
                headers=header)
```

3. Report

```python
# report
report = s.post(url='https://app.buaa.edu.cn/buaaxsncov/wap/default/save',
                data=json.loads(info.text)['d']['oldInfo'],
                headers=header)
```

### `report.yml`

`buaa-ncov-report-action` use [GitHub Action](https://github.com/features/actions) to trigger `report.py`.

`report.yml` schedules a workflow to run at specific UTC times using POSIX cron syntax:

```yaml
on:
  workflow_dispatch:
  push:
    branches:
      - main
  schedule:  
  - cron: '0,30 9 * * *'
```

In order to avoid network error, `buaa-ncov-report-action` triggers the workflow to run at 9:00 UTC and 9:30 UTC everyday to ensure report successfully.

## Known BUGs

1. There is a slight difference between the real report data and yesterday's data.

## License

`buaa-ncov-report-action` released under the MIT license.