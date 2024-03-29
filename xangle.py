import os
from typing import Dict, List

import requests


class Xangle(object):
    def __init__(self, api_key: str = os.environ.get("XANGLE_API_KEY", None)) -> None:
        super().__init__()
        if api_key is None:
            raise ValueError(
                "An API key is required to interact with the Xangle API.\nProvide one to the api_key parameter or by setting the environment variable 'XANGLE_API_KEY'."
            )
        # self.api_key = api_key
        self.headers = {"X-XANGLE_API_KEY": api_key}
        self.baseurl = "https://pro-api.xangle.io/v1/"

    # https://pro-api.xangle.io/#operation/project-list
    def get_project_list(
            self,
            page: int = 0
    ) -> Dict:
        try:
            response = requests.get(
                "https://pro-api.xangle.io/v1/project/list",
                headers=self.headers,
                params={"page": page},
            )
            return response.json()
        except requests.exceptions.ConnectionError as e:
            return {"error": f"{e}"}

    # https://pro-api.xangle.io/#operation/project-list
    def search_project(
            self,
            search_type: str,
            symbol: str = None,
            token_address: str = None,
    ) -> Dict:
        try:
            response = requests.get(
                "https://pro-api.xangle.io/v1/project/search",
                headers=self.headers,
                params={"search_type": search_type, "symbol": symbol, "token_address": token_address},
            )
            return response.json()
        except requests.exceptions.ConnectionError as e:
            return {"error": f"{e}"}

    # https://pro-api.xangle.io/#operation/disclosure-detail
    def get_disclosure_detail(
            self,
            disclosure_id: str,
            lang: str = "en"
    ) -> Dict:
        try:
            response = requests.get(
                "https://pro-api.xangle.io/v1/disclosure/detail",
                headers=self.headers,
                params={"disclosure_id": disclosure_id, "lang": lang},
            )
            return response.json()
        except requests.exceptions.ConnectionError as e:
            return {"error": f"{e}"}

    # https://pro-api.xangle.io/#operation/disclosure-list-all
    def get_disclosure_list_all(
            self,
            lang: str = "en",
            page: int = 0,
            project_ids: List[str] = [],
            exchange: str = None,
            exclude_types: List[str] = [],
    ) -> Dict:
        try:
            response = requests.get(
                "https://pro-api.xangle.io/v1/disclosure/list/all",
                headers=self.headers,
                params={
                    "lang": lang,
                    "page": page,
                    "project_ids": project_ids,
                    "exchange": exchange,
                    "exclude_types": exclude_types,
                },
            )
            return response.json()
        except requests.exceptions.ConnectionError as e:
            return {"error": f"{e}"}

    # https://pro-api.xangle.io/#operation/disclosure-list-project
    def get_disclosure_list_project(
            self,
            project_ids: str,
            lang: str = "en",
            page: int = 0,
            exclude_types: List[str] = [],
    ) -> Dict:
        try:
            response = requests.get(
                "https://pro-api.xangle.io/v1/disclosure/list/project",
                headers=self.headers,
                params={
                    "project_ids": project_ids,
                    "lang": lang,
                    "page": page,
                    "exclude_types": exclude_types,
                },
            )
            return response.json()
        except requests.exceptions.ConnectionError as e:
            return {"error": f"{e}"}

    # https://pro-api.xangle.io/v1/index/xangle-bluechip
    def get_xangle_bluechip(
            self,
            reference_timestamp: str
    ) -> Dict:
        try:
            response = requests.get(
                "https://pro-api.xangle.io/v1/index/xangle-bluechip",
                headers=self.headers,
                params={
                    "reference_timestamp": reference_timestamp
                },
            )
            return response.json()
        except requests.exceptions.ConnectionError as e:
            return {"error": f"{e}"}

    # https://pro-api.xangle.io/v1/index/xangle-bluechip-batch
    def get_xangle_bluechip_batch(
            self,
            start_timestamp: str,
            end_timestamp: str
    ) -> Dict:
        try:
            response = requests.get(
                "https://pro-api.xangle.io/v1/index/xangle-bluechip-batch",
                headers=self.headers,
                params={
                    "start_timestamp": start_timestamp,
                    "end_timestamp": end_timestamp
                },
            )
            return response.json()
        except requests.exceptions.ConnectionError as e:
            return {"error": f"{e}"}

    # https://pro-api.xangle.io/v1/index/xangle-bluechip-batch
    def get_xangle_bluechip_batch(
            self,
            start_timestamp: str,
            end_timestamp: str
    ) -> Dict:
        try:
            response = requests.get(
                "https://pro-api.xangle.io/v1/index/xangle-bluechip-batch",
                headers=self.headers,
                params={
                    "start_timestamp": start_timestamp,
                    "end_timestamp": end_timestamp
                },
            )
            return response.json()
        except requests.exceptions.ConnectionError as e:
            return {"error": f"{e}"}

    # https://pro-api.xangle.io/v1/index/xangle-largecap
    def get_xangle_largecap(
            self,
            reference_timestamp: str
    ) -> Dict:
        try:
            response = requests.get(
                "https://pro-api.xangle.io/v1/index/xangle-largecap",
                headers=self.headers,
                params={
                    "reference_timestamp": reference_timestamp
                },
            )
            return response.json()
        except requests.exceptions.ConnectionError as e:
            return {"error": f"{e}"}