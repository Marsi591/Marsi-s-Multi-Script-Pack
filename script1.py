
import random
import string

file = open('nitro-gen.txt', 'w+')

while True:
    random_str = ''.join(random.choices(string.ascii_letters + string.digits, k=12))
    discord_str = 'discord.gift/' + random_str
    file.write(discord_str + '\n')
    print(discord_str)
