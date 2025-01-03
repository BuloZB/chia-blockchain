from __future__ import annotations

SSL_TEST_PRIVATE_CA_CRT = b"""-----BEGIN CERTIFICATE-----
MIIDKTCCAhGgAwIBAgIUZnoqyaLGQMl08azdwpafGGfEGR0wDQYJKoZIhvcNAQEL
BQAwRDENMAsGA1UECgwEQ2hpYTEQMA4GA1UEAwwHQ2hpYSBDQTEhMB8GA1UECwwY
T3JnYW5pYyBGYXJtaW5nIERpdmlzaW9uMB4XDTIyMDMyMzE3MjkyMFoXDTMyMDMy
MDE3MjkyMFowRDENMAsGA1UECgwEQ2hpYTEQMA4GA1UEAwwHQ2hpYSBDQTEhMB8G
A1UECwwYT3JnYW5pYyBGYXJtaW5nIERpdmlzaW9uMIIBIjANBgkqhkiG9w0BAQEF
AAOCAQ8AMIIBCgKCAQEAmal1SzZpSVae9RShUcN1MjM/B8rJD47K0c49Uxj/YUD7
oGuSKWpYw/nM7aylODTqfJt660KN+Q5AeiZemKZ+YfbiQJ+1YUZazTcjoqOghXFl
E70KM6xyOiTr1SBSS1zf161BHPvTmbBQpkqsUStSZISBKaqU4lhJnBsllei8eFFN
mHEO+bgGQbTnjVWwHS+xgdajMiemK+Cql+pIpaoduTTtNyfwp9m2wF45EUT4DyUu
cU8En3NOOrarkPPG7x+FEANo0/UrqJwozY91Qsv6EPkhFUbBvF8l/p7uNCK0CIBK
yTOoPkeHvEeWX+LZlbICpdJQXIdiZJAqIu56yOPqAQIDAQABoxMwETAPBgNVHRMB
Af8EBTADAQH/MA0GCSqGSIb3DQEBCwUAA4IBAQBiRATAkJaW55BPdZ6TKMYfSFlJ
9lO3K0eS6miuX6HG7OI6DHCBf18fjDLxg7O/HeVxSgI5txB4iEulRBcv35veDti+
R6PuebE1+g0QTMlw0WXlRMg+6bVaV2XwXoWQhhSnDexdQtcDPKd4xC6VGfK3sPjQ
ZSriMmrerVhGL9d1pYBtxolDbk9e/AwrnWKLPUDrR8W5DA+yJ/lL+k5pPrACNR82
cljDU3YA+bE+9LpNtfatPZwceaM7GupXJy9lngwlNAM42XFvWsTjH8Uy7ZJFOi0B
+3rLUOIXxCdpb88qeUGBN6BAUMhItoflSktN813vgKkiV7I0gNoU3XnUqG7w
-----END CERTIFICATE-----
"""

SSL_TEST_PRIVATE_CA_KEY = b"""-----BEGIN PRIVATE KEY-----
MIIEvwIBADANBgkqhkiG9w0BAQEFAASCBKkwggSlAgEAAoIBAQCZqXVLNmlJVp71
FKFRw3UyMz8HyskPjsrRzj1TGP9hQPuga5IpaljD+cztrKU4NOp8m3rrQo35DkB6
Jl6Ypn5h9uJAn7VhRlrNNyOio6CFcWUTvQozrHI6JOvVIFJLXN/XrUEc+9OZsFCm
SqxRK1JkhIEpqpTiWEmcGyWV6Lx4UU2YcQ75uAZBtOeNVbAdL7GB1qMyJ6Yr4KqX
6kilqh25NO03J/Cn2bbAXjkRRPgPJS5xTwSfc046tquQ88bvH4UQA2jT9SuonCjN
j3VCy/oQ+SEVRsG8XyX+nu40IrQIgErJM6g+R4e8R5Zf4tmVsgKl0lBch2JkkCoi
7nrI4+oBAgMBAAECggEAFZu+4tTD+Yw0zkIYbWcPFAAg3PenTojF/LsD5KufPg3l
VKnL5AcQdH6sUr/0e/L1BpDWuD6juGJIruS2aMEBBMWzC2NqHkPGgRU/7Z8U867+
h8gNpzaY2ZRXlaD18aMd1zaF8Y14NCSXMstNcByneXsorrNOPIYt08X9gxc3abPN
Zrln8Prqr3FcAhmdjSCCPjAnag4m9urlV5zX81pdlwpnq5LxrsAn3jXfci2bF4HE
kBKDL7IXZPVg86rSUrs6lTiqsbrqIcC0H7Mspqjp1eJhkbm64nWPfQaTZX9CRP40
lIOc1yWIrmmaaNQoesOLyjD2b52XsCNBOWMIHDsAAQKBgQDMfXuYlHb947kwcaHP
ndAj5H19xvsOINPujcz+uPxUr6yTmjmGpCcP7lHLL0fdRVN5fAMhrIzbdykSYkUI
FnhxGfP5PXVlno/1Ewht8/E7qigsVyIfIeMwa84Z0fXgyP1qwFrylK2GU80X3MdD
Y66hLhUFyU+uaJAUZF9AFyr8UQKBgQDAXlNG/vPR220syjaNpMKuiiuoPwUCkaor
+EaiXQ8XqjMNcmoLvsIF+hx+jEr1UCDtWf0hHBZAWIgZ0ek+6g3RufhTvlfjdxR7
t6h2lyTzxLL4oPC6tZU9DqW07+ENy/FGoCysB8ICob+VHHsbHTwWa2KbcqlHKJXT
K8ZMfhSWsQKBgQCqCi4cUlggBpyXi+XhnnjVX8p6LFvXA7U3SPKNXYV1Zh87HaN4
MkfJF4MsUcSQWnVvL4/rEHCQjiW5A74jW4wLgGk/d7uHJLLQN2NrCs4trvB47nuR
J7yjJwHatpyeroMLoaf+z2L7r/N7RDrt7pXnsUoJ5bw8avZj/pK12I4GAQKBgQCg
2j6oTudxwxk3Kp8TMYHYkJCQzqFR1JuGyMPHYCkOkLK/u7wQtiFm/gx1hLnpBmeC
EI0o8mNoyp6DeJKgmPWVOPv8ilzTRu9Jw/iJsTik3QUKAQlKFiwEMgs9kJePAclu
VOEFuDbyHG4mMPp/YaKs3H5HnUkOx1EAksntjD+LAQKBgQCo2BKFm+NNWwXPWFEp
M98luElmx6qq437HKkkxnKhgkc0XlSuTlgQHIdADMAhwxjOxK+oZBsMrbZRU/8jd
qpzP0kB/WyXqmv4oZE94i6ZU4+ywowiE/7GK89zIr1sKOsmKKvH5NKJHLXr3yl2n
50PAWFxodEEV/oUmDHAUeAz0bA==
-----END PRIVATE KEY-----
"""

SSL_TEST_FULLNODE_PRIVATE_CRT = b"""-----BEGIN CERTIFICATE-----
MIIDLDCCAhSgAwIBAgIUT5GDbvyrLH9Vkb7sFWPi1uFfhnEwDQYJKoZIhvcNAQEL
BQAwRDENMAsGA1UECgwEQ2hpYTEQMA4GA1UEAwwHQ2hpYSBDQTEhMB8GA1UECwwY
T3JnYW5pYyBGYXJtaW5nIERpdmlzaW9uMCAXDTIyMDMyMjEwMjkyMFoYDzIxMDAw
ODAyMDAwMDAwWjBBMQ0wCwYDVQQDDARDaGlhMQ0wCwYDVQQKDARDaGlhMSEwHwYD
VQQLDBhPcmdhbmljIEZhcm1pbmcgRGl2aXNpb24wggEiMA0GCSqGSIb3DQEBAQUA
A4IBDwAwggEKAoIBAQC8vFVDrrbPlVphmwXld9chzAuCt6cUwFYBTxaIW01Ex5Ft
sJvGti6ve5BFx+B+wwA19Y1t6QOOnOn56x0Phm5/NqYidqYCBcrrHK28OH3kBhiO
NZiJi+tybGhxg2kjZldPBmoVA2r9MU1qA0PrRpozYi1mH8W2f/7yCstAHaYxZcjn
T70KkjWc7jMpV2g/6wLUaKJEgryQWqMr1Ru6BR2Q7IVIe688ptO53JRutPj/Fh6t
J9jWyF7b0EwoYc0Un2lRrzYgGQ0gGXGJCax3pWjZAokvVG5PQEPqK9TXqWVj/J+c
aA9jPEQcfivNW0nU8LmKHZyOaG/q39Y1wd9EhfOtAgMBAAGjFzAVMBMGA1UdEQQM
MAqCCGNoaWEubmV0MA0GCSqGSIb3DQEBCwUAA4IBAQAvyyCobTP0LbxqcCcNhY+3
/GPpUfYgjZdRy4uRtSLjcY3v604Azyuv07rMlT8qkvyYTuTzGXqpqVN1XJnllklH
psdkdA4uhlzx2ewhZw6usGV8QZEcOl6kMUeZK7TDMRkE10EnH2Qzg7R24coy9cEr
anGHgti6QrTK62aNT7aBGIDmteI3BRXc8Pb3BClDKLPpOC8DwRPD7nmQ/0awF3nN
B7caCwX4NCUuL1/Kbpz5Nt8wZepCcnXwF8BrSsiBFoUI01tGTm4BQVc1mufCmAlX
G8mCVW2JuymC6yia/bAUbvFhowbUrX55/z8SVEKQTLRQK2CglORjOTko0UbUcgN+
-----END CERTIFICATE-----
"""

