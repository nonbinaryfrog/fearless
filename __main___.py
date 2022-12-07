import pulumi
import pulumi_aws as aws
import json 
from datetime import datetime
import ssl
import OpenSSL

def get_cert(host, port=443):
    #get cert on default port 443
    cert = ssl.get_server_certificate((host,port))
    #load certificate into x509
    x509 = OpenSSL.crypto.load_certificate(OpenSSL.crypto.FILETYPE_PEM, cert)
    return x509

def sslchecker(host):
    #take host and check if ssl cert is up to date
    context = get_cert(host)
    #check cert expiration
    certexpiration = datetime.strptime(context.get_notAfter().decode('utf-8', '%Y%m%D%H%M%SZ'))
    if datetime.utcnow() < certexpiration:
        return "SSL certificate is up to date"
    else:
        return "SSL certificate is expired"

if __name__ == "__main__":
   host = "google.com"
   print("Checking {}".format(host))
   print(sslchecker(host))