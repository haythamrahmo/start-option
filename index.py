from deriv_api import DerivAPI
api = DerivAPI(endpoint='wss://ws.binaryws.com/websockets/v3', app_id=1234);
response = await api.ping({'ping': 1})
print(response) 
   api = DerivAPI(endpoint='wss://ws.binaryws.com/websockets/v3', app_id=1234);
   connection = await websockets.connect(''wss://ws.binaryws.com/websockets/v3')
   api = DerivAPI(connection=connection)
