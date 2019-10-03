# DCS python client

(c) Crown copyright; not open source

A client to check passport validity using the [Document Checking Service (DCS) API](https://dcs-pilot-docs.cloudapps.digital/message-flow/#message-flow).

This client is currently missing:

- [ ] documentation, including guidance on creating the necessary keys and certificates
- [ ] error handling
- [ ] the ability to handle non-error responses; such responses are simply printed to stdout
- [ ] tests - both unit and integration
- [ ] a stub DCS to give non-government users something to run this client again
- [ ] the ability to send in custom passport data
- [ ] publication to pypi.org

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
