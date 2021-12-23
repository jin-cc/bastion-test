# -*- coding: utf-8 -*-
import requests


def init_system_to_iam():
    system_info = {
        "id": "bastion",
        "name": "堡垒机IAM测试",
        "name_en": "bastion",
        "description": "堡垒机IAM测试",
        "description_en": "bastion iam test",
        "clients": "bastion,",
        "provider_config": {
            "host": "http://bkdev-paas3.canway.net:8082/t/bastion/",
            "auth": "basic",
            "healthz": "/test/"
        }
    }
    # 必须是内网
    IAM_HOST = "http://bkiam.service.consul:5001"
    APP_CODE = "bastion"
    SECRET_KEY = "9b08cb45-5c51-459a-9faf-21f9bc8fcf58"
    API = "/api/v1/model/systems/"
    URL = IAM_HOST + API
    # A = "http://paas.opsany.com/bk_iam"
    # URL = A + API
    headers = {
        "X-Bk-App-Code": APP_CODE,
        "X-Bk-App-Secret": SECRET_KEY,
        "Content-Type": "application/json"
    }
    res = requests.post(URL, headers=headers, json=system_info)

