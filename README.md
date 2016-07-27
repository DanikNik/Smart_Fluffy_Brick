# Ветка "request" проекта "Smarl_Fluffy_Brick"
#### Python3
## Проблемы, которые еще не решены:

 * У нас нет платы.
 * "Погода за окном" поддерживает не все города(лень)
 * Однако. Переводить мы можем только на английский(Yandex speechkit)
 * Не реализована поддержка свободных вопросов(Это основная проблема)
 * Не реализована поддержка пути(как дойти...) и т.д(Еще одна неприятность)
 * На некоторые запросы выдаются некорректные ответы(можно считать, что решено)
 * Возможна проблема в общении двух программных частей проекта, например проблема с кодировками(speech <=> request)
 * Возможны проблемы с памятью(Не тестировалось)

## Проблемы, которые уже решены:

 * Мы подружились с BeautifulSoup
 * Перевод фраз.
 * Теперь с именами почти нет проблем.
 * Теперь программа выдаёт чистый текст без скобок.
 * Мы выгнали лягушку(!!!)
 * К чёрту DuckDuckGo! Теперь у нас есть Wikipedia

## Глобальные изменения:

 * *27.07* : Теперь у нас есть консольный GUI.
 * *25.07* : Новый сервис --погода за окном.
 * *22.07* : Изменён синтаксис общения с программой путём добавления вводных слов.
 * *23.07* : Добавлен функционал перевода фраз.

## Краткая техническая документация:

#### При разработке использовались:
***ЯП:*** Python 3.5 <br>
***БТ:*** requests, os, BeautifulSoup4, urwid, subprocess

#### Как ЭТИМ пользоваться:
Вы хотите задать вопрос? скажите контрольную фразу. Возможно, мы её потом изменим, но пока это 'Слыш ты..!'
Затем вам нужно уточнить вид запроса: скажите 'вопрос', чтобы задать вопрос; 'погода' или 'какая погода', чтобы узнать погоду в конкретном городе; 'переведи', чтобы перевести на язык фразу.
Ну и ждите ответа, наслаждаять нашим **GUI**...
