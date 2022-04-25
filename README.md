# buaa-ncov-report-action

[![GitHub stars](https://img.shields.io/github/stars/xxgj/buaa-ncov-report-action)](https://github.com/xxgj/buaa-ncov-report-action/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/xxgj/buaa-ncov-report-action)](https://github.com/xxgj/buaa-ncov-report-action/network)
![GitHub commit activity](https://img.shields.io/github/commit-activity/m/xxgj/buaa-ncov-report-action)
[![GitHub issues](https://img.shields.io/github/issues/xxgj/buaa-ncov-report-action)](https://github.com/xxgj/buaa-ncov-report-action/issues)
[![GitHub pulls](https://img.shields.io/github/issues-pr/xxgj/buaa-ncov-report-action)](https://github.com/xxgj/buaa-ncov-report-action/pulls)
[![Contributors](https://img.shields.io/github/contributors/xxgj/buaa-ncov-report-action)](https://github.com/xxgj/buaa-ncov-report-action/graphs/contributors)
[![GitHub license](https://img.shields.io/github/license/xxgj/buaa-ncov-report-action)](https://github.com/xxgj/buaa-ncov-report-action/blob/master/LICENSE)

Minimal GitHub action for BUAA NCOV daily report.

## Quick Start

**Only 2 steps needed:**

1. Creating a repository by `Use this template`: See [Creating a repository from a template](https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-repository-from-a-template#creating-a-repository-from-a-template) for details.
1. Creating encrypted secrets: See [Creating encrypted secrets for a repository](https://docs.github.com/en/actions/security-guides/encrypted-secrets#creating-encrypted-secrets-for-a-repository) for details.

    You should create two secrets:
    - `USERNAME`: your BUAA SSO username
    - `PASSWORD`: your BUAA SSO password

## How It Works

### [report.py](https://github.com/xxgj/buaa-ncov-report-action/blob/main/report.py)

`buaa-ncov-report-action` uses [python-requests](https://docs.python-requests.org/en/latest/) to report.

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

1. Getting yesterday's info

    ```python
    # get info
    info = s.get(url='https://app.buaa.edu.cn/buaaxsncov/wap/default/get-info',
                    headers=header)
    ```

1. Report

    ```python
    # report
    report = s.post(url='https://app.buaa.edu.cn/buaaxsncov/wap/default/save',
                    data=json.loads(info.text)['d']['oldInfo'],
                    headers=header)
    ```

### [report.yml](https://github.com/xxgj/buaa-ncov-report-action/blob/main/.github/workflows/report.yml)

`buaa-ncov-report-action` uses [GitHub Action](https://github.com/features/actions) to trigger `report.py`.

`report.yml` schedules a workflow to run at specific UTC times(9:00 UTC) using POSIX cron syntax:

```yaml
on:
  workflow_dispatch:
  schedule:  
  - cron: '0 9 * * *'
```

Since GitHub will send an email notification of workflow error messages to you when workflow fails, `buaa-ncov-report-action` does not implement another way for notification.

You can run workflow by yourself and view log at [here](https://github.com/xxgj/buaa-ncov-report-action/actions).

## Known BUGs

> Feel free to open an issue if you have any questions.

1. There is slight difference between the real report data and yesterday's data. However, it doesn't matter.
1. Scheduled workflows will be disabled automatically after 60 days of repository inactivity.

## License

`buaa-ncov-report-action` released under the MIT license.
