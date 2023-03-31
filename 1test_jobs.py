from requests import get, post, delete

print(get('http://127.0.0.1:5000/api/v2/jobs').json())  # все пользователи
print(get('http://127.0.0.1:5000/api/v2/jobs/3').json())  # пользователь 2
try:
    print(get('http://127.0.0.1:5000/api/v2/jobs/bububub').json())  # ошибка
except Exception:
    print('ошибка')
print(get('http://127.0.0.1:5000/api/v2/jobs/7777777').json())  # нет пользователя

print(post('http://127.0.0.1:5000/api/v2/jobs',
           json=dict(job='негр', work_size=9999, collaborators='black_people', start_date='1999-03-31',
                     end_date='2023-03-31',
                     is_finished=False, category=1)).json())  # успех
print(post('http://127.0.0.1:5000/api/v2/jobs',
           json=dict(job='негр', work_size=9999, start_date='1999-03-31', end_date=None,
                     is_finished=False, category=1)).json())  # ошибка
print(delete('http://127.0.0.1:5000/api/v2/jobs/7777777').json())  # ошибка
print(delete('http://127.0.0.1:5000/api/v2/jobs/2').json())  # успех
