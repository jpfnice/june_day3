"""
Exercise 9:
    
Create a function that will give the possibility 
to obtain the translation of a french word in english

The function will use a small (6 or 7 pair of words) french/english dict

The function will check if the word exists or not, if it exists it will return its translation in English.
If it does not exist it will raise an exception

Note: you should be able to provide the french word using any case
"""

fr_en_dict={"Ciel":"Sky", 
            "Terre":"Earth", 
            "Ville":"City", 
            "Voiture":"Car", 
            "Rouge":"Red", 
            "Mer":"Sea"}

def translate(french):
    french=french.capitalize()
    if french in fr_en_dict:
        return fr_en_dict.get(french)
    else:
        raise Exception (f"{french} cannot be translated")
     
try:        
    fr=input("Enter a french word: ")
    print(f"The translation of {fr} is {translate(fr)}")
except Exception as ex:
    print(ex)


