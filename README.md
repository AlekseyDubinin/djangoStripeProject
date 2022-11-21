Задание:
-------

* Реализовать Django + Stripe API бэкенд со следующим функционалом и условиями:
* Django Модель `Item` с полями `(name, description, price) `
* API с двумя методами:
    * GET `/buy/{id}`, c помощью которого можно получить Stripe Session Id для оплаты выбранного Item. При выполнении
      этого метода c бэкенда с помощью python библиотеки stripe должен выполняться
      запрос` stripe.checkout.Session.create(...)` и полученный session.id выдаваться в результате запроса
    * GET `/item/{id}`, c помощью которого можно получить простейшую HTML страницу, на которой будет информация о
      выбранном `Item` и кнопка Buy. По нажатию на кнопку Buy должен происходить запрос на `/buy/{id}`, получение
      session_id и далее с помощью JS библиотеки Stripe происходить редирект на Checkout
      форму `stripe.redirectToCheckout(sessionId=session_id)`

* Залить решение на Github, описать запуск в README.md

* Опубликовать свое решение чтобы его можно было быстро и легко протестировать. 


Получение всех api ключей
-------------------------

Publishable key:
https://dashboard.stripe.com/apikeys

Secret key:
https://dashboard.stripe.com/apikeys

Webhooks:
https://dashboard.stripe.com/webhooks


### Для корректной работы нужно активировать приложение:
https://dashboard.stripe.com/settings/account


Запуск
------

```
git clone https://github.com/AlekseyDubinin/djangoStripeProject.git
cd stripe_task
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

#### Для админки:
```
python manage.py createsuperuser
```

Главная страница: http://localhost:8000/

Если сервер не отдаёт информацию, подождите пару секунд и перезагрузите страницу

Товары можно добавить через Админку:
http://127.0.0.1:8000/admin/

Пример Админки:
----------
![img.png](https://github.com/AlekseyDubinin/djangoStripeProject/blob/master/%20img/img_1.png)

Сервис
------

* `/` - товары в виде ссылки на item
* `admin/` - Админка
* `buy/<item_id>` - Купить товар
* `item/<item_id>` - Страница товара

Скриншоты
---------

#### Главная страница с ссылками на товары:

![img.png](https://github.com/AlekseyDubinin/djangoStripeProject/blob/master/%20img/img_2.png)

#### Товар и ссылка на оплату:

![img_2.png](https://github.com/AlekseyDubinin/djangoStripeProject/blob/master/%20img/img_3.png)

#### Оплата товара:

![img_1.png](https://github.com/AlekseyDubinin/djangoStripeProject/blob/master/%20img/img_4.png)
