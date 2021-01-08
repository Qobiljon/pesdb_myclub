import requests
import re


legends = open('legend_players.csv', 'a+', encoding='utf8')
regulars = open('regular_players.csv', 'a+', encoding='utf8')

legends.write('name, position, max_rating\n')
regulars.write('name, position, max_rating\n')

input_name = ''
while input_name != 'end':
	input_name = input("Name : ")
	text = requests.get(f'https://pesdb.net/pes2021/?name={input_name}').text

	if 'No players found.' in text:
		text = requests.get(f'https://pesdb.net/pes2021/?name={input_name}&all=1').text
		if 'No players found.' in text:
			print('player not found')
			continue
		else:
			# legend player
			is_legend = True
	else:
		# regular player
		is_legend = False

	substr = text[text.index('<td class="pos'):]
	substr = substr[:substr.index('</div>')]
	_pos = substr[substr.rindex('>')+1:]

	substr = text[text.index('<td class="left"><a href="./?id='):]
	substr = substr[:substr.index('</a>')]
	_name = substr[substr.rindex('>')+1:]
	_id = substr[substr.rindex('=')+1:substr.rindex('"')]

	text = requests.get(f'https://pesdb.net/pes2021/?id={_id}').text

	_re = re.search(r'(abilities = \[\[)(.+)+(\]];)', text)
	arr = _re.group(2)
	_rate = arr[arr.rindex(',')+1:]

	if is_legend:
		legends.write(f'{_name}, {_pos}, {_rate}\n')
	else:
		regulars.write(f'{_name}, {_pos}, {_rate}\n')

	print(_name, _pos, _rate)

legends.close()
regulars.close()
