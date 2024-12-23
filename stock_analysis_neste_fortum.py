# -*- coding: utf-8 -*-
"""Tehtävä2_osa1.ipynb

# Tarkastellaan Nesteen ja Fortumin osakekurssien aikasarjoja.
"""

# Tuodaan tarvittavat kirjastot
import pandas as pd  # pandas on kirjasto, jota käytetään datan käsittelyyn ja analysointiin
import matplotlib.pyplot as plt  # matplotlib mahdollistaa graafien ja kuvioiden luomisen
import seaborn as sns  # seaborn on laajennus, joka helpottaa visuaalisesti houkuttelevien graafien luomista
import yfinance as yf  # yfinancea käytetään taloustiedon, kuten osakekurssien, lataamiseen

# Määritetään visualisointien tyyli
sns.set_style("whitegrid")  # Asetetaan Seabornin graafien tyyli "whitegridiksi", joka lisää valkoisen taustan ja ruudukon

"""# Datojen nouto
Yahoo Finance -palvelu https://finance.yahoo.com/ sisältää tietoa osakkeista, valuutoista, raaka-aineista jne.
"""

# tuodaan Yahoo Financesta tiedot:
neste = yf.download('NESTE.HE', start='2018-01-01')
fortum = yf.download('FORTUM.HE', start='2018-01-01')

# Datan alku- ja loppuosa
neste

# Datan alku- ja loppuosa
fortum

"""# Aikasarjan kuvaaja"""

# Visualisoidaan osakekurssien kehitys koko aikavälillä
fig, axs = plt.subplots(nrows=1, ncols=2, figsize=(10, 3))  # Luodaan kaksi rinnakkaista kuvaajaa (1 rivi, 2 saraketta), joiden koko on määritelty (10 x 3 tuumaa)
neste['Close'].plot(ax=axs[0])  # Piirretään Nesteen osakekurssin päätöskurssien kehitys ensimmäiseen kuvaajaan
fortum['Close'].plot(ax=axs[1])  # Piirretään Fortumin osakekurssin päätöskurssien kehitys toiseen kuvaajaan

# Kehitys viime vuonna
fig, axs = plt.subplots(nrows=1, ncols=2, figsize=(10, 3))  # Luodaan kaksi rinnakkaista kuvaajaa (1 rivi, 2 saraketta), joiden koko on määritelty (10 x 3 tuumaa)
neste['Close']['2023':].plot(ax=axs[0])  # Piirretään Nesteen osakekurssin päätöskurssien kehitys vuodesta 2023 lähtien ensimmäiseen kuvaajaan
fortum['Close']['2023':].plot(ax=axs[1])  # Piirretään Fortumin osakekurssin päätöskurssien kehitys vuodesta 2023 lähtien toiseen kuvaajaan

# tarkemman ajanjakson voi määritellä myös ilmoittamalla alku- ja loppupäivän
neste['Close']['2024-01-01':'2024-10-13'].plot()

"""# Aggregointi
Tässä yhteydessä aggregointi tarkoittaa päivittäisten päätöshintojen ryhmittelyä ja tiivistämistä kuukausitasolle laskemalla kunkin kuukauden päätöshintojen keskiarvo. Käytännössä jokaisen kuukauden päätöshintojen joukosta lasketaan yksi keskiarvo, joka edustaa kyseisen kuukauden hintakehitystä.


resample-funktiota käytetään ajanjaksotetussa datassa (time series data) näytteistämiseen tai uudelleennäytteistämiseen eri aikaväleillä. Sitä hyödynnetään esimerkiksi silloin, kun halutaan muuttaa dataa eri aikaskaalalle — esimerkiksi päivittäisistä arvoista kuukausittaisiin, viikoittaisiin tai vuosittaisiin arvoihin.
"""

