import pytest
import logging
LOGGER = logging.getLogger(__name__)


# Demo we can pass parameter to decide test environment
def pytest_addoption(parser):
    parser.addoption("--env", action="store", default="stag", help="option: stag (default) or prod")


@pytest.fixture
def env(request):
    return request.config.getoption("--env")
