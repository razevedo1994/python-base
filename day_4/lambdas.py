nomes = ["Bruno", "João", "Maria", "Carlos", "Erik"]
print(sorted(nomes, key=len))
# ['João', 'Erik', 'Bruno', 'Maria', 'Carlos']

print(list(filter(lambda x: x.startswith("B"), nomes)))
# ['Bruno']
