create table dim_fund(fund_id integer primary key autoincrement, amfi_code integer unique,
fund_name text);

create table dim_date(
    date_id integer primary key autoincrement,
    date date unique,
    year integer,
    month integer,
    day integer
);

create table fact_nav(
    nav_id integer primary key autoincrement,
    amfi_code integer,
    date date,
    nav real
);

create table fact_transactions(transaction_id integer primary key autoincrement,
investor_id text,
transaction_date date,
transaction_type text,
amount_inr real,
kyc_status text
);

create table fact_performance(
    performance_id integer primary key autoincrement,
    amfi_code integer,
    return_1y real,
    return_3y real,
    expense_ratio real
);

create table fact_aum(
    aum_id integer primary key autoincrement,
    amfi_code integer,
    month date,
    aum real
);
  