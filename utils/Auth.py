import pyotp


def get_2FA(key):
    GAuth = pyotp.TOTP(key)
    return GAuth.now()


if __name__ == '__main__':
    pass
