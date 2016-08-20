import os
import ssl

keyfile = '/tmp/ssl_private_key'
with open(keyfile, 'w') as keyf:
    print(os.environ.get('SSL_PRIVATE_KEY'))
    keyf.write(os.environ.get('SSL_PRIVATE_KEY', ''))

certfile = '/tmp/ssl_certificate'
with open(certfile, 'w') as certf:
    print(os.environ.get('SSL_CERTIFICATE'))
    certf.write(os.environ.get('SSL_CERTIFICATE', ''))

cert_reqs = ssl.CERT_OPTIONAL
