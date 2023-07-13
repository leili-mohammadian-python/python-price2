number=int(input("enter number to seconds:"))
##if number>3600:
hour=number//3600
minute=(number%3600)//60
second=(number%3600)%60    
print("hour:",hour,"minute:",minute,"second:",second)