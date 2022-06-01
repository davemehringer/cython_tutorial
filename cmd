python setup.py build_ext --inplace

# generate html
cython -a example_cy.pyx
