current_weather = int(input("What's the weather like today? (sunny/rainy/cold"))

if current_weather == "sunny":
    print("Wear a t-shirt and sunglasses.")
    if current_weather == "rainy":
        print("Don't forget your umbrella and a raincoat.")
        if current_weather == "cold":
            print("Make sure to wear a warm coat and a scarf.")
        else:
            print("Sorry, I don't have recommendations for this weather.")
                          
