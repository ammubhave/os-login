import os
import logging
import sys
import ssl

keyfile = '/tmp/ssl_private.key'
with open(keyfile, 'w') as keyf:
    keyf.write(os.environ.get('SSL_PRIVATE_KEY', ''))

certfile = '/tmp/ssl_certificate.crt'
with open(certfile, 'w') as certf:
    certf.write(os.environ.get('SSL_CERTIFICATE', ''))

ca_certs = 'conf/mitca.pem'

cert_reqs = ssl.CERT_OPTIONAL
