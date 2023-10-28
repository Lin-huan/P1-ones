import json
import time
import requests
import os
import jenkins


def get_phone_code(phone=13902995544, preview='preview3'):

    os.environ['PYTHONHTTPSVERIFY'] = '0'
    server = jenkins.Jenkins('https://cd.myones.net/', 'linhuan@ones.ai', '1141e60a525f3edd925742df0e1c3bdd55')
    build_num_1 = server.get_job_info(f'{preview}_phone_code')['builds'][0]['number']
    server.build_job(f'{preview}_phone_code', {'phone': phone})
    build_num = server.get_job_info(f'{preview}_phone_code')['builds'][0]['number']
    while build_num == build_num_1:
        time.sleep(3)
        build_num = server.get_job_info(f'{preview}_phone_code')['builds'][0]['number']
    time.sleep(2)
    print(str(server.get_build_console_output(f'{preview}_phone_code', build_num)))
    code = str(server.get_build_console_output(f'{preview}_phone_code', build_num)).split('\n')[-3]
    print(code, build_num)
    return code


def create_pending(edition='free', preview='preview3', language='zh', mail=''):
    if preview == 'preview1':
        preview_base_url = 'https://preview1.myones.net/project/api/project'
    elif preview == 'preview3':
        preview_base_url = 'https://preview3.myones.net/project/api/project'
    else:
        preview_base_url = ''
    time1 = time.strftime('%m%d%H%M%S', time.localtime(time.time()))
    if mail == '':
        mail = str(time1) + '@ones.ai'
    phone = '1' + str(time1)
    json1 = {
        "phone": f"+86{phone}"
    }
    headers = {'referer': preview_base_url,
               'User-Agent': 'PostmanRuntime/7.29.0',
               'Content-Type': 'text/plain',
               'Accept-Language': f'{language}'}
    url1 = preview_base_url + '/auth/verify_sms'
    re1 = requests.post(url=url1, data=json.dumps(json1), headers=headers)
    print(re1.json())
    ma = get_phone_code(int(phone), preview=preview)
    json2 = {
        "email": mail,
        "password": "a12345678",
        "phone": f'+86{phone}',
        "phone_code": f'{ma}',
        "edition": f'{edition}'
    }
    url2 = preview_base_url + '/auth/create_pending_org'
    re2 = requests.post(url=url2, data=json.dumps(json2), headers=headers)
    print(re2.json())
    print('email:  ' + mail)
    print('org_uuid: ' + re2.json()['org']['org_uuid'])
    with open('/Users/lay/PycharmProjects/pythonProject/account', 'a') as f:
        f.write(f'{preview}  ' + edition + '  ')
        f.write('email: ' + str(mail) + '  ')
        f.write('org_uuid: ' + str(re2.json()['org']['org_uuid']))
        f.write('\n')


if __name__ == '__main__':
    # get_phone_code(13902995544, 'preview3')
    for i in range(1):
        create_pending('free', 'preview1', 'zh')
