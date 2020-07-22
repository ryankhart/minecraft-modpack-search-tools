# minecraft-modpack-search-tools
This is a very work-in-progress, alpha version of a set of tools I'm developing for working with data about Minecraft mods and modpacks webscraped from Curseforge. Currently, it is only set up to take in a particular mod you want to play with and find a modpack that includes that mod. Then, you can filter and sort that list of modpacks by any metric that is collected by your webscraping.

In its current stage, to use it, you will need to actually alter the code until I eventually get it working with command-line arguments, and maybe eventually a graphical user interface, if I take it that far.

Images and Javascript have been disabled for the sake of speed and network usage, but they can easily be turned back on by removing those lines of code from `__main__`

Below, is a gif showing an example of how it should look when it's set up as expected. In this example, I want to find a list of all the modpacks that include Gregtech Community Edition, filter that list to only show modpacks that are on Minecraft version 1.12.2, then sort them by total downloads.

## Demo
![](demo1.gif)

<details>
  <summary>Output text at the very end of this</summary>
  
  ```
  Project Name: FTB Interactions
  Total Downloads: 401123
  Last Updated: 2019-06-26
  
  Project Name: Omnifactory
  Total Downloads: 338313
  Last Updated: 2020-04-20

  Project Name: GregBlock
  Total Downloads: 150923
  Last Updated: 2019-04-10

  Project Name: Infitech 3
  Total Downloads: 9236
  Last Updated: 2020-06-06

  Project Name: Craftologia
  Total Downloads: 6198
  Last Updated: 2019-02-23

  Project Name: Ascension Of Chaos 
  Total Downloads: 3256
  Last Updated: 2019-01-24

  Project Name: DrTARDIS 2 - New Adventures
  Total Downloads: 2917
  Last Updated: 2020-03-29

  Project Name: Howdy do we do?
  Total Downloads: 2170
  Last Updated: 2020-04-03

  Project Name: Darkest Journey 2
  Total Downloads: 1901
  Last Updated: 2020-07-15

  Project Name: qraft
  Total Downloads: 1761
  Last Updated: 2019-08-19

  Project Name: Just Every Mod
  Total Downloads: 1485
  Last Updated: 2019-07-12

  Project Name: New Avalon
  Total Downloads: 1407
  Last Updated: 2019-05-14

  Project Name: Redacted
  Total Downloads: 1340
  Last Updated: 2019-10-29

  Project Name: Living Skies
  Total Downloads: 1300
  Last Updated: 2020-03-01

  Project Name: Monknot Monksnottery
  Total Downloads: 1202
  Last Updated: 2018-09-11

  Project Name: ArchitPack Greg
  Total Downloads: 1165
  Last Updated: 2020-05-24

  Project Name: Gregicality Skyblock Edition
  Total Downloads: 1079
  Last Updated: 2020-06-28

  Project Name: the big F-ing pack
  Total Downloads: 1029
  Last Updated: 2018-08-26

  Project Name: TechMonger SkyBlock Hard Mode Challenge Pack
  Total Downloads: 934
  Last Updated: 2019-04-12

  Project Name: Greglorious
  Total Downloads: 843
  Last Updated: 2019-01-09

  Project Name: AnvilcraftGregging
  Total Downloads: 562
  Last Updated: 2020-04-22

  Project Name: dH WarPack
  Total Downloads: 536
  Last Updated: 2020-07-21

  Project Name: Society Builder
  Total Downloads: 533
  Last Updated: 2019-01-16

  Project Name: Overloaded
  Total Downloads: 488
  Last Updated: 2020-03-20

  Project Name: OmniTech
  Total Downloads: 391
  Last Updated: 2019-10-26

  Project Name: Magic, Tech and More
  Total Downloads: 380
  Last Updated: 2019-08-22

  Project Name: SealCity - Come one Come All
  Total Downloads: 357
  Last Updated: 2020-07-18

  Project Name: Dragoncraft Final Mix
  Total Downloads: 347
  Last Updated: 2019-07-21

  Project Name: Shattered Realities
  Total Downloads: 343
  Last Updated: 2019-04-20

  Project Name: Amaster15 Pack
  Total Downloads: 338
  Last Updated: 2019-06-18

  Project Name: Dimensional Adventurer
  Total Downloads: 338
  Last Updated: 2019-02-16

  Project Name: Gregish Darkcraft
  Total Downloads: 322
  Last Updated: 2020-01-27

  Project Name: AngryRoosters
  Total Downloads: 318
  Last Updated: 2020-05-09

  Project Name: Cybernetic Alchemy
  Total Downloads: 311
  Last Updated: 2020-04-13

  Project Name: Technology & Society
  Total Downloads: 311
  Last Updated: 2020-04-02

  Project Name: [GTCE] Completely Gregged 2
  Total Downloads: 308
  Last Updated: 2020-05-13

  Project Name: Just Building
  Total Downloads: 292
  Last Updated: 2019-05-28

  Project Name: DeltaPack
  Total Downloads: 257
  Last Updated: 2019-01-09

  Project Name: RhettGuyer Server Pack
  Total Downloads: 250
  Last Updated: 2020-07-09

  Project Name: DieK�seKuchen Community Pack
  Total Downloads: 238
  Last Updated: 2020-06-13

  Project Name: Notex 2
  Total Downloads: 226
  Last Updated: 2019-06-15

  Project Name: Im Lande des Donnervogels
  Total Downloads: 222
  Last Updated: 2019-02-22

  Project Name: OnCraftu
  Total Downloads: 215
  Last Updated: 2020-02-08

  Project Name: Infection
  Total Downloads: 208
  Last Updated: 2020-05-23

  Project Name: Stargate Gamma site
  Total Downloads: 207
  Last Updated: 2020-07-13

  Project Name: Nexus Evolution
  Total Downloads: 204
  Last Updated: 2018-11-16

  Project Name: ByteMyASCII's Modded TwitchSpawn Experience
  Total Downloads: 199
  Last Updated: 2020-05-25

  Project Name: Optipixel
  Total Downloads: 193
  Last Updated: 2019-06-01

  Project Name: Progressing Up
  Total Downloads: 189
  Last Updated: 2020-04-01

  Project Name: Crazy Mods Revamped
  Total Downloads: 182
  Last Updated: 2019-11-30

  Project Name: D1ldo Craft
  Total Downloads: 159
  Last Updated: 2020-07-21

  Project Name: Superbia's Modern World
  Total Downloads: 141
  Last Updated: 2020-02-10

  Project Name: All I Can Think
  Total Downloads: 140
  Last Updated: 2019-12-20

  Project Name: Gluggavedur
  Total Downloads: 140
  Last Updated: 2019-06-16

  Project Name: TechnoCraft
  Total Downloads: 127
  Last Updated: 2019-11-11

  Project Name: Blood, Sweat and Gears
  Total Downloads: 120
  Last Updated: 2020-06-06

  Project Name: Galactic Conquest 2
  Total Downloads: 120
  Last Updated: 2019-11-15

  Project Name: MC Anarchy The Unseen Pack
  Total Downloads: 120
  Last Updated: 2020-05-20

  Project Name: Minefactory Reloaded
  Total Downloads: 116
  Last Updated: 2020-05-04

  Project Name: Chakona
  Total Downloads: 113
  Last Updated: 2018-09-28

  Project Name: Gregafirmacraft
  Total Downloads: 111
  Last Updated: 2020-07-05

  Project Name: MC Nullified W.I.P.
  Total Downloads: 105
  Last Updated: 2020-07-06

  Project Name: Anycraft
  Total Downloads: 104
  Last Updated: 2019-09-19

  Project Name: IpHotTub
  Total Downloads: 103
  Last Updated: 2020-06-16

  Project Name: eientei
  Total Downloads: 102
  Last Updated: 2019-07-09

  Project Name: Finity
  Total Downloads: 97
  Last Updated: 2018-08-29

  Project Name: ConfusionPack
  Total Downloads: 95
  Last Updated: 2019-08-28

  Project Name: Standard Deviation
  Total Downloads: 91
  Last Updated: 2020-03-27

  Project Name: Emperor Lelouch's Eternal Crusade
  Total Downloads: 89
  Last Updated: 2019-10-07

  Project Name: Technoblox
  Total Downloads: 89
  Last Updated: 2019-09-29

  Project Name: O.B.O. - Our best Of
  Total Downloads: 85
  Last Updated: 2018-10-21

  Project Name: Nigh-Tech 2
  Total Downloads: 79
  Last Updated: 2019-07-13

  Project Name: Fiore Gaming Modpack
  Total Downloads: 76
  Last Updated: 2019-07-18

  Project Name: Kitsunes Den
  Total Downloads: 70
  Last Updated: 2020-07-06

  Project Name: Gamerland Exploration
  Total Downloads: 68
  Last Updated: 2020-02-03

  Project Name: GentBros Server Pack
  Total Downloads: 61
  Last Updated: 2019-07-18

  Project Name: MBC Kek
  Total Downloads: 59
  Last Updated: 2019-09-07

  Project Name: The Bottle
  Total Downloads: 58
  Last Updated: 2019-02-16

  Project Name: OldNew
  Total Downloads: 57
  Last Updated: 2020-01-05

  Project Name: HMMR Pack
  Total Downloads: 54
  Last Updated: 2020-02-25

  Project Name: Le pack de mods du CREW
  Total Downloads: 54
  Last Updated: 2020-06-11

  Project Name: MoleCraft Tech / Explore / Build / Magic
  Total Downloads: 53
  Last Updated: 2020-05-21

  Project Name: SupremeGaming MC Pack
  Total Downloads: 53
  Last Updated: 2019-05-14

  Project Name: Nexus Evo Lite
  Total Downloads: 46
  Last Updated: 2018-11-17

  Project Name: Chill
  Total Downloads: 44
  Last Updated: 2020-06-07

  Project Name: Techmix
  Total Downloads: 44
  Last Updated: 2020-06-07

  Project Name: Technerds
  Total Downloads: 43
  Last Updated: 2020-07-12

  Project Name: Tech Ultimate
  Total Downloads: 37
  Last Updated: 2020-04-12

  Project Name: Floof Pack
  Total Downloads: 35
  Last Updated: 2020-07-20

  Project Name: Simply Technology
  Total Downloads: 35
  Last Updated: 2019-03-02

  Project Name: Altercraft Ultra
  Total Downloads: 31
  Last Updated: 2019-12-10

  Project Name: Baryon
  Total Downloads: 23
  Last Updated: 2020-04-14

  Project Name: Qwoplandia
  Total Downloads: 21
  Last Updated: 2019-10-11

  Project Name: DiffiCraft
  Total Downloads: 18
  Last Updated: 2019-10-23

  Project Name: suda_pack
  Total Downloads: 15
  Last Updated: 2020-02-10

  Project Name: ArcticCraft Lite
  Total Downloads: 12
  Last Updated: 2020-07-17

  Project Name: gregtech: pioneers
  Total Downloads: 11
  Last Updated: 2020-03-11

  Project Name: Don't Evade Your Taxes p.3
  Total Downloads: 9
  Last Updated: 2020-06-18

  Project Name: SCD - Secure, Contain, And Destroy
  Total Downloads: 9
  Last Updated: 2019-11-05

  Project Name: MCMCMC (MC Modding Community) YesPack
  Total Downloads: 8
  Last Updated: 2020-01-30

  Project Name: TechBlock: SkyTech (WIP)
  Total Downloads: 7
  Last Updated: 2020-07-16

  Project Name: Gefory Modpack
  Total Downloads: 6
  Last Updated: 2020-03-25

  Project Name: Atomic Oblivion
  Total Downloads: 5
  Last Updated: 2020-03-05

  Project Name: BusterGod Pack
  Total Downloads: 5
  Last Updated: 2019-07-29

  Project Name: DuckPack
  Total Downloads: 5
  Last Updated: 2020-04-06

  Project Name: Just another Nightmare
  Total Downloads: 4
  Last Updated: 2020-04-05

  Project Name: MekaSkism
  Total Downloads: 4
  Last Updated: 2020-03-27

  Project Name: DeLuxCraft
  Total Downloads: 3
  Last Updated: 2019-09-30

  Project Name: Jade's Light
  Total Downloads: 3
  Last Updated: 2020-04-29

  Project Name: Romain's modpack
  Total Downloads: 3
  Last Updated: 2019-07-11

  Project Name: Disco's Psycho Depressive LSD Trip
  Total Downloads: 2
  Last Updated: 2020-07-07

  Project Name: Project X
  Total Downloads: 2
  Last Updated: 2019-11-09

  Project Name: Tales of The Wild
  Total Downloads: 2
  Last Updated: 2019-07-18

  Project Name: NolanDoesYT's Modded Series
  Total Downloads: 1
  Last Updated: 2019-12-09

  Project Name: ESE (Enhancing Space Exploration)
  Total Downloads: 0
  Last Updated: 2020-06-09

  ```
</details>

## Instructions
```bash
pip3 install beautifulsoup4
pip3 install selenium
pip3 install lxml
```
Make sure that Google Chrome is installed in the default location it picks on your PC.

Download and install ChromeDriver into a folder of your choosing.
https://chromedriver.chromium.org/downloads

Add the path to your ChromeDriver folder to your Windows path by doing the following:
- Open any File Explorer window.
- Right-click "This PC"
- Click "Properties"
- Click "Advanced system settings"
- Click the "Advanced" tab.
- Click "Environment Variables..."
- In the "System variables" pane, click the "Path" row.
- In the "System variables" pane, click the "Edit..." button.
- Click the "New" button.
- Type or paste the path you chose for your ChromeDriver location.
- Click "OK" when you are finished.

Note: ChromeDriver does not need to be already running in order for the script to work. The script will do that automatically.


```
python3 ./script.py
```