SSL_TEST_FULLNODE_PRIVATE_KEY = b"""-----BEGIN PRIVATE KEY-----
MIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQC8vFVDrrbPlVph
mwXld9chzAuCt6cUwFYBTxaIW01Ex5FtsJvGti6ve5BFx+B+wwA19Y1t6QOOnOn5
6x0Phm5/NqYidqYCBcrrHK28OH3kBhiONZiJi+tybGhxg2kjZldPBmoVA2r9MU1q
A0PrRpozYi1mH8W2f/7yCstAHaYxZcjnT70KkjWc7jMpV2g/6wLUaKJEgryQWqMr
1Ru6BR2Q7IVIe688ptO53JRutPj/Fh6tJ9jWyF7b0EwoYc0Un2lRrzYgGQ0gGXGJ
Cax3pWjZAokvVG5PQEPqK9TXqWVj/J+caA9jPEQcfivNW0nU8LmKHZyOaG/q39Y1
wd9EhfOtAgMBAAECggEAWcRt/YIk+zi7Qz9bn5fPYAjP1L2LH4iXn4nBWtuqNbOC
DRz6CppuPBLWPQpjUYdoG0IOoZ85jOQ/ORpFuTOkbKdOf4fVT5L3v7nlPGfWINVx
ano9cfZ15vd++baaFDdCAZk4bYQxp/mCK5EgBdCP2S6yDye/fx0D4pWVtIolmMpR
dViuWmLF+nPP1n8K6Gi5G6d0X/I0FVtKfNG/vTLCNUbKR/RgPrLlkNbcFECDuVEn
98XVsrcv+xsuPgG6Ayz2CO35wxFy6wl2g/qdaTlnoyjlV1mylvfnURyk2zUBtNvj
Qxqo1C42D2MiCz2tl3lk4xHRrvtC59IzMwuo0UFCoQKBgQD0CYvX+ChKhxQRRhGK
KgysySbQ4Dn/HCumnyVw5hRUCEvZUP6UU1pXiG3HJQ64TVzNA9dKZ+KjFCtt8ebS
7E8xhQNbKB1z/PI6VFu8yqaCKY0WpEGIaH/zk25gxJ/oA57uL6HCpm79ksOXMDuY
RAbRyxUuQ+mF7kcQG7R3la7UtQKBgQDF/MzTFd7KhzK4luUs5DFJ+fCicb13wXiE
Q7jaUIQQOHzNUiTbe8nkTvZg/C6JFTj1muk+gqIz1OPOyadAhFqfLsGY2O26GW8y
KvAi17Qd6VzSSzginOPKZZKXXaaw4TgmyyXpzLfFxf4T4kTytVyvEO7ZoA6IELV+
YstAmWE2GQKBgDNta5YIytzh2H3HaVzXfbJP9akhB7fWRPCpKye+pNwMn4ddhTjW
0/wMWS4VhiOa0gq2W4FnoSBC2OAjkUQz3oCOCmYEbyiJTrayHl8Lyck2XnA+Dz1i
4EwBbspfxV8MnEqPqSQvFMbFTgindnehJlrB1GXak/TQgRNI82AcICrdAoGAVbDV
weKsW8HqTQRaSnS1dIwt/1D1LTjafXyGLE8+6XpZYdBUzX4lYqBeeJmNVp2N2pdi
rkCCDabttlmG/yCJzG3DMvFo6uwJOZBmAN6VQYD4QLh3olt/J+GQcd0BwXqo//la
/ncxbvMDxf1f1CB07fyJND3XLEL3Gq2NxPbdoTkCgYEAntyUO95C6BQL46heCu7R
6ZvexdGTyRcOpRONSWyNTWbh/cPxkjHv4TrjFUETFcd10zH1BiInm5WRw0HpTGGm
mqWwk+grKPx28NNh4L3xmb9MWXQH8/iJjwPfD9EQ39zy3ahg6nLz/SSCnazOWIN5
APGqKKOj0t5FGbG9NZgAkwg=
-----END PRIVATE KEY-----
"""

SSL_TEST_FULLNODE_PUBLIC_CRT = b"""-----BEGIN CERTIFICATE-----
MIIDLDCCAhSgAwIBAgIUBV+nxo/NCVdtZFyXlpmq8HplFQQwDQYJKoZIhvcNAQEL
BQAwRDENMAsGA1UECgwEQ2hpYTEQMA4GA1UEAwwHQ2hpYSBDQTEhMB8GA1UECwwY
T3JnYW5pYyBGYXJtaW5nIERpdmlzaW9uMCAXDTIyMDMyMjEwMjkyMFoYDzIxMDAw
ODAyMDAwMDAwWjBBMQ0wCwYDVQQDDARDaGlhMQ0wCwYDVQQKDARDaGlhMSEwHwYD
VQQLDBhPcmdhbmljIEZhcm1pbmcgRGl2aXNpb24wggEiMA0GCSqGSIb3DQEBAQUA
A4IBDwAwggEKAoIBAQDXf+htQ1YfVlp2jqHJ+EUmB6bhxE1tYl5i2VaZVanzjYgA
9LDKeRhvUnaOWvLkGQbyzqvnAylXHXSNe9KAZrphoxDP40Ogu4IEGatxkAKafJ0s
KKAB3QwJlnOm2NJNuH9vOirw66ihkpz6Ydg7hmdWCF7bJgG82qwzQvEtIABUxZeq
EMJHLuTlVC5fyuIyggzzU1h+ss3bleM6oqT54yxJPoZYmvy067jeLGiyPg95EP+s
nuxLFhzeW1OZHMGmniDvO0zKGr9chiXKUSgugtT3MHUndociVCmc2OQaqjmWKwGr
O0mU5+lMgP2SojC7wpItyHSfn62YTLQ5VduDd5+fAgMBAAGjFzAVMBMGA1UdEQQM
MAqCCGNoaWEubmV0MA0GCSqGSIb3DQEBCwUAA4IBAQBeYWzDc79lXdOi2iopi50n
Hoc+91TiUr9Ubbd8lHWhidHcRYYWo1vFwM3of3eJ4rhAKPgwx9aclkryUEcZ05U9
tzs5OrmYsgnzdoX+zJenx/7NwuMO7Oe+XBAd16/4vGgSU9vPge1Ny4zN+zA1vn2V
zVlSBuGzmJI1ugPOVK9e0XAzJNsG5/pPRB29mbWWrrmFBmHvf33+PJms19aSfKrV
lJXYQV4Q9/xt5ehTPo20HF2r2CDiEjhV+P9QVRnwymuE/Zap+e1v+N+iWJVUB9hR
il4RskorFB1oY+FcNvDlsfO2bl29hGX3nNBQ0o8k1fjvuLz55MUNyGTeeqBGKkU2
-----END CERTIFICATE-----
"""

SSL_TEST_FULLNODE_PUBLIC_KEY = b"""-----BEGIN PRIVATE KEY-----
MIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQDXf+htQ1YfVlp2
jqHJ+EUmB6bhxE1tYl5i2VaZVanzjYgA9LDKeRhvUnaOWvLkGQbyzqvnAylXHXSN
e9KAZrphoxDP40Ogu4IEGatxkAKafJ0sKKAB3QwJlnOm2NJNuH9vOirw66ihkpz6
Ydg7hmdWCF7bJgG82qwzQvEtIABUxZeqEMJHLuTlVC5fyuIyggzzU1h+ss3bleM6
oqT54yxJPoZYmvy067jeLGiyPg95EP+snuxLFhzeW1OZHMGmniDvO0zKGr9chiXK
USgugtT3MHUndociVCmc2OQaqjmWKwGrO0mU5+lMgP2SojC7wpItyHSfn62YTLQ5
VduDd5+fAgMBAAECggEAOrRYX7NxOZYvjI5sWnWseKCrAGOWaA7dAXaNVbX1Vyid
/QyrQGzekCzZqQvzkNmUf/5267Z7w4R9pLEvddUGPuTKBqe1W4rY7z8C6iu92dHK
iyYB+J/70HzQwoncOFnjNSyWWA0KYgFri/WtjwGdEt2y4WYoIQc807YPtyg5jt3I
hz4wcXbj2crI9gyN97IrIAuoXkRxA8v/YqmVJpHp0mhDIyj9/4i8XevZQJ8sxZak
rYwO4ulK8AhLL4YXg60vjAFn5HcEbynZ3Da16wUhUt8php+lmJVDPo9rUIhC+nXn
QQW2KVnBJskHIrmrK5spM5PW7hX4A0XiCKJJ+H0XEQKBgQD+CNiObbyzBM+WH7uz
gFRJtZkwnkWBiMW4YdpEpBuoPyTJ8QgyJ70+7aI5pLlib7Rn9wjuaqZ6lB1+Qvk1
+SiwdlUDQpHg/VCGt9yddsiKd9gOU9obgR6zJaQNggkNrBNYMxC8GcaXICLd47ud
QmhaR7mjMeD1XFFZ7U1YM2oW1wKBgQDZKrzcMrQfXpgzO2ftoohYxL/XsTXUXyFl
pJaJFdM2B2dNzJ7rhj7AvN9BrD+csXD6tI6oeNxMrffeX3SXSAp+UkF485GERnv/
mn+jfE4J2xEofyK0f7bVqr8r6nhea+h2BV22dj3dBxGJ3pTt79kNbeh3qmMwuWUk
1SQqMm1MeQKBgDenjHo3xH2b8ja7oQ3EcbLsXDFwm12zr02j8oPTSFPl8ZNkgR0r
46Qjv8TNN+g+/NFCJ+zD5NE6HfQJjDus6KMwaZObRAZ8uOWq5mSBH5JmiykoacJY
2Xb6KiTjdkROjLZoCaSMKRv26GygdfwQDnio+hys0tIudYw0FxvZt8ZlAoGAa5TC
bosntAqWd3rMZ2qHBQKizuVY91YRI1s/v7VyJmfQgzgE2kRsvepS5yO/d45nm6rq
qQcGi237Rswe4/qqSB3TlWmEAvUv5FXTOVgRCMzfWSJyPNyv5HVrswO6kXv/csgB
vqwgxWgFBjmfqaeR7RcvfGiKLs8JDhAQlF7aynECgYEAhYFtUuphLMVnPObGE90a
Ly00uCPeJ2RUA746+7B/hEuK6Vq0lx5sjkAcC4lljtczMYqytNfRlj+Pm5i49qsD
LSTPIGleWHgW/GzAUL5HYaIAxdckKpcvY321szR2CiYjG52H/iB+sJSJ3iY0S1gA
uqiteEzAks8NoZnUpvLK1LA=
-----END PRIVATE KEY-----
"""

SSL_TEST_WALLET_PRIVATE_CRT = b"""-----BEGIN CERTIFICATE-----
MIIDLDCCAhSgAwIBAgIUXxPjAJgu/kDoq+EOobX/wSYZjW4wDQYJKoZIhvcNAQEL
BQAwRDENMAsGA1UECgwEQ2hpYTEQMA4GA1UEAwwHQ2hpYSBDQTEhMB8GA1UECwwY
T3JnYW5pYyBGYXJtaW5nIERpdmlzaW9uMCAXDTIyMDMyMjEwMjkyMFoYDzIxMDAw
ODAyMDAwMDAwWjBBMQ0wCwYDVQQDDARDaGlhMQ0wCwYDVQQKDARDaGlhMSEwHwYD
VQQLDBhPcmdhbmljIEZhcm1pbmcgRGl2aXNpb24wggEiMA0GCSqGSIb3DQEBAQUA
A4IBDwAwggEKAoIBAQCzYrIdaNeAReJVfaMXpHtY1JgjpAAP3XipZfrmRj0SY4pS
zHfEDSZByX7LLwde8B2ivQHDDmmIgDhL9TZ3pZlYmk2Vq0BQHJMciaI/fzF1+FNQ
imkccmvsC+LXft3SMG61ldFszMkVWGOLdflBzBudGa7z034czq3/Ucj2mE4jEsPI
OxnFH06DBadMDtGfaiyFPvEc1Ywr+LdJQ24LVrih1IZ2dmQtS40n2K77UUsvUs3s
jNx27qISfUI/tspa8DnKujuY/9x9AIzo5ldq8N20Ccns6kXxSewsxX1vH2uNH9RP
ReReTFsZU3z8xicFx8SBE4VcRXXTTsqm974QMYJlAgMBAAGjFzAVMBMGA1UdEQQM
MAqCCGNoaWEubmV0MA0GCSqGSIb3DQEBCwUAA4IBAQA52jQ4+CoZILaTRP3mFYpg
1OmD/bwzBsHbDZhB1co6d6lWel07fj3uNekBigyHgnciMGvXm2wSJIxEvsMoXIPh
yyBjdLb8IwaZRldnLPewUuTuA6WQx6eNwA+qEn6vT9tBVLMO0pRNXy1201c7oeCj
QCJQzn+tZweNdGuX06xgPX5q196gFS+BZDw/sn3ctQ/xCXC6gno21NRqyM2VdSCM
UIzCBQLoL9DVvpmC0atV9BO7LTvOYlEuCF58IXpBBi7P+3i1Q2z4SLamsKKcU1Pp
dJkK0lA+FfIYEGsUV09ddxGXRghU7YV0kU4iPMRs/ckin95kPiUOQx4lLo3N6u8+
-----END CERTIFICATE-----
"""

