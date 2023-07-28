# -*- coding: utf-8 -*-

# На основе своего кода из lesson_009/02_log_parser.py напишите итератор (или генератор)
# который читает исходный файл events.txt и выдает число событий NOK за каждую минуту
# <время> <число повторений>
#
# пример использования:
#
# grouped_events = <создание итератора/генератора>
# for group_time, event_count in grouped_events:
#     print(f'[{group_time}] {event_count}')
#
# на консоли должно появится что-то вроде
#
# [2018-05-17 01:57] 1234

# def grouped_events_generator(file_name):
#     current_event = None
#     current_count = 0
#
#     with open(file_name, 'r', encoding='utf8') as file:
#         for line in file:
#             if 'NOK' in line:
#                 event_time = line[1:17]
#                 event_count = 1
#                 for next_line in file:
#                     if 'NOK' in next_line:
#                         next_event_time = next_line[1:17]
#                         if next_event_time == event_time:
#                             event_count += 1
#                         else:
#                             yield event_time, event_count
#                             break
#                 else:
#                     yield event_time, event_count


# Пример использования:

# grouped_events = grouped_events_generator(file_name='events.txt')
# for group_time, event_count in grouped_events:
#     print(f'[{group_time}] {event_count}')


import itertools

def grouped_events_generator(file_name):
    with open(file_name, 'r', encoding='utf8') as file:
        for line in file:
            if 'NOK' in line:
                event_time = line[1:17]
                event_count = sum(1 for _ in itertools.takewhile(lambda x: 'NOK' in x, file))
                yield event_time, event_count


grouped_events = grouped_events_generator(file_name='events.txt')
for group_time, event_count in grouped_events:
    print(f'[{group_time}] {event_count}')
