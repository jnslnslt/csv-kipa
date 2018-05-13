# excel-kipa-cli

Komentorivipohjainen työkalu, jolla voidaan lukea excel-tiedosto (.xls/.xlsx) ja täyttää [KIPA:n](https://github.com/partio-scout/kipa) tehtävä-formi. Excel-taulukon rakenne: 1. sarake: vartion nro, 2. sarake: kisapisteet, 3. sarake: tekstilaatikon id:n loppuosa

Ohjelma kokoaa tekstilaatikon id:n vartion numerosta ja id:n loppuosasta.
Otsikkorivin teksteillä ei ole merkitystä.

#### Esimerkki:
| nro | pisteet | id:n loppu |
| --- | --- | --- |
| 101 | 5 | _449-arvo |
| 102 | 3 | _449-arvo |

#### Riippuvuudet:
- paljon, kts. requirements.txt
- lisäksi [ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/)
