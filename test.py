import requests

headers = {
    'Ones-Plugin-Id': '49603a62',
    'Ones-Check-Point': 'team',
    'Content-Type': 'application/json',
}

json_data = {
    'type': 'task',
    'group_name': '部门岗位职级属性组67',
    'group_uuid': '新建时无需填写',
    'fields': [
        {
            'name': '部门部门部门部门部门部门部门部门部门部门部门foot',
            'uuid': '新建时无需填写',
            'type': 'multipleChoice',
            'field_position': 1,
            'options': [
                {
                    'uuid': 'yanfa1',
                    'name': '研发一组',
                    'index': 1,
                    'path': 'yanfa1',
                },
                {
                    'uuid': 'yanfa2',
                    'name': '研发二组',
                    'index': 2,
                    'path': 'yanfa2',
                },
                {
                    'uuid': 'yanfa3',
                    'name': '研发三组三三三三三三三三三三三三三',
                    'index': 3,
                    'path': 'yanfa3',
                },
                {
                    'uuid': 'yanfa4',
                    'name': '研发四组44444444444',
                    'index': 4,
                    'path': 'yanfa4',
                },
                {
                    'uuid': 'yanfa5',
                    'name': '研发五组呜呜呜呜呜呜呜呜呜呜呜呜呜呜呜呜呜呜呜呜呜呜呜呜呜呜呜呜呜呜呜',
                    'index': 5,
                    'path': 'yanfa5',
                },

            ],
        },
        {
            'name': '岗位foot',
            'uuid': '新建时无需填写',
            'type': 'multipleChoice',
            'field_position': 2,
            'options': [
                {
                    'uuid': 'Front-End',
                    'name': '前端开发',
                    'index': 1,
                    'path': 'yanfa1::Front-End',
                },
                {
                    'uuid': 'Back-End',
                    'name': '后端开发',
                    'index': 2,
                    'path': 'yanfa1::Back-End',
                },
                {
                    'uuid': 'UI',
                    'name': '界面设计',
                    'index': 3,
                    'path': 'yanfa1::UI',
                },
                {
                    'uuid': 'yunwei',
                    'name': '运维',
                    'index': 4,
                    'path': 'yanfa1::yunwei',
                },
                {
                    'uuid': 'Back-End',
                    'name': '后端开发',
                    'index': 2,
                    'path': 'yanfa2::Back-End',
                },
                {
                    'uuid': 'yunwei',
                    'name': '运维',
                    'index': 3,
                    'path': 'yanfa2::yunwei',
                },
                {
                    'uuid': 'Front-End',
                    'name': '前端开发',
                    'index': 1,
                    'path': 'yanfa2::Front-End',
                },
            ],
        },
        {
            'name': '职级foot',
            'uuid': '新建时无需填写',
            'type': 'singleChoice',
            'field_position': 3,
            'options': [
                {
                    'uuid': 'rank1',
                    'name': '初级',
                    'index': 1,
                    'path': 'yanfa1::Front-End::rank1',
                },
                {
                    'uuid': 'rank2',
                    'name': '资深',
                    'index': 1,
                    'path': 'yanfa1::Front-End::rank2',
                },
                {
                    'uuid': 'rank1',
                    'name': '初级',
                    'index': 1,
                    'path': 'yanfa1::Back-End::rank1',
                },
                {
                    'uuid': 'rank1',
                    'name': '初级',
                    'index': 1,
                    'path': 'yanfa1::UI::rank1',
                },
                {
                    'uuid': 'rank1',
                    'name': '初级',
                    'index': 1,
                    'path': 'yanfa1::yunwei::rank1',
                },
                {
                    'uuid': 'rank2',
                    'name': '资深',
                    'index': 2,
                    'path': 'yanfa1::yunwei::rank2',
                },
                {
                    'uuid': 'rank3',
                    'name': '炒鸡资深',
                    'index': 3,
                    'path': 'yanfa1::yunwei::rank3',
                },
                {
                    'uuid': 'rank3',
                    'name': '炒鸡资深',
                    'index': 1,
                    'path': 'yanfa2::Front-End::rank3',
                },
                {
                    'uuid': 'rank2',
                    'name': '资深',
                    'index': 2,
                    'path': 'yanfa2::Front-End::rank2',
                },
                {
                    'uuid': 'rank1',
                    'name': '初级',
                    'index': 3,
                    'path': 'yanfa2::Front-End::rank1',
                },
                {
                    'uuid': 'rank1',
                    'name': '初级',
                    'index': 1,
                    'path': 'yanfa2::Back-End::rank1',
                },
                {
                    'uuid': 'rank2',
                    'name': '资深',
                    'index': 1,
                    'path': 'yanfa2::yunwei::rank2',
                },
                {
                    'uuid': 'rank3',
                    'name': '炒鸡资深',
                    'index': 2,
                    'path': 'yanfa2::yunwei::rank3',
                },
                {
                    'uuid': 'rank1',
                    'name': '初级',
                    'index': 3,
                    'path': 'yanfa2::yunwei::rank1',
                },
            ],
        },
    ],
}

