from pymongo import MongoClient
import pymongo
class MongoDBManagement:
	def __init__(self):
		self.client = MongoClient("tiennguyen.koreasouth.cloudapp.azure.com:27017")
		#self.client = MongoClient()
		#self.db = self.client['databaseiot']
		self.db = self.client['device']
		self.coll_device = self.db['device']
		self.coll_data = self.db['data']
	# def insert_one_data(self):
	# 	self.coll_data.insert_one({
	# 		"_id": "1244",
	# 		"mac": "12:22:33:87",
	# 		"humid": "33",
	# 		"time_date": "14:37,12/4/2019",

	# 		})

	def update_a_device(self):
		self.coll.find_one_and_update(
			{

			})

	def find_all_device(self):
		all_data = self.coll_data.find().sort("_id", 1)
		for i in all_data:
			k = i

			#a = self.coll_data.find({"mac": "12:22:33:5E"})
		return k
		
	def find_neast_data(self):
		find_sun = self.coll_data.find().sort("_id", 1)
		for i in find_sun:
			k = i
		#print("Số lượng data: " + str(self.coll_data.find({}).sort("_id": 1)))
		# find_sun_moning = self.coll_data.find({})
		return k
	def find_morning_data(self):
		find_ = self.coll_data.find({'param.hum':22,'date.hour':{'$gt': 6, '$lt':12}})
		for i in find_:
			k = i

		return k
if __name__ == "__main__":
	mongoDB = MongoDBManagement()
	#mongoDB.insert_one_data()
	print(mongoDB.find_morning_data()['param']['hum'])
	print(mongoDB.find_neast_data()['param'])
	# print(mongoDB.find_morning_data())

