import hashlib


class EncryptError(Exception):
    pass


def encrypt(string, method='SHA256'):
    if method.upper() == 'SHA256':
        hash_string = hashlib.sha256()
    else:
        print(EncryptError('Only SHA256 currently.'))
        return False

    hash_string.update(string.encode())
    return hash_string.hexdigest()


if __name__ == '__main__':
    pass
