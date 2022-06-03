# import example_cy
import timeit

# example_cy.test(5)
cy = timeit.timeit(
    'example_cy.test(5000)',
    setup='import example_cy',
    number=10000
)
py = timeit.timeit(
    'example_py.test(5000)',
    setup='import example_py',
    number=10000
)

py_typed = timeit.timeit(
    'example_py.test1(5000)',
    setup='import example_py',
    number=10000
)

print(cy,py, py_typed)
print(f'cython is {py/cy} times faster')