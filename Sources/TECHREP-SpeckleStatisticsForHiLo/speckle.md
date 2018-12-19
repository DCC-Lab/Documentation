# ![image](fig/logo.png)

# Statistiques des speckles

[**Quentin Perry-Auger
([quentin.perry-auger.1@ulaval.ca](quentin.perry-auger.1@ulaval.ca))**]

Stagiaire CERVO
Été 2018

**Résumé**
==========

Cet ouvrage résume les différents aspects des statistiques des speckles.
Les statistiques de premier ordre (en un seul point) sont d’abord
étudiées pour l’amplitude, l’intensité et la phase. Les statistiques de
deuxième ordre (en deux points) sont également abordées afin de trouver
la taille approximative des speckles dans les différents axes de
l’espace. Ensuite, l’intensité intégrée est abordée. Le concept de
speckles contraints, qui s’applique aux fibres optiques, est introduit
et les caractéristiques des speckles observés à la sortie d’une fibre
optique multimode sont détaillés. Enfin, une discussion sur les
différents facteurs qui permettent de modifier le contraste d’un
ensemble de speckles est présentée.

Somme de champs phaseurs
========================

Les speckles sont le résultat d’une somme de phaseurs de phase et/ou
d’amplitude aléatoires. On peut donc écrire le champ électrique
résultant en un point de l’ensemble de speckles de la façon suivante:

$$
A e^{j\theta} = \frac{1}{\sqrt{N}}\sum_{n=1}^{N}a_{n}e^{j\phi_{n}} \label{eq1}
$$

où le facteur 1/$\sqrt{N}$ est introduit afin d’avoir un moment de
second ordre fini lorsque le nombre de phaseurs $N$ de la somme tend
vers l’infini. À partir de cette équation, on pose trois conditions sur
les phaseurs sommés: $\ref{eq1}$

1.  Les amplitudes et les phases de deux phaseurs sont statistiquement
    indépendantes

2.  L’amplitude de tout phaseur est indépendante de sa phase et
    vice-versa

3.  Les phases sont distribuées uniformément sur l’intervalle \[-$\pi$,
    $\pi$\]

Dans le cas où le nombre de phaseurs N tend vers l’infini (pour une
discussion où ce n’est pas le cas, voir les sections 2.5 et 3.2.3 de
[@Manuel]), après avoir utilisé le théorème central limite et effectué
quelques manipulations mathématiques, on trouve que la fonction de
densité de probabilités (FDP) de l’amplitude du champ résultant est de
forme gaussienne:
$$
\label{Eq:FDPAmp}
P_{A}(A) = \frac{A}{\sigma^2}\exp\left(\frac{-A^2}{2\sigma^2}\right)
$$

De plus, il peut être pertinent de mentionner que d’additionner
plusieurs sommes de phaseurs ne changent pas la forme l’équation
\[Eq:SomPhas\].\

