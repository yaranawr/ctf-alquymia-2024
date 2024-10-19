import math

def revert_substitutes(s):
    return s.replace('a', '0').replace('r', '5').replace('k', '7')

matrix = [
    ['k469', '8932', '88rr', 'kkkk', '2464', '8393', 'k469', '8aa8', '8239', '8kk8', 'raar'],
    ['8kk8', '8r4k', '8624', '2464', 'kkkk', '8932', '88rr', '8a8r', '8kk8', '8932', '2464'],
    ['9a86', '2464', 'k469', '8393', '9aa9', '2464', '88rr', '8a8r', 'k469', '8393', '2464'],
    ['9aa9', '8ka1', '2464', '8393', 'kkkk', '8kk8', 'kkkk', '8932', '2464', '9394', 'kkkk'],
    ['2464', 'k469', '9aa9', '88rr', '2464', '8r4k', 'kkaa', 'k469', '8kk8', 'kr46', 'kkkk'],
    ['8kk8', 'k623', '2464', '8316', 'kkkk', '9a86', '8a8r', '8kk8', 'k623', '84ka', '8a8r'],
    ['2r41', 'k469', '8a8r', 'k8r4', 'k469', '8kk8', 'k931', '8r4k', '8932', '8624', '8a8r'],
    ['k469', '9aa9', '88rr', '2464', 'k469', '9aa9', 'k931', 'kkkk', '616a', '2464', '2r41'],
    ['94k1', '623k', 'r8r2', 'raar', '2464', '4466', 'k931', 'k469', '8316', 'k8r4', '2464'],
    ['931k', '8kk8', 'k623', 'k31r', '88rr', 'k469', 'kkaa', 'k31r', '8a8r', '392k', '8kk8'],
    ['3r42', '962r', '4aa4', '38ra', '3696', '38ra', 'k31r', '88rr', '3696', '8932', '8624']
]

flattened = []
for row in matrix:
    flattened.extend(row[::-1])  

reverted = [revert_substitutes(num) for num in flattened]
numbers = [int(num) for num in reverted]
ascii_values = [num // 77 for num in numbers]
message = ''.join(chr(num) for num in ascii_values)

print("Mensagem decifrada:", message)
