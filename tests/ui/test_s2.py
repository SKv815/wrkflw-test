import pytest


class TestS2:
    @pytest.fixture(autouse=True, scope='function')
    def setup(self):
        print("setup S2")

    def test_s2_t1(self):
        actual = 3
        expected = 3
        assert actual == expected

    def test_s2_t2(self):
        actual = 4
        expected = 4
        assert actual == expected