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

#2021-07-05,written for KT Cloud Autoscaling Service

import common as c
import base64 #2021-05-04 추가 

def listAutoScalingGroups(**kargs):
    """ list up watch metrics 
    * Args:
        - dimensions_member(list,optional): dimensions_member=['name','i-2901-32012-VM']
    * Examples : print(watch.listMetrics(zone='KR-M'))
    * Ref :  https://cloud.kt.com/portal/openapi-guide/computing_enterprise-Server-server_api_make
    """
    my_apikey, my_secretkey = c.read_config()

    kargs['command'] = 'listAutoScalingGroups'
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
    baseurl = c.geturl(ctype='as', m2=M2Bool)

    #return c.makerequest(kargs, baseurl, my_secretkey)
    return c.makerequest_debug(kargs, baseurl, my_secretkey)

def listMetricCollectionTypes(**kargs):
    
    my_apikey, my_secretkey = c.read_config()

    kargs['command'] = 'listMetricCollectionTypes'
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
    baseurl = c.geturl(ctype='as', m2=M2Bool)

    #return c.makerequest(kargs, baseurl, my_secretkey)
    return c.makerequest_debug(kargs, baseurl, my_secretkey)

def createLaunchConfiguration(**kargs):
    
    my_apikey, my_secretkey = c.read_config()

    kargs['command'] = 'createLaunchConfiguration'
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
    baseurl = c.geturl(ctype='as', m2=M2Bool)

    if 'userdata' in kargs:
        kargs['userdata'] = base64.b64encode(kargs['userdata'].encode('UTF-8'))
    
    if not 'LaunchConfigurationName' in kargs:
            return '[ktcloud] Missing required argument \"LaunchConfigurationName\"'
    
    if 'productcode' in kargs:
        if 'serviceofferingid' in kargs:
            return '[ktcloud] Not required argument \"serviceofferingid\"'
        if 'templateid' in kargs:
            return '[ktcloud] Not required argument \"templateid\"'
        if 'diskofferingid' in kargs:
            return '[ktcloud] Not required argument \"diskofferingid\"'
    else:
        if not 'serviceofferingid' in kargs:
            return '[ktcloud] Missing required argument \"serviceofferingid\"'
        if not 'templateid' in kargs:
            return '[ktcloud] Missing required argument \"templateid\"'
#         if not 'diskofferingid' in kargs:
#             return '[ktcloud] Missing required argument "diskofferingid"'
    #return c.makerequest(kargs, baseurl, my_secretkey)
    return c.makerequest_debug(kargs, baseurl, my_secretkey)

def createAutoScalingGroup(**kargs):
    """ query for createAutoScalingGroup 
    * Args:
        - AutoScalingGroupName(String, Required) : astest0714
        - AvailabilityZones_member(list, Required) : AvailabilityZones_member = [zoneid] -> zone name 입력 받아서 처리 
        - LaunchConfigurationName(String, Required) : launch0713
        - MaxSize(String, Required) : 3
        - MinSize(String, Required) : 1
        - LoadBalancers_member(list,optional):tuple list 형식으로 전달: LoadBalancers_member=[('LoadBalancerId','LoadBalancerType','IpAddressId','PublicPortRangeFrom','PublicPortRangeTo','PrivatePort')]
        
    
    """
    my_apikey, my_secretkey = c.read_config()

    kargs['command'] = 'createAutoScalingGroup'
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
    baseurl = c.geturl(ctype='as', m2=M2Bool)

    kargs['AvailabilityZones.member.1'] = c.getzoneidbyhname(ZoneName)
    
    if not 'AutoScalingGroupName' in kargs:
            return '[ktcloud] Missing required argument \"AutoScalingGroupName\"'
    if not 'LaunchConfigurationName' in kargs:
            return '[ktcloud] Missing required argument \"LaunchConfigurationName\"'
#     if not 'AvailabilityZones_member' in kargs:
#             return '[ktcloud] Missing required argument \"AvailabilityZones_member\"'
    if not 'MaxSize' in kargs:
            return '[ktcloud] Missing required argument \"MaxSize\"' 
    if not 'MinSize' in kargs:
            return '[ktcloud] Missing required argument \"MinSize\"' 
    
    #AvailabilityZones_member 관련 argument를 위한 처리 -> Python의 변수명 규격 이슈(statistics.member.1과 같이 변수명 생성 안됨)
