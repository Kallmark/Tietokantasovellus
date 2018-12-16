# Tietokantasovellus

## Aihekuvaus 

Sovellus on eräänlainen virvoikekauppa, jonka aihe on muokattu aiheesta Drinkkiarkisto. Sovellus rakentuu tietokantaan tallennettavien käyttäjien ja tavaroiden päälle. Käyttäjät voivat merkitsemällä ostaa itselleen eri tavaroita. Merkitessään itselleen jonkin tietyn tavaran, sovellus tallentaa tästä merkinnän tietokantaan. Samalla sivu vähentää käyttäjän saldosta tuotteen hinnan ja päivittää tuotteen määrää tietokannasssa. Tallentamalla erikseen jokaisen ostotapahtuman sovellus kerää dataa myös käyttäjien ostoskäyttäytymisestä.

Tavallisten käyttäjien on mahdollista tarkastella tuotelistaa, tehdä ostoksia, tarkastella sovelluksen statistiikkaa ja tarvittaessa muokata omia tietojaan. 

Sovelluksessa on admin-käyttäjä, joka käyttäjätoiminnallisuuksian lisäksi pystyy tarkastelemaan kättäjälistoja, muokkaamaan käyttäjien saldoa, poistamaan käyttäjätunnuksia, ja poistamaan sekä muokkaamaan tuotteita. 

Statistiikkanäkymässä sivu näyttää listauksen eniten ostetuista tuotteista ja eniten tuotteita ostaneista käyttäjistä.


## Dokumentaatiota

[Työaikakirjanpito](https://github.com/Kallmark/Tietokantasovellus/blob/master/documentation/ty%C3%B6aikakirjanpito.md)

[Tietokantakuvaus](https://github.com/Kallmark/Tietokantasovellus/blob/master/documentation/arkkitehtuurikuvaus.md)

[Käyttötapauksia / user stories](https://github.com/Kallmark/Tietokantasovellus/blob/master/documentation/stories.md)

[Tarkempi käyttöohje](https://github.com/Kallmark/Tietokantasovellus/blob/master/documentation/k%C3%A4ytt%C3%B6ohje.md)


## Sovelluksen käyttäminen

### Heroku

[Linkki Herokussa olevaan sovellukseen](https://tietokantasovellus-python.herokuapp.com/)

Herokussa olevaa sovellusta voi testata admin-oikeudet omaavalla testikäyttäjätunnuksella:

- Tunnus: hello
- Salasana: world

Käyttäjän on mahdollisuutta käyttää sovellusta myös rekisteröitymällä sinne itse. 

### Lokaali sovellus

Lokaalisti sovellusta voi käyttää lataamalla sovelluksen tiedostot suoraan repositoriosta komennolla:

```
git clone https://github.com/Kallmark/Tietokantasovellus.git
```

Ennen sovelluksen käyttöä sinun pitää vielä asentaa virtuaaliympäristö sovelluksen juurikansioon. Tämä onnistuu seuraamalla kommennolla sovelluksen juurikansiossa:

```
python3 -m venv venv
```
Tämän jälkeen virtuaaliympäristön voi käynnistää seuraavalla komennolla sovelluksen juurikansiossa:

```
source venv/bin/activate
```
Virtuaaliympäristössä sovelluksen saa käynnistettyä seuraavalla komennolla sovelluksen juurikansiossa:

```
python run.py
```

Sovellus on tämän jälkeen nähtävissä osoitteessa localhost:5000. 






