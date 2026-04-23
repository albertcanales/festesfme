# Web Festes FME

Codi font de la [Web de Festes FME](https://apps.dafme.upc.edu/festes).

La web té tres objectius principals:

4. Conservar el catàleg històric de dissenys de Festes de la FME.
5. Mostrar les persones que han fet possible cada comissió de Festes.
6. Facilitar la tasca de reimpressió de dissenys a futures generacions.

La web està feta amb [Zola](https://www.getzola.org/), un SSG (Static Site Generator) ben simple. L'estil està fet amb [Bulma](https://bulma.io/), un CSS framework també triat per la seva simplicitat.

## Configuració Inicial

- Instal·leu Docker per executar Zola ([instruccions aquí](https://docs.docker.com/engine/install/)).
- Cloneu el repositori privat amb els dissenys originals al directori `dissenys`: `git clone git@github.cgit clone git@github.com:albertcanales/festesfme-dissenys.git dissenys`
- Instal·leu les dependències pel generador de samarretes: `make install`.
