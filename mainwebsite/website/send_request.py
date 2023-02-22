import requests
from bs4 import BeautifulSoup
import threading


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


class Main:
    def send_design_count_request(keyword):
        url = "https://www.redbubble.com/shop/?query={}&ref=search_box".format(
            keyword)
        # Make a request to the web page
        response = requests.get(url)
        # Parse the HTML of the web page
        soup = BeautifulSoup(response.text, 'html.parser')
        target_span = soup.find("span", {
                                "class": "styles__box--2Ufmy styles__text--23E5U styles__body--3StRc styles__muted--8wjeu"})
        design_count = target_span.text
        return design_count
    

    def send_request_google(keyword):
      payload = {"locationIds": [2840], "keyword": keyword}

      response = requests.post(
          url="https://tools.wordstream.com/api/free-tools/google/keywords", json=payload)

      value =dict(response.json())
      search_Volume=value['keywords'][0]['searchVolume']
      competetion=value['keywords'][0]['competition']
      return search_Volume,competetion


class RunAsThread:

    def search_nd_add_to_dictionary(self, keywords_list,target):
        result_dict = {}
        threads = []
        for i, keyword in enumerate(keywords_list):
            thread = threading.Thread(target=target, args=(i, keyword, result_dict))
            threads.append(thread)
            thread.start()
        
        for thread in threads:
            thread.join()
        
        return result_dict

    def fetch_design_count1(self, index, keyword, result_dict):
        design_count = Main.send_design_count_request(keyword)
        search_Volume,competetion=Main.send_request_google(keyword)
        result_dict[index+1] = { 'keyword':keyword,'design_count':design_count,'search_Volume':search_Volume,'competetion':competetion}

        
    def __init__(self):
        self.result_dict = {}
        

    def search_and_add_to_dictionary(self, keyword_list):
        threads = []
        for keyword in keyword_list:
            t = threading.Thread(target=self.add_to_dict, args=(keyword,))
            threads.append(t)
            t.start()
        
        for t in threads:
            t.join()
        
        return self.result_dict
    
    def add_to_dict(self, keyword):
        design_count = main.send_design_count_request(keyword)
        self.result_dict[keyword] = design_count
        




