import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))))
import database as db

# ref : https://cloud.kt.com/portal/openapi-guide/database-ucloudDB-Instance

# simple example
print(db.updateInstanceParameterGroup(
    instanceid='94699dfe-f3f9-4867-8fe7-14b5298792ce',
    parametergroupid='d83cdb0a-a5a3-44ce-874e-612bf9ed4620'
))