# Päivän päätöshintojen aggregointi kuukausitasolle keskiarvoja käyttäen
fig, axs = plt.subplots(nrows=1, ncols=2, figsize=(10, 3))  # Luodaan kaksi rinnakkaista kuvaajaa (1 rivi, 2 saraketta), joiden koko on määritelty (10 x 3 tuumaa)
neste['Close'].resample('ME').mean().plot(ax=axs[0])  # Ryhmitellään Nesteen päivittäiset päätöshinnat kuukausittain ja lasketaan keskiarvo, jonka jälkeen piirretään kuukausitasoinen keskiarvokäyrä ensimmäiseen kuvaajaan
fortum['Close'].resample('ME').mean().plot(ax=axs[1])  # Tehdään sama Fortumille

# Lasketaan vaihdon kokonaismäärät kuukausitasolla
fig, axs = plt.subplots(nrows=1, ncols=2, figsize=(14, 5))  # Luodaan kaksi rinnakkaista kuvaajaa (1 rivi, 2 saraketta), joiden koko on määritelty (14 x 5 tuumaa)
neste['Volume'].resample('ME').sum().plot(ax=axs[0])  # Ryhmitellään Nesteen päivittäinen vaihto kuukausittain ja lasketaan kokonaismäärä, jonka jälkeen piirretään kuukausitasoinen vaihtokäyrä ensimmäiseen kuvaajaan
fortum['Volume'].resample('ME').sum().plot(ax=axs[1])  # Ryhmitellään Fortumin päivittäinen vaihto kuukausittain ja lasketaan kokonaismäärä, jonka jälkeen piirretään kuukausitasoinen vaihtokäyrä toiseen kuvaajaan

"""Koronapandemia on todennäköisesti ollut merkittävä tekijä sekä Nesteen että Fortumin osakkeiden vaihtomäärien piikeissä erityisesti vuonna 2020. Pandemia aiheutti suurta epävarmuutta markkinoilla, ja tämä näkyy kasvaneena kaupankäyntivolyymina, kun sijoittajat yrittivät reagoida nopeasti muuttuviin markkinaolosuhteisiin."""

# Osakkeiden vaihdon määrät (kpl) vuosineljänneksittäin (aggregointi summaa käyttäen)
# Viimeisen vuosineljänneksen kohdalla voi olla äkillinen pudotus, jos vuosineljännes on vasta aluillaan
# Vaihdon aggregointi neljännesvuositasolle ja visualisointi
fig, axs = plt.subplots(nrows=1, ncols=2, figsize=(10, 3))  # Luodaan kaksi rinnakkaista kuvaajaa (1 rivi, 2 saraketta), joiden koko on määritelty (10 x 3 tuumaa)
(neste['Volume'] / 1000000).resample('QE').sum().plot(ax=axs[0])  # Ryhmitellään Nesteen vaihto neljännesvuosittain, muunnetaan miljooniksi kappaleiksi ja piirretään ensimmäiseen kuvaajaan
(fortum['Volume'] / 1000000).resample('QE').sum().plot(ax=axs[1])  # Ryhmitellään Fortumin vaihto neljännesvuosittain, muunnetaan miljooniksi kappaleiksi ja piirretään toiseen kuvaajaan
axs[0].set_ylabel('Miljoonaa kpl')  # Asetetaan y-akselin nimeksi 'Miljoonaa kpl' ensimmäisessä kuvaajassa

"""# Liukuvia keskiarvoja
Liukuvat keskiarvot ovat menetelmä, jolla pyritään tasoittamaan aikasarjadataa poistamalla lyhyen aikavälin vaihteluita ja korostamalla pidemmän aikavälin trendejä. Tämä on erityisen hyödyllistä silloin, kun halutaan vähentää satunnaisten piikkien vaikutusta, jotka voivat häiritä kokonaiskuvaa. Liukuvien keskiarvojen avulla voidaan esimerkiksi paremmin havaita selkeä trendi osakekurssien muutoksessa, lämpötilan vaihteluissa tai muissa aikasarjoissa.

Liukuva keskiarvo lasketaan ottamalla useamman peräkkäisen ajanjakson (esim. päivien, viikkojen tai kuukausien) arvojen keskiarvo ja siirtämällä tätä laskentaa ajassa eteenpäin. Jokaisessa vaiheessa lasketaan keskiarvo esimerkiksi edellisen kolmen päivän arvoista, ja tämä keskiarvo päivitetään, kun edetään ajassa. Näin saadaan "liukuva" keskiarvo, joka muuttuu ajan myötä mutta tasoittaa lyhyen aikavälin vaihteluita.

Tunnuslukujen laskenta onnistuu **rolling**-funktiolla.
Teknisessä analyysissä aikasarjan ja liukuvien keskiarvojen leikkauskohtia käytetään osto- ja myyntisignaaleina.


"""

