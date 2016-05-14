running = True
click("1462760519675.png")
click("1462895329907.png")



while (running):
    while(not exists(Pattern("1462765029872.png").similar(0.80))):
        click(Pattern("1462760893884.png").similar(0.56))
        while(not exists(Pattern("1462763144399.png").targetOffset(1,-5))):
            missionRunning = True 
            exists(Pattern("1462764604011.png").targetOffset(-2,-2))
            missionRunning = False
        click(Pattern("1462764604011.png").targetOffset(-2,-2))
        if exists(Pattern("1462765029872.png").similar(0.80)):
            click(Pattern("1462769658093.png").similar(0.75))
        if exists("1462896497006.png"):
            click("1462896529590.png")
            
            

    if exists(Pattern("1462765029872.png").similar(0.80)):
        click(Pattern("1462769658093.png").similar(0.75))

            

    
    



















