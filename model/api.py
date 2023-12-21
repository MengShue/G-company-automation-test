from model.baseApi import BaseApi


class Api(BaseApi):
    # in good api design, should be api/v1, api/v2
    # Should naming class v1 or class v2

    def __init__(self):
        super().__init__(path='api/')

    def get_starship(self):
        res = self.httpClient.http_request(api_path='starships', method='GET')
        return res

    def get_people(self, page=None):
        para = {"page": page} if page is not None else page
        res = self.httpClient.http_request(api_path='people', method='GET', parameter=para)
        return res

    def get_people_by_id(self, people_id=None):
        res = self.httpClient.http_request(api_path=f'people/{people_id}', method='GET', parameter=None)
        return res

    def get_films(self, page=None):
        para = {"page": page} if page is not None else page
        res = self.httpClient.http_request(api_path='films', method='GET', parameter=para)
        return res

    def get_vehicles(self, path_para=None):
        res = self.httpClient.http_request(api_path=f'vehicles/{path_para}', method='GET', parameter=None)
        return res



if __name__ == "__main__":  # For quick debug
    print("api.py is running directly")
    api = Api()
    r = api.get_starship()
    print(r.status_code)
    print(r.json())
