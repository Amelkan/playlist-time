## project_6
# Задание
# 1. Посчитайте общее время звучания n случайных песен, где n - количество запрошенных песен
# 2. Используйте модули random и datetime. Или любые другие.
# 3. Решение должно включать функцию, которая в качестве аргумента способна принимать плейлисты разных типов данных

#Решение
import random
from datetime import timedelta
from typing import List, Tuple, Dict, Union

def get_duration(playlist: Union[List[List[Union[str, float]]], Tuple[Dict[str, float], ...]], n: int) -> timedelta:
    
    # Создаем пустой список для хранения длительностей песен
    durations = []
    
    # Проверяем, является ли плейлист списком списков
    if isinstance(playlist, list):
        for song in playlist:
            minutes = int(song[1])                 # целое число минут
            seconds = int((song[1] - minutes) * 100)  # целое число секунд
            durations.append(timedelta(minutes=minutes, seconds=seconds))
    
    # Проверяем, является ли плейлист кортежем словарей
    elif isinstance(playlist, tuple):
        for dictionary in playlist:
            for time in dictionary.values():
                minutes = int(time)
                seconds = int((time - minutes) * 100)
                durations.append(timedelta(minutes=minutes, seconds=seconds))
    else:
        raise ValueError("Неподдерживаемый формат плейлиста")
    
    # Проверяем, чтобы n не превышало количество песен
    if n > len(durations):
        raise ValueError("n больше количества песен в плейлисте")
    
    # Выбираем случайные песни
    selected_durations = random.sample(durations, n)
    
    # Суммируем длительность выбранных песен
    total_duration = sum(selected_durations, timedelta())
    
    return total_duration

playlist_a = [
    ['Waste a Moment', 3.03],
    ['New Salvation', 4.02],
    ['Staying\' Alive', 3.40],
    ['Out of Touch', 3.03],
    ['A Sorta Fairytale', 5.28],
    ['Easy', 4.15],
    ['Beautiful Day', 4.04],
    ['Nowhere to Run', 2.58],
    ['In This World', 4.02],
]

playlist_f = (
    {"Free Bird": 9.08, "Enter Sandman": 5.31, "One" : 7.45, "Sliver" : 2.10, "Come as You Are": 3.45},
    {"Thunderstruck": 4.53, "You Shook Me All Night Long": 3.29, "Everlong" : 4.51, "My Hero" : 4.02},
)

# Пример вызова функции
print(get_duration(playlist_a, 3))  # случайная длительность 3 песен из списка списков
print(get_duration(playlist_f, 3))  # случайная длительность 3 песен из кортежа словарей
