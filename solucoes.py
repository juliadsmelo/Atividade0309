def sao_anagramas(string1, string2):
    s1 = ''.join(string1.lower().split())
    s2 = ''.join(string2.lower().split())

    return sorted(s1) == sorted(s2)

print(sao_anagramas("caro", "arco"))
print(sao_anagramas("luar", "raul"))
print(sao_anagramas("vida", "mesa"))
    
pass