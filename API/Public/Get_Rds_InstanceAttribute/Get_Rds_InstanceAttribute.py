# -*- coding:utf8 -*-
import json
from aliyunsdkcore import client
from aliyunsdkcore.request import CommonRequest
from aliyunsdkrds.request.v20140815 import DescribeBackupPolicyRequest, DescribeDBInstancesRequest, \
    DescribeRegionsRequest, DescribeDBInstanceAttributeRequest, DescribeSlowLogsRequest, DescribeDatabasesRequest
# from rds_api import AliyunRDSAPI

class AliyunRDSAPI:
    def __init__(self, access_id, access_secret, region):
        self.clt = client.AcsClient(str(access_id), str(access_secret), str(region))

    def get_DescribeDBInstances(self):
        '获取某地域所有RDS'
        request = DescribeDBInstancesRequest.DescribeDBInstancesRequest()
        request.set_accept_format('json')
        request.set_action_name('DescribeDBInstances')
        return self.clt.do_action_with_exception(request)
    def get_DescribeDBInstanceAttribute(self, DBInstanceId):
        '获取RDS基本属性'
        request = DescribeDBInstanceAttributeRequest.DescribeDBInstanceAttributeRequest()
        request.set_accept_format('json')
        request.set_action_name('DescribeDBInstanceAttribute')
        request.set_DBInstanceId(str(DBInstanceId))
        return self.clt.do_action_with_exception(request)
    def get_DescribeDatabasesRequest(self, DBInstanceId):
        """
        获取RDS数据库明细
        :return:
        """
        request = DescribeDatabasesRequest.DescribeDatabasesRequest()
        request.set_accept_format('json')
        request.set_action_name('DescribeDatabases')
        request.set_DBInstanceId(str(DBInstanceId))
        return self.clt.do_action_with_exception(request)


def mymap(func,*iterable):
    return list(map(func,*iterable))
# 获取RDS实例ID
def get_rdsinstance(**kwargs):
    cli = AliyunRDSAPI(kwargs['access_id'],kwargs['access_secret'],kwargs['region'])
    response = json.loads(cli.get_DescribeDBInstances())
    Instances = mymap(lambda x:x['DBInstanceId'],response['Items']['DBInstance'])
    # print (Instance)
    a_result= []
    # 获取实例详细信息
    for instance in Instances:
        response = json.loads(cli.get_DescribeDBInstanceAttribute(instance))
        response1 = json.loads(cli.get_DescribeDatabasesRequest(instance))
        databases = mymap(lambda x:x['DBName'],response1['Databases']['Database'])
        a_result.append(mymap(lambda x:
                              {'DBInstanceId' : x['DBInstanceId'],
                               'DB_Server' : x['ConnectionString'] + ':' + x['Port'],
                               'DBInstanceDescription' : x['DBInstanceDescription'],
                               'DBName' : databases,
                               'RegionId' : x['RegionId'],
                               'DBInstanceType' : x['DBInstanceType'],
                              # 'DBInstanceDescription' : x['DBInstanceDescription']
                               },
                              response['Items']['DBInstanceAttribute'])[0])

    f = open('out.txt',mode='a',encoding='utf-8')
    f.write(json.dumps(a_result,indent=2,ensure_ascii=False))
    f.close()


if __name__ == "__main__":
    params = {'access_id' : '',
          'access_secret' : '',
          'region' : 'cn-shenzhen'
          }
    get_rdsinstance(**params)