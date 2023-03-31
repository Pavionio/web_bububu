from requests import get, post, delete
from datetime import datetime

print(get('http://127.0.0.1:5000/api/v2/users').json())  # все пользователи
print(get('http://127.0.0.1:5000/api/v2/users/2').json())  # пользователь 1
try:
    print(get('http://127.0.0.1:5000/api/v2/users/bububub').json())  # ошибка
except Exception:
    print('ошибка')
print(get('http://127.0.0.1:5000/api/v2/users/7777777').json())  # нет пользователя

print(post('http://127.0.0.1:5000/api/v2/users', json=dict(surname='bububub1', name='artem1', age=0,
                                                            position='уборщик', speciality='посудомойка',
                                                            address='балтийск', email='artembububфы@bubub.ru',
                                                            hashed_password='bububub')).json())  # успех
print(post('http://127.0.0.1:5000/api/v2/users', json=dict(surname='bububub', name='artem', age=0,
                                                            speciality='посудомойка',
                                                            address='балтийск', email='artembubub@bubub.ru',
                                                            hashed_password='bububub')).json())  # ошибка
print(delete('http://127.0.0.1:5000/api/v2/users/7777777').json())  # ошибка
print(delete('http://127.0.0.1:5000/api/v2/users/3').json())  # успех
