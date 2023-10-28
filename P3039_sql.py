import pymysql
import time

database = 'project_p3039_p1055'


def select(org_uuid: str):
    db = pymysql.connect(host='119.23.130.213',
                         user='onesdev',
                         password='onesdev',
                         database=database,
                         charset='utf8')

    cursor = db.cursor()

    sql = f"SELECT * FROM license WHERE org_uuid='{org_uuid}'"
    print(sql)

    cursor.execute(sql)
    result = cursor.fetchall()

    for data in result:
        print(data)

    db.close()


def set_expire_time(org_uuid, license_type=0, edition='enterprise-trial'):
    db = pymysql.connect(host='119.23.130.213',
                         user='onesdev',
                         password='onesdev',
                         database=database,
                         charset='utf8')

    cursor = db.cursor()
    expire_time = int(time.time()) + 10

    if license_type == 0:
        sql = f"update license set " \
              f"expire_time={expire_time} where org_uuid='{org_uuid}' AND expire_time>100;"
        print(sql)
    else:
        sql = f"update license set " \
              f"expire_time={expire_time} where org_uuid='{org_uuid}' AND type={license_type} AND edition='{edition}';"
        print(sql)

    cursor.execute(sql)
    db.commit()
    db.close()


def set_multi_team(org_uuid):
    db = pymysql.connect(host='119.23.130.213',
                         user='onesdev',
                         password='onesdev',
                         database=database,
                         charset='utf8')

    cursor = db.cursor()
    sql = f"update organization set visibility=1 where uuid='{org_uuid}';"
    cursor.execute(sql)
    db.commit()
    db.close()


def run_sql(sql):
    db = pymysql.connect(host='119.23.130.213',
                         user='onesdev',
                         password='onesdev',
                         database=database,
                         charset='utf8')

    cursor = db.cursor()
    cursor.execute(sql)
    db.commit()
    result = cursor.fetchall()
    for i in result:
        print(i)
    db.close()


if __name__ == '__main__':
    set_expire_time('RXaMvMqk')
    select('RXaMvMqk')
    # set_multi_team('Pr9md2QV')
    # run_sql("update license"
    #         " set expire_time=1658139957 where org_uuid='5QPKKejf' AND type=3 AND edition='enterprise-trial';")
