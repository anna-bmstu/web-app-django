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


## Screenshots
#### Home page
Домашняя страница блога, на которой отображаются посты пользователей<br><br>
![home_page2](https://user-images.githubusercontent.com/55577096/183099269-ff3808eb-63a1-435d-97e9-b9d041e1367f.png)
#### Register
Регистрация пользователя<br><br>
![register_page](https://user-images.githubusercontent.com/55577096/182869620-1efd0082-6c78-47b2-b546-1e05004d1ef6.png)
#### Log in
После регистрации пользователь перенаправляется на страницу для входа в учетную запись<br><br>
![after_reg](https://user-images.githubusercontent.com/55577096/182869640-448f0320-53f8-4371-9ddc-298687740587.png)
#### Profile
Пользователь может зайти на страницу своего профиля. Здесь он может изменить никнейм, почту и дефолтную аватарку<br><br>
![profile](https://user-images.githubusercontent.com/55577096/183101761-dd863dab-5605-467c-986d-ff5d20ffb76a.png)
#### New post
Пользователь может написать пост<br><br>
![new_post](https://user-images.githubusercontent.com/55577096/183102808-14731eda-d314-432a-9555-54ef945dd5aa.png)
#### Post details
Страница поста. Пользователь может обновить или удалить свой пост<br><br>
![post_page](https://user-images.githubusercontent.com/55577096/183103543-132ec27e-2b84-45da-85a4-9ed3a51b2fc5.png)
#### Post delete
Подтверждение удаления<br><br>
![post_delete](https://user-images.githubusercontent.com/55577096/183103918-74c6451c-3f09-496e-987f-40a7ec7b178d.png)
#### Log out
![logout](https://user-images.githubusercontent.com/55577096/183104337-dd7a8cc4-b8ef-453b-9f57-2167a152a83a.png)
