# DCS python client

This is a worked example of a client for the [Document Checking Service (DCS) API](https://dcs-pilot-docs.cloudapps.digital/message-flow/#message-flow). It serves as an example of how to create a request for the DCS and how to decrypt the response.

You should not attempt to use this as a client library, since it is currently missing:

- [ ] documentation, including guidance on creating the necessary keys and certificates
- [ ] handling responses; currently, decrypted responses are just printed to stdout
- [ ] error handling
- [ ] tests
- [ ] a stub DCS to give non-government users something to run this client against
- [ ] the ability to send in custom passport data
- [ ] publication to pypi.org

This client does not support checking the validity of driving licences. This functionality is currently available only to identity providers for GOV.UK Verify - not to participants in [the DCS pilot](https://www.gov.uk/guidance/apply-for-the-document-checking-service-pilot-scheme).

## Installation

Run `pip3 install .`

## Usage

```
Make a test passport request to the Document Checking Service (DCS)

Usage: client.py [--url <url>] --client-signing-certificate <PATH> --client-signing-key <PATH> --server-encryption-certificate <PATH> --client-encryption-key <PATH> --server-signing-certificate <PATH> [--client-ssl-certificate <PATH> --client-ssl-key <PATH> --server-ssl-ca-bundle <PATH>]

Options:
    -h --help                               Show this screen.
    --url <url>                             The DCS passport endpoint [default: http://127.0.0.1:52110/checks/passport]
    --client-signing-certificate <PATH>     The certificate with which the client signs requests
    --client-signing-key <PATH>             The key with which the client signs requests
    --server-encryption-certificate <PATH>  The server certificate for which the client encrypts requests
    --client-encryption-key <PATH>          The key with which the client decrypts responses
    --server-signing-certificate <PATH>     The certificate with which the server signs responses
    --client-ssl-certificate <PATH>         The client certificate used for mutual TLS
    --client-ssl-key <PATH>                 The client key used for mutual TLS
    --server-ssl-ca-bundle <PATH>           The server SSL CA bundle

This client is intended as an example of how to write a DCS client. It should not be used against a production DCS.
See https://dcs-pilot-docs.cloudapps.digital/message-structure for public documentation of the DCS API.
```

## Support and raising issues

If you think you have discovered a security issue in this code please email [disclosure@digital.cabinet-office.gov.uk](mailto:disclosure@digital.cabinet-office.gov.uk) with details.

For non-security related bugs and feature requests please [raise an issue](https://github.com/alphagov/dcs-python-client/issues/new) in the GitHub issue tracker.

## Code of Conduct
This project is developed under the [Alphagov Code of Conduct](https://github.com/alphagov/code-of-conduct)
