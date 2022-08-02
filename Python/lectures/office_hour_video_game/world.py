import player
import weapons

first_player = {
    'name': 'Bill',
    'strength': 75,
    'speed': 65
}

second_player = {
    'name': 'Jorge',
    'strength': 20,
    'speed': 40,
}

Bill = player.Player(first_player) #looking inside 'player' file to find 'Player' class
Jorge = player.Player(second_player)

#print(Joe.name)
#print(player.Player.all_players)
player.Player.print_all_player_names()

ax = {
    'name': 'Arthur',
    'damage': 50,
    'weight': 20,
    'type': 'blunt'
}

green_ax = weapons.Weapon(ax)
#print(green_ax)

# Bill.weapons.append(green_ax)
Bill.add_weapon(green_ax)
print(Bill.weapons)

Bill.use_weapon(Jorge, green_ax)
Bill.use_weapon(Jorge, green_ax)