# response = requests.post('http://39.108.121.40/project/api/project/create_field_group', headers=headers, json=json_data)
response = requests.post('http://preview3.myones.net/project/api/project/create_field_group', headers=headers, json=json_data)

# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{\n        "type": "task",\n        "group_name": "部门岗位职级属性组67",\n        "group_uuid": "新建时无需填写",\n        "fields": [{\n                        "name": "部门",\n                        "uuid": "新建时无需填写",\n                        "type": "multipleChoice",\n                        "field_position": 1,\n                        "options": [{\n                                        "uuid": "yanfa1",\n                                        "name": "研发一组",\n                                        "index": 1,\n                                        "path": "yanfa1"\n                                },\n                                {\n                                        "uuid": "yanfa2",\n                                        "name": "研发二组",\n                                        "index": 2,\n                                        "path": "yanfa2"\n                                }\n                        ]\n                },\n                {\n                        "name": "岗位",\n                        "uuid": "新建时无需填写",\n                        "type": "multipleChoice",\n                        "field_position": 2,\n                        "options": [{\n                                        "uuid": "Front-End",\n                                        "name": "前端开发",\n                                        "index": 1,\n                                        "path": "yanfa1::Front-End"\n\n                                },\n                                {\n                                        "uuid": "Back-End",\n                                        "name": "后端开发",\n                                        "index": 2,\n                                        "path": "yanfa1::Back-End"\n\n                                },\n                                {\n                                        "uuid": "UI",\n                                        "name": "界面设计",\n                                        "index": 3,\n                                        "path": "yanfa1::UI"\n                                },\n                                {\n                                        "uuid": "yunwei",\n                                        "name": "运维",\n                                        "index": 4,\n                                        "path": "yanfa1::yunwei"\n                                },\n                                {\n                                        "uuid": "Back-End",\n                                        "name": "后端开发",\n                                        "index": 2,\n                                        "path": "yanfa2::Back-End"\n                                },\n                                {\n                                        "uuid": "yunwei",\n                                        "name": "运维",\n                                        "index": 3,\n                                        "path": "yanfa2::yunwei"\n                                },\n                                {\n                                        "uuid": "Front-End",\n                                        "name": "前端开发",\n                                        "index": 1,\n                                        "path": "yanfa2::Front-End"\n                                }\n                        ]\n                }, {\n                        "name": "职级",\n                        "uuid": "新建时无需填写",\n                        "type": "singleChoice",\n                        "field_position": 3,\n                        "options": [{\n                                        "uuid": "rank1",\n                                        "name": "初级",\n                                        "index": 1,\n                                        "path": "yanfa1::Front-End::rank1"\n                                },\n                                {\n                                        "uuid": "rank2",\n                                        "name": "资深",\n                                        "index": 1,\n                                        "path": "yanfa1::Front-End::rank2"\n                                },{\n                                        "uuid": "rank1",\n                                        "name": "初级",\n                                        "index": 1,\n                                        "path": "yanfa1::Back-End::rank1"\n                                },{\n                                        "uuid": "rank1",\n                                        "name": "初级",\n                                        "index": 1,\n                                        "path": "yanfa1::UI::rank1"\n                                },{\n                                        "uuid": "rank1",\n                                        "name": "初级",\n                                        "index": 1,\n                                        "path": "yanfa1::yunwei::rank1"\n                                },{\n                                        "uuid": "rank2",\n                                        "name": "资深",\n                                        "index": 2,\n                                        "path": "yanfa1::yunwei::rank2"\n                                },{\n                                        "uuid": "rank3",\n                                        "name": "炒鸡资深",\n                                        "index": 3,\n                                        "path": "yanfa1::yunwei::rank3"\n                                },{\n                                        "uuid": "rank3",\n                                        "name": "炒鸡资深",\n                                        "index": 1,\n                                        "path": "yanfa2::Front-End::rank3"\n                                },{\n                                        "uuid": "rank2",\n                                        "name": "资深",\n                                        "index": 2,\n                                        "path": "yanfa2::Front-End::rank2"\n                                },{\n                                        "uuid": "rank1",\n                                        "name": "初级",\n                                        "index": 3,\n                                        "path": "yanfa2::Front-End::rank1"\n                                },{\n                                        "uuid": "rank1",\n                                        "name": "初级",\n                                        "index": 1,\n                                        "path": "yanfa2::Back-End::rank1"\n                                },{\n                                        "uuid": "rank2",\n                                        "name": "资深",\n                                        "index": 1,\n                                        "path": "yanfa2::yunwei::rank2"\n                                },{\n                                        "uuid": "rank3",\n                                        "name": "炒鸡资深",\n                                        "index": 2,\n                                        "path": "yanfa2::yunwei::rank3"\n                                },{\n                                        "uuid": "rank1",\n                                        "name": "初级",\n                                        "index": 3,\n                                        "path": "yanfa2::yunwei::rank1"\n                                }\n                        ]\n                }\n        ]\n}'.encode()
#response = requests.post('http://<换成你的>/project/api/project/create_field_group', headers=headers, data=data)