# Проект интернет-магазина

В  проекте Django создано приложение Catalog и подключено к базе банных.
Реализованы HTML-шаблоны для домашней страницы и страницы с контакной информацией. Для стилизации страниц инспользован 
Bootstrap. Созданы контроллеры для отображения этих 2 страниц и страницы с товаром, настроена маршрутизация для контроллеров.

В приложении каталога реализованы модели Product и Category с их базовыми настройками. Для Product - наименование, описание, изображение, категория, цена за покупку, дата создания, дата последнего изменения. Для Category - наименование, описание.
Модели зарегистрированы в админке и настроено их отображение.
Настроена фильтрация продуктов по категории и  поиск по полям name и description.

С главной страницы можно переходить в контакты, каталог, карточки товаров и обратно. В каталоге отображены карточки товаров с изображениями. На главной выводится 3 карточки товаров.

Все контроллеры приложения Catalog переведены с FBV на CBV.

В приложение Catalog интегрировано приложение Blog для публикации тематических статей. 

Создана модель блоговой записи BlogPost с полями: заголовок, содержимое, изображение, дата создания, признак публикации (булевое поле), количество просмотров. Можно создавать статьи блога, редактировать их, удалять. После успешного редактирования записи идет перенаправление на просмотр этой статьи.

При открытии отдельной статьи увеличивается счетчик просмотров (метод get_object).

Настроена фильтрация опубликованных статей (метод get_queryset): отображаются только те, которые имеют положительный признак публикации.

## Установка:
Клонируйте репозиторий:
git@github.com:valentinaovsianik/Project_int_magazin.git


## Как запустить:
После клонирования репозитория выполните python manage.py runserver.


## Документация:
Описание проекта в файле README.md.


## Лицензия:
На проект распространяется [лицензия MIT](LICENSE).