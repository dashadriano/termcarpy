import prompts
import conditions

outsideCar = True
prompts.space()
prompts.greeting()
prompts.help()
name = prompts.askName() 

while outsideCar is True:
    if len(name) < 1:
        prompts.space()
        prompts.invalidName()
        prompts.space()
        name = prompts.secondAskName() 
        prompts.space()

    else:
        if name.lower() == "start":
            prompts.space()
            prompts.firstStartReq()
            name = prompts.secondAskName() 
            prompts.space()

        elif name.lower() == "stop":
            prompts.space()
            prompts.stopReq()
            name = prompts.secondAskName() 
            prompts.space()

        elif name.lower() == "faster":
            prompts.space()
            prompts.startReq()
            prompts.firstStartReq()
            name = prompts.secondAskName() 
            prompts.space()

        elif name.lower() == "slower":
            prompts.space()
            prompts.stopReq()
            name = prompts.secondAskName()
            prompts.space()


        elif name.lower() == "quit":
            prompts.space()
            wannaQuit = prompts.firstQuitReq()
            prompts.space()
            if wannaQuit.lower() == "y":
                prompts.bye()
                prompts.quit()
                prompts.space()
                break

            elif wannaQuit.lower() == "n":
                prompts.assurance()
                name = prompts.secondAskName()
                prompts.space()
            
            else:
                prompts.invalid()
                prompts.space()

        elif name.lower() == "help":
            prompts.space()
            wantHelp = prompts.needHelp() 
            prompts.space()
            if wantHelp.lower() == "y":
                prompts.help()
                name = prompts.secondAskName()
                prompts.space()

            elif wantHelp.lower() == "n":
                prompts.space()
                prompts.assurance()
                name = prompts.secondAskName()
                prompts.space()
        
            else:
                prompts.invalid()
                prompts.space()

        else:
            car = conditions.Car(name)
            outsideCar = False

else:
    prompts.space()
    prompts.welcome(name)
    prompts.space()
    car.state()