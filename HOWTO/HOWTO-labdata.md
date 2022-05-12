# Labdata: DCCLab data repository

Archiving data is not only useful, it is essential for a serious laboratory. In order to ensure the sustainability of the data, we must agree to a standard to save our data on our disks (lab, personal, laptop, etc ...). With a simple nomenclature, anyone can access the data easily and we can archive it systematically. The server Cafeine2 is the main repository of the data produced by the group and to avoid total clutter, here is the nomenclature to follow.

**Note: this is not a recommendation, but a mandatory method for all group members. You must copy your data every day to labdata.**

Caffeine contains everyone's archives, in a folder that reads as follows:

`/ labdata / username / project / YYYYMMDD * /`

So: your username, the project name (only valid names, see below) and the date (Year, Month and Day) and then what you want. Here is an example:

! [Image 20190614114449466] (assets / labdata.png)

These data are accessible **universally** and **eternally,** **that is to say that once the data on caffeine, one cannot change their name or their location.** Consider this data as "data from laboratory notebooks ", so nothing should be deleted.

To do this, you must use the following structure and rules:

1. On all computers (laptop, desktop, lab), there must be a "**labdata**" directory (in lower case) in which all the data is saved. You can put it wherever you want.
2. Never use spaces in names. Try to use lowercase in your personal section.
3. The structure is then "the name" of the user **in lowercase letters** (for your laptops and personal computers, you can skip this step, but for laboratory computers, indicate your name). **You must use the same spelling all the time** See below for the number of projects.
4. Next, your projects, **in lower case letters**. Again, **you must use the same spelling all the time.** There are few projects in the group. There may already be one or more projects under your username, before creating a project, you must look below for project names.
5. Finally, when you do an experiment, or even an analysis, you must save in a folder whose name begins with the date in YYYYMMDD format then you can add whatever you want (such as: 20101029-WavelengthSwept_Test). You should avoid accents and /, if possible spaces (to avoid complicated URLs).
6. Then you can name your files and remake folders as it is appropriate for what you are doing.
7. Negotiable, but desirable: you should have a README.txt which indicates what the file contains.


Next, you need to "synchronize" your computers with cafeine if you keep your data on your computer. Note:

1. Synchronization should be done approximately once a day (before leaving in the evening or arriving in the morning).
2. Once this synchronization is done, you can no longer rename files in your labdata. If you want to do this, it must be done before synchronization.
3. There are tools to do this synchronization easily and quickly. rsync exists for Windows, macOS and Unix.

In your laboratory notebook, you can link to this data, which will end up on caffeine. You could write for example, "data in labdata at ws-cars / 20101029-Test /" without putting your name since your notebook belongs to you but you must put the project and the dated file.


# Labdata: DCCLab data repository

L'archivage des données n'est pas seulement utile, il est essentiel pour un laboratoire sérieux. Dans le but de s'assurer de la pérennité des données, nous devons avoir une convention pour sauvegarder nos données sur nos disques (laboratoire, personnel, portable, etc...). En ayant une nomenclature simple, n'importe qui pourra accéder aux données facilement et nous pourrons les archiver de façon systématique. Donc, Caféine aura la totalité des données qui proviendront des multiples ordinateurs du groupes, mais pour ce faire et éviter le fouilli total, voici la nomenclature à suivre.

**Notez: ce n'est pas une recommandation, mais bien une méthode obligatoire pour tous les membres du groupe. Vous devez copier vos données à chaque jour sur labdata.**



Caféine contient les archives de tous, dans un dossier qui se lit comme suit:

`/labdata/username/project/YYYYMMDD*/`

Donc: votre username, le nom du projets (seulement les noms valides, voir ci-dessous) et la date (Année, Mois et Jour) et ensuite ce que vous voulez. Voici un example:

![image-20190614114449466](assets/labdata.png)





Ces données sont accessibles **universellement** et **éternellement,** **c'est à dire qu'une fois les données sur caféine, on ne peut changer leur nom ou leur emplacement.** Considérez ces données comme "des données de cahiers de laboratoire", donc on n'efface rien.

Pour ce faire, vous devez utiliser la structure suivante:

1. Sur tous les ordinateurs (portable, desktop, labo), il doit y avoir un répertoire "**labdata**" (en minuscule) dans lequel toutes les données sont sauvegardées. Vous pouvez le mettre où vous voulez.
2. La structure est ensuite "le nom" de l'usager **en lettres minuscules** (pour vos portables et ordinateurs personnel, vous pouvez sauter cette etape, mais pour les ordinateurs de laboratoire, indiquez votre nom). **Vous devez utiliser le même orthographe tout le temps** Voir ci-dessous pour les nombns de projets.
3. Ensuite, vos projets, **en lettres minuscules**. Encore une fois, **vous devez utiliser le même orthographe tout le temps.** Il y a peu de projets dans le groupe. Il y a peut être déjà un ou des projets sous votre nom d'usager, avant de créer un projet, vous devez regarder sur [cette page du wiki ](http://cafeine.crulrg.ulaval.ca/groups/cote/wiki/7642b/Noms_et_projets_pour_larchivage_des_donnees.html)ou dans votre section sur caféine à [http://cafeine.crulrg.ulaval.ca/labdata/](http://cafeine.crulrg.ulaval.ca/labdata/(votrenom)/)
4. Finalement, lorsque vous faites une expériences, ou encore une analyse, vous devez sauvegarder dans un dossier dont le nom commence par la date en format YYYYMMDD ensuite vous pouvez ajouter ce que vous voulez (comme par exemple: 20101029-WavelengthSwept_Test). Vous devez éviter les accents et les /, si possible les espaces (pour éviter les URL compliqués).
5. Ensuite, vous pouvez nommer vos fichiers et refaire des dossiers comme il est approprié pour ce que vous faites.
6. Négociable, mais souhaitable: vous devriez avoir un README.txt qui indique ce que le dossier contient.



