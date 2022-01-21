from prettytable import PrettyTable

table = PrettyTable()

table.add_column("Pokemon", ["Pikachu", "Chamandar", "Squirtle"])
table.add_column("Type", ["Electric", "Fire", "Water"])
table.align = "l"
print(table)