SSL_TEST_WALLET_PRIVATE_KEY = b"""-----BEGIN PRIVATE KEY-----
MIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQCzYrIdaNeAReJV
faMXpHtY1JgjpAAP3XipZfrmRj0SY4pSzHfEDSZByX7LLwde8B2ivQHDDmmIgDhL
9TZ3pZlYmk2Vq0BQHJMciaI/fzF1+FNQimkccmvsC+LXft3SMG61ldFszMkVWGOL
dflBzBudGa7z034czq3/Ucj2mE4jEsPIOxnFH06DBadMDtGfaiyFPvEc1Ywr+LdJ
Q24LVrih1IZ2dmQtS40n2K77UUsvUs3sjNx27qISfUI/tspa8DnKujuY/9x9AIzo
5ldq8N20Ccns6kXxSewsxX1vH2uNH9RPReReTFsZU3z8xicFx8SBE4VcRXXTTsqm
974QMYJlAgMBAAECggEAT059DH+DdtRuofkvl45Cch1bPbaNyHXTmKDbcd7vtSeI
yd5XvLdLiJ46jj22doSVtZL2KnQ+t/hn6zz33aG6z+84CclyX3iimWVH8+aZyVwG
CX+HxOnZSLxgh4ExNHHxIBqiQgWviN5Q9CEuF6bTNntaW7XO9ZFyX4Sa4lqngN1W
7eOlt11xwnTSd+7D4YODKeFsmNEGatL7Z/5rj2p8fYdKjEMQd4Am4tqnhvuy+/Ia
XUbrzloMaDH+aqwfE8leJq8VhBpVjUwFSKo0zHw1Rm3EVqFkiyPhJy7M7HqZWEO5
0yWq18FnRzhp7Q4iZapYNHLHqQk4D77lE0TSAvG66QKBgQDmqiCEvRksmTxQjIEj
X9cQIrUM/Rxs5VM9I65gG7726vfoGFL1c8ZS3gzdgBgtxx+9X3CqiVnPfzXWRPUT
S+pYc2DJnsjZVY/rytbX6T4Xu9mV3ROFeuZPxBsfwgUaMbA8Qn8ETY5inqvrABoB
DYuvyvTxvRd6Bktthf56hf1z0wKBgQDHFrHQbq6rLrvP9vn86s/pLf9dIgYRjAKs
CoeKQMFfbZB5Oinkx53N/cwUebFLtU5hnRdO6jmiJ5ITkMdjwiHoMnWFz7wvI/Zp
V3XjgDR/lIhAUnF8jEwkKnbD/2sqDJiXBGxGqx0nvlreMGmjs2HBtCGvj7Ep3FNR
YEo0FG2l5wKBgQDa0jIfOrUTFhud3mzz/gusBwDy3XuF4tfgfGUET84NuEKOL+Uj
bT2Lh5N03fwSEYEOyee8IKjOq8OLDcfhEneyiWIcY0Huy7jI25iNI3wAT/jOrvfB
/SFYMpX4vrrQaqrhv8N3dYvKCvTU7ze8H/mQP123pscKv8X2lNMhsNMMeQKBgQCp
tcTaAp/OuMXM36H2YUveYCGBCJHXv1w/v7IOvmiYqlMvo882gJsaj7C5+4qRGPq5
5ymJUczTV5wEJbRya3hv8SORb6XhIWzaG34Y8p7N6pXDDwRCwW3ennwjU8XMUHR6
t4B9NTxjNrdLFEXZD/7TGnRkrb6+ClzTz5sxjgByHQKBgEzWqkA8UPHV+QhRzq4K
vn4ImY3nZ2O42Hk9CQG6g3hL1z3yUpZeL6p5Wuw0p8NLn73YTY7iIqBZ31oJHOrH
Gr/SYiBP7dAtSPzhLJfGWuStXRCJTfEyudAv8KMXlxspdyLFu4iVN8rCiqlGP+KB
OEAo20EYspmrDR5Xq4hJtsM3
-----END PRIVATE KEY-----
"""

SSL_TEST_WALLET_PUBLIC_CRT = b"""-----BEGIN CERTIFICATE-----
MIIDLDCCAhSgAwIBAgIUIlcBc0KB9zljlWlercBlXSmz7i8wDQYJKoZIhvcNAQEL
BQAwRDENMAsGA1UECgwEQ2hpYTEQMA4GA1UEAwwHQ2hpYSBDQTEhMB8GA1UECwwY
T3JnYW5pYyBGYXJtaW5nIERpdmlzaW9uMCAXDTIyMDMyMjEwMjkyMVoYDzIxMDAw
ODAyMDAwMDAwWjBBMQ0wCwYDVQQDDARDaGlhMQ0wCwYDVQQKDARDaGlhMSEwHwYD
VQQLDBhPcmdhbmljIEZhcm1pbmcgRGl2aXNpb24wggEiMA0GCSqGSIb3DQEBAQUA
A4IBDwAwggEKAoIBAQDFXFmZ+JAM+10oeWht8WutI9nkQRV2oMtCwmdJYerOQXEx
NGNAsUZAYQi7pUi3WFfKIOXcr+hwCFdCaoXG8A07kpAXnKlFYO8agYCwcyiYGx1Z
raB2UtUik/6j1/N6bluG4uMljojWRIAK5umAVALAmEHj4Qu0QSsv2Bi9cjqlPn80
/mM0iMqXhuQ3u+ae3t8yxbI8pQ2Zt6WJV1q9idiu6JB1ZBkm1VSO2m80rVIia4JS
nK5y/psDK5xzhi2NMp6WrCAc9ll0uNEysW2c+1ZZ5K5Sx6aEuOJadDGmZwxaHBdg
EUxrKtCTFRppHmgsr/pBwwXtI1g6rHY/Zm/8SRsDAgMBAAGjFzAVMBMGA1UdEQQM
MAqCCGNoaWEubmV0MA0GCSqGSIb3DQEBCwUAA4IBAQAn8BB5RX1ZvKsKEY+UMEEZ
7u/yoXiocrxFsRyHGgjaB3Lh4ArMsFM6I3xIbeKjojidci2d5IxWACM4V4A2MQoG
FTiX192lg0a0VgutjcylGfXQuQuC4vQux+WaShksDTYn+CKl4vSDaZIkGi6j/MNb
lqgULuMUuilLJyNPqGobz/b1jE2N6uqMD6YUJHakD4ph/oVKOcxyvlcV9jGIdOgd
UlEk/zn3PPC6CadBQ3diEm9LYoLi3QPcsLYIFRSt2YcmdvMSl/9+uLAlP2Ja7RQr
8KPvq4WWGh7S/9tblPBrPeab+Zw405qBc3RfAYuLvk4+DXA0iXIBO5yNSDpXzN3U
-----END CERTIFICATE-----
"""

SSL_TEST_WALLET_PUBLIC_KEY = b"""-----BEGIN PRIVATE KEY-----
MIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQDFXFmZ+JAM+10o
eWht8WutI9nkQRV2oMtCwmdJYerOQXExNGNAsUZAYQi7pUi3WFfKIOXcr+hwCFdC
aoXG8A07kpAXnKlFYO8agYCwcyiYGx1ZraB2UtUik/6j1/N6bluG4uMljojWRIAK
5umAVALAmEHj4Qu0QSsv2Bi9cjqlPn80/mM0iMqXhuQ3u+ae3t8yxbI8pQ2Zt6WJ
V1q9idiu6JB1ZBkm1VSO2m80rVIia4JSnK5y/psDK5xzhi2NMp6WrCAc9ll0uNEy
sW2c+1ZZ5K5Sx6aEuOJadDGmZwxaHBdgEUxrKtCTFRppHmgsr/pBwwXtI1g6rHY/
Zm/8SRsDAgMBAAECggEBAI0bZzDP5+ZwPf33N/QLfWoQTPSGmBr2Af3cUs7DxIbt
gUml5CTX2pujBQRsu13jOvlYpiAwYSbgv8rLsJQ5A60JMB7BssDY+ntgBiuiWm7O
TCDXI/gVZy/O0mxAtWNeze/V/oPWsf1IgqfIy0AmUMV01v9f4udhBMizX5TrvARy
M41moISNV51S9CvVyKto4ojA9G4xkritKMJ0lsh4Pgs7Jp+/dIpWm1pZ8/bi0YEs
cJhxNswOfIM191G8u1Qr13/279aCauObqY9t6a1zuCeG9nqdbJJVK/OmjxX5W1Uk
vnKmxRyzxyw59kmnO5Gm63YE5gLZ99K/3qrVod0RZ+kCgYEA/+xtdwM5r0bwOaIT
bsVNO44Hn/9k+igkjXFNrt2e3nE0bOKwZY1lfhTknGBpVdHe4Tw+VJ1NA/nCAlXx
vlsVFjdyekC3gSAfsVyS2/F5BTMOPOf8ixcHXE759pyyXtKyTzhBZyJLXD6ge15U
SZkZhsetTKTkcFsFK+eYT4tLdM8CgYEAxWtxlFFbtyOfE8uIgRv9gnBS2bPusXHZ
MWnd/W1PtDgXdwWli1L2mFMbrY2UtKae20SiSZGRkjg8qZK+KedR7yxGu+AiUXte
fWnerz3UGIWbD5uPfTmpQBvBdXSZ0WTGTqsiqZawajpd7y0oOc/2HuBBKGpMped9
XgHrHKP1K40CgYEAk+8bu47OumXcGMR6TS6ZnVJVUAQ2X2/y6RvUlr8exWBUuJg0
9Q7N2xrCpy4H1YbSOgoz0X939FNb9TOu4KUPxF7aupZMPMTP7Rsg/ShRF1NS6JwE
3HW8WHyCey5K4QsT7T0MeUxWmYTOCWIWgNCR89nacBJkxhmnHKDr5xcSz/sCgYB8
1+lHhfud4OTkO73jB7RVHHsIOQUlKX3UBcLgVJQmv6H3HpcFeD2BLm0+X14+r2+d
8dU++NM5yF50Tdv729CwkytX+/E33fBvFtg/sbXCnBrmz9T5t9EUPXklscrj4/qU
HR0aabS+OJLWgZQCm0RlWiNaT36RG8boAAaSYgzUsQKBgHsZ9rP2HRruZvKKIx3u
BeNhXvrT/uyCgmGZ6DfncWsobF9HKjCd1e47wjhoPBJsKq0u79DZc5mhb6NyGa8e
qz8qD09ZqK3uVvxtZwDGFy4LR3vo6kLKnnJL+pstMrBGKyRBHryMF3srhMzS9guL
JzcZQSFoJRcYc82gq29lDJVe
-----END PRIVATE KEY-----
"""

