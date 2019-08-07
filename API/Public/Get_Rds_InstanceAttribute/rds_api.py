# -*- coding:utf8 -*-
from aliyunsdkcore import client
from aliyunsdkcore.request import CommonRequest
from aliyunsdkrds.request.v20140815 import DescribeBackupPolicyRequest, DescribeDBInstancesRequest, \
    DescribeRegionsRequest, DescribeDBInstanceAttributeRequest, DescribeSlowLogsRequest, DescribeDatabasesRequest


class AliyunRDSAPI:
    def __init__(self, access_id, access_secret, region):
        self.clt = client.AcsClient(str(access_id), str(access_secret), str(region))

    def get_DescribeRegions(self):
        '获取所有region'
        request = DescribeRegionsRequest.DescribeRegionsRequest()
        request.set_accept_format('json')
        request.set_action_name('DescribeRegions')
        return self.clt.do_action_with_exception(request)

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

    def get_DescribeSlowLogsRequest(self, **kwargs):
        '获取RDS慢查询'
        request = DescribeSlowLogsRequest.DescribeSlowLogsRequest()
        request.set_accept_format('json')
        request.set_action_name('DescribeSlowLogs')
        request.set_DBInstanceId(kwargs['DBInstanceId'])
        request.set_DBName(kwargs['DBName'])
        request.set_StartTime(kwargs['StartTime'])
        request.set_EndTime(kwargs['EndTime'])
        """
        排序依据，取值如下：
        TotalExecutionCounts：总执行次数最多；
        TotalQueryTimes：总执行时间最多
        TotalLogicalReads：总逻辑读最多；
        TotalPhysicalReads：总物理读最多。此参数对SQL Server实例有效，SQL Server类型必传此参数。
        """
        request.set_SortKey(kwargs['SortKey'])
        request.set_PageSize(100)
        request.set_PageNumber(1)
        return self.clt.do_action_with_exception(request)

    def get_DescribeSlowLogs(self, db):
        request = CommonRequest()
        request.set_accept_format('json')
        request.set_action_name("DescribeSlowLogs")
        request.set_DBInstanceId(db)
        return self.clt.do_action_with_exception(request)

    def get_DescribeSlowLogRecordsRequest(self, **kwargs):
        '用户可以查询某日期范围内、某个用户实例下、某个数据库的慢查询明细，目前支持MySQL、PostgreSQL和PPAS类型的实例。'
        request = DescribeSlowLogsRequest.DescribeSlowLogsRequest()
        request.set_accept_format('json')
        request.set_action_name('DescribeSlowLogRecords')
        request.set_DBInstanceId(kwargs['DBInstanceId'])
        request.set_DBName(kwargs['DBName'])
        request.set_StartTime(kwargs['StartTime'])
        request.set_EndTime(kwargs['EndTime'])
        # request.set_PageSize(100)
        # request.set_PageNumber(1)
        return self.clt.do_action_with_exception(request)

    def get_DescribeBackupPolicyRequest(self, **kwargs):
        """
        查看系统设置的备份策略
        :param db:
        :return:
        """
        request = DescribeBackupPolicyRequest.DescribeBackupPolicyRequest()
        request.set_accept_format('json')
        request.set_action_name('DescribeBackupPolicy')
        request.set_DBInstanceId(kwargs['DBInstanceId'])
        request.add_query_param('BackupPolicyMode', kwargs['BackupPolicyMode'])
        return self.clt.do_action_with_exception(request)


if __name__ == '__main__':
    print("This is aliyun's RDS For MySQL API")
