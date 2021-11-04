# Webhook Listener
A Python Lambda Webhook Listener - Generates a permanent URL on created assets.
See doc on Generating a Permanent URL: https://www.contentstack.com/docs/developers/apis/content-management-api/#generate-permanent-asset-url

**Not officially supported by Contentstack**

Note: This can only be executed once on every asset. The permanent URL cannot be changed after generating it.

Python 3.9.

Step by step:
1. Create a Lambda function and an API Gateway in AWS Lambda. Based on these documentation articles:
   * [TUTORIAL: Build an API Gateway API with Lambda Non-Proxy Integration](https://docs.aws.amazon.com/apigateway/latest/developerguide/getting-started-lambda-non-proxy-integration.html).
   * [AWS Lambda Deployment Package in Python](https://docs.aws.amazon.com/lambda/latest/dg/python-package.html)
   * (Optional) Create tests in Lambda, using the`testLambda.py` script - Note: You will need to change the asset uid to make it work on a asset on your stack.

 2. Environmental variables needed:
  * `CS_APIKEY` -> API Key of the Stack.
  * `CS_MANAGEMENTTOKEN` -> Management Token on the stack with write access
  * `CS_REGION` -> Either NA (North America Region) or EU (Europe Region)
  * `CS_SECRET` -> Defined secret - Used as a custom header in the webhook settings in Contentstack.
    * Note: The header value in Contentstack (`secret`) needs to match the value of this environmental variable.

You can define those environmental variables in your OS and run `testLambda.py`. You will need to define them in the Lambda configuration for it to work in a real world scenario.

3. It's good to update both code and configuration in Lambda with `awscli`.
   * To update code via `awscli`:
    * install pip module into a subdirectory like this:
      * `pip install --target ./package requests`.
    * Add all files and folders from the `package` folder (not the `package` folder itself) into a zip file with the `lambda_function.py`, along with the `config` and `cma` folders. Finally upload the zip file to Lambda like this:
      * `aws lambda update-function-code --function-name <Name of your Lambda function> --zip-file fileb://function.zip`

4. Define a webhook in Contentstack.
   * Give it a descriptive name
   * The URL should be the URL generated by the API Gateway in step 1.
   * Leave authentication information empty
   * Define a custom header `secret` - Give it the same value as the `CS_SECRET` variable in step 2.
   * Define the condition for the webhook: When `Any` -> `Asset` is `Created`.
   * Make sure the webhook is not set to concise and is enabled (The two checkmarks at the bottom).
