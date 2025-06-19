# References

ingredients = ["flour", "yeast", "salt"] # list

# dictionary
barm_cake = {
    "name": "Barm Cake", # key: name, value: "Barm Cake"
    "ingredients": ingredients # store the REFERENCE to ingredients
}

roll = {
    "name": "Roll",
    "ingredients": ingredients # store the REFERENCE to ingredients
}

barm_cake["ingredients"].append("water")

print(barm_cake["ingredients"] == roll["ingredients"])

print(barm_cake['ingredients'] is roll["ingredients"])

# various_ingredients = [ingredients] # ["salt", "water", "whatver"] OR the REFERENCE

