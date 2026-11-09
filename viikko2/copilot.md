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

Toteutin joukkueen mukaan pistejärjestykseen lajittelevan toiminnon ja
testasin sen `StubPlayerReader`-oliolla. Testit eivät tee verkkopyyntöjä,
ja niissä tarkistetaan myös pelaaja, jonka tiedoissa on useampi joukkue.
Kaikki kolme `PlayerStats`-testiä menivät läpi.

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

Opin, että pelaajien hakemisen erottaminen tilastojen muodostamisesta
helpottaa tilastologiikan testaamista. Stubin avulla lajittelun voi testata
ennalta tunnetulla aineistolla ilman, että testi riippuu verkkopalvelusta.
Opin myös, että Copilotin ehdotuksen oikeellisuus kannattaa tarkistaa
tehtävän vaatimuksia vasten ja varmistaa testeillä.
