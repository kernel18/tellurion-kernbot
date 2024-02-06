"""View classes."""

import discord

from modules.game.views import GameView, PlayView
from modules.petrigon.player import Player
from modules.petrigon.hex import Hex


class PanelView(GameView):
    update_on_init = False

    def __init__(self, game, panel, *args, **kwargs):
        super().__init__(game, *args, **kwargs)
        self.panel = panel

        if self.update_on_init: self.update()

    def update(self):
        pass


class JoinView(PanelView):
    def check_for_enough_players(self):
        if self.game.mainclass.debug:
            return True, "Démarrer"

        if len(self.game.players) < 2:
            return False, "Pas assez de joueurs"
        
        if len(self.game.players) > 6:
            return False, "Trop de joueurs"
        
        return True, "Démarrer"

    def update(self):
        super().update()
        can_start, message = self.check_for_enough_players()
        self.children[1].label = message
        self.children[1].disabled = not can_start
        self.children[1].style = discord.ButtonStyle.green if can_start else discord.ButtonStyle.gray

    @discord.ui.button(label="Rejoindre ou quitter", style=discord.ButtonStyle.blurple)
    async def join_or_leave(self, button, interaction):
        if len(self.game.players) > 6:
            return await interaction.response.send_message("Le nombre maximum de joueurs est atteint.", ephemeral=True)

        if interaction.user.id not in self.game.players:
            self.game.players[interaction.user.id] = Player(self.game, interaction.user)
        else:
            del self.game.players[interaction.user.id]

        await self.panel.update(interaction)
    
    @discord.ui.button(label="Pas assez de joueurs", disabled=True, style=discord.ButtonStyle.gray)
    async def start(self, button, interaction):
        if interaction.user.id not in self.game.players:
            return await interaction.response.defer()

        await self.game.start()

    @discord.ui.button(label="Pouvoirs désactivés", emoji="🦸", style=discord.ButtonStyle.gray)
    async def send_input_modal(self, button, interaction):
        if interaction.user.id in self.game.players:
            self.game.powers_enabled = not self.game.powers_enabled
            button.label = f"Pouvoirs {'activés' if self.game.powers_enabled else 'désactivés'}" 
            button.style = discord.ButtonStyle.green if self.game.powers_enabled else discord.ButtonStyle.gray
            return await self.panel.update(interaction)

        await interaction.response.defer()


class FightView(PanelView, PlayView):
    update_on_init = True

    def update(self):
        self.children[7].disabled = not (self.game.current_player.power and self.game.current_player.power.active)

    @discord.ui.button(emoji="↖️", style=discord.ButtonStyle.blurple)
    async def move_up_left(self, button, interaction):
        await self.try_to_move(interaction, Hex(0, -1))

    @discord.ui.button(emoji="⬅️", style=discord.ButtonStyle.blurple)
    async def move_left(self, button, interaction):
        await self.try_to_move(interaction, Hex(-1, 0))

    @discord.ui.button(emoji="↗️", style=discord.ButtonStyle.blurple)
    async def move_up_right(self, button, interaction):
        await self.try_to_move(interaction, Hex(1, -1))
    
    @discord.ui.button(emoji="↙️", style=discord.ButtonStyle.blurple, row=1)
    async def move_down_left(self, button, interaction):
        await self.try_to_move(interaction, Hex(-1, 1))
    
    @discord.ui.button(emoji="➡️", style=discord.ButtonStyle.blurple, row=1)
    async def move_right(self, button, interaction):
        await self.try_to_move(interaction, Hex(1, 0))
    
    @discord.ui.button(emoji="↘️", style=discord.ButtonStyle.blurple, row=1)
    async def move_down_right(self, button, interaction):
        await self.try_to_move(interaction, Hex(0, 1))

    async def try_to_move(self, interaction, direction):
        if interaction.user != self.game.current_player.user:
            return await interaction.response.defer()
        
        if self.game.current_player.move(direction):
            await self.game.next_turn(interaction)
        else:
            await interaction.response.send_message("Ce mouvement ne cause aucun changement du plateau.", ephemeral=True)

    @discord.ui.button(emoji="💀", style=discord.ButtonStyle.red)
    async def forfeit(self, button, interaction):
        player = self.game.players[interaction.user.id]
        player.forfeit()
        
        if player == self.game.current_player:
            await self.game.next_turn(interaction)
        else:
            await self.game.check_for_game_end(interaction)

    @discord.ui.button(emoji="🦸", style=discord.ButtonStyle.green, row=1)
    async def use_ability(self, button, interaction):
        if interaction.user != self.game.current_player.user:
            return await interaction.response.defer()
        
        if self.game.current_player.use_power():
            await self.panel.update(interaction)
        else:
            await interaction.response.send_message("Vous ne pouvez pas utiliser votre pouvoir.", ephemeral=True)


class PowerView(PlayView):
    pass