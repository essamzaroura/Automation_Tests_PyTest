from api.user_api_client import UserAPIClient


def get_api(api_type):
    if api_type == "user":
        return UserAPIClient()
    elif api_type == "provider":
        print("Provider API- coming soon")
    else:
        raise ValueError("API type not supported.")