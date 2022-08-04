# Веб-приложение 
Блог<br>
Пользователь может создать аккаунт, есть аккаунт уже есть,
то он может войти в него.
Также пользователь может зайти на страницу своего профиля и внести изменения: сменить никнейм, 
email и обновить фото профиля.

### Приложения
- blog<br>
Шаблоны с использованием Bootstrap (здесь базовый шаблон base.html)<br>
База данных, содержащая информацию о постах (таблица Post)<br><br>
- users<br> 
Регистрация пользователя<br>
Автоматическое создание профиля
<br><br>
Система аутентификации (log in/log out)<br>
Встроенные в django LoginView и LogoutView

  
В Django есть встроенная система аутентификации пользователей, которая входит в состав модуля django.contrib.auth.
Она обрабатывает учетные записи пользователей, группы и разрешения.
Система включает в себя:
- модель User в django.contrib.auth.models
- Permissions. Флаги, определяющие, может ли пользователь выполнять определенную задачу.
- Groups
- Формы в django.contrib.auth.forms (UserCreationForm)
- Подключаемая бэкэнд-система

Объекты User представляют людей, взаимодействующих с сайтом, и используются для ограничения доступа, регистрации профилей пользователей, 
связывания контента с создателем. Superuser и staff - это просто объекты User со специальным набором атрибутов.

Основные атрибуты пользователя по умолчанию: username, password, email, first_name, last_name.

Фильтры date

![home_page](https://user-images.githubusercontent.com/55577096/182869552-4560f7a3-0a04-48d5-8c4b-cfbedabe8b5a.png)

![register_page](https://user-images.githubusercontent.com/55577096/182869620-1efd0082-6c78-47b2-b546-1e05004d1ef6.png)
![after_reg](https://user-images.githubusercontent.com/55577096/182869640-448f0320-53f8-4371-9ddc-298687740587.png)
