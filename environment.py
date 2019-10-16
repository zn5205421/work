from selenium import webdriver

def before_all(context):
    context.driver = webdriver.Chrome('driver/chromedriver.exe')
    pass
def before_feature(context,feature):
    print 'before features'
    pass
def before_scenario(context,feature):
    pass
def before_step(context,step):
    pass
def after_step(context,step):
    pass
def after_scenario(context,step):
    pass