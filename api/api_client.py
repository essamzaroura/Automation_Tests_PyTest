from abc import abstractmethod

from api.api_config import  APIConfig
import requests

class APIClient:
    def __init__(self):
        self.base_url = APIConfig.get_base_url("mock")
        self.headers = APIConfig.HEADERS
        self.timeout = APIConfig.TIMEOUT

    @abstractmethod
    def build_url(self, endpoint: str) -> str:
        pass #  (UserAPI, ProviderAPI) עשוי להשתמש בכתובת בסיס שונה

    def send_request(self, method, endpoint, params=None, json=None):
        url = self.build_url(endpoint)
        response = requests.request(method, url, headers=self.headers, params=params, json=json, timeout=self.timeout)
        return response
