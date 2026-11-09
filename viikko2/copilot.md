# Copilot-tehtävän raportti

## Koodin täydennys

Copilot ehdotti `top_goal_scorers`-metodiin pelaajien hakemista, lajittelua
maalien mukaan laskevasti ja tuloksen rajaamista `how_many`-parametrilla.
Ehdotus vastasi docstringin kuvausta ja projektin tarvitsemaa toimintaa.

## Pylint-selitys

Pylint antoi tahallisesti lisätystä pitkästä kommentista varoituksen
`C0301: Line too long (117/100)`. Selitys oli, että rivi ylitti projektin
100 merkin maksimipituuden. Pitkän rivin jakaminen tai poistaminen korjasi
varoituksen.

## Agentin ratkaisu ja testit

Joukkueen mukaan pistejärjestykseen lajitteleva toiminto tarkistaa myös
pelaajan kaikki joukkueet, jos joukkuetieto sisältää useamman joukkueen.
`PlayerStats`-testit käyttävät `StubPlayerReader`-oliota, joten ne eivät tee
verkkopyyntöjä. Testit kattavat kansalaisuuden, maalintekijät ja joukkueen
mukaan lajittelun. Kaikki kolme testiä menivät läpi.

## Erot edellisen viikon testeihin

Tässä testissä tilastoluokalle annetaan ennalta määriteltyjä pelaajia
palauttava stub-lukija. Näin testattava lajittelu ja suodatus eivät riipu
HTTP-yhteydestä tai NHL-palvelun saatavuudesta.

## Pylintin löytämät virheet

Kehityksen aikana Pylint huomautti ensin `main`-funktion liian monista
lauseista ja `PlayerReader`-luokan vähäisistä julkisista metodeista.
Ne korjattiin tai käsiteltiin projektin konfiguraatiossa. Tehtävän
tarkoituksellinen pitkä kommentti tuotti `line-too-long`-varoituksen.
Väliaikaisen kommentin poistamisen jälkeen Pylint antoi 10/10.

## Muut opit

`uv`-komennot toimivat tässä ympäristössä Ubuntu/WSL-terminaalissa projektin
juuresta, jossa `pyproject.toml` sijaitsee. Windowsin PowerShell ei löytänyt
`uv`-komentoa. Testit ja Pylint voi ajaa WSL:ssä komennoilla
`uv run pytest` ja `uv run pylint src`.
