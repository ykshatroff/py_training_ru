Лекция 4. Циклы. Операторы присваивания с модификацией. Логический тип данных. Строки 
=========

### Значки, используемые в тексте

* :clock2: &mdash; отмечает, что высказывание не совсем верно, но будет уточнено позднее.
* :star: &mdash; выделяет определение нового понятия.
* :exclamation: &mdash; привлекает внимание к высказыванию.
* :point_up: &mdash; указывает на небольшое отступление от темы или уточнение.
* :bulb: &mdash; индикатор традиций и договорённостей. 
* :warning: &mdash; требуется осторожность: возможно, сложное высказывание.  

### Повторение терминов из третьей лекции

* *Функция* &mdash; это сущность, которая может принимать значения и возвращать результат.   
* *Функция `input()`* &mdash; это функция, запрашивающая ввод значения пользователем.   
* *Функции `abs(x)`, `min(x, y, ...)`, `max(x, y, ...)`, `round(x)` и `round(x, N)`*     &mdash; 
  встроенные функции в Python.
* *Пользовательские функции* &mdash; функции, объявляемые в программах с использованием ключевого слова `def`.
* *Контекст вызова* и *контекст объявления* функции &mdash; состояние программы в моменты соответственно вызова и
  объявления функции, то есть набор доступных функции переменных: в качестве аргументов или для использования в теле функции.
* *Утверждение `return`* &mdash; утверждение, указывающее интерпретатору на окончание выполнения функции и необходимость 
  возврата предоставленного выражения в контекст вызова в качестве результата.
* *Константы* &mdash; переменные, объявляемые один раз и используемые в дальнейшем только для вычислений, имеющие
  специальное оформление идентификаторов в заглавном регистре.
* *Объект `None` ("ничто")*  &mdash; объект, возвращаемый функцией в случае отсутствия в ней утверждения `return` или
  неполучения им управления (программа до него "не дошла").
  

## Циклический алгоритм. Цикл `while`

Мы с вами уже не раз встречались с заданиями, в которых требовалось повторить одно и то же действие несколько раз:
ввести несколько значений, сравнить несколько чисел (найти максимум или минимум), посчитать значения, соответствующие условию. 
Часто подобные операции однотипны и повторяются по определённому шаблону.
Например, умножение на N &mdash; это повторение операции сложения N раз, 
возведение в степень &mdash; это повторение операции умножения, а
посчитать количество чётных чисел из набора заданных  &mdash; это повторение операции 
присваивания с увеличением счётчика на единицу, если число делится на 2 без остатка.

Попробуем записать это в псевдокоде:

    счётчик = 0
    ВВЕДЁМ переменную Х
    ЕСЛИ Х чётное: 
        увеличим счётчик на 1
    ВВЕДЁМ переменную Y
    ЕСЛИ Y чётное: 
        увеличим счётчик на 1
    и так далее...
 
У нас уже есть возможность управлять течением программы, используя условные конструкции.
Но когда повторений много, нам пришлось бы много раз копировать и вставлять один и тот же по смыслу код, 
что нарушает принцип "не повторяйся".
И даже в таком случае, это работает только до тех пор, пока точно известно количество проверок и условий. 
В случае, если мы хотим задать количество повторений
извне, мы уже не можем просто скопировать условную конструкцию N раз. Нам хотелось бы видеть что-то подобное:  

    счётчик = 0
    ВВЕДЁМ количество_проверок 
    количество_пройденных_проверок = 0
    ПОКА количество_пройденных_проверок не больше количество_проверок:
        ВВЕДЁМ переменную Х
        ЕСЛИ Х чётное: 
            увеличим счётчик на 1
        количество_пройденных_проверок увеличим на 1


В Python эта возможность является элементарной и обеспечивается конструкцией `while` &mdash; "пока", и выглядит она так:

    while УСЛОВИЕ: БЛОК_КОДА
   
:star: Конструкция цикла `while` &mdash; это *сложное утверждение*, вводимое ключевым словом `while` и указывающее на повторение 
содержащегося в нём блока кода до тех пор, пока выполняется
заданное в ней условие. 

