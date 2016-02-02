# hpkp-pinfail

a webservice for accepting HTTP Public-Key-Pins Pin failure reports

## Requirements

1.  Use `virtualenv` and install flask in your environment.

```
virtualenv env
source env/bin/activate
pip install flask
```

## Installation

## Testing

A sample report that you can send with curl is included.

```sh
curl -d @samples/sample-json --header "Content-Type: application/json" \
-vX POST http://localhost:5000/hpkp
```

## Report Spec

```json
{
  "date-time": date-time,
  "hostname": hostname,
  "port": port,
  "effective-expiration-date": expiration-date,
  "include-subdomains": include-subdomains,
  "noted-hostname": noted-hostname,
  "served-certificate-chain": [
   pem1, ... pemN
  ],
  "validated-certificate-chain": [
   pem1, ... pemN
  ],
  "known-pins": [
   known-pin1, ... known-pinN
  ]
}
```

## Sample Report

```json
{
  "date-time": "2014-04-06T13:00:50Z",
  "hostname": "www.example.com",
  "port": 443,
  "effective-expiration-date": "2014-05-01T12:40:50Z"
  "include-subdomains": false,
  "served-certificate-chain": [
    "-----BEGIN CERTIFICATE-----\n
    MIIEBDCCAuygAwIBAgIDAjppMA0GCSqGSIb3DQEBBQUAMEIxCzAJBgNVBAYTAlVT\n
    ...
    HFa9llF7b1cq26KqltyMdMKVvvBulRP/F/A8rLIQjcxz++iPAsbw+zOzlTvjwsto\n
    WHPbqCRiOwY1nQ2pM714A5AuTHhdUDqB1O6gyHA43LL5Z/qHQF1hwFGPa4NrzQU6\n
    yuGnBXj8ytqU0CwIPX4WecigUCAkVDNx\n
    -----END CERTIFICATE-----",
    ...
  ],
  "validated-certificate-chain": [
    "-----BEGIN CERTIFICATE-----\n
    MIIEBDCCAuygAwIBAgIDAjppMA0GCSqGSIb3DQEBBQUAMEIxCzAJBgNVBAYTAlVT\n
    ...
    HFa9llF7b1cq26KqltyMdMKVvvBulRP/F/A8rLIQjcxz++iPAsbw+zOzlTvjwsto\n
    WHPbqCRiOwY1nQ2pM714A5AuTHhdUDqB1O6gyHA43LL5Z/qHQF1hwFGPa4NrzQU6\n
    yuGnBXj8ytqU0CwIPX4WecigUCAkVDNx\n
    -----END CERTIFICATE-----",
    ...
  ],
  "known-pins": [
    'pin-sha256="d6qzRu9zOECb90Uez27xWltNsj0e1Md7GkYYkVoZWmM="',
    "pin-sha256=\"E9CZ9INDbd+2eRQozYqqbQ2yXLVKB9+xcprMF+44U1g=\""
  ]
}
```

## TODOs

- [ ] finish rest of README
- [ ] accept/decode/validate JSON POSTed requests
  - [ ] log to sqlite
  - [ ] log to mysql
- [ ] log to couchdb
- [ ] nagios check_hpkp_pinfail util to check number of records and subtract previous to show growth and alarm

## Reference

* [IETF: Public Key Pinning Extension for HTTP](https://tools.ietf.org/html/draft-ietf-websec-key-pinning-21#section-3)

