# Tehtävän raportti kokemuksista

## Koodin täydennys

Inline-ehdotus oli hyödyllinen lähinnä metodin perusrakenteen muistuttajana, mutta sen hyväksymistä ei olisi voinut tehdä lukematta ehdotusta. Olennaista oli tarkistaa, että lajittelu tapahtui maalien eikä pisteiden perusteella ja että `how_many` rajasi palautettavan listan. Ehkä ehdotusten haittapuoli oli se, että ne voivat ohjata ratkaisua ennen kuin ehtii itse suunnitella sen.

## Pylint

Pylint-varoituksen selityksessä korostui, että varoitus kertoo koodin laadusta ja ylläpidettävyydestä, ei ehkä välttämättä ohjelman suorasta toimintavirheestä. Selitys piti tarkistaa Pylintin dokumentaatiosta. Tämän projektin valmiissa koodissa oli useita aiempia Pylint-varoituksia, kuten puuttuvia docstringejä ja `requests.get`-kutsun puuttuva timeout.

## Agentin tekemä toiminnallisuus ja testit

Joukkueen pelaajien pistejärjestyksessä näyttävä toiminnallisuus toteutettiin `PlayerStats.top_scorers_by_team`-metodilla ja käyttöliittymän joukkuevalinnalla. Ratkaisu palauttaa vain valitun joukkueen pelaajat ja järjestää heidät maalien ja syöttöjen summan mukaan laskevasti. Yksikkötestit käyttävät HTTP-yhteyden sijasta `StubPlayerReader`-luokkaa, joten testit ovat nopeita ja toistettavia eivätkä tee verkkopyyntöjä.
