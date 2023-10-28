import requests

cookies = {
    'ones-uid': 'Lk4hwHR7',
    'ones-lt': 'Eb2z2uNSgC18ShqrhxKX3TrkPze6KUiTns49woOn5pgeBS4aXw5VVrFcO1Lsb7Nk',
    'sensorsdata2015jssdkcross': '%7B%22distinct_id%22%3A%22Lk4hwHR7%22%2C%22first_id%22%3A%22187fe6debe9a9-00a47c74067621d8-1e525634-1296000-187fe6debea7cb%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22url%E7%9A%84domain%E8%A7%A3%E6%9E%90%E5%A4%B1%E8%B4%A5%22%2C%22%24latest_search_keyword%22%3A%22url%E7%9A%84domain%E8%A7%A3%E6%9E%90%E5%A4%B1%E8%B4%A5%22%2C%22%24latest_referrer%22%3A%22url%E7%9A%84domain%E8%A7%A3%E6%9E%90%E5%A4%B1%E8%B4%A5%22%7D%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfbG9naW5faWQiOiJMazRod0hSNyIsIiRpZGVudGl0eV9jb29raWVfaWQiOiIxODdmZTZkZWJlOWE5LTAwYTQ3Yzc0MDY3NjIxZDgtMWU1MjU2MzQtMTI5NjAwMC0xODdmZTZkZWJlYTdjYiJ9%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%24identity_login_id%22%2C%22value%22%3A%22Lk4hwHR7%22%7D%2C%22%24device_id%22%3A%22187fe6debe9a9-00a47c74067621d8-1e525634-1296000-187fe6debea7cb%22%7D',
    'timezone': 'Asia/Shanghai',
    'language': 'zh',
    'ct': '290cad076e1dc1ce35422934f5a682ea5156c16965b522a1561e58980752e026',
}

headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'zh',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json',
    # 'Cookie': 'ones-uid=Lk4hwHR7; ones-lt=Eb2z2uNSgC18ShqrhxKX3TrkPze6KUiTns49woOn5pgeBS4aXw5VVrFcO1Lsb7Nk; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22Lk4hwHR7%22%2C%22first_id%22%3A%22187fe6debe9a9-00a47c74067621d8-1e525634-1296000-187fe6debea7cb%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22url%E7%9A%84domain%E8%A7%A3%E6%9E%90%E5%A4%B1%E8%B4%A5%22%2C%22%24latest_search_keyword%22%3A%22url%E7%9A%84domain%E8%A7%A3%E6%9E%90%E5%A4%B1%E8%B4%A5%22%2C%22%24latest_referrer%22%3A%22url%E7%9A%84domain%E8%A7%A3%E6%9E%90%E5%A4%B1%E8%B4%A5%22%7D%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfbG9naW5faWQiOiJMazRod0hSNyIsIiRpZGVudGl0eV9jb29raWVfaWQiOiIxODdmZTZkZWJlOWE5LTAwYTQ3Yzc0MDY3NjIxZDgtMWU1MjU2MzQtMTI5NjAwMC0xODdmZTZkZWJlYTdjYiJ9%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%24identity_login_id%22%2C%22value%22%3A%22Lk4hwHR7%22%7D%2C%22%24device_id%22%3A%22187fe6debe9a9-00a47c74067621d8-1e525634-1296000-187fe6debea7cb%22%7D; timezone=Asia/Shanghai; language=zh; ct=290cad076e1dc1ce35422934f5a682ea5156c16965b522a1561e58980752e026',
    'Origin': 'http://47.106.163.47',
    'Referer': 'http://47.106.163.47/project/',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
    'X-CSRF-TOKEN': '290cad076e1dc1ce35422934f5a682ea5156c16965b522a1561e58980752e026',
}

json_data = {
    'third_party_type': 7,
    'json_config': '{"corp_uuid":"wwa76530a1feeaaab1","agent_id":1000026,"secret":"qVHNppUGQnMMddP1lBbPYf8OotHTYjsZ8OXfXJgtXIE","token":"2za8fujwHwYyttad","encoding_aes_key":"itdWckX3pFMPb7Erm8hWNq8e8b4uYsLtcLveVHKCY9k","redirect_domain":"47.106.172.17","home_url":"http://47.106.163.47/project/#/org/YJgSSh2e/","message_url":"http://47.106.163.47/api/project/organization/YJgSSh2e/wechat"}',
    'match_user_by': 1,
    'mappings': [
        {
            'system_property_key': 'name',
            'third_party_property_key': 'name',
        },
        {
            'system_property_key': 'email',
            'third_party_property_key': 'email',
        },
    ],
}

response = requests.post(
    'http://47.106.163.47/project/api/project/organization/YJgSSh2e/thirdparty/base/add_or_update',
    cookies=cookies,
    headers=headers,
    json=json_data,
    verify=False,
)

# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"third_party_type":7,"json_config":"{\\"corp_uuid\\":\\"wwa76530a1feeaaab1\\",\\"agent_id\\":1000026,\\"secret\\":\\"qVHNppUGQnMMddP1lBbPYf8OotHTYjsZ8OXfXJgtXIE\\",\\"token\\":\\"2za8fujwHwYyttad\\",\\"encoding_aes_key\\":\\"itdWckX3pFMPb7Erm8hWNq8e8b4uYsLtcLveVHKCY9k\\",\\"redirect_domain\\":\\"47.106.163.47\\",\\"home_url\\":\\"http://47.106.163.47/project/#/org/YJgSSh2e/\\",\\"message_url\\":\\"http://47.106.163.47/api/project/organization/YJgSSh2e/wechat\\"}","match_user_by":1,"mappings":[{"system_property_key":"name","third_party_property_key":"name"},{"system_property_key":"email","third_party_property_key":"email"}]}'
#response = requests.post(
#    'http://47.106.163.47/project/api/project/organization/YJgSSh2e/thirdparty/base/add_or_update',
#    cookies=cookies,
#    headers=headers,
#    data=data,
#    verify=False,
#)