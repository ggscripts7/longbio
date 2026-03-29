"""

"""
import requests
import json
from flask import Flask, request, jsonify, render_template
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import os
from typing import Optional
from urllib.parse import urlparse

KEY = bytes([89, 103, 38, 116, 99, 37, 68, 69, 117, 104, 54, 37, 90, 99, 94, 56])
IV = bytes([54, 111, 121, 90, 68, 114, 50, 50, 69, 51, 121, 99, 104, 106, 77, 37])
FREEFIRE_VERSION = "OB52"

REGION_TO_BASE_URL = {
    'IND': "https://client.ind.freefiremobile.com",
    'BR': "https://client.us.freefiremobile.com",
    'US': "https://client.us.freefiremobile.com",
    'SAC': "https://client.us.freefiremobile.com",
    'NA': "https://client.us.freefiremobile.com",
}
ENDPOINT_PATH = "/UpdateSocialBasicInfo"
DEFAULT_BASE_URL = "https://clientbp.ggblueshark.com"

def get_full_url(region: Optional[str]) -> str:
    region_code = region.upper() if region else None
    base_url = REGION_TO_BASE_URL.get(region_code, DEFAULT_BASE_URL)
    return base_url + ENDPOINT_PATH

from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# ============================================================================
# PROTOBUF DESCRIPTOR
# ============================================================================
try:
    _sym_db = _symbol_database.Default()
    DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\ndata.proto\"\xbb\x01\n\x04\x44\x61ta\x12\x0f\n\x07\x66ield_2\x18\x02 \x01(\x05\x12\x1e\n\x07\x66ield_5\x18\x05 \x01(\x0b\x32\r.EmptyMessage\x12\x1e\n\x07\x66ield_6\x18\x06 \x01(\x0b\x32\r.EmptyMessage\x12\x0f\n\x07\x66ield_8\x18\x08 \x01(\t\x12\x0f\n\x07\x66ield_9\x18\t \x01(\x05\x12\x1f\n\x08\x66ield_11\x18\x0b \x01(\x0b\x32\r.EmptyMessage\x12\x1f\n\x08\x66ield_12\x18\x0c \x01(\x0b\x32\r.EmptyMessage\"\x0e\n\x0c\x45mptyMessageb\x06proto3')
    _globals = globals()
    _builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
    _builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'data1_pb2', _globals)

    if _descriptor._USE_C_DESCRIPTORS == False:
        DESCRIPTOR._options = None
        _globals['_DATA']._serialized_start = 15
        _globals['_DATA']._serialized_end = 202
        _globals['_EMPTYMESSAGE']._serialized_start = 204
        _globals['_EMPTYMESSAGE']._serialized_end = 218

    Data = _sym_db.GetSymbol('Data')
    EmptyMessage = _sym_db.GetSymbol('EmptyMessage')
except Exception as e:
    print(f"Error initializing Protobuf: {e}")

# ============================================================================
# UPDATE BIO REQUEST
# ============================================================================
def update_bio_request(url: str, token: str, bio_text: str) -> dict:
    api_hostname = urlparse(url).netloc
    truncated_bio = (bio_text[:50] + "...") if len(bio_text) > 50 else bio_text

    try:
        data = Data()
        data.field_2 = 17
        data.field_5.CopyFrom(EmptyMessage())
        data.field_6.CopyFrom(EmptyMessage())
        data.field_8 = bio_text
        data.field_9 = 1
        data.field_11.CopyFrom(EmptyMessage())
        data.field_12.CopyFrom(EmptyMessage())
        data_bytes = data.SerializeToString()

        padded_data = pad(data_bytes, AES.block_size)
        cipher = AES.new(KEY, AES.MODE_CBC, IV)
        encrypted_data = cipher.encrypt(padded_data)

        payload_data = encrypted_data
 
        headers = {
            "Expect": "100-continue",
            "Authorization": f"Bearer {token}",
            "X-Unity-Version": "2018.4.11f1",
            "X-GA": "v1 1",
            "ReleaseVersion": FREEFIRE_VERSION,
            "Content-Type": "application/x-www-form-urlencoded",
            "User-Agent": "Dalvik/2.1.0 (Linux; U; Android 11; SM-A305F Build/RP1A.200720.012)",
            "Connection": "Keep-Alive",
            "Accept-Encoding": "gzip"
        }

        res_bio = requests.post(url, headers=headers, data=payload_data)

        """

"""
        response_data = {
            "api_url": api_hostname,
            "bio_submitted": truncated_bio,
            "status_code": res_bio.status_code,
            "success": res_bio.status_code == 200,
        }
        return response_data

    except Exception as e:
        return {
            "api_url": api_hostname,
            "bio_submitted": truncated_bio,
            "status_code": 500,
            "success": False,
            "error_message": f"Internal error: {str(e)}"
        }

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return jsonify({
        "message": "Nicchen Long Bio API is running",
        "status": "online",
        "usage": "/updatebio?token={your_token}&bio={your_bio}&region={your_region}"
    })

@app.route('/updatebio', methods=['GET'])
def update_bio_endpoint():
    token = request.args.get('token')
    bio_text = request.args.get('bio')
    region = request.args.get('region')

    if not token or not bio_text:
        return jsonify({
            "success": False,
            "message": "Both 'token' and 'bio' query parameters are mandatory.",
            "example_url": "/updatebio?token=YOUR_JWT_TOKEN&bio=YOUR_NEW_BIO_TEXT&region=PK"
        }), 400

    full_url = get_full_url(region)

    result = update_bio_request(full_url, token, bio_text)

    return jsonify(result), result.get("status_code", 500)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=os.environ.get('PORT', 5500))
    """

"""