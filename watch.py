#
#  kt cloud SDK v1.0
#
#  Copyright (c) 2020 kt corp. All rights reserved.
#
#  This is a proprietary software of kt corp
#  and you may not use this file except in compliance
#  with license agreement with kt corp.
#  Any redistribution or use of this software,
#  with or without modification shall be strictly
#  prohibited without prior written approval of kt corp,
#  and the copyright notice above does not evidence
#  any actual or intended publication of such software.
#

#2021-05-18,written for KT Cloud Watch Service

import common as c
import base64 #2021-05-04 추가 

def listMetrics(**kargs):
    """ list up watch metrics 
    * Args:
        - dimensions_member(list,optional):tuple list 형식으로 전달: dimensions_member=[('name','i-2901-32012-VM')]
    * Examples : print(watch.listMetrics(zone='KR-M'))
    * Ref :  https://cloud.kt.com/portal/openapi-guide/computing_enterprise-Server-server_api_make
    """
    my_apikey, my_secretkey = c.read_config()

    kargs['command'] = 'listMetrics'
    kargs['response'] = 'json'
    kargs['apikey'] = my_apikey

    if not 'zone' in kargs:
        return 'Missing required argument \"zone\" \n \
  - KR-CA : KOREA-Central A Zone \n \
  - KR-CB : KOREA-Central B Zone \n \
  - KR-M  : KOREA M Zone  \n \
  - KR-M2 : KOREA M2 Zone '
    ZoneName = kargs['zone']
    del kargs['zone']
    M2Bool = c.IsM2(ZoneName)
    baseurl = c.geturl(ctype='watch', m2=M2Bool)

    #dimension name 관련 argument를 위한 처리 -> Python의 변수명 규격 이슈(statistics.member.1과 같이 변수명 생성 안됨)
    if kargs.get("dimensions_member"):
        dimensions_member = kargs["dimensions_member"]
        del kargs["dimensions_member"]
        for d_index in range(0,len(dimensions_member)):
            temp_arg_name = "dimensions.member."
            temp_arg_name += (str(d_index+1)+'.name')

            temp_arg_value = "dimensions.member."
            temp_arg_value += (str(d_index+1)+'.value')

            kargs[temp_arg_name] = dimensions_member[d_index][0]
            kargs[temp_arg_value] = dimensions_member[d_index][1]
    
    #return c.makerequest(kargs, baseurl, my_secretkey)
    return c.makerequest_debug(kargs, baseurl, my_secretkey)

def listAlarms(**kargs):
    """ list up watch alarms 
    * Args:
        - 
    * Examples : print(watch.listMetrics(zone='KR-M'))
    * Ref :  https://cloud.kt.com/portal/openapi-guide/computing_enterprise-Server-server_api_make
    """
    my_apikey, my_secretkey = c.read_config()

    kargs['command'] = 'listAlarms'
    kargs['response'] = 'json'
    kargs['apikey'] = my_apikey

    if not 'zone' in kargs:
        return 'Missing required argument \"zone\" \n \
  - KR-CA : KOREA-Central A Zone \n \
  - KR-CB : KOREA-Central B Zone \n \
  - KR-M  : KOREA M Zone  \n \
  - KR-M2 : KOREA M2 Zone '
    ZoneName = kargs['zone']
    del kargs['zone']
    M2Bool = c.IsM2(ZoneName)
    baseurl = c.geturl(ctype='watch', m2=M2Bool)

    
    return c.makerequest(kargs, baseurl, my_secretkey)

def getMetricStatistics(**kargs):
    """ query for watch metric data 
    * Args:
        - namespace(String, Required) : ucloud/server
        - metricname(String, Required) : NetworkIn
        - starttime(String, Required) : 2021-05-17T12:00:00.000
        - endtime(String, Required) : 2021-05-18T12:00:00.000
        - period(String, Required) : 5
        - statistics_member(list, Required) : statistics_member=['Average', 'Sum', 'SampleCount', 'Maximum', 'Minimum']
        - unit(String, Required) : Bytes
        - dimensions_member(list,optional):tuple list 형식으로 전달: dimensions_member=[('name','i-2901-32012-VM')]
        
    * Examples : print(watch.listMetrics(zone='KR-M'))
    * Ref :  https://cloud.kt.com/portal/openapi-guide/computing_enterprise-Server-server_api_make
    """
    my_apikey, my_secretkey = c.read_config()

    kargs['command'] = 'getMetricStatistics'
    kargs['response'] = 'json'
    kargs['apikey'] = my_apikey

    if not 'zone' in kargs:
        return 'Missing required argument \"zone\" \n \
  - KR-CA : KOREA-Central A Zone \n \
  - KR-CB : KOREA-Central B Zone \n \
  - KR-M  : KOREA M Zone  \n \
  - KR-M2 : KOREA M2 Zone '
    ZoneName = kargs['zone']
    del kargs['zone']
    M2Bool = c.IsM2(ZoneName)
    baseurl = c.geturl(ctype='watch', m2=M2Bool)

    #metric name 관련 argument를 위한 처리 -> Python의 변수명 규격 이슈(statistics.member.1과 같이 변수명 생성 안됨)
    statistics_member = kargs["statistics_member"]
    del kargs["statistics_member"]
    for index in range(0,len(statistics_member)):
        temp_arg = "statistics.member."
        temp_arg += str(index+1)
        kargs[temp_arg] = statistics_member[index]
    
    #dimension name 관련 argument를 위한 처리 -> Python의 변수명 규격 이슈(statistics.member.1과 같이 변수명 생성 안됨)
    if kargs.get("dimensions_member"):
        dimensions_member = kargs["dimensions_member"]
        del kargs["dimensions_member"]
        for d_index in range(0,len(dimensions_member)):
            temp_arg_name = "dimensions.member."
            temp_arg_name += (str(d_index+1)+'.name')

            temp_arg_value = "dimensions.member."
            temp_arg_value += (str(d_index+1)+'.value')

            kargs[temp_arg_name] = dimensions_member[d_index][0]
            kargs[temp_arg_value] = dimensions_member[d_index][1]
    #return c.makerequest(kargs, baseurl, my_secretkey)
    return c.makerequest_debug(kargs, baseurl, my_secretkey)

# End Of File

