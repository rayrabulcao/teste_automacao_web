from selenium import webdriver

def before_all(context):
    context.web = webdriver.Chrome()
    context.web.maximize_window()

def after_step(context, step):
    print()

def after_all(context):
    context.web.quit()