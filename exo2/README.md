Usage :

`python3 exo1.py`

Run test :

`python3 test_exo1.py`



Imaginez comment modifier votre algorithme, si au lieu de vouloir trouver le jour de lasemaine le moins fréquenté, vous aviez pour mission de trouver les K dates les plusfréquentés (avec K très grand). Donnez la complexité algorithmique de votre solution,et donnez une justification quant à son efficacité.

J'appliquerais un tri par fusion (https://fr.wikipedia.org/wiki/Tri_fusion) sur ma liste de date/nombre de visiteurs. Cet algorithme a une complexité de n log n. Cet algorithme offre un temps d'exécution correct dans le pire comme dans le meilleur des cas. Ensuite je ne retournerais que les K premier élément.