SSL_TEST_FARMER_PRIVATE_CRT = b"""-----BEGIN CERTIFICATE-----
MIIDLDCCAhSgAwIBAgIUH4ybLZJDdYBBZEXa7rRC0r1WLYUwDQYJKoZIhvcNAQEL
BQAwRDENMAsGA1UECgwEQ2hpYTEQMA4GA1UEAwwHQ2hpYSBDQTEhMB8GA1UECwwY
T3JnYW5pYyBGYXJtaW5nIERpdmlzaW9uMCAXDTIyMDMyMjEwMjkyMVoYDzIxMDAw
ODAyMDAwMDAwWjBBMQ0wCwYDVQQDDARDaGlhMQ0wCwYDVQQKDARDaGlhMSEwHwYD
VQQLDBhPcmdhbmljIEZhcm1pbmcgRGl2aXNpb24wggEiMA0GCSqGSIb3DQEBAQUA
A4IBDwAwggEKAoIBAQCr67MRDiKgPiH15yQ6ZJeEcghZEoYXb98sCwHKTk7cDMp+
9Q92IP761jOmqXn1BTXNZQc62a1kZ0yIBUdqCxH5R3+BGF31fDwK0VPQhSh7Np85
iv3SHlrJBmNF+JX6A+aiKf0f6Zaq0pK1NiTaY7mfXMynSVdxJwwTgqQR0qfvqXEm
XWBeARhXpUelIyUexXHrGpXumAWY4wn1YEW+SpcGNXElidd/HLbJ/OHkCExd0nge
yKDQBabCAiIb6fm0wmL6HcD++mqsEt9II8U1qoUPfpUWxFpUSWBoZWcATqrPIPYu
LeHPvl3ZctQCuTthWHvum1zRK3G8YUXcTWwWsNBHAgMBAAGjFzAVMBMGA1UdEQQM
MAqCCGNoaWEubmV0MA0GCSqGSIb3DQEBCwUAA4IBAQAb3eNfxvPPv3QjmDEIcOhv
fyGS8orMzygz0eCtX0ODKsIWEBZw7bSym6fhEYvkltSf41KkeBInjDJnqiCJ2Yef
VvXcGLyHw/klmkafcvcVCoa95TNTuKb9ElJbdIuoQ3EWk4uQEK0ARH4K+mXA5lzh
RVbG9EWvmdYXaG9BrnX9Hr/lCEPXynGtbgKvglpFn8mAWz2ru44BsrkiZgMFBpPF
R6VJV3SRCTib0nsYXkLXyRgG5JcH/VPpFfyS+sLi/98AIG2mTWXTpj4dT5f9epTr
Cn00kytB4+9ZUvCMUrg0BciQkCz6lr46gcOwbMpzoxXWnK+cwPcr9zu+LLEs1NiZ
-----END CERTIFICATE-----
"""

SSL_TEST_FARMER_PRIVATE_KEY = b"""-----BEGIN PRIVATE KEY-----
MIIEvAIBADANBgkqhkiG9w0BAQEFAASCBKYwggSiAgEAAoIBAQCr67MRDiKgPiH1
5yQ6ZJeEcghZEoYXb98sCwHKTk7cDMp+9Q92IP761jOmqXn1BTXNZQc62a1kZ0yI
BUdqCxH5R3+BGF31fDwK0VPQhSh7Np85iv3SHlrJBmNF+JX6A+aiKf0f6Zaq0pK1
NiTaY7mfXMynSVdxJwwTgqQR0qfvqXEmXWBeARhXpUelIyUexXHrGpXumAWY4wn1
YEW+SpcGNXElidd/HLbJ/OHkCExd0ngeyKDQBabCAiIb6fm0wmL6HcD++mqsEt9I
I8U1qoUPfpUWxFpUSWBoZWcATqrPIPYuLeHPvl3ZctQCuTthWHvum1zRK3G8YUXc
TWwWsNBHAgMBAAECggEAeYUdCY0oRIQmlR5QqUW5I9FGvU8uoRpecU9GcK1xaHFS
IPMvfpxMHxmRYNiib+LC6O/kcGC1AydRHUQ9+mLgzYcQRTvoDkFGX48e42F7/7vY
SGBKkV8LZNSzDx5rRFHFkBKF7Sy7Zvt438XpvsSGzHJX5lcdC8pB6viI6GAyfF/r
wG5ikvh7Jh8+UoWVI3VhwEKm6H4E8G5V2pUlIcG6avhIEcWsb8af4inMAncTIHuJ
1NifePOv+Jeq3COFIj70eaHyuzhy0ESWvE6h/nu3e487ZnXZxC0w3b2QlOmVe53o
AkFpwzUBaVjeNtRwBiWpC3IUY2VbCqNR0/7NfIC2gQKBgQDcRd8sM2e6VHiyjkBv
qtiHFGZvZz7kd7sE1zV8KuLlT9sTsY+HQTC4cMtreZzdescTB3oHUOmfOmJXxrst
v1TfbE9ihfvfvndrlFovGv/KtllnK6Ku1MS8p3I5W5+g7MPndcO+VS2QPBgvLAUq
mIhWn77Cx/sF4q64nugek+7B9wKBgQDHzifuyvoywqLMYwQti2MhDbikd3MNBbpS
TdTYFTaCW/M0nQog6B1g3edD/gsGEQ2BEvX6a0OBD/40X1DgOCmuIBAKnwq2HiGi
yAc5ln2Zs/Ay8vjRfFc62TU84dY3xJdZ1TW0fDr3IyTi9LUiCMawbpC81+g2Wxw2
PNbv8YPQMQKBgCOZp1gddsZGoLs7Am8JzbUHNwcKSL/kGfXOUnae98zX+zBToj7Z
6mXk1PupzBB/p20L6E0GZru1U++bzuS156G0f6AMx4iB4AsjDvBODMlWb1ydUM2w
1Zsn9O4QQNxhZ8gg4GICojqNe9sj4jHgNSjK6KnSaF+rI1HzXNCUWCJBAoGASzcp
QzR38Wnh3S0dIoQJYiUHMCqjTfCtDlSsXlfF+Fbi/Bht+qtGe/OtHqRgw/zhZ4ia
vpVoiQpbOJ31FSMvVZROVaE/aAV5xgyk46HqUFUzhAqBbmLvd4DTEMM3YDEKhM/F
ctcdX3GEbkeOdGx3V22X4O8qRGQR/7zxcMwrQdECgYAg658h3apvIUbFaV3kOlZN
vZE+3uCFvFgrpI1eTmbMo50oDpzktr168MVu2fSZ8hB//ip+2AAIdNhzH8hi04fO
Xzesu+4/RgTv7wStTxMJS1rWUA4gGqb9Y7ZGMVuXkbEnG2EjFPQIrcESPytK7CT2
leydrAQ8338JrQG6x4jLmg==
-----END PRIVATE KEY-----
"""

SSL_TEST_FARMER_PUBLIC_CRT = b"""-----BEGIN CERTIFICATE-----
MIIDLDCCAhSgAwIBAgIUQv7oQqnVOgMJxwGj1o9mVlDjSV8wDQYJKoZIhvcNAQEL
BQAwRDENMAsGA1UECgwEQ2hpYTEQMA4GA1UEAwwHQ2hpYSBDQTEhMB8GA1UECwwY
T3JnYW5pYyBGYXJtaW5nIERpdmlzaW9uMCAXDTIyMDMyMjEwMjkyMVoYDzIxMDAw
ODAyMDAwMDAwWjBBMQ0wCwYDVQQDDARDaGlhMQ0wCwYDVQQKDARDaGlhMSEwHwYD
VQQLDBhPcmdhbmljIEZhcm1pbmcgRGl2aXNpb24wggEiMA0GCSqGSIb3DQEBAQUA
A4IBDwAwggEKAoIBAQDWc6RPgLnigv9641Ig8ro/KxVnUM3ORHs2hgp9Cj4lljnn
3Pl1IOlZu4pI8nQ0MGNVaiRTH5iqi1PmxfngFSsCAKjLFjty/Av2HpFiuYXQPxrC
suMPbF+KTpxi0QyxM/04inX9sZZpAPXbRtJ7XuFq71jB1mHvvyq/7/0mzTMwdUnX
LRfTMSN8TKVc+x0nGaQynIQbFxW2UcWLShaeNpfk0++2MeHOqrJo1LRta3uN8MBT
tdd7ISMv85gbwBajJ833BeE5/hxbDuohWnN6NOko+lKf+iaiVZG6LIqg4YLO8nEC
3eCtPSqZDeMcojF2TpfAs7RYy/uPTnrurq1I3M1VAgMBAAGjFzAVMBMGA1UdEQQM
MAqCCGNoaWEubmV0MA0GCSqGSIb3DQEBCwUAA4IBAQBQPItY6FjeAmX7cpd0BPdo
lWYb1yYOUVdVkHV5S160tGhLCcipZF511IOvjH+UUh/YVRUPyAhb+tCURTxWMAmz
xKiMESk5uJWoxWKZYOTkEE1SzTHdOLIO4gVz+z5ewovgSHOQ6R95AtCCeFNf+G8K
JZux2BbxkHZTiUK21UiarheTIOvdwn4W3NaGnDaxgIQncptLlLUSHKcc5FbLNhU9
4dlPe/VMglwI6R7euYFBdcJCpAnyhkeGGiEGZMPgu7oG8AY/PnbiAq4EFQa5rwB9
KtZGtuEvHhChxuCJrdhS3arkhq7qNPQc2iYRUeAnzK+CqVMMP+j9SqJA47YEoLKN
-----END CERTIFICATE-----
"""

