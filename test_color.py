from scipy.spatial import KDTree
from webcolors import (
    css3_hex_to_names,
    hex_to_rgb)




h = input('Enter hex: ').lstrip('#')
print('RGB =', tuple(int(h[i:i+2], 16) for i in (0, 2, 4)))

