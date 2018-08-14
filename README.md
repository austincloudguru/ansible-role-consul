consul
===================
[![Build Status](https://travis-ci.org/AustinCloudGuru/ansible-role-consul.svg?branch=master)](https://travis-ci.org/AustinCloudGuru/ansible-role-consul)

This role installs consul as either a server or a client in AWS.

Requirements
------------

None.

Role Variables
--------------

### Default
For most people, the default variables that are set should be fine, but there are use cases for changing them. They are:

    consul_group:       # Default group name (consul)
    consul_gid:         # Default gid (10010)
    consul_user:        # Default username (consul)
    consul_uid:         # Default uid (10010)
    consul_version:     # Default consul version (1.2.2)


### Playbook Variables
Within your playbook, you should set the following variables:

    consul_role:          # Set to client or server
    consul_datacenter:    # name for the cluster
    consul_encryptkey:    # key generated by consul keygen
    consul_cert:          # SSL Certificate for the cluster
    consul_key:           # SSL Key for the cluster
    ca_cert:              # Intermediate SSL Cert for the cluster

Dependencies
------------

This role is written to run in AWS using the AWS provider for the retry_join configuration parameter using the role: consul parameter.

    "retry_join": ["provider=aws tag_key=role tag_value=consul"]

If you want to run it outside of AWS, you will need to update the retry_join value to use a different method.

Example Playbook
----------------

You should define the required variables in your playbook and call the role:

    - name: Converge
      hosts: all
      vars:
        consul_role: server
        consul_datacenter: "us-east-1"
        consul_encryptkey: "YKbtX0Gc3mnJ7QwaNwNYtg=="
        consul_cert: |
          -----BEGIN CERTIFICATE-----
          MIID0DCCArigAwIBAgIBCjANBgkqhkiG9w0BAQUFADBkMQswCQYDVQQGEwJVUzEO
          MAwGA1UECAwFVGV4YXMxDzANBgNVBAcMBkF1c3RpbjEbMBkGA1UECgwSTWFjbWls
          bGFuIExlYXJuaW5nMRcwFQYDVQQLDA5Db25zdWwgQ0EgQ2VydDAeFw0xNzEwMDUw
          MjE3MjZaFw0xODEwMDUwMjE3MjZaMGkxHzAdBgNVBAMMFmNvbnN1bC5tYWNtaWxs
          YW4uY2xvdWQxDjAMBgNVBAgMBVRleGFzMQswCQYDVQQGEwJVUzEbMBkGA1UECgwS
          TWFjbWlsbGFuIExlYXJuaW5nMQwwCgYDVQQLDANTUkUwggEiMA0GCSqGSIb3DQEB
          AQUAA4IBDwAwggEKAoIBAQDHa1FiN4520HHaCO7PyMy+DTJYciDxF7zdtLzujSkB
          BKMF2xKyKRZE8QbQjP5zgvOzkGxpFlTaMudAYrNEGJTZctlBqOZxVOi1zwHUKWfG
          rImcBYiY+W22DgD+IXF6qyD88peXjzggyMBt+7wuqrto/Y7A+PrNN1ZICNlaCeh9
          MGJgnS3Vjc7oMfZMix+Q/nmu12Nunqd/qS0mXBvWFb3WQehG5az3t/Z1QTTh6eYv
          1TabdV5QKRbZuOLIn3l9Di29b/7xOCZzhjqIr9X2ERuB97XOXCFoG3NaT0l2uWf/
          TzHFxqQe+hZVV2YpjSUPtRv62cIKX1JylI9wIPN6jwJZAgMBAAGjgYcwgYQwCQYD
          VR0TBAIwADAdBgNVHQ4EFgQUJYbDAwcNvH+YYWcqoNg26nezGGUwCwYDVR0PBAQD
          AgWgMB0GA1UdJQQWMBQGCCsGAQUFBwMBBggrBgEFBQcDAjAsBgNVHR8EJTAjMCGg
          H6AdhhtodHRwOi8vcGF0aC50by5jcmwvZGVtby5jcmwwDQYJKoZIhvcNAQEFBQAD
          ggEBACBvIpqeepCaWwiWy+5yPLMUOyC+VqiXgok6kLdX1CiiUkGF5KLWXU1GuWEq
          18oW5AdMvYuxOf4yYQYOIHYdYl6jCGdekHXTD1BDuWc8hvCucfQjLBsWJVwkjEEV
          +mZyi6dxnmxaGkhKlC8T35XeJeJfacARBMHgFS/UWCDKzFc+Wkbos1ZyiaHoxhHW
          TowkYnFqhErc4msOYYSRGhM3ryC05CPwVRymagTzmRoxnb6yqRh240CzYRyr3gex
          jgTb7gAnrK95CKUZqCA33Ff3EsqvNUPX5DneplhRdqb9ehAFcYgq1tU/E957Bkme
          rkt6x7V4L2FK+ukkxgSPE/RpbGc=
          -----END CERTIFICATE-----
        consul_key: |
          -----BEGIN PRIVATE KEY-----
          MIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQDHa1FiN4520HHa
          CO7PyMy+DTJYciDxF7zdtLzujSkBBKMF2xKyKRZE8QbQjP5zgvOzkGxpFlTaMudA
          YrNEGJTZctlBqOZxVOi1zwHUKWfGrImcBYiY+W22DgD+IXF6qyD88peXjzggyMBt
          +7wuqrto/Y7A+PrNN1ZICNlaCeh9MGJgnS3Vjc7oMfZMix+Q/nmu12Nunqd/qS0m
          XBvWFb3WQehG5az3t/Z1QTTh6eYv1TabdV5QKRbZuOLIn3l9Di29b/7xOCZzhjqI
          r9X2ERuB97XOXCFoG3NaT0l2uWf/TzHFxqQe+hZVV2YpjSUPtRv62cIKX1JylI9w
          IPN6jwJZAgMBAAECggEBALd39dUd9fU8CzMk+smyHSRRMduLjOEjDMEREq2Ks4nb
          QT0W85l0Eaf19GYVAdk2Ro4StprsT768DGQBKprg3rk8X8N36COmkb8LJ8yRF4gC
          n0wrDyRmfth7A9DK5gOMw/nUG0H2IxaOe/P0IYrxyyBp/1ds+hmp6ri1Y3riGMJr
          DGc18YPR7ViY7zkLS0gYDe90QI0vAG8ZfTsOmPYFJk0DSe4Tl+19udpGvXSFxfg2
          QtkfYnCMAAxgcwlOCbuZ2u4WLCvTG+ChmEJsT/NnHgjAZXxiG4hcJcuk3S2Jcj+f
          0XTGCpgDUneh112hIh2qq4BQdzQ/68/QEx7cYBDaQj0CgYEA6eW5L9BxDyunyuLm
          EVksDFWZTTg3CqV7OCDy6pCKp50zgFfX+u9H7o4MqU3D9DoEg2aZA6gCXVc9/QYw
          Jhcc7nrZLjWIPXiSmCl2vLOkAG/bF1euejhhLGmtg6ED3apcgaFqBaHsyO123uJY
          VV2sgAGMTCuuBTRWF/Ab+uS58bMCgYEA2kOGJPr4sn7x4Me99cCNUXohL4Yp8KE6
          D3qE4RMTzd6hkuh8vn1gbiz+vDaPv4mJv5O8eW49tXY7q/ITmpFU9Q+XrRkmCJQc
          xJjjD3Pxz3MTSjyL80k4ghFXy30N6twOqt/vO7OQZLT1Rfv/m76qb9juzF3KMc3A
          kzrH/Bu6/cMCgYEAuhdp5V7j9Pv4vfUUswzNfOrF06g8Mp5CkP+2BWYGyyDJjv1U
          +3NROb2O2Uzj8PYQDTOd3kjXyMfWq+82c7fD7wGSta8lvDKn/6RNsgkDHM3h9Ipw
          aRFeTuWthaKf3sbiXsi7/8s7BwnXn7FaMmEbE6UnqJrAE6f2L4l72XwNbP0CgYAm
          y7PPZPDJwXi67KYeRZCY9+1oJh/UTsQkNjHiU+LESBtOIpbxwRVf4A2TZNteP1NF
          wzvQFcFQPOjUYl4LrmN8f74FHaA+DB2k8EwD1icYKas3GdYCc3Rg4jZJzDuqEF1n
          EBDU+tDipaunOeiwRU7EPLoNh2pGOf1N7jfX3xH4wwKBgCkt/CO9mr8aC5X+8hAs
          j7lBwtsV67nbB6DhRlVMwwLj75EGf2qDVfDl7fGkjudhf9fN5YxlBU2lUACp+GPC
          VhfycE+bg0JxDMvMEhI2y8SQ44RZZ49i8QJQWL1adTQi/smi3tF85g+tH4aXsJfE
          ZazHZyqVNJx0P4AAkdhIJznE
          -----END PRIVATE KEY-----
        ca_cert: |
          -----BEGIN CERTIFICATE-----
          MIIDRDCCAiwCCQDEav6U/66tTzANBgkqhkiG9w0BAQsFADBkMQswCQYDVQQGEwJV
          UzEOMAwGA1UECAwFVGV4YXMxDzANBgNVBAcMBkF1c3RpbjEbMBkGA1UECgwSTWFj
          bWlsbGFuIExlYXJuaW5nMRcwFQYDVQQLDA5Db25zdWwgQ0EgQ2VydDAeFw0xNzEw
          MDUwMjE0NDNaFw0yNzEwMDMwMjE0NDNaMGQxCzAJBgNVBAYTAlVTMQ4wDAYDVQQI
          DAVUZXhhczEPMA0GA1UEBwwGQXVzdGluMRswGQYDVQQKDBJNYWNtaWxsYW4gTGVh
          cm5pbmcxFzAVBgNVBAsMDkNvbnN1bCBDQSBDZXJ0MIIBIjANBgkqhkiG9w0BAQEF
          AAOCAQ8AMIIBCgKCAQEAwWEC0XIjruB/Vv2w7VLaGGlcX04DrmBV+lZpG6IigAdi
          QfuA00RtsjVxi4VCYARR66W2bKrTrKFpuRrOCt+OzcCu1T0Z0+VfxDiJmCfNfUxt
          IFG3+42DJmGhfLWFp06fBxEWzvwDFbbND3F8mAJXSMIs5HrPnSFIdWR5eC2t/vBb
          T4IB1ntt4QulE+sKrxxfeDDeoeVuj5LG9pmM4VrAnaRbcfp4UDGAbv9W0TbSsqWc
          oe0bp/5+d1i7Z/fes20k1kzjI7N3M3RUPf7hI3TV24ljGxHCGaqR/3Ozv0bhmm28
          Mr1ScEwBY1BsDkuvGwZlkmU4sjZGrYQwv8DFHExAIQIDAQABMA0GCSqGSIb3DQEB
          CwUAA4IBAQB4wyRZSwvs9qgHUb8fl83pSQAnFNg3qffqNN2wBQbNUcCFUtx/XL6d
          J0i/AEvBmy9SXnTTSuN4udDkdxpznWtHtagIvC7CA70zRxF0PPdhOCBqInrAX0l3
          vFSBXIONfI1wMxdUCkP/A3EZEAIsON0zhVpUhbwaNkiEeuMahG3VFv2VFt/ANE1L
          QCulz7aUoUEXfXjDmpidVD/wzqBjUbJc0FEqTniaBDBNaN7bEogNZlRU/vGhZ2O1
          KBn9wSWwYRXmLICv7s6GrsYMoOFit4FrXQdj42hzqpGugXbAlOTknV6KZbwptSuG
          lEhOBOqUfdiXqUszPbSsRtFpmA+hA0vT
          -----END CERTIFICATE-----
      roles:
        - role: austincloudguru.consul


License
-------

MIT

Author Information
------------------

Mark Honomichl aka [AustinCloudGuru](https://austincloud.guru)
Created in 2018