SSL_TEST_FARMER_PUBLIC_KEY = b"""-----BEGIN PRIVATE KEY-----
MIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQDWc6RPgLnigv96
41Ig8ro/KxVnUM3ORHs2hgp9Cj4lljnn3Pl1IOlZu4pI8nQ0MGNVaiRTH5iqi1Pm
xfngFSsCAKjLFjty/Av2HpFiuYXQPxrCsuMPbF+KTpxi0QyxM/04inX9sZZpAPXb
RtJ7XuFq71jB1mHvvyq/7/0mzTMwdUnXLRfTMSN8TKVc+x0nGaQynIQbFxW2UcWL
ShaeNpfk0++2MeHOqrJo1LRta3uN8MBTtdd7ISMv85gbwBajJ833BeE5/hxbDuoh
WnN6NOko+lKf+iaiVZG6LIqg4YLO8nEC3eCtPSqZDeMcojF2TpfAs7RYy/uPTnru
rq1I3M1VAgMBAAECggEAKxheIqPptv1APf/El15v0xXjXTm9wf+9Cv3wyaPvTTpd
NJ0RfFo6yo+HgJVIiNxYeee0mQe2dD8/gxax2jgmxmY/hWBYXgkMlk8aRE6n92tX
A11Th9vtbyvQ/YKpHEsoTd51S6AOa9eHkKMw1R4CCq1CluFwGO+/tYaSxuNhsBDj
dQfz/MMWlIOYxs+NQc6cqgJlIULch8KhQ+DxTnkBYFBVCeo/kTRHfw+kB5OYevzQ
cUE+mli14Ifv84BOvz/t9+/tV3XT9tUvUM8uprxhl00/ZQ60oIOdvGrgIsWb2BDa
MjCGMvlzpgNW9d45aI3k8rJuGBTTJfeZBlpQwUv9GQKBgQD72XuhG1e3gx7UCRIt
Ky1CXIZowQSdgDB/qJT8cG710ftkBp217aBqf2xyIlSU4O9yPd8rysh7CAkVj/DN
1k+4JC/d9AaCGsz2BcyDPw2JTWErQAr9cjbNTBUmmIVeN6ZGXLjVKzlQbUfe0dA5
uXpDIR4DOklms0Q0AsUvp7HBDwKBgQDZ/GIFEavfIer239GwKWk+VIe4TUgzWXwb
WFfGuRE6jzd0gsSy8hwciee2gnTdI8kj01PQ5r9dD9D/bXE86aNiX5veMoGf1hpp
3SX+bCgbUz41cSeJnb8WiTcQaq7SGho+kn+KkK2c1a6sDwFpKdAkP/YW7RSdl17G
UeWyvfYDWwKBgFmkdKPIlrVEH5H7VJPtPWPUiSb6JQlmmlymBbnAz04CGsfkrvgV
h7bAejo5y/9d/Pyd1zTALhHUr18UZ/LsKF3zy3HmLPbcUT30nHHO3KOVflOlrQO/
RpBWV2TwfvAlQLLkyAlgJDtjWmSOK96QDVudixA9C+lZP5p/re4jc1qzAoGBAIoy
vL3z9x/uc/Vx7pGdn3B5zNWmgUi0yb7YYkXFnMugcor2QNgmMHZTY8jMqmRsxJ9m
4jOFpvrMBTd63hi9Eu1SKhJTuORpq7NEFktXrJGuU7kz9NoFXVlfQr6wtAbVr5/N
5vglQzw0KJpCpSVT8faZal4cjj5e8iIPV+3bCvYTAoGBAMwzbamlJ/bYK/1rDtVB
bY4kcjf7bYvIvtIKpAOooY+ecOXIq0vP+wqJCjNtltKZUcVvPQMkw0ykhabuKsPj
hx2mcPHE7koN3UUmMfYdr9GI8DpACImSI5OgAUn+0U9kX59oSGxxMF0ZTjJLp+sN
UMYmnIWCoC9PGLsfs9Gt9E/p
-----END PRIVATE KEY-----
"""

SSL_TEST_HARVESTER_PRIVATE_CRT = b"""-----BEGIN CERTIFICATE-----
MIIDLDCCAhSgAwIBAgIUCg9lMTGr9/8DyLNEaafobyIYAS0wDQYJKoZIhvcNAQEL
BQAwRDENMAsGA1UECgwEQ2hpYTEQMA4GA1UEAwwHQ2hpYSBDQTEhMB8GA1UECwwY
T3JnYW5pYyBGYXJtaW5nIERpdmlzaW9uMCAXDTIyMDMyMjEwMjkyMVoYDzIxMDAw
ODAyMDAwMDAwWjBBMQ0wCwYDVQQDDARDaGlhMQ0wCwYDVQQKDARDaGlhMSEwHwYD
VQQLDBhPcmdhbmljIEZhcm1pbmcgRGl2aXNpb24wggEiMA0GCSqGSIb3DQEBAQUA
A4IBDwAwggEKAoIBAQC7v3qmcCjmcREbWhZbtKpeZEwUPVkFpHg9yd0YQW0ZACZf
BZsJn5S9fkpfpJ9E758wRqvntAoKUwh0yntqjSNVEF+IwPs8eVV85yJLjZWzRlYN
FyZnr4ihtKAleDkXnSwDKKuWI3tm68GCmGlvzRvv8gR9/8Wut01JB4LjUslzaL5B
dM36gzjWGSxUD1A0gdG6leCMbJkRV6VQDLKMzMqfkrkleNZMfarrh4y2odaxGSlt
YGvIkeJg4R/vhUdWWnSCSZk8EtPZTC2ic/dMh0TZTw6zsaq0kkSf17a9HQ7exjgj
AMzTl4/O2mPQ1/j6t3nLqxXAMKRmQwe0RhW47fCzAgMBAAGjFzAVMBMGA1UdEQQM
MAqCCGNoaWEubmV0MA0GCSqGSIb3DQEBCwUAA4IBAQBSd5/DP0a3Pi7gQeYounMW
9qa/ZCn2JyIlCSKPiQ2lRJeFLzXzG/e1hEiNtSBWS0oMi5HtyhsBSbmPeEp4Enl4
Ri7UR4OhyEOddOAI98IEPtditV7YVczQi0h8a3/518yxvqVcUUOmIsABIvNWWtB+
jov5sHygh2gQ9LK/9SXWxguvI4U0AiFteJvLKSFqqcUWbNXQn09fJNyM8Cx6mnTG
5pba3FCnr39CdRgzn21Zp+plodI6xu2T/VmvkBcU4jFVY/i36LJkJ0EBjcaUiE3h
/1+POQXMivBuERizoRvtIx/xmsfKaFSp26iBW0I/AkQjCAJiVS+RF4DfaHLzg8jT
-----END CERTIFICATE-----
"""

SSL_TEST_HARVESTER_PRIVATE_KEY = b"""-----BEGIN PRIVATE KEY-----
MIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQC7v3qmcCjmcREb
WhZbtKpeZEwUPVkFpHg9yd0YQW0ZACZfBZsJn5S9fkpfpJ9E758wRqvntAoKUwh0
yntqjSNVEF+IwPs8eVV85yJLjZWzRlYNFyZnr4ihtKAleDkXnSwDKKuWI3tm68GC
mGlvzRvv8gR9/8Wut01JB4LjUslzaL5BdM36gzjWGSxUD1A0gdG6leCMbJkRV6VQ
DLKMzMqfkrkleNZMfarrh4y2odaxGSltYGvIkeJg4R/vhUdWWnSCSZk8EtPZTC2i
c/dMh0TZTw6zsaq0kkSf17a9HQ7exjgjAMzTl4/O2mPQ1/j6t3nLqxXAMKRmQwe0
RhW47fCzAgMBAAECggEARnkheMgxEg7u9O1j5xhxuuy7Af3lJJEP8WGMdEZaxT+h
J5nbEEmuc1KsaCpK/n1Tq7NbY6XY/vcb/XrjyKMh2BRFR/foVlLVHAVGgkWrI5gL
RO6jo9fn2YsLcgUmqQ5+LtFdVwYKlB96i6LaMPU0v2SA+yq+8U4s3HTNVLcGlyLc
v4eBAdGBIElWMK4ucH4IXmeVvxpvOHiC/mfMTu/LH6xk0lb6qTdM3zIzsPXjhjEp
dmnPMrS1AKOZ/abw/Yvi+4kuG6iLjeQWB+Z+BZQ0VJ82u1KRVxiH1USJo3Rm2lls
OB806LFcgOrk3TCErceglIzSixJP8LYLP1W7JcDBQQKBgQDwVRUx6Tvhc5cpYOu8
LrB6fIpdDTGccnLeoC8flqY7ou+ddYuvQTFlsPP4FLMcFuPJjbqbXPjwFRLcZFjn
aZE5VOVYlP5EzN2MQNZl3GNsKquUK/HqZ8hmacAknagDDad3Dxr/a+2hUDNrLHPr
YtQ5jabUfCi1eHz9FL3/RRyhdQKBgQDH/NApKnpYHYyvAr6vl8uWYm01VkS+pqON
wPyD/USCAU3lAPlr+Yt6hphhEQ67+aZZ4kcZIrYWdIJ6JNjNxVtqjcEPu72m3/qz
56/9CmIEDEKfIoBDvNOJUS/O+u4SEuLpMGreuO+POw7PQ9iA1PMrTXH9lTwEivlz
NwpEnvwchwKBgQC+SI9EekcIBQ4tG+jpkQn3oP2oGRcrqE4cyDUnTI8HbsVLJVNY
ikSDIGy6AiGh3tmxrn6OHjmXVQge6XCeoK3z96yyyxza+l17e6aE9c7eSJaa9YRP
tKYtuBMCqrTo3fm2wYX9r8Vw0GA1vfd16kTf4LCzUi6lJ+XGN5MLNvwpNQKBgCoW
8jSHxSIAbhhzSnCoUOfApV1hX6yEY820vTCGQEHgRmWZE+V+qrVJ2I4tSd2UCEfI
kNAgdxQ4xzEvyhVcoQXG+cf26k5Ru3DbpTVrVv+lGOxnFXmsJxUyag50z2Asa2dK
kmN3pquNcWt7yvgqWVdWwFPvcac/HIr8HYQdtc/HAoGACSOB38Pq/wsud66os5i+
4TBx5wK46uSRWXpLbjL8afuFLhrCiOmtqiOVmTVmVYnASPcpiny2jLtanPlu9WZl
PqdUO50/a4zLcGuJ8grnNn+YplngmZTtZJVHn72XAIphdQO8rt1UFjozyiHxYPkX
q0cBfURX9v88SepGlqqyMaI=
-----END PRIVATE KEY-----
"""

SSL_TEST_TIMELORD_PRIVATE_CRT = b"""-----BEGIN CERTIFICATE-----
MIIDLDCCAhSgAwIBAgIUZZmj3NMn41MJf/JZnA19S7GWBEcwDQYJKoZIhvcNAQEL
BQAwRDENMAsGA1UECgwEQ2hpYTEQMA4GA1UEAwwHQ2hpYSBDQTEhMB8GA1UECwwY
T3JnYW5pYyBGYXJtaW5nIERpdmlzaW9uMCAXDTIyMDMyMjEwMjkyMVoYDzIxMDAw
ODAyMDAwMDAwWjBBMQ0wCwYDVQQDDARDaGlhMQ0wCwYDVQQKDARDaGlhMSEwHwYD
VQQLDBhPcmdhbmljIEZhcm1pbmcgRGl2aXNpb24wggEiMA0GCSqGSIb3DQEBAQUA
A4IBDwAwggEKAoIBAQDiAHh3GaeWWIKsNlwDE6s8EfKs8AKvq7ThxFGtTAbZs1MT
ckyg/7/phaihOVXmpdl9Lhul9nUxr3pFkW3pDuCXWeF/QB4pJqbbDUdOl1fu1g6z
8H3hLIKK8+yKm8SliLKGlYlm0lrCh+bR1gn46ACImMxs2PiLJydaG6TH/rnQZo8k
8S8unwpjrI09dwnwdhTGG6F3789bEHyZbwzmitHRrzYUKDviazaWvyspDNg6CJ9x
+ufdVyY3vTAVsQZaGyTZMqxE/3cLtT3CHCGZaMddlVmicEIkgKh4vCYV//6suVbW
cQnzBXYCbAC0jp+TaHFoLztoB++ODJbQ02kI6xylAgMBAAGjFzAVMBMGA1UdEQQM
MAqCCGNoaWEubmV0MA0GCSqGSIb3DQEBCwUAA4IBAQCMUxFYqgEUN06caqVcTTZ5
rW3V8oRETxkCZ5okxRnKKJk6L9YhdkiL4Mjsbn+9ZwmWwEZJjlqOGUC8uZZgrRjr
fqyftmYjvRVMZNZoh1wqp3kcEDXPLOqM7ixpK/D/ScOZc8G0EpiTykj4lmgF8/7t
11fCyv6vHYLqsDFNC3BJ8g8E09Zej2bEBwTXp6g52J/YCuJ2xpu9g8mOF2xs3ECv
M74JEGlF0eNjuAQ+R5J5DaNwojHDoVYMYT5X/KaPxmLLl6b6n7ZvKuCZHs1CoLFn
1Jg1JGLOczrHvHnRPr4zLqffdnq/SFQP1MLFs+QUORLpHved+PPZJogSbRn7HzGQ
-----END CERTIFICATE-----
"""

