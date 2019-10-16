def Username_TextBox(context):
    context.driver.implicitly_wait(15)
    return context.driver.find_element_by_id('i0116')

def Next_Button(context):
    return context.driver.find_element_by_id('idSIButton9')

def Password_TextBox(context):
    return context.driver.find_element_by_id('i0118')

def Signin_Button(context):
   context.driver.implicitly_wait(15)
   return context.driver.find_element_by_id('idSIButton9')


