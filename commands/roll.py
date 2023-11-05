from discord.ext import commands
from tools.dice import roll_dice
from discord.commands import Option

async def roll_logic(ctx, num_dice, sides, slash=False):
    initial_rolls = roll_dice(num_dice, sides)
    response = format_dice_rolls(initial_rolls)
    if slash:
        await ctx.respond(response)
    else:
        await ctx.send(response)

def format_dice_rolls(rolls):
    roll_results = ", ".join(map(str, rolls))
    return f"🎲 Lancers de dés: {roll_results}"

def setup(bot):
    @bot.command(name='roll')
    async def roll(ctx, *, dice_input):
        try:
            num_dice, sides = map(int, dice_input.lower().split('d'))
            await roll_logic(ctx, num_dice, sides)
        except (ValueError, IndexError):
            await ctx.send("Format incorrect. Utilisez `!roll [nombre]d[côtés]`.")

    @bot.slash_command(name='roll')
    async def roll_slash(
        ctx,
        num_dice: Option(int, "Nombre de dés à lancer", required=True),
        sides: Option(int, "Nombre de faces du dé", required=True)
    ):
        await ctx.defer()
        await roll_logic(ctx, num_dice, sides, slash=True)
