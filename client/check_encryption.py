#!/usr/bin/env python3
"""
Check you are encrypting correctly for the Document Checking Service (DCS)

Usage: check_encryption --server-encryption-key <PATH> --jwe <JWE> [--payload <PAYLOAD>]

Options:
    -h --help                               Show this screen.
    --jwe <JWE>                             The string that is output by your encryption implementation
    --server-encryption-key <PATH>          The path to the key the DCS will use to decrypt your requests
    --payload                               The expected payload of the JWS object. Provide this if you wish to check that the JWE contains the expected payload.
"""

from docopt import docopt
from jwcrypto import jwe
import sys

from client import load_pem


def decrypt(encrypted_jwe, key):
    jwe_token = jwe.JWE()
    try:
        jwe_token.deserialize(raw_jwe=encrypted_jwe, key=key)
    except jwe.InvalidJWEData as e:
        print(
            f"Decryption failed. Check that the encryption key matches the certificate used to encrypt the JWE\n\n{e}"
        )
        sys.exit(1)

    if encrypted_jwe.count(".") != 4:
        print("JWE not in compact form")
        print(encrypted_jwe.count("."))
        sys.exit(1)

    print("Successfully decrypted")

    return jwe_token


def check_headers(jwe_token):
    headers = jwe_token.jose_header
    header_errors = {}

    alg_header = headers.get("alg")
    if alg_header != "RSA-OAEP":
        header_errors["alg"] = f"Expected 'RSA-OAEP', was '{alg_header}'"

    if headers["enc"] != "A128CBC-HS256":
        header_errors["enc"] = f"Expected 'A128CBC-HS256', was '{alg_header}'"

    if header_errors:
        print("Header errors:")
        for (header, err) in header_errors.items():
            print(f"  {header} - {err}")
        sys.exit(1)

    print("All required headers are correct")


def check_payload(actual_payload, expected_payload=None):
    if expected_payload:
        if expected_payload == actual_payload:
            print("Supplied payload matches extracted payload.")
        else:
            print("Supplied payload did not match extracted payload.")
            print(f"  Expected: {expected_payload}")
            print(f"  Actual: {actual_payload}")
            sys.exit(1)
    else:
        print(f"Payload: '{actual_payload}'")


def check_jwe(cert_path, encrypted_jwe, expected_payload=None):
    jwe_token = decrypt(encrypted_jwe, load_pem(cert_path))

    check_headers(jwe_token)

    check_payload(jwe_token.payload.decode("utf-8"), expected_payload)

    return jwe_token.payload.decode("utf-8")


def main():
    arguments = docopt(__doc__)
    print("")

    check_jwe(
        arguments["--server-encryption-key"],
        arguments["--jwe"],
        arguments["<PAYLOAD>"],
    )


if __name__ == "__main__":
    main()
