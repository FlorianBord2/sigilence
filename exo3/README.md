1. Donnez les caractéristiques attendues pour la banque d'images.

La banque d'image doit dans l'ideal couvrir toute les possibiliters de formes et de couleur de bagage. D'angles de vue et de luminositer. Au vue de l'objectif final du modele il me sembble important que la banque d'image couvre aussi les cas ou le bagage n'est pas entiérement visible ( bagage sous un banc, derrier une poubel ...)

2. Comment constituer un tel jeu de données ?

Une première solution serait de récupérer sur les sites vendeur de bagages les photos de promotion, a l'aide d'un robot. Ensuite on peut se tourner vers les aéroports. Peut être ont il déjà des caméras qui filment les bagages en soute lors de leurs passage sur les tapis roulant. L'idéal serait de récupérer des vidéosurveillance de gare et d'aéroport et de labelliser les bagages des voyages en train d'attendre. Ce cas étant celui qui se rapproche le plus de l'application final du modèle, il me semble être le plus pertinent bien qu'il soulève des questions sur le droit d'accéder et d'utiliser de telles images.

3. Dans le cas où la banque d'images est incomplète, quelles sont les possibilitéstechniques pour y remédier ?

On peut alors appliquer des algorithmes d'augmentation sur les images déjà en notre possession. Cela consiste à créer de nouvelles versions de nos images modifiées. Par exemple en changent l'inclinaison de l'image, en la deforment ou en applicant des filtre de couleur ou des filtre offuscant certaine partie de l'image. Cela permet de soumettre plus de cas à notre modèle.

4. Écrire en C++ la structure du code d'une application permettant l'augmentation d'unebanque d'images. Cela inclut classes, fonctions, algorithmes de haut niveau. Il n'estpas demandé une implémentation complète, mais un code qui compile.

Voilà différents outils qui permettent d'augmenter une banque d'image.
https://github.com/albumentations-team/albumentations

https://github.com/takmin/DataAugmentation

https://github.com/aleju/imgaug#installation