Ensuite, vous devez "synchroniser" vos ordinateurs avec caféine. Notez:

1. La synchronisation doit se faire environ une fois par jour (avant de partir le soir ou en arrivant le matin).
2. Une fois cette synchronisation faite, vous ne pouvez plus renommer de fichiers dans votre labdata. Si vous voulez le faire, cela doit être fait avant la synchronisation.
3. Il existe des outils pour faire cette synchronisation facilement et rapidement. rsync existe pour Windows, Mac OS X et Unix. **Une page WIki** [**sera créée**](http://cafeine.crulrg.ulaval.ca/groups/cote/wiki/8c93a/rsync_pour_tous.html) **pour expliquer l'installation de rsync pour chacune des plateformes [Volontaire SVP]**.

Dans votre cahier de laboratoire, vous pouvez faire un lien faire ces données, qui se retrouveront sur caféine. Vous pourriez écrire par exemple, "données dans labdata à ws-cars/20101029-Test/" sans mettre votre nom puisque votre cahier vous appartient mais vous devez mettre le projet et le dossier daté.



# Projets

| Nom de dossier | Description |
| ---- | ---- |
| 3d | Imagerie 3D grand volume (cakitegetse) |
| 6-color | Modification du microscope video pour donner 6-couleur en meme temps  |
| autofluo | Autofluorescence des tissus |
| axons | Projets utilisant les souris Thy1-YFP pour la caracterisation des axones |
| b-cars | Projet broadband CARS avec une source provenant du continuum (sbegin) |
| beautiful | Les belles images du groupe.  Vous pouvez recopier les votres dans ce repertoire |
| bone-ablation | Projet d'ablation des os avec les lasers amplifies |
| brainstem | Projet d'imagerie du brainstem avec David Kleinfeld |
| cam | Projet d'imagerie des CAM (Cellular Adhesion Molecules) dans les vaisseaux |
| cars | Imagerie CARS, test, initiatives personnelles, etc… GENERAL. |
| clearing | Tout projet impliquant l'imagerie avec les techniques de clearing |
| cs-cars | CARS correlation spectroscopie pour la detection de l'eau deutere |
| dbs | Projet de Deep Brain Stimulation avec les sondes fibrees (CARS, reflectance ou autre) |
| eae | Tous les projets de scleroses |
| fiber-probes | Fabrication ou caracterisation des sondes fibrees de tout genre |
| functional | Projets d'imagerie fonctionnel dans les animaux vivants |
| functional-uncaging | Projet d'imagerie dans les epines avec l'uncaging de molecules excitatrice |
| grintech | Projet avec l'endoscope de GRINTech (toute modalite) |
| hres-cars | Projet d'hyper-resolution CARS  |
| infiltration | Projet d'infiltration cellulaire dans la moelle epiniere en EAE (Steve Lacroix) |
| invivobeads | Projet de detection de billes fluorescentes magnetiques InVivo (Armen) |
| inflammation | Projet d'inflammation cellulaire dans la moelle epiniere en EAE |
| iphoton | Amelioration de iPhoton |
| lightsheet | Imagerie par lightsheet Bessel |
| microglia | Imagerie de la microglie dans la moelle (son infiltration) |
| microglialmotility | Imagerie dynamique de la microglie (son activite) |
| mneptune | Imagerie de mNeptune (proteine fluorescente rouge) |
| monocytes | Infiltration des monocytes dans la moelle epiniere |
| mri-gratio | Comparaison du g-ratio mesure par MRI et par CARS (Julien Cohen Adad) |
| oblique | Imagerie par illumination ou detection oblique (Jerome Mertz) |
| optogenetics |  |
| pd-cars | Polarization-dependent CARS |
| fixation-morphometry | Validation des protocoles de perfusion et leur effets sur la morphometrie de la myeline  |
| ppix | Fluorescence du PPIX en epilepsie |
| raman | Spectroscopie Raman spontanee |
| rfp | Red fluorescent protein comparison (Karen Lypka) |
| rms | Imagerie de Rostral Migratiory Stream (Armen Saghatelyan) |
| rotaryprobe | Imagerie par la sonde rotative panoramique |
| sciaticnerve | Imagerie des lesions du nerf sciatique par crusj injury |
| serotonin | Imagerie de la fluorescence de la serotonine |
| spinalcord | Imagerie generale de la moelle epiniere |
| sted | Imagerie par STED |
| suicide | Imagerie du corps calleux dans les cas de suicides et d'abus |
| summerschool | Neuropthonics SummerSchool |
| tf-dh |  |
| unassigned | Junk  |
| vasculature | Imagerie de la vasculature et de se permeabilite |
| vss | Voltage sensitive sensing |
| w-cars | Water-CARS, CARS de l'eau |
| window | Imagerie longitudinal de la moelle avec une fenetre spinale |
| ws-cars | Wavelength-swept CARS (sbegin) |
| zebrafish | Imagerie calcique du poisson zèbre |
