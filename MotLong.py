phrase = "";

def trouver_le_gros_mot(phrase):
    mots = phrase.split();

    plus_gros_mot = "";
    nb_de_char = 0;

    for mot in mots:
        if len(mot) > nb_de_char:
            plus_gros_mot = mot;
            nb_de_char = len(mot);

    print(f"'{plus_gros_mot}' contient {nb_de_char} characteres.");

while phrase == "":
    phrase = input("Entrez la phrase: ");
    if phrase == "":
        print("\n\nVeuillez entrez une phrase.");
    else:
        trouver_le_gros_mot(phrase);
        break;


