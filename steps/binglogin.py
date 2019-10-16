# coding=utf-8
from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import PageObject.binghomepageobject as HomePage
import PageObject.bingloginpageobject as LoginPage

@when(u'我在bing首页进入登录界面')
def step_impl(context):
    HomePage.Open(context)
    WebDriverWait(context.driver, 10).until(expected_conditions.element_to_be_clickable((By.ID, 'id_s')))
    HomePage.Signin_Link(context).click()

@given (u'我登录账号"{keyword1}"密码"{keyword2}"')
def step_impl(context, keyword1, keyword2):
   # WebDriverWait(context.driver, 15).until(expected_conditions.element_to_be_clickable((By.ID, 'i0116')))
    LoginPage.Username_TextBox(context).clear()
    LoginPage.Username_TextBox(context).send_keys(keyword1)
    LoginPage.Next_Button(context).click()
    WebDriverWait(context.driver, 10).until(expected_conditions.element_to_be_clickable((By.ID, 'i0118')))
    LoginPage.Password_TextBox(context).clear()
    LoginPage.Password_TextBox(context).send_keys(keyword2)
    LoginPage.Signin_Button(context).click()

@then (u'我应该看见包含"{success_name}"的登录成功用户信息')
def step_impl(context,success_name):
    WebDriverWait(context.driver, 10).until(expected_conditions.new_window_is_opened)
    assert HomePage.Login_Name(context).__contains__(success_name)
