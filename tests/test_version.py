import todo


def test_version() -> None:
    with open("pyproject.toml") as pyproject:
        assert f'version = "{todo.__version__}"\n' in pyproject
