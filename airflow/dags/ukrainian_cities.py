def get_some_Ukrainian_cities():
    ukrainian_region_centers = [
        'Kyiv', 'Kostyantynivka', 'Kharkiv', 'Dnipro', 'Odesa', 'Lviv', 'Donetsk', 'Zaporizhzhia', 'Kryvyi Rih', 'Mykolaiv', 'Mariupol',
        'Luhansk', 'Makiivka', 'Vinnytsia', 'Simferopol', 'Kherson', 'Poltava', 'Chernihiv', 'Cherkasy', 'Sumy', 'Sevastopol',
        'Zhytomyr', 'Khmelnytskyi', 'Rivne', 'Ivano-Frankivsk', 'Kropyvnytskyi', 'Ternopil', 'Lutsk', 'Bila Tserkva',
        'Kramatorsk', 'Melitopol', 'Kerch', 'Kremenchuk', 'Uzhhorod', 'Chernivtsi','Melitopol'
    ]

    return ukrainian_region_centers

# Call the function to retrieve the list of Ukrainian region centers
list_ukrainian_cities = get_some_Ukrainian_cities()
print('Cities are defined')

if __name__ == "__main__":
    print(len(list_ukrainian_cities))
    # Print the list of Ukrainian region centers
    for city in list_ukrainian_cities:
        print(city)