# piirretään samaan kuvaan erilaisia liukuvia keskiarvoja:
# arvot sellaisenaan
neste['Close'].plot(figsize=(14,5))
# liukuva keskiarvo (50 arvoa)
neste['Close'].rolling(50).mean().plot()
# liukuva keskiarvo (200 arvoa):
neste['Close'].rolling(200).mean().plot()
# lisätään selitelaatikko
plt.legend(['Arvot sellaisenaan', '50 pvn liukuva keskiarvo', '200 päivän liukuva keskiarvo'])

# sama Fortumin osakkeilla
# arvot sellaisenaan
fortum['Close'].plot(figsize=(14,5))
# liukuva keskiarvo (50 arvoa)
fortum['Close'].rolling(50).mean().plot()
# liukuva keskiarvo (200 arvoa):
fortum['Close'].rolling(200).mean().plot()
# lisätään selitelaatikko
plt.legend(['Arvot sellaisenaan', '50 pvn liukuva keskiarvo', '200 päivän liukuva keskiarvo'])

"""# Muutosprosentit
Muutosprosentit lasketaan pct_change-funktiolla. Tulos on desimaalimuodossa; tarvittaessa saan prosenttiluvut kertomalla luvulla 100.

Kun lasketaan aina peräkkäisille arvoille muutosprosentti, muodostuu uusi aikasarja.
"""

# lasketaan prosentuaaliset muutokset, tarkastellaan päätöshintoja:
# Ensimmäinen arvo puuttuu, niinkuin kuuluukin
neste['neste_muutos%'] = neste['Close'].pct_change()
fortum['fortum_muutos%'] = fortum['Close'].pct_change()

# tarkistetaan
neste

# muodostetaan uusi dataframe, johon kerätään molempien osakkeiden muutosprosentit
muutosprosentit = pd.concat([neste['neste_muutos%'], fortum['fortum_muutos%']], axis=1)

#korvataan puuttuvat arvot nollilla
muutosprosentit = muutosprosentit.fillna(0)

muutosprosentit

# tarkastellaan vuotta 2024 ja siirrytään desimaaliluvuista prosentteihin
(muutosprosentit.loc['2024']*100).plot()
# y-akselin otsikko
plt.ylabel('Prosentit')
# merkitään 0-kohta selkeämmin
plt.axhline(0, color='black')

# tunnuslukuja muutosprosenteista
(muutosprosentit*100).describe().round(3)

"""Nesteen osake näyttää hieman volatiilimmalta kuin Fortumin, sillä sen keskihajonta on suurempi ja päivittäiset hinnanmuutokset ovat olleet suurempia.
Molemmilla osakkeilla on ollut yksittäisiä päiviä, jolloin hinnat ovat joko laskeneet tai nousseet huomattavasti, mutta yleisesti muutokset ovat keskittyneet hyvin lähelle nollaa.
Fortumin osakkeella on hieman positiivisempi mediaani, mikä viittaa siihen, että sillä on ollut keskimäärin hieman enemmän positiivisia päiviä kuin Nesteellä.

"""

# Sama laatikkojanakuviolla
sns.boxplot(data=muutosprosentit*100)

"""Molempien osakkeiden päivittäiset muutokset ovat jakautuneet siten, että mediaanit ovat hyvin lähellä nollaa, mikä tarkoittaa, että keskimäärin päivittäiset muutokset ovat pieniä.

Neste näyttää hieman volatiilimmalta, sillä sillä on enemmän äärimmäisiä poikkeavia havaintoja, erityisesti suuria laskuja, jotka ovat yli 10 %.

Fortumilla vaihtelut ovat tasaisempia, mutta silläkin on useita poikkeavia päiviä
"""