Смысл данной конструкции такой: вначале проверяется  _УСЛОВИЕ_, если оно верно, то выполняется *БЛОК_КОДА* (*тело цикла*), в котором 
изменяются используемые в условии значения; затем снова проверяется условие, и так до тех пор, пока оно верно;
затем управление переходит к следующему утверждению.
Если условие изначально неверно, то весь *БЛОК_КОДА* пропускается.

Продемонстрируем цикл на следующем задании: вывести числа от 1 до 10.

```python
x = 1  # переменная, содержащая выводимое число, она же счётчик выполнений цикла
while x <= 10:
    print x
    x = x + 1  # увеличиваем счётчик
```

Эта конструкция очень похожа на `if`-конструкцию, с той лишь разницей, что блок кода в `if`-утверждении выполняется 0 или 1 раз,
а в `while`-утверждении &mdash; 0 или более раз. 

:star: Одно выполнение цикла называется *итерацией*, таким образом цикл состоит из 0 или более итераций.

:point_up: Количество выполнений блока кода в циклах `while` не ограничено, и нужно быть 
крайне внимательным и *не допускать*, чтобы выражение
 в условии выполнялось всегда: это приведёт к бесконечному циклу и является распространённой ошибкой. Обязательно 
 проверяйте, чтобы условие менялось в каждой итерации или хотя бы периодически.


## Операторы присваивания "на месте" (in-place). Оператор остатка от деления по модулю `%`

В приведённом примере мы увеличиваем счётчик выполнений цикла в каждой итерации с помощью оператора присваивания.
Такой приём настолько распространён в программировании, и в частности в Python, что для сокращения кода (и заодно
во избежание повторений названий переменных) имеется специальный набор операторов *присваивания с модификацией на месте*, 
одним из них является сложение с модификацией:

    x += y

эквивалентно 

    x = x + y
    
Также существуют вычитание с модификацией: `x -= y`, умножение: `x *= y`, деление: `x /= y`, 
и возведение в степень: `x **= y`.
 
В задании к прошлой лекции мы вычисляли *остаток от деления по модулю*. Впрочем, в Python уже есть и такой оператор:
 
    x % y
    
означает остаток от деления `x` на `y` (как целочисленного, так и вещественного). И для него есть аналогичный оператор
присваивания "на месте":

    x %= y
    
:point_up: В других ЯП типа С, помимо указанных операторов, существуют и операторы `++` и `--` (увеличить и уменьшить на 1).
В Python такого оператора намеренно нет, чтобы всегда сохранять явность операнда.

## Логический тип данных

Теперь мы можем записать наш пример по подсчёту чётных чисел на Python во всей красе. :warning: Для краткости (и также ради 
демонстрации техники работы с циклами) мы не будем вводить отдельный счётчик цикла, а сразу уменьшать введённую нами
переменную *количество_проверок*, пока она не достигнет 0:

```python
inputs_count = input()  # вводим счётчик выполнений цикла, он же - количество вводимых значений
evens_count = 0  # счётчик чётных чисел среди введённых

while inputs_count > 0:
    x = input()  # вводим число
    if x % 2 == 0:  # число чётное?
        evens_count += 1  # увеличиваем счётчик чётных чисел
    inputs_count -= 1  # уменьшаем счётчик цикла

print evens_count
```

Если мы введём первое число 5, то условие `inputs_count > 0` в утверждении `while` проверится 6 раз, 
и на 6-й раз оно будет неверно.
Также мы проверяем в теле цикла условие `x % 2 == 0`, и если оно верно применительно к введённому в текущей итерации `x`,
 увеличиваем счётчик чётных чисел.
 
Мы уже не раз использовали слова "верно" или "неверно" применительно к условиям, и как оказывается, в Python существует
тип данных специально для таких понятий. 

Мы можем выразить "счётчик чётных чисел" простым языком: 
количество чётных чисел во множестве равно *сумме раз*, когда число чётное. Если обозначить результат проверки каждого числа
 за 1 ("раз"), если оно чётное (условие "верно") и 0, есло оно нечётное ("неверно"), сумма этих результатов и будет искомым счётчиком. 
