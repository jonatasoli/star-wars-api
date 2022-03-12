yavin_dict = dict(
    name='Yavin IV',
    climate='temperate, tropical',
    diameter='10200',
    population='1000',
    films=[dict(title='A New Hope', release_date='1977-05-25')],
)
alderaan_dict = dict(
    name='Alderaan',
    climate='temperate',
    diameter='12500',
    population='2000000000',
    films=[
        dict(title='A New Hope', release_date='1977-05-25'),
        dict(title='Revenge of the Sith', release_date='2005-05-19'),
    ],
)
hoth_dict = dict(
    name='Hoth',
    climate='frozen',
    diameter='7200',
    population='unknown',
    films=[
        dict(title='The Empire Strikes Back', release_date='1980-05-17'),
    ],
)

list_planets = dict(result=[yavin_dict, alderaan_dict])
list_yavin = dict(result=[yavin_dict])
list_alderaan = dict(result=[alderaan_dict])
list_hoth = dict(result=[hoth_dict])