# poimitaan isot muutokset (abs-toiminnolla saadaan >10% tai <10%)
# Koodi poimii ne rivit, joissa joko Nesteen tai Fortumin osakkeen muutosprosentti on absoluuttisesti suurempi kuin 10 % (eli muutos on joko suurempi kuin +10 % tai pienempi kuin -10 %).
muutosprosentit[(abs(muutosprosentit['neste_muutos%']) > 0.1) | (abs(muutosprosentit['fortum_muutos%']) > 0.1)]

"""# Muutosprosenttien välinen korrelaatio"""

# muutosten korrelaatiot
muutosprosentit.corr()

"""Päivittäisten muutosprosenttien välillä on positiivinen mutta melko heikko korrelaatio. Positiivinen korrelaatio tarkoittaa, että kun Nesteen osake nousee, Fortumin osake nousee yleensä samansuuntaisesti, mutta vaikutus ei ole kovin vahva."""

# tarkastellaan yhteyttä vielä hajontakuviolla
plt.scatter(muutosprosentit['neste_muutos%'], muutosprosentit['fortum_muutos%'])
plt.xlabel('Nesteen muutosprosentti desimaalilukuna')
plt.ylabel('Fortumin muutosprosentti desimaalilukuna')

"""Hajontakuvio auttaa tunnistamaan, onko kahden muuttujan välillä positiivinen, negatiivinen vai ei lainkaan korrelaatiota. Jos pisteet sijoittuvat nousevasti vasemmalta oikealle, muuttujat ovat positiivisesti korreloituneita. Jos pisteet laskevat vasemmalta oikealle, korrelaatio on negatiivinen. Jos pisteet ovat satunnaisesti hajallaan, korrelaatio on heikko tai olematon.

Vaikka Nesteen ja Fortumin osakkeiden päivittäisten muutosprosenttien välillä on jonkinlainen positiivinen korrelaatio, se ei ole erityisen vahva. Molemmat yhtiöt toimivat samalla alalla, mikä saattaa selittää joidenkin päivien samansuuntaiset liikkeet, mutta yrityskohtaiset tekijät voivat silti aiheuttaa eroja päivittäisissä muutoksissa.
"""

# lasketaan vielä liukuva korrelaatio
muutosprosentit['neste_muutos%'].rolling(50).corr(muutosprosentit['fortum_muutos%']).plot()
plt.axhline(color='red')

"""Nesteen ja Fortumin osakemuutosten välinen korrelaatio ei ole vakio, vaan vaihtelee merkittävästi ajan myötä. On ajanjaksoja, jolloin osakkeet liikkuvat hyvin samansuuntaisesti (korkea positiivinen korrelaatio), mutta on myös aikoja, jolloin niiden muutokset eivät näytä olevan merkittävässä yhteydessä toisiinsa (matala tai negatiivinen korrelaatio). Tämä voi viitata siihen, että molemmat yritykset altistuvat paitsi yhteisille markkinatekijöille myös yksilöllisille tapahtumille, jotka vaikuttavat niihin eri tavoin eri aikoina.

# Osakkeisiin liittyvä riski eli volatiliteetti

Volatiliteetti voidaan laska päivittäisten muutosprosenttien keskihajontana ( std-funktiolla ) ja se skaaltaaan vuositasolle kertomalla vuoden kaupantekopäivien lukumäärän neliöjuurella (sama kuin korotus potenssiin 0.5). Vuoteen sisältyvien kaupantekopäivien lukumäärä vaihtelee vuodesta toiseen. Tässä käytetty lukumäärää 252.

Liukuva volatiliteetti kuvaa, miten volatiliteetti (riski) on muuttunut ajan kuluessa.
"""

# lasketaan 200 päivän liukuva volatiliteetti
plt.figure(figsize=(14,5))
(muutosprosentit['neste_muutos%'].rolling(200).std()*(252**0.5)).plot()
(muutosprosentit['fortum_muutos%'].rolling(200).std()*(252**0.5)).plot()
plt.legend(['Neste', 'Fortum'])

