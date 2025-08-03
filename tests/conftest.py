#conftest.py
import pytest
from api.api_factory import get_api

@pytest.fixture(scope="function")
def user_api():
    print("\n[Setup] Starting test")
    api = get_api("user")
    yield api
    print("[Teardown] Test finished")

def pytest_runtest_setup(item):
    print(f"[Hook] Before test: {item.name}")

def pytest_runtest_teardown(item, nextitem):
    print(f"[Hook] After test: {item.name}")

@pytest.fixture(scope="module")
def setup_for_sanity():
    print("Setting up SANITY group...")
    yield
    print("Cleaning up SANITY group...")
