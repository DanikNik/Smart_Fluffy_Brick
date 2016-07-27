import start_request
import os

command2 = ''
while True:
	command1 = start_request.listen_for_speech()
	os.remove('command.pcm')
	if command1 == 'кирпич':
		print("I'm listening, my Owner!")
		command2 = start_request.listen_for_speech()
		print(command2)
		break
	else:
		continue

 