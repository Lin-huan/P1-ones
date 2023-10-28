import json
import random

import requests

new_dev = {
    'referer_url': f'http://47.106.207.123/project',
    'base_url': f'http://47.106.207.123/project/api/project'
    # 'referer_url': f'http://120.79.214.210/project',
    # 'base_url': f'http://120.79.214.210/project/api/project'
}
# 运行环境配置
data = new_dev

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
        teams_uuid = "PCXFsr34"
        user_dict = {"user_uuid": user_uuid, "token": token, "teams_uuid": teams_uuid}
        return user_dict

    def addDanhang(self, user_dict):
        url = f'{data["base_url"]}/team/{user_dict["teams_uuid"]}/items/add'
        json_data = {'Item': {
            "field_type": "text",
            "name": "a" + str(random.randint(100000, 999999)),
            "item_type": "field",
            "pool": "project",
            "context": {"type": "team"}
        }}
        # json_data = {
        #     'field': {
        #         'name': 'zzzz单行文本11'+str(random.randint(100000, 999999)),
        #         'type': 2,
        #         'renderer': 1,
        #         'filter_option': 0,
        #         'search_option': 1,
        #     },
        # }
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

    # def addDanxuan(self, user_dict, type):
    #     url = base_url + f"/team/{user_dict['teams_uuid']}/items/add"
    #     json_data = {
    #         "item": {
    #             "field_type": type,
    #             "name": "b" + str(random.randint(100000, 999999)),
    #             "options": [{
    #                 "value": "选项a",
    #                 "background_color": "#307fe2",
    #                 "color": "#fff"
    #             },
    #                 {
    #                     "value": "选项b",
    #                     "background_color": "#00b388",
    #                     "color": "#fff"
    #                 }
    #             ],
    #             "item_type": "field",
    #             "pool": "projec"
    #                     "t",
    #             "context": {
    #                 "type": "team"
    #             }
    #         }
    #     }
    #     headers = {'referer': data['base_url'],
    #                'User-Agent': 'PostmanRuntime/7.29.2',
    #                'Content-Type': 'text/plain',
    #                'Ones-User-Id': user_dict['user_uuid'],
    #                'Ones-Auth-Token': user_dict['token']}
    #
    #     res = requests.post(url=url, data=json.dumps(json_data), headers=headers)
    #     if res.status_code == 200:
    #         print(res.json())
    #     else:
    #         print(res.status_code)
    #         print(res.json())


if __name__ == '__main__':
    test = add()
    # user_dict = test.login("lin806527@ones.ai", "a123456789")
    user_dict = test.login("marsdev@ones.ai", "Test1234")
    for i in range(5):
        test.addDanhang(user_dict)
        # test.addDanxuan(user_dict, type="option")
