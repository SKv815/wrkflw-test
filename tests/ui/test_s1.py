import pytest


class TestS1:
    @pytest.fixture(autouse=True, scope='function')
    def setup(self):
        print("setup S1")

    def test_s1_t1(self):
        actual = 5
        expected = 1
        assert actual == expected

    def test_s1_t2(self):
        actual = 2
        expected = 2
        assert actual == expected