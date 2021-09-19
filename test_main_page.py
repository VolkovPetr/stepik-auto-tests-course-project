from pages.main_page import MainPage
from pages.login_page import LoginPage
	
    
def test_guest_should_see_login_link(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209?promo=midsummer"
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()
    
    
def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209?promo=midsummer"
    page1 = MainPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page1.open()                      # открываем страницу
    page1.go_to_login_page()          # выполняем метод страницы — переходим на страницу логина
    page2 = LoginPage(browser, browser.current_url)
    page2.should_be_login_url()
    page2.should_be_login_form()
    page2.should_be_register_form()


