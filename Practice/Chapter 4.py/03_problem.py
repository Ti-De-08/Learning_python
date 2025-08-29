'''Check that a tuple type cannot be changed in python.'''

a = (34, 51, 'Tirtha')

a[2] = "Debnath" # This will throw an error as tuples are immutable