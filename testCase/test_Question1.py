from testCase.test_Base import TestBase
from model.api import Api
from utils.verify import *
import logging


class TestQuestion(TestBase):

    def test_for_question_1(self):
        api = Api()
        res = api.get_starship()
        verify_status_code(res, 200)
        count = res.json()['count']
        logging.info(f"星際大戰內出現過的飛船 ( starship )總共有 {count} 艘\n")

    def test_for_question_2(self):
        api = Api()
        res = api.get_people()
        verify_status_code(res, 200)
        people = []
        page = 1
        while True:
            count = len(res.json()['results'])
            for i in range(count):
                if res.json()['results'][i]['hair_color'] == 'none':
                    people.append(res.json()['results'][i]['name'])
            page = page + 1
            if res.json()['next'] is None:
                break
            else:
                res = api.get_people(page=page)

        logging.info(f"星際大戰內頭髮顏色 ( hair_color )為 none 的人有哪些\n")
        logging.info(f"{people}\n")

    def test_for_question_3(self):
        api = Api()
        res = api.get_films()
        verify_status_code(res, 200)
        count = len(res.json()['results'])
        vehicles = []
        index = 0
        for i in range(count):
            if res.json()['results'][i]['episode_id'] == 6:
                index = i
                break
        for item in res.json()['results'][index]['vehicles']:
            item = str(item).split('/')[-2]
            res_v = api.get_vehicles(path_para=item)
            verify_status_code(res_v, 200)
            if int(res_v.json()['passengers']) > 10:
                vehicles.append(res_v.json()['name'])

        logging.info(f"列出在第六部電影 ( episode_id = 6 ) 中出現的載具可乘載乘客 ( passengers ) 數量大於10的有那\n")
        logging.info(f"{vehicles}\n")

    def test_for_question_4(self):
        logging.info(f"這一case是以任意單元測試框架來設計一個API測試案例\n")
        api = Api()
        res = api.get_people_by_id(people_id=1)
        verify_status_code(res, 200)
        verify_key_exist(res.json(), "name")
        verify_key_exist(res.json(), "height")
        verify_key_exist(res.json(), "mass")
        verify_key_exist(res.json(), "hair_color")
        verify_key_exist(res.json(), "skin_color")
        verify_key_exist(res.json(), "eye_color")
        verify_key_exist(res.json(), "birth_year")
        verify_key_exist(res.json(), "gender")
        verify_key_exist(res.json(), "homeworld")
        verify_key_exist(res.json(), "films")
        verify_key_exist(res.json(), "species")
        verify_key_exist(res.json(), "vehicles")
        verify_key_exist(res.json(), "starships")
        verify_key_exist(res.json(), "created")
        verify_key_exist(res.json(), "edited")
        verify_key_exist(res.json(), "url")
        verify_list_length(res.json()['films'], 4)
        verify_list_length(res.json()['species'], 0)
        verify_content_value(res.json()['name'], 'Luke Skywalker')
        verify_content_value_regex(res.json()['created'],
                                   '[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}.[0-9]{6}Z')
        verify_content_value_regex(res.json()['edited'],
                                   '[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}.[0-9]{6}Z')
        logging.info(f"以上即為API測試案例\n")

