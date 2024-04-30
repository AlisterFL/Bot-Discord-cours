import asyncio
import random
import discord
from discord.ext import commands

intents = discord.Intents().all()
bot = commands.Bot(command_prefix="!", intents=intents)

intents.message_content = True
# guilds = serveurs discords
intents.guilds = True
intents.members = True

# Liste de blagues
jokes = [
    "Pourquoi la petite fille tombe-t-elle de la balançoire? Parce qu’elle n’a pas de bras.",
    "Grâce à quoi peut-on enlever le chewing-gum dans les cheveux ? Le cancer.",
    "Qu'est-ce qui est mieux que gagner une médaille d'or aux Jeux Paralympiques ? Marcher.",
    "Un prêtre demande à un tueur condamné à la chaise électrique : - Avez-vous un dernier souhait ? - Oui, pouvez-vous me tenir la main ? "
]

# Liste d'insultes
insultes = ["tg", "vtf", "connard"]

# Liste de proverbes motivants
proverbes_motivants = [
    "L'avenir appartient à ceux qui croient en la beauté de leurs rêves. - Eleanor Roosevelt",
    "Ne regarde pas en arrière, tu n'y vas pas. - Walt Disney",
    "Le seul moyen de faire du bon travail est d'aimer ce que vous faites. - Steve Jobs",
    "Là où il y a une volonté, il y a un chemin. - Winston Churchill",
    "Le succès n'est pas la clé du bonheur. Le bonheur est la clé du succès. Si vous aimez ce que vous faites, vous réussirez. - Albert Schweitzer",
    "La vie est 10% ce qui nous arrive et 90% comment nous y réagissons. - Charles R. Swindoll",
    "La seule limite à notre épanouissement de demain sera nos doutes d'aujourd'hui. - Franklin D. Roosevelt",
    "La seule façon de faire du bon travail est d'aimer ce que vous faites. - Steve Jobs",
    "N'abandonnez jamais vos rêves. Ils vous guident vers votre objectif. - Inconnu",
    "Chaque jour est une nouvelle opportunité de changer votre vie. - Inconnu"
]

@bot.event
async def on_ready():
    print(f"{bot.user.name} s'est bien connecté !")

@bot.command()
async def ping(ctx):
    """Affiche "Pong 🏓"."""
    await ctx.send("Pong 🏓")

@bot.command()
async def touché(ctx):
    """Affiche "Coulé ⚓️"."""
    await ctx.send("Coulé ⚓️")
@bot.command()
async def members(ctx):
    """Affiche la liste des membres du serveur."""
    members_list = ctx.guild.members
    members_string = "Liste des membres du serveur :\n"
    for member in members_list:
        members_string += f"{member.display_name}\n"
    await ctx.send(members_string)

@bot.command()
async def joke(ctx):
  """Affiche une blague aléatoire depuis la liste."""
  random_joke = random.choice(jokes)
  await ctx.send(random_joke)

@bot.command()
async def welcome(ctx):
    """Souhaite la bienvenue à un utilisateur."""
    author_name = ctx.author.display_name
    await ctx.send(f"Bienvenue, {author_name} ! Nous sommes ravis de te voir parmi nous.")
    await ctx.send("https://tenor.com/view/namasthe-namaskaram-hi-bean-mr-bean-gif-18425301")

@bot.command()
async def motivation(ctx):
    """Affiche un proverbe motivant depuis la liste."""
    random_proverbe = random.choice(proverbes_motivants)
    await ctx.send(random_proverbe)

@bot.event
async def on_message(message):
    if "MSPR" in message.content:
        await message.channel.send("Bravo a toi, c'etait le mot de trop")
        await message.channel.send("https://tenor.com/view/salut-mon-pote-hi-buddy-michel-drucker-gif-16070000")
        await asyncio.sleep(3)
        await message.author.kick(reason="Utilisateur a écrit MSPR")

    for insulte in insultes:
        if insulte in message.content.lower():
            await message.channel.send("Ce serveur prône le respect et la bienveillance. Merci de ne pas utiliser de langage inapproprié.")
            await message.channel.send("https://tenor.com/view/holly-logan-comedian-comic-not-today-satan-not-today-gif-15388448")
            break  # Sort de la boucle dès qu'une insulte est trouvée


    await bot.process_commands(message)

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("Cette commande n'existe pas.")



#connexion du bot au serveur avec au token
bot.run("TOKEN")