SSL_TEST_TIMELORD_PRIVATE_KEY = b"""-----BEGIN PRIVATE KEY-----
MIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQDiAHh3GaeWWIKs
NlwDE6s8EfKs8AKvq7ThxFGtTAbZs1MTckyg/7/phaihOVXmpdl9Lhul9nUxr3pF
kW3pDuCXWeF/QB4pJqbbDUdOl1fu1g6z8H3hLIKK8+yKm8SliLKGlYlm0lrCh+bR
1gn46ACImMxs2PiLJydaG6TH/rnQZo8k8S8unwpjrI09dwnwdhTGG6F3789bEHyZ
bwzmitHRrzYUKDviazaWvyspDNg6CJ9x+ufdVyY3vTAVsQZaGyTZMqxE/3cLtT3C
HCGZaMddlVmicEIkgKh4vCYV//6suVbWcQnzBXYCbAC0jp+TaHFoLztoB++ODJbQ
02kI6xylAgMBAAECggEAOAKJ2GqBQB97cxadwx1yyJZiID3zTHovf+xZmatH31gz
9JPVLel0NHmtixdclKbxubZdn8nuzXuBwBAEv0eynY/m9NR9JRGxNISb8XxMjKJ8
TlgBunZ/e9RsAQYNvECejgAtZ1AmsiNgLwzut8M3rqK/txImtsXjWM+VDQOyJVVu
SZRVCZvjSjmLKZE7GPVqzyi8MWo8LaY8i7H3iCko1/QVzA39Y+HPq6od2QPboTmU
gpIfLgbQqjS4FbIhNg8NCen7nshGybmCjP3wXPMoqVA46H8w/iOid0KM1tBdQw0P
YT8xRmhr9Yfkk62GSsaeu6lrJD1ZI9aOYN1G74MzGQKBgQD3wRJHZBrG74u92MtO
Xhz8b4jr/qkqYqkCGiZZLWzlrijPmWUll4zdsbFAlgzlmT1/mWEGAe0zfQ3hbmxf
toqCLF4r6shOqd5fSMT17If9aKwjhYc7DHARda5aE4rkyRy1k+6u7MKRosC+HG2y
Y5AqGtI7mgKwF6zRUr92WCVElwKBgQDphhBK5qb85ySqZiVu743WSbgC1E7o76pu
RGwNPzy8fVn88AghtLRdiXOF9z+NK1m1Q4STlSYRWox4MccceD96NzNs09VpObSh
Z9ZgfoPVRB1pCwj4AUN9hu5Vzr2KT2J2elv7zJQfIjuKSOjAq9/R//iuAeZlfgHs
ZrmC1W6kIwKBgQDp+n/Nxl93gyFhIM4Ya89KI/eWkMGoUta0MogG7lyKqSjHrmGU
2ARkFn2EtnDloQwwZmT37HfciXzDaqqU1esHNumU5j1X9Rsat7mzWzeu/dycC24E
OSHZi18mmJAyszAW1+excc3rBl6q7GQ49chfy0bCnRduwF0ortI87M/9bwKBgQDF
RI0K2OGDjrb4gyVoG1FUDh41taebOqpcT8x/PEZQbAvSkeosnvwmb/B44K580HwN
laWvDjWEP1ueRV6P/DyTP4JfkmsbYrXmC1ObXAR96fZ2P+4poteieJNpRSX0aq8g
qqh9gwo1arOlU4XbDNYcDgHC7LP2VIXHb9eSYD4AxQKBgHjHyFvTfm6ZRv6WHcTJ
LTp50k9l2sdXe14kBnblEBTvo5DMbN+d0JJWGCywj0s9Zhdo7W9Lu72NKDnp/rM0
8e2meBI5lz27JJ1Iggozulu5xiYkHQmt2FvceZ2ROlvrCVkP/r0AXr77T1veIWTr
vGxAJJJJPWNb/rpmosGSnnt/
-----END PRIVATE KEY-----
"""

SSL_TEST_TIMELORD_PUBLIC_CRT = b"""-----BEGIN CERTIFICATE-----
MIIDLDCCAhSgAwIBAgIUCo4bPbI2+6ucwAKVWOVvza/5Ve0wDQYJKoZIhvcNAQEL
BQAwRDENMAsGA1UECgwEQ2hpYTEQMA4GA1UEAwwHQ2hpYSBDQTEhMB8GA1UECwwY
T3JnYW5pYyBGYXJtaW5nIERpdmlzaW9uMCAXDTIyMDMyMjEwMjkyMVoYDzIxMDAw
ODAyMDAwMDAwWjBBMQ0wCwYDVQQDDARDaGlhMQ0wCwYDVQQKDARDaGlhMSEwHwYD
VQQLDBhPcmdhbmljIEZhcm1pbmcgRGl2aXNpb24wggEiMA0GCSqGSIb3DQEBAQUA
A4IBDwAwggEKAoIBAQDTrCQBeTfXl3xKstyCxQpGelFNEagDRZLaJe/dPLN9FiBq
N25JmL0mMiJfSSI1HQQoMMM0ayilEU8epeqWkWLi+Pw2aR7nuayPzlqfY411pOVy
I0lZWi/M+w+ytyHA+/ORZHqSUf3Zccs8PouexC7bU4ScLHo6X7bOSiLfezNsqPAc
RngI9C1rPLrzQQHUd1m2aQOhvMmbXfawaofZzSRZT/Ipdhm6TsTy4325XM8BtoXm
CQtEUyM8xgmOkQF/4m/N51/+7Jnchcb3pBP1RujmibOwH4fAlDwu6A5kwe1oFMaq
ql15KdElfkRvzbVDdyAVjUnW2j0WZ3WnumM0uTSbAgMBAAGjFzAVMBMGA1UdEQQM
MAqCCGNoaWEubmV0MA0GCSqGSIb3DQEBCwUAA4IBAQBGVJ1SnI7UT7M9BSt6Sfnu
noJa96HgjVJTwMBkGIP7phGY8sm2B9OSVlaVUC6tZkJaXSPDqejdHRFleFrMn+yS
eY3apM70u+GHRIjozf6FtQQ8D9AWY3sL1eDVfoNh/w6UPaLtt0GtvLXhR9gCvPgH
WKNJ7/5hSsJHRVKBRZtuLwrU4nIwrdvcFHh9btAeNU+ZQ9BPx+jD7G0b3MC4aePg
M/mUQkCBShhQPFIuPO5B5hYmyqvSfKfRCCXz3yObo0/DmEk1XlWu5fUStUXMoBRl
JQ8AxL5aH9GLLkdhMqzInZiiEgFEEEF9OjeA0FpwG7qmRMwL0d6Mp/VfyMV3CwqT
-----END CERTIFICATE-----
"""

SSL_TEST_TIMELORD_PUBLIC_KEY = b"""-----BEGIN PRIVATE KEY-----
MIIEwAIBADANBgkqhkiG9w0BAQEFAASCBKowggSmAgEAAoIBAQDTrCQBeTfXl3xK
styCxQpGelFNEagDRZLaJe/dPLN9FiBqN25JmL0mMiJfSSI1HQQoMMM0ayilEU8e
peqWkWLi+Pw2aR7nuayPzlqfY411pOVyI0lZWi/M+w+ytyHA+/ORZHqSUf3Zccs8
PouexC7bU4ScLHo6X7bOSiLfezNsqPAcRngI9C1rPLrzQQHUd1m2aQOhvMmbXfaw
aofZzSRZT/Ipdhm6TsTy4325XM8BtoXmCQtEUyM8xgmOkQF/4m/N51/+7Jnchcb3
pBP1RujmibOwH4fAlDwu6A5kwe1oFMaqql15KdElfkRvzbVDdyAVjUnW2j0WZ3Wn
umM0uTSbAgMBAAECggEBAKXCtmeY/8wLS0BMFTcrCsLqYuSRoRr+zuOatd5w/LZG
L5g+VFW6ENXqiNRJt0oUsP6wQQ25pRivF2CO2ciTjfbkuM37QEKDOsla9ci/8zVf
rnbVf0lDwQ8qxL5Vf09bfwAqyXnwT3SLEnbZHAl25KLJIp4Sjp1L+yJNGEYeesTp
kUb1CwxMqGwtTRZ9AVjeH03OYC/mE3l461q9Wh8yc4tE94ASm/DRLOacd/+gGzRx
X8lN7P8bUsH/G0bpBfaSj8NuOO2Uo+vyRP4nPyLakm+HcgDhnElhrs+IHEuzMq8O
CI69sj8/rIoDBt4HQ7VhZ6IR3NDC6N0SnPLT602UTVECgYEA/Wo1m9QEkMYJUUos
o34xTfUrrefMYRNXiQOy6u/ExLGFJ44kgttpLHrZ0JYrJT+auoT65SukChXftOna
vPIN6rI5IGhb93uyGxiTRj7+hhCne3gMHsmDwJB0veKGBS843AFRwbsxbv9HJc/b
01rZ4BKWSRF0s+U/6Mb1aXO3WocCgYEA1dTr1BHH/iD8vJgKKeSB4eo2q7hU5FvJ
3lud8JeQ/AOmlXfXusm4w4mPJ7whCeBfobR850VdrEZYcT7DbpsYjmBG+4+sbjg2
cPrEt+nZ8Vr6JRpbyq1j3P2osrnDpErusZ+gxX9zGh9alKsRVC7hmiOzCmAFAf6H
Gj5zrbzRtk0CgYEA4uuBV6lx8SW0YDtYX4p3ogRBebdQVzkXsFREmYXcn/kKcBIj
dZ39vtu/Qb3GotMivZSoiiAbAwD1Ui36NilV9uxipTdt6t2z7fmCn2t3RRuSrcgg
qkzukreIIiS+t9PCSZdQ23bBXFBxKFXJ1afL448hTgq4gwJsyQen6Ca7b+8CgYEA
xbDabvAZhBufTgUKsHxwkBrnfI8o/Q7XbVoqhPq7siL16g4oRqqkxTLyRPwrV2Q3
RdsF9xMsbU+ECP7L1ABUDZ15Qq4r7qLNwlo1cQsk0X0Y8yCRaKoxP2jMhKA1/jjA
wTshejZAhhAiwHv/w2KsdMM4jgkD2DonUd4XOLLu96kCgYEA6qvaeKQulvy8GjN8
eZdxPHvZxEc6bncv27dTBTCfJAwvQnAM17XGuYpL+wpmBWT5NyMQhqR8ufTjCaTZ
mYQ8D+fbP1dzXsNCWy2ULXQyDp4iBr8DD+yhxXe0T/osEC2w9GOpHhTskriyjrDr
jMdzq9sbblgFm6dKe56DLvc4z/c=
-----END PRIVATE KEY-----
"""