Например,  для множества чисел 2, 3, 5, 8, 13,  это будет суммой 1 + 0 + 0 + 1 + 0 = 2.

И действительно, в Python существует логический тип данных (так называемый *Булевский* или "булев" тип, по имени изобретателя логической
алгебры Джорджа Буля), который состоит из двух значений, являющихся встроенными в язык объектами
`True` (*истинно*, верно) и `False` (*ложно*, неверно). При этом,  `True` &mdash; это "надстройка" над 1, 
а  `False`  &mdash; "надстройка" над 0. Что это значит, мы узнаем буквально через пару строк. 
 
:exclamation: Результатом любой операции сравнения является булев объект `True`  или `False`. 

Записав в интерактивном python условное выражение, мы увидим именно *булев* результат:
  
    >>> 4 % 2 == 0
    True
    >>> 5 % 2 == 0
    False

А вот и объяснение про магическую надстройку:

    >>> False == 0
    True
    >>> True == 1
    True
    >>> True + True
    2
    >>> True + False
    1

Фактически, мы можем использовать `True`  и `False` вместо 1 и 0. Конечно, там, где это уместно. В нашем примере мы спокойно
можем заменить `if`-конструкцию на одно утверждение присваивания с модификацией:

```python
inputs_count = input()  # вводим счётчик выполнений цикла, он же - количество вводимых значений
evens_count = 0  # счётчик чётных чисел среди введённых

while inputs_count > 0:
    x = input()  # вводим число
    evens_count += (x % 2 == 0)  # увеличиваем счётчик чётных чисел на результат сравнения (1 или 0)
    inputs_count -= 1  # уменьшаем счётчик цикла

print evens_count
```

Скобки вокруг выражения проверки условия чётности не обязательны, но в подобных случаях их принято ставить для лучшей читаемости.

:point_up: И всё-таки так писать не рекомендую, ибо эта форма записи часто не интуитивна и сбивает с толку.   

## Приведение выражений к булеву типу

Мы выяснили, что можно использовать `True` вместо 1, `False` вместо 0. Можно ли наоборот? Да, можно:

```python
if 1:
    print 1  # -> 1

if 0:
    print 0  # не выполнится
```

То есть, в блоке УСЛОВИЕ в `if`-конструкции допускается число. С 0 и 1 всё понятно &mdash; будут использоваться их булевы эквиваленты,
а что же с другими числами? Ответ прост: любое число, кроме 0, считается в контексте "УСЛОВИЕ" истинным. Этот ответ выводится из 
булевой алгебры, а именно логических операций И и ИЛИ, которые являются аналогами соответственно умножения и сложения.

:point_up: Для доказательства, давайте немного вспомним алгебру логики. Это нам пригодится чуть позже. Итак, у нас существует
выражения, которые могут иметь значение ИСТИНА или ЛОЖЬ, и три определённых над ними операции: И, ИЛИ, НЕ. Таким образом,
 например, НЕ ИСТИНА = ЛОЖЬ, ИСТИНА ИЛИ ЛОЖЬ = ИСТИНА, ЛОЖЬ И ИСТИНА = ЛОЖЬ и т.п. (Подробнее см. [Алгебра логики].) 

Возьмём два положительных числа A и B. Обозначим, в контексте доказательства, логическую операцию *И* как `*`, а операцию *ИЛИ* как `+`.
* `А * В` всегда ненулевое (выражение `А И В` истинно, если истинны и А, и В), в то же время `А * 0 == В * 0 == 0`.
* `А + В` равно нулю только если `А == В == 0 `(`А ИЛИ В` истинно, если хоть одно из А и В истинно),
 в то же время `А + 0 == А`, `В + 0 == В`. 
 
Таким образом, для булевой алгебры значение `False` то же самое, что число 0 для арифметики, а любое другое положительное
 число аналогично значению `True`.
 
На отрицательные числа распространяется то же правило &mdash; любое ненулевое отрицательное число истинно. Это следует из
того, что арифметическое понятие знака для логического выражения не имеет смысла и не меняет значения его истинности. 
(Существующая логическая
операция отрицания, *НЕ*, арифметически может быть эквивалентна выражению `1 - A` для А из множества логических значений 0 и 1.)
 
