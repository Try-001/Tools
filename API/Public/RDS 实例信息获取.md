RDS 备份信息获取

```shell
from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.acs_exception.exceptions import ClientException
from aliyunsdkcore.acs_exception.exceptions import ServerException
from aliyunsdkrds.request.v20140815.DescribeDBInstancesRequest import DescribeDBInstancesRequest
import json
# class RdsAPI:
def get_DBInstances():
    client = AcsClient('LTAIuW6MzJzqo9VK', 'S5U2HuoUYnnSF0ItGKsvz2PHTOpXkN', 'cn-shanghai')
    request = DescribeDBInstancesRequest()
    request.set_accept_format('json')
    response = client.do_action_with_exception(request)
    a = json.loads(response)
    a_result = a['Items']['DBInstance']
    return a_result
def solve_DBInstances():
    instance_result = []
    # b = get_DBInstances()
    for i in get_DBInstances():
        result = {
            'ZoneId':i['ZoneId'],
             'DBInstanceId':i['DBInstanceId'],
            'Engine':i['Engine'],
             'EngineVersion':i['EngineVersion'],
             'DBInstanceType':i['DBInstanceType'],
            'PayType':i['PayType']
         }
        instance_result.append(result)
    return json.dumps(instance_result, indent=2)
print (solve_DBInstances())
```

