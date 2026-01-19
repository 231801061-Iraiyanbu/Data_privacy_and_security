import pyotp, qrcode
secret =pyotp.random_base32() 
totp =pyotp.TOTP(secret)
uri = totp.provisioning_uri(name="student@example.com",
issuer_name="AD23631-MFA-Lab")
qrcode.make(uri).save("totp-qr.png")
print("Secret:",secret)

import qrcode
qr = qrcode.QRCode()
qr.add_data(uri)
qr.make()
qr.print_ascii(invert=True)


import time
MAX_ATTEMPTS = 3
attempts = 0
while attempts < MAX_ATTEMPTS:
    code = input("Enter the 6-digit code: ")
    if totp.verify(code, valid_window=1):  # allows +/-30s drift
        print("Authentication Successful")
        break
    attempts += 1
    print("Invalid code. Attempts left:", MAX_ATTEMPTS - attempts)
else:
    print("Too many failures — account locked, alert security team")

