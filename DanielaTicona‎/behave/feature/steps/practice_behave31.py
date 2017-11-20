
@given(u'User first name is {name:w}')
def step_impl(context,name):
    name= 'Daniela'

@given(u'user last name is {lastname:w}')
def step_impl(context,lastname):
    lastname = 'Ticona'

@given(u'username is {username:w}')
def step_impl(context,username):
    username= 'dticona'

@given(u'password is {pw:d}')
def step_impl(context,pw):
    pw= '4444'

@given(u'confirm password contains {passw:d}')
def step_impl(context,passw):
    passw = '4444'

@given(u'birthday month is {month:w}')
def step_impl(context,month):
    month= 'March'

@given(u'birthday day is {day:d}')
def step_impl(context,day):
    day= '19'

@given(u'birthday year is {year:d}')
def step_impl(context,year):
    year= '1988'

@given(u'gender is {gen:w}')
def step_impl(context,gen):
    gen= 'Female'

@given(u'Mobile phone is {tel:d}')
def step_impl(context,tel):
    tel= '59179152648'

@given(u'the current mail is {mail:w}')
def step_impl(context,mail):
    mail= 'dticonahotmailoom'

