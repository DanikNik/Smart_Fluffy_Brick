import config

def getProto():

    #with open('output.pcm', 'rb') as audio:
    #   command_in_bytes = audio.read()

    with open('connection_request.proto', 'w') as proto_file:
        proto_file.write("""
    message ConnectionRequest
    {{
    optional int32 protocolVersion = 1;
  
    required string speechkitVersion = '';
            
    required string serviceName = 'asr_dictation';

    required string uuid = '{0}';
            
    required string apiKey = '{1}';
            
    required string applicationName = 'SmartBrick';
            
    required string device = 'Intel_Galileo';
          
    required string coords = '0,0';
            
    required string topic = 'notes';
          
    required string lang = 'ru-RU';
            
    required string format = 'audio/x-pcm;bit=16;rate=16000';
            
    optional bool punctuation = true;
            
    }}""".format(config.uuid, config.key))
    pass

getProto()