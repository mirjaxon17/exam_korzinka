from base import Base


def create_table():


    city = f"""
        create table city(
        city_id serial primary key ,
        country_id int references country(country_id),
        name varchar(20),
        create_date date,
        last_update timestamp default now());
        """

    adress = f"""
        create table adress(
        adress_id serial primary key ,
        city_id int references adress(adress_id),
        name varchar(20),
        create_date date,
        last_update timestamp default  now());
        """


    store = f"""
        create table store(
        store_id serial primary key ,
        name varchar(20),
        adress_id int references adress(adress_id),
        create_date date,
        last_update timestamp default now());
        """

    product = f"""
        create table product(
        product_id serial primary key,
        name varchar(20),
        description text,
        store_id int references store(store_id),
        price smallint,
        create_date date,
        last_update timestamp default now());

        """
    staff = f"""
    create table staff(
    staff_id serial primary_key,
    first_name varchar(20),
    last_name varcgar(20),
    user_name varcgar(20),
    password varchar(20),
    last_update timestamp default now());
    """

    customer = f"""
        create table customer(
        customer_id serial primary key ,
        adress_id int references adress(adress_id),
        product_id int references product(product_id),
        first_name varchar(20),
        last_name varchar(20),
        user_name varchar(20),
        password(20),
        create_date date,
        last_update timestamp default now());
        """

    payment_type = f"""
        create table payment_type(
        payment_type_id serial primary key,
        name varchar(20),
        last_update timestamp default now());
        """

    payment = f"""
        create table payment(
        payment_id serial primary key ,
        payment_type_id int references payment_type(payment_typ_id),
        product_id int references product(product_id),
        customer_id int references customer(customer_id),
        last_update timestamp default now());
        
        """
    kassa = f"""
        create table kassa(
        kassa_id serial primary key ,
        staff_id int references staff(staff_id),
        customer_id int references customer(customer_id),
        payment_type_id int references payment_type(payment_type_id),
        last_update timestamp default now());
        
        )"""
    delivery = f"""
         create table delivery(
         delivery_id serial primary key,
         product_id int references product(product_id),
         customer_id int references customer(customer_id),
         last_update timestamp default now());
         """

    data_table = {
        'city': city,
        'adress': adress,
        'store': store,
        'product': product,
        'staff':staff,
        'customer': customer,
        'payment_type': payment_type,
        'payment': payment,
        'kassa': kassa,
        'delivery': delivery

    }

    for i in data_table:
        print(f"""{i}{Base.connect(data_table[i], "create")}""")


if __name__ == '__main__':
    create_table()




