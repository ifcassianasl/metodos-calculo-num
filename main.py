import numpy as np

# definindo a função
def f(h):
  return (np.arcsin(h) + (h * np.sqrt(1-h**2)) + 1.24 - 0.5 * np.pi)

# definindo a derivada da função
def df(h):
  return ( (2 - 2*h**2) / (np.sqrt(1-h**2)))

def fx(x):
  return x**3 - 9*x + 3

# Método da bissecção
def bissecao(f, a, b, tol):
  i = 1
  while True:
    if f(a) * f(b) < 0:
      p = (a + b) / 2 
      fp = f(p)
    if ((abs(fp) < tol) or (b - a < tol)):  
      return (p, i, fp, (b-a)/2)
    
    i = i+1
    if f(a) * fp < 0:
      b = p
    else:
      a = p   

print('bissecao', bissecao(f, 0, 1, 1e-2))


# Método da falsa posição
def falsa_posicao(f, a, b, tol):
  i = 1
  while True:
    fa = f(a)
    fb = f(b)
    if fa * fb < 0:
      p = (a*fb - b*fa) / (fb - fa)
      fp = f(p)

    if ((abs(fp) < tol) or (b - a < tol)):  
      return (p, i, fp, (b-a)/2)
    
    i = i+1
    if fa * fp < 0:
      b = p
      fb = fp
    else:
      a = p   
      fa = fp

print('falsa posicao', falsa_posicao(f, 0, 1, 1e-2))

# Método do ponto fixo
# Método de Newton
# Método da secante