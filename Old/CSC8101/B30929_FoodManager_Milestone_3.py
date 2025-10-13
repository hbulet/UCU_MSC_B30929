import uuid
import datetime

class Person:
    """"""
    id = ""
    name = ""
    contact = ""
    address = ""

    def __init__(self, _name, _contact, _address) -> None:
        self.id = str(uuid.uuid1())
        self.name = _name
        self.contact = _contact
        self.address = _address

    def get_details(self):
        return "Name: " + self.name + ", Contact: " + self.contact + ", Address: " + self.address


class Donor(Person):
    """"""
    is_organisation = False

    def __init__(self, _name, _contact, _address, _is_organisation) -> None:
        super().__init__(_name, _contact, _address)
        self.is_organisation = _is_organisation

    def get_details(self):
        _details = super().get_details()
        _details += ", Organisation: " + self.is_organisation
    

class Refugee(Person):
    """"""
    family_size = 1
    origin_country = ""

    def __init__(self, _name, _contact, _address, _family_size, _origin_country) -> None:
        super().__init__(_name, _contact, _address)
        self.family_size = _family_size
        self.origin_country = _origin_country

    def get_details(self):
        _details = super().get_details()
        _details += ", Family size: " + self.family_size + ", Origin Country" + self.origin_country

class Unit:
    """"""
    id = ""
    name = ""
    def __init__(self, _name) -> None:
        self.id = str(uuid.uuid1())
        self.name = _name
    
    def get_details(self):
        return "NAME: " + self.name + ", ID:" + self.id

class Food:
    """"""
    id = ""
    name = ""
    quantity_per_family_member = 0
    def __init__(self, _name, _unit, _quantity_per_family_member) -> None:
        self.id = str(uuid.uuid1())
        self.name = _name
        self.unit = _unit
        self.quantity_per_family_member = _quantity_per_family_member
        if not isinstance(_unit, Unit):
            raise TypeError("variable '_unit' must be of type 'Unit")
    
    def get_details(self):
        #return "Name: " + self.name + ", Contact: " + self.unit + ", Address: " + self.address
        pass

    def get_unit_cap(self):
        return self.quantity_per_family_member
    
    def set_unit_cap(self, _unit_cap):
        if not isinstance(_unit_cap, int):
            raise TypeError("variable '_unit_cap' must be of type 'int")
        self.quantity_per_family_member = _unit_cap
        
class Supply:
    id = ""
    quantity = 0
    quantity_available = 0
    expiration_date = datetime.datetime.now
    def __init__(self, _food_item, _quantity, _expiration_date) -> None:
        if not isinstance(_food_item, Food):
            raise TypeError("variable '_food_item' must be of type 'Food'")
        if not isinstance(_quantity, int):
            raise TypeError("variable '_quantity' must be of type 'int'")
        if not isinstance(_food_item, Food):
            raise ValueError("variable '_quantity' must be greater than zero")
        if not isinstance(_expiration_date, datetime.datetime):
            raise TypeError("variable '_quantity' must be of type 'datetime.datetime'")
        
        self.id = str(uuid.uuid1())
        self.food_item = _food_item
        self.quantity = _quantity
        self.expiration_date = _expiration_date
    
    def add_expire_date(self, _new_expire_date):
        self.expiration_date = _new_expire_date

    def is_expired(self):
        return (self.expiration_date > datetime.datetime.now)   
    
    def update_quantity(self, _quantity_used):
        if self.quantity_available > 0 :
            if (self.quantity_available - _quantity_used) >= 0 :
                self.quantity_available -= _quantity_used
        return self.quantity_available

    def get_quantity_available(self):
        return self.quantity_available

class Donation:
    id = ""
    delivered_date = datetime.datetime.now
    supply_list = []
    def __init__(self, _donor, _supply_list) -> None:
        if not isinstance(_donor, Donor):
            raise TypeError("variable '_donor' must be of type 'Donor'")
        
        self.id = str(uuid.uuid1())
        self.donor = _donor
        self.supply_list = _supply_list

    def add_donor(self, _donor):
        if not isinstance(_donor, Donor):
            raise TypeError("variable '_donor' must be of type 'Donor'")
        self.donor = _donor

    def add_supply(self, _supply):
        if not isinstance(_supply, Supply):
            raise TypeError("variable '_supply' must be of type 'Supply'")
        self.supply_list.append(_supply)

    def get_supplies(self):
        return self.supply_list

        
