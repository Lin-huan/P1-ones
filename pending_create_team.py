import json
import requests
import pymysql
import random
import os

branch = "P1080"
base_url = f"https://devapi.myones.net/project/{branch}"
phone = "+8613724272946"
database = 'project_p1080'


class PendingCreateTeam():

    def send_code(self):
        url = base_url + "/auth/verify_sms"
        json_data = {"phone": phone}
        headers = {'referer': base_url}
        # os.popen('/Users/linhuan/Documents/reflushRedis')
        os.popen('reflushRedis')
        res = requests.post(url=url, data=json.dumps(json_data), headers=headers)
        if res.status_code == 200:
            print(res.json())
        else:
            print(res.status_code)

    def select_sql(self):
        db = pymysql.connect(host='119.23.130.213',
                             user='onesdev',
                             password='onesdev',
                             database=database,
                             charset='utf8')
        cursor = db.cursor()
        cursor.execute(f"SELECT * FROM phone_code WHERE phone ={phone}")
        result = cursor.fetchall()
        code = result[-1][1]
        db.close()
        return code

    def create_pending_org(self):
        code = self.select_sql()
        url1 = base_url + "/auth/create_pending_org"
        email = "lin" + str(random.randint(100000, 999999)) + "@ones.ai"
        json_data1 = {
            "email": email,
            "password": "a123456789",
            "phone": phone,
            "phone_code": code,
            "edition": "free"
        }
        headers1 = {
            "referer": base_url,
            "Accept-Language": "cn"
        }
        res1 = requests.post(url=url1, data=json.dumps(json_data1), headers=headers1)
        print(email)
        org_uuid = res1.json()["org"]["org_uuid"]
        user_uuid = res1.json()["user_uuid"]
        return org_uuid, user_uuid

    def create_pending_team(self):
        a = self.create_pending_org()
        org_uuid = a[0]
        user_uuid = a[1]
        url2 = base_url + "/auth/complete_pending_org"
        json_data2 = {
            "org_uuid": org_uuid,
            "name": "lin",
            "team_name": "ones-tim3",
            "user_uuid": user_uuid,
            "referrer": "",
            "keyword": "",
            "channel": "",
            "team_role": "测试",
            "team_scale": "11-30人",
            "industry": "电商",
            "scenarios": "效能管理,项目集管理,工单管理,DevOps,产品管理",
            "need_support": True
        }
        headers2 = {
            "referer": base_url,
            "Accept-Language": "cn"
        }
        res2 = requests.post(url=url2, data=json.dumps(json_data2), headers=headers2)
        if res2.status_code == 200:
            print("email:" + res2.json()["user"]["email"])
            print("org_uuid:" + res2.json()["org"]["uuid"])
        else:
            print(res2.status_code)


if __name__ == "__main__":

    test = PendingCreateTeam()
    test.send_code()
    test.create_pending_org()

    # test.create_pending_team()
