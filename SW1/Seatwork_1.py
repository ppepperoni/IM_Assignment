while True:
    print("Enter dollar ($) (* to exit): ")
    dollar = input()
    
    if dollar == '*':
        print("Bye")
        break
    
    def convert(x):
        rupees = x * 88.15
        pound = x * 0.74
        yuan = x * 7.12
        return (rupees, pound, yuan)
    
    dollarList = dollar.split('@')
    dollarTuple = tuple(int(elements) for elements in dollarList)
    
    print(f"{'Dollar($)':<10} {'Indian Rupee(R)':<20} {'British(£)':<20} {'China (Y)':<20}")
    
    for i in dollarTuple:
        converted = convert(i)
        print(f"{i:<10} {converted[0]:<20.2f} {converted[1]:<20.2f} {converted[2]:<20.2f}")
        