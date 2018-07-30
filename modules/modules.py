import discord
import asyncio
import os
import importlib
import traceback
class MainClass():
    def __init__(self, client, modules, saves):
        self.states={}
        for moduleName in os.listdir('modules'):
            if moduleName.endswith(".py"):
                self.states.update({moduleName[:-3:]:'not loaded'})
        self.client = client
        self.modules = modules
        self.saves = saves
        self.events=['on_message', 'on_ready'] #events list
        self.command="/modules" #command prefix (can be empty to catch every single messages)

        self.name="Modules"
        self.description="Module de gestion des modules"
        self.help="""
 /modules list
 => liste les modules ainsi que leurs états
 
 /modules enable <module/modules>
 => Charge et active le / les modules spécifié(s)
 
 /modules disable <module/modules>
 => Désactive et décharge le / les modules spécifié(s)
 
 /modules reload <module/modules>
 => Désactive, puis décharge, puis recharge, puis réactive le / les modules spécifié(s)
 
 => <module/modules>
 ==> unique module ou liste de module séparés par des virgules
"""[1::]
        self.states.update({'modules': 'initialized'})
    async def on_message(self, message):
        args = message.content.split(" ")
        if len(args) == 2 and args[1]=='list':
            await message.channel.send(embed=discord.Embed(title="[Modules] - Modules list", description="```PYTHON\n{0}```".format(str(self.states).replace(',', '\n,'))))
        elif len(args) == 3 and args[2] in ['enable', 'disable', 'reload']:
            pass
    async def on_ready(self):
        for fileName in os.listdir('modules'):
            try:
                self.load_module(fileName[:-3:])
                self.init_module(fileName[:-3:])
            except:
                pass

    def load_module(self, moduleName):
        if moduleName + ".py" in os.listdir('modules'):
            if self.states[moduleName] == 'not loaded':
                try:
                    self.modules.update({moduleName:[importlib.import_module('modules.' + moduleName)]})
                    print("Module {0} chargé.".format(moduleName))
                    self.states[moduleName] = 'loaded'
                except:
                    print("[ERROR] Le module {0} n'a pas pu être chargé.".format(moduleName))
                    self.unload_module(moduleName)
                    raise
    def init_module(self, moduleName):
        if moduleName + ".py" in os.listdir('modules'):
            if self.states[moduleName] == 'loaded':
                try:
                    self.modules[moduleName].append(self.modules[moduleName][0].MainClass(self.client, self.modules, self.saves))
                    print("Module {0} initialisé.".format(moduleName))
                    self.states[moduleName] = 'initialized'
                except:
                    print("[ERROR] Le module {0} n'a pas pu être initialisé.".format(moduleName))
                    self.unload_module(moduleName)
                    raise
    def unload_module(self, moduleName):
        if moduleName + ".py" in os.listdir('modules'):
            self.states[moduleName] = 'not loaded'
            self.modules.pop(moduleName, None)
            print("Module {0} déchargé.".format(moduleName))
