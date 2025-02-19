
from collections import Counter
import sys

def son_permutaciones(s1, s2):
    if len(s1) != len(s2):
        return "NO"
    return "SI" if Counter(s1) == Counter(s2) else "NO"

def main():
    s1 = input().strip()
    s2 = input().strip()
    print(son_permutaciones(s1, s2))
    
son_permutaciones('aroma', 'romaa')
son_permutaciones('arroz', 'lentejas')

if __name__ == '__main__':
    main()

