import base64
import json
from io import BytesIO
import requests
import config

def recognize(img):
    output = BytesIO()
    img.save(output, format='JPEG')
    b64 = base64.b64encode(output.getvalue()).decode()
    data = {
        "username": config.get_value("tt_username"),
        "password": config.get_value("tt_password"),
        "typeid": 3,
        "image": b64}
    result = json.loads(requests.post(
        "http://api.ttshitu.com/predict", json=data).text)
    if result['success']:
        return result["data"]["result"], result["data"]["id"]
    else:
        return result["message"], result["data"]["id"]


def report_error(reg_id):
    data = {"id": reg_id}
    result = json.loads(requests.post(
        "http://api.ttshitu.com/reporterror.json", json=data).text)
    if result['success']:
        return "报错成功"
    else:
        return result["message"]
