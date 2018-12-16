## Alustava tietokantakaavio (alkuperäinen)

Tietokannan oli tarkoitus noudattaa alustavasti seuraavanlaista tietokantaa:

![Tietokantakaavio](https://raw.githubusercontent.com/Kallmark/Tietokantasovellus/master/documentation/pictures/tietokantakaavio_syksy2019.jpg "Alustava tietokantakaavio")

## Ajantasainen tietokantakaavio

Tietokannan ajantasainen tietokantakaavio noudattaa seuraavaanlaista tietokantaa:

![Tietokantakaavio](https://raw.githubusercontent.com/Kallmark/Tietokantasovellus/master/documentation/pictures/tietokantakaavio2.jpg "Ajantasainen tietokantakaavio")

## Tietokantakyselyt

Tietokanta käyttää seuraavia kyselyitä tietokannan luomiseen:

```
CREATE TABLE account (
        id INTEGER NOT NULL,
        date_created DATETIME,
        date_modified DATETIME,
        name VARCHAR(144) NOT NULL,
        username VARCHAR(144) NOT NULL,
        password VARCHAR(144) NOT NULL,
        balance FLOAT NOT NULL,
        PRIMARY KEY (id)
)

CREATE TABLE product (
        id INTEGER NOT NULL,
        date_created DATETIME,
        date_modified DATETIME,
        name VARCHAR(144) NOT NULL,
        price FLOAT,
        amount INTEGER,
        PRIMARY KEY (id)
)

CREATE TABLE role (
        id INTEGER NOT NULL,
        date_created DATETIME,
        date_modified DATETIME,
        name VARCHAR(144) NOT NULL,
        account_id INTEGER NOT NULL,
        PRIMARY KEY (id),
        FOREIGN KEY(account_id) REFERENCES account (id)
)

CREATE TABLE purchase (
        id INTEGER NOT NULL,
        date_created DATETIME,
        date_modified DATETIME,
        account_id INTEGER NOT NULL,
        product_id INTEGER NOT NULL,
        PRIMARY KEY (id),
        FOREIGN KEY(account_id) REFERENCES account (id),
        FOREIGN KEY(product_id) REFERENCES product (id)
)
```

Sovelluksessa olevat itse tehdyt kyselyt (löytyvät purchases-kansion models-tiedostosta) ovat seuraavat:


```

SELECT COUNT(purchase.account_id), name, purchase.account_id FROM purchase INNER JOIN account on account_id = purchase.account_id GROUP BY purchase.account_id LIMIT 5;
 
```
```

SELECT COUNT(purchase.product_id), name, purchase.product_id FROM purchase INNER JOIN product on product_id = purchase.product_id GROUP BY purchase.product_id;

```





