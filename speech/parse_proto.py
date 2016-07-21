import config

def getProto():

	with open('output.pcm', 'rb') as audio:
		command_in_bytes = audio.read()

	with open('connection_request.proto', 'w') as proto_file:
		proto_file.write("""
	message ConnectionRequest\n
	{\n
  	optional int32 protocolVersion = 1 ;\n
  
	required string speechkitVersion = ;\n
            
  	required string serviceName = 'asr_dictation';\n
            
  	required string uuid = {0};\n
            
  	required string apiKey = {1};\n
            
  	required string applicationName = 'SmartBrick';\n
            
  	required string device = 'Intel_Galileo';\n
            
  	required string coords = 0,0;\n
            
  	required string topic = 'notes';\n
            
  	required string lang = 'ru-RU';\n
            
  	required string format = 'audio/x-pcm;bit=16;rate=16000';\n
            
  	optional bool punctuation = true;\n
            
 	}\n

 	message AddData\n
	{\n
  	optional bytes audioData = {2};\n
            
  	required bool lastChunk = true;\n
  	}""".format(config.uuid, config.key, command_in_bytes))
	pass

getProto()