# Copilot-tehtävän raportti

## Koodin täydennys

Inline-ehdotus oli hyödyllinen lähinnä metodin perusrakenteen muistuttajana,
mutta sen hyväksymistä ei olisi voinut tehdä lukematta ehdotusta. Olennaista
oli tarkistaa, että lajittelu tapahtui maalien eikä pisteiden perusteella ja
että `how_many` rajasi palautettavan listan. Ehdotusten haittapuoli oli se,
että ne voivat ohjata ratkaisua ennen kuin ehtii itse suunnitella sen.

## Chat ja Pylint

Pylint-varoituksen selityksessä korostui, että varoitus kertoo koodin
laadusta ja ylläpidettävyydestä, ei välttämättä ohjelman suorasta
toimintavirheestä. Selitys piti tarkistaa Pylintin dokumentaatiosta. Tämän
projektin valmiissa koodissa oli useita aiempia Pylint-varoituksia, kuten
puuttuvia docstringejä ja `requests.get`-kutsun puuttuva timeout.

## Agentin tekemä toiminnallisuus ja testit

Joukkueen pelaajien pistejärjestyksessä näyttävä toiminnallisuus toteutettiin
`PlayerStats.top_scorers_by_team`-metodilla ja käyttöliittymän joukkuevalinnalla.
Ratkaisu palauttaa vain valitun joukkueen pelaajat ja järjestää heidät maalien
ja syöttöjen summan mukaan laskevasti. Yksikkötestit käyttävät HTTP-yhteyden
sijasta `StubPlayerReader`-luokkaa, joten testit ovat nopeita ja
toistettavia eivätkä tee verkkopyyntöjä.

Testeissä stubi eroaa hieman edellisen viikon tavasta siinä, että se korvaa
riippuvuuden kokonaan ja palauttaa valmiiksi rakennetut pelaajat. Testit
keskittyvät `PlayerStats`-luokan omaan logiikkaan eivätkä verkon tai
`PlayerReader`-luokan toimintaan.

## Muut havainnot

Pylint ei löytänyt uusista `PlayerStats`-metodeista toiminnallisia virheitä.
Se ilmoitti kuitenkin projektissa ennestään olleista puuttuvista docstringeistä,
puuttuvasta `requests.get`-kutsun timeoutista ja muista tyyliongelmista.
Tässä tehtävässä opin erityisesti sen, että agentin käännös- tai
linttaustarkistus ei korvaa toiminnallisia yksikkötestejä.
Lisäksi opin tarkistamaan muutokset `git diff`-komennolla ja varmistamaan,
että testit eivät kutsu verkkoa.
