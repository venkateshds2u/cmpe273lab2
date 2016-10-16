import logging
import requests
import json
logging.basicConfig(level=logging.DEBUG)
from collections import Counter
from spyne import Application, srpc, rpc, ServiceBase, \
	Integer, Unicode

from spyne import Iterable

from spyne.protocol.http import HttpRpc
from spyne.protocol.json import JsonDocument

from spyne.server.wsgi import WsgiApplication

class HelloWorldService(ServiceBase):
	@srpc(Unicode, Unicode, Unicode, _returns=Iterable(Unicode))
   
	def say_hello(lat, lon, radius):
		jsonArray = requests.get("https://api.spotcrime.com/crimes.json?lat=%s&lon=%s&radius=%s&key=."%(lat,lon,radius))
		#jsonArray = requests.get("https://api.spotcrime.com/crimes.json?lat=37.334164&lon=-121.884301&radius=0.02&key=.")
		#result=json.dumps
		#someArray = json_decode(jsonArray.json(), true)
		json_data=json.dumps(jsonArray.json())
		leng=len(jsonArray.json())
		item_dict = json.loads(json_data)
		total_crime= len(item_dict['crimes'])
		dictresult = { }
		dictresult["total_crime"]=total_crime
		
		Arrest=0
		Other=0
		Burglary=0
		Theft=0
		Robbery=0
		Assault=0
		for s in item_dict['crimes']:
			if s["type"] == 'Other':
				Other = Other+1
			elif s['type'] == 'Assault':
				Assault = Assault+1
			elif s['type'] == 'Arrest':
				Arrest = Arrest+1
			elif s['type'] == 'Burglary':
				Burglary = Burglary+1
			elif s['type'] == 'Theft':
				Theft = Theft+1
			elif s['type'] == 'Robbery':
				Robbery = Robbery+1
			else:
				count1=0

		#dictresult = {'total_crime': total_crime}
		crime_type_count={}

		dictresult["Assault"]=Assault
		dictresult["Arrest"]=Arrest
		dictresult["Other"]=Other
		dictresult["Burglary"]=Burglary
		dictresult["Theft"]=Theft
		dictresult["total_crime"]=total_crime
		dictresult["total_crime"]=Robbery

		

		#yield 'total_crime %s'%total_crime
		#yield 'Assault %s'%Assault
		#yield 'Arrest %s'%Arrest
		#yield 'Other %s'%Other
		#yield 'Burglary %s'%Burglary
		#yield 'Theft %s'%Theft
		#yield 'Robbery %s'%Robbery 


		count12=0
		count3=0
		count6=0
		count9=0
		count1212=0
		count33=0
		count66=0
		count99=0
		for dic in item_dict['crimes']:
			for s in dic:
				if s=='date':
					if ((dic[s][9:11]=='12' and dic[s][15:17]=='AM') or (dic[s][9:11]=='01' and dic[s][15:17]=='AM') or (dic[s][9:11]=='02' and dic[s][15:17]=='AM')):
						count12=count12+1
					elif ((dic[s][9:11]=='03' and dic[s][15:17]=='AM') or (dic[s][9:11]=='04' and dic[s][15:17]=='AM') or (dic[s][9:11]=='05' and dic[s][15:17]=='AM')):
						count3=count3+1
					elif ((dic[s][9:11]=='06' and dic[s][15:17]=='AM') or (dic[s][9:11]=='07' and dic[s][15:17]=='AM') or (dic[s][9:11]=='08' and dic[s][15:17]=='AM')):
						count6=count6+1
					elif ((dic[s][9:11]=='09' and dic[s][15:17]=='AM') or (dic[s][9:11]=='10' and dic[s][15:17]=='AM') or (dic[s][9:11]=='11' and dic[s][15:17]=='AM')):
						count9=count9+1
					elif ((dic[s][9:11]=='12' and dic[s][15:17]=='PM') or (dic[s][9:11]=='01' and dic[s][15:17]=='PM') or (dic[s][9:11]=='02' and dic[s][15:17]=='PM')):
						count1212=count1212+1
					elif ((dic[s][9:11]=='03' and dic[s][15:17]=='PM') or (dic[s][9:11]=='04' and dic[s][15:17]=='PM') or (dic[s][9:11]=='05' and dic[s][15:17]=='PM')):
						count33=count33+1
					elif ((dic[s][9:11]=='06' and dic[s][15:17]=='PM') or (dic[s][9:11]=='07' and dic[s][15:17]=='PM') or (dic[s][9:11]=='08' and dic[s][15:17]=='PM')):
						count66=count66+1
					elif ((dic[s][9:11]=='09' and dic[s][15:17]=='PM') or (dic[s][9:11]=='10' and dic[s][15:17]=='PM') or (dic[s][9:11]=='11' and dic[s][15:17]=='PM')):
						count99=count99+1
					else:
						count13=0

		event_time_count={}

		dictresult["12:01am-3am"]=count12
		dictresult["3:01am-6am"]=count3
		dictresult["6:01am-9am"]=count6
		dictresult["9:01am-12noon"]=count9
		dictresult["12:01pm-3pm"]=count1212
		dictresult["3:01pm-6pm"]=count33
		dictresult["6:01pm-9pm"]=count66
		dictresult["9:01pm-12midnight"]=count99

		#yield '12:01am-3am: %s'%count12 
		#yield '3:01am-6am: %s'%count3
		#yield '6:01am-9am: %s'%count6
		#yield '9:01am-12noon: %s'%count9
		#yield '12:01pm-3pm: %s'%count1212
		#yield '3:01pm-6pm: %s'%count33
		#yield '6:01pm-9pm: %s'%count66
		#yield '9:01pm-12midnight: %s'%count99

		stringlist = []


		for s in item_dict['crimes']:
			result=s['address']
			if "BLOCK OF" in result:
				a, b = s['address'].split('BLOCK OF ')
				stringlist.append(b)
				

			elif "BLOCK BLOCK" in result:
				c, d = s['address'].split('BLOCK BLOCK')
				stringlist.append(d)
				

			elif "& " in result:
				e, f = s['address'].split('&')
				stringlist.append(f)
				stringlist.append(e)
				
			
			elif "BLOCK" in result:
				g, h = s['address'].split('BLOCK')
				stringlist.append(h)
				

			else:
				waste = s['address']
				stringlist.append(waste)
				

		
		c = Counter(stringlist)
		#dictresult[crime_type_count]=crime_type_count
		#dictresult[event_time_count]=event_time_count
		#yield 'most common: %s'%c.most_common(3)
		dictresult["the_most_dangerous_streets"]=c.most_common(3)
		yield ' %s'%dictresult
		


	
		  
application = Application([HelloWorldService],
	tns='spyne.examples.hello',
	in_protocol=HttpRpc(validator='soft'),
	out_protocol=JsonDocument()
)

if __name__ == '__main__':
	
	from wsgiref.simple_server import make_server

	wsgi_app = WsgiApplication(application)
	server = make_server('0.0.0.0', 8000, wsgi_app)
	server.serve_forever()




