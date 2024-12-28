from .Divarication import Divarication
from .Model import Model
import random

class Controller():
    def __init__(self,stores,s_class,s_uri):
        self.stores = stores #Config/Config.py const STORES
        self.s_class = s_class #Config/Config.py const STORES_CLASS
        self.s_uri = s_uri #Config/Config.py const STORES_URI
        self.main_func()
        self.main_data = None

    def return_store(self,var):
        try:
            return self.stores[int(var)-1]
        except IndexError:
            return 

    def main_func(self):
        print("Выберите магазины:")
        for i in range(1,len(self.stores)+1):
            print(i,self.stores[i-1])
        list_used_store = list(map(self.return_store,input("").split()))
        article_product = str(input("Какой товар искать?"))
        store = self.receiving_requests(list_used_store,article_product)
        self.main_data = Divarication(store,self.s_class).main_data
        print(self.main_data)
        self.save_data(article_product)
        
    def save_data(self,article):
        model = Model()
        con = model.create_connection()
        for key,valuess in self.main_data.items():
            name = key + article +str(random.randint(1,2**5))
            model.execute_query(con,model.create_products_table_template(name))
            for values in valuess:
                m = model.create_products_insert_template(name,model.create_products_values_template(values))
                model.execute_query(con,m)


    def receiving_requests(self,list_used,article):
        pages = range(1,3)
        store = {}
        for used_store in list_used:
            store[used_store] = []
            try:
                uri = self.s_uri[used_store]
            except KeyError:
                pass
            for page in pages:
                store[used_store].append(uri.format(text = article,page=page))
        return store