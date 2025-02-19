
def es_palindromo(s):
    return "Es palindrome" if s == s[::-1] else "No es palindrome"

def main():
    S = input().strip()
    print(es_palindromo(S))

if __name__ == '__main__':
    main()
    
es_palindromo(reconocer)
es_palindromo(correr)

