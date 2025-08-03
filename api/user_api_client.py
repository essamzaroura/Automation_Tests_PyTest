from api.api_client import APIClient

class UserAPIClient(APIClient):
    def build_url(self, endpoint):
        return f"{self.base_url}{endpoint}"

    def get_users(self):
        return self.send_request("GET", "/users")

    def get_user(self, user_id):
        return self.send_request("GET", f"/users/{user_id}")

    def get_user_by_name(self, user_name):
        return self.send_request("GET", "/users", params={"name": user_name})

    def create_user(self, payload):
        return self.send_request("POST", "/users", json=payload)

    def update_user(self, user_id, payload):
        return self.send_request("PUT", f"/users/{user_id}", json=payload)

    def delete_user(self, user_id):
        return self.send_request("DELETE", f"/users/{user_id}")