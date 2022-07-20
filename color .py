from scipy.spatial import KDTree
from webcolors import (
    css3_hex_to_names,
    hex_to_rgb)




hello = input('Enter hex: ').lstrip('#')
print('RGB =', tuple(int(hello[i:i+2], 16) for i in (0, 2, 4)))

