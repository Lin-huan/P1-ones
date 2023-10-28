import json
import sys
import requests
import os

branch='P3039_P1055'
def register(mail, branch):
    base_url = f'https://devapi.myones.net/project/{branch}'
    json1 = {
        "phone": "+8613902995544"
    }
    os.popen('/Users/lay/Desktop/reflushRedis')
    headers = {'referer': base_url, 'User-Agent': 'PostmanRuntime/7.29.0', 'Content-Type': 'text/plain'}
    url1 = base_url + '/auth/verify_sms'
    re1 = requests.post(url=url1, data=json.dumps(json1), headers=headers)
    print(re1.json())
    branch1 = str(branch).lower()
    ma = os.popen(f'/Users/lay/Desktop/getPhoneCode --db project_{branch1} --phone 13902995544').read()[:6]
    json2 = {
        "phone": "+8613902995544",
        "phone_code": f"{ma}",
        "name": "吴帅",
        "referrer": "",
        "keyword": "",
        "channel": "",
        "email": f"{mail}",
        "password": "a12345678",
        "team_name": "ones",
        "team_role": "CTO",
        "team_scale": "10 人以下",
        "industry": "互联网"
    }
    url2 = base_url + '/auth/create_team'
    re2 = requests.post(url=url2, data=json.dumps(json2), headers=headers)
    print('email:  ' + re2.json()['user']['email'])
    print('org_uuid: ' + re2.json()['org']['uuid'])
    with open('/Users/lay/PycharmProjects/pythonProject/account', 'a') as f:
        f.write('email: ' + str(re2.json()['user']['email']) + '   ')
        f.write('org_uuid: ' + str(re2.json()['org']['uuid']))
        f.write('\n')


def register_pending(mail, branch):
    base_url = f'https://devapi.myones.net/project/{branch}'
    json1 = {
        "phone": "+8613902995544"
    }
    os.popen('/Users/lay/Desktop/reflushRedis')
    headers = {'referer': base_url, 'User-Agent': 'PostmanRuntime/7.29.0', 'Content-Type': 'text/plain'}
    url1 = base_url + '/auth/verify_sms'
    re1 = requests.post(url=url1, data=json.dumps(json1), headers=headers)
    print(re1.json())
    branch1 = str(branch).lower()
    ma = os.popen(f'/Users/lay/Desktop/getPhoneCode --db project_{branch1} --phone 13902995544').read()[:6]
    json2 = {
        "phone": "+8613902995544",
        "phone_code": f"{ma}",
        "email": f"{mail}",
        "password": "a12345678"
    }
    url2 = base_url + '/auth/create_pending_org'
    re2 = requests.post(url=url2, data=json.dumps(json2), headers=headers)
    print(re2.json())
    print('email:  ' + mail)
    print('org_uuid: ' + re2.json()['org']['org_uuid'])
    with open('/Users/lay/PycharmProjects/pythonProject/account', 'a') as f:
        f.write('email: ' + mail + '   ')
        f.write('org_uuid: ' + str(re2.json()['org']['org_uuid']))
        f.write('\n')


if __name__ == '__main__':
    branch = 'P3039_P1055'
    if len(sys.argv) > 1:
        register(sys.argv[2], sys.argv[1])
        print('password:  a12345678')
    else:
        register('072212@ones.ai', branch)
    # register_pending('P303704@ones.ai', branch)
