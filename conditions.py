import prompts

class Car:
    def __init__(self, driver):
        self.driver = driver
        self.speed = 0
        self.maxSpeed = 3
        self.isNotStarted = True
        self.carStarted = False
    
    def state(self):
        prompts.help()
        while self.isNotStarted is True:
            gameCommand = input("> ")

            if gameCommand.lower() == "help":
                prompts.help()
                prompts.space()

            elif gameCommand.lower() == "start":
                if self.carStarted is True:
                    prompts.started()
                    prompts.space()

                else:
                    self.carStarted = True
                    prompts.start()
                    prompts.space()

            elif gameCommand.lower() == "stop":
                if self.speed == 0:
                    if self.carStarted is False:
                        prompts.stopped()
                        prompts.space()

                    else:
                        prompts.stop()
                        self.carStarted = False
                        prompts.space()

                else:
                    prompts.moving()
                    prompts.space()

            elif gameCommand.lower() == "faster":
                if self.carStarted is False:
                    prompts.startReq()
                    prompts.space()

                else:
                    if self.speed < self.maxSpeed:
                        self.speed += 1
                        prompts.faster()
                        prompts.space()

                    else:
                        prompts.fastest()
                        prompts.ceil()
                        prompts.space()

            elif gameCommand.lower() == "slower":
                if self.carStarted is False:
                    prompts.startReq()
                    prompts.space()

                else:
                    if self.speed > 0:
                        prompts.slower()
                        self.speed -= 1
                        prompts.space()

                    else:
                        prompts.floor()
                        prompts.space()

            elif gameCommand.lower() == "quit":
                if self.carStarted is True:
                    prompts.quitReq()
                    prompts.space()

                else:
                    prompts.quit()
                    prompts.bye()
                    prompts.space()
                    break

            else:
                prompts.invalid()
                prompts.space()