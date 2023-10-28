import jenkins
import os
import time
import threading
import requests
import json


# 1.
def build_package(branch):
    os.environ['PYTHONHTTPSVERIFY'] = '0'  # 不认证证书
    server = jenkins.Jenkins('https://cd.myones.net/', jenkins_user_name, jenkins_token_cd)  # 连接jenkins

    project_name = f'development/generate-package/tar-project-api/{branch}'
    build_history = server.get_job_info(project_name)['builds']  # 获取指定job的信息get_job_info
    if len(build_history) > 0:
        build_num_1 = server.get_job_info(project_name)['builds'][0]['number']
    else:
        build_num_1 = 0
    server.build_job(project_name)  # 构建指定的job，并且传入参数build_job

    if build_num_1 == 0:
        while True:
            while True:
                try:
                    build_new = server.get_job_info(project_name)['builds']
                    break
                except BaseException:
                    time.sleep(10)
            if len(build_new) > 0:
                while True:
                    try:
                        build_num = server.get_job_info(project_name)['builds'][0]['number']
                        success = str(server.get_build_console_output(project_name, build_num))[-8:-1]
                        # 获取构建build的打印信息 get_build_console_output
                        break
                    except BaseException:
                        time.sleep(10)
                if success == 'SUCCESS' or success == 'FAILURE':
                    break
                else:
                    time.sleep(10)
            else:
                time.sleep(10)
    else:
        while True:
            while True:
                try:
                    build_num = server.get_job_info(project_name)['builds'][0]['number']
                    break
                except BaseException:
                    time.sleep(10)
            if build_num != build_num_1:
                while True:
                    try:
                        success = str(server.get_build_console_output(project_name, build_num))[-8:-1]
                        break
                    except BaseException:
                        time.sleep(10)
                if success == 'SUCCESS' or success == 'FAILURE':
                    break
                else:
                    time.sleep(10)
            else:
                time.sleep(10)



SUCCESS_list = []
FAILURE_list = []

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
    # build_private('master', [])
    # 分支名和需要打包的组件，是否机器人通知开关
    build_package('P3069')
