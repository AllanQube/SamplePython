def trafficLights():
    light=input("Enter the traffic color: ").lower()
    if(light=="red"):
        print("Stop")
    elif(light=="yellow"):
        print("Wait")
    elif(light=="green"):
        print("Go")
        
    else:
        print("Plese Enter Red, Yellow or Green traffic light")
    

trafficLights()