Statistiques de premier ordre {#Sec:PremierOrdre}
=============================

À partir de l’équation $\ref{Eq:FDPAmp}$ et de la relation entre l’intensité
et l’amplitude ($I=A^2$), on peut obtenir la FDP de l’intensité en un
point de l’ensemble de speckles,

$$
\label{Eq:FDPInt}
​    P_{I}(I) = \frac{1}{\overline{I}}\exp(-I/\overline{I}),
$$

et celle de la phase

$$
\label{Eq:FDPPhase}
​    P_{\theta}(\theta) = \frac{1}{2\pi}.
$$

Le résultat de l’équation \[Eq:FDPPhase\] n’est pas surprenant puisque
la distribution de la phase a été considérée comme uniforme (pour une
discussion où ce n’est pas le cas, voir la section 2.6 de [@Manuel]).
Les speckles ayant une FDP d’intensité de cette forme sont dits
complètement développés (fully-developed speckles).\

Contraste et SNR
================

Le contraste est défini comme étant la variance sur la moyenne d’une
distribution. Dans le cas des speckles, il est donc donné par

$$
C = \frac{\sigma_I}{\overline{I}}.
$$

Ce concept est important pour la microscopie HiLo puisque c’est en
calculant celui-ci sur la différence d’images
($I_{uniforme}-I_{speckle}$) que l’on peut extraire les basses
fréquences spatiales contenues au plan focal. On introduit également le
“signal to noise ratio” (SNR) qui est égal à l’inverse du contraste:

$$
SNR = \frac{1}{C} = \frac{\overline{I}}{\sigma_I}.
$$

Plusieurs facteurs peuvent influencer le contraste. Par exemple, lorsque
N ensembles indépendants de speckles sont superposés, le contraste
diminue jusqu’à un minimum de 1/$\sqrt{N}$ lorsque tous les ensembles
ont une intensité moyenne égale. Ainsi, si on voulait augmenter le
contraste des speckles à la sortie d’une fibre multimode, on pourrait y
placer un polariseur pour ainsi passer de deux ensembles indépendants
(un pour chaque composante de la polarisation) à un seul. Aussi, un
ensemble de speckles complètement polarisé a un contraste plus élevé
qu’un ensemble partiellement polarisé (pour un minimum de 1/$\sqrt{2}$
lorsque l’ensemble n’est pas du tout polarisé). Il est à noter que, dans
ces deux cas, la FDP de l’intensité n’est plus une fonction
exponentielle décroissante. Ces cas sont traités plus en détail au
chapitre 3 de [@Manuel]. Les autres facteurs qui influencent le
contraste sont détaillés à la section \[Sec:Reduction\] de cet ouvrage.\

Statistiques de deuxième ordre {#méthodes_expérimentales}
==============================

Il est possible de trouver les FDP jointes en deux points (dans l’espace
ou dans le temps) d’un ensemble de speckles. Toutefois, celles-ci étant
bien détaillées à la section 4.3 de [@Manuel], elles ne seront pas
énumérées ici. Nous nous intéressons plutôt aux dimensions des speckles
dans l’espace, à commencer par celles dans le plan transverse. En
assumant une propagation paraxiale et un ensemble de speckles formé par
une surface non-uniforme à l’ordre de la longueur d’onde de la lumière
(un diffuseur, par exemple), on obtient l’aire d’un speckle en intégrant
le carré du coefficient de corrélation transverse complexe qui
représente la fonction d’autocorrélation de l’amplitude normalisée
([@Manuel], p. 75). Celui-ci est égal à:

$$
\label{Eq:CoeffCorrel}
​    \mu_{A}(\Delta x, \Delta y) = \frac{\Gamma_{A}(\Delta x, \Delta y)}{\Gamma_{A}(0,0)} = \frac{\int\int_{-\infty}^{\infty}I(\alpha, \beta)e^{-j\frac{2\pi}{\lambda z}(\alpha \Delta x + \beta \Delta y)}\text{d}\alpha\text{d}\beta}{\int\int_{-\infty}^{\infty}I(\alpha, \beta)\text{d}\alpha\text{d}\beta}
$$

où $I(\alpha, \beta)$ est l’illumination sur la surface diffusante et
$x$ et $y$ sont les coordonnées sur le plan de speckles. Ce coefficient
est obtenu à partir de l’équation de diffraction de Fresnel, donc
l’équation \[Eq:CoeffCorrel\] est valide pour le champ proche comme pour
le champ lointain. Pour une surface de diffusion circulaire ou
rectangulaire d’aire A, on obtient que l’aire d’un speckle est environ
donnée par

$$
A_{s} = \frac{(\lambda z)^2}{A}
$$

où $\lambda$ est la longueur d’onde et $z$ est la distance axiale.

De façon plus générale, l’aire transverse d’un speckle est donnée par

$$
A_{s} = \frac{(\lambda z)^{2}\int\int_{-\infty}^{\infty}I^{2}(\text{x,y})\text{dxdy}}{\left[\int\int_{-\infty}^{\infty}I(\text{x,y})\text{dxdy}\right]^2}
$$

Pour ce qui est de la longueur des speckles dans la direction axiale
(profondeur), celle-ci est définie dans [@Manuel] comme étant la largeur
à mi-hauteur du coefficient de corrélation axial normalisé et est égal à
$6,7\lambda(z/D)^2$ pour une surface circulaire de diamètre $D$ et à
$4,8\lambda(z/L)^2$ pour une surface carrée de côté L. On remarque donc
que la longueur d’un speckle dans la direction axiale est bien plus
grande (elle varie en fonction de $z^2$) que les dimensions dans le plan
transverse (où l’aire varie en fonction de $z^2$, donc les dimensions
varient en fonction de $z$).\

Intensité intégrée
==================

Dans plusieurs applications, l’intensité n’est pas mesurée directement,
mais est plutôt intégrée, que ce soit dans l’espace pour la microscopie
HiLo ou dans le temps par un détecteur. Ainsi, on s’intéresse à la FDP
de l’intensité une fois intégrée, que nous dénotons W. En approximant le
profil d’intensité des speckles comme des boîtes rectangulaires, on
obtient la forme approximative de la FDP ([@Manuel], p. 112):

$$
\label{Eq:IntIntUn}
​    P(W) = \frac{(M/\overline{W})^{M}W^{M-1}\exp(-MW/\overline{W})}{\Gamma(M)}
$$

où $M$ est le nombre de degrés de liberté et est environ égale au
rapport entre l’aire sur laquelle on intègre et l’aire approximative
d’un speckle. La FDP de l’équation \[Eq:IntIntUn\] est appelée
distribution gamma. On remarque que lorsqu’on intègre sur seulement un
speckle ($M\approx1$), la FDP devient une exponentielle décroissante
comme pour un point d’un ensemble complètement développé.

Dans le cas des fibres optiques - speckles contraints {#Sec:SpeckCons}
-----------------------------------------------------

Dans le cas d’une fibre optique, lorsque l’aire d’intégration $A_i$ est
faible par rapport à l’aire totale du coeur de la fibre $A_c$ (ou encore
le rapport entre le nombre de speckles N dans l’aire d’intégration et le
nombre total de speckles N$_T$ sur une section du coeur de la fibre est
faible), la distribution de l’intensité intégrée semble concorder avec
la distribution gamma. Toutefois, les expériences montrent que les
probabilités s’éloignent de ce type de distribution lorsque le rapport

$$
\kappa = A_{i}/A_{c} = N/N_{T}
$$

s’approche de l’unité. Une nouvelle formule plus représentative du
comportement observé a été proposée par Goodman. Certaines suppositions
sont toutefois nécessaires ([@Manuel], p. 240):\

1.  Tout le volume modal de la fibre est rempli (donc tous les modes
    possibles dans la fibre sont excités)

2.  Le nombre de modes se propageant dans la fibre est très grand

3.  La distribution des speckles dans le coeur de la fibre est
    spatialement stationnaire et aléatoire, ce qui est, d’après Goodman,
    une bonne approximation pour les fibres à saut d’indice, mais moins
    pour une fibre à gradient d’indice

4.  Le nombre de speckles est égal au nombre de modes se propageant dans
    la fibre, ce qui est une bonne approximation si tous les modes
    véhiculent la même puissance (à nouveau, ceci est une bonne
    approximation pour les fibres à saut d’indice, mais moins pour une
    fibre à gradient d’indice)

Lorsque ces conditions sont remplies, la FDP en un point de la surface
du coeur de la fibre a une forme exponentielle décroissante. La méthode
proposée par Goodman pour trouver la nouvelle FDP est d’appliquer une
contrainte à celle-ci, soit que la puissance totale $W_T$ est constante
le long du coeur de la fibre. On cherche donc la FDP conditionnelle
$P(W|W_T)​$ qui est obtenue à partir de l’équation \[Eq:IntIntUn\] et de
la loi de Bayes:

$$
P(W|W_T) = \frac{1}{W_T}\left(\frac{W}{W_T}\right)^{\kappa N_{T}-1}\left(1-\frac{W}{W_T}\right)^{(1-\kappa)N_{T}-1}\frac{\Gamma(N_{T})}{\Gamma(\kappa N_{T})\Gamma((1-\kappa)N_{T})}
$$

Speckles à la sortie d’une fibre multimode
==========================================

Dans une fibre multimode, la plus petite taille possible pour un speckle
peut être trouvée en ne considérant que deux modes: un mode d’ordre très
élevé et le mode d’ordre le plus bas [@FiberStats]. La taille minimale
d’un speckle correspond alors à la taille d’une frange du patron
d’interférence résultant à la surface de la fibre:

$$
\Delta x = \lambda/(2\text{NA})
$$

On trouves alors le nombre de speckles approximatif à la surface du
coeur de rayon $a$ de la fibre:

$$
N = \pi\left(\frac{2a\text{NA}}{\lambda}\right)^2
$$

On remarque donc que l’approximation mentionnée à la section
\[Sec:SpeckCons\] qui stipule que le nombre de speckles est égal au
nombre de modes est assez bonne pour une fibre a saut d’indice
considérant qu’une telle fibre contient environ
$2(\pi a\text{NA}/\lambda)^2$ modes. On en conclut également qu’une
fibre à saut d’indice aura des speckles plus fins et en plus grand
nombre qu’une fibre à gradient d’indice qui contient deux fois moins de
modes.

Speckles dans le champ proche (Fresnel)
---------------------------------------

À la sortie immédiate de la fibre, si on intègre l’intensité sur une
faible portion du coeur, puisque les speckles résultent d’un grand
nombre de modes dont les phases sont aléatoires, la FDP devrait être
près d’une exponentielle décroissante. Ceci semble également concorder
avec les résultats obtenus lors de la mesure du signal to noise ratio
(SNR) dans [@Constrained]. Théoriquement, puisque la distribution est la
même que celle obtenue par un diffuseur et que c’est la méthode utilisée
par la plupart des microscopes HiLo, en imageant le bout de la fibre sur
l’échantillon, l’imagerie serait possible. Toutefois, dans ce cas, le
laser ne serait pas collimé et la taille des speckles changerait avec la
distance et l’illumination ne serait pas uniforme (au niveau de la
symétrie générale, évidemment, puisqu’une illumination avec speckles
n’est pas uniforme).

Speckles dans le champ lointain (Fraunhoffer)
---------------------------------------------

Dans le champ lointain, la distribution spatiale de l’ensemble de
speckles cesse de varier avec la distance ([@Commerce], p. 1). On
obtient donc une illumination symétrique. Pour ce qui est des
statistiques de cette distribution, celles-ci sont peu documentées
explicitement. Toutefois, on remarque que l’ensemble de speckles au
champ lointain ressemble énormément à celui au champ proche
([@FiberStats], Fig. 1 a). Les résultats de la FDP de l’intensité en
régime de Fraunhoffer pour une courte fibre optique à saut d’indice
semble également se rapprocher de la distribution exponentielle négative
([@FiberStats], Fig. 5 a) et celle-ci s’éloigne peu de cette forme même
en augmentant la longueur de la fibre (la FDP s’applatit toutefois
légèrement). Ceci semble avoir du sens, puisque la distribution spatiale
du champ électrique à la sortie de la fibre est aléatoire si le nombre
de modes est élevé, donc le champ lointain, qui est la somme de toutes
ces contributions aléatoires, devrait également l’être.\

Réduction de speckles (paramètres qui affectent le contraste) {#Sec:Reduction}
=============================================================

Contrôler le contraste du patron de speckles est important en
microscopie HiLo, puisqu’un meilleur contraste permet d’avoir des
mesures plus précises lors de l’application de l’algorithme HiLo. Tel
que mentionné plus tôt, des paramètres comme le nombre d’ensembles de
speckles indépendants ou encore la polarisation affectent le contraste.
Toutefois, plusieurs autres paramètres influencent celui-ci, dont
certains sont propres aux fibres optiques.

Moyennage temporel
------------------

Si le patron de speckles fluctue dans le temps à une fréquence très
élevée en comparaison avec le temps d’intégration de la caméra, la
distribution spatiale est moyennée et on obtient une illumination
uniforme. Ceci peut être effectué en faisant vibrer la fibre optique
assez rapidement. Il est également possible d’augmenter cet effet en
ajoutant un diffuseur à la sortie de la fibre au prix d’une perte de
puissance envoyée sur l’échantillon puisqu’il y a alors plus de
divergence ([@Manuel], section 5.2).

Longueur de la fibre
--------------------

Tout d’abord, en allongeant la fibre, les modes d’ordre supérieur
interfèrent de plus en plus avec les modes d’ordre inférieur, ce qui
tend à diminuer le contraste des speckles ([@FiberStats], Fig. 6).
Aussi, si la longueur de la fibre est assez importante, les modes
peuvent cesser d’interférer puisque la différence de chemin optique
entre ceux-ci peut dépasser la longueur de cohérence de la source. La
longueur critique où les rayons parallèles à l’axe optique et les rayons
incidents à l’angle critique cessent d’interférer dans une fibre à saut
d’indice est [@Coherence]

$$
L_{c} = \frac{c n_{2} t_{c}}{n_{1}(n_{1} - n_{2})}
$$

où $t_c$ est le temps de cohérence de la source.

Largeur du spectre de la source
-------------------------------

Puisque la largeur du spectre de la source est inversement
proportionnelle à son temps de cohérence [@Coherence], augmenter la
largeur du spectre diminue rapidement la longueur critique à laquelle
les modes cessent d’interférer.

Courbures dans la fibre optique
-------------------------------

Une fibre entortillée a un contraste plus faible qu’une fibre droite. Le
contraste diminue jusqu’à atteindre un plateau où une redistribution
stable des modes est atteinte ([@FiberStats], Fig. 8).

Diversité angulaire
-------------------

Une réduction du contraste peut également être obtenue avec de la
diversité angulaire. Dans [@Angular], ceci est effectué en envoyant
plusieurs faisceaux à différents angles d’incidence sur un diffuseur à
l’entrée de la fibre.

Annexe I - Termes et concepts de probabilités et statistiques {#AnnexeI .unnumbered}
=============================================================

NB: Dans cette annexe, la notation $E[X]$ est utilisée pour dénoter la
moyenne plutôt que $\overline{X}$.

-   **Espérance (expected value, mean)**: valeur moyenne qu’on s’attend
    à retrouver si on répète l’expérience un grand nombre de fois.

    $$
    E[X] = \int_{-\infty}^{\infty}X P(x) dx
    $$

    P(x): densité de probabilité\

-   **Écart-type (standard deviation)**: mesure de l’écart entre les
    valeurs et la moyenne (mesure de la dispersion d’un échantillon).

    $$
    \sigma_X = \left(E[(X - E[X])^2]\right)^{1/2} = \left(E[X^2]-E[X]^2\right)^{1/2}
    $$

-   **Variance**: carré de l’écart-type, donc mesure de la dispersion
    également.\

-   **Covariance**: variance conjointe entre deux variables. Elle prend
    des grandes valeurs si les écarts des variables correspondent.

    $$
    cov(X,Y) = E[(X-E[X])(Y-E[Y])]
    $$

-   **Corrélation**: Indication du degré de dépendance entre deux
    variables aléatoires.

    $$
    corr(X,Y) = \frac{cov(X,Y)}{\sigma_{X}\sigma_{Y}}
    $$

-   **Autocorrélation**: corrélation d’une variable avec elle-même
    (décalée d’un certain temps ou d’une certaine valeur). Ceci permet
    de trouver par exemples des segments périodiques dans un signal
    bruité.\

-   **Fonction caractéristique**: Pour une variable X, la fonction
    caractéristique est la valeur attendue (expected value, mean) de
    exp(j$\omega$x), ou encore, la transformée de Fourier inverse de la
    densité de probabilité. En 2D, la fonction caractéristique est la
    transformée de Fourier inverse en 2D de la densité de probabilité
    jointe.

[9]{}

Goodman, Joseph W., *Speckle phenomena in optics: theory and
applications*, Roberts and Company Publishers (2007).

Goodman, J. W., Rawson, E. G., *Statistics of modal noise in fibers: a
case of constrained speckle*, Optics Letter Vol. 6 No. 7 (1981).

Kim, E. M, Franzen, D. L., *Measurements of Far-Field and Nead-Field
Radiation Patterns from Optical Fiber*, US National Bureau of Standards
(1981).

Masaaki, Imai, *Statistical Properties of Optical Fiber Speckles*,
Bulletin of the Faculty of Engineering, Hokkaido University (1985).

Crosignani, B. et al., *Speckle-pattern visibility of light transmitted
through a multimode optical fiber*, Optical Society of America Vol. 66
No. 11 (1976).

Mehta, D. S. et al., *Laser speckle reduction by multimode optical fiber
bundle with combined temporal, spatial, and angular diversity*, Applied
Optics Vol. 51 No. 12 (1976).