# Web FestesFME

L'objectiu d'aquesta web es mantenir un arxiu sobre els dissenys de les promocions de festes i alguna cosa més per l'estil, evitant així que tota petjada que deixi una promoció s'acabi perdent amb els anys.

La web està feta amb [Zola](https://www.getzola.org/), un SSG (Static Site Generator) bastant simple però flexible. Per fer les templates s'utilitza [Bulma](https://bulma.io/), un framework CSS que és també molt senzillet.

Si no entens res del paràgraf anterior no et preocupis, no et farà falta. Tota la web està muntada perquè, a grans trets, la teva única feina sigui canviar "Festes N" a "Festes N+1" i pujar les quatre fotos amb els vostres dissenys, en la següent secció concreto més.

Si en canvi tens interès en modificar les templates (ja sigui per canviar el estil com per afegir funcionalitats), més endavant també comento com fer-ho per sobre.

## Imprescindible per una nova promoció de festes

Com s'ha dit abans, no cal que hagueu de programar res si no voleu, està tot muntat. Per afegir el contingut de la vostra promoció haureu de seguir els següents passos:

1. Actualitzeu els mantainers
    1. Decidir qui portarà el manteniment de la web, ja que si una promoció antiga vol alguna cosa és a qui es dirigiran.
    2. A la pàgina de contacte (`content/generacions/contacte.md`) canvieu les dades dels mantainers actuals per les dels nous
3. Crear la carpeta *festesXX* a `static` i pujar-hi el vostre disseny principal de camiseta
4. Opcionalment, podeu pujar també la vostra foto de grup i altres dissenys que hagueu fet a la mateixa carpeta
5. Copieu el fitxer `content/generacions/festes50.md` a `content/generacions/festesXX.md`, on *XX* és el nombre de la vostra promoció (**és necessari que coincideixi amb el nom de la carpeta anterior!!!**)
6. Modifiqueu el contingut de la vostra promoció
    1. Canvieu el títol i la descripció
    2. Canvieu `true` per `false` a la línea on hi diu *draft*
    3. Actualitzeu el nom del fitxer de `disseny_principal` i, opcionalment, dels dissenys secundaris
    4. Actualitzeu la llista d'integrants, seguint el mateix format
    5. Canvieu el text de sota del `+++` pel que vulgueu
7. Ja hauríeu de tenir tot funcionant!!

Algunes suggerències:

- Les fotos de les camisetes haurien de ser quadrades i amb fons transparent. Intenteu deixar un marge similar al de les fotos de la resta de promocions
- La foto de grup ha de ser horitzontal, ja que el format quedarà molt malament
- No feu una descripció gaire llarga, ja que si ocupa 2 línies trencarà la graella principal (no passa res, però quedarà menys bonic)ç
- Natualment, no poseu un mail de contacte que no mireu xD

### Històric de mantainers

En un futur potser passa que voleu canviar una cosa i penseu: "Qui serà l'inútil que va programar això tant malament?". En aquest apartat tens la solució