SSL_TEST_CRAWLER_PRIVATE_CRT = b"""-----BEGIN CERTIFICATE-----
MIIDLDCCAhSgAwIBAgIUZXUt4iAbkAXAUd0mDEZSMXmcl3YwDQYJKoZIhvcNAQEL
BQAwRDENMAsGA1UECgwEQ2hpYTEQMA4GA1UEAwwHQ2hpYSBDQTEhMB8GA1UECwwY
T3JnYW5pYyBGYXJtaW5nIERpdmlzaW9uMCAXDTIyMDMyMjEwMjkyMVoYDzIxMDAw
ODAyMDAwMDAwWjBBMQ0wCwYDVQQDDARDaGlhMQ0wCwYDVQQKDARDaGlhMSEwHwYD
VQQLDBhPcmdhbmljIEZhcm1pbmcgRGl2aXNpb24wggEiMA0GCSqGSIb3DQEBAQUA
A4IBDwAwggEKAoIBAQDxVh9zMP+GF0XYDAqC3vehKpK2gTXSZTdgQWn0YMOkKQFZ
NNHHkWAtePO5p7wSbysSUnurh9GlYtsK4kDnkj1eVBCWfVyPM/0cfkbhIcv5Jpkr
qKABv+6b3v1mikl+erJ2SE3GEWY7wThZuPvNh8kDAYs7MuN766jQ59wSIxvCPlpp
cObzbz21dHRrxDl8zCzNOk2z41sY12sGvtR1fWTIByqxnNy7mfa15/uEtY5qVaVz
uQBm+gYV+lRoW3sHBJz9TEH92s+VnSpZj/hHbL8kpN8y0zichH9vG17E78LcCfCR
B6fd/Civ8mZZNhH1cCGlm26w8y7qM2PnEwvsVJ/xAgMBAAGjFzAVMBMGA1UdEQQM
MAqCCGNoaWEubmV0MA0GCSqGSIb3DQEBCwUAA4IBAQAyQKtGaSz4s/U85m3zSqTm
fykoZVo9+BhqPEK3bqiA/wQ4RnQushPEuaLqdD/qI9l6h6jKgnx3hyJ0Ht8CYo4r
KAEhRVSoImdqW8TpFIOG2vNgK09HuI0ahwT3NfmXz8uI87IkzHco+QS/i7AMvU7V
vjyFXSjWWQYmnzb7gWw/LEcpqScMB6/4UOam3G/xznMiFCmUDn9CEh/VNFaE6YK5
9VcfE2mcOftm8/jstoOgz5a/XduxJGObE/esMf2XeLLvfhIJV5yL+AkyVUrgESeB
/SVfSH0gcu98o+jp3fT8zKF6Q53D4Uyf28HUY261pvvvZFnshprKR3Tzfjo+LcpW
-----END CERTIFICATE-----
"""

SSL_TEST_CRAWLER_PRIVATE_KEY = b"""-----BEGIN PRIVATE KEY-----
MIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQDxVh9zMP+GF0XY
DAqC3vehKpK2gTXSZTdgQWn0YMOkKQFZNNHHkWAtePO5p7wSbysSUnurh9GlYtsK
4kDnkj1eVBCWfVyPM/0cfkbhIcv5JpkrqKABv+6b3v1mikl+erJ2SE3GEWY7wThZ
uPvNh8kDAYs7MuN766jQ59wSIxvCPlppcObzbz21dHRrxDl8zCzNOk2z41sY12sG
vtR1fWTIByqxnNy7mfa15/uEtY5qVaVzuQBm+gYV+lRoW3sHBJz9TEH92s+VnSpZ
j/hHbL8kpN8y0zichH9vG17E78LcCfCRB6fd/Civ8mZZNhH1cCGlm26w8y7qM2Pn
EwvsVJ/xAgMBAAECggEAaPItnPb6twHZ0nhx/bUd9AzCXfDUSdjP+uCXRbjqerGG
L5ejfeg+7adCPUKuq0mCbmZF9zKJvSS+4f2/gbP7UdC2oeqD3JYcBE75XZ9HxuG9
C9o5MmmXRlry0KtkCEcs4fjRMUeRsHx2l7W0cg0RIWiDdkvL1rCE6ctZzN1Njeqd
UuX9K4ruErxZOO2GXlkEheK/6C9ezvt5qGUNpr2rcpBHCVoOmOuQeIzwfdPrjlNE
SFq0wG+kTE7z1ucwc81OIuHlQX1IGuMXtFHEnB9iuAqZ/8Y9J5a9vj5EEZTAIcKa
4UeJvKon9UtP+kp5PNBYso/Fq+uCYQgnKo31Hjte7QKBgQD4nHqIqF0kzcSCnqTW
Ys4tDab7KNNTkPf38OMiF0S798jzMEZLDA4m0AaP2pSk0bSbvjCp3fLz74sjEmZO
NKob1nWPFP+yuLhS9PdupnLpHLj+LCT4pmvwg5gvM2Z3EOFrNJNrdR4ei682Z4vC
bMII0JCQcA3aMqx2MmIh7dmQvwKBgQD4gkt2JY7IFwy1wgf5sJpTzQ5hGIw5q17G
S0Ee7TuvV4IROVck+feJ+Zysz0leEIqqVVz1ku6c+rQ3Cod00ZVMG1TaBq7QOGia
tevvLhYY52IHbtxXUWy5T0+am8vXz/wBbFmMSqZ3cu5emFh0daGf03v1jHB2Xtgo
cBRdgHdLTwKBgQDVUh9qJ11U+SLHGa1DL6DN08sV85/xMpEzNIUQeXrG9wR8d025
k2yJLTKUOPAWxMH+aSGEgCe53C89NsqGDHZyUICq90+4YPv4Yq31SemL0NODdQl8
OgCgbaolxisDu35Q6Nod+G6RszXyrsKjX4LW4W9KIHwiYBzPhsfhaR+oLQKBgHPd
bAmd4UBxXr+vw8ArEwlXZgjnRRnuSLXziF0/BsDt7/rP3U2kLkHqW55G11JALCbW
vgzRgOc4DKZNBnL09MMTSzCMRR1X742SnHpb5nmeCBqnGZysniCYVekkEpqAomKX
ffjnJU40C+eW6EcEQWMfW4BVBmpqNiZEe3pM11IJAoGBAMHxD5Waq3fg//mCKmhg
Ud0FqKksa6lqYnUIFfUqiq2YwRYOBLGEYjheG2bgALZ/rHCWjdL1HvhCKl4PJTSA
3Ut8Yx1fyexZQ/aBzLpvWbWRIcj97gDMniVoOSMnCSilrK0ASr9JUCGo08d20fSK
EuQE6iLXGSX27W02kzBke/Q0
-----END PRIVATE KEY-----
"""

SSL_TEST_DAEMON_PRIVATE_CRT = b"""-----BEGIN CERTIFICATE-----
MIIDLDCCAhSgAwIBAgIUQBjubkcEz8Ame+evhVR/P+08N7IwDQYJKoZIhvcNAQEL
BQAwRDENMAsGA1UECgwEQ2hpYTEQMA4GA1UEAwwHQ2hpYSBDQTEhMB8GA1UECwwY
T3JnYW5pYyBGYXJtaW5nIERpdmlzaW9uMCAXDTIyMDMyMjEwMjkyMVoYDzIxMDAw
ODAyMDAwMDAwWjBBMQ0wCwYDVQQDDARDaGlhMQ0wCwYDVQQKDARDaGlhMSEwHwYD
VQQLDBhPcmdhbmljIEZhcm1pbmcgRGl2aXNpb24wggEiMA0GCSqGSIb3DQEBAQUA
A4IBDwAwggEKAoIBAQClp3iVfH6FLpZut6UdSrfkIfqED7h0aj8rkUi934BDFQiP
I87MuuAl7N3Nj3U3my+vppp3se0kt4cro79KStORGGuKm6EftkWJj9PIx/UKU0jv
PmtU2T7jzmohwM0RFwXSUUpAnInGUptSNlngbDJSQo92KYqCnCCw2Kllh8tSnaqn
/cVeBeOQ6ippM6YwJGs4rVMzS0v93aUvTXsKHaqq+wLe7Jcbiy2iAZT2HWZcuIt/
uhWDTRiDMxFsSl53O2dtG5tlvxS+kjZ0YOZbhJMcddHBNg0fX6oPeEzMB0DMs7Nj
3Q4CDrPXYIaLryMccGDljrF8xZ1+rlOLar1A8pufAgMBAAGjFzAVMBMGA1UdEQQM
MAqCCGNoaWEubmV0MA0GCSqGSIb3DQEBCwUAA4IBAQCKnK69Hada53vK4LIQS8mk
PqMiGLkrNsdqo+8/zm31wWQaL+XfWEzdEWfpSy4nPAKN8PriBafoRJynxUzNKNfP
YwzSpdwh49I/hQXgTg43Ps/Ud8eMAOwZ8hQFjtpxwMN5KMCNUZ2WkN7gyHN4eCFL
Vi52fq0zSvKIgCiB/G5oauC+4oesD3KhNFNdGDM+u4cZowfJP0ytetW9YRppUDyL
Di8vN8lRfLQmt/yvEF0Qgxuz1w/4D090mSHNwkiQFvu1+A21PEkk/FGsOqaEXyjN
a/hVuQii73GQQJgDCbeBECbmNz32rXYhzm0/Gg2QQ3B592qNnyDfU0Jxsq/IJtcU
-----END CERTIFICATE-----
"""

