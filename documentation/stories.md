# Käyttötapaukset

## Tietokannan omistaja

- Tietokannan omistaja voi lisätä tietokantaan tavaroita. TOTEUTETTU
- Tietokannan omistaja voi hallita tietokannan käyttäjätunnuksia. TOTEUTETTU
    - Nykyisessä versiossa tietokannan mostaja voi muokata käyttäjien saldoja, muttei tarkoituksella voi muuttaa käyttäjän nimeä, tunnusta tai salasanaa
- Tietokannan omistaja voi tuottaa raportteja tietokannan datasta. TOTEUTETTU
    - Ominaisuus toteutettiin siten, että tietokannan omistaja voi tarkastella tietokannan statistiikkaa. 
- Tietokannan omistaja voi tarkastella tuotteiden ja käyttäjien tietoja. TOTEUTETTU

## Tietokannan käyttäjä

- Tietokannan käyttäjä voi rekisteröidä itselleen tunnuksen. TOTEUTETTU
- Tietokannan käyttäjä voi kirjautua sisään. TOTEUTETTU
- Tietokannan käyttäjä voi merkitä tuotteita "ostetuksi." TOTEUTETTU
    - Käyttäjän tekemä ostos kasvattaa käyttäjän saldoa (miinustaa saldoa) ja vähentää varastossa olevan tuotteen määrää.
- Tietokannan käyttäjä voi tarkastella omia tietojaan. TOTEUTETTU
    - Käyttäjä voi tarkastella omia tietojaan ja tarvittaessa myös muokata nimeään, tunnustaan ja salasanaansa.
- Tietokannan käyttäjä voi tarkastella omaa ostohistoriaansa. TOTEUTETTU
    - Käyttäjä voi tarkastella omaa ostoshistoriaansa. Käyttäjä voi myös tarkastella sovelluksen yleistä statistiikkaa.
    
 ## Tulevaisuuden laajennusmahdollisuuksia
 
 - Sovellukseen voidaan lisätä myös muita statistiikkoja.
    -Esimerkiksi viimeisen kahden tunnin aikana eniten tuotteita ostaneet henkilöt.
 - Sovelluksen ulkoasuun voitaisiin implementoida esimerkiksi kuvia jokaisen tuotteen kohdalle. 
 - Tuotteita voisi tarvittaessa ostaa usean kerrallaan. Tämä jätettiin toistaiseksi kuitenkin tarkoituksella tekemättä.
