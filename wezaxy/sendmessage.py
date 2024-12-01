import requests
import uuid

import time
from urllib.parse import quote

def mesj(
    token,
    user_id,
    device_id,
    text,
    user_ids,
    thread_id,
    item_id,
    timestamp=None
):
    
    if timestamp is None:
        timestamp = int(time.time())

    headers = {
        "Authorization": token,
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Host": "i.instagram.com",
        "IG-INTENDED-USER-ID": user_id,
        "IG-U-DS-USER-ID": user_id,
        "IG-U-IG-DIRECT-REGION-HINT": f"CLN,{user_id},{timestamp}:dummy",
        "IG-U-SHBID": f"dummy,{user_id},{timestamp}:dummy",
        "IG-U-SHBTS": f"dummy,{user_id},{timestamp}:dummy",
        "Priority": "u=3",
        "User-Agent": "Instagram 342.0.0.33.103 Android (31/12; 454dpi; 1080x2254; Xiaomi/Redmi; Redmi Note 9 Pro; joyeuse; qcom; tr_TR; 627400398)",
        "X-Bloks-Is-Layout-RTL": "false",
        "X-Bloks-Is-Prism-Enabled": "true",
        "X-Bloks-Prism-Button-Version": "CONTROL",
        "X-Bloks-Prism-Colors-Enabled": "true",
        "X-Bloks-Prism-Font-Enabled": "false",
        "X-Bloks-Version-Id": "dummy",
        "X-FB-Connection-Type": "WIFI",
        "X-FB-HTTP-Engine": "Tigon-HUC-Fallback",
        "X-FB-Network-Properties": "dummy",
        "X-IG-Android-ID": device_id,
        "X-IG-App-ID": "567067343352427",
        "X-IG-App-Locale": "tr_TR",
        "X-IG-Bandwidth-Speed-KBPS": "1934.000",
        "X-IG-Bandwidth-TotalBytes-B": "1375348",
        "X-IG-Bandwidth-TotalTime-MS": "785",
        "X-IG-Capabilities": "3brTv10=",
        "X-IG-CLIENT-ENDPOINT": "DirectThreadFragment:direct_thread",
        "X-IG-Connection-Type": "WIFI",
        "X-IG-Device-ID": device_id,
        "X-IG-Device-Locale": "tr_TR",
        "X-IG-Family-Device-ID": "dummy",
        "X-IG-Mapped-Locale": "tr_TR",
        "X-IG-Nav-Chain": "dummy",
        "X-IG-SALT-IDS": "dummy",
        "X-IG-SALT-LOGGER-IDS": "dummy",
        "X-IG-Timezone-Offset": "10800",
        "X-IG-WWW-Claim": "dummy",
        "X-MID": "dummy",
        "X-Pigeon-Rawclienttime": str(timestamp),
        "X-Pigeon-Session-Id": f"dummy-{uuid.uuid4()}"
    }

    data = (
        f"is_written_with_ai=0&action=send_item&is_x_transport_forward=false&is_shh_mode=0"
        f"&send_silently=false&send_attribution=inbox"
        f"&client_context={timestamp}&text={quote(text)}&device_id={device_id}"
        f"&mutation_token={timestamp}&_uuid={device_id}&btt_dual_send=false"
        f"&nav_chain=dummy&is_ae_dual_send=false&offline_threading_id={timestamp}"
        f"&recipient_users={quote(str([[int(uid) for uid in user_ids]]))}"
        f"&thread_id={thread_id}&item_id={item_id}"
    )

    response = requests.post("https://i.instagram.com/api/v1/direct_v2/threads/broadcast/text/", data=data, headers=headers).text
    print(response)


