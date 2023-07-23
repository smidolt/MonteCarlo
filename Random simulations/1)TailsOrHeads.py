import random

n = 1000 # количество симуляций
heads = 0 # количество выпадений орла
tails = 0 # количество выпадений решки

for i in range(n): # повторить n раз
  coin = random.randint(0, 1) # подбросить монетку (0 - орел, 1 - решка)
  if coin == 0: # если выпал орел
    heads += 1 # увеличить heads на 1
  else: # если выпала решка
    tails += 1 # увеличить tails на 1

p_heads = heads / n # вероятность орла
p_tails = tails / n # вероятность решки
print(f"Орел выпал {heads} раз из {n}, вероятность = {p_heads}")
print(f"Решка выпала {tails} раз из {n}, вероятность = {p_tails}")
