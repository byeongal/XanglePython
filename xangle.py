import os
from typing import Dict, List, Literal

import requests


class Xangle(object):
    """
    Python client library for Xangle. With this library you can interact with the Xangle API and automate your workflow quickly and efficiently.
    Args:
        api_key (`str`): Xangle API Key
    """
    
    def __init__(self, api_key: str = os.environ.get("XANGLE_API_KEY", None)) -> None:
        super().__init__()
        if api_key is None:
            raise ValueError(
                "An API key is required to interact with the Xangle API.\nProvide one to the api_key parameter or by setting the environment variable 'XANGLE_API_KEY'."
            )
        self.headers = {"X-XANGLE_API_KEY": api_key}
        self.baseurl = "https://pro-api.xangle.io/v1/"

    # https://pro-api.xangle.io/#operation/project-list
    def get_project_list(self, page: int = 0) -> Dict:
        """
        List of projects including the project_id which is the key value of each project.
        Args:
            page (int, optional): page number of the list. (default is 0)
        Returns:
            Dict: application/json Object about list of projects
        Example:
            >>> get_project_list()
            {
                "data": {
                    "projects": [
                        {
                            "name": "EXPORT MOTORS PLATFORM",
                            "onchain_ready": False,
                            "onchain_type": "token",
                            "project_id": "61244dff2aee1c486071a843",
                            "status": "active",
                            "symbol": " EMP"
                        },
                        ...
                    ]
                },
                "status": {
                    "credit": 1,
                    "current_credit": 1999999,
                    "error_code": 0,
                    "error_message": None,
                    "timestamp": "2022-04-04T07:51:25.216838"
                }
            }        
        """
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
        search_type: Literal["symbol", "token_address"],
        symbol: str = None,
        token_address: str = None,
    ) -> Dict:
        """
        Search projects with symbol or token address.
        Args:
            search_type (Literal["symbol", "token_address"]): Type of search: [symbol, token_address]
            symbol (str, optional): Symbol of the project. (BTC, ETH, ...)
            token_address (str, optional): Token's contract address representing the project. (Only supported for Ethereum)
        Returns:
            Dict: application/json Object about information of symbol or token address
        Example:
            >>> search_project("symbol", "BTC")
            {
                "data": {
                    "projects": [
                        {
                            "name": "EXPORT MOTORS PLATFORM",
                            "onchain_ready": False,
                            "onchain_type": "token",
                            "project_id": "61244dff2aee1c486071a843",
                            "status": "active",
                            "symbol": " EMP"
                        },
                        ...
                    ]
                },
                "status": {
                    "timestamp": "2022-04-04T08:17:02.177326", 
                    "error_code": 0, 
                    "error_message": None, 
                    "credit": 1, 
                    "current_credit": 1999997
                }
            }
        """
        try:
            response = requests.get(
                "https://pro-api.xangle.io/v1/project/search",
                headers=self.headers,
                params={
                    "search_type": search_type,
                    "symbol": symbol,
                    "token_address": token_address
                }
            )
            return response.json()
        except requests.exceptions.ConnectionError as e:
            return {"error": f"{e}"}

    # https://pro-api.xangle.io/#operation/disclosure-detail
    def get_disclosure_detail(self, disclosure_id: str, lang: Literal["en", "ko"] = "en") -> Dict:
        """
        Contents of the disclosure_id
        Args:
            disclosure_id (str): id of the disclosure
            lang (Literal["en", "ko"], optional): language specification. Defaults to "en".
        Returns:
            Dict: application/json Object about information of disclosure
        Example:
            >>> get_disclosure_detail("624ab34956d727e7126da0a9")
            {
                "data": {
                    "project_id": "5cde464e602c16381e881010",
                    "project_symbol": "ETH",
                    "project_logo": "https://s3.ap-northeast-2.amazonaws.com/upload.xangle.io/images/project/5cde464e602c16381e881010/32.png",
                    "title": "Public Vulnerability Disclosures: Protecting the Ethereum consensus-layer",
                    "publish_status": "public",
                    "publish_timestamp": "2022-03-10T06:11:14.788000+00:00",
                    "publish_timestamp_utc": "2022-03-10T06:11:14.788000",
                    "last_modified_timestamp": None,
                    "valid": True,
                    "disclosure_type": "standard",
                    "resolved": False,
                    "validation_method": "not_applicable",
                    "meta": {
                    "official_company_name": "Ethereum",
                    "jurisdiction": "switzerland",
                    "address": "Zug, Switzerland (Ethereum Foundation)",
                    "website_url": "https://ethereum.org"
                    },
                    "data": {
                    "title": "Public Vulnerability Disclosures: Protecting the Ethereum consensus-layer",
                    "subjects": [
                        {
                        "subject": "Public Vulnerability Disclosures: Protecting the Ethereum consensus-layer",
                        "date_start": "2022-03-09T00:00:00",
                        "date_end": None,
                        "details": "<p>On March 9, 2022, the Ethereum Foundation announced that it has disclosed the first set of vulnerabilities from the Ethereum Foundation\u2019s Bug Bounty Programs. These vulnerabilities were previously discovered and reported directly to the Ethereum Foundation or client teams via the Bug Bounty Programs for both the Execution Layer and Consensus Layer.</p><p>Through its Bug Bounty Programs, which allow the Ethereum Foundation to coordinate and cross-check vulnerabilities across clients, the foundation currently accepts vulnerability reports for Nimbus, Teku, Lighthouse, Prysm, Lodestar, Go Ethereum, Nethermind, Erigon and Besu.</p><p><i>For more information, and to learn more about disclosure policies, timelines, and cataloging, head over to the new&nbsp;</i><a href=\"https://github.com/ethereum/public-disclosures/\"><i>disclosures repository</i></a><i>.</i></p>"
                        }
                    ],
                    "associated_links": [
                        {
                        "title": "Ethereum - Announcement",
                        "url": "https://blog.ethereum.org/2022/03/09/secured-no-2/"
                        }
                    ],
                    "files": [
                        {
                        "title": "Ethereum - Announcement.pdf",
                        "url": "https://s3.ap-northeast-2.amazonaws.com/upload.xangle.io/files/project/5cde464e602c16381e881010/disclosure/Ethereum_-_Announcement-975a1959-ba9d-4a0f-8958-35d732758518.pdf"
                        }
                    ]
                    },
                    "details": "\n            \n                        <h3>1. Subject</h3>\n\n                        <p>Public Vulnerability Disclosures: Protecting the Ethereum consensus-layer</p></br>\n\n                    \n                        <h3>2. Applicable Date(s)</h3>\n\n                        <p>2022-03-09 ~ </p></br>\n\n                    \n                        <h3>3. Details</h3>\n\n                        <p><p>On March 9, 2022, the Ethereum Foundation announced that it has disclosed the first set of vulnerabilities from the Ethereum Foundation\u2019s Bug Bounty Programs. These vulnerabilities were previously discovered and reported directly to the Ethereum Foundation or client teams via the Bug Bounty Programs for both the Execution Layer and Consensus Layer.</p><p>Through its Bug Bounty Programs, which allow the Ethereum Foundation to coordinate and cross-check vulnerabilities across clients, the foundation currently accepts vulnerability reports for Nimbus, Teku, Lighthouse, Prysm, Lodestar, Go Ethereum, Nethermind, Erigon and Besu.</p><p><i>For more information, and to learn more about disclosure policies, timelines, and cataloging, head over to the new&nbsp;</i><a href=\"https://github.com/ethereum/public-disclosures/\"><i>disclosures repository</i></a><i>.</i></p></p></br>\n\n                    \n        ",
                    "translator": None,
                    "pdf_file_url": None
                },
                "status": {
                    "timestamp": "2022-04-04T10:03:32.950164",
                    "error_code": 0,
                    "error_message": None,
                    "credit": 1,
                    "current_credit": 1999990
                }
            }
            
        """
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
    def get_xangle_bluechip(self, reference_timestamp: str) -> Dict:
        try:
            response = requests.get(
                "https://pro-api.xangle.io/v1/index/xangle-bluechip",
                headers=self.headers,
                params={"reference_timestamp": reference_timestamp},
            )
            return response.json()
        except requests.exceptions.ConnectionError as e:
            return {"error": f"{e}"}

    # https://pro-api.xangle.io/v1/index/xangle-bluechip-batch
    def get_xangle_bluechip_batch(
        self, start_timestamp: str, end_timestamp: str
    ) -> Dict:
        try:
            response = requests.get(
                "https://pro-api.xangle.io/v1/index/xangle-bluechip-batch",
                headers=self.headers,
                params={
                    "start_timestamp": start_timestamp,
                    "end_timestamp": end_timestamp,
                },
            )
            return response.json()
        except requests.exceptions.ConnectionError as e:
            return {"error": f"{e}"}

    # https://pro-api.xangle.io/v1/index/xangle-bluechip-batch
    def get_xangle_bluechip_batch(
        self, start_timestamp: str, end_timestamp: str
    ) -> Dict:
        try:
            response = requests.get(
                "https://pro-api.xangle.io/v1/index/xangle-bluechip-batch",
                headers=self.headers,
                params={
                    "start_timestamp": start_timestamp,
                    "end_timestamp": end_timestamp,
                },
            )
            return response.json()
        except requests.exceptions.ConnectionError as e:
            return {"error": f"{e}"}

    # https://pro-api.xangle.io/v1/index/xangle-largecap
    def get_xangle_largecap(self, reference_timestamp: str) -> Dict:
        try:
            response = requests.get(
                "https://pro-api.xangle.io/v1/index/xangle-largecap",
                headers=self.headers,
                params={"reference_timestamp": reference_timestamp},
            )
            return response.json()
        except requests.exceptions.ConnectionError as e:
            return {"error": f"{e}"}
