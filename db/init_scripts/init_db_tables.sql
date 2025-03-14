
CREATE TABLE Cards (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    category_sale JSON,
    interest_on_loan SMALLINT,
    category_cashback JSON,
    bank VARCHAR(255),
    rating SMALLINT
);



CREATE TABLE Users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    money INTEGER,
    cashback_importance SMALLINT
);