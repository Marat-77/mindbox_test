import pytest

from mindbox_test.geometric_figure import Figure


results = [(2, 3, 4, (2, 3, 4)),
           (3, 4, 5, (3, 4, 5)),
           (4, 5, 6, (4, 5, 6))]


@pytest.mark.parametrize('a, b, c, expected_result', results)
def test_set_sides(a, b, c, expected_result):
    figure1 = Figure()
    figure1.set_sides(a, b, c)
    assert figure1.figure_sides == expected_result


@pytest.mark.parametrize('expected_exception, a, b, c, r', [(AttributeError, 3, 4, 5, 2)])
def test_polygon_set_radius_raise(expected_exception, a, b, c, r):
    figure_triangle = Figure()
    figure_triangle.set_sides(a, b, c)
    with pytest.raises(expected_exception):
        figure_triangle.set_radius(r)


@pytest.mark.parametrize('expected_exception, a, b, c, r', [(AttributeError, 3, 4, 5, 2)])
def test_circle_set_sides_raise(expected_exception, a, b, c, r):
    figure_circle = Figure()
    figure_circle.set_radius(r)
    with pytest.raises(expected_exception):
        figure_circle.set_sides(a, b, c)


@pytest.mark.parametrize('expected_exception, args', [
    (AttributeError, (-1,)),
    (AttributeError, (-1, -2)),
    (AttributeError, (15, 20, 0)),
    (AttributeError, (-1, 3, 10)),
    (AttributeError, (20, 3, -10)),
    (TypeError, 5),
    (TypeError, '5')
])
def test_set_sides_raise_negative_numbers(expected_exception, args):
    figure1 = Figure()
    with pytest.raises(expected_exception):
        figure1.set_sides(*args)


results_area_triangle = [(0.97, 1, 2, 2),
                         (2.9, 2, 4, 3),
                         (88.74, 10, 22, 18),
                         (1.98, 2, 2, 3),
                         (6.0, 5, 4, 3),
                         (3.8, 4, 2, 5)]


@pytest.mark.parametrize('expected_result, a, b, c', results_area_triangle)
def test_figure_area_triangle(expected_result, a, b, c):
    figure1 = Figure()
    figure1.set_sides(a, b, c)
    assert round(figure1.figure_area(), 2) == expected_result


results_area_rectangle = [(2, 1, 2),
                          (8, 2, 4),
                          (220, 10, 22),
                          (4, 2, 2),
                          (20, 5, 4),
                          (8, 4, 2)]


@pytest.mark.parametrize('expected_result, a, b', results_area_rectangle)
def test_figure_area_rectangle(expected_result, a, b):
    figure1 = Figure()
    figure1.set_sides(a, b)
    assert round(figure1.figure_area(), 2) == expected_result


results_area_line = [(None, 2),
                     (None, 4),
                     (None, 300)]


@pytest.mark.parametrize('expected_result, a', results_area_line)
def test_figure_area_line(expected_result, a):
    figure1 = Figure()
    figure1.set_sides(a)
    assert figure1.figure_area() == expected_result


@pytest.mark.parametrize('expected_result, a, b, c', [(True, 3, 4, 5),
                                                      (False, 6, 8, 11)])
def test_figure_area_triangle(expected_result, a, b, c):
    figure1 = Figure()
    figure1.set_sides(a, b, c)
    assert figure1.is_right_triangle() == expected_result


results2 = [(1, 'Line'),
            (1.9, 'Line'),
            (3, 'Line'),
            (300, 'Line')]


@pytest.mark.parametrize('a, expected_result', results2)
def test_figure_type_line(a, expected_result):
    figure1 = Figure()
    figure1.set_sides(a)
    assert figure1.figure_type == expected_result


results3 = [(2, 2),
            (3, 3),
            (3.6, 3.6),
            (4, 4)]


@pytest.mark.parametrize('r, expected_result', results3)
def test_set_radius(r, expected_result):
    figure1 = Figure()
    figure1.set_radius(r)
    assert figure1.circle_radius == expected_result


@pytest.mark.parametrize('expected_exception, r', [
    (AttributeError, -1),
    (AttributeError, -0.25),
    (AttributeError, 0),
    (AttributeError, -150),
    (TypeError, (-1, 3, 10)),
    (TypeError, (20, 3, -10)),
    (TypeError, [5]),
    (TypeError, '5')
])
def test_set_radius_raise_negative_numbers(expected_exception, r):
    figure1 = Figure()
    with pytest.raises(expected_exception):
        figure1.set_radius(r)


results4 = [(1, 'Circle'),
            (1.9, 'Circle'),
            (300, 'Circle')]


@pytest.mark.parametrize('r, expected_result', results4)
def test_figure_type_circle(r, expected_result):
    figure1 = Figure()
    figure1.set_radius(r)
    assert figure1.figure_type == expected_result
