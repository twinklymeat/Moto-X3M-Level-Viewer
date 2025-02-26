# Moto X3M Level Viewer
 Moto X3M Level viewing tool for seeing triggers and stuff

![image](https://github.com/user-attachments/assets/6f97bb75-e66f-4289-a12e-48192a35a89a)

![image](https://github.com/user-attachments/assets/f2398655-959d-4736-93e0-66bd79ab3516)

![image](https://github.com/user-attachments/assets/2185a99c-4072-4b3e-9326-8cacde5127fa)


# How to use:

main.py is the powerhouse of this project, download.py will just download all the levels from og, winter, pool party, and spooky land. 

the directories will look somethink like this:

moto/(1-25).json

winter/(1-25).json

spooky/(1-22).json

pool/(1-22).json

you do not need to put .json after the file name for the program to work. 

# KEY: 

### Lines: 

LandscapeShaper: RED

DynamicPather: Green

PillarPather: Blue

GroundPather: Magenta

MoverPather: Cyan

Others: white




### Boxes:

FinishZone: Green

Toggle Triggers: Yellow

Barrels: Light Grey

TNT: Brown

Pivot Joint: Grey

Motor Joint: Cyan

EggE?: White

NOT EVERYTHING HAS A SPECIFIC COLOR

if a box/line does not have a set color, it is purple

# CONTROLS:

Arrows: Move

T: show/hide triggers

D: show/hide decorations

Ctrl + D: toggle dev mode (prints uncolored objects to the terminal)

C: show/hide checkpoint triggers

+/-: zoom in/out

Ctrl + O: open a new file

# Install:
Make sure you have python installed on your computer
### Linux/Mac (maybe idk i dont use macs)
use the following commands
```bash
git clone https://github.com/twinklymeat/Moto-X3M-Level-Viewer.git
```
```bash
cd Moto-X3M-Level-Viewer
```
```bash
python3 main.py
```

(downloading release technically works but i find it more convenient to use the above method for linux)

### Windows 

just download the latest release, 

But if u want to be fancy with it:

```bash
git clone https://github.com/twinklymeat/Moto-X3M-Level-Viewer.git
```
```bash
cd Moto-X3M-Level-Viewer
```
```bash
main.py
```


