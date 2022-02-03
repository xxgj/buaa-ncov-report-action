import json
import logging
import os
import requests

header = {
    'Accept': 'application/json, text/plain, */*',
    'X-Requested-With': 'XMLHttpRequest',
    'Accept-Language': 'en-us',
    'Accept-Encoding': 'gzip, deflate, br',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Origin': 'https://app.buaa.edu.cn',
    'User-Agent': 'Mozilla/5.0 (iPhone CPU iPhone OS 14_8 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.13(0x18000d30) NetType/WIFI Language/zh_CN miniProgram',
    'Connection': 'keep-alive'
}


def checkin() -> None:
    # logging
    logging.basicConfig(level=logging.INFO, format='%(asctime)s %(message)s')

    # request session
    s = requests.Session()

    # login
    login = s.post(url='https://app.buaa.edu.cn/uc/wap/login/check',
                   data={
                       'username': os.environ['USERNAME'],
                       'password': os.environ['PASSWORD']
                   },
                   headers=header)
    logging.info('「登录结果」' + login.text)
    if json.loads(login.text)['e'] != 0:
        raise Exception('「登录失败」')

    # get info
    info = s.get(url='https://app.buaa.edu.cn/buaaxsncov/wap/default/get-info',
                 headers=header)
    if json.loads(info.text)['e'] != 0:
        raise Exception('「获取信息失败」')

    # report
    report = s.post(url='https://app.buaa.edu.cn/buaaxsncov/wap/default/save',
                    data=json.loads(info.text)['d']['oldInfo'],
                    headers=header)
    logging.info('「打卡结果」' + report.text)
    if json.loads(report.text)['e'] != 0:
        raise Exception('「打卡失败」')


if __name__ == '__main__':
    checkin()
