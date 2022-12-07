# SSL Checker

Upon logging into AWS, navigate to AWS Lambda and then to Functions. Create a function named SSLchecker and under runtime, choose python 3.9. Then paste the code from __main__.py into the code.

Then navigate to API Gateway to create a REST API. Then create a resource titled 'SSLchecker'. Under that, create a method with 'ANY' selected in the dropdown. Under integration type, select Lambda Function. Select 'Use Lambda Proxy Integration'. In the searchbar below, type the name of the lambda function and click save. A pop-up will remind you that you are about to give API Gateway permission to invoke Lambda, which is fine.

Afterwards, deploy the API. To test, click on any of the methods underneath 'SSLChecker' and use the invoke URL to check the response.

## Future updates

In the future, steps should be taken to encrypt the SSL information when receieved as well as restrict access to certain methods if needed.
