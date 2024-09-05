#project-->online vegetable/fruits website
#language used-->python
#Made by-->Amritansh Khatri

vegetable=['tomato','potato','ladyfinger','reddish','carrot','apples','mangoes','graphes','cherry','banana','strawberries']

while True:
    print("Welcome to online vegetable/fruits shop  press 'yes' to buy vegetable 'No' for exit")
    
    order_box={}
    
    def vegetables():
    
        print("\nThe vegetables list is",vegetable)
        
        much=int(input("\nEnter how many vegetable you want to buy = "))
            
        if(much==1):
            buy=input("Enter the  item to buy = ")
                    
            quantity=input("Enter the  quantity in kg = ")
                    
            order_box['Item1']=buy
                    
            order_box['quantity']=quantity
                    
            print("Item added to cart")
                    
            print(order_box)
            
            print("Your order will be at your door step soon..........")
        elif(much==2):
            buy=input("\nEnter the  item to buy = ")
                    
            quantity=input("\nEnter the quantity in kg  = ")
                    
            order_box['Item1']=buy
                    
            order_box['quantity1']=quantity
                    
            yub=input("\nEnter the item to buy  = ")
                    
            ytitnauq=input("\nEnter  the quantity in kg  = ")
                    
            order_box['Item2']=yub
                    
            order_box['quantity2']=ytitnauq
                    
            print("\nBoth the  items are added in order cart")
                    
            print(order_box)
            
            print("\nYour order will be at your door step soon..........")
    
    choice=input("\nEnter your choice = ").strip().lower()
    
    if(choice=="yes"):
                print("\n*Select the location from where you want to buy vegetables")
                
                print("1.dehradun")
                
                print("2.delhi")
                
                print("3.Punjab")
                
                a=int(input("\n*select from(1-3) the location = "))
                
                if(a==1):
                        print("\nThe location in dehradun where we deliver our vegetables")
                    
                        print("1.Clement town")
                    
                        print("2.ISBT")
                    
                        print("3.Race course")
                    
                        b=int(input("\nEnter the selection = "))
                    
                        if(b==1):
                            vegetables()
                    
                        elif(b==2):
                            vegetables()
                    
                        elif(b==3):
                            vegetables()        
                elif(a==2):
                        print("\nThe location in delhi where we deliver  our vegetables")
                        
                        print("1.Connaught Place")
                        
                        print("2.South Extension")
                        
                        print("3.Dwarka ")
                        
                        b=int(input("\nEnter the selection = "))
                        
                        if(b==1):
                            vegetables()
                        
                        elif(b==2):
                            vegetables()
                        
                        elif(b==3):
                            vegetables()              
                elif(a==3):
                        print("\nThe locations in Punjab where we deliver our vegetables:")
                        
                        print("1. Chandigarh")
                        
                        print("2. Amritsar")
                        
                        print("3. Ludhiana")
                        
                        b=int(input("\nEnter the selection = "))
                        if(b==1):
                            vegetables() 
                        
                        elif(b==2):
                            vegetables()    
                        
                        elif(b==3):
                            vegetables()                     
                elif(a==4):
                        print("\nThe locations in Haryana where we deliver our vegetables:")
                        
                        print("1. Gurgaon (Gurugram)")
                        
                        print("2. Faridabad")
                        
                        print("3. Ambala")
                        
                        
                        b=int(input("\nEnter the selection = "))
                        if(b==1):
                            vegetables()
                        
                        elif(b==2):
                            vegetables()
                        
                        elif(b==3):
                            vegetables()
                elif(a==5):
                        print("\nThe locations in Rajasthan where we deliver our vegetables:")
                        
                        print("1. Jaipur")
                        
                        print("2. Udaipur")
                        
                        print("3. Jodhpur")
    
                        b=int(input("\nEnter the selection = "))
                        if(b==1):
                            vegetables()   
                    
                        elif(b==2):
                            vegetables()
                        
                        elif(b==3):
                            vegetables()    
                        break
    else:
        print("\nThanks ! visit again")
