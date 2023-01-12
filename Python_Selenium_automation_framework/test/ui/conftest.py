"""The module serves as a means of providing fixtures for an entire directory."""

import pytest

from test.ui.execution_utils.webdriver import get_driver


@pytest.fixture(scope='module')
def driver_item():
	driver = get_driver()
	yield driver
	driver.close()

