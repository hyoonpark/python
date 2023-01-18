members = [
	{'id': 102, 'name': "Ashley Allen", 'address': "Seoul"},
	{'id': 202, 'name': "Peter Parker", 'address': "New York"},
	{'id': 104, 'name': "John Smith", 'address': "Tokyo"},
]
print(list(m['address'] for m in members))
## ['Seoul', 'New York', 'Tokyo']