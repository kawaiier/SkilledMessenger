from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding

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
MIIFLTBXBgkqhkiG9w0BBQ0wSjApBgkqhkiG9w0BBQwwHAQIUbLn4YoBeYgCAggA
MAwGCCqGSIb3DQIJBQAwHQYJYIZIAWUDBAEqBBCL87wS822SvvuxBlS8QsFdBIIE
0MIJFRE7yJYZrObhjY1ntvBpgBvY4X7I9irMCuQiMDnF9pzizBjMBdvfCPcgMZXa
nv9OKkiOcrfk+cMTRfTCi0jYIvOLwIiX0JmMeloE6xml6OZIcZbJdclpbqYXIeS/
dALMyEhUTrc6zA/MR337Bo5zFD+WJdtLCwhWeKK4IjoHxJws9JPlEhDw3Zm0ihrp
WgM2RMEpGNPO3p2301syai1bY12x3WxvQyGJHhl8rdDHfpi2s3M4qW7aBQ5GWAVb
l7vsTJCUaBj44wDF2fDyA5XsjvQoYQWZ8MdbA9QI8zzWrLkr7TBqw22O57JYpx7q
y4dXcr4+3+15daQ0fuhsVcfRJEH+l7GS3Bx0tB5/nwhsvYwbHZ2SB90JlwPYnEbR
kiTs8hZm4mAooxXGfs4pF+l3OL6fcaMzXiJlOj0YsY1aWnXRArB3z3NPT4T1iq2a
u6osLd95Rg2OFD2SKSpMwW4GgQaRivA11CUuOZ1SoNXOmgaiDTU/vFMQ5cOV6HCN
kz0XoOHx5i0RM4q/thId0rZLGTIsEZxM4imYwllxSljczoGV4bgimG/lIn5uMGrl
KEhNyUjhsGDpedvKbpKm7KH90ckfA2aj8Om1G+fyR0Et7Y7qk3tgHKSJv1IzI6/V
uimtl0MUmn+EFDp+xi6QSHc0JQxcHzJBDp2/OCJc8hhFAWyFRv1G1IuJzk4u62Xq
9NNoymLG9bE/0jL/YOVdT/IxbAkTr4fNYNrHZqD8Y8HiAL/ri+x1WagY2PqwkLl2
xBWK79IFB93UfILEILTeO9x4zc7NQeu9bwOkmbwj7laP6WmnLgxnhAVgU6WZ58iV
gS+nLZTraqIYgTWkbmtuD0XmCWgimicF4Levcy2TiYm54t4EqEXJCfitYUfIYuF4
gzfD3zI9dkswLAemBCGCY1x4AMxoWsLSjyZ4MgKle+ctYUsaudQXOcu9Cp+x+TEW
nfNKWhCqrStI7FyGTM8Fvf0mnu6EjT9YSZA+ehZPS3SCjzDmYmSShNUo5WxnVox6
k/9jDu5lfAV5dZDxZATap1SfVnlXE+oHoAlI4aVIRV1rA3HY9YW9Lvpoa9XRdqov
7OLkq43aHAyCiL+OT+uHCZGMKx711N5MRVxSg/bH8qS51Q4/F3sDoM5QPYC85UaG
R1D3NA2u0BvQWweJ7xuM/k/dwz3hXfokAftH9jy/GcsbOTKq0I8VaE0svM9LeSeY
r2Lw3vTWGLd6llitymPbdIOhLCUfUrn9ZNe1JUEUtiAbcNfspoq6fWJoarIN3Fdg
DE1rguszmTrq8Mj9NXK7EZ71LzUm238+gT/A/O8kpCvl6b/9XihqBzeQv6FA+Fk6
5FRMtlXpf9w5tO1nvxxPFIcH5m6iMd4oUp/mPdeTW1DQ0hYQ3V+vW3Vw00M/Ca9J
JnCqjA9e0kt1pcA4NhSMBl/wBZydpAuKemX2QdtSgaP/G8cHGH3i3ff4FH93tA0J
DxgZAhCMxplk2oZWPU2QdTjgLdlrfUrTk0ANzivJnbVX4Aweosm4+MymUJdQEH7k
zqzt+g2L4xcw3TgCxe03ssw6S77rOd86CuxjckMncokKqLxX6pNMlVT3hZkHparZ
Fp37ziYQQfuOfjYdx24q1ppySSv8UU8YX9xmV84BJkk9
-----END ENCRYPTED PRIVATE KEY-----
"""

loaded_private_key = serialization.load_pem_private_key(
    bytes_private_pem,
    password=b'bestmessenger',
    backend=default_backend()
)

message = b"A message I want to sign"
signature = loaded_private_key.sign(
    message,
    padding.PSS(
        mgf=padding.MGF1(hashes.SHA256()),
        salt_length=padding.PSS.MAX_LENGTH
    ),
    hashes.SHA256()
)

#print('Signature: ' + signature)

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
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA2FFIfmrJDYJi7UZRXnd1
cCwidyA9JIxUecqMmIhdJGtSfdoXDCvLiiyJc/zMml0DAw9bD7Lu8tDqHHLTM4mo
2A/6Y8WkYdYSz5VNKSjWqm8TEFbMoWbUGrg32o0tQwJvO+kl0dnTnoGzJKr9GwZI
gfvbiqZHDALPt/QBk/Rn6PfI4QUpfdkSuEVGUKlHSM8sRfUQjgFKrubRBl1U2P1T
JReVChDe637UEaD6+v9Otn0cwdDPdw4AhVCf0xkMQAtzON58xPfk1MKSuw57ymjw
FBF3fC5wIkTGmOYJWdaNtxnnIKTXSIhOBWUVkGeHhE7RBHHSaH1fjs4XhD3+BK11
GwIDAQAB
-----END PUBLIC KEY-----
"""

loaded_public_key = serialization.load_pem_public_key(
    bytes_public_pem,
    backend=default_backend()
)

try:
    loaded_public_key.verify(
        signature,
        message,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )

    ciphertext = loaded_public_key.encrypt(
        message,
        padding.OAEP(
            mgf = padding.MGF1(algorithm=hashes.SHA256()),
            algorithm = hashes.SHA256(),
            label = None
        )
    )

    #print(ciphertext)
except:
    print('Invalid signature')

plaintext = loaded_private_key.decrypt(
    ciphertext,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)
plaintext == message
print(plaintext)