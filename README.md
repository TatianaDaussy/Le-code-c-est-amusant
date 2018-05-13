Comment utiliser efficacement git :

Git est un versionneur de code, c'est à dire qu'il te permet de maintenir ton code à jour avec les gens avec lesquels tu travailles au cours d'un projet.

Les commandes utilises sont :

git clone <urlDuRepository>
- Cette commande te permet de récupérer le code sur un repo distant est au préalable créer et initialisé.

git add .
- Ajoute la totalité des fichiers que tu as modifié au prochain push que tu vas effectuer.

git commit -m "Message De Commit Explicatif"
- Permet d'ajouter un message explicatif pour tenir au courant tes comparses de ce que tu as modifié dans le code.

git push
- Pousse la totalité des modifications que tu as fait en local sur la branche distante

git pull
- Te permet de récupérer les modifications de tes comparses sur ta branche en local


Il est possible qu'avec votre binôme, vous ayez des soucis de merge ( fusion ) des modifications que vous avez tous les deux effectuées sur la branche distante.
Dans le cas de figure où la fusion automatique échoue, il vous faudra par vous même aller fusionner le fichier concerné, puis pull again.

git status
- Vous permet de connaître l'état de votre branche local par rapport à la branche distante.


---

Autre commande basique :

mkdir <NomDeDossier> : Te permet de créer un dossier
rm -rf <NomDeDossier> : Te permet de supprimer un dossier et son contenu, marche aussi avec les fichiers


Happy coding ! :)
