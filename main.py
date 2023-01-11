import numpy as np

# definindo a função
def f(h):
  return (np.arcsin(h) + (h * np.sqrt(1-h**2)) + 1.24 - 0.5 * np.pi)

# definindo a derivada da função
def df(h):
  return ( (2 - 2*h**2) / (np.sqrt(1-h**2)))

def fx(x):
  return x**3 - 9*x + 3

def qx(h):
  return (np.sin(-1.24 + 0.5*np.pi - h*np.sqrt(1-h**2)))

# Método da bissecção
def bissecao(f, a, b, tol):
  i = 1
  while True:
    if f(a) * f(b) < 0:
      p = (a + b) / 2 
      fp = f(p)
    if ((abs(fp) < tol) or (b - a < tol)):  
      return (p, i, fp, a, b, b-a)
    
    i = i+1
    if f(a) * fp < 0:
      b = p
    else:
      a = p   

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
      return (p, i, fp, (b-a))
    
    i = i+1
    if fa * fp < 0:
      b = p
      fb = fp
    else:
      a = p   
      fa = fp

# Método do ponto fixo
def ponto_fixo(f, qx, x0, tol, n):
  i = 1
  while i <= n:
    x1 = qx(x0)
    fx1 = f(x1)
    if ((abs(fx1) < tol)  or (abs(x1 - x0) < tol)):  
      return (x1, i, fx1, (x1 - x0))

    x0 = x1
    i = i+1

# na iteração, x nao pode ser  1, pois anula a divisao
# Método de Newton
def newton(f, df, x0, tol):
  i = 1
  while True:
    fx0 = f(x0)
    dfx0 = df(x0)
    
    x1 = (x0 - (fx0/dfx0))
    fx1 = f(x1)
    
    if ((abs(fx1) < tol)):  
      return (x1, i, fx1, (x1-x0)/2)
    
    x0 = x1
    i = i + 1

# Método da secante
def secante(f, x1, x0, tol):
  i = 1
  while True:
    fx0 = f(x0)
    fx1 = f(x1)

    qx = (x0*fx1 - x1*fx0) / (fx1 - fx0)

    fqx = f(qx)

    if ((abs(fqx) < tol) or (abs(qx - x1) < tol)):  
      return (qx, i, fqx, abs(qx - x1))
    
    i = i+1
    x0 = x1
    x1 = qx

print('bissecao', bissecao(f, 0, 1, 1e-2))
print('falsa posicao', falsa_posicao(f, 0, 1, 1e-2))
print('ponto fixo', ponto_fixo(f, qx, 0.171875, 1e-2, 300))
print('newton', newton(f, df, 0, 1e-2))
print('secante', secante(f, 0, 1, 1e-2))