"""Sekä Nesteellä (sininen viiva) että Fortumilla (oranssi viiva) volatiliteetti nousi jyrkästi vuoden 2020 alussa, mikä osuu yhteen koronapandemian alkuvaiheen kanssa. Tämä viittaa siihen, että pandemian aiheuttama epävarmuus ja markkinoiden heilahtelut vaikuttivat merkittävästi molempien osakkeiden hintojen vaihteluun.

Vuoden 2021 jälkeen Nesteen volatiliteetti laski, mutta se on noussut uudelleen vuoden 2023 lopusta lähtien ja on selvästi matkalla ylöspäin.

Fortumin volatiliteetti nousi myös merkittävästi vuoden 2020 aikana, mutta se laski nopeammin verrattuna Nesteeseen. Vuoden 2021 jälkeen Fortumin volatiliteetti pysyi melko matalana ja vakaana verrattuna Nesteen volatiliteettiin.

Vuoden 2022 jälkeen Fortumin volatiliteetti on pysynyt tasaisempana ja alhaisempana kuin Nesteen, mikä voi viitata siihen, että Fortumin osake ei ole kokenut yhtä suuria markkinashokkeja tai hintavaihteluita.

# Kaahden arvoakselin viivakaavio
Nesteen ja Fortumin päätöshinnat ovat eri suuruusluokkaa. Jos haluan kuvata ne päällekkäin samaan kaavioon, niin voin käyttää kahden arvoakselin kaaviota.
"""

# Viivakaavio Nesteen ja Fortumin päätöshinnoista yhdellä kuvaajalla
fig, ax = plt.subplots(figsize=(10, 6))
neste['Close'].plot(ax=ax, color='dodgerblue', label='Neste')  # Piirretään Nesteen päätöshinnat
twin_ax = ax.twinx()  # Luodaan toinen y-akseli Fortumia varten
fortum['Close'].plot(ax=twin_ax, color='darkviolet', label='Fortum')  # Piirretään Fortumin päätöshinnat
twin_ax.set_ylabel('Fortum', color='darkviolet', fontsize=14)
ax.set_ylabel('Neste', color='dodgerblue', fontsize=14)
plt.title('Nesteen ja Fortumin osakkeiden hinnan kehitys')
ax.legend(loc='upper left')
twin_ax.legend(loc='upper right')

"""# Onko viikonpäivällä yhteyttä tuottoprosenttiin?"""

viikonpaivat = ['ma', 'ti', 'ke', 'to', 'pe']

muutosprosentit['Weekday'] = muutosprosentit.index.weekday

df1 = (muutosprosentit*100).groupby('Weekday')['neste_muutos%'].describe()
df1.index = viikonpaivat
df1

"""Tiistaina on näyttänyt olevan positiivisin keskiarvo, mikä saattaa viitata siihen, että viikon alun markkinatunnelma muuttuu myönteisemmäksi tiistaisin.
Maanantaina ja keskiviikkona keskimääräiset tuotot ovat olleet hieman negatiivisia.
Torstain ja keskiviikon tuottoprosentit näyttävät olevan kaikkein vaihtelevimpia, mikä voi viitata näinä päivinä tapahtuvaan markkinavolatiliteettiin.
"""

# Testataan onko tiistain ja keskiviikon välillä merkitsevää eroa

# Vertailtavien ryhmien muodostaminen
ti = muutosprosentit['neste_muutos%'][muutosprosentit['Weekday']==1]
ke = muutosprosentit['neste_muutos%'][muutosprosentit['Weekday']==2]

# Kahden riippumattoman (ind) otoksen t-testi
from scipy.stats import ttest_ind
ttest_ind(ti, ke, equal_var=False, nan_policy='omit')

"""p-arvo on > 5%, eli analyysi ei löydä merkittävää eroa tiistain ja keskiviikon keskimääräisten tuottoprosenttien välillä. Tämä viittaa siihen, että näiden päivien tuottojen keskiarvoissa ei ole systemaattista eroa, ainakaan käytettävissä olevan datan perusteella."""

