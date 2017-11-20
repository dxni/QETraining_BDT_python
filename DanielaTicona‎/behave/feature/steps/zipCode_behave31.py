@given(u'a Zip code #{zip:d}')
def step_impl(context,zip):
   zip = 15454

@given(u'the country of customer Ctr. {country:w}')
def step_impl(context,country):
   country= 'Argentina'

@given(u'the number of habitats Num {habit:n}')
def step_impl(context,habit):
   habit=1,000