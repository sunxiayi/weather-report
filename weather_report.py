from twilio.rest import TwilioRestClient
import urllib2
import json
import StringIO
import emoji

# get weather report through API
f = urllib2.urlopen('http://api.wunderground.com/api/32f52fce23bd21c2/forecast/q/MI/Ann_Arbor.json')
json_string = f.read()
parsed_json = json.loads(json_string)['forecast']['txt_forecast']['forecastday']

# get weather messages of the next two days
msg_list = []
for x in xrange(1,5):
	time = parsed_json[x]['title']
	report = parsed_json[x]['fcttext_metric']
	final_msg = time + ': ' + report
	msg_list.append(final_msg)
f.close()

# convert messages to strings
output = StringIO.StringIO()
for msg in msg_list:
	output.write('\n' + '\n')
	output.write(emoji.emojize(':heartbeat:', use_aliases=True))
	output.write(' ' + msg)

# send messages
accountSID = ''
authToken = ''
twilioCli = TwilioRestClient(accountSID, authToken)
myTwilioNumber = ''
myCellPhone = ''
message = twilioCli.messages.create(body = output.getvalue(), from_ = myTwilioNumber, to = myCellPhone)

output.close()