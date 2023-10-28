import jenkins
import os
import time
import threading
import requests
import json


def send_message(message, member_list):
    url = send_message_url
    headers = {'Content-Type': 'application/json'}
    data = {
        "msgtype": "text",
        "text": {
            "content": message,
            "mentioned_list": member_list
        }
    }
    re1 = requests.post(url=url, data=json.dumps(data), headers=headers)
    print(re1.json())


def build_package(branch, tar):
    os.environ['PYTHONHTTPSVERIFY'] = '0'
    server = jenkins.Jenkins('https://cd.myones.net/', jenkins_user_name, jenkins_token_cd)

    project_name = f'development/generate-package/tar-{tar}/{branch}'
    build_history = server.get_job_info(project_name)['builds']
    if len(build_history) > 0:
        build_num_1 = server.get_job_info(project_name)['builds'][0]['number']
    else:
        build_num_1 = 0
    server.build_job(project_name)

    if build_num_1 == 0:
        while True:
            build_new = server.get_job_info(project_name)['builds']
            if len(build_new) > 0:
                build_num = server.get_job_info(project_name)['builds'][0]['number']
                success = str(server.get_build_console_output(project_name, build_num))[-8:-1]
                if success == 'SUCCESS' or success == 'FAILURE':
                    break
                else:
                    time.sleep(10)
            else:
                time.sleep(10)
    else:
        while True:
            build_num = server.get_job_info(project_name)['builds'][0]['number']
            if build_num != build_num_1:
                success = str(server.get_build_console_output(project_name, build_num))[-8:-1]
                if success == 'SUCCESS' or success == 'FAILURE':
                    break
                else:
                    time.sleep(10)
            else:
                time.sleep(10)
    if success == 'SUCCESS':
        SUCCESS_list.append(tar)
    else:
        FAILURE_list.append(
            f'https://cd.myones.net/job/development/job/generate-package/job/tar-{tar}/job/{branch}/')


def build_image(branch, tag_list: list):
    os.environ['PYTHONHTTPSVERIFY'] = '0'
    server = jenkins.Jenkins('https://marsdev-ci.myones.net/', jenkins_user_name, jenkins_token_ci)

    project_name = f'build-image-v2'
    build_num_1 = server.get_job_info(project_name)['builds'][0]['number']

    parameters = {'projectApiBranch': 'master',
                  'projectWebBranch': 'master',
                  'wikiApiBranch': 'master',
                  'wikiWebBranch': 'master',
                  'thirdImportTag': 'v1.0.7',
                  'devopsBranch': 'master',
                  'auditlogSyncTag': 'master',
                  'mobileWebTag': '3.6.x_integration',
                  'binlogSyncTag': 'master',
                  'ones_platform_api': 'master',
                  'ones_plugin_hostboot': 'master',
                  'ones_plugin': 'master',
                  'ones_plugin_node': 'master',
                  'enablePerformancePro': 'true',
                  'supersetBranch': 'master',
                  'biSyncBranch': 'master',
                  'project_migrations': '',
                  'wiki_migrations': '',
                  'wizEditorBranch': 'master',
                  'wizEditorConvertBranch': 'master',
                  '': '',
                  'onesAIDockerVersion': 'master',
                  'baseImageVersion': 'v1.0.19',
                  'onesDataCollectorBranch': 'master',
                  'plugin_service_proxy': 'master',
                  'mysqlOperator': 'S1092',
                  'kafkaBackup': 'kafka-backup-dev-v0.0.5'
                  }
    for i in tag_list:
        parameters[change[i]] = branch
    server.build_job(project_name, parameters)
    while True:
        build_num = server.get_job_info(project_name)['builds'][0]['number']
        if build_num != build_num_1:
            break
        else:
            time.sleep(10)
    while True:
        success = str(server.get_build_console_output(project_name, build_num))[-8:-1]
        if success == 'SUCCESS' or success == 'FAILURE':
            break
        else:
            time.sleep(10)
    version = str(server.get_build_console_output(project_name, build_num)).split('\n')[22][-9:]
    if success == 'SUCCESS':
        return version
    else:
        return False


