
from src.sel import *
import pytest
import allure
from pytest_bdd import *
from pytest_bdd import parsers
'''
Background Предварительные действия    Предыстория
Given Дано, предварительные действия   Допустим
When  Что мы делаем, действия          Когда
Then  Что мы проверяем, результат      Тогда
And   доп условие/ доп проверка        И
But   условие исключение               Но
'''
# BDD-тестирование Behavior-Driven Development
@allure.feature('Регистрация')
@allure.story('Успешный вход')
@scenario('feature/reg.feature', 'Успешный вход')
def test_registration_enter():
    pass

@given('пользователь на главной странице')
def reg10(start):
    pass

@when(parsers.parse('заполняет логин "{value}"'))
def reg11(start,value):
    toSend(start, By.ID, 'user-name',value)

@when(parsers.parse('заполняет пароль "{value}"'))
def reg12(start,value):
    toSend(start, By.ID, 'password', value)

@when(parsers.parse('нажимает кнопку "{value}"'))
def reg13(start,value):
    toClick(start, By.ID, value)

@then('переходит на другую страницу')
def reg21():
    pass

@then(parsers.parse('проверка адреса "{result}"'))
def reg22(start,result):
    with allure.step('проверка адреса'):
        assert result in start.current_url

@then(parsers.parse('проверка заголовка "{result}"'))
def reg23(start,result):
    with allure.step('проверка заголовка'):
        e0 = toFind(start, By.CLASS_NAME, "title")
        assert result in e0.text


@allure.feature('Регистрация')
@allure.story('Успешный вход под разными пользователями')
@scenario('feature/reg.feature', 'Успешный вход  под разными пользователями')
def test_registration_enter2():
    pass

@given('пользователь на главной странице')
def reg10(start):
    pass

@when(parsers.parse('заполняет логин "{value}"'))
def reg11(start,value):
    toSend(start, By.ID, 'user-name',value)

@when(parsers.parse('заполняет пароль "{value}"'))
def reg12(start,value):
    toSend(start, By.ID, 'password', value)

@when(parsers.parse('нажимает кнопку "{value}"'))
def reg13(start,value):
    toClick(start, By.ID, value)

@then('переходит на другую страницу')
def reg21():
    pass

@then(parsers.parse('проверка адреса "{result}"'))
def reg22(start,result):
    with allure.step('проверка адреса'):
        assert result in start.current_url

@then(parsers.parse('сделали скриншот "{result}"'))
def reg23(start,result):
    with allure.step('делаем скриншот'):
        assert getScreen(start,result)


@allure.feature('Регистрация')
@allure.story('Множественная негативная авторизация')
@scenario('feature/reg.feature','Множественная негативная авторизация')
def test_manyNegReg():
    pass

@given('пользователь на главной странице')
def neg_reg(start):
    pass

@when(parsers.parse('заполняет логин "{value}"'))
def neg_reg1(start,value):
    with allure.step('Ввели данные в поле логин'):
        toSend(start, By.ID, 'user-name', value)

@when(parsers.parse('заполняет пароль "{value}"'))
def neg_reg11(start,value):
    with allure.step('Ввели данные в поле пароль'):
        toSend(start,By.ID,'password',value)

@when(parsers.parse('нажимает кнопку "{value}"'))
def neg_reg21(start,value):
    with allure.step(f'Нажали кнопку Login'):
        toClick(start,By.ID,value)

@then('перехода на другую страницу не происходит')
def neg_reg31():
    pass

@then(parsers.parse('URL страницы не содержит "{result}"'))
def neg_ref41(start,result):
    with allure.step('проверка адреса страницы'):
        assert result not in start.current_url

@then(parsers.parse('заголовок содержит "{result}"'))
def neg_reg51(start,result):
    with allure.step('проверяем что Swag Labs присутствует в тексте'):
        e2 = toFind(start, By.CLASS_NAME, "login_logo")
        assert result in e2.text

@then(parsers.parse('сделали скриншот "{result}"'))
def reg61(start,result):
    with allure.step('делаем скриншот'):
        assert getScreen(start,result)




# @pytest.mark.parametrize ('log,pas,num',[
#     ('standard_user','secret_sauce',111),
#     ('error_user','secret_sauce',112),
#     ('visual_user','secret_sauce',113),
# ])
# @pytest.mark.regression
# def test_manyReg(start,log,pas,num):
#     toSend(start,By.ID,'user-name',log)
#     toSend(start,By.ID,'password',pas)
#     toClick(start,By.ID,'login-button')
#     # assert toFind(start,By.CLASS_NAME,'title')
#     assert getScreen(start,num)
#     assert "/inventory.html" in start.current_url




# def test_registration(start):
#     toSend(start,By.ID,'user-name','standard_user')
#     toSend(start,By.ID,'password','secret_sauce')
#     toClick(start,By.ID,'login-button')
#     e0=toFind(start,By.CLASS_NAME,"title")
#     assert "/inventory.html" in start.current_url
#     assert "Products" in e0.text
