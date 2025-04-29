Slug: python_type_challenges
Date: 2025/04/28
Category: Python
Title: Прохождение Python Type Challenges

# Прохождение Python Type Challenges

Для тренировки и проверки навыков типизации в Python есть интересный
челлендж - [Python Type Challenges](https://python-type-challenges.zeabur.app/).
На сайте можно непосредственно выполнять задания и тут же их проверять.

Всего 4 уровня сложности:

- [Базовый уровень](#basic)
- [Средний уровень](#intermediate)
- [Продвинутый уровень](#advanced)
- [Экстремальный уровень](#extreme)

## Базовый уровень {#basic}

- [Произвольный тип](#any)
- [Словарь](#dict)
- [Запрет переопределения](#final)
- [Именованные аргументы](#kwargs)
- [Список](#list)
- [Опциональные аргумент](#optional)
- [Обязательный аргумент](#parameter)
- [Возвращаемый тип](#return)
- [Кортеж](#tuple)
- [Пользовательский тип](#typealias)
- [Объединение типов](#union)
- [Переменная](#variable)

### Произвольный тип {#any}

Измените функцию `foo` таким образом, чтобы она принимала
аргумент произвольного типа.

```python
def foo():
    ...
```

Решение:

```python
from typing import Any

def foo(x: Any):
    ...
```

Тестовые примеры:

```python
foo(1)
foo("10")

foo(1, 2)  # Ошибочный вариант
```

### Словарь {#dict}

Измените функцию `foo` таким образом, чтобы она принимала аргумент типа
`dict`, ключи и значения которого являются строками.

```python
def foo():
    pass
```

Решение:

```python
def foo(x: dict[str, str]):
    pass
```

Тестовые примеры:

```python
foo({"foo": "bar"})

foo({"foo": 1})  # Ошибочный вариант
```

### Запрет переопределения {#final}

Аннотируйте переменную `my_list` таким образом, чтобы ее нельзя было переназначить.

```python
my_list = []
```

Решение:

```python
from typing import Final

my_list: Final[list[int]] = []
```

Тестовые примеры:

```python
my_list.append(1)

my_list = []  # Ошибочный вариант
my_list = "something else"  # Ошибочный вариант
```

### Именованные аргументы {#kwargs}

Измените аннотацию функции `foo` таким образом, чтобы она принимала
произвольное количество именованных целочисленных или строковых аргументов.

```python
def foo(**kwargs):
    ...
```

Решение:

```python
def foo(**kwargs: int | str):
    ...
```

Тестовые примеры:

```python
foo(a=1, b="2")

foo(a=[1])  # Ошибочный вариант
```

### Список {#list}

Измените аннотацию функции `foo` таким образом, чтобы она принимала
список строк.

```python
def foo(x):
    pass
```

Решение:

```python
def foo(x: list[str]):
    pass
```

Тестовые примеры:

```python
foo(["foo", "bar"])

foo(["foo", 1])  # Ошибочный вариант
```

### Опциональные аргумент {#optional}

Измените аннотацию функции `foo` таким образом, чтобы она принимала
опциональный целочисленный аргумент.

```python
def foo(x):
    pass
```

Решение:

```python
def foo(x: int | None = None):
    pass
```

Тестовые примеры:

```python
foo(10)
foo(None)
foo()

foo("10")  # Ошибочный вариант
```

### Обязательный аргумент {#parameter}

Измените аннотацию функции `foo` таким образом, чтобы она принимала
обязательный целочисленный аргумент.

```python
def foo(x):
    pass
```

Решение:

```python
def foo(x: int):
    pass
```

Тестовые примеры:

```python
foo(10)

foo("10")  # Ошибочный вариант
```

### Возвращаемый тип {#return}

Измените аннотацию функции `foo`, чтобы обозначить возвращаемое
целочисленное значение.

```python
def foo():
    return 1
```

Решение:

```python
def foo() -> int:
    return 1
```

Тестовые примеры:

```python
from typing import assert_type

assert_type(foo(), int)
assert_type(foo(), str)
```

### Кортеж {#tuple}

Измените аннотацию функции `foo` таким образом, чтобы она принимала кортеж
из двух элементов - строки и целого числа.

```python
def foo(x):
    pass
```

Решение:

```python
def foo(x: tuple[str, int]):
    pass
```

Тестовые примеры:

```python
foo(("foo", 1))

foo((1, 2))  # Ошибочный вариант
foo(("foo", "bar"))  # Ошибочный вариант
foo((1, "foo"))  # Ошибочный вариант
```

### Пользовательский тип {#typealias}

Объявите тип `Vector`, который представляет собой список чисел с плавающей
точкой.

Решение:

```python
type Vector = list[int | float]
```

Тестовые примеры:

```python
def foo(v: Vector):
    ...

foo([1.1, 2])

foo(1)  # Ошибочный вариант
foo(["1"])  # Ошибочный вариант
```

### Объединение типов {#union}

Измените аннотацию функции `foo` таким образом, чтобы она принимала
либо строку либо целое число.

```python
def foo(x):
    pass
```

Решение:

```python
def foo(x: str | int):
    pass
```

Тестовые примеры:

```python
foo("foo")
foo(1)

foo([])  # Ошибочный вариант
```

### Переменная {#variable}

Аннотируйте тип переменной `a` таким образом, чтобы она могла принимать
только целочисленные значения.

```python
from typing import Any

a: Any
```

Решение:

```python
a: int
```

Тестовые примеры:

```python
a = 2

a = "1"  # Ошибочный вариант
```

## Средний уровень {#intermediate}

- [Awaitable объект](#await)
- [Вызываемый объект](#callable)
- [Атрибут класса](#class-var)
- [Простой декоратор](#simple-decorator)
- [Пустой кортеж](#empty-tuple)
- [Универсальная функция 1](#generic)
- [Универсальная функция 2](#generic2)
- [Универсальная функция 3](#generic3)
- [Атрибут экземпляра](#instance-var)
- [Литерал](#literal)
- [Строковый литерал](#literalstring)
- [`self`](#self)
- [Типизированный словарь 1](#typed-dict)
- [Типизированный словарь 2](#typed-dict2)
- [Типизированный словарь 3](#typed-dict3)
- [Распаковка](#unpack)

### Awaitable объект {#await}

Измените функцию `run_async` таким образом, чтобы она принимала awaitable
объект, возвращающий целое число.

```python
def run_async():
    ...
```

Решение (вариант 1):

```python
from collections.abc import Awaitable

def run_async(func: Awaitable[int]):
    ...
```

Решение (вариант 2):

!!! tip
    В качестве замены `Awaitable` можно указать любых наследников, например класс `Coroutine`

```python
from collections.abc import Coroutine

def run_async(func: Coroutine[None, None, int]):
    ...
```

Тестовые примеры:

```python
from asyncio import Queue

queue: Queue[int] = Queue()
queue2: Queue[str] = Queue()

async def async_function() -> int:
    return await queue.get()

async def async_function2() -> int:
    return await queue2.get()

run_async(async_function())

run_async(1)  # Ошибочный вариант
run_async(async_function2())  # Ошибочный вариант
```

### Вызываемый объект {#callable}

Объявите вызываемый тип, который должен принимать обязательный аргумент
строкового типа и возвращать `None` (*имя аргумента может быть произвольным*).

```python
SingleStringInput = ...
```

Решение:

```python
from collections.abc import Callable

SingleStringInput = Callable[[str], None]
```

Тестовые примеры:

```python
def accept_single_string_input(func: SingleStringInput) -> None:
    ...

def string_name(name: str) -> None:
    ...

def string_value(value: str) -> None:
    ...

def int_value(value: int) -> None:
    ...

def new_name(name: str) -> str:
    return name


accept_single_string_input(string_name)
accept_single_string_input(string_value)

accept_single_string_input(int_value)  # Ошибочный вариант
accept_single_string_input(new_name)  # Ошибочный вариант
```

### Атрибут класса {#class-var}

Дополните класс `Foo` атрибутом класса `bar` целочисленного типа.

```python
class Foo:
    ...
```

Решение:

```python
from typing import ClassVar

class Foo:
    bar: ClassVar[int]
```

Тестовые примеры:

```python
Foo.bar = 1

Foo.bar = "1"  # Ошибочный вариант
Foo().bar = 1  # Ошибочный вариант
```

### Простой декоратор {#simple-decorator}

Измените аннотацию декоратора, который обертывает функцию и возвращает
функцию с той же сигнатурой.

```python
from typing import Callable, TypeVar

def decorator(func):
    return func
```

Решение (вариант 1, для версий >= 3.12):

```python
from typing import Callable


def decorator[**P, R](func: Callable[P, R]) -> Callable[P, R]:
    return func
```

Подробнее см. в [документации](https://docs.python.org/3/library/typing.html#typing.ParamSpec).

Решение (вариант 2):

```python
from typing import Callable


def decorator[T: Callable](func: T) -> T:
    return func
```

Тестовые примеры:

```python
@decorator
def foo(a: int, *, b: str) -> None:
    ...

@decorator
def bar(c: int, d: str) -> None:
    ...

foo(1, b="2")
bar(c=1, d="2")

foo(1, "2")  # Ошибочный вариант
foo(a=1, e="2")  # Ошибочный вариант
decorator(1)  # Ошибочный вариант
```

### Пустой кортеж {#empty-tuple}

Измените аннотацию функции `foo` таким образом, чтобы она принимала пустой кортеж.

```python
def foo(x):
    pass
```

Решение:

```python
def foo(x: tuple[()]):
    pass
```

Тестовые примеры:

```python
foo(())

foo((1, ))  # Ошибочный вариант
```

### Универсальная функция 1 {#generic}

Измените аннотацию функции `add` таким образом, чтобы она принимала два
аргумента одинакового типа и возвращала значение того же типа.

```python
def add(a, b):
    ...
```

Решение:

```python
def add[T](a: T, b: T) -> T:
    ...
```

Тестовые примеры:

```python
from typing import List, assert_type

assert_type(add(1, 2), int)
assert_type(add("1", "2"), str)
assert_type(add(["1"], ["2"]), List[str])

assert_type(add(1, "2"), int)  # Ошибочный вариант
```

### Универсальная функция 2 {#generic2}

Измените аннотацию функции `add` таким образом, чтобы она принимала два
аргумента одинакового типа и возвращала значение того же типа. Типом может
быть либо строка либо целое число.

```python
def add(a, b):
    ...
```

Решение:

```python
def add[T: (int, str)](a: T, b: T) -> T:
    ...
```

Тестовые примеры:

```python
from typing import List, assert_type

assert_type(add(1, 2), int)
assert_type(add("1", "2"), str)

add(["1"], ["2"])  # Ошибочный вариант
add("1", 2)  # Ошибочный вариант
```

### Универсальная функция 3 {#generic3}

Измените аннотацию функции `add` таким образом, чтобы она принимала
аргумент и возвращала значение того же типа. Типом может
быть только целое число или его подклассы.

```python
def add(a):
    ...
```

Решение:

```python
def add[T: int](a: T) -> T:
    ...
```

Тестовые примеры:

```python
from typing import List, assert_type
class MyInt(int):
    pass

assert_type(add(1), int)
assert_type(add(MyInt(1)), MyInt)
assert_type(add("1"), str)

add(["1"], ["2"])  # Ошибочный вариант
add("1", 2)  # Ошибочный вариант
```

### Атрибут экземпляра {#instance-var}

Добавьте в класс `Foo` атрибут экземпляра `bar` целочисленного типа.

```python
class Foo:
    ...
```

Решение:

```python
class Foo:
    bar: int
```

Тестовые примеры:

```python
foo = Foo()
foo.bar = 1

foo.bar = "1"  # Ошибочный вариант
```

### Литерал {#literal}

Измените аннотацию функции `foo` таким образом, чтобы она принимала
аргумент строкового типа только с двумя значениями `left` или `right`.

```python
def foo(direction):
    ...
```

Решение:

```python
from typing import Literal

def foo(direction: Literal['left', 'right']):
    ...
```

Тестовые примеры:

```python
foo("left")
foo("right")

a = "".join(["l", "e", "f", "t"])
foo(a)  # Ошибочный вариант
```

### Строковый литерал {#literalstring}

Измените аннотацию функции `execute_query`, которая выполняет SQL запрос,
а также может предотвращать атаки с использованием SQL-инъекций.

```python
from typing import Iterable

def execute_query(sql, parameters: Iterable[str] = ...):
    ...
```

Решение:

```python
from typing import Iterable, LiteralString


def execute_query(sql: LiteralString, parameters: Iterable[str] = ...):
    ...
```

Тестовые примеры:

```python
def query_user(user_id: str):
    query = f"SELECT * FROM data WHERE user_id = {user_id}"
    execute_query(query)  # Ошибочный вариант

def query_data(user_id: int, limit: bool) -> None:
    query = """
        SELECT
            user.name
            user.age
        FROM data
        WHERE user_id = ?
    """
    if limit:
        query += " LIMIT 1"
    execute_query(query, (user_id, ))
```

### self {#self}

Измените аннотацию метода `return_self` таким образом, чтоба она
возвращала экземпляр текущего класса.

```python
import typing

class Foo:
    def return_self(self):
        ...
```

Решение (вариант 1):

```python
import typing

class Foo:
    def return_self(self) -> typing.Self:
        ...
```

Решение (вариант 2, устаревший):

```python
from typing import TypeVar

Self = TypeVar("Self", bound="Foo")

class Foo:
    def return_self(self: Self) -> Self:
        ...
```

Тестовые примеры:

```python
class SubclassOfFoo(Foo):
    pass

f: Foo = Foo().return_self()
sf: SubclassOfFoo = SubclassOfFoo().return_self()
sf: SubclassOfFoo = Foo().return_self()  # Ошибочный вариант
```

### Типизированный словарь 1 {#typed-dict}

Определите класс `Student`, который представляет собой словарь с тремя ключами:

- `name` в виде строки
- `age` в виде целого числа
- `school` в виде строки

Решение:

```python
from typing import TypedDict


class Student(TypedDict):
    name: str
    age: int
    school: str
```

Тестовые примеры:

```python
a: Student = {"name": "Tom", "age": 15, "school": "Hogwarts"}
assert Student(name="Tom", age=15, school="Hogwarts") ==  dict(name="Tom", age=15, school="Hogwarts")

a: Student = {"name": 1, "age": 15, "school": "Hogwarts"}  # Ошибочный вариант
a: Student = {(1,): "Tom", "age": 2, "school": "Hogwarts"}  # Ошибочный вариант
a: Student = {"name": "Tom", "age": "2", "school": "Hogwarts"}  # Ошибочный вариант
a: Student = {"name": "Tom", "age": 2}  # Ошибочный вариант
```

### Типизированный словарь 2 {#typed-dict2}

Определите класс `Student`, который представляет собой словарь с тремя ключами:

- `name` в виде строки
- `age` в виде целого числа
- `school` в виде строки (опциональное поле)

Решение:

```python
from typing import TypedDict, NotRequired

class Student(TypedDict):
    name: str
    age: int
    school: NotRequired[str]
```

Тестовые примеры:

```python
a: Student = {"name": "Tom", "age": 15}
a: Student = {"name": "Tom", "age": 15, "school": "Hogwarts"}
a: Student = {"name": 1, "age": 15, "school": "Hogwarts"}  # Ошибочный вариант
a: Student = {(1,): "Tom", "age": 2, "school": "Hogwarts"}  # Ошибочный вариант
a: Student = {"name": "Tom", "age": "2", "school": "Hogwarts"}  # Ошибочный вариант
a: Student = {"z": "Tom", "age": 2}  # Ошибочный вариант
assert Student(name="Tom", age=15) == dict(name="Tom", age=15)
assert Student(name="Tom", age=15, school="Hogwarts") ==  dict(name="Tom", age=15, school="Hogwarts")
```

### Типизированный словарь 3 {#typed-dict3}

Определите класс `Person`, который представляет собой словарь с пятью
ключами:

- name в виде строки (обязательное)
- age в виде целого числа (опциональное)
- gender в виде строки (опциональное)
- address в виде строки (опциональное)
- email в виде строки (опциональное)

Решение:

```python
from typing import TypedDict, Required


class Person(TypedDict, total=False):
    name: Required[str]
    age: int
    gender: str
    address: str
    email: str
```

Тестовые примеры:

```python
a: Person = {
    "name": "Capy",
    "age": 1,
    "gender": "Male",
    "address": "earth",
    "email": "capy@bara.com",
}
a: Person = {"name": "Capy"}

a: Person = {
    "age": 1,
    "gender": "Male",
    "address": "",
    "email": "",
}  # Ошибочный вариант

```

### Распаковка {#unpack}

Измените аннотацию функции `foo` таким образом, чтобы она принимала
именованные аргументы `name` строкового типа и `age` целочисленного типа.

```python
from typing import TypedDict


class Person(TypedDict):
    name: str
    age: int


def foo(**kwargs):
    ...
```

Решение:

```python
from typing import TypedDict, Unpack


class Person(TypedDict):
    name: str
    age: int


def foo(**kwargs: Unpack[Person]):
    ...
```

Тестовые примеры:

```python
person: Person = {
    "name": "The Meaning of Life",
    "age": 1983,
}
foo(**person)
foo(**{"name": "Brian", "age": 30})

foo(**{"name": "Brian"})  # Ошибочный вариант
person2: dict[str, object] = {"name": "Brian", "age": 30}
foo(**person2)  # Ошибочный вариант
foo(**{"name": "Brian", "age": "1979"})  # Ошибочный вариант
```

## Продвинутый уровень {#advanced}

- [Протокол буфера](#buffer)
- [Протокол вызываемого объекта](#callable-protocol)
- [Декоратор с аргументов](#decorator)
- [Дескриптор](#descriptor)
- [Копирование объекта](#forward)
- [Генератор](#generator)
- [Универсальный класс](#generic-class)
- [Запрет вызова функции 1](#never)
- [Запрет вызова функции 2](#never2)
- [Перегрузка функций](#overload)
- [Перегрузка функций с литералами](#overload-literal)
- [Декоратор в виде класса](#paramspec)
- [Протокол](#protocol)
- [Рекурсивный тип](#recursive)
- [Фабрика](#type)
- [Типизированный словарь 4](#typed-dict4)
- [Сужение типов](#typeguard)
- [`typeshed`](#typeshed)
- [Вариативные обобщения](#variadic-generics)

### Протокол буфера {#buffer}

Измените аннотацию функции `foo` таким образом, чтобы она принимала все
объекты, реализующие протокол буфера.

```python
def read_buffer(b):
    ...
```

Решение:

```python
from collections.abc import Buffer

def read_buffer(b: Buffer):
    ...
```

Тестовые примеры:

```python
from array import array

class MyBuffer:
    def __init__(self, data: bytes):
        self.data = data = bytearray(data)
        self.view = None
    
    def __buffer__(self, flags: int) -> memoryview:
        self.view = memoryview(self.data)
        return self.view

read_buffer(b"foo")
read_buffer(memoryview(b"foo"))
read_buffer(array("l", [1, 2, 3, 4, 5]))
read_buffer(MyBuffer(b"foo"))

read_buffer("foo")  # Ошибочный вариант
read_buffer(1)  # Ошибочный вариант
read_buffer(["foo"])  # Ошибочный вариант
```

### Протокол вызываемого объекта {#callable-protocol}

Определите вызываемый тип, который принимает строковый аргумент с
именем `name` и возвращает `None`.

```python
class SingleStringInput:
    ...
```

Решение:

```python
from typing import Protocol

class SingleStringInput(Protocol):
    def __call__(self, name: str) -> None:
        ...
```

Тестовые примеры:

```python
def accept_single_string_input(func: SingleStringInput) -> None:
    func(name="name")

def string_name(name: str) -> None:
    ...

def string_value(value: str) -> None:
    ...

def return_string(name: str) -> str:
    return name

accept_single_string_input(string_name)

accept_single_string_input(string_value)  # Ошибочный вариант
accept_single_string_input(return_string)  # Ошибочный вариант
```

### Декоратор с аргументов {#decorator}

Измените аннотацию декоратора `decorator` таким образом, чтобы он принимал
и возвращал функцию с той же сигнатурой, а также аргумент `message`
строкового типа.

```python
def decorator(message):
    ...
```

Решение:

```python
from collections.abc import Callable

def decorator[T: Callable](message: str) -> T:
    ...
```

Тестовые примеры:

```python
@decorator(message="x")
def foo(a: int, *, b: str) -> None:
    ...

@decorator  # Ошибочный вариант
def bar(a: int, *, b: str) -> None:
    ...

foo(1, b="2")

foo(1, "2")  # Ошибочный вариант
foo(a=1, e="2")  # Ошибочный вариант
decorator(1)  # Ошибочный вариант
```

### Дескриптор {#descriptor}

Аннотируйте метод `__get__` класса дескриптора.

```python
class Descriptor:
    def __get__(self, instance, owner):
        ...
```

Решение:

```python
from typing import Any, Self, overload

class Descriptor:
    @overload
    def __get__(self, instance: None, owner: type) -> Self:
        """you don't need to implement this"""
        ...
    @overload
    def __get__(self, instance: Any, owner: type) -> str:
        """you don't need to implement this"""
        ...

    def __get__(self, instance: Any | None, owner: type) -> Self | str:
        """you don't need to implement this"""
        ...
```

Тестовые примеры:

```python
class TestClass:
    a = Descriptor()

def descriptor_self(x: Descriptor) -> None:
    ...

def string_value(x: str) -> None:
    ...

descriptor_self(TestClass.a)
string_value(TestClass().a)

descriptor_self(TestClass().a)  # Ошибочный вариант
string_value(TestClass.a)  # Ошибочный вариант
```

### Копирование объекта {#forward}

Исправьте ошибку в аннотации типов для метода `copy`.

```python
class MyClass:
    def __init__(self, x: int) -> None:
        self.x = x

    # TODO: Fix the type hints of `copy` to make it type check
    def copy(self) -> MyClass:
        copied_object = MyClass(x=self.x)
        return copied_object
```

Решение (вариант 1):

```python
class MyClass:
    def __init__(self, x: int) -> None:
        self.x = x

    # TODO: Fix the type hints of `copy` to make it type check
    def copy(self) -> 'MyClass':
        copied_object = MyClass(x=self.x)
        return copied_object
```

Решение (вариант 2):

```python
from __future__ import annotations

class MyClass:
    def __init__(self, x: int) -> None:
        self.x = x

    def copy(self) -> MyClass:
        copied_object = MyClass(x=self.x)
        return copied_object
```

Решение (вариант 3, но изменен код задачи):

```python
from typing import Self

class MyClass:
    def __init__(self, x: int) -> None:
        self.x = x

    def copy(self) -> Self:
        copied_object = self.__class__(x=self.x)
        return copied_object
```

Тестовые примеры:

```python
from typing import assert_type

inst = MyClass(x=1)
assert_type(inst.copy(), MyClass)
```

### Генератор {#generator}

Аннотируйте генератор `gen` таким образом, чтобы он выдавал целое число
и принимал строку, но ничего не возвращал.

```python
def gen():
    ...
```

Решение:

```python
from collections.abc import Generator

def gen() -> Generator[int, str, None]:
    ...
```

Тестовые примеры:

```python
from typing import assert_type

generator = gen()
assert_type(next(generator), int)
generator.send("sss")

generator.send(3)  # Ошибочный вариант
```

### Универсальный класс {#generic-class}

Аннотируйте универсальный класс `Stack`. Его экземпляр может быть создан
с определенным типом, при этом метод `push` принимает объект указанного
типа, а `pop` возвращает объект того же типа.

```python
class Stack:
    def __init__(self) -> None:
        self.items = []

    def push(self, item) -> None:
        self.items.append(item)

    def pop(self):
        return self.items.pop()
```

Решение:

```python
class Stack[T]:
    def __init__(self) -> None:
        self.items: list[T] = []

    def push(self, item: T) -> None:
        self.items.append(item)

    def pop(self) -> T:
        return self.items.pop()
```

Тестовые примеры:

```python
from typing import assert_type

s = Stack[int]()
s.push(1)
assert_type(s.pop(), int)

s.push("foo")  # Ошибочный вариант
assert_type(s.pop(), str)  # Ошибочный вариант
```

### Запрет вызова функции 1 {#never}

Аннотируйте функцию, которую не следует вызывать.

```python
def never_call_me(arg):
    pass
```

Решение:

```python
from typing import Never

def never_call_me(arg: Never):
    pass
```

Тестовые примеры:

```python
def int_or_str(arg: int | str) -> None:
    never_call_me(arg)  # Ошибочный вариант
    match arg:
        case int():
            print("It's an int")
        case str():
            print("It's a str")
        case _:
            never_call_me(arg)
```

См. [пример](https://typing.python.org/en/latest/guides/unreachable.html#assert-never-and-exhaustiveness-checking)
использования `Never` для проверки невозможных вариантов исполнения.

### Запрет вызова функции 2 {#never2}

Реализуйте функцию `stop`, чтобы она удовлетворяла типизации.

```python
from typing import Never

def stop() -> Never:
    ...
```

Решение:

```python
from typing import Never

def stop() -> Never:
    raise ValueError("Error!")
```

Тестовые примеры:

```python
from typing import assert_never

assert_never(stop())
```

### Перегрузка функций {#overload}

Аннотируйте функцию `process` таким образом, чтобы:

- когда в качестве `response` передают `bytes` возвращается строка
- когда в качестве `response` передают `int` возвращается кортеж из целого числа и строки
- когда в качестве `response` передают `None` возвращается `None`

```python
def process(response: int | bytes | None) -> str | None | tuple[int, str]:
    ...
```

Решение:

```python
from typing import overload

@overload
def process(response: bytes) -> str:
    ...

@overload
def process(response: int) -> tuple[int, str]:
    ...

@overload
def process(response: None) -> None:
    ...

def process(response: int | bytes | None) -> str | None | tuple[int, str]:
    ...
```

Тестовые примеры:

```python
from typing import assert_type

assert_type(process(b"42"), str)
assert_type(process(42), tuple[int, str])
assert_type(process(None), None)

assert_type(process(42), str)  # Ошибочный вариант
assert_type(process(None), str)  # Ошибочный вариант
assert_type(process(b"42"), tuple[int, str])  # Ошибочный вариант
assert_type(process(None), tuple[int, str])  # Ошибочный вариант
assert_type(process(42), str)  # Ошибочный вариант
assert_type(process(None), str)  # Ошибочный вариант
```

### Перегрузка функций с литералами {#overload-literal}

Аннотируйте функцию `foo` таким образом, чтобы:

- если второй аргумент равен 1, возвращалось целое число
- если второй аргумент равен 2, возвращалась строка
- если второй аргумент равен 3, возвращался список
- в противном случае возвращался первый аргумент

```python
def foo(value, flag):
    ...
```

Решение:

```python
from typing import overload, Any, Literal

@overload
def foo(value: Any, flag: Literal[1]) -> int:
    ...

@overload
def foo(value: Any, flag: Literal[2]) -> str:
    ...

@overload
def foo(value: Any, flag: Literal[3]) -> list[Any]:
    ...

@overload
def foo[T](value: T, flag: Any) -> T:
    ...

def foo(value: Any, flag: Any) -> Any:
    ...
```

Тестовые примеры:

```python
foo("42", 1).bit_length()
foo(42, 2).upper()
foo(True, 3).append(1)
foo({}, "4").keys()

foo("42", 1).upper()  # Ошибочный вариант
foo(42, 2).append(1)  # Ошибочный вариант
foo(True, 3).bit_length()  # Ошибочный вариант
foo({}, "4").upper()  # Ошибочный вариант
```

### Декоратор в виде класса {#paramspec}

Аннотируйте класс `Wrap`, чтобы его можно было вызывать с теми же
аргументами, что и функцию, которую он декорирует.

```python
class Wrap:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        return self.func(*args, **kwargs)
```

Решение:

```python
from collections.abc import Callable

class Wrap[**P, R]:
    def __init__(self, func: Callable[P, R]) -> None:
        self.func = func

    def __call__(self, *args: P.args, **kwargs: P.kwargs) ->R:
        return self.func(*args, **kwargs)
```

Тестовые примеры:

```python
from typing import assert_type

@Wrap
def add(a: int, b: int) -> int:
    return a + b

@Wrap
def replace_wildcard(string: str, replacement: str, *, count: int = -1) -> str:
    return string.replace("*", replacement, count)

assert_type(add(1, 2), int)
assert_type(replace_wildcard("Hello *", "World"), str)
assert_type(replace_wildcard("Hello *", "World", 1), str)

replace_wildcard("Hello *", 1)  # Ошибочный вариант
replace_wildcard("Hello *", "World", 1)  # Ошибочный вариант
```

### Протокол {#protocol}

Определите протокол `SupportsQuack`, который поддерживает метод `quack`.

```python
from typing import Protocol

class SupportsQuack:
    ...
```

Решение:

```python
from typing import Protocol

class SupportsQuack(Protocol):
    def quack(self) -> None:
        ...
```

Тестовые примеры:

```python
class Duck:
    def quack(self) -> None:
        print("quack!")

class Dog:
    def bark(self) -> None:
        print("bark!")

duck: SupportsQuack = Duck()
dog: SupportsQuack = Dog()  # Ошибочный вариант
```

### Рекурсивный тип {#recursive}

Определите тип `Tree`, представляющий словарь, ключами которого являются
строки, а значениями тот же тип `Tree`.

```python
Tree = ...
```

Решение (python >= 3.12):

```python
type Tree = dict[str, "Tree"]
```

Решение (python < 3.12):

```python
from typing import TypeAlias

Tree: TypeAlias = dict[str, 'Tree']
```

Тестовые примеры:

```python
def f(t: Tree):
    pass

f({})
f({"foo": {}})
f({"foo": {"bar": {}}})
f({"foo": {"bar": {"baz": {}}}})

f(1)  # Ошибочный вариант
f({"foo": []})  # Ошибочный вариант
f({"foo": {1: {}}})  # Ошибочный вариант

```

### Фабрика {#type}

Аннотируйте функцию `make_object` таким образом, чтобы аннотация типов
соответствовала реализации.

```python
def make_object(cls):
    return cls()
```

Решение:

```python
def make_object[T](cls: type[T]) -> T:
    return cls()
```

Тестовые примеры:

```python
class MyClass:
    pass

def f():
    pass

c = make_object(MyClass)
c = make_object(int)
c = make_object(f)  # Ошибочный вариант
c = make_object("sss")  # Ошибочный вариант
c = make_object(["sss"])  # Ошибочный вариант
```

### Типизированный словарь 4 {#typed-dict4}

Определите класс `Undergraduate`, используя предопределенный класс `Student`.
У `Undergraduate` должен быть дополнительный атрибут `major` строкового типа.

```python
from typing import TypedDict

class Student(TypedDict):
    name: str
    age: int
    school: str

class Undergraduate:
    ...
```

Решение:

```python
from typing import TypedDict


class Student(TypedDict):
    name: str
    age: int
    school: str


class Undergraduate(Student):
    major: str
```

Тестовые примеры:

```python
a: Undergraduate = {"name": "Tom", "age": 20, "school": "MIT", "major": "Math"}
assert Undergraduate(name="Tom", age=20, school="MIT", major="Math") == {
    "name": "Tom",
    "age": 20,
    "school": "MIT",
    "major": "Math",
}

a: Undergraduate = {"name": "Tom", "age": 20, "school": "MIT"}  # Ошибочный вариант
```

### Сужение типов {#typeguard}

Реализуйте пользовательскую функцию сужения типов `is_string`, которая
будет проверять что переданное значение является строкой.

```python
from typing import Any

def is_string(value: Any):
    return isinstance(value, str)
```

Решение:

```python
from typing import Any, TypeGuard

def is_string(value: Any) -> TypeGuard[str]:
    return isinstance(value, str)
```

Тестовые примеры:

```python
from typing import assert_type

a: str | None = "hello"
if is_string(a):
    assert_type(a, str)
else:
    assert_type(a, type(None))  # Ошибочный вариант
```

### `typeshed` {#typeshed}

Аннотируйте класс `MyContainer` таким образом, чтобы он поддерживал
операцию доступа к элементу по его имени через оператор квадратных
скобок, т.е. `[x]`.

```python
class MyContainer:
    ...
```

Решение:

```python
from _typeshed import SupportsItemAccess

class MyContainer(SupportsItemAccess):
    ...
```

Тестовые примеры:

```python
from typing import assert_type
from collections.abc import Mapping

c = MyContainer()
c[1] = 1
c["2"] = 2

print(c[1])
print(c["2"])

del c[1]
del c["2"]

assert_type(c, dict)  # Ошибочный вариант
assert_type(c, Mapping)  # Ошибочный вариант
```

### Вариативные обобщения {#variadic-generics}

Определите тип `Array`, который поддерживает операцию поэлементного
сложения двух массивов одинакового размера и типов.

```python
class Array:
    def __add__(self, other):
        ...
```

Решение:

```python
class Array[*Ts]:
    def __add__(self, other: "Array[*Ts]") -> "Array[*Ts]":
        ...
```

Тестовые примеры:

```python
from typing import assert_type

a: Array[float, int] = Array()
b: Array[float, int] = Array()
assert_type(a + b, Array[float, int])

c: Array[float, int, str] = Array()
assert_type(a + c, Array[float, int, str])  # Ошибочный вариант
```

## Экстремальный уровень {#extreme}

- [Объединение параметров](#concatenate)
- [Декоратор-конструктор](#constructor)
- [Декоратор, добавляющий параметр](#self-casting)
- [Последовательности](#variance)

### Объединение параметров {#concatenate}

Предположим, есть функция `foo`, первым параметром которой может быть
что угодно. Вы хотите использовать `foo`, но хотите ограничить первый
аргумент значением `Person`. Изменение исходного кода `foo` невозможно,
поэтому вы решаете написать функцию `transform`, чтобы преобразовать
`food` в нужную функцию.

```python
class Person:
    pass

def transform(f):
    def wrapper(value: Person, *args, **kwargs):
        return f(value, *args, **kwargs)

    return wrapper
```

Решение:

```python
from collections.abc import Callable
from typing import Concatenate

class Person:
    pass

def transform[**P, R](f: Callable[Concatenate[Person, P], R]):
    def wrapper(value: Person, *args: P.args, **kwargs: P.kwargs) -> R:
        return f(value, *args, **kwargs)

    return wrapper
```

Тестовые примеры:

```python
def foo(value, mode: str) -> None:
    pass

foo_with_person = transform(foo)
foo_with_person(Person(), "1")
foo_with_person(Person(), mode="1")
foo_with_person(1, "1")  # Ошибочный вариант
foo_with_person(Person(), 1)  # Ошибочный вариант
foo_with_person(Person(), "1", 2)  # Ошибочный вариант

def foo2(value, mode: str, *, maybe: bool) -> int:
    return 1

foo_with_person = transform(foo2)
foo_with_person(Person(), "1", maybe=True)
foo_with_person(value=Person(), mode="1", maybe=True)
foo_with_person(Person(), mode="1", maybe=True)
foo_with_person(Person(), mode="1")  # Ошибочный вариант
foo_with_person(Person(), 1, maybe=True)  # Ошибочный вариант
foo_with_person(Person(), "1", maybe=1)  # Ошибочный вариант
foo_with_person(Person(), "1", True)  # Ошибочный вариант
```

### Декоратор-конструктор {#constructor}

Определите декоратор `constructor_parameter`, который принимает тип `Foo`
и возвращает функцию-обертку с той же сигнатурой, что и у конструктора `Foo`.
При этом функция, декорированная с помощью `constructor_parameter`, может
быть вызвана с экземпляром `Foo`.

```python
def constructor_parameter[T](class_: T):
    ...
```

Решение:

```python
```

Тестовые примеры:

```python
```

### Декоратор, добавляющий параметр {#self-casting}

Аннотируйте декоратор класса `Fn`, который принимает вызываемый объект `f`.
Метод `transform_callable` класса `Fn` преобразует `f` в другой вызываемый
объект с дополнительным параметром `Any` в начале, сохраняя при этом остальные
части сигнатуры функции.

```python
class Fn:
    def __init__(self, f):
        self.f = f

    def transform_callable(self):
        ...
```

Решение (python >= 3.12):

```python
from collections.abc import Callable
from typing import Concatenate, Any

class Fn[**P, R]:
    def __init__(self, f: Callable[P, R]) -> None:
        self.f = f

    def transform_callable(self) -> Callable[Concatenate[Any, P], R]:
        ...
```

Решение (python < 3.12):

```python
R = TypeVar("R")
P = ParamSpec("P")

class Fn(Generic[R, P]):
    def __init__(self, f: Callable[P, R]):
        self.f = f

    def transform_callable(self) -> Callable[Concatenate[object, P], R]:
        ...
```

Тестовые примеры:

```python
from typing import assert_type, Any

@Fn
def example(a: int, b: str, c: float, *, d: bool = False) -> None:
    return

assert_type(example.f(1, "1", 1.0, d=False), None)

a: Any = 11111111
b = example.transform_callable()(a, 1, "1", 1.0, d=False)
assert_type(b, None)

example.transform_callable()(1, "1", 1.0, d=False)  # Ошибочный вариант
```

### Последовательности {#variance}

Аннотируйте функции `f` и `g`, чтобы тесты прошли успешно.

```python
def f(a):
    pass

def g(a):
    pass
```

Решение:

```python
from collections.abc import Sequence

def f(a: list[int | str]):
    pass

def g(a: Sequence[int | str]):
    pass
```

Тестовые примеры:

```python

l1: list[int] = [1, 2]
f(l1)  # Ошибочный вариант
g(l1)

l2: list[int | str] = [1, 2]
f(l2)
g(l2)

f(1)  # Ошибочный вариант
f("abc")  # Ошибочный вариант
g("abc")
g(b"abc")
g([1, "2"])
g((1, "2", 3))
g(1)  # Ошибочный вариант
g({1})  # Ошибочный вариант
```
