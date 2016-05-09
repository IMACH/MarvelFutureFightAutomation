missionRunning = False 
click("1462760519675.png")
click(Pattern("1462806289444.png").similar(0.74))



for x in range(20):
    while(not exists(Pattern("1462765029872.png").similar(0.80))):
        click("1462760893884.png")
        while(not exists(Pattern("1462763144399.png").targetOffset(1,-5))):
            missionRunning = True 
            exists(Pattern("1462764604011.png").targetOffset(-2,-2))
            missionRunning = False
        click(Pattern("1462764604011.png").targetOffset(-2,-2))
        if exists(Pattern("1462765029872.png").similar(0.80)):
            click(Pattern("1462769658093.png").exact())
    x += 1
            

    
    



















