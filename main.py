
from base_tokenizer import BaseTokenizer
from utils import load_n_grams
from dict_models import LongMatchingTokenizer
import os
import json
from APIwithMongo import MongoDBManagement
from read_input import readInputData


s = readInputData.read_input()

print(s)

lm_token = LongMatchingTokenizer()
token = lm_token.tokenize(s)
print(token)
param = open("param.txt","r")
param = param.read()
for i in range(len(token)):
	if token[i] in param:
		par = token[i]
	else: 
		t = - 0.1
if(par == None):
	par = t
	
ApiMongo = MongoDBManagement()
mongo_neast_find = ApiMongo.find_neast_data()
# mongo_neast_find = ApiMongo.find_neast_data()
mongo_morning_find = ApiMongo.find_morning_data()
# print(mongo_morning_find)

with open('time.json','r') as time_data:
	times = json.load(time_data)
for time in times['times']:
	for i in range(len(token)):
		if token[i] in time['time_neast']:	
			k = token[i]

write = open("output.txt","w",encoding = 'utf-8')

if (par == 'độ ẩm'or par == 'do am'):
	out_put = mongo_neast_find['param']['hum']
	print(mongo_neast_find['param']['hum'])
	write_ = write.write("Độ ẩm bây giờ là:{}".format(out_put))
elif (par == 'nhiệt độ' or par == 'nhiet do'):
	out_put = mongo_neast_find['param']['temp']
	print(out_put)
	write_ = write.write("Nhiệt độ bây giờ là:{}".format(out_put))
		 		# print(mongo_neast_find['date']['hour': {'$lt': 6}])
		 		
else:
	write_ = write.write("Sai cứ pháp, vui lòng nhập lại")
