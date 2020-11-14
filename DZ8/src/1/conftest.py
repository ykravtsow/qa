import pytest


def pytest_addoption(parser):
    parser.addoption(
        "--server",
        default="http://localhost"
    )
    parser.addoption(
        "--port",
        default=None
    )
    parser.addoption(
        "--user",
        default=None
    )
    parser.addoption(
        "--password",
        default=None
    )


@pytest.fixture
def server(request):
    return request.config.getoption("--server")


@pytest.fixture
def port(request):
    return request.config.getoption("--port")


@pytest.fixture
def user(request):
    return request.config.getoption("--user")


@pytest.fixture
def passwd(request):
    return request.config.getoption("--password")