def build_install_pak(version):
    os.environ['PYTHONHTTPSVERIFY'] = '0'
    server = jenkins.Jenkins('https://marsdev-ci.myones.net/', jenkins_user_name, jenkins_token_ci)

    project_name = f'build-install-pak'
    build_num_1 = server.get_job_info(project_name)['builds'][0]['number']

    parameters = {'parameters': 'master',
                  'version': version,
                  'certificate': 'master_cn'}

    server.build_job(project_name, parameters)

    while True:
        build_num = server.get_job_info(project_name)['builds'][0]['number']
        if build_num != build_num_1:
            break
        else:
            time.sleep(10)
    while True:
        success = str(server.get_build_console_output(project_name, build_num))[-8:-1]
        if success == 'SUCCESS' or success == 'FAILURE':
            break
        else:
            time.sleep(10)

    return success


def build_create_test_env(branch, version, config='--'):
    os.environ['PYTHONHTTPSVERIFY'] = '0'
    server = jenkins.Jenkins('https://marsdev-ci.myones.net/', jenkins_user_name, jenkins_token_ci)

    project_name = f'create-test-env'
    build_num_1 = server.get_job_info(project_name)['builds'][0]['number']

    parameters = {'instance_name': branch,
                  'version': version,
                  'onesConfigureInitExtraParams': config}

    server.build_job(project_name, parameters)
    while True:
        build_num = server.get_job_info(project_name)['builds'][0]['number']
        if build_num != build_num_1:
            break
        else:
            time.sleep(10)
    while True:
        success = str(server.get_build_console_output(project_name, build_num))[-8:-1]
        if success == 'SUCCESS' or success == 'FAILURE':
            break
        else:
            time.sleep(10)

    return success


SUCCESS_list = []
FAILURE_list = []


def build_private(branch, tag_list):
    for tag in tag_list:
        thread1 = threading.Thread(target=build_package, args=(branch, tag))
        thread1.start()
    while len(SUCCESS_list) + len(FAILURE_list) != len(tag_list):
        time.sleep(10)
    if len(SUCCESS_list) != len(tag_list):
        print(f'打包失败：\n{FAILURE_list}')
        send_message(f'打包失败： \n{FAILURE_list}', ['@all'])
        return
    print(f'SUCCESS： {SUCCESS_list}')

    version = build_image(branch, tag_list)
    if not version:
        print(f'构建镜像失败')
        send_message(f'构建镜像失败: \nhttps://marsdev-ci.myones.net/view/build-private-test-env/job/build-image-v2/',
                     ['@all'])
        return
    print(f'SUCCESS build-image-v2 version: {version}')

    success = build_install_pak(version)
    if success != 'SUCCESS':
        print(f'构建安装包失败')
        send_message(f'构建安装包失败: \nhttps://marsdev-ci.myones.net/view/BUILD_PACKAGE/job/build-install-pak/',
                     ['@all'])
        return
    print(f'{success} build-install-pak')

    success = build_create_test_env(branch, version)
    if success != 'SUCCESS':
        print(f'创建测试实例失败')
        send_message(f'创建测试实例失败: \nhttps://marsdev-ci.myones.net/view/AUTO_DEPLOY/job/create-test-env/',
                     ['@all'])
    else:
        print('打包成功')
        send_message(f'{branch}私有部署打包成功', ['@all'])
        send_message(f'用完记得删除实例： \nhttps://marsdev-ci.myones.net/view/AUTO_DEPLOY/job/remove-test-env/',
                     [])


# 提醒机器人的url
send_message_url = 'https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=569464bd-e522-4a8a-82a8-294c963b4595'
# tag名称和构建参数名称映射，目前这几个是常用的，没有的自己加。。。
change = {'project-web': 'projectWebBranch',
          'project-api': 'projectApiBranch',
          'wiki-web': 'wikiWebBranch',
          'wiki-api': 'wikiApiBranch',
          'audit-log-sync': 'auditlogSyncTag',
          'onesconfigure_tool': 'onesAIDockerVersion'
          }
# 替换成自己的jenkins账号的和token，路径https://marsdev-ci.myones.net/user/***@ones.ai/configure，创建API Token
# 注意CI和CD的token不一样，需要分别获取
jenkins_user_name = 'wujiacun@ones.ai'
jenkins_token_ci = '11e7b38a13794c4ddd39a62fb82460fd4e'
jenkins_token_cd = '116c13ead74879ca807a992f2b605ca1aa'

if __name__ == '__main__':
    # 分支名和需要打包的组件
    build_private('P6869', ['project-web', 'project-api', 'audit-log-sync'])