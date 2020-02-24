#!/usr/bin/env python3
"""
Check you are signing and encrypting correctly for the Document Checking Service (DCS)

Usage: check_jose --client-signing-certificate <PATH> --sha1-thumbprint <SHA1> --sha256-thumbprint <SHA256>

Options:
    -h --help                               Show this screen.
    --client-signing-certificate <PATH>
    --sha1-thumbprint <SHA1>
    --sha256-thumbprint <SHA256>
"""

from cryptography import x509
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from datetime import datetime
from docopt import docopt
from jwcrypto import jwk, jws, jwe
from jwcrypto.common import json_encode, json_decode
import base64
import requests
import urllib.parse
import uuid



def generate_thumbprints(path):
    """Generate the thumbprints needed for the `x5t` and `x5t256` headers"""
    with open(path, "rb") as f:
        cert = x509.load_pem_x509_certificate(f.read(), default_backend())

    sha1_thumbprint = (
        base64.urlsafe_b64encode(
            cert.fingerprint(hashes.SHA1())
        )  # The thumbprint is a URL-encoded hash...
        .decode("utf-8")  # ... as a Python string ...
        .strip("=")  # ... with the padding removed.
    )

    sha256_thumbprint = (
        base64.urlsafe_b64encode(
            cert.fingerprint(hashes.SHA256())
        )  # The thumbprint is a URL-encoded hash...
        .decode("utf-8")  # ... as a Python string ...
        .strip("=")  # ... with the padding removed.
    )

    return sha1_thumbprint, sha256_thumbprint

def main():
    arguments = docopt(__doc__)
    print(arguments)