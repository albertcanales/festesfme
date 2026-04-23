# Web Festes FME

Codi font de la [Web de Festes FME](https://apps.dafme.upc.edu/festes).

La web té tres objectius principals:

4. Conservar el catàleg històric de dissenys de Festes de la FME.
5. Mostrar les persones que han fet possible cada comissió de Festes.
6. Facilitar la tasca de reimpressió de dissenys a futures generacions.

La web està feta amb [Zola](https://www.getzola.org/), un SSG (Static Site Generator) ben simple. L'estil està fet amb [Bulma](https://bulma.io/), un CSS framework també triat per la seva simplicitat.

## Configuració Inicial

- Instal·la Docker per executar Zola ([instruccions aquí](https://docs.docker.com/engine/install/)).
- Clona el repositori privat amb els dissenys originals al directori `dissenys`: `git clone git@github.cgit clone git@github.com:albertcanales/festesfme-dissenys.git dissenys`
- Instal·la les dependències pel generador de samarretes: `make install`.

## Afegir una Generació

Hi ha una generació d'exemple disponible a `content/generacions/festes50.md`. Copia el fitxer a `content/generacions/festesXX.md`, on _XX_ denota l'any de la teva generació. El fitxer té comentaris explicant tots els camps

### Afegir un Disseny i Generar Samarretes

Afegeix els vostres dissenys originals (amb bona qualitat) a `dissenys/festesXX/`. El script de generació de dissenys s'encarregarà de generar les imatges de la samarreta amb el vostre disseny a sobre.

La posició del disseny a la samarreta depèn del nom del fitxer:

- Front (`*.png`): Es mostrarà en gran sobre la part davantera de la samarreta
- Back (`*_back.png`): Es mostrarà en gran sobre la part posterior de la samarreta
- Heart (`*_heart.png`): Es mostrarà en la zona del cor sobre la part davantera de la samarreta

De fet, no cal que siguin PNGs, poden ser altres formats. El tipus de posició es determina a partir de com acaba el basename del fitxer. Per tant, si no vols que el teu disseny sigui del tipus _front_, reanomena'l adequadament.

Genera les samarretes amb `make designs`. Ja hauries de veure la teva generació al menú principal, amb el disseny de la teva samarreta.

### Ajustar Posició del Disseny a la Samarreta

És possible que, per defecte, el disseny no quedi posicionat a la samarreta exactament com voldries. No et preocupis, hi ha les eines per ajustar això fàcilment!

Executa `make designs-debug`. Si recarregues la pàgina, hauries de veure que tots els dissenys estan encapsulats dins de dos rectangles:

- Taronja: Les dimensions del disseny.
- Groc: Les dimensions de la _box_. La box és la regió de la samarreta on es fa encabir el disseny. És diferent pels tipus _front_, _back_ i _heart_.

Les regles per les dimensions i posició del disseny dins de la _box_ són:

- El disseny es farà el més gran possible dins dels límits de la box, sense tallar-lo.
- Si queda espai sobrant als laterals (perquè ocupa el màxim verticalment), quedarà centrat horitzontalment.
- Si queda espai sobrant a dalt i a baix (perquè ocupa el màxim horitzontalment), es deixarà tot l'espai sobrant a la part de sota.

**No se t'acudeixi canviar les box del codi!!!** Estan prou ajustades i canviar-les trencaria tots els dissenys anteriors. El que hauries de fer és afegir el padding necessari per fer encabir el teu disseny com voldries.

Exemple: En el disseny de _Festes 91_, el generador per defecte posava el disseny massa amunt. S'ha afegit espai en blanc al disseny original perquè quedi més avall.

Pensa a tornar a executar `make designs` / `make designs-debug` cada cop que modifiquis el disseny per actualitzar-lo a la web.

POSICIÓ

**Quan acabis, no t'oblidis de commitejar els repos de dissenys i el de la web, s'han de fer els dos per separat!!**
