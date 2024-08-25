from assertpy import assert_that
import pytest
from coding_exercise.application.splitter import Splitter
from coding_exercise.domain.model.cable import Cable


def test_should_not_return_none_when_splitting_cable():
    assert_that(Splitter().split(Cable(10, "coconuts"), 1)).is_not_none()


def test_should_raise_error_if_zero_times():
    with pytest.raises(ValueError):
        Splitter().split(Cable(10, "test"), 0)


def test_should_not_raise_error_if_times_is_1():
    assert_that(Splitter().split(Cable(1024, "test"), 1)).is_not_none()


def test_should_not_raise_error_if_times_is_more_than_1():
    assert_that(Splitter().split(Cable(1024, "test"), 2)).is_not_none()


def test_should_not_raise_error_if_times_is_less_than_64():
    assert_that(Splitter().split(Cable(1024, "test"), 63)).is_not_none()


def test_should_not_raise_error_if_times_is_64():
    assert_that(Splitter().split(Cable(1024, "test"), 64)).is_not_none()


def test_should_raise_error_if_times_is_more_than_64():
    with pytest.raises(ValueError):
        Splitter().split(Cable(1024, "test"), 65)


def test_should_raise_error_if_cable_length_is_less_than_2():
    with pytest.raises(ValueError):
        Splitter().split(Cable(1, "test"), 1)


def test_should_not_raise_error_if_cable_length_is_2():
    assert_that(Splitter().split(Cable(2, "test"), 1)).is_not_none()


def test_should_not_raise_error_if_cable_length_is_more_than_2():
    assert_that(Splitter().split(Cable(3, "test"), 1)).is_not_none()


def test_should_not_raise_error_if_cable_length_is_less_than_1024():
    assert_that(Splitter().split(Cable(1023, "test"), 1)).is_not_none()


def test_should_not_raise_error_if_cable_length_is_1024():
    assert_that(Splitter().split(Cable(1024, "test"), 1)).is_not_none()


def test_should_raise_error_if_cable_length_is_more_than_1024():
    with pytest.raises(ValueError):
        Splitter().split(Cable(1025, "test"), 1)


def test_should_raise_error_if_split_length_is_less_than_1():
    with pytest.raises(ValueError):
        Splitter().split(Cable(10, "test"), 10)


def test_should_not_raise_error_if_split_length_is_more_than_or_equal_1():
    assert_that(Splitter().split(Cable(10, "test"), 9)).is_not_none()


def test_should_split_without_remainder_1():
    cables = Splitter().split(Cable(10, "test"), 1)
    assert_that([cable.length for cable in cables]).is_equal_to([5] * 2)


def test_should_split_without_remainder_2():
    cables = Splitter().split(Cable(50, "test"), 49)
    assert_that([cable.length for cable in cables]).is_equal_to([1] * 50)


def test_should_split_with_remainder_1():
    cables = Splitter().split(Cable(5, "test"), 2)
    assert_that([cable.length for cable in cables]).is_equal_to([1, 1, 1, 1, 1])


def test_should_split_with_remainder_2():
    cables = Splitter().split(Cable(7, "test"), 1)
    assert_that([cable.length for cable in cables]).is_equal_to([3, 3, 1])


def test_should_have_single_digit_id():
    cables = Splitter().split(Cable(7, "test"), 1)
    assert_that([cable.name for cable in cables]).is_equal_to(["test-0", "test-1", "test-2"])


def test_should_have_double_digit_id():
    cables = Splitter().split(Cable(11, "test"), 9)
    assert_that([cable.name for cable in cables]).is_equal_to(["test-00", "test-01", "test-02", "test-03", "test-04", "test-05", "test-06", "test-07", "test-08", "test-09", "test-10"])