RawFruitsDict ={
  "apple" : 130 , "banana" : 110 ,
  "grapefruit" : 60 , "honeydewmelon" : 50 ,
  "lemon" : 15 , "nectarine" : 60 ,
  "peach" : 60 , "pineapple" : 50 ,
  "avocado" : 50 , "kiwifruit" : 90 ,
  "pear" : 100 , "sweet cherries" : 100 ,
  "grapes" : 90 , "lime" : 20 ,
  "cantaloupe" : 50 , "orange" : 80 
}
item = input("Item: ").lower()
if item in RawFruitsDict:
    print("Calories:" , RawFruitsDict[item])

