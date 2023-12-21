import pytest
import logging


class TestBase:

    @pytest.fixture(autouse=True)
    def before_and_after_test_fixture(self, env):
        logging.info(f"[Environment] {env}")
        logging.info("[Fixture Setup] Start")
        yield
        logging.info("[Fixture Setup] End")
