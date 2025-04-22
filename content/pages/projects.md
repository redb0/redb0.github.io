Slug: projects
Order: 002
Title: Проекты

<!-- https://github.com/simple-icons/simple-icons/blob/develop/slugs.md -->

Корпоративная SDK {#sdk}
=================

Python библиотеки и предоставляет функционал по авторизации, логированию,
резервному копированию, обработке исключений, соединению с базами данных,
конфигурации приложения, базовым моделям и пр. Библиотека позволяет
подключать стандартные API к приложению, написав минимум кода. SDK
используется во всех python проектах компании.

**Обязанности:**

- Сбор и формализация требований
- Проектирвоание архитектуры
- Постановка задач
- Реализация функционала
- Тестирование
- Документирование

**Команда:** 1 backend-разработчик

<img src="https://img.shields.io/badge/Python-999999?logo=python" title="Python" alt="Python" height="40"/>
<img src="https://img.shields.io/badge/FastAPI-999999?logo=fastapi" title="FastAPI" alt="FastAPI" height="40"/>
<img src="https://img.shields.io/badge/PostgreSQL-999999?logo=postgresql" title="PostgreSQL" alt="PostgreSQL" height="40"/>

----------

Система мониторинга и управления серверами {#ems}
==========================================

Система позволяет собирать инвентарные сведения, показания
сенсоров, записи журналов, общее сосотояние, управлять
питанием, подсветкой, обновлять прошивки, а также настраивать собственные
шаблоны мониторинга (границы показаний датчиков, критичность записей
журнала, изменениеинвентарных данных). Основаная проблема - работа с
медленными железками и нестабильной сетью. Реализовано в виде монолита,
где часть логики по сбору и обработки информации от оборудования
выполняется отдельными сервисами.

**Обязанности:**

- Проектирвоание архитектуры
- Постановка и декомпозиция задач
- Разработка бизнес логики на бэкенде
- Выступал в роли тех лида команды
- Проведение code review

**Команда:** 4 backend-разработчика, 3 frontend-разработчика, 1 аналитик, тестировщик, тим лид.

<img src="https://img.shields.io/badge/Python-999999?logo=python" title="Python" alt="Python" height="40"/>
<img src="https://img.shields.io/badge/FastAPI-999999?logo=fastapi" title="FastAPI" alt="FastAPI" height="40"/>
<img src="https://img.shields.io/badge/PostgreSQL-999999?logo=postgresql" title="PostgreSQL" alt="PostgreSQL" height="40"/>
<img src="https://img.shields.io/badge/Vault-999999?logo=vault" title="Vault" alt="Vault" height="40"/>
<img src="https://img.shields.io/badge/ClickHouse-999999?logo=clickhouse" title="ClickHouse" alt="ClickHouse" height="40"/>
<img src="https://img.shields.io/badge/RabbitMQ-999999?logo=rabbitmq" title="RabbitMQ" alt="RabbitMQ" height="40"/>
<img src="https://img.shields.io/badge/Docker-999999?logo=docker" title="Docker" alt="Docker" height="40"/>

----------

Веб-приложение поддержки процессов обработки персональных данных {#fz}
================================================================

Приложение позволяет пользователю контролировать персональные данные в
каждом из процессов компании, а также проводить аудиты в соответствии с
ФЗ-152. Оно реализовано на основе
[мультитенантной архитектуры](https://en.wikipedia.org/wiki/Multitenancy)
для поддержки независимой работы нескольких компаний.

- Описание (микросервис для РКН)

**Обязанности:**

- Проектирвоание архитектуры
- Постановка и декомпозиция задач
- Разработка бизнес логики на бэкенде
- Проведение code review
- Интеграции с внешними системами (сайт Роскомнадзора)

**Команда:** 4 backend-разработчика, 2 frontend-разработчика, 1 аналитик, тестировщик, тим лид.

<img src="https://img.shields.io/badge/Python-999999?logo=python" title="Python" alt="Python" height="40"/>
<img src="https://img.shields.io/badge/FastAPI-999999?logo=fastapi" title="FastAPI" alt="FastAPI" height="40"/>
<img src="https://img.shields.io/badge/PostgreSQL-999999?logo=postgresql" title="PostgreSQL" alt="PostgreSQL" height="40"/>
<img src="https://img.shields.io/badge/Vault-999999?logo=vault" title="Vault" alt="Vault" height="40"/>
<img src="https://img.shields.io/badge/MinIO-999999?logo=minio" title="MinIO" alt="MinIO" height="40"/>
<img src="https://img.shields.io/badge/YDB-999999?logo=data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTI4IiBoZWlnaHQ9IjEyOCIgdmlld0JveD0iMCAwIDEyOCAxMjgiIGZpbGw9Im5vbmUiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+CjxjaXJjbGUgY3g9IjY0IiBjeT0iNjQiIHI9IjY0IiBmaWxsPSIjMjM5OUZGIi8+CjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgY2xpcC1ydWxlPSJldmVub2RkIiBkPSJNMzYuOTYwNSAzMS45NTAzQzI3LjI5NzYgMzEuOTUwMyAxOS40NjQ0IDM0LjcwMDkgMTkuNDY0NCAzOS44NjA3VjY2LjY2NjdDMTkuNDY0NCA3MS44MjY2IDI3LjI5NzYgNzQuNTc3MiAzNi45NjA1IDc0LjU3NzJDNDAuMzQ2NCA3NC41NzcyIDQzLjUwNzYgNzQuMjM5NSA0Ni4xODU5IDczLjU3ODdWOTUuOTMzQzQ2LjE4NTkgMTAxLjA5MyA1NC4wMTkyIDEwMy44NDMgNjMuNjgyIDEwMy44NDNDNzMuMzQ0OSAxMDMuODQzIDgxLjE3ODEgMTAxLjA5MyA4MS4xNzgxIDk1LjkzM1Y3My40MTMyQzgzLjk4NiA3NC4xODMgODcuMzgxNyA3NC41NzcyIDkxLjAzOTYgNzQuNTc3MkMxMDAuNzAyIDc0LjU3NzIgMTA4LjUzNiA3MS44MjY2IDEwOC41MzYgNjYuNjY2N1YzOS44NjA3QzEwOC41MzYgMzQuNzAwOSAxMDAuNzAyIDMxLjk1MDMgOTEuMDM5NiAzMS45NTAzQzgxLjM3NjggMzEuOTUwMyA3My41NDM1IDM0LjcwMDkgNzMuNTQzNSAzOS44NjA3VjQ5Ljc2NDVINTQuNDU2NlYzOS44NjA3QzU0LjQ1NjYgMzQuNzAwOSA0Ni42MjMzIDMxLjk1MDMgMzYuOTYwNSAzMS45NTAzWk04MS4xNzgxIDcwLjg5ODVMOTAuNzIxNyA1OC4wMzU0SDgzLjcyMzNMNzguNzU1MyA2NC43NTY3QzgwLjI5NDggNjUuOTMzMSA4MS4xNzgxIDY3LjM5NDIgODEuMTc4MSA2OS4xMjdWNzAuODk4NVpNNzMuNTQzNSA2Mi4zODA1VjU1LjQ5MDVINTQuNDU2NlY2Mi4yMTVDNTcuMTM0OSA2MS41NTQyIDYwLjI5NjEgNjEuMjE2NSA2My42ODIgNjEuMjE2NUM2Ny4zMzk5IDYxLjIxNjUgNzAuNzM1NyA2MS42MTA3IDczLjU0MzUgNjIuMzgwNVpNNDguNjA5IDY0Ljc1NjVMNDMuNjQxMiA1OC4wMzU0SDM2LjY0MjhMNDYuMTg1OSA3MC44OTc5VjY5LjEyN0M0Ni4xODU5IDY3LjM5NDEgNDcuMDY5NCA2NS45MzI5IDQ4LjYwOSA2NC43NTY1Wk03OS44MzY4IDM2Ljk2OThDNzcuMDc4MSAzOC4xNjk5IDc2LjcyNDkgMzkuMzQyMSA3Ni43MjQ5IDM5LjkwMzFDNzYuNzI0OSA0MC40NjQgNzcuMDc4MSA0MS42MzYzIDc5LjgzNjggNDIuODM2M0M4Mi40NzUxIDQzLjk4NCA4Ni40MDY3IDQ0LjY3NDcgOTEuMDM5OSA0NC42NzQ3Qzk1LjY3MyA0NC42NzQ3IDk5LjYwNDYgNDMuOTg0IDEwMi4yNDMgNDIuODM2M0MxMDUuMDAyIDQxLjYzNjMgMTA1LjM1NSA0MC40NjQgMTA1LjM1NSAzOS45MDMxQzEwNS4zNTUgMzkuMzQyMSAxMDUuMDAyIDM4LjE2OTkgMTAyLjI0MyAzNi45Njk4Qzk5LjYwNDYgMzUuODIyMSA5NS42NzMgMzUuMTMxNCA5MS4wMzk5IDM1LjEzMTRDODYuNDA2NyAzNS4xMzE0IDgyLjQ3NTEgMzUuODIyMSA3OS44MzY4IDM2Ljk2OThaTTIyLjY0NTcgMzkuOTAzMUMyMi42NDU3IDM5LjM0MjEgMjIuOTk5IDM4LjE2OTkgMjUuNzU3NiAzNi45Njk4QzI4LjM5NiAzNS44MjIxIDMyLjMyNzUgMzUuMTMxNCAzNi45NjA3IDM1LjEzMTRDNDEuNTkzOSAzNS4xMzE0IDQ1LjUyNTQgMzUuODIyMSA0OC4xNjM4IDM2Ljk2OThDNTAuOTIyNCAzOC4xNjk5IDUxLjI3NTcgMzkuMzQyMSA1MS4yNzU3IDM5LjkwMzFDNTEuMjc1NyA0MC40NjQxIDUwLjkyMjQgNDEuNjM2MyA0OC4xNjM4IDQyLjgzNjNDNDUuNTI1NCA0My45ODQgNDEuNTkzOSA0NC42NzQ3IDM2Ljk2MDcgNDQuNjc0N0MzMi4zMjc1IDQ0LjY3NDcgMjguMzk2IDQzLjk4NCAyNS43NTc2IDQyLjgzNjNDMjIuOTk5IDQxLjYzNjMgMjIuNjQ1NyA0MC40NjQxIDIyLjY0NTcgMzkuOTAzMVpNNTIuNDc4OCA2Ni4yMzYxQzQ5LjcyMDIgNjcuNDM2MSA0OS4zNjY5IDY4LjYwODMgNDkuMzY2OSA2OS4xNjkzQzQ5LjM2NjkgNjkuNzMwMyA0OS43MjAyIDcwLjkwMjUgNTIuNDc4OCA3Mi4xMDI2QzU1LjExNzIgNzMuMjUwMyA1OS4wNDg3IDczLjk0MSA2My42ODE5IDczLjk0MUM2OC4zMTUxIDczLjk0MSA3Mi4yNDY2IDczLjI1MDMgNzQuODg1IDcyLjEwMjZDNzcuNjQzNiA3MC45MDI1IDc3Ljk5NjkgNjkuNzMwMyA3Ny45OTY5IDY5LjE2OTNDNzcuOTk2OSA2OC42MDgzIDc3LjY0MzYgNjcuNDM2MSA3NC44ODUgNjYuMjM2MUM3Mi4yNDY2IDY1LjA4ODQgNjguMzE1MSA2NC4zOTc2IDYzLjY4MTkgNjQuMzk3NkM1OS4wNDg3IDY0LjM5NzYgNTUuMTE3MiA2NS4wODg0IDUyLjQ3ODggNjYuMjM2MVoiIGZpbGw9IndoaXRlIi8+Cjwvc3ZnPgo=" title="YDB" alt="YDB" height="40"/>
<img src="https://img.shields.io/badge/Docker-999999?logo=docker" title="Docker" alt="Docker" height="40"/>

----------

Система оптимизации ЖД грузоперевозок {#navigator}
=====================================

[Система](https://habr.com/ru/companies/pgk/articles/583208/)
позволяет экономить расходы на порожний пробег вагонов за счет
автоматизации выбора оптимального маршрута, учитывая выполнение заданного
уровня сервиса и необходимый спрос со стороны клиентов. Решение включает
в себя функцию формирования рекомендаций для диспетчеров, разработанных
с помощью модели машинного обучения. Система реализована в виде
приложения с микросервисной архитектурой.

**Обязанности:**

- Разработка бизнес логики на бэкенде
- Разработка корпоратичных инструментов логирования и генерации документации
- Разработка микросервиса управления рассылками

**Команда:** 4 backend-разработчика, 1 frontend-разработчик, тим лид.

<img src="https://img.shields.io/badge/Python-999999?logo=python" title="Python" alt="Python" height="40"/>
<img src="https://img.shields.io/badge/FastAPI-999999?logo=fastapi" title="FastAPI" alt="FastAPI" height="40"/>
<img src="https://img.shields.io/badge/PostgreSQL-999999?logo=postgresql" title="PostgreSQL" alt="PostgreSQL" height="40"/>
<img src="https://img.shields.io/badge/Oracle-999999?logo=data:image/svg+xml;base64,PHN2ZyByb2xlPSJpbWciIHZpZXdCb3g9IjAgMCAyNCAyNCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48dGl0bGU+T3JhY2xlPC90aXRsZT48cGF0aCBkPSJNNy41NjY4OCwxOS41NjY4QTcuNTY2ODgsNy41NjY4OCAwIDAgMSAwLDEyYzAtNC4yMDM4MiAzLjM2MzA2LTcuNTY2ODggNy41NjY4OC03LjU2Njg4aDguODY2MjRDMjAuNjM2OTQsNC40MzMxMiAyNCw3Ljc5NjE4IDI0LDEyYzAsNC4yMDM4Mi0zLjM2MzA2LDcuNTY2ODgtNy41NjY4OCw3LjU2Njg4SDcuNTY2ODhtOC42MzY5NC0yLjY3NTE2YzIuNzUxNTksMCA0Ljg5MTcyLTIuMjE2NTYgNC44OTE3Mi00Ljg5MTcyIDAtMi43NTE1OS0yLjIxNjU2LTQuODkxNzItNC44OTE3Mi00Ljg5MTcySDcuNzk2MThjLTIuNzUxNTksMC00Ljg5MTcyLDIuMjE2NTYtNC44OTE3Miw0Ljg5MTcyIDAsMi42NzUxNiAyLjIxNjU2LDQuODkxNzIgNC44OTE3Miw0Ljg5MTcyaDguNDA3NjQiLz48L3N2Zz4=" title="Oracle" alt="Oracle" height="40"/>
<img src="https://img.shields.io/badge/Kafka-999999?logo=apachekafka" title="Kafka" alt="Kafka" height="40"/>
<img src="https://img.shields.io/badge/Redis-999999?logo=redis" title="Redis" alt="Redis" height="40"/>
<img src="https://img.shields.io/badge/Docker-999999?logo=docker" title="Docker" alt="Docker" height="40"/>
<img src="https://img.shields.io/badge/ELK-999999" title="ELK" alt="ELK" height="40"/>

----------

Спецификатор оборудования {#spec}
=========================

Веб-приложение для спецификации оборудования предназначено для
составления перечня компонент оборудовани (серверов, СХД и прочего), а
также возможности конвертации спецификации одного бренда в спецификацию
другого.

**Обязанности:**

- Сбор и формализация требований
- Постановка и декомпозиция задач
- Проектирвоание архитектуры
- Разработка бизнес логики на бэкенде

**Команда:** 1 backend-разработчик, 1 frontend-разработчик, 2 аналитика, тестировщик, тим лид.

<img src="https://img.shields.io/badge/Python-999999?logo=python" title="Python" alt="Python" height="40"/>
<img src="https://img.shields.io/badge/FastAPI-999999?logo=fastapi" title="FastAPI" alt="FastAPI" height="40"/>
<img src="https://img.shields.io/badge/MongoDB-999999?logo=mongodb" title="MongoDB" alt="MongoDB" height="40"/>
<img src="https://img.shields.io/badge/Docker-999999?logo=docker" title="Docker" alt="Docker" height="40"/>

----------

Веб-приложение оптимизации смешивания катализаторов {#cat}
===================================================

Веб-приложение позволяет пользователю составлять оптимальные смеси
материалов в зависимости от многих параметров (химический состав, масса,
приоритетные партии и др.) с целью максимизации массы перерабатываемых
материалов (модифицированная задача о
[диете Стиглера](https://en.wikipedia.org/wiki/Stigler_diet)).

**Обязанности:**

- Разработка оптимизатора (на основе [`HiGHS`](https://highs.dev/) и библиотеке [`pulp`](https://github.com/coin-or/pulp))
- Разработка бэкенд части с бизнес логикой и зачами оптимизации, запускаемыми через `Celery`
- Разработка пользовательского интерфейса на основе шаблонов и [`django-bootstrap-modal-forms`](https://github.com/trco/django-bootstrap-modal-forms)

**Команда:** 1 backend-разработчик, 1 frontend-разработчик, 1 аналитик.

<img src="https://img.shields.io/badge/Python-999999?logo=python" title="Python" alt="Python" height="40"/>
<img src="https://img.shields.io/badge/Django-999999?logo=django" title="Django" alt="Django" height="40"/>
<img src="https://img.shields.io/badge/JavaScript-999999?logo=javascript" title="JavaScript" alt="JavaScript" height="40"/>
<img src="https://img.shields.io/badge/PostgreSQL-999999?logo=postgresql" title="PostgreSQL" alt="PostgreSQL" height="40"/>
<img src="https://img.shields.io/badge/Celery-999999?logo=celery" title="Celery" alt="Celery" height="40"/>
<img src="https://img.shields.io/badge/LDAP-999999" title="LDAP" alt="LDAP" height="40"/>
<img src="https://img.shields.io/badge/Линейное программирование-999999" title="Линейное программирование" alt="Линейное программирование" height="40"/>

----------

Система раскроя круглых сеток {#mesh}
=============================

Система реализована в виде веб-приложения и позволяет оптимальным образом
располагать
[круглые каталитические сетоки](https://www.krastsvetmet.ru/products-and-services/industrial-appliances/catalog/catalytic-systems/)
на прямоугольном полотне с учетом различных ограничений (количество
резов на сетке, размеры и др.) одновременно подбирая его параметры
(размеры) таким образом, чтобы минимизировать количество отходов.

**Обязанности:**

- Сбор и формализация требований
- Наставничество стажеров (выступал в роли тим лида команды)
- Разработка алгоритма оптимизации
- Проектирование архитектуры

**Команда:** 2 backend-разработчика, тим лид.

<img src="https://img.shields.io/badge/Python-999999?logo=python" title="Python" alt="Python" height="40"/>
<img src="https://img.shields.io/badge/Django-999999?logo=django" title="Django" alt="Django" height="40"/>
<img src="https://img.shields.io/badge/JavaScript-999999?logo=javascript" title="JavaScript" alt="JavaScript" height="40"/>
<img src="https://img.shields.io/badge/PostgreSQL-999999?logo=postgresql" title="PostgreSQL" alt="PostgreSQL" height="40"/>
<img src="https://img.shields.io/badge/Celery-999999?logo=celery" title="Celery" alt="Celery" height="40"/>
<img src="https://img.shields.io/badge/LDAP-999999" title="LDAP" alt="LDAP" height="40"/>

----------

Стоматологическая система поставноки диагнозов {#dental}
==============================================

Система построена в виде модульного монолита и включает - личный кабинет
пользователя с возможность записи к врачу, личный кабинет врача с
возможность просматривать расписание и анкеты пациентов, модуль тестирования
(анкетирование пациентов, результаты анализов), модуль постановки диагнозов
на основе правил, и др.

**Обязанности:**

- Сбор и формализация требований
- Разработка бизнес логики

**Команда:** 2 backend-разработчика, 1 frontend-разработчик.

<img src="https://img.shields.io/badge/Python-999999?logo=python" title="Python" alt="Python" height="40"/>
<img src="https://img.shields.io/badge/Django-999999?logo=django" title="Django" alt="Django" height="40"/>
<img src="https://img.shields.io/badge/JavaScript-999999?logo=javascript" title="JavaScript" alt="JavaScript" height="40"/>
<img src="https://img.shields.io/badge/PostgreSQL-999999?logo=postgresql" title="PostgreSQL" alt="PostgreSQL" height="40"/>

----------

Раскрой слитка {#oci}
==============

Desctop приложение раскроя слитка оптимизирует последовательность
технологических операций по изготовлению
[фильерных питателей](https://www.krastsvetmet.ru/products-and-services/industrial-appliances/catalog/bushings-and-glass-melters/glass-and-basalt-fiber-brushings/)
из слитков драгоценных металлов с целью уменьшения количества отходов.

**Обязанности:**

- Разработка оптимизатора для задачи модифицированной
[раскроя слитка](https://iopscience.iop.org/article/10.1088/1742-6596/2373/3/032015/pdf)
- Разработка пользовательского интерфейса и бизнес-логики

**Команда:** 2 разработчика, аналитик, тестировщик.

<img src="https://img.shields.io/badge/Python-999999?logo=python" title="Python" alt="Python" height="40"/>
<img src="https://img.shields.io/badge/PyQt-999999?logo=qt" title="PyQt" alt="PyQt" height="40"/>
<img src="https://img.shields.io/badge/SQLite-999999?logo=sqlite" title="SQLite" alt="SQLite" height="40"/>
