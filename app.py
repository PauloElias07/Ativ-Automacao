def soma(a, b):
  return a + b


def sub(a, b):
  return a - b


def multi(a, b):
  return a * b
  

def divi(a, b):
  if b == 0:
    raise ValueError("Nao e possivel dividir por zero!")
  return a / b
