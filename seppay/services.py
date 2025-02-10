import uuid

import requests

from .utils import get_seppy_terminal_id, make_request, get_seppy_base_domain, make_sec_string


def get_payment_link(amount: int, redirect_url: str, phone_number: str, res_number: str = None):
    terminal_id = get_seppy_terminal_id()
    _base_domain = get_seppy_base_domain()

    sec, secval = make_sec_string()

    if res_number and len(phone_number) < 6:
        raise Exception("Phone number must be at least 6 characters")
    if not res_number:
        res_number = uuid.uuid4().hex
    if not _base_domain:
        _base_domain = "sep.shaparak.ir"

    _json = {
        "action": "token",
        "TerminalId": terminal_id,
        "Amount": amount,
        "ResNum": res_number,
        "RedirectUrl": redirect_url,
        "CellNumber": phone_number
    }
    if sec and secval:
        _json["secval"] = secval
        _json["sec"] = sec

    try:
        res = make_request('post', f"https://{_base_domain}/onlinepg/onlinepg", json=_json)
    except requests.RequestException as e:
        raise e
    if res.status_code != 200:
        raise Exception(res.text)
    data = res.json()

    _status = data['status']
    _token = None

    if int(_status) == 1:
        token = data['token']
        return {
            "status": int(_status),
            "url": f'https://sep.shaparak.ir/OnlinePG/SendToken?token=' + token,
            "ref": res_number,
            "errorDesc": None,
            "errorCode": None,
        }
    return {
        "status": int(_status),
        "url": None,
        "ref": res_number,
        "errorDesc": data.get("errorDesc", None),
        "errorCode": data.get('errorCode', None)
    }


def verify_transaction(ref_number: str):
    terminal_id = get_seppy_terminal_id()
    _base_domain = get_seppy_base_domain()

    sec, secval = make_sec_string()

    if not _base_domain:
        _base_domain = "sep.shaparak.ir"

    _json = {
        "RefNum": ref_number,
        "TerminalNumber": terminal_id,
    }
    if sec and secval:
        _json["secval"] = secval
        _json["sec"] = sec

    try:
        res = make_request('post', f"https://{_base_domain}/verifyTxnRandomSessionkey/ipg/VerifyTransaction",
                           json=_json)
    except requests.RequestException as e:
        raise e
    if res.status_code != 200:
        raise Exception(res.text)
    data = res.json()

    _status = data['Success']
    _result_code = data.get('ResultCode', None)
    if not _result_code:
        return False, 'Could not find result code in response.'

    if _status and _result_code == 0:
        return True, None
    else:
        if _result_code == -2:
            return False, 'Transaction not found.'
        elif _result_code == -6:
            return False, 'More than 30 minutes passed.'
        elif _result_code == 2:
            return False, 'It is a duplicate request.'
        elif _result_code == 5:
            return False, 'Transaction is reversed.'
        elif _result_code == -104:
            return False, 'TerminalID is disabled.'
        elif _result_code == -105:
            return False, 'TerminalID is invalid.'
        elif _result_code == -106:
            return False, 'IP address is invalid.'
        else:
            return False, 'Unknown result code'


def reverse_transaction(ref_number: str):
    terminal_id = get_seppy_terminal_id()
    _base_domain = get_seppy_base_domain()

    sec, secval = make_sec_string()

    if not _base_domain:
        _base_domain = "sep.shaparak.ir"

    _json = {
        "RefNum": ref_number,
        "TerminalNumber": terminal_id,
    }
    if sec and secval:
        _json["secval"] = secval
        _json["sec"] = sec
    try:
        res = make_request('post', f"https://{_base_domain}/verifyTxnRandomSessionkey/ipg/ReverseTransaction",
                           json=_json)
    except requests.RequestException as e:
        raise e
    if res.status_code != 200:
        raise Exception(res.text)
    data = res.json()

    _status = data['Success']
    _result_code = data.get('ResultCode', None)
    if not _result_code:
        return False, 'Could not find result code in response.'

    if _status and _result_code == 0:
        return True, None
    else:
        if _result_code == 2:
            return False, 'It is a duplicate request.'
        elif _result_code == -104:
            return False, 'TerminalID is disabled.'
        elif _result_code == -105:
            return False, 'TerminalID is invalid.'
        elif _result_code == -106:
            return False, 'IP address is invalid.'
        else:
            return False, 'Unknown result code'
