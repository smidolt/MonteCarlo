import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

S0 = 5.65 # начальная цена акции в долларах (за 29 июня 2010) после разделения
drift = 0.006 # средняя доходность акции за год после разделения
volatility = 0.143 # стандартное отклонение доходности акции за год после разделения
n = 1000 # количество симуляций
T = 252 # количество дней (торговых дней в году)
dt = 1/T # длина каждого шага в годах
Z = np.random.normal(0, 1, (n, T)) # массив случайного шума из стандартного нормального распределения

S = np.zeros((n, T)) # массив цены акции из нулей
S[:, 0] = S0 # первый столбец равен начальной цене акции для всех сценариев

for t in range(1, T): # для каждого следующего шага (дня)
  S[:, t] = S[:, t-1] * np.exp((drift - 0.5 * volatility**2) * dt + volatility * np.sqrt(dt) * Z[:, t]) # применить формулу GBM для каждого сценария

plt.plot(S.T) # построить линии для каждого сценария
plt.xlabel("Дни") # подписать ось x
plt.ylabel("Цена акции в долларах") # подписать ось y
plt.title("Симуляция движения акции Tesla с GBM") # добавить заголовок графика
plt.show() # отобразить график

expected_price = np.mean(S[:, -1]) # ожидаемая цена акции на конец периода
risk = np.std(S[:, -1]) # риск акции на конец периода
print(f"Ожидаемая цена акции Tesla на конец периода = {expected_price:.2f} долларов")
print(f"Риск акции Tesla на конец периода = {risk:.2f} долларов")

p_higher = np.sum(S[:, -1] > 10) / n # вероятность того, что цена акции будет выше 10 долларов
p_lower = np.sum(S[:, -1] < 2) / n # вероятность того, что цена акции будет ниже 2 долларов
print(f"Вероятность того, что цена акции Tesla будет выше 10 долларов на конец периода = {p_higher:.2%}")
print(f"Вероятность того, что цена акции Tesla будет ниже 2 долларов на конец периода = {p_lower:.2%}")
