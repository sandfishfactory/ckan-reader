
from typing import Dict, Any
from urllib.request import Request, urlopen
from urllib.parse import urlencode, urljoin, urlparse, quote_plus
from urllib.error import HTTPError
import json

from ckanreader.base import CkanRequest


class RequestV3(CkanRequest):

    def __init__(self, address: str, headers: Dict[str, str] = {}, decode="utf-8"):
        api_context = "{}/{}/{}".format("api", "3", "action")
        self.base_url = urljoin(address, api_context)
        self.headers = headers
        self.decode = decode

    def gets(self, resource: str, headers: Dict[str, str] = None, query: Dict[str, str] = None) -> Dict:
        req_headers = self.__get_headers(headers)
        query_str = self.__get_query_str(query)
        req_url = self.__get_req_url(resource, query=query_str)
        return self.__ckan_request(req_headers, req_url)

    def __ckan_request(self, headers, url) -> Dict:
        print("url:{}".format(url))
        req = Request(url, headers=headers, method="GET")
        try:
            with urlopen(req) as res:
                body = res.read().decode(self.decode)
                return json.loads(body)

        except HTTPError as e:
            if e.code >= 400:
                print(e.reason)
            else:
                raise e

    def __get_headers(self, headers: Dict[str, str]) -> Dict:
        if headers:
            return headers
        else:
            return self.headers

    def __get_query_str(self, query: Dict[str, str]) -> str:
        if query:
            return urlencode(query)
        else:
            return None

    def __get_req_url(self, resource, id=None, query=None) -> str:

        if self.base_url.endswith("/"):
            req_url = self.base_url
        else:
            req_url = self.base_url + "/"

        req_url = urljoin(req_url, resource)

        if id:
            req_url = urljoin(req_url, id)

        if query:
            req_url = "{}?{}".format(req_url, query)

        return req_url
