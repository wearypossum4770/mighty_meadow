use rusqlite::NO_PARAMS;
use rusqlite::{Connection, Result};
use std::collections::HashMap;

#[derive(Debug)]
struct User {
    first_name : String,
    last_name : String,
    middle_name : String,
    title : String,
    honorific_prefix : String,
    honorific_suffix : String,
    suffix : String,
    date_of_birth : String,
    is_patient : String,
    is_authorized_party : String,
    is_clinic_staff : String,
    date_of_death : String,
    retention_only : String,
    do_not_contact : String,
}

fn main() -> Result<()> {
    let conn = Connection::open("../../db.sqlite3")?;

    let mut app_users = HashMap::new();
    println!("Hello, world!");
}
