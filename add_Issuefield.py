import json
import random

import requests
preview1 = {
    'referer_url': f'https://preview1.myones.net/project',
    'base_url': f'https://preview1.myones.net/project/api/project'
}
new_dev = {
    'referer_url': f'http://119.23.64.94/project',
    'base_url': f'http://119.23.64.94/project/api/project'
    # 'referer_url': f'http://120.79.214.210/project',
    # 'base_url': f'http://120.79.214.210/project/api/project'
}


new_dev1 = {
    'referer_url': f'https://preview3.dev.myones.net/project/',
    'base_url': f'https://preview3.dev.myones.net/project/api/project/'
    # 'referer_url': f'http://120.79.214.210/project',
    # 'base_url': f'http://120.79.214.210/project/api/project'
}
# 运行环境配置
data = new_dev1

class add():

    def login(self, email, password):
        headers = {'referer': data['referer_url'],
                   'User-Agent': 'PostmanRuntime/7.29.0',
                   'Content-Type': 'text/plain'}
        data1 = {
            "password": password,
            "email": email
        }
        url1 = f'{data["base_url"]}/auth/login'
        result = requests.post(url=url1, data=json.dumps(data1), headers=headers)
        print(result.json())

        user_uuid = result.json()["user"]["uuid"]
        token = result.json()["user"]["token"]
        # teams_uuid = result.json()["teams"][0]["uuid"]
        teams_uuid = "BkcCPv2Q"
        user_dict = {"user_uuid": user_uuid, "token": token, "teams_uuid": teams_uuid}
        return user_dict

    def addDanhang(self, user_dict):
        url = f'{data["base_url"]}/team/{user_dict["teams_uuid"]}/fields/add'

        json_data = {
            'field': {
                'name': 'zdy单行文本'+str(random.randint(100000, 999999)),
                'type': 2,
                'renderer': 1,
                'filter_option': 0,
                'search_option': 1,
            },
        }
        headers = {'referer': data['base_url'],
                   'User-Agent': 'PostmanRuntime/7.29.2',
                   'Content-Type': 'text/plain',
                   'Ones-User-Id': user_dict['user_uuid'],
                   'Ones-Auth-Token': user_dict['token']}

        res = requests.post(url=url, data=json.dumps(json_data), headers=headers)
        if res.status_code == 200:
            print(res.json())
        else:
            print(res.status_code)
            print(res.json())

        def addDanhang(self, user_dict):
            url = f'{data["base_url"]}/team/{user_dict["teams_uuid"]}/fields/add'

            json_data = {
                'field': {
                    'name': 'dy单行文本' + str(random.randint(100000, 999999)),
                    'type': 2,
                    'renderer': 1,
                    'filter_option': 0,
                    'search_option': 1,
                },
            }
            headers = {'referer': data['base_url'],
                       'User-Agent': 'PostmanRuntime/7.29.2',
                       'Content-Type': 'text/plain',
                       'Ones-User-Id': user_dict['user_uuid'],
                       'Ones-Auth-Token': user_dict['token']}

            res = requests.post(url=url, data=json.dumps(json_data), headers=headers)
            if res.status_code == 200:
                print(res.json())
            else:
                print(res.status_code)
                print(res.json())
    def addDuohang(self, user_dict):
        url = f'{data["base_url"]}/team/{user_dict["teams_uuid"]}/fields/add'
        json_data = {
            'field': {
                'name': 'zdy多行文本'+str(random.randint(100000, 999999)),
                'type': 15,
                'renderer': 1,
                'filter_option': 0,
                'search_option': 1,
            },
        }
        headers = {'referer': data['base_url'],
                   'User-Agent': 'PostmanRuntime/7.29.2',
                   'Content-Type': 'text/plain',
                   'Ones-User-Id': user_dict['user_uuid'],
                   'Ones-Auth-Token': user_dict['token']}

        res = requests.post(url=url, data=json.dumps(json_data), headers=headers)
        if res.status_code == 200:
            print(res.json())
        else:
            print(res.status_code)
            print(res.json())
    def addDanxuan(self, user_dict):
        url = f'{data["base_url"]}/team/{user_dict["teams_uuid"]}/fields/add'
        json_data = {
            'field': {
                'name': 'zdy单选菜单'+str(random.randint(100000, 999999)),
                'type': 1,
                'options': [
                    {
                        'value': '1111aaaaa啊啊啊啊啊啊啊啊啊啊啊',
                        'background_color': '#307fe2',
                        'color': '#fff',
                    },
                    {
                        'value': '2222bbbb拜拜拜拜拜拜拜拜拜拜拜拜吧',
                        'background_color': '#00b388',
                        'color': '#fff',
                    },
                ],
                'renderer': 1,
                'filter_option': 0,
                'search_option': 1,
            },
        }
        headers = {'referer': data['base_url'],
                   'User-Agent': 'PostmanRuntime/7.29.2',
                   'Content-Type': 'text/plain',
                   'Ones-User-Id': user_dict['user_uuid'],
                   'Ones-Auth-Token': user_dict['token']}

        res = requests.post(url=url, data=json.dumps(json_data), headers=headers)
        if res.status_code == 200:
            print(res.json())
        else:
            print(res.status_code)
            print(res.json())
    def addDuoxuan(self, user_dict):
        url = f'{data["base_url"]}/team/{user_dict["teams_uuid"]}/fields/add'
        json_data = {
            'field': {
                'name': 'zdy多选菜单'+str(random.randint(100000, 999999)),
                'type': 16,
                'options': [
                    {
                        'value': 'qqqq钱钱钱钱',
                        'background_color': '#307fe2',
                        'color': '#fff',
                    },
                    {
                        'value': 'wwwwwwwwwwwwwwwwww我呜呜呜呜',
                        'background_color': '#00b388',
                        'color': '#fff',
                    },
                ],
                'renderer': 1,
                'filter_option': 0,
                'search_option': 1,
            },
        }
        headers = {'referer': data['base_url'],
                   'User-Agent': 'PostmanRuntime/7.29.2',
                   'Content-Type': 'text/plain',
                   'Ones-User-Id': user_dict['user_uuid'],
                   'Ones-Auth-Token': user_dict['token']}

        res = requests.post(url=url, data=json.dumps(json_data), headers=headers)
        if res.status_code == 200:
            print(res.json())
        else:
            print(res.status_code)
            print(res.json())
    def addRiqi(self, user_dict):
        url = f'{data["base_url"]}/team/{user_dict["teams_uuid"]}/fields/add'
        json_data = {
            'field': {
                'name': 'zdy日期'+str(random.randint(100000, 999999)),
                'type': 5,
                'renderer': 1,
                'filter_option': 0,
                'search_option': 1,
            },
        }
        headers = {'referer': data['base_url'],
                   'User-Agent': 'PostmanRuntime/7.29.2',
                   'Content-Type': 'text/plain',
                   'Ones-User-Id': user_dict['user_uuid'],
                   'Ones-Auth-Token': user_dict['token']}

        res = requests.post(url=url, data=json.dumps(json_data), headers=headers)
        if res.status_code == 200:
            print(res.json())
        else:
            print(res.status_code)
            print(res.json())
    def addShijian(self, user_dict):
        url = f'{data["base_url"]}/team/{user_dict["teams_uuid"]}/fields/add'
        json_data = {
            'field': {
                'name': 'zdy时间'+str(random.randint(100000, 999999)),
                'type': 6,
                'renderer': 1,
                'filter_option': 0,
                'search_option': 1,
            },
        }
        headers = {'referer': data['base_url'],
                   'User-Agent': 'PostmanRuntime/7.29.2',
                   'Content-Type': 'text/plain',
                   'Ones-User-Id': user_dict['user_uuid'],
                   'Ones-Auth-Token': user_dict['token']}

        res = requests.post(url=url, data=json.dumps(json_data), headers=headers)
        if res.status_code == 200:
            print(res.json())
        else:
            print(res.status_code)
            print(res.json())
    def addDanxuanDiedai(self, user_dict):
        url = f'{data["base_url"]}/team/{user_dict["teams_uuid"]}/fields/add'
        json_data = {
            'field': {
                'name': 'zdy单选迭代'+str(random.randint(100000, 999999)),
                'type': 7,
                'renderer': 1,
                'filter_option': 0,
                'search_option': 1,
            },
        }
        headers = {'referer': data['base_url'],
                   'User-Agent': 'PostmanRuntime/7.29.2',
                   'Content-Type': 'text/plain',
                   'Ones-User-Id': user_dict['user_uuid'],
                   'Ones-Auth-Token': user_dict['token']}

        res = requests.post(url=url, data=json.dumps(json_data), headers=headers)
        if res.status_code == 200:
            print(res.json())
        else:
            print(res.status_code)
            print(res.json())
    def addDanxuanChengyuan(self, user_dict):
        url = f'{data["base_url"]}/team/{user_dict["teams_uuid"]}/fields/add'
        json_data = {
            'field': {
                'name': 'zdy单选成员'+str(random.randint(100000, 999999)),
                'type': 8,
                'renderer': 1,
                'filter_option': 0,
                'search_option': 1,
            },
        }
        headers = {'referer': data['base_url'],
                   'User-Agent': 'PostmanRuntime/7.29.2',
                   'Content-Type': 'text/plain',
                   'Ones-User-Id': user_dict['user_uuid'],
                   'Ones-Auth-Token': user_dict['token']}

        res = requests.post(url=url, data=json.dumps(json_data), headers=headers)
        if res.status_code == 200:
            print(res.json())
        else:
            print(res.status_code)
            print(res.json())
    def addDuoxuanChengyuan(self, user_dict):
        url = f'{data["base_url"]}/team/{user_dict["teams_uuid"]}/fields/add'
        json_data = {
            'field': {
                'name': 'zdy多选成员'+str(random.randint(100000, 999999)),
                'type': 13,
                'renderer': 1,
                'filter_option': 0,
                'search_option': 1,
            },
        }
        headers = {'referer': data['base_url'],
                   'User-Agent': 'PostmanRuntime/7.29.2',
                   'Content-Type': 'text/plain',
                   'Ones-User-Id': user_dict['user_uuid'],
                   'Ones-Auth-Token': user_dict['token']}

        res = requests.post(url=url, data=json.dumps(json_data), headers=headers)
        if res.status_code == 200:
            print(res.json())
        else:
            print(res.status_code)
            print(res.json())
    def addDuoxuanXiangmu(self, user_dict):
        url = f'{data["base_url"]}/team/{user_dict["teams_uuid"]}/fields/add'
        json_data = {
            'field': {
                'name': 'zdy多选项目'+str(random.randint(100000, 999999)),
                'type': 50,
                'renderer': 1,
                'filter_option': 0,
                'search_option': 1,
            },
        }
        headers = {'referer': data['base_url'],
                   'User-Agent': 'PostmanRuntime/7.29.2',
                   'Content-Type': 'text/plain',
                   'Ones-User-Id': user_dict['user_uuid'],
                   'Ones-Auth-Token': user_dict['token']}

        res = requests.post(url=url, data=json.dumps(json_data), headers=headers)
        if res.status_code == 200:
            print(res.json())
        else:
            print(res.status_code)
            print(res.json())
    def addZhengshu(self, user_dict):
        url = f'{data["base_url"]}/team/{user_dict["teams_uuid"]}/fields/add'
        json_data = {
            'field': {
                'name': 'zdy整数'+str(random.randint(100000, 999999)),
                'type': 3,
                'renderer': 1,
                'filter_option': 0,
                'search_option': 1,
            },
        }
        headers = {'referer': data['base_url'],
                   'User-Agent': 'PostmanRuntime/7.29.2',
                   'Content-Type': 'text/plain',
                   'Ones-User-Id': user_dict['user_uuid'],
                   'Ones-Auth-Token': user_dict['token']}

        res = requests.post(url=url, data=json.dumps(json_data), headers=headers)
        if res.status_code == 200:
            print(res.json())
        else:
            print(res.status_code)
            print(res.json())
    def addFudianshu(self, user_dict):
        url = f'{data["base_url"]}/team/{user_dict["teams_uuid"]}/fields/add'
        json_data = {
            'field': {
                'name': 'zdy浮点数'+str(random.randint(100000, 999999)),
                'type': 4,
                'renderer': 1,
                'filter_option': 0,
                'search_option': 1,
            },
        }
        headers = {'referer': data['base_url'],
                   'User-Agent': 'PostmanRuntime/7.29.2',
                   'Content-Type': 'text/plain',
                   'Ones-User-Id': user_dict['user_uuid'],
                   'Ones-Auth-Token': user_dict['token']}

        res = requests.post(url=url, data=json.dumps(json_data), headers=headers)
        if res.status_code == 200:
            print(res.json())
        else:
            print(res.status_code)
            print(res.json())


if __name__ == '__main__':
    test = add()
    user_dict = test.login("marsdev@ones.ai", "Test1234")
    # user_dict = test.login("marsdev@ones.ai", "Test1234")
    # user_dict = test.login("admin@localhost", "qwertyui1")
    # user_dict = test.login("wuxingjuan+01@ones.ai", "juan1997")
    for i in range(1):
        test.addDanhang(user_dict) #单行
        test.addDuohang(user_dict) #多行
        test.addDanxuan(user_dict) #单选
        test.addDuoxuan(user_dict) #多选
        test.addRiqi(user_dict) #日期
        test.addShijian(user_dict) #时间
        test.addDanxuanDiedai(user_dict) #单选迭代
        test.addDanxuanChengyuan(user_dict) #单选成员
        test.addDuoxuanChengyuan(user_dict) #多选成员
        test.addDuoxuanXiangmu(user_dict) #多选项目
        test.addZhengshu(user_dict) #整数
        test.addFudianshu(user_dict) #浮点数
        # test.addDanxuan(user_dict, type="option")
