﻿<p align="center">МИНИСТЕРСТВО НАУКИ  И ВЫСШЕГО ОБРАЗОВАНИЯ РОССИЙСКОЙ ФЕДЕРАЦИИ<br>
Федеральное государственное автономное образовательное учреждение высшего образования<br>
"КРЫМСКИЙ ФЕДЕРАЛЬНЫЙ УНИВЕРСИТЕТ им. В. И. ВЕРНАДСКОГО"<br>
ФИЗИКО-ТЕХНИЧЕСКИЙ ИНСТИТУТ<br>
Кафедра компьютерной инженерии и моделирования</p>
<br>
<h3 align="center">Отчёт по лабораторной работе № 4<br> по дисциплине "Программирование"</h3>
<br><br>
<p>студента 1 курса группы ПИ-б-о-201(1)<br>
Шенгелай Всеволод Михайлович<br>
направления подготовки 09.03.04 "Программная инженерия"</p>
<br><br>
<table>
<tr><td>Научный руководитель<br> старший преподаватель кафедры<br> компьютерной инженерии и моделирования</td>
<td>(оценка)</td>
<td>Чабанов В.В.</td>
</tr>
</table>
<br><br>
<p align="center">Симферополь, 2020</p>
<hr>

## Постановка задачи

Настроить рабочее окружение, для разработки программного обеспечения при помощи Qt и IDE Qt Creator, а также изучить базовые возможности данного фреймворка.

## Выполнение работы

- Закрепить навыки разработки многофайловыx приложений;
- Изучить способы работы с API web-сервиса;
- Изучить процесс сериализации/десериализации данных в/из json;
- Получить базовое представление о сетевом взаимодействии приложений.

#### Заданиие 1
1. Скачиваем с официального сайта и устанавливаем последнюю стабильную версию фреймворка Qt. Версия ОС на сайте опрделилась правильно. (Windows 10, 64-bit) 
![](./images/pic1.png)

*Рис. 1. Скачиваем онлайн-инсталлятор фреймворка Qt*

2. В процессе установки выбираем компоненты Qt для сборки, как было показано на видео:
[Qt - Установка](https://www.youtube.com/watch?v=f6iJ13i8ulk&list=PLKssqRhCd4-BPcXUHRo6uDQ6E0BKkkOuc&index=4)
![](./images/pic1.png)

*Рис. 2. Один из пунктов установки*

3. Соберём и настроим проект Calculator Form Example.

4. На боковой панели в разделе Проекты в каталоге Формы открываем главную форму проекта и заменяем текст "Input 1", "Input 2", "Output" на "Ввод 1", "Ввод 2" и "Вывод" соответственно.

5. Прикрепляем скриншот прирложения
![](./images/pic1.png)

*Рис. 3. Скриншот приложения "Калькулятор"*

#### Заданиие 2
Ответы на вопросы:
1. **Как изменить цветовую схему (оформление) среды?**<br>
    1. Перейти к `"Tools"` -> `"Options"` -> `"Environment"` -> `"General"`,
    1. Изменить `"Theme"` на темный
2. **Как закомментировать/раскомментировать блок кода средствами Qt Creator?**<br> 
Щёлкнуть в любом месте целевой строки правой кнопкой мыши и в выпавшем меню выбрать пунккт `закомментировать/раскомментировать` (или нажать сочетание клавишь Ctrl+/)
3. **Как открыть в проводнике Windows папку с проектом средствами Qt Creator?**<br>
`File` -> `Open File or Project`
4. **Какое расширение файла-проекта используется Qt Creator?**<br>
`<имя проекта>.pro` для сборщика QT
`CMakeLists.txt` для сборщика CMake, а также файлы *.cmake для библиотек.
5. **Как запустить код без отладки?**<br>
Нажать на зелёный треугольник слева снизу или `Сборка` -> `Запустить` (Ctrl+R)
6. **Как запустить код в режиме отладки?**<br>
Нажать на зелёный треугольник с жучком слева снизу или `Отладка` -> `Начать отладку` -> `Начать отладку запускающего проекта` (F5)
7. **Как установить/убрать точку останова (breakpoint)?**<br>
Нажать слева от нумерации строки либо переместить курсор на нужную строку и нажать `Отладка` -> `Поставить/снять точку останова` (F9)

#### Заданиие 3

1. Создаём консольное приложение без Qt.
2. Заменяем содержимое файла main.cpp на:

```C++
#include <iostream>
 
int main() {
    int i;
    double d;
    i = 5;
    d = 5;
    std::cout << i << d;
}
```

3. Переключаем режим сборки в режим Отладка;
4. Устанавлтиваем точки останова на 6, 7, 8 строках;
5. Выполняем программу в режиме отладки;
6. Отладочные данные:

| Номер строки  |  Значение i   |  Значение d   |
| :-----------: | :-----------: | :-----------: |
|       6       |       0       | 3.564988e-317 |
|       7       |       5       | 3.564988e-317 |
|       8       |       5       |       5       |

#### Задание 4
Настраиваем файл .gitignore, чтобы в репозиторий не попадал всякий мусор.

#### Вывод

В ходе выполнения лабораторной работы я научился:

- Устанавливать Open-Sourse среды разработки
- Раборать в среде разработки QT Creator
- Настраивать среду разработки QT Creator
- Добавлять и удалять компоненты QT с помощью MaintenanceTool
- Собирать с помощью QT Creator классические консольные проекты