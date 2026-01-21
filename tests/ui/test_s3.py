import pytest


class TestS3:
    @pytest.fixture(autouse=True, scope='function')
    def setup(self):
        print("setup S3")

    def test_s3_t1(self):
        actual = 5
        expected = 5
        assert actual == expected

    def test_s3_t2(self):
        actual = 6
        expected = 6
        assert actual == expected