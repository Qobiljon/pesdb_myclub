import matplotlib.pyplot as plt
import os

for players in ['legend_players', 'regular_players']:
	with open(f'{players}.csv', 'r', encoding='utf8') as r:
		counts = {}
		for line in r.readlines()[1:]:
			name, position, rating = line[:-1].split(', ')
			rating = int(rating)
			if position in counts:
				if rating in counts[position]:
					counts[position][rating] += 1
				else:
					counts[position][rating] = 1
			else:
				counts[position] = {rating:1}

	if not os.path.exists(f'plots/{players}'):
		os.mkdir(f'plots/{players}')
	for position in counts:
		x = list(range(85, 101))
		y = [counts[position][rate] if rate in counts[position] else 0 for rate in x]
		print(position, x, y)
		
		plt.clf()
		plt.bar(x, y)
		plt.ylim(0, 10)
		plt.xlabel('Ratings')
		plt.ylabel('Counts')
		plt.xticks(x)
		plt.yticks(list(range(1, max(y)+1)))
		plt.savefig(f'plots/{players}/{position}.png', dpi=400)
