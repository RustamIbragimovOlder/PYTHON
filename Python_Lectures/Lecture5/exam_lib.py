# # Библиотека определения четности числа
# from isOdd import isOdd

# print(isOdd(0)) #=> false
# print(isOdd(4)) #=> false
# print(isOdd(345))

# # Библиотека демонстрации процесса (загрузки, скачивания и т.п.)
# from progress.bar import Bar
# import time

# bar = Bar('Смотрите! Как идет процесс!', max=20)
# for i in range(20):
#     time.sleep(1) # торможение процесса для наглядности
#     bar.next()
# bar.finish()

# # Библиотека смайлов (эмодзи)
# import emoji

# print(emoji.emojize('Python is :thumbs_up:'))
# # Python is 👍
# print(emoji.emojize('Python is :thumbsup:', language='alias'))
# # Python is 👍
# print(emoji.demojize('Python is 👍'))
# # Python is :thumbs_up:
# print(emoji.emojize("Python is fun :red_heart:"))
# # Python is fun ❤
# print(emoji.emojize("Python is fun :red_heart:", variant="emoji_type"))
# # Python is fun ❤️ #red heart, not black heart
# print(emoji.is_emoji("👍"))
# # True

# # Библиотека рисования графиков различных функций (здесь - спектр радиосигнала)
# # Другими словами - визуализация данных

# import numpy as np
# import matplotlib.pyplot as plt

# # Fixing random state for reproducibility
# np.random.seed(19680801)

# dt = 0.01
# t = np.arange(0, 30, dt)
# nse1 = np.random.randn(len(t))                 # white noise 1
# nse2 = np.random.randn(len(t))                 # white noise 2

# # Two signals with a coherent part at 10Hz and a random part
# s1 = np.sin(2 * np.pi * 10 * t) + nse1
# s2 = np.sin(2 * np.pi * 10 * t) + nse2

# fig, axs = plt.subplots(2, 1)
# axs[0].plot(t, s1, t, s2)
# axs[0].set_xlim(0, 2)
# axs[0].set_xlabel('time')
# axs[0].set_ylabel('s1 and s2')
# axs[0].grid(True)

# cxy, f = axs[1].cohere(s1, s2, 256, 1. / dt)
# axs[1].set_ylabel('coherence')

# fig.tight_layout()
# plt.show()

# Свой пример рисования графика
import numpy as np
import matplotlib.pyplot as plt

list_check = [1, 3, 7, 4, 3, 0, 5, 1]
plt.plot(list_check)
plt.show()