:exclamation: Помимо чисел, мы уже знаем ещё один тип данных, к которому принадлежит объект `None`. Так вот, объект `None`
 в логическом контексте эквивалентен значению `False`.


## Логические операторы

В Python, неудивительно, поддерживается и набор логических операторов, которые мы перечислили выше, только
 записываются они на английском языке. Эти операторы: И &mdash; `and`, ИЛИ &mdash; `or`, НЕ &mdash; `not`, где `and`, `or`, `not` &mdash; 
 ключевые слова.
Операторы `and` и `or` принимают по 2 операнда, а `not`, как и оператор изменения знака `-`, является унарным правоассоциативным (относится к выражению справа от себя).

Их используют для того, чтобы в одном блоке УСЛОВИЕ можно было указать несколько выражений. Например:
 
```python
if x > 0 and x % 2 == 0 or not x > y:  # если х > 0 *И* чётное *ИЛИ* *НЕ* x > y
    print x
```

Порядок вычисления таков: это операторы с самым низким приоритетом, ниже операторов сравнения.
При этом они выполняются последовательно так же, как и читаются:
 
    ЕСЛИ УСЛОВИЕ_1 И УСЛОВИЕ_2 И УСЛОВИЕ_3: ...    
    ЕСЛИ УСЛОВИЕ_1 ИЛИ УСЛОВИЕ_2 И НЕ УСЛОВИЕ_3: ...

Приоритет вычислений можно, как обычно, изменять скобками.

Примеры:

```python
x = input()
if x > 5 and x < 10 and x % 4 == 0:
    print 1  # выполнится, если x == 8
if x > 5 and x < 10 or x % 4 == 0:
    print 2  #  выполнится, если (x между 5 и 10) либо (х делится на 4 без остатка)
if x > 5 and x < 10 and x % 4 == 0 or x % 4 == 1:
    print 3  # выполнится, если x == 8 или x == 9
if x > 5 and x < 10 and not x % 4 == 0 or x % 4 == 1:
    print 4  # выполнится, если x одно из чисел 6,7,9; 
    # условие `x % 4 == 1` здесь бессмысленно, так как уже подпадает под `not x % 4 == 0`
if x > 5 and x < 10 and not (x % 4 == 0 or x % 4 == 1):
    print 5  # выполнится, если x == 6 или x == 7
```

:point_up: Выражения вида `not x == y` предпочтительнее записывать в виде `x != y`, т.е. менять оператор сравнения 
на противоположный по смыслу. Но в некоторых редких случаях нагляднее бывает использовать `not`.

### Вычисление выражений с логическими операторами

Если мы посмотрим на записанные выше примеры, мы можем заметить, что в некоторых случаях достаточно вычислить одну или несколько
частей сложного условного выражения, чтобы сказать, будет ли условие выполняться. Например, в случае: 

```python
if x > 5 and x < 10 and x % 4 == 0:
    print 1  # выполнится, если x == 8
```

если `x = 0`, то очевидно, что условие уже никак не сможет быть истинным. То есть, два следующих выражения, в принципе,
можно и не вычислять. Для `x = 20`, достаточно двух первых выражений, чтобы сказать, 
что всё условие будет эквивалентно `False`.

Python поступает точно так же: он не вычисляет "ненужные" выражения-операнды. "Ненужность" определяется во время вычисления,
 то есть когда получено достаточно информации о том, что дальнейшие выражения не повлияют на результат условия.

:exclamation: Если одного из двух операндов операторов `and` и `or` достаточно для определения истинности всего
выражения, то результатом всего выражения будет результат этого операнда,
и вычисление второго операнда не состоится. В противном случае результатом выражения будет результат второго операнда.

Выше мы упомянули о том, что условие необязательно должно иметь булев тип: это может быть и арифметическое выражение,
и объект типа `None`, и т.п. Логические операторы `and` и `or` в Python имеют одну важную особенность:  
они всегда сохраняют тип выражений-операндов, в отличие от `not` &mdash; выражение, начинающееся с `not`, 
всегда будет иметь булев тип.

