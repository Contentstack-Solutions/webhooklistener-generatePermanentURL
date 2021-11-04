import os
import json
import cma

def defineVars():
    return os.environ['CS_REGION'], os.environ['CS_APIKEY'], os.environ['CS_MANAGEMENTTOKEN'], os.environ['CS_SECRET']

def returnStatement(code = 200, msg = 'OK'):
    return {
        'statusCode': code,
        'body': json.dumps(msg)
    }

def defineBody(body):
    '''
    If you want to change how the permanent URL looks like, you can do that here.
    '''
    domain = body['data']['asset']['url'].split('/')[2] # Either eu-images.contentstack.com or images.contentstack.io
    apiKey = body['api_key']
    assetUid = body['data']['asset']['uid']
    fileName = body['data']['asset']['filename']
    url = 'https://{domain}/v3/assets/{apiKey}/{assetUid}/{fileName}'.format(domain=domain, apiKey=apiKey, assetUid=assetUid, fileName=fileName)

    newBody = {
        'permanent_url': url
    }
    return newBody



    

def lambda_handler(event, context):
    body = json.loads(event['body'])
    try:
        triggerSecret = event['headers']['secret']
    except KeyError:
        returnStatement(403, 'Custom header "Secret" missing!')
    try:
        region, apiKey, managementToken, secretHeader = defineVars()
        region = cma.regionMap[region]
    except:
        return returnStatement(400, 'Error! Make sure environmental variables are defined.')

    if secretHeader != triggerSecret:
        # If the custom header secret is not identical to the variable set in Lambda - we exit
        return returnStatement(403, 'Incorrect secret')
    
    assetUid = body['data']['asset']['uid']

    updateBody = defineBody(body)

    result = cma.generateAssetPermanentURL(apiKey, managementToken, region, assetUid, updateBody)
    if result:
        msg = str(result['notice']) + ' uid: ' + str(result['asset']['uid'])
        return returnStatement(200, msg)
    else:
        return returnStatement(400, 'Updating asset with permanent URL did not work. Find more information in AWS Lambda logs.')
