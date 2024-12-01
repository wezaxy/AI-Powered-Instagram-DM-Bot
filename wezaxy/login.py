import requests,json
import base64
import time
import random,uuid
import string
import secrets
from Cryptodome.Cipher import AES, PKCS1_v1_5
from Cryptodome.PublicKey import RSA
from Cryptodome.Random import get_random_bytes
cookie = secrets.token_hex(8)*2
from user_agent import generate_user_agent
def generate_jazoest(symbols: str) -> str:
    amount = sum(ord(s) for s in symbols)
    return f"2{amount}"

def gen_token(size=10, symbols=False) -> str:
    """Generate CSRF or other token."""
    chars = string.ascii_letters + string.digits
    if symbols:
        chars += string.punctuation
    return "".join(random.choice(chars) for _ in range(size))

def enc(pw):
    pki, pk = get_pks()
    sk = get_random_bytes(32)
    iv = get_random_bytes(12)
    ts = str(int(time.time()))
    dpk = base64.b64decode(pk.encode())
    rk = RSA.import_key(dpk)
    cr = PKCS1_v1_5.new(rk)
    re = cr.encrypt(sk)
    ca = AES.new(sk, AES.MODE_GCM, iv)
    ca.update(ts.encode())
    ae, tg = ca.encrypt_and_digest(pw.encode("utf8"))
    sb = len(re).to_bytes(2, byteorder="little")
    pl = base64.b64encode(
        b"".join(
            [
                b"\x01",
                pki.to_bytes(1, byteorder="big"),
                iv,
                sb,
                re,
                tg,
                ae,
            ]
        )
    )
    return f"#PWD_INSTAGRAM:4:{ts}:{pl.decode()}"

def get_pks():
        resp = requests.get("https://i.instagram.com/api/v1/qe/sync/",verify=False)
        publickeyid = int(resp.headers.get("ig-set-password-encryption-key-id"))
        publickey = resp.headers.get("ig-set-password-encryption-pub-key")
        return publickeyid, publickey


def login(username: str, password: str):

    r = requests.session()


    enc_password = enc(password)
    data = {"jazoest": "22565","country_codes": "[{\"country_code\":\"1\",\"source\":[\"default\"]}]","phone_id": "6ee4b60f-ca75-4412-ad1e-cd5ba98e874a","enc_password": enc_password,"username": username,"adid": "8c68106b-25ae-4657-9dd7-f4877d728c4a","guid": "ffbbe586-a8c6-4b3d-b55b-898c86ce0025","device_id": "android-a3b32e4e9a655927","google_tokens": "[]","login_attempt_count": "0"}


    timestamp = int(time.time())
    headers = {"Host": "i.instagram.com","Accept": "*/*","X-IG-App-Locale": "en_US","X-IG-Device-Locale": "en_US","X-IG-Mapped-Locale": "en_US","X-Pigeon-Session-Id": "UFS-68326ae0-7772-4e21-92c1-5bcbaa601370-1","X-Pigeon-Rawclienttime": str(timestamp),"X-IG-Bandwidth-Speed-KBPS": "2880.01","X-IG-Bandwidth-TotalBytes-B": "82172548","X-IG-Bandwidth-TotalTime-MS": "3917","X-IG-App-Startup-Country": "US","X-Bloks-Version-Id": "ce555e5500576acd8e84a66018f54a05720f2dce29f0bb5a1f97f0c10d6fac48","X-IG-WWW-Claim": "0","X-Bloks-Is-Layout-RTL": "false","X-Bloks-Is-Panorama-Enabled": "true","X-IG-Device-ID": "ffbbe586-a8c6-4b3d-b55b-898c86ce0025","X-IG-Family-Device-ID": "6ee4b60f-ca75-4412-ad1e-cd5ba98e874a","X-IG-Android-ID": "android-a3b32e4e9a655927","X-IG-Timezone-Offset": "-14400","X-IG-Connection-Type": "WIFI","X-IG-Capabilities": "3brTvx0=","X-IG-App-ID": "567067343352427","Priority": "u=3","User-Agent": "Instagram 269.0.0.18.75 Android (26/8.0.0; 480dpi; 1080x1920; OnePlus; 6T Dev; devitron; qcom; en_US; 314665256)","Accept-Language": "en-US","X-MID": "Zubi8QABAAH3mzXqiwAsBoWjRlKM","X-FB-HTTP-Engine": "Liger","Connection": "keep-alive","X-FB-Client-IP": "True","X-FB-Server-Cluster": "True","IG-INTENDED-USER-ID": "0","X-IG-Nav-Chain": "9MV:self_profile:2,ProfileMediaTabFragment:self_profile:3,9Xf:self_following:4","X-IG-SALT-IDS": "1061223170","Authorization": "","Content-Type": "application/x-www-form-urlencoded; charset=UTF-8","Accept-Encoding": "gzip, deflate"}


    try:
        res = r.post("https://i.instagram.com/api/v1/accounts/login/", data=data, headers=headers, verify=False)
        print(res.headers.get('ig-set-authorization'))
        
        if res.status_code == 200:
            print("Login successful")
            return [True,res.headers.get('ig-set-authorization'),res.json().get("logged_in_user", {}).get("pk")]
        else:
            print(f"Login failed: {res.text}")
            return [False]
    except requests.exceptions.RequestException as e:
        print(e)
        return [False]


