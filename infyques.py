class bill:
    counter = 1000
    def __init__(self):
        self.__bill_id = 1000
        self.__bill_amount = 0

    def generate_bill_amount(self,item_quantity,items):
        bill.counter += 1
        self.__bill_amount = 0
        self.__bill_id = 'B'+str(bill.counter)
        temp_dict = item_quantity
        a = {}

        for item in temp_dict:
            a[item.lower()] = temp_dict[item]

        for prod,quan in a.items():
            for item in items:
                if item.get_item_id().lower()==prod:
                    self.__bill_amount+=quan*item.get_price_per_quantity()
                    break


    def get_bill_id(self):
        return self.__bill_id

    def ge_bill_amount(self):
        return self.__bill_amount

class customer