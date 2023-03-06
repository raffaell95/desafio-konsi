from fastapi.testclient import TestClient
from typing import Generator
import pytest
from src.server import app


@pytest.fixture(scope='function')
def client() -> Generator:
    with TestClient(app) as client:
        yield client