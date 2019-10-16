def Open(context):
    context.driver.get('http://www.bing.com')
    context.driver.maximize_window()


def Search_TextBox(context):
    return context.driver.find_element_by_id('sb_form_q')


def Submit_Button(context):
    return context.driver.find_element_by_id('sb_go_par')

def Signin_Link(context):
    return context.driver.find_element_by_id('id_s')

def Login_Name(context):
    return context.driver.find_element_by_id('id_n').get_attribute("title")