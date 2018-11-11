# Tietokantasovellus

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

## Tietokanta

Tietokannan on tarkoitus noudattaa alustavasti seuraavanlaista tietokantaa:

![Tietokantakaavio](https://raw.githubusercontent.com/Kallmark/Tietokantasovellus/master/documentation/pictures/tietokantakaavio_syksy2019.jpg "Alustava tietokantakaavio")

Huom! Sovellus ei tällä hetkellä noudata em. tietokantakaaviota. Ymmärsin tehtävänannon väärin tehdessäni 2 viikon materiaaliesimerkkiä, joten koodi on esimerkin mukainen. Tehtävänäni on seuraavaksi saada myös koodi vastaamaan sovelluksen omaa tietokantakaaviota. 

## Linkkejä

Linkki Herokussa olevaan sovellukseen: https://tietokantasovellus-python.herokuapp.com/