class Distribution:
    """"""
    id = ""
    release_date = datetime.datetime.now
    food_list = []
    refugee_list = []
    def __init__(self, _release_date, _food_list, _refugee_list) -> None:
        if not isinstance(_release_date, datetime.datetime):
            raise TypeError("variable '_release_date' must be of type 'datetime.datetime'")
        self.id = str(uuid.uuid1())
        self.release_date = _release_date
        self.food_list = _food_list
        self.refugee_list = _refugee_list

    def add_refugee(self, _refugee):
         if not isinstance(_refugee, Refugee):
            raise TypeError("variable '_refugee' must be of type 'Refugee'")   
         self.refugee_list.append(_refugee)
    
    def add_food(self, _food):
        if not isinstance(_food, Food):
            raise TypeError("variable '_food' must be of type 'Food'")   
        self.food_list.append(_food)

    def get_details(self):
        pass


class StockCount:
    id = ""
    quantity = 0
    def __init__(self, _food_item) -> None:
        if not isinstance(_food_item, Food):
            raise TypeError("variable '_food_item' must be of type 'Food'")
        
        self.id = str(uuid.uuid1())
        self.food_item = _food_item
    
    def get_count(self, _food):
        if not isinstance(_food, Food):
            raise TypeError("variable '_food' must be of type 'Food'")

    def set_count(self, _food):
        if not isinstance(_food, Food):
            raise TypeError("variable '_food' must be of type 'Food'")

    def get_details(self):
        pass

      
class Inventory:
    """"""
    id = ""
    name = ""
    stock_count_list = []
    store_list = []
    donation_list = []
    distribution_list = []
    release_date = datetime.datetime.now
    def __init__(self, _name) -> None:
        self.id = str(uuid.uuid1())
        self.name = _name

    def get_stock_count(self, _food):
        if not isinstance(_food, Food):
            raise TypeError("variable '_food' must be of type 'Food'")
        self.stock_count_list

    def get_stock_count_details(self):
        return ""    
    
    def add_donation(self, _donation):
        if not isinstance(_donation, Donation):
            raise TypeError("variable '_donation' must be of type 'Donation'")
    
        if len(_donation.get_supplies()) == 0:
            return False
        
        return True
    
    def release_distibution(self, _distribution):
        if not isinstance(_distribution, Distribution):
            raise TypeError("variable '_distribution' must be of type 'Distribution'")
        return True
    
    def get_history(self, _person):
        if not isinstance(_person, Person):
            raise TypeError("variable '_person' must be of type 'Person'")
        return True
    
    def get_details(self, _person):
        if not isinstance(_person, Person):
            raise TypeError("variable '_person' must be of type 'Person'")
        return True
    

#------ Implementation --------------------------------------
# Units to use
unit_Kilos = Unit("Kilograms")
unit_Liters = Unit("Litres")
unit_Bunches = Unit("Bunches")

# Foods to use
food_Matooke = Food("Matooke", unit_Bunches, 1)
food_Ugali = Food("Ugali", unit_Kilos, 2)
food_Sugar = Food("Sugar", unit_Kilos, 1)
food_Beans = Food("Beans", unit_Kilos, 2)
food_CookingOil = Food("Cooking Oil", unit_Liters, 1)
food_Salt = Food("Kitchen Salt", unit_Kilos, 1)

# Donors
donor_UG_Gvt = Donor("Uganda Government", "0700 153, 556", "Kampala", True)
donor_UCU = Donor("Uganda Christian University", "0700 153, 556", "Mukono", True)
donor_Jude = Donor("Jude", "0700 155, 556", "Jinja", False)
donor_Zadiya = Donor("Zadiya", "0700 133, 556", "Hoima", False)

# Inventory
inventory_kasese_store = Inventory("Kasese Community Relifee Store")
inventory_karamoja_store = Inventory("Karamoja Community Relifee Store")

# UG Govt donation
ug_Govt_donation = Donation(donor_UG_Gvt, [])

isAdded = inventory_kasese_store.add_donation(ug_Govt_donation)
if isAdded:
    print("Donation added")
else:
    print("Donation not added")

