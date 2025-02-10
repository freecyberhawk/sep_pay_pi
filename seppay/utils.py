import uuid

import requests
from django.conf import settings
from django.core.exceptions import ImproperlyConfigured
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes
import base64
from cryptography.hazmat.primitives.serialization import load_pem_private_key


def get_seppy_terminal_id():
    try:
        sti = settings.SEPPY_TERMINAL_ID
        assert type(sti) is str
        return sti
    except AttributeError:
        raise ImproperlyConfigured("SEPPY_TERMINAL_ID is not set in settings.py!")
    except AssertionError:
        raise ImproperlyConfigured("SEPPY_TERMINAL_ID is not string!")


def make_request(method, url, **kwargs):
    response = getattr(requests, method)(url, **kwargs)
    response.raise_for_status()
    return response


def get_seppy_base_domain():
    try:
        sti = settings.SEPPY_BASE_DOMAIN
        assert type(sti) is str
        return sti
    except AttributeError:
        raise ImproperlyConfigured("SEPPY_BASE_DOMAIN is not set in settings.py!")
    except AssertionError:
        raise ImproperlyConfigured("SEPPY_BASE_DOMAIN is not string!")


def get_seppy_private_key_address():
    try:
        sti = settings.SEPPY_PRIVATE_KEY_ADDRESS
        assert isinstance(sti, str)
        return sti
    except (AttributeError, AssertionError):
        return None


def sign_string(private_key, data):
    signature = private_key.sign(
        data.encode(),
        padding.PKCS1v15(),
        hashes.SHA256()
    )
    _signature = base64.b64encode(signature).decode('utf-8')
    return _signature


def make_sec_string():
    _private_key_address = get_seppy_private_key_address()
    sec = None
    secval = None
    if _private_key_address:
        try:
            with open(_private_key_address, 'r') as key_file:
                private_key = key_file.read()
                private_key_pem = load_pem_private_key(private_key.encode(), password=None)
                secval = str(uuid.uuid4().hex)
                sec = sign_string(private_key_pem, secval)
        except FileNotFoundError:
            print(f"File not found at: {_private_key_address}")
        except Exception as e:
            print(f"An error occurred while reading the private key file: {e}")
    else:
        print("Private key address is not set.")
    return sec, secval
