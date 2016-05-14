#testing script 
#finish timeline daily challenge 
click("1462809835414.png")
click(Pattern("1462809973592.png").targetOffset(6,189))
wait("1462810042503.png")
click("1462810042503.png")
wait(Pattern("1462838903822.png").similar(0.83))

click("1462810083650.png")


for x in range (0,5):
    while(not exists("1462810111265-1.png")):
        exists("1462810111265-1.png") 
    click("1462810111265-1.png")
    while (not exists("1462810342528.png")):
        exists("1462810342528.png")  
    if exists("1462807610868.png"):
        click("1462807632587.png")
    if exists(Pattern("1462839078921.png").exact()): 
        click(Pattern("1462810342528.png").targetOffset(-84,0))
    else: 
        click(Pattern("1462810342528.png").targetOffset(79,-5))

if exists("1462807610868.png"):
    click("1462807632587.png")
    