def sao_anagramas(string1, string2):
  # TODO: Implementar a lógica
  pass

def cifra_cesar(texto, deslocamento):
    resultado = ''
    for char in texto:
        if char.islower():
            resultado += chr((ord(char) - ord('a') + deslocamento) % 26 + ord('a'))
        else:
            resultado += char  # mantém o caractere original
    return resultado
