#This is to run the Marvel Daily Challenge
# Goal is to finish all challenges and be rewarded the 25 crystals 

#start from home screen
click("1462760519675.png")
click(Pattern("1462893035991.png").similar(0.79))



#this loops runs 5 times to complete the missions
for x in range(0, 5):
    wait("1462893281759.png")
    
    click("1462893281759.png")
    while(not exists(Pattern("1462763144399.png").targetOffset(1,-5))):
        exists(Pattern("1462764604011.png").targetOffset(-2,-2))
                
    click(Pattern("1462764604011.png").targetOffset(-2,-2))
    if exists("1462807610868.png"):
        click("1462807632587.png")
    if exists("1462807769542.png"):
        click("1462807783700.png")

#exit mission stage select 
if exists("1462808254558.png"):
   click("1462809102142.png") 
   click(Pattern("1462808254558.png").targetOffset(-76,-1))
if exists("1462808310047.png"):
    click(Pattern("1462808310047.png").targetOffset(-117,0))
#should now be back at home screen 
#Daily Mission Clear x1 
click("1462760519675.png")
click("1462808985556.png")
click("1462809015305.png")
click("1462809122078.png")
while(not exists(Pattern("1462763144399.png").targetOffset(1,-5))):
        exists(Pattern("1462764604011.png").targetOffset(-2,-2))
        click(Pattern("1462764604011.png").targetOffset(-182,-5))
if exists("1462807610868.png"):
        click("1462807632587.png")

#should be back at home
#finish timeline daily challenge 
click("1462809835414-1.png")
click(Pattern("1462809973592-1.png").targetOffset(6,189))
wait("1462810042503-1.png")
click("1462810042503-1.png")
wait("1462810083650-1.png")
click("1462810083650-1.png")


for x in range (0,5):
    while(not exists("1462810111265-1.png")):
        exists("1462810111265-1.png") 
    click("1462810111265-1.png")
    while (not exists("1462810342528-1.png")):
        exists("1462810342528-1.png")  
    if exists("1462807610868-1.png"):
        click("1462807632587-1.png")
    if x == 5: 
        click(Pattern("1462810342528-1.png").targetOffset(-84,0))
    else: 
        click(Pattern("1462810342528-1.png").targetOffset(79,-5))
    








    
    
    
 
        
        
        
        
