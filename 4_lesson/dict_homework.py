#Work with dictionaries
dct = {
    "Name": "Max",
    "Surname": "Verstappen",
    "Age": 28,
    "Sport": "F1",
    "Team": "Red Bull Racing"
}
print(f"Dictionary, task1 {dct}")

#Update dictionary
Books = {
    "Name": ["The Shining", "The Murder on the Orient Express"],
    "Author": ["Stephen King", "Agatha Christie"]
}
Books["Name"].append("The Café on the Edge of the World")
Books["Author"].append("John P. Streleki")
print(f"Updated list of books: {Books}")

#Value search
Countries = {
    "United Kingdom": "London",
    "France": "Paris",
    "Germany": "Berlin",
}
input_country = input("Enter country: ")
print(Countries[input_country])