Результатом составного выражения с `and` или `or` будет "чистый" результат того из выражений, 
которое должно быть вычислено исходя из правил логики после приведения выражений к логическому типу. 
 
Так, например, значением выражения `0 and 1` будет целое число `0`, а не `False`;
`0 or 1` &mdash; `1`, а не `True`; `5 and 0 or None` &mdash; `None` и т.п.; выражение `not 0`, однако, будет равно `True`, `not 1` &mdash; `False`,
как и `not 5` и `not -10`, то есть `not` возвращает булево значение, противоположное уже приведённому к булеву типу.
 

## Строки

Мы с вами уже, пожалуй, достаточно хорошо знаем арифметику и различные элементы синтаксиса Python, чтобы перейти к изучению строк.
Строковые данные в Python представлены двумя типами, `str` и `unicode`, пока рассмотрим первый.
 
:star: *Строка* &mdash; это упорядоченная последовательность любых символов. При использовании в строках (и не только) символов кириллицы
необходимо помнить о требовании указания кодировки с помощью комментария `coding: utf-8` в первой строке программы.
(В интерактивном режиме кодировка берётся из окружения и чаще всего уже установлена в utf-8.)
 
Строковые литералы в Python записываются с помощью кавычек и апострофов:

    "любые символы, кроме кавычки"
    'любые символы, кроме апострофа'

