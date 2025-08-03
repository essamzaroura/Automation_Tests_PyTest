class APIConfig:
    MOCK_API_URL = "https://688dfa54a459d5566b13b497.mockapi.io"
    TIMEOUT=3
    HEADERS = {"content-type": "application/json"}

    @staticmethod
    def get_base_url(api_type: str) -> str:
        return APIConfig.MOCK_API_URL if api_type == "mock" else ""