import pytest
from sbpyEmailWrapper.wrapper import EmailWrapper

def test_instantiation():
    inst = EmailWrapper()
    assert isinstance(inst, EmailWrapper) == True

if __name__ == "__main__":
    pytest.main()