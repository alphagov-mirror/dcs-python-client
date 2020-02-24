#!/usr/bin/env python3
"""
Check you are signing correctly for the Document Checking Service (DCS)

Usage: check_signing --client-signing-certificate <PATH> --client-signing-key <PATH> --jws <JWS> [--payload <PAYLOAD>]

Options:
    -h --help                               Show this screen.
    --jws <JWS>                             The string that is output by your signing implementation
    --client-signing-certificate <PATH>     The path to the certificate you used to sign the JWS
    --client-signing-key <PATH>             The path to the key you used to sign the JWS
    --payload                               The expected payload of the JWS object. Provide this if you wish to check that the JWS object contains the expected payload.
"""

from docopt import docopt
from jwcrypto import jws
import sys

from check_thumbprint import generate_thumbprints
from client import load_pem


def validate_signature(jws_string, key):
    jws_token = jws.JWS()
    try:
        jws_token.deserialize(raw_jws=jws_string, key=key)
    except jws.InvalidJWSSignature:
        print(
            "Signature validation failed. "
            "Check that the signing certificate provided matches the key used to sign the JWS"
        )
        sys.exit(1)
    except jws.InvalidJWSObject as e:
        print(e)
        sys.exit(1)

    print("Successfully validated signature")

    return jws_token


def check_headers(jws_token, cert_path):
    header_errors = {}

    alg_header = jws_token.jose_header.get("alg", "absent")
    if alg_header != "RS256":
        header_errors["alg"] = f"Expected 'RS256', was '{alg_header}'"

    expected_sha1, expected_sha256 = generate_thumbprints(cert_path)

    sha1_header = jws_token.jose_header.get("x5t", "absent")
    if sha1_header != expected_sha1:
        header_errors["x5t"] = f"Expected '{expected_sha1}', was '{sha1_header}'"

    sha2_header = jws_token.jose_header.get("x5t#S256", "absent")
    if sha2_header != expected_sha256:
        header_errors["x5t#S256"] = f"Expected '{expected_sha256}', was '{sha2_header}'"

    if header_errors:
        print("Header errors")
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


def check_jws(cert_path, user_jws, expected_payload=None):
    jws_token = validate_signature(user_jws, load_pem(cert_path))

    check_headers(jws_token, cert_path)

    check_payload(jws_token.payload.decode("utf-8"), expected_payload)


def main():
    arguments = docopt(__doc__)
    print("")
    check_jws(
        arguments["--client-signing-certificate"],
        arguments["--jws"],
        arguments["<PAYLOAD>"],
    )


if __name__ == "__main__":
    main()
