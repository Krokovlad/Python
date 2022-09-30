def main(x):
    dict31 = {'XTEND': 0, 'LEX': 1, 'MESON': 2}
    dict32 = {'XTEND': 3, 'LEX': 4, 'MESON': 5}
    dict33 = {1994: 8, 1993: 9}
    dict21 = {'AWK': dict31[x[2]], 'VCL': dict32[x[2]]}
    dict22 = {'AWK': 6, 'VCL': 7}
    dict23 = {'AWK': dict33[x[3]], 'VCL': 10}
    dict1 = {'ROFF': dict21[x[1]], 'NSIS': dict22[x[1]], 'C': dict23[x[1]]}
    return dict1[x[0]]

print(main(['NSIS', 'AWK', 'XTEND', 1994]))
print(main(['C', 'AWK', 'MESON', 1994]))