#     az_member = kargs["AvailabilityZones_member"]
#     del kargs["AvailabilityZones_member"]
#     for index in range(0,len(az_member)):
#         temp_arg = "AvailabilityZones.member."
#         temp_arg += str(index+1)
#         kargs[temp_arg] = az_member[index]
    
    #LoadBalancers_member 관련 argument를 위한 처리 -> Python의 변수명 규격 이슈(statistics.member.1과 같이 변수명 생성 안됨)
    if kargs.get("LoadBalancers_member"):
        lb_member = kargs["LoadBalancers_member"]
        lb_member_name = ['LoadBalancerId','LoadBalancerType','IpAddressId','PublicPortRangeFrom','PublicPortRangeTo','PrivatePort']
        del kargs["LoadBalancers_member"]
        for d_index in range(0,len(lb_member)):
            for n_index in range(0,len(lb_member[d_index])):
                temp_arg = "LoadBalancers.member."
                temp_arg  += (str(d_index+1) + '.' + lb_member_name[n_index])
                kargs[temp_arg] = lb_member[d_index][n_index]
                #print(kargs)
            
            
    #return c.makerequest(kargs, baseurl, my_secretkey)
    return c.makerequest_debug(kargs, baseurl, my_secretkey)


def listScalingActivities(**kargs):
    
    my_apikey, my_secretkey = c.read_config()

    kargs['command'] = 'listScalingActivities'
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
    baseurl = c.geturl(ctype='as', m2=M2Bool)

    #return c.makerequest(kargs, baseurl, my_secretkey)
    return c.makerequest_debug(kargs, baseurl, my_secretkey)

def setDesiredCapacity(**kargs):
    
    my_apikey, my_secretkey = c.read_config()

    kargs['command'] = 'setDesiredCapacity'
    kargs['response'] = 'json'
    kargs['apikey'] = my_apikey

    if not 'zone' in kargs:
        return 'Missing required argument \"zone\" \n \
  - KR-CA : KOREA-Central A Zone \n \
  - KR-CB : KOREA-Central B Zone \n \
  - KR-M  : KOREA M Zone  \n \
  - KR-M2 : KOREA M2 Zone '
    
    if not 'AutoScalingGroupName' in kargs:
            return '[ktcloud] Missing required argument \"AutoScalingGroupName\"'
    if not 'DesiredCapacity' in kargs:
            return '[ktcloud] Missing required argument \"DesiredCapacity\"'
    
    ZoneName = kargs['zone']
    del kargs['zone']
    M2Bool = c.IsM2(ZoneName)
    baseurl = c.geturl(ctype='as', m2=M2Bool)

    #return c.makerequest(kargs, baseurl, my_secretkey)
    return c.makerequest_debug(kargs, baseurl, my_secretkey)


def putScheduledUpdateGroupAction(**kargs):
    
    my_apikey, my_secretkey = c.read_config()

    kargs['command'] = 'putScheduledUpdateGroupAction'
    kargs['response'] = 'json'
    kargs['apikey'] = my_apikey

    if not 'zone' in kargs:
        return 'Missing required argument \"zone\" \n \
  - KR-CA : KOREA-Central A Zone \n \
  - KR-CB : KOREA-Central B Zone \n \
  - KR-M  : KOREA M Zone  \n \
  - KR-M2 : KOREA M2 Zone '
    
    if not 'AutoScalingGroupName' in kargs:
            return '[ktcloud] Missing required argument \"AutoScalingGroupName\"'
    if not 'ScheduledActionName' in kargs:
            return '[ktcloud] Missing required argument \"ScheduledActionName\"'
    
    ZoneName = kargs['zone']
    del kargs['zone']
    M2Bool = c.IsM2(ZoneName)
    baseurl = c.geturl(ctype='as', m2=M2Bool)

    #return c.makerequest(kargs, baseurl, my_secretkey)
    return c.makerequest_debug(kargs, baseurl, my_secretkey)



# End Of File

