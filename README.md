# Tietokantasovellus

## Aihekuvaus 

Sovellus on eräänlainen dirnkkitietokanta, jonka aihe on muokattu aiheesta Drinkkiarkisto. Sovellus rakentuu tietokantaan tallennettavien käyttäjien ja juomien päälle. Käyttäjät voivat merkitä itselleen eri juomia. Merkitessään itselleen jonkin tietyn juoman, sovellus tallentaa tästä merkinnän tietokantaan. Näin ollen sovellus kerää dataa käyttäjien itselleen merkitsemistä juomista.

Sovelluksessa on määrä olla admin-käyttäjä, joka pystyy tarkastelemaan kättäjälistoja, juomalistoja sekä tilastoja merkityistä juomista. Järjestelmän on mahdollista tuottaa ajantasoisia listoja käyttäjistä, juomista ja merkintätilastoista. Järjestelmään kirjaudutaan sisään ja tavallisen käyttäjän oikeudet ovat admin-käyttäjää rajoitetumpia. Admin käyttäjän tulee hyväksyä uudet käyttäjät ja juomat sovellukseen. Admin käyttäjä voi antaa laajennettuja oikeuksia muille käyttäjille. 

Alustavia toimintoja:

- Kirjautuminen
- Juomien haku
- Juomien selailu
- Juoman merkitseminen käyttäjälle
- Juoman lisääminen tietokantaan
- Juomien sisäänluku tiedostosta
- Käyttäjätunnuksen luominen
- Käyttäjätietojen muutos ja tilin poisto

## Dokumentaatiota

[Työaikakirjanpito](https://github.com/Kallmark/Tietokantasovellus/blob/master/documentation/ty%C3%B6aikakirjanpito.md)

[Arkkitehtuurkuvaus(tietokanta)](https://github.com/Kallmark/Tietokantasovellus/blob/master/documentation/arkkitehtuurikuvaus.md)

[Käyttötapauksia / user stories](https://github.com/Kallmark/Tietokantasovellus/blob/master/documentation/stories.md)


## Käyttöohje

Sovellusta voi käyttää joko herokussa tai lokaalisti. 

Linkki Herokussa olevaan sovellukseen: https://tietokantasovellus-python.herokuapp.com/

Herokussa olevaa sovellusta voi testata testikäyttäjätunnuksella:

- Tunnus: hello
- Salasana: world

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






