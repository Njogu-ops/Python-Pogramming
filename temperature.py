from xml.sax.handler import property_interning_dict

temperature= float(input("Enter current room temperature :"))


if temperature > 25 :
    print("It is too hot")

elif temperature < 25 :
    print("It is too cold")
else:
    print("Normal Temperature")
