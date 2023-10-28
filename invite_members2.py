import json
import requests
import time


# 登录邀请方账号/auth/login
def login(email, password='a12345678'):
    headers = {'referer': data['referer_url'],
               'User-Agent': 'PostmanRuntime/7.29.0',
               'Content-Type': 'text/plain'}
    data1 = {
        "password": password,
        "email": email
    }
    url1 = f'{data["base_url"]}/auth/login'
    re1 = requests.post(url=url1, data=json.dumps(data1), headers=headers)
    print(re1.json())
    dict1 = {'uuid': re1.json()['user']['uuid'],
             'token': re1.json()['user']['token'],
             'team_uuid': re1.json()['teams'][0]['uuid']}
    print(dict1)
    return dict1


# 邀请成员/invitations/add_batch
def invite_members(team_uuid, uuid, token, invite_count, license_types=(1, 2, 3)):
    license_types = list(license_types)
    headers = {'referer': data['referer_url'],
               'User-Agent': 'PostmanRuntime/7.29.0',
               'Content-Type': 'text/plain',
               'Ones-User-Id': uuid,
               'Ones-Auth-Token': token}

    time1 = time.strftime('%m%d%H%M%S', time.localtime(time.time()))  # 获取当前时间戳
    mail_list = []
    for i in range(invite_count):
        mail = str(time1) + str(i) + '@ones.ai'
        # dictnew={"email":mail}
        mail_list.append({"email": mail})
    print(mail_list)

    url1 = f'{data["base_url"]}/team/{team_uuid}/invitations/add_batch'
    data1 = {"invite_settings": mail_list, "license_types": license_types}
    re1 = requests.post(url=url1, data=json.dumps(data1), headers=headers)
    print(re1.json())


# 获取验证码get
def get_invite_code(uuid, token, team_uuid):
    headers = {'referer': data['referer_url'],
               'User-Agent': 'PostmanRuntime/7.29.0',
               'Content-Type': 'text/plain',
               'Ones-User-Id': uuid,
               'Ones-Auth-Token': token}

    url1 = f'{data["base_url"]}/team/{team_uuid}/invitations'

    response = requests.get(url1, headers=headers)
    invite_code = []
    for i in response.json()['invitations']:
        if i['status'] == 1:
            list1 = [i['email'], i['code']]
            invite_code.append(list1)
    print(invite_code)
    return invite_code


# 邀请方加入
def invite_join_team(uuid, token, invite_email, invite_code):
    headers = {'referer': data['referer_url'],
               'User-Agent': 'PostmanRuntime/7.29.0',
               'Content-Type': 'text/plain',
               'Ones-User-Id': uuid,
               'Ones-Auth-Token': token}
    json_data = {
        'email': invite_email,
        'password': 'a12345678',
        'name': invite_email,
        'invite_code': invite_code,
    }
    url1 = f'{data["base_url"]}/auth/invite_join_team'
    response = requests.post(url1, headers=headers, json=json_data)
    print(response.json())


def invite(email, invite_count, invite_team='', password='a12345678', license_type=(1, 2, 3)):
    """
    :param email: 管理员账号
    :param invite_count: 邀请成员数量
    :param invite_team: 在哪个团队邀请，默认为空字符串代表多团队时在第一个团队邀请，单团队时为空字符串即可
    :param password: 管理员账号对应的密码，默认为a12345678
    :param license_type: 邀请成员授权管理，默认为三大件
    :return: Null
    """
    user_data = login(email, password)
    if invite_team == '':
        invite_members(user_data['team_uuid'], user_data['uuid'], user_data['token'], invite_count, license_type)
        invite_code = get_invite_code(user_data['uuid'], user_data['token'], user_data['team_uuid'])
    else:
        invite_members(invite_team, user_data['uuid'], user_data['token'], invite_count, license_type)
        invite_code = get_invite_code(user_data['uuid'], user_data['token'], invite_team)
    for i in invite_code:
        invite_join_team(user_data['uuid'], user_data['token'], i[0], i[1])
        # 循环


# dev
branch = 'P3064'
dev = {
    'referer_url': f'https://dev.myones.net/project/{branch}',
    'base_url': f'https://devapi.myones.net/project/{branch}'
}
# preview3
preview3 = {
    'referer_url': f'https://preview3.myones.net/project',
    'base_url': f'https://preview3.myones.net/project/api/project'
}
# preview1
preview1 = {
    'referer_url': f'https://preview1.myones.net/project',
    'base_url': f'https://preview1.myones.net/project/api/project'
}
# 私有部署
port = '14118'
private = {
    'referer_url': f'https://mars-dev.myones.net:{port}/project',
    'base_url': f'https://mars-dev.myones.net:{port}/project/api/project'
}

# SaaS
SaaS = {
    'referer_url': f'https://ones.cn/project/api/project',
    'base_url': f'https://ones.cn/project/api/project'
}

# 堡垒机
new_dev = {
    'referer_url': f'http://39.108.97.156/project',
    'base_url': f'http://39.108.97.156/project/api/project'
    # 'referer_url': f'http://120.79.214.210/project',
    # 'base_url': f'http://120.79.214.210/project/api/project'
}
# 堡垒机
new_dev1 = {
    'referer_url': f'https://preview3-0823.dev.myones.net/project',
    'base_url': f'https://preview3-0823.dev.myones.net/project/api/project'
    # 'referer_url': f'http://120.79.214.210/project',
    # 'base_url': f'http://120.79.214.210/project/api/project'
}
# 运行环境配置
data = new_dev1

if __name__ == '__main__':
    invite(email='marsdev@ones.ai', invite_count=10, invite_team='',
           password='Test1234', license_type=("1", "2", "3"))
