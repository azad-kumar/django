import requests
from bs4 import BeautifulSoup
import threading


class request:

    def __init__(self, url):
        self.url = url

    def send_get_request(self):
        response = requests.get(self.url)
        if response.status_code == 200:
            return response
        else:
            return False

    def send_post_request(self, payload):
        response = requests.post(self.url, json=payload)
        if response.status_code == 200:
            return response
        else:
            return False

    def fetch_json(self, response):
        if response:
            return response.json()
        else:
            return False


class keyword:

    def __init__(self, keyword):
        self.keyword = keyword

    def send_request_to_redbubble(self):
        url = "https://www.redbubble.com/shop/?query={}&ref=search_box".format(
            self.keyword)
        request_obj = request(url)
        response = request_obj.send_get_request()
        if response:
            return response
        else:
            return False

    def fetch_design_count(self, response):
        if response:
            soup = BeautifulSoup(response.text, 'html.parser')
            design_count = (soup.find("span", {
                "class": "styles__box--2Ufmy styles__text--23E5U styles__body--3StRc styles__muted--8wjeu"})).text
            return design_count
        else:
            return False

    def fetch_keywords(self, response):
        if response:
            soup = BeautifulSoup(response.text, 'html.parser')
            links = [a['href']
                     for a in soup.find_all('a', href=True) if '-by-' in a['href']]
            substrings = [link.split('/')[-2] for link in links]
            # Print the substrings
            main_list = []
            for i in substrings:
                string = i
                parts = string.split("-by-")
                design = parts[0].replace("-", " ")
                main_list.append(design)
            return main_list
        else:
            return False

    def fetch_only_design_count(self):
        response = self.send_request_to_redbubble()
        if response:
            return self.fetch_design_count(response=response)
        else:
            return False

    def fetch_only_keywords(self):
        response = self.send_request_to_redbubble()
        if response:
            return self.fetch_keywords(response=response)
        else:
            return False

    def get_keywords_and_design_count(self):
        design_count = self.fetch_only_design_count()
        keywords = self.fetch_only_keywords()
        return design_count, keywords

    
    def get_keyword_trend_request(self):
        url = "https://www.redbubble.com/typeahead/?term={}&locale=en".format(
            self.keyword)
        # Make a request to the web page
        response = requests.get(url).json()
        keyword_trend = response['data']['popular_searches']
        my_dict = {i: d for i, d in enumerate(keyword_trend)}
        return my_dict


class google:
    def __init__(self, keyword):
        self.keyword = keyword

    def get_searchvolume_competetion(self):
        url = 'https://tools.wordstream.com/api/free-tools/google/keywords'
        payload = {"locationIds": [2840], "keyword": self.keyword}
        request_obj = request(url)
        response = request_obj.send_post_request(payload=payload)
        if response:
            value = dict(response.json())
            search_Volume = value['keywords'][0]['searchVolume']
            competetion = value['keywords'][0]['competition']
            return search_Volume, competetion
        else:
            return False


    def get_response_json(self):
        url = 'https://tools.wordstream.com/api/free-tools/google/keywords'
        payload = {"locationIds": [2840], "keyword": self.keyword}
        request_obj = request(url)
        response = request_obj.send_post_request(payload=payload)
        if response:
            if len(response.json())>0:
                return dict(response.json())
            else:
                return False
        else:
            return False


class get_trending:
    main_url = 'https://www.redbubble.com/typeahead/?locale=en'
    main_object = None

    def __init__(self):
        pass

    def get_main_object(self):
        try:
            response = (requests.get(self.main_url)).json()
            trending_searches = response['data']
            self.main_object = trending_searches
        except requests.exceptions.RequestException as e:
            print("Error occured while connecting to the server: ", e)
            return None

    def get_trending_keywords(self):
        if self.main_object != None:
            main_object2 = self.main_object['trending_searches']
            main_list = []

            for i in range(len(main_object2)):
                main_list.append(
                    (i+1, main_object2[i]['label']))
            main_list = dict(main_list)
            return main_list
        else:
            self.get_main_object()
            return self.get_trending_keywords()

    def get_popular_searches(self):
        if self.main_object != None:
            second_object = self.main_object['popular_searches']
            my_dict = {i: d for i, d in enumerate(second_object)}
            return my_dict
        else:
            self.get_main_object()
            return self.get_popular_searches()

    def get_popular_artist(self):
        if self.main_object != None:
            second_object = self.main_object['artists']
            my_dict = {i: d for i, d in enumerate(second_object)}
            return my_dict
        else:
            self.get_main_object()
            return self.get_popular_artist()

    def get_fan_art_properties(self):
        if self.main_object != None:
            second_object = self.main_object['fan_art_properties']
            my_dict = {i: d for i, d in enumerate(second_object)}
            return my_dict
        else:
            self.get_main_object()
            return self.get_fan_art_properties()


class random:
    def __init__(self, keyword):
        self.keyword = keyword

    def send_keyword_trend_request(self):
        url = "https://www.redbubble.com/typeahead/?term={}&locale=en".format(
            self.keyword)
        request_obj = request(url)
        response = request_obj.send_get_request()
        json_variable = request_obj.fetch_json(response=response)

        if json_variable:
            keyword_trend = json_variable['data']['popular_searches']
            my_dict = {i: d for i, d in enumerate(keyword_trend)}
            return my_dict
        else:
            return False


class keyword_properties:
    main_dict = {}

    def add_to_dict(self, keyword, design_count, search_Volume, competetion, index):
        self.main_dict[index] = {'keyword': keyword, 'design_count': design_count,
                            'search_Volume': search_Volume, 'competetion': competetion}
        return True

    def fetch_keyword_properties(self, main_keyword):
        keyword_obj = keyword(main_keyword)
        keyword_count = keyword_obj.fetch_only_design_count()
        google_obj = google(main_keyword)
        try:
            search_volume, competetion = google_obj.get_searchvolume_competetion()
        except:
            search_volume='Na'
            competetion='NA'
        return main_keyword, keyword_count, search_volume, competetion

    def fetch_and_add(self, main_keyword, index):
        keyword, design_count, search_volume, competetion = self.fetch_keyword_properties(
            main_keyword)
        self.add_to_dict(keyword, design_count,
                         search_volume, competetion, index)

    def thread_and_add(self, keyword_list):
        threads = []
        for index, key in enumerate(keyword_list):
            thread = threading.Thread(target=self.fetch_and_add, args=(key, index,))
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()

    def get_dict_with_properties(self, keyword_list):
        self.thread_and_add(keyword_list)
        return self.main_dict


