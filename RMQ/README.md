# RMQ

RMQ расшифровывается как Range Minimum (Maximum) Query – запрос минимума (максимума) на отрезке в массиве.

# Разделение

Глобально есть 2 отличительные черты, и у каждой из них есть 2 варианта.

  1. Static / Dynamic
  2. Offline / Online

Static — неизменность массива.

Dynamic — возможность изменения элементов массива. Например увеличение всех элементов на подотрезке на 3.

Offline — можно получить все запросы сразу, как-нибудь их проанализировать, и только потом выдать на них ответ.

Online — в этом варианте запросы выдаются по очереди, и пока не дать ответ на один запрос, следующий получить не выйдет.

# Методы решений

  1. Sqrt-декомпозиция
  2. Дерево отрезков