Данные две строки абсолютно эквивалентны, и их единственным отличием является возможность вставки апострофа в строку с
кавычками и кавычек в строку с апострофом. (Кавычки и апострофы можно вставлять в любую строку, если при этом "экранировать"
эти символы с помощью вставки перед ними символа `\` (обратный слэш):
 
```python
# coding: utf-8
print "вставленные \"кавычки\" и \'апостроф\'"  # вставленные "кавычки" и 'апостроф'
print 'вставленные \"кавычки\" и \'апостроф\''  # вставленные "кавычки" и 'апостроф'
```
    
:exclamation: обратный слэш также вводит некоторые другие сочетания символов (спецсимволы), поэтому для указания одиночного
обратного слэша его обычно также предваряют обратным слэшом:

```python
# coding: utf-8
print "обратный \\ слэш"  # обратный \ слэш
```

Для того, чтобы не было необходимости экранировать большие количества кавычек, можно воспользоваться ещё одной парой
способов объявления строк &mdash; тройными кавычками или тройными апострофами:

```python
# coding: utf-8
print """\"кавычки" и 'апостроф'"""  # "кавычки" и 'апостроф'
print '''"кавычки" и 'апостроф\''''  # "кавычки" и 'апостроф'
```

(Однако надо иметь в виду, что четыре кавычки или апострофа подряд не будут распознаны корректно, 
поэтому в таких случаях их нужно экранировать!)

### Соединение строк

Две строки, написанных рядом (с любыми кавычками в качестве разделителя), между которыми нет других символов или есть только пробелы,
 считаются как одна строка:
 
```python
# coding: utf-8
print '"кавычки"' """ и """ "'апостроф'"  # "кавычки" и 'апостроф'
```

У утверждения `print` существует также возможность выводить несколько разных объектов в одном утверждении, разделяя их
запятыми (при выводе они будут отделены пробелами):

```python
# coding: utf-8
print "единица", 1, "двойка", 2, "ИСТИНА", True
```

### Операции со строками

Строки можно использовать как просто для вывода текста, так и в некоторых других интересных контекстах: например,
известная нам функция `input()` принимает аргумент-строку, которую выведет в качестве подстказки перед вводом.

Строки также поддерживают *интерполяцию* &mdash; подстановку значений в строку вместо специальных последовательностей
символов (так называемых *плейсхолдеров*), что является также удобным для вывода значений. Это делается, применяя к строке
оператор `%` (да, тот самый, который является оператором деления по модулю для чисел: операторы в Python так же могут
выдавать разный результат в зависимости от контекста, как и функции):

```python
# coding: utf-8
print "единица=%s" % 1  # единица=1
```

В данном случае *плейсхолдер* `%s` будет заменён на значение `1`.

## Функции-типы данных

Для того, чтобы явно преобразовать выражение в булев тип (узнать его булево значение), существует функция `bool(expr)`, 
возвращающая всегда булев тип, в соответствии со значением истинности выражения:

```python
print bool(1)   # True
print bool(0)   # True
print bool(None)   # False
print bool(None or not None)   # True
```

Такие же функции есть и для целого числа &mdash; `int()`, и для дробного &mdash; `float()`. Но их аргументом может быть только численный
или булев тип, либо численная строка, в противном случае возникнет ошибка TypeError или ValueError:

```python
print int(True)  # 1
print int(False)  # 0
print int(2.5)  # 2 &mdash; отбрасывает дробную часть
print int(-2.5)  # -2 &mdash; отбрасывает дробную часть в сторону 0
print int("2")  # 2 &mdash; извлекает число из строки
print float(2)  # 2.0
print float("2")  # 2.0
print float("2.0")  # 2.0

# print int(None)  # TypeError &mdash; неверный тип данных
# print int("test")  # ValueError &mdash; некорректная строка
```

Также почти любой тип данных можно преобразовать в строку с помощью функции `str()` &mdash; фактически именно это происходит,
 когда мы передаём нестроковые аргументы в утверждение `print`:
 
```python
print True  # 
print str(True)  # аналогично
```

И то же преобразование в строку происходит при передаче значения в интерполяции: 

```python
# coding: utf-8
print "единица=%s" % 1  # единица=1
print "единица=%s" % str(1)  # единица=1
```

### Улучшенная функция `input()`

Мы много раз сталкивались с тем, что функция `input()` при вызове из программы просто ожидает ввода, 
но пользователю не всегда понятно, что происходит и что делать. Для того, чтобы явно показать, что программа ожидает ввода,
 функция `input()` принимает один аргумент &mdash; строку, которая будет выведена перед запросом на ввод. 
 
```python
# coding: utf-8
x = input("Введите х:")
```

Так гораздо понятнее, что программа не "висит", а ждёт ввода.

## Резюме

Сегодня мы научились эффективно выполнять повторяющиеся действия в цикле, писать сложные логические условия и приводить
выражения к логическим значениям, а также переводить значения между типами данных, которые пополнились логическим типом
и строками. В дополнение, мы можем более красиво использовать утверждения вывода и функцию ввода.

## Задания

1. Написать программу, которая запрашивает ввод двух чисел `x, y` и выводит целые числа от `x` до `y` включительно.
2. Написать программу, которая запрашивает ввод целого числа `x` и вычисляет сумму всех чётных чисел от 0 до `x` (если
   х чётное, то включительно). *Примечание*: Попробуйте сделать это разными способами.
3. Написать программу, которая регулярно (в цикле) запрашивает ввод целого числа `x` до тех пор, пока не введён `х == 0`,
   и для каждого введённого числа проверяет, является ли число простым 
   (число является простым, если оно не делится без остатка ни на одно другое число, кроме 1 и самого себя). 
   Данную проверку оформить в виде функции от `x`, которая возвращает булевский результат: истинно, если число `x` не делится ни на
   одно число от 2 до `x/2` (делить на числа больше `x/2`, очевидно, уже не требуется); 
   ложно, если делится хоть на одно &mdash; и вызывать эту функцию в цикле.
4. Посчитать и вывести в одном цикле от 10 до 100 все числа, которые состоят из либо двух цифр,
   идущих подряд (например, 12), либо в обратную сторону (например, 21). Выводить эти числа, предваряя вывод текстом с указанием,
   какой вид числа выводится.

[Следующая лекция](./lecture_05.md) [Оглавление](./README.md) [Предыдущая лекция](./lecture_03.md) 


[Алгебра логики]: https://ru.wikipedia.org/wiki/%D0%90%D0%BB%D0%B3%D0%B5%D0%B1%D1%80%D0%B0_%D0%BB%D0%BE%D0%B3%D0%B8%D0%BA%D0%B8

