#!/usr/bin/env python3
"""
Check you have correctly constructed the JOSE object for the Document Checking Service (DCS)

Usage: check_jose --server-encryption-key <PATH> --server-encryption-certificate <PATH> --client-signing-certificate <PATH> --jose <JOSE> [--payload <PAYLOAD>]

Options:
    -h --help                               Show this screen.
    --jose <JOSE>                           The string that is output by your encryption implementation
    --server-encryption-key <PATH>          The path to the key the DCS will use to decrypt your requests
    --server-encryption-certificate <PATH>  The path to the certificate used to encrypt your requests
    --client-signing-certificate <PATH>     The path to the certificate you used to sign the JWS
    --payload                               The expected payload. Provide this if you wish to check that the JOSE object contains the expected payload.
"""

from docopt import docopt
from check_encryption import check_jwe
from check_signing import check_jws


def main():
    arguments = docopt(__doc__)

    print("\n**Verifying outer signature**\n")
    outer_jws_payload = check_jws(
        arguments["--client-signing-certificate"], arguments["--jose"]
    )

    print("\n**Decrypting**\n")
    jwe_payload = check_jwe(
        arguments["--server-encryption-key"],
        arguments["--server-encryption-certificate"],
        outer_jws_payload,
    )

    print("\n**Verifying inner signature**\n")
    check_jws(
        arguments["--client-signing-certificate"], jwe_payload, arguments["<PAYLOAD>"],
    )


if __name__ == "__main__":
    main()
