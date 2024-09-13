import json
import codecs
import pygame

name = input("File: ")
pygame.init()

resolution = (1000,1000)
SCREEN = pygame.display.set_mode(resolution, pygame.RESIZABLE)

SCREEN.fill((0,0,0))


pygame.display.flip()

file = codecs.open(name, encoding= "utf-8-sig")
text = file.read()
data = json.loads(text)

# print(data)

layers = data["layers"][0]
# data["layers"][0] is the landscape 
# data["layers"][1] contain decorations
# data["layers"][2] contain barrels/tnt  ?? EggE may be sawblade
# data["layers"][3] is null
# data["layers"][4] is the player respawn points/checkpoints 
# data["layers"][5] MAY BE TRIGGER SHIT

objectList = []

objectListHW = []

objectName = []
objectHWName = []

def getObjects(layers):
    for i in layers:
        print(i["className"])
        x = int(i["params"]["x"])
        y = int(i["params"]["y"])

        print(x,y)
        globalPos = []
        try: 
            for v in i["params"]["vertices"]:
                print("X/Y",v["x"], v["y"])
                localx = int(v["x"])
                localy = int(v["y"])
                globalPos.append([localx + x, localy + y])
            objectList.append(globalPos)
            objectName.append(i["className"])
        except:
            print("H/W",i["params"]["height"], i["params"]["width"])
            objectListHW.append((x,y,i["params"]["height"], i["params"]["width"]))
            objectHWName.append(i["className"])
        print(globalPos)
        print("\n")
    return objectList, objectListHW, objectName, objectHWName

decLayer = data["layers"][2]
layer5 = data["layers"][5]
decs = getObjects(decLayer)
triggers = getObjects(layer5)
OBJ = getObjects(layers)

objectList = OBJ[0]
objectListHW = OBJ[1]
objectName = OBJ[2]
objectHWName = OBJ[3]





rect = pygame.rect.Rect(0,0,1,1)

vertex = pygame.image.load("vertices.png")

moveV = [0,0]
zoomV = 1
timer = pygame.time.Clock()
for item in objectList:
    if objectName[objectList.index(item)] == "frg.game.editor.objects::LandscapeShaper":
        item.append(item[0])

while True:
    timer.tick(60)
    SCREEN.fill((0,0,0))
    for v in objectListHW:
        
        surface = pygame.surface.Surface((v[3]*zoomV,v[2]*zoomV))
        rec = pygame.rect.Rect(zoomV*(v[0] + moveV[0]), zoomV*(v[1] + moveV[1]), v[3]*zoomV, v[2]*zoomV)
        rec.center = (zoomV*(v[0] + moveV[0]), zoomV*(v[1] + moveV[1]))
        if objectHWName[objectListHW.index(v)] == "FinishZone":
            surface.fill((50,255,50,100))
        elif objectHWName[objectListHW.index(v)] == "PivotJointE":
            surface.fill((100,100,100,100))
        elif objectHWName[objectListHW.index(v)] == "ToggleE":
            surface.fill((255,255,100,100))
        elif objectHWName[objectListHW.index(v)] == "MotorJointE":
            surface.fill((100,255,255,100))
        elif objectHWName[objectListHW.index(v)] == "Tnt1":
            surface.fill((120,60,0,150))
        elif objectHWName[objectListHW.index(v)] == "BarrelE":
            surface.fill((100,100,100))
        else:
            surface.fill((255,0,255,100))
        SCREEN.blit(surface, rec)#(zoomV*(v[0] + moveV[0]),zoomV*(v[1] + moveV[1])))

    for item in objectList:
        vOG = item[0]
        for v in item:
            # print([(v[0] + moveV[0])*zoomV,(v[1] + moveV[1])*zoomV])
# LandscapeShaper: RED
# 
# DynamicPather: Green
# 
# PillarPather: Blue
# 
# GroundPather: Magenta
#             
# FinishZone: Green
# 
# MoverPather: Cyan
# 
# Others: white
            SCREEN.blit(vertex, [(v[0] + moveV[0])*zoomV,(v[1] + moveV[1])*zoomV])
            if objectName[objectList.index(item)] == "frg.game.editor.objects::LandscapeShaper":
                pygame.draw.line(SCREEN,pygame.color.Color(255,0,0,255),[int(zoomV*(vOG[0] + moveV[0])),int((vOG[1]+moveV[1])*zoomV)],[int((v[0] + moveV[0])*zoomV), int((v[1] + moveV[1])*zoomV)])
            elif objectName[objectList.index(item)] == "frg.game.editor.objects::DynamicPather":
                pygame.draw.line(SCREEN,pygame.color.Color(0,255,0,255),[int(zoomV*(vOG[0] + moveV[0])),int((vOG[1]+moveV[1])*zoomV)],[int((v[0] + moveV[0])*zoomV), int((v[1] + moveV[1])*zoomV)])
            elif objectName[objectList.index(item)] == "frg.game.editor.objects::PillarPather":
                pygame.draw.line(SCREEN,pygame.color.Color(0,0,255,255),[int(zoomV*(vOG[0] + moveV[0])),int((vOG[1]+moveV[1])*zoomV)],[int((v[0] + moveV[0])*zoomV), int((v[1] + moveV[1])*zoomV)] )
            elif objectName[objectList.index(item)] == "frg.game.editor.objects::GroundPather":
                pygame.draw.line(SCREEN,pygame.color.Color(255,0,255,255),[int(zoomV*(vOG[0] + moveV[0])),int((vOG[1]+moveV[1])*zoomV)],[int((v[0] + moveV[0])*zoomV), int((v[1] + moveV[1])*zoomV)])
            elif objectName[objectList.index(item)] == "frg.game.editor.objects::MoverPather":
                pygame.draw.line(SCREEN,pygame.color.Color(100,255,255,100),[int(zoomV*(vOG[0] + moveV[0])),int((vOG[1]+moveV[1])*zoomV)],[int((v[0] + moveV[0])*zoomV), int((v[1] + moveV[1])*zoomV)])
            else:
                print(objectName[objectList.index(item)])
                pygame.draw.line(SCREEN,pygame.color.Color(255,255,255,255),[int(zoomV*(vOG[0] + moveV[0])),int((vOG[1]+moveV[1])*zoomV)],[int((v[0] + moveV[0])*zoomV), int((v[1] + moveV[1])*zoomV)])
            vOG = v
    
    keys = pygame.key.get_pressed()

    if keys[pygame.K_RIGHT]:
        moveV[0] -= 40
    elif keys[pygame.K_LEFT]:
        moveV[0] += 40
    if keys[pygame.K_UP]:
        moveV[1] += 40
    if keys[pygame.K_DOWN]:
        moveV[1] -= 40
    # if keys[pygame.K_EQUALS]:
    #     print("+")
    #     zoomV = zoomV * 2
    # if keys[pygame.K_MINUS]: # and zoomV > 1:
    #     print("-")
    #     zoomV = zoomV * .5
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_EQUALS:
                print("+")
                zoomV = zoomV * 2
            if event.key == pygame.K_MINUS:
                print("-")
                zoomV = zoomV * .5
    pygame.display.flip()

print()
