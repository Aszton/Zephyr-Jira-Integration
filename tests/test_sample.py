import pytest


class TestClass:
    def test_method_1_ZIT_T3(self):
        assert 1 == 1

    @pytest.mark.skip(reason='no way of currently testing this')
    def test_method_2_ZIT_T4(self):
        assert 3 == 5

    # will match with test case with key ZIT-T14
    def test_method_3_ZIT_T14(self):
        assert 5 == 5

    # will match with test case named tests.test_sample.TestClass.test_method
    def test_method(self):
        x = 'this'
        assert 'h' in x


# will match with test case named tests.test_sample.test_method_1_without_class
def test_method_1_without_class():
    assert 1 == 1


def test_method_2_without_class_ZIT_T16():
    assert 1 == 0
