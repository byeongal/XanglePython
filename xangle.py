import os
import pprint
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

    def get_disclosure_detail(self, disclosure_id: str, lang: str = "en") -> Dict:
        try:
            response = requests.get(
                "https://pro-api.xangle.io/v1/disclosure/detail",
                headers=self.headers,
                params={"disclosure_id": disclosure_id, "lang": lang},
            )
            return response.json()
        except requests.exceptions.ConnectionError as e:
            return {"error": f"{e}"}

    def get_disclosure_list_all(
        self,
        lang: str = "en",
        page: int = 0,
        status: str = "public",
        project_ids: List[str] = [],
        exclude_types: List[str] = [],
    ) -> Dict:
        try:
            response = requests.get(
                "https://pro-api.xangle.io/v1/disclosure/list/all",
                headers=self.headers,
                params={
                    "lang": lang,
                    "page": page,
                    "status": status,
                    "project_ids": project_ids,
                    "exclude_types": exclude_types,
                },
            )
            return response.json()
        except requests.exceptions.ConnectionError as e:
            return {"error": f"{e}"}

    def get_disclosure_list_project(
        self,
        project_ids: List[str],
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