SSL_TEST_DAEMON_PRIVATE_KEY = b"""-----BEGIN PRIVATE KEY-----
MIIEvwIBADANBgkqhkiG9w0BAQEFAASCBKkwggSlAgEAAoIBAQClp3iVfH6FLpZu
t6UdSrfkIfqED7h0aj8rkUi934BDFQiPI87MuuAl7N3Nj3U3my+vppp3se0kt4cr
o79KStORGGuKm6EftkWJj9PIx/UKU0jvPmtU2T7jzmohwM0RFwXSUUpAnInGUptS
NlngbDJSQo92KYqCnCCw2Kllh8tSnaqn/cVeBeOQ6ippM6YwJGs4rVMzS0v93aUv
TXsKHaqq+wLe7Jcbiy2iAZT2HWZcuIt/uhWDTRiDMxFsSl53O2dtG5tlvxS+kjZ0
YOZbhJMcddHBNg0fX6oPeEzMB0DMs7Nj3Q4CDrPXYIaLryMccGDljrF8xZ1+rlOL
ar1A8pufAgMBAAECggEBAJgRbu67hGG6bLpit552Mu2oC5Mj405rImZaTo6PF+18
54iPdI4Ylx/5m3vSz+Yl/dafeHmcynfESr/S6A3JNwKhikeJqpWz+43WjLJqbRX3
cqK9iEYx0DvMBz3JAfdITT3PBfzeNtPqjU8hOcx9RoyhMZVleROBQ7lUi9z6lbnW
LJneYPx4fgyaRX8ah44GQPtPVMytOIyl4MMrXyWGaYR4wyqnuWFnvzWmd+71bMd5
jpvfuRqnbgQYGANQM21N2G7Zs3Z6NbiD5UfQLNlxgnTaPBjVQT1/F838ZeR91Dm8
8PLzF2juYTc3Sgyp8P4jkxl1mobzEMqeh+CpI2/YtbECgYEA1yZUeyYAy+3QVdDW
PcYP/AmTnL+3L5QSp9WrtuZ2kVhLFLgIo7aZOVGBz7s0RjPnH/bL/s+OLiXvAgIH
KZuC/H4Z2vrQcQX9E7rB1iBk2ZFxHl2gdzREG37wXdgKvI3YCicDRpulr+ZG7dA0
1k2vxWhvDm/eSGuEHt5JkC2REv0CgYEAxRtWTUMNMSWA8zN5eONYPZQ4GkuA0kEr
0q7p4a7zvR44Pf+g3QzBi3paugQSmQLcRTlDYBOp6LlODQji2V2VPtsD9FjduFjX
uuQ3ze/ZKnT3ECflO9VExohX2bUaxJGS4KqGAowChknCO4BoSygBrkijIWa7b+AU
gJM4QXiI0csCgYA3WWkKdXBnBjs+mIdFRRr/oAcVoEykNNfHzbRrTUbbhXdrUR0H
4QXyNQHMS0DbfqbLFlbMquDNBn1CavskvRkpk9da+oN9UCkXVkhfqd3ICx6qzTNm
908+M53qxpWchHE7y2WQWKJ7aiZ9L78oErxRcNiBQk5RGzfWKSGLse1MkQKBgQCd
4pfuq5cVlwUDymey/ejg6qlF5tT5llqUGKgfrxRumJZUkz830c/2+btS5ZBAIJpw
mL3vZ9DiKgzrRALyOpQiFS3FvKld0Ux81/Ibc9RwveBpgIuOsfa1UOGN8hPPAQy2
CeHuiFg9WTfMkb749MLj6CtDxha+NrA1jbeyOereoQKBgQCysqn3E91OkbpjguGE
EXU7t8/YhP/xohYw0I+hNNuGSFQuVihFd/iEqlhGelaSe10ap6PRurUgG3z2PcsX
wosAbh3TOHIRCUW5xaJ93vqys4/DrSPzoA4jHb0M2MP1EBM7OkMS+CntHsfj9trN
ypymj8/PSQTf9TC4KL55sXK34Q==
-----END PRIVATE KEY-----
"""

SSL_TEST_INTRODUCER_PUBLIC_CRT = b"""-----BEGIN CERTIFICATE-----
MIIDLDCCAhSgAwIBAgIUbJaDX38rnF2BylBTXCWNjn1E4kkwDQYJKoZIhvcNAQEL
BQAwRDENMAsGA1UECgwEQ2hpYTEQMA4GA1UEAwwHQ2hpYSBDQTEhMB8GA1UECwwY
T3JnYW5pYyBGYXJtaW5nIERpdmlzaW9uMCAXDTIyMDMyMjEwMjkyMVoYDzIxMDAw
ODAyMDAwMDAwWjBBMQ0wCwYDVQQDDARDaGlhMQ0wCwYDVQQKDARDaGlhMSEwHwYD
VQQLDBhPcmdhbmljIEZhcm1pbmcgRGl2aXNpb24wggEiMA0GCSqGSIb3DQEBAQUA
A4IBDwAwggEKAoIBAQDfTXQTHHDgCbBC8m1oybg5od+wH7Pfh4duI9m/I1JZLZoz
74GaQZlDG2bTHwwa3ccXDF5N3BbVG5BWGhFKquy37Od5mB88pDLngazumte0DaRC
MvM542TUwBVwLruT2jNDIPtXFZ5b7XMZh+dyLXHbvP9wyEUUBKcSi5kRgp02OYJC
g053dKazEAFtmOHoPNlCWlqqjfpMAXsbiFUBCoXmqYcyRBnNpzV1ET0nZC9W6Don
racpKDIvCGQPvZ6PL1iP/SLGx2n8QQ6y+MwRO+f4A+5dabTJHgLBQ6s3nL8ijPUU
V8jLUAkP4Yzrg127RqfHRolf644d3RqMyxGabOlPAgMBAAGjFzAVMBMGA1UdEQQM
MAqCCGNoaWEubmV0MA0GCSqGSIb3DQEBCwUAA4IBAQBKXvslWP38FdHCrH4uZq6C
r38iUHhM83Bd5PWOWpJLSepoDuAuV6FaLsDVqjQxI8M1sv6uLfBbfsCBZY6e61QM
vWI8vzDiCaUicntxozI02gSedAOyecUksADYkoL0xTPWlWHoD3EwASbwTC9Giip6
0A3Aja5mgDxB6vwRjhXs2hX0ERTJ0kmXG4As2gPhuqoXYKo5E2y+z8PkvEkjEeUx
laMTDrnaYZjfk1Vq5qED49CwAZljaIghe+Bad84JtEOckAEUteoCtsG7Th2/nQ9t
Qs81jLixhO1sYJmhoYxM8kwtv8/hC18u9qvKxZfqZfa178G3eePvbYNeS3LRlhg6
-----END CERTIFICATE-----
"""

SSL_TEST_INTRODUCER_PUBLIC_KEY = b"""-----BEGIN PRIVATE KEY-----
MIIEvAIBADANBgkqhkiG9w0BAQEFAASCBKYwggSiAgEAAoIBAQDfTXQTHHDgCbBC
8m1oybg5od+wH7Pfh4duI9m/I1JZLZoz74GaQZlDG2bTHwwa3ccXDF5N3BbVG5BW
GhFKquy37Od5mB88pDLngazumte0DaRCMvM542TUwBVwLruT2jNDIPtXFZ5b7XMZ
h+dyLXHbvP9wyEUUBKcSi5kRgp02OYJCg053dKazEAFtmOHoPNlCWlqqjfpMAXsb
iFUBCoXmqYcyRBnNpzV1ET0nZC9W6DonracpKDIvCGQPvZ6PL1iP/SLGx2n8QQ6y
+MwRO+f4A+5dabTJHgLBQ6s3nL8ijPUUV8jLUAkP4Yzrg127RqfHRolf644d3RqM
yxGabOlPAgMBAAECggEAPXeclAYoLAN+uW7yHv4n7/VXFawkX0t3RCIqNisK5/Fd
mR48lrGn9oj8bPEG6/5QZ0/IRbZnspG70XeretpB/v7/WME/F/o66O8RIz0MU0vO
A0rzGOQ3RTj6rb6vc6uEoN3bUcVpqfRa0pROaWeJB+umhO0b1r7RHpG+uMsza1E1
b/nrZs9H61Saj0IcZcjA9YRvevuwP7xRN/XJL/HCrkdYtqdyOI58Rs2TmHB5cj53
bHwlvy88zgObh+t18VYi3kx6TftpIT8Oft/0PEp9infCspffvw/1LrSBXyqo5MQx
CUFCgM6Q8nFyiQZi1trgyWfoCkBKpXo5ydrJChEQQQKBgQD8UxWV6hrVi39hfhQN
yjgHDKHcI1+Wcm9MxFp0oFvuqXU68r91JZtadMhz82aLnIC9+FQJC3PDaN2c4fVt
7slD4yR9hWCl4pqcC1cbEyV2C/zQW1AVdBiqKkaeJsAeM5aeKia61XVZbpsYGIDx
FR1zGH5xUJ3uhGJ+Wno2OeimywKBgQDijiV4g2+hxwELgMPlmgdzNqp1rmqDP3O+
HdzqoI4V0cfIIf/OUfvksHMY0AfUgWppwH+d9ImwxXrntenS5mLXpihU9UIcIUD1
sU2jbDm5tph4V1I9CLxnBsmCZi0A+/IOhZNQdPzVFD4ZLJFpZV7Lf1FwdyyhrLWK
UKz/ouYzDQKBgDQFzUWDZtTwVer725acQsDxUc3ZXTPflCL3uM6i4VFrjsgAlIjK
oCUePtXpMRNHySNht7HFsrBvRoG59Kgdu1FL25Illa+d8NKLZAIpCGg2QIGU0gYa
UZuD69tfkeyoJj2l4yZSLEesDj4Bj1QlTlUUj709KdKraMM0VE4p0lXRAoGAf0pK
d1mx4P2E8seYSWqvgOZYA+LJaZC/ITR6KUGoU04Yp7OinHOnyafyIyDPJXDJLz2+
9iqtKirqkUG+bIaRRoTO6F0cld2BOAo0ivuFu3iCVisJw80ivegsVB3Ab2sfZ1VZ
nbz9SWMkONS3prYT+tZAFaZ/5x64qUwGx2LpYAkCgYA3NbPLd4OmQhaANknb6QKL
BIBhiZzKHRiFkQ2KiYd2/lILEBnOmiYcjtWRmUdLMZidodpSpFbVNVc3U+BjEjgc
p0aVjmQpCXDRpWFQQ/Ak0XYeHECW0uwWKp5GuMkwks0dDCys4Z+Gf4kJSWmtu5OG
NR6RKo206k2HeqrAQC0L0A==
-----END PRIVATE KEY-----
"""

SSL_TEST_PRIVATE_CA_CERT_AND_KEY_1: tuple[bytes, bytes] = (SSL_TEST_PRIVATE_CA_CRT, SSL_TEST_PRIVATE_CA_KEY)

SSL_TEST_NODE_CERTS_AND_KEYS_1: dict[str, dict[str, dict[str, bytes]]] = {
    "full_node": {
        "private": {"crt": SSL_TEST_FULLNODE_PRIVATE_CRT, "key": SSL_TEST_FULLNODE_PRIVATE_KEY},
        "public": {"crt": SSL_TEST_FULLNODE_PUBLIC_CRT, "key": SSL_TEST_FULLNODE_PUBLIC_KEY},
    },
    "wallet": {
        "private": {"crt": SSL_TEST_WALLET_PRIVATE_CRT, "key": SSL_TEST_WALLET_PRIVATE_KEY},
        "public": {"crt": SSL_TEST_WALLET_PUBLIC_CRT, "key": SSL_TEST_WALLET_PUBLIC_KEY},
    },
    "farmer": {
        "private": {"crt": SSL_TEST_FARMER_PRIVATE_CRT, "key": SSL_TEST_FARMER_PRIVATE_KEY},
        "public": {"crt": SSL_TEST_FARMER_PUBLIC_CRT, "key": SSL_TEST_FARMER_PUBLIC_KEY},
    },
    "harvester": {
        "private": {"crt": SSL_TEST_HARVESTER_PRIVATE_CRT, "key": SSL_TEST_HARVESTER_PRIVATE_KEY},
    },
    "timelord": {
        "private": {"crt": SSL_TEST_TIMELORD_PRIVATE_CRT, "key": SSL_TEST_TIMELORD_PRIVATE_KEY},
        "public": {"crt": SSL_TEST_TIMELORD_PUBLIC_CRT, "key": SSL_TEST_TIMELORD_PUBLIC_KEY},
    },
    "crawler": {
        "private": {"crt": SSL_TEST_CRAWLER_PRIVATE_CRT, "key": SSL_TEST_CRAWLER_PRIVATE_KEY},
    },
    "daemon": {
        "private": {"crt": SSL_TEST_DAEMON_PRIVATE_CRT, "key": SSL_TEST_DAEMON_PRIVATE_KEY},
    },
    "introducer": {
        "public": {"crt": SSL_TEST_INTRODUCER_PUBLIC_CRT, "key": SSL_TEST_INTRODUCER_PUBLIC_KEY},
    },
}
