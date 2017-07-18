def calculate_bill(price):
    service_charge = float(price * 0.1)
    service_tax = float(price * 0.06)
    vat = float(price * 0.15)
    cal_bill = float(price + service_charge + service_tax + vat)
    print "bill=" + str(cal_bill)

restaurant_details={
    'dominoz':{
        'owner name':'juhi',

        'ratings':'*****',

        'restaurant address':'huda city center,gurgaon',

        'menu':{

            'small pizza':'100',

            'medium pizza':'200',

            'large pizza':'300',

            'loaded pizza':'400'
        }
    },

    'pizza hut':{
        'owner name':'kavita',

        'ratings':'****',

        'restaurant address':'shahpur jat,delhi',

        'menu':{

            'loaded pizza':'200',

            'cheese pizza':'100',

            'veg pizza':'300',

            'chocolate pizza ':'400'
        }
    },
}

user_identification=raw_input("who are you? owner or customer")
if user_identification=='owner':
    restaurant_details.keys()
    restaurant_name=raw_input("you are which restraunt owner? Dominoz or pizza hut ")

    owner_choice=int(raw_input("what you want to do?\n 1.add an item in the food list\n 2.delete an item from the food list\n 3.update the price of existing item"))

    if owner_choice==1:

        new_item_name=raw_input("name of item you want to add")
        item_price=raw_input("price of the new item")
        restaurant_details[restaurant_name]['menu'][new_item_name]=item_price
        print restaurant_details
    elif owner_choice==2:
        del_item_name=raw_input("which item you want to delete?")
        del restaurant_details[restaurant_name][del_item_name]
        print restaurant_details
    elif owner_choice==3:
        update_item_name=raw_input("the item which price you want to update")
        new_price=raw_input("enter new price")
        restaurant_details[restaurant_name]['menu'][update_item_name]['price']=new_price
        print restaurant_details
    else:
        print "wrong choice"


elif user_identification=='customer':
    customer_choice1=raw_input("what you want to do? 1.order food or 2.ratings")
    if customer_choice1=='order food':
        pickup_way = raw_input("home delivery or walk in")
        if pickup_way == 'home delivery':
            print "choosen method is delivery"
            print restaurant_details
            restaurant_name2 = raw_input("from which restaurant you want to order? dominoz or pizza hut")
            print restaurant_details[restaurant_name2]['menu']
            pizza_choice = raw_input("which pizza you want to order")
            customer_name = raw_input("what is your name?")
            customer_address = raw_input("what is your address?")
            print "we will deliver %s's order at %s within one hour."%(customer_name,customer_address)
            calculate_bill(float(restaurant_details[restaurant_name2]['menu'][pizza_choice]))
        elif pickup_way == 'walk in':
            print "choosen method is walk in"
            print restaurant_details
            restaurant_name2 = raw_input("from which restraunt you want to order? dominoz or pizza hut")
            print restaurant_details[restaurant_name2]['menu']
            pizza_choice = raw_input("which pizza you want to order")
            print "order is placed at " + restaurant_details[restaurant_name2]['restaurant address']
            calculate_bill(float(restaurant_details[restaurant_name2]['menu'][pizza_choice]))

        if pizza_choice in restaurant_details[restaurant_name2]['menu'].keys():
            print "order successful"

        else:
            print "sorry the pizza you ordered is unavailable"

    elif customer_choice1=='ratings':
        restraunt_choice=raw_input("choose name of restaurant you want to give ratings.\n dominoz or pizza hut")
        new_ratings=raw_input("give ratings")
        restaurant_details[restraunt_choice]['ratings']=new_ratings
        print restaurant_details