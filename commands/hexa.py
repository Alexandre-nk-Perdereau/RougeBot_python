import discord
from discord.ext import commands
from tools.dice import hexa_roll

async def common_hexa_logic(ctx, num_dice: int, slash: bool = False):
    successes, all_rolls = hexa_roll(num_dice)
    roll_strs = [' , '.join(map(str, rolls)) for rolls in all_rolls]
    response = (f'🎲 Vous avez lancé {num_dice} dés. Résultats :\n' +
                '\n'.join(roll_strs) +
                f'\nNombre de succès : {successes}.')

    if slash:
        await ctx.respond(response)
    else:
        await ctx.send(response)

def setup(bot):
    @bot.command(name='hexa', aliases=['h'])
    async def hexa(ctx, num_dice: int):
        await common_hexa_logic(ctx, num_dice)

    @bot.slash_command(name='hexa')
    async def hexa_slash(ctx, num_dice: int):
        await common_hexa_logic(ctx, num_dice, slash=True)
