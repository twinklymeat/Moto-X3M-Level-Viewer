import json
import codecs
import pygame
from math import *

pygame.init()


def __main__():
    while True:
        try:
            name = input("File: ")
            file = codecs.open(name, encoding= "utf-8-sig")
            break
        except:
            pass
    pygame.display.set_caption(name)
    text = file.read()
    data = json.loads(text)

    resolution = (1000,1000)
    SCREEN = pygame.display.set_mode(resolution, pygame.RESIZABLE)

    SCREEN.fill((0,0,0))


    pygame.display.flip()


    # print(data)

    layers = data["layers"][0]
    # data["layers"][0] is the landscape 
    # data["layers"][1] contain decorations
    # data["layers"][2] contain barrels/tnt  ?? EggE may be sawblade
    # data["layers"][3] is a second Decoration Category?? maybe??
    # data["layers"][4] is the player respawn points/checkpoints 
    # data["layers"][5] MAY BE TRIGGER SHIT

    objectList = []

    objectListHW = []

    objectName = []
    objectHWName = []
    def getObjects(layers):
            for i in layers:
                # print(i["className"])
                x = int(i["params"]["x"])
                y = int(i["params"]["y"])

                # print(x,y)
                globalPos = []
                try: 
                    for v in i["params"]["vertices"]:
                        # print("X/Y",v["x"], v["y"])
                        localx = int(v["x"])
                        localy = int(v["y"])
                        globalPos.append([localx + x, localy + y])
                    objectList.append(globalPos)
                    objectName.append(i["className"])
                except:
                    # print("H/W",i["params"]["height"], i["params"]["width"])
                    objectListHW.append((x,y,i["params"]["height"], i["params"]["width"],i["params"]["rotation"]))
                    objectHWName.append(i["className"])
                # print(globalPos)
                # print("\n")
            return objectList, objectListHW, objectName, objectHWName


        # def getObjects(layers):
        #     for i in layers:
        #         # print(i["className"])
        #         x = int(i["params"]["x"])
        #         y = int(i["params"]["y"])

        #         # print(x,y)
        #         globalPos = []
        #         try: 
        #             for v in i["params"]["vertices"]:
        #                 # print("X/Y",v["x"], v["y"])
        #                 localx = int(v["x"])
        #                 localy = int(v["y"])
        #                 globalPos.append([localx + x, localy + y])
        #             objectList.append(globalPos)
        #             objectName.append(i["className"])
        #         except:
        #             # print("H/W",i["params"]["height"], i["params"]["width"])
        #             objectListHW.append((x,y,i["params"]["height"], i["params"]["width"],i["params"]["rotation"]))
        #             objectHWName.append(i["className"])
        #         # print(globalPos)
        #         # print("\n")
        #     return objectList, objectListHW, objectName, objectHWName

    decLayer = data["layers"][1]
    try:
        layer5 = data["layers"][5]
    except:
        layer5 = None
    checkpoints = data["layers"][4]
    tnt = data["layers"][2]
    mystery = data["layers"][3]

    if decLayer != None:
        decs = getObjects(decLayer)
    if layer5 != None:
        triggers = getObjects(layer5)
    if tnt != None:
        tntLayer = getObjects(tnt)
    if mystery != None:
        mysteryLayer = getObjects(mystery)
    # try:
    #     print("2nd Decoration Successful!")
    # except:
        # pass
    if checkpoints != None:
        savepoints = getObjects(checkpoints)

    # try:

    OBJ = getObjects(layers)

    objectList = OBJ[0]
    objectListHW = OBJ[1]
    objectName = OBJ[2]
    objectHWName = OBJ[3]



    # start(objectListHW, objectList, objectName, objectHWName)



    rect = pygame.rect.Rect(0,0,1,1)

    vertex = pygame.image.load("vertices.png")

    moveV = [0,0]
    zoomV = 1
    timer = pygame.time.Clock()
    for item in objectList:
        if objectName[objectList.index(item)] in ["frg.game.editor.objects::LandscapeShaper", "frg.game.editor.objects::FinishShaper", "frg.game.editor.objects::WaterShaper"]:
            item.append(item[0])

    showTriggers = True
    showCheck = True
    showDecs = False
    debug = False

    # start()
    restart = False
    while True:
        timer.tick(60)
        SCREEN.fill((0,0,0))
        for v in objectListHW:
            
            surface = pygame.surface.Surface((v[3]*zoomV,v[2]*zoomV))
            rec = pygame.rect.Rect(zoomV*(v[0] + moveV[0]), zoomV*(v[1] + moveV[1]), v[3]*zoomV, v[2]*zoomV)
            rec.center = (zoomV*(v[0] + moveV[0]), zoomV*(v[1] + moveV[1]))
            """
            v[0] = x
            v[1] = y
            v[2] = width
            v[3] = height
            v[4] = rotation
            """
            if not showTriggers:
                if objectHWName[objectListHW.index(v)] in ["ToggleE", "EggE", "OvalTemplate","CameraZoneE"]:
                    continue
            
            if not showCheck:
                if objectHWName[objectListHW.index(v)] == "SafePointE":
                    continue

            if not showDecs:
                if "Dec" in objectHWName[objectListHW.index(v)]:
                    continue
            # print(v)
            color = ()
            if  objectHWName[objectListHW.index(v)] == "FinishZone":
                color = (50,255,50)
            elif objectHWName[objectListHW.index(v)] == "PivotJointE":
                color = (100,100,100,100)
            elif objectHWName[objectListHW.index(v)] == "ToggleE":
                color = (255,255,100,100)
            elif objectHWName[objectListHW.index(v)] == "MotorJointE":
                color = (100,255,255,100)
            elif objectHWName[objectListHW.index(v)] == "Tnt1":
                color = (120,60,0,150)
            elif objectHWName[objectListHW.index(v)] == "BarrelE":
                color = (200,200,200)
            elif objectHWName[objectListHW.index(v)] == "EggE": # I think this is to load other geometry
                color = (255,255,255)
            elif objectHWName[objectListHW.index(v)] == "SpikesE":
                color = (255,0,0)
            elif objectHWName[objectListHW.index(v)] in ["Removed0","Removed1"]: #removed0 is vertical Removed1 is horizontal
                color = (150,80,0)
            elif objectHWName[objectListHW.index(v)] == "PlayerWP":
                color = (255,255,255)
            elif objectHWName[objectListHW.index(v)] == "SafePointE":
                color = (0,150,0)
            elif objectHWName[objectListHW.index(v)] in ["GlassCrashed1","GlassCrashed0"]:
                color = (0,255,255)
            elif objectHWName[objectListHW.index(v)] == "GeyserE":
                color = (0,0,255)
            elif objectHWName[objectListHW.index(v)] == "BoostE":
                color = (0,0,150)
            elif objectHWName[objectListHW.index(v)] == "CameraZoneE":
                color = (255,255,255)
            elif objectHWName[objectListHW.index(v)] == "OvalTemplate":
                color = (255,0,255)
            elif objectHWName[objectListHW.index(v)] == "SignPillar":
                color = (255,255,255)
            elif objectHWName[objectListHW.index(v)] in ["PlankWipe0", "PlankCandy"]:
                color = (150,80,0)
            elif "SpikeBall" in objectHWName[objectListHW.index(v)]:
                color = (150,0,0)
            
            else:
                if debug:
                    print(objectHWName[objectListHW.index(v)])
                color = (255,0,255,100)
            
            x = v[0]
            y = v[1]
            w = v[2]
            h = v[3]
            r = v[4]

            r= radians(r) + pi/2
            # print(r)
            topL = (int(((w/2)*cos(r)-(h/2)*sin(r))*zoomV),int(((w/2)*sin(r)+(h/2)*cos(r))*zoomV))
            topR = (int(-((w/2)*cos(r)+(h/2)*sin(r))*zoomV),int(-((w/2)*sin(r)-(h/2)*cos(r))*zoomV))
            bottomL = (-1*topR[0], -1*topR[1])
            bottomR = (-1*topL[0], -1*topL[1])

            pygame.draw.lines(SCREEN,color,False, ((rec.center[0]+topR[0],rec.center[1]+topR[1]), (rec.center[0]+topL[0],rec.center[1]+topL[1]), (rec.center[0]+bottomL[0], rec.center[1]+bottomL[1]), (rec.center[0]+bottomR[0],rec.center[1]+bottomR[1]), (rec.center[0]+topR[0],rec.center[1]+topR[1]), (rec.center[0]+bottomL[0], rec.center[1]+bottomL[1])))



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
    # WaterShaper: Blue
    # 
    # DevPather: White # ???????
    # 
    # Others: white
                
                SCREEN.blit(vertex, [(v[0] + moveV[0])*zoomV - 1,(v[1] + moveV[1])*zoomV - 1])
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
                elif objectName[objectList.index(item)] == "frg.game.editor.objects::WaterShaper":
                    pygame.draw.line(SCREEN,pygame.color.Color(0,0,255,100),[int(zoomV*(vOG[0] + moveV[0])),int((vOG[1]+moveV[1])*zoomV)],[int((v[0] + moveV[0])*zoomV), int((v[1] + moveV[1])*zoomV)])
                elif objectName[objectList.index(item)] == "frg.game.editor.objects::FinishShaper":
                    pygame.draw.line(SCREEN,pygame.color.Color(0,255,0,100),[int(zoomV*(vOG[0] + moveV[0])),int((vOG[1]+moveV[1])*zoomV)],[int((v[0] + moveV[0])*zoomV), int((v[1] + moveV[1])*zoomV)])
                elif objectName[objectList.index(item)] == "frg.game.editor.objects::DevPather":
                    pygame.draw.line(SCREEN,pygame.color.Color(255,255,255),[int(zoomV*(vOG[0] + moveV[0])),int((vOG[1]+moveV[1])*zoomV)],[int((v[0] + moveV[0])*zoomV), int((v[1] + moveV[1])*zoomV)])
                elif objectName[objectList.index(item)] == "frg.game.editor.objects::BonesPather":
                    pygame.draw.line(SCREEN,pygame.color.Color(255,200,200),[int(zoomV*(vOG[0] + moveV[0])),int((vOG[1]+moveV[1])*zoomV)],[int((v[0] + moveV[0])*zoomV), int((v[1] + moveV[1])*zoomV)])
                else:
                    print(objectName[objectList.index(item)])
                    pygame.draw.line(SCREEN,pygame.color.Color(255,255,255,255),[int(zoomV*(vOG[0] + moveV[0])),int((vOG[1]+moveV[1])*zoomV)],[int((v[0] + moveV[0])*zoomV), int((v[1] + moveV[1])*zoomV)])
                vOG = v
        
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:
            moveV[0] -= 20 * (1/zoomV)
        elif keys[pygame.K_LEFT]:
            moveV[0] += 20 * (1/zoomV)
        if keys[pygame.K_UP]:
            moveV[1] += 20 * (1/zoomV)
        if keys[pygame.K_DOWN]:
            moveV[1] -= 20 * (1/zoomV)
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
                if event.key == pygame.K_t:
                    if showTriggers:
                        showTriggers = False
                    else:
                        showTriggers = True

                if event.key == pygame.K_c:
                    if showCheck:
                        showCheck = False
                    else:
                        showCheck = True
                if event.key == pygame.K_d:
                    if keys[pygame.K_LCTRL] or keys[pygame.K_RCTRL]:
                        if debug:
                            debug = False
                        else:
                            debug = True
                        continue
                    if showDecs:
                        showDecs = False
                    else:
                        showDecs = True
                if event.key == pygame.K_o:
                    if keys[pygame.K_LCTRL] or keys[pygame.K_RCTRL]:
                        restart = True
                        pygame.quit()
        if restart:
            break

        pygame.display.flip()
    if restart:
        __main__()
    # print()


__main__()