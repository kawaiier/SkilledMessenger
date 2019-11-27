from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa

private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
    backend=default_backend()
)

private_pem = private_key.private_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PrivateFormat.PKCS8,
    encryption_algorithm=serialization.BestAvailableEncryption(b'bestmessenger')
)

#print('Private pem: ' + str(private_pem))

for char in private_pem:
    print(chr(char), end='')

bytes_private_pem = b"""
-----BEGIN ENCRYPTED PRIVATE KEY-----
MIIFLTBXBgkqhkiG9w0BBQ0wSjApBgkqhkiG9w0BBQwwHAQI8OGwhBSDAbkCAggA
MAwGCCqGSIb3DQIJBQAwHQYJYIZIAWUDBAEqBBB93f6JsDIWHFMfGjyb1o1dBIIE
0CPTxQcsRY8POi/1ZII1zmp2++j7ES3RHsY2IWfboUW4QkROGM5cumKsRjfvCHsX
2VFVpNY0HjYvmFM3nxaWT1dvOIqI89qQKSvnDdY2xw/ba0/B9Or1F98J9NX+y/mR
JAX0m64+9C2gvfFQrpOjuTM4IBZOaXnjr3AwM0X9FkksBcRFHBD4EXrUJUi6prL9
urJ0UBqmZ965BM1JBCtOM31zPBvlfVd/1mO1v2OVfjRD6XX6SMRxbLd++u6pYF5A
odm6mB1Vo56Xdh5x+hYPIJ5z90bj3M2ijxlt4NMKzRpjhP3QaXkHnMExziTRKG5Z
kOLIiG3g1FyqRDOajLvNKE6cOlTpFai+GxSIE+Z9k1jGJhKz7ZIyyek1e99oGyfq
cqdTKkt/W3rZhyoyqyrYNrazzSIj8lmtCW92pOMpEmgx5D7fIPzS9agkyiQNLWJ/
cEQaknv9pPk6lhT04TbdCC0ff89iFGoHLY7dmza6YzmGWvdyjGGCTe8Nv2mxMFaw
/kCKJB1Das5EZVKD0YvtIBB/2dC/VkiXWoku19WJUx4yxytKlHf/6Pat+GgOqfi3
BAVpmRj063QFUP6W/o4Bam21iChN5oXqDAxpDOTl9fxbINeYYsw90OdzJmQa446B
Bp/e/HRCMOb0dwjXm596Sq3wTBeaKt8rD5se8esNrcC8qukxfY5pr9/ABiSXe7sA
jCwOPryFv5AbsMGf4sYkv0qBjX+P2RCElX2eu1SAzh6g2mERtFg4XpukIuNsoh/t
GafTWemiQaJQ7RFTDo94Ibx8gIhwMQokkNTPUCh426aGHyiIA7Xw2hFp+U2rnT50
CkF5LwBa/8j09/dqkVMy3wv6V9LPOMBQmWG4NeyA66BQHtZ2mTqQVE91sXnmsjCo
pUnj9D3nA/zVBeOdnoRMGIEr6MOgS3TL0OT91gfD6928BXH7zWf6uZRYxbv0Oow+
KN4cvAMd7biQy248uID7X0bQbJ067OOJWAxcDaItBlJsBGiTDHOE4m6UJCb6EuLI
8FI1OSYNRkTMaD9SO1ahGOae+fYae2dyeyLu6fRP/oUa0Q5DXL2EskvK+iv2XmtR
lchXFQMvNwF0qgq3D9ytViZuL42yue++WIG/CEiIG2QXKMc7zYyFYCWrW3AxslSc
hf4rpxsCML+SnoEzJg6WoDqepecI0sK+OHLsU7mRqAGoXehEba4/QHbXWnhlHc4h
0ORUuEzyRINnuc/mC1Ap3SwxDe55PQbkaRZppQPZr41Ya8CdPjI8Sy+3RwT7waKh
4sY3+hVwal5ooRzwwiCa1WtLc/CvysP0zyQ4tA0q2hRcEraMtq0uRSUGj2ObEHDF
QwcpvdEeOi1I/n/cZpEZ5HaQo9RVZj/o3GK20u0BIV3KwehA6dpP5CcPB59MKI1t
eOCSTCZ9BjKodijQR/+7eveJCJ62E1rUUFsKAOkzYAxdYU/r8vzsTYdsPVigjPPv
0W8Xg8fBTSBbsPEeDiWOMnWBFCOIxCWl7itc0nzIuIwB2QydXVfKLKxbr4WgsQpX
+35gYDhAlFBJlA+wi6EyDjlkZoC6BB2wpxOIJEnT03+Hf8Q8dAAxDhAlPA5lp1J+
QHH6eLQG2u8ucn+Wr82/BBk09+WUZE1X87cgo6xLrnvk
-----END ENCRYPTED PRIVATE KEY-----
"""

loaded_private_key = serialization.load_pem_private_key(
    bytes_private_pem,
    password=b'bestmessenger',
    backend=default_backend()
)

#print('Private pem: ' + str(loaded_private_key))

public_key = private_key.public_key()

public_pem = public_key.public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo
)

#print('Public pem: ' + str(public_pem))

for char in public_pem:
    print(chr(char), end='')

bytes_public_pem = b"""
-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAmYiDpFTxp/k5x6+7aXaf
bnlN7kP4EM2+wUZ/D3bE4rUB4oASixuQhuM4/H3q4+2WlPlXDc4gytSFPR3OGhoE
e3ajKZowfkSiPHWos237AzTNoTd4vyfXApheX/AEM8aqCMeIfdSjzL+92HUFWDvn
f5r7UrG8rZjdD9xudKlk56O2U5717uFZAMvQ8Mg5/owzOEYhTmOQ+DRqZp9ATwwt
8fAw4ZjNqYcR+SW6p7zclPkg+f9+VittW4uiM6OW8cMqEIgG84dLlpfoGhQ+0rfE
he6NHPYyISCQGSAanc1957NWcKaDCUqgW4Y3frem+JhqP/JmBAhE9OrJTnt13HjI
cwIDAQAB
-----END PUBLIC KEY-----
"""

loaded_public_key = serialization.load_pem_public_key(
    bytes_public_pem,
    backend=default_backend()
)
