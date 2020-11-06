# Import elasticsearch module
from elasticsearch import Elasticsearch,ImproperlyConfigured,TransportError
import json

class ElasticsearchConnector:

	def __init__(self,credobject=None):
		"""
			Description:
						Accepts elasticsearch connection parameters and connects to elasticsearch cloud 
		"""

		#Parameter check
		try:
			assert credobject is not None,"Found credentials object empty"
		except AssertionError:
			print("Empty Credentials")

		try:
			with open(credobject, "r") as f:
				credentials = json.load(f)
		except OSError:
			print("Unable to open file. Invalid path.")
			return
		except TypeError:
			credentials = credobject

		#Initializing parameters
		self.user = credentials.get('user',None) 
		self.password = credentials.get('password',None)
		self.endpoint = credentials.get('endpoint',None)
		self.port = credentials.get('port',None)
		self.protocol = credentials.get('protocol',None)

		self.connection = self.get_connection()

	def get_connection(self):
		print("Establishing connection to Elasticsearch")
		try:
			es = Elasticsearch([self.endpoint],http_auth=(self.user,self.password),scheme=self.protocol,port=self.port)
			print("Connection established")
			return es
		except ImproperlyConfigured as e:
			print("Unable to connect to Elasticsearch server : Invalid credentials")

	def save_data(self,parameters,data):
		print("Saving data to Elasticsearch")
		try:
			resultset = self.connection.index(index=parameters.get('index',None),doc_type=parameters.get('type',None),body=data)
			return resultset
		except TransportError as e:
			print("Unable to save data to elasticsearch. Please check your connection credentials")

	def search_data(self,parameters,query,search_type='search'):
		# import pdb;pdb.set_trace()
		print("Fetching data from Elasticsearch server")
		if(search_type == 'search'):
			try:
				resultset = self.connection.search(index=parameters.get('index',None), body=query[0])
				return resultset
			except TransportError as e:
				print("Unable to search data. Please check your query and try again")
			except AttributeError as e:
				print("Please connect to Elasticsearch server and try again")
		elif(search_type == 'msearch'):
			response = []
			try:
				for each in query:
					req_head = {'index': parameters.get('index',None), 'type': parameters.get('type',None)}
					req_body = each
					response.append(self.connection.msearch(body = [req_head,req_body]))
				return response
			except TransportError as e:
				print("Unable to search data. Please check your query and try again")
			except AttributeError as e:
				print("Please connect to Elasticsearch server and try again")
		else:
			print("Invalid Search type : Use 'search' or 'msearch' as valid search types")