import hashlib
import time

import requests
from urllib.parse import urlencode

from get_sixflurls import get_sixflurl


def encryption(s):
    re_md5 = None
    try:
        md = hashlib.md5()
        md.update(s.encode())
        re_md5 = md.hexdigest()
    except Exception as e:
        print(e)

    return re_md5.upper()


def json_to_url_params(data):
    params = urlencode(data)
    return params

url = "https://api22-normal-c-useast1a.tiktokv.com/tiktok/v1/addyours/invite"

_rticket = str(time.time() * 1000).split(".")[0]
ts = str(int(time.time()))
query = {
    "iid": "7413950845966419717",
    "device_id": "7387066460868593195",
    "ac": "WIFI",
    "channel": "googleplay",
    "aid": "1233",
    "app_name": "musical_ly",
    "version_code": "360404",
    "version_name": "36.4.4",
    "device_platform": "android",
    "os": "android",
    "ab_version": "36.4.4",
    "ssmix": "a",
    "device_type": "Pixel 3",
    "device_brand": "google",
    "language": "en",
    "os_api": "31",
    "os_version": "12",
    "openudid": "b2f1d524d3aea23f",
    "manifest_version_code": "2023604040",
    "resolution": "1080*2028",
    "dpi": "440",
    "update_version_code": "2023604040",
    "_rticket": _rticket,
    "is_pad": "0",
    "current_region": "JP",
    "app_type": "normal",
    "sys_region": "US",
    "last_install_time": "1726199719",
    "timezone_name": "America/Los_Angeles",
    "residence": "JP",
    "app_language": "en",
    "ac2": "wifi5g",
    "uoo": "0",
    "op_region": "JP",
    "timezone_offset": "-28800",
    "build_number": "36.4.4",
    "host_abi": "armeabi-v8a",
    "locale": "en",
    "region": "US",
    "content_language": "es,",
    "ts": ts,
    "cdid": "619b414a-f1ea-4f1c-a8ef-5e7dbb5de495"
}


payload = {
    "invitees": "7045273197155533871",
    "topic_id": "7259786833683731461",
    "item_id": "7413884927676026120"
}

STUB = encryption(json_to_url_params(payload)).upper()
TICKET = str(time.time() * 1000).split(".")[0]
headers = {
    "rpc-persist-pyxis-policy-v-tnc": "1",
    "x-ss-stub": STUB,
    "accept-encoding": "gzip",
    "x-tt-app-init-region": "carrierregion=;mccmnc=;sysregion=US;appregion=US",
    "x-tt-request-tag": "n=0",
    "x-tt-pba-enable": "1",
    "x-metasec-event-source": "native",
    "x-bd-kmsv": "0",
    "x-tt-dm-status": "login=1;ct=1;rt=1",
    "X-SS-REQ-TICKET": TICKET,
    "x-bd-client-key": "#f2TW3EA00mhtd+SoXXIaKOixCzWO+SI8uT7DtIkvH9dYqLT6TlkfRWx2m6cBQzdhd9JSEF9oY/Jrmyrr",
    "x-metasec-pns-event-id": "4aee5e68-1294-4287-9d73-5eeea3f98f61",
    "tt-ticket-guard-public-key": "BDEJGI8P8K678lplo6Ap0w1dqgq2J+Ymy16KJkipTJ3/ULHerny2Fcn1uOQ06PjoQEZmdtiJ3mYK3ncNeqlBV5w=",
    "sdk-version": "2",
    "tt-ticket-guard-iteration-version": "0",
    "tt-ticket-guard-client-data": "eyJyZXFfY29udGVudCI6InRpY2tldCxwYXRoLHRpbWVzdGFtcCIsInJlcV9zaWduIjoiTUVVQ0lRRGhkWjR0QlpmUUFYVFozd2o4eDBHaVRSWFdCdUZ4Ry91cVl6YzB5L3FwUFFJZ1gwejdzZCtTUmthcGdsWlZIUmZ3YWsvWkpnNWxYck9XdmoxKzJNV21QdGNcdTAwM2QiLCJ0aW1lc3RhbXAiOjE3MjYyMDAwNTAsInRzX3NpZ24iOiJ0cy4xLjU0Y2UyMzYxZmFmNWU0MWFjNGI3ZmEwZmNhMDQyOGFlMDI5ZGUxMzQ3MGYwNmQxMjY4OWVkZWMwMTU1YWMwMTkwZTcwYjRiZGE4MmMxMzgzNmU1Y2ZhMTgzOTRkNzAyNDBmOGFmMTYzMWYxNjVhZTk2MDEyMmVlZmZkNDUzM2RkIn0=",
    "x-tt-token": "",
    "tt-ticket-guard-version": "3",
    "passport-sdk-version": "6030790",
    "x-vc-bdturing-sdk-version": "2.3.8.i18n",
    "x-tt-store-region": "mx",
    "x-tt-store-region-src": "uid",
    "user-agent": "com.zhiliaoapp.musically/2023604040 (Linux; U; Android 12; en; Pixel 3; Build/SP1A.210812.016.C2;tt-ok/3.12.13.4-tiktok)",
    "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
    "host": "api22-normal-c-useast1a.tiktokv.com",
    "connection": "Keep-Alive",
    "cookie": "sessionid=8254efa57feffd8cdea845e2ff0d2ec3; sessionid_ss=8254efa57feffd8cdea845e2ff0d2ec3;"
}


sign_headers, sign_urls = get_sixflurl(api=url, params=query, data=payload, header=headers, platform="tiktok")


toUserProxy = "127.0.0.1:7890"
proxies = {
'http': 'http://{}'.format(toUserProxy),
'https': 'http://{}'.format(toUserProxy)
}

response = requests.post(sign_urls, data=payload, headers=sign_headers, proxies=proxies)

print(response.text)
