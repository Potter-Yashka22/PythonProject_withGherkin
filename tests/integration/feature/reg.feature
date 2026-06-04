Feature: Регистрация
    Scenario: Успешный вход
        Given пользователь на главной странице
        When заполняет логин "standard_user"
        And заполняет пароль "secret_sauce"
        And нажимает кнопку "login-button"
        Then переходит на другую страницу
        And проверка адреса "inventory.html"
        And проверка заголовка "Products"

    Scenario Outline: Успешный вход  под разными пользователями
        Given пользователь на главной странице
        When заполняет логин "<login>"
        And заполняет пароль "<passw>"
        And нажимает кнопку "login-button"
        Then переходит на другую страницу
        And проверка адреса "inventory.html"
        And сделали скриншот "<screen>"

        Examples:
        | login         | passw        | screen |
        | standard_user | secret_sauce | 111 |
        | error_user    | secret_sauce | 112 |
        | visual_user   | secret_sauce | 113 |

    @negative @params
    Scenario Outline: Множественная негативная авторизация
        Given пользователь на главной странице
        When заполняет логин "<log>"
        And заполняет пароль "<pass>"
        And нажимает кнопку "login-button"
        Then перехода на другую страницу не происходит
        And URL страницы не содержит "inventory.html"
        And заголовок содержит "Swag Labs"
        And сделали скриншот "<num>"

        Examples:
        | log         | pass          | num |
        | ''          | ''            | 211 |
        | 123         | secret_sauce  | 212 |
        | visual_user | 123           | 213 |
