from pymongo import MongoClient
from bson.objectid import ObjectId
from pprint import pprint


print('Hello, welcome to the AAC (Austin Animal Center)')
#creation of global variables in python
userCreateData = {}   # input data for write function
userSearchdata = {}  # data data for search function
userUpdateFromdata = {}  # update data for update function
userUpdateTodata = {}  # update data for update function
userDeletedata = {}  # delete data for delete function
#class
class AnimalShelter(object):
    """CRUD Operations for Animal collection in MongoDB"""
    def __init__(self, user, password):
            # Initializing the MongoClient. This helps to
            # access the MongoDB databases and collections.
            self.client = MongoClient('mongodb://%s:%s@localhost:46789' % (user, password))
            self.database = self.client['AAC']

    #obtain create data from user
    def obtainCreateData(self):
        #table to ensure data dict conforms to the expected format
        values = ['1', 'age_upon_outcome', 'animal_id', 'animal_type', 'breed', 'color', 'date_of_birth', 'datetime', 
          'monthyear', 'name', 'outcome_subtype', 'outcome_type', 'sex_upon_outcome', 'location_lat', 
          'location_long', 'age_upon_outcome_in_weeks']
        #loop to obtain input values from the user
        for i in range (len(values)):
            key = values[i]
            value = input("Enter " + values[i] + ": ")
            userCreateData.update({key: value})          #creates dict item with user input data
        
    #C operation      
    def create(self, data):
        
            if data is not None:
                #print(type(data))  <- was used to confirm the data was a dictionary
                result = self.database.animals.insert_one(data)     # data should be dictionary
                pprint(result)
            
            else:
                # lets the user know something went wrong
                raise Exception("Nothing to save, because the data parameter is empty")
     
            
    #R operation
    def obtainReadData(self):
        #loop to obtain a key/value pair
        for i in range(1):
            key = input("Enter search key: ")
            value = input("Enter search value: ")
            userSearchdata.update({key: value})    #creates dict object to hold search terms
        

    #R operation for R in CRUD
    def read(self, data):
        # try/except block for testing in the unit tests
        try:
            if data is not None:
                #print(type(data))       # data should be dictionary - confirmed
                read_result = list(self.database.animals.find(data, {"_id": False}))
                #pprint(read_result)   # displays the results in the console
                return read_result
            else:
                #lets the user know there was a problem
                raise Exception("Nothing to search, because the data parameter is empty")
                return False
        except Exception as e:
            print("An exception occurred: ", e)
    def readall(self, data):
        read_result = self.database.animals.find(data, {"_id": False})
        
        return read_result
    
    #obtain data data for U in CRUD
    def obtainUpdateData(self):
        #loop to obtain a key/value pair
        for i in range(1):
            key = input("Enter update key: ")
            value = input("Enter update value: ")
        userUpdateFromdata.update({key: value})
        #obtain new data to change the data to
        for i in range(1):
            key = input("Enter update key: ")
            value = input("Enter new update value: ")
        userUpdateTodata.update({'$set': {key: value}})
        print(userUpdateTodata)

    #U operation for U in CRUD
    def update(self, fromdata, todata, count):
        if fromdata is not None:
            if count == 1:
                update_result = self.database.animals.update_one(fromdata, todata)
                pprint("Matched Count: " + str(update_result.matched_count) + ", Modified Count: " + str(update_result.modified_count))
                if update_result.modified_count == 1:
                    print("Success!")
                    print(update_result)
                    return True
                else:
                    print("Something went wrong")
                    return False
            elif count == 2:
                update_result = self.database.animals.update_many(fromdata, todata)
                pprint("Matched Count: " + str(update_result.matched_count) + ", Modified Count: " + str(update_result.modified_count))
                if update_result.modified_count == update_result.matched_count:
                    print("Success!")
                    print(update_result)
                    return True
                else:
                    print("Something went wrong, all items matching the data may not have been updated. Run a search to verify")
                    print(update_result)
                    return True
            else:
                print("Count not recognized - try again.")
                return False
        else:
            #lets the user know there was a problem
            raise Exception("Nothing to update, because at least one of the data parameters is empty")
            return False
    #obtain data data for D in CRUD
    def obtainDeleteData(self):
        #loop to obtain key/value pair
        for i in range(1):
            key = input("Enter delete key: ")
            value = input("Enter delete value: ")
            userDeletedata.update({key: value})
    #delete function for either single or many
    def deleteData(self, data, count):
        if data is not None:
            if count == 1:
                try:
                    delete_result = self.database.animals.delete_one(data)
                    pprint("Deleted Count: " + str(delete_result.deleted_count))
                    if delete_result.deleted_count == 0:
                        print("Nothing to be deleted using the data data.")
                        print(delete_result)
                        return True
                    else:
                        print("Success!")
                        print(delete_result)
                        return True
                except Exception as e:
                    print("An exception has occurred: ", e)
            elif count == 2:
                try:
                    delete_result = self.database.animals.delete_many(data)
                    pprint("Deleted Count: " + str(delete_result.deleted_count))
                    if delete_result.deleted_count == 0:
                        print("Nothing to be deleted using the data data.")
                        print(delete_result)
                        return True
                    else:
                        print("Success!")
                        print(delete_result)
                        return True
                except Exception as e:
                    print("An exception has occurred: ", e)
                    return False
            else:
                print("Count not recognized - try again.")
                return False
        else:
            #lets the user know there was a problem
            raise Exception("Nothing to delete, because the data parameter is empty")
            return False
       