import json

from django.contrib.auth import get_user_model

from users.models import Profile

u = """
[
    {

      
      
        "is_staff": true,
        "is_active": true,
        "date_joined": "2021-05-30T12:34:34.709Z",
        "is_patient": false,
        "is_authorized_party": false,
        "is_clinic_staff": false,
        "first_name": "George",
        "middle_name": "",
        "last_name": "Washington",
        "suffix": "",
        "password": "RzMdsJLufx2FvVi",
        "username": "george.washington",
        "email": "george.washington@us.presidents.com"
      }
    ,
    {

      
      
        "is_staff": true,
        "is_active": true,
        "date_joined": "2021-05-30T12:34:34.709Z",
        "is_patient": false,
        "is_authorized_party": false,
        "is_clinic_staff": false,
        "first_name": "John",
        "middle_name": "",
        "last_name": "Adams",
        "suffix": "Jr",
        "password": "RzMdsJLufx2FvVi",
        "username": "john.adams.jr",
        "email": "john.adams.jr@us.presidents.com"
      }
    ,
    {

      
      
        "is_staff": true,
        "is_active": true,
        "date_joined": "2021-05-30T12:34:34.709Z",
        "is_patient": false,
        "is_authorized_party": false,
        "is_clinic_staff": false,
        "first_name": "Thomas",
        "middle_name": "",
        "last_name": "Jefferson",
        "suffix": "",
        "password": "RzMdsJLufx2FvVi",
        "username": "thomas.jefferson",
        "email": "thomas.jefferson@us.presidents.com"
      }
    ,
    {

      
      
        "is_staff": true,
        "is_active": true,
        "date_joined": "2021-05-30T12:34:34.709Z",
        "is_patient": false,
        "is_authorized_party": false,
        "is_clinic_staff": false,
        "first_name": "James",
        "middle_name": "",
        "last_name": "Madison",
        "suffix": "Jr",
        "password": "RzMdsJLufx2FvVi",
        "username": "james.madison.jr",
        "email": "james.madison.jr@us.presidents.com"
      }
    ,
    {

      
      
        "is_staff": true,
        "is_active": true,
        "date_joined": "2021-05-30T12:34:34.709Z",
        "is_patient": false,
        "is_authorized_party": false,
        "is_clinic_staff": false,
        "first_name": "James",
        "middle_name": "",
        "last_name": "Monroe",
        "suffix": "",
        "password": "RzMdsJLufx2FvVi",
        "username": "james.monroe",
        "email": "james.monroe@us.presidents.com"
      }
    ,
    {

      
      
        "is_staff": true,
        "is_active": true,
        "date_joined": "2021-05-30T12:34:34.709Z",
        "is_patient": false,
        "is_authorized_party": false,
        "is_clinic_staff": false,
        "first_name": "John",
        "middle_name": "Quincy",
        "last_name": "Adams",
        "suffix": "",
        "password": "RzMdsJLufx2FvVi",
        "username": "john.quincy.adams",
        "email": "john.quincy.adams@us.presidents.com"
      }
    ,
    {

      
      
        "is_staff": true,
        "is_active": true,
        "date_joined": "2021-05-30T12:34:34.709Z",
        "is_patient": false,
        "is_authorized_party": false,
        "is_clinic_staff": false,
        "first_name": "Andrew",
        "middle_name": "",
        "last_name": "Jackson",
        "suffix": "",
        "password": "RzMdsJLufx2FvVi",
        "username": "andrew.jackson",
        "email": "andrew.jackson@us.presidents.com"
      }
    ,
    {

      
      
        "is_staff": true,
        "is_active": true,
        "date_joined": "2021-05-30T12:34:34.709Z",
        "is_patient": false,
        "is_authorized_party": false,
        "is_clinic_staff": false,
        "first_name": "Martin",
        "middle_name": "",
        "last_name": "Van Buren",
        "suffix": "",
        "password": "RzMdsJLufx2FvVi",
        "username": "martin.van buren",
        "email": "martin.van buren@us.presidents.com"
      }
    ,
    {

      
      
        "is_staff": true,
        "is_active": true,
        "date_joined": "2021-05-30T12:34:34.709Z",
        "is_patient": false,
        "is_authorized_party": false,
        "is_clinic_staff": false,
        "first_name": "William",
        "middle_name": "Henry",
        "last_name": "Harrison",
        "suffix": "",
        "password": "RzMdsJLufx2FvVi",
        "username": "william.henry.harrison",
        "email": "william.henry.harrison@us.presidents.com"
      }
    ,
    {

      
      
        "is_staff": true,
        "is_active": true,
        "date_joined": "2021-05-30T12:34:34.709Z",
        "is_patient": false,
        "is_authorized_party": false,
        "is_clinic_staff": false,
        "first_name": "John",
        "middle_name": "",
        "last_name": "Tyler",
        "suffix": "",
        "password": "RzMdsJLufx2FvVi",
        "username": "john.tyler",
        "email": "john.tyler@us.presidents.com"
      }
    ,
    {

      
      
        "is_staff": true,
        "is_active": true,
        "date_joined": "2021-05-30T12:34:34.709Z",
        "is_patient": false,
        "is_authorized_party": false,
        "is_clinic_staff": false,
        "first_name": "James",
        "middle_name": "Knox",
        "last_name": "Polk",
        "suffix": "",
        "password": "RzMdsJLufx2FvVi",
        "username": "james.knox.polk",
        "email": "james.knox.polk@us.presidents.com"
      }
    ,
    {

      
      
        "is_staff": true,
        "is_active": true,
        "date_joined": "2021-05-30T12:34:34.709Z",
        "is_patient": false,
        "is_authorized_party": false,
        "is_clinic_staff": false,
        "first_name": "Zachary",
        "middle_name": "",
        "last_name": "Taylor",
        "suffix": "",
        "password": "RzMdsJLufx2FvVi",
        "username": "zachary.taylor",
        "email": "zachary.taylor@us.presidents.com"
      }
    ,
    {

      
      
        "is_staff": true,
        "is_active": true,
        "date_joined": "2021-05-30T12:34:34.709Z",
        "is_patient": false,
        "is_authorized_party": false,
        "is_clinic_staff": false,
        "first_name": "Millard",
        "middle_name": "",
        "last_name": "Fillmore",
        "suffix": "",
        "password": "RzMdsJLufx2FvVi",
        "username": "millard.fillmore",
        "email": "millard.fillmore@us.presidents.com"
      }
    ,
    {

      
      
        "is_staff": true,
        "is_active": true,
        "date_joined": "2021-05-30T12:34:34.709Z",
        "is_patient": false,
        "is_authorized_party": false,
        "is_clinic_staff": false,
        "first_name": "Franklin",
        "middle_name": "",
        "last_name": "Pierce",
        "suffix": "",
        "password": "RzMdsJLufx2FvVi",
        "username": "franklin.pierce",
        "email": "franklin.pierce@us.presidents.com"
      }
    ,
    {

      
      
        "is_staff": true,
        "is_active": true,
        "date_joined": "2021-05-30T12:34:34.709Z",
        "is_patient": false,
        "is_authorized_party": false,
        "is_clinic_staff": false,
        "first_name": "James",
        "middle_name": "",
        "last_name": "Buchanan",
        "suffix": "Jr",
        "password": "RzMdsJLufx2FvVi",
        "username": "james.buchanan.jr",
        "email": "james.buchanan.jr@us.presidents.com"
      }
    ,
    {

      
      
        "is_staff": true,
        "is_active": true,
        "date_joined": "2021-05-30T12:34:34.709Z",
        "is_patient": false,
        "is_authorized_party": false,
        "is_clinic_staff": false,
        "first_name": "Abraham",
        "middle_name": "",
        "last_name": "Lincoln",
        "suffix": "",
        "password": "RzMdsJLufx2FvVi",
        "username": "abraham.lincoln",
        "email": "abraham.lincoln@us.presidents.com"
      }
    ,
    {

      
      
        "is_staff": true,
        "is_active": true,
        "date_joined": "2021-05-30T12:34:34.709Z",
        "is_patient": false,
        "is_authorized_party": false,
        "is_clinic_staff": false,
        "first_name": "Andrew",
        "middle_name": "",
        "last_name": "Johnson",
        "suffix": "",
        "password": "RzMdsJLufx2FvVi",
        "username": "andrew.johnson",
        "email": "andrew.johnson@us.presidents.com"
      }
    ,
    {

      
      
        "is_staff": true,
        "is_active": true,
        "date_joined": "2021-05-30T12:34:34.709Z",
        "is_patient": false,
        "is_authorized_party": false,
        "is_clinic_staff": false,
        "first_name": "Hiram",
        "middle_name": "Ulysses",
        "last_name": "Grant",
        "suffix": "",
        "password": "RzMdsJLufx2FvVi",
        "username": "hiram.ulysses.grant",
        "email": "hiram.ulysses.grant@us.presidents.com"
      }
    ,
    {

      
      
        "is_staff": true,
        "is_active": true,
        "date_joined": "2021-05-30T12:34:34.709Z",
        "is_patient": false,
        "is_authorized_party": false,
        "is_clinic_staff": false,
        "first_name": "Rutherford",
        "middle_name": "Birchard",
        "last_name": "Hayes",
        "suffix": "",
        "password": "RzMdsJLufx2FvVi",
        "username": "rutherford.birchard.hayes",
        "email": "rutherford.birchard.hayes@us.presidents.com"
      }
    ,
    {

      
      
        "is_staff": true,
        "is_active": true,
        "date_joined": "2021-05-30T12:34:34.709Z",
        "is_patient": false,
        "is_authorized_party": false,
        "is_clinic_staff": false,
        "first_name": "James",
        "middle_name": "Abram",
        "last_name": "Garfield",
        "suffix": "",
        "password": "RzMdsJLufx2FvVi",
        "username": "james.abram.garfield",
        "email": "james.abram.garfield@us.presidents.com"
      }
    ,
    {

      
      
        "is_staff": true,
        "is_active": true,
        "date_joined": "2021-05-30T12:34:34.709Z",
        "is_patient": false,
        "is_authorized_party": false,
        "is_clinic_staff": false,
        "first_name": "Chester",
        "middle_name": "Alan",
        "last_name": "Arthur",
        "suffix": "",
        "password": "RzMdsJLufx2FvVi",
        "username": "chester.alan.arthur",
        "email": "chester.alan.arthur@us.presidents.com"
      }
    ,
    {

      
      
        "is_staff": true,
        "is_active": true,
        "date_joined": "2021-05-30T12:34:34.709Z",
        "is_patient": false,
        "is_authorized_party": false,
        "is_clinic_staff": false,
        "first_name": "Stephen",
        "middle_name": "Grover",
        "last_name": "Cleveland",
        "suffix": "",
        "password": "RzMdsJLufx2FvVi",
        "username": "stephen.grover.cleveland",
        "email": "stephen.grover.cleveland@us.presidents.com"
      }
    ,
    {

      
      
        "is_staff": true,
        "is_active": true,
        "date_joined": "2021-05-30T12:34:34.709Z",
        "is_patient": false,
        "is_authorized_party": false,
        "is_clinic_staff": false,
        "first_name": "Benjamin",
        "middle_name": "",
        "last_name": "Harrison",
        "suffix": "",
        "password": "RzMdsJLufx2FvVi",
        "username": "benjamin.harrison",
        "email": "benjamin.harrison@us.presidents.com"
      }
    ,
    {

      
      
        "is_staff": true,
        "is_active": true,
        "date_joined": "2021-05-30T12:34:34.709Z",
        "is_patient": false,
        "is_authorized_party": false,
        "is_clinic_staff": false,
        "first_name": "William",
        "middle_name": "",
        "last_name": "McKinley",
        "suffix": "",
        "password": "RzMdsJLufx2FvVi",
        "username": "william.mckinley",
        "email": "william.mckinley@us.presidents.com"
      }
    ,
    {

      
      
        "is_staff": true,
        "is_active": true,
        "date_joined": "2021-05-30T12:34:34.709Z",
        "is_patient": false,
        "is_authorized_party": false,
        "is_clinic_staff": false,
        "first_name": "Stephen",
        "middle_name": "Grover",
        "last_name": "Cleveland.twice",
        "suffix": "",
        "password": "RzMdsJLufx2FvVi",
        "username": "stephen.grover.cleveland.twice",
        "email": "stephen.grover.cleveland.twice@us.presidents.com"
      }
    ,
    {

      
      
        "is_staff": true,
        "is_active": true,
        "date_joined": "2021-05-30T12:34:34.709Z",
        "is_patient": false,
        "is_authorized_party": false,
        "is_clinic_staff": false,
        "first_name": "Theodore",
        "middle_name": "",
        "last_name": "Roosevelt",
        "suffix": "Jr",
        "password": "RzMdsJLufx2FvVi",
        "username": "theodore.roosevelt.jr",
        "email": "theodore.roosevelt.jr@us.presidents.com"
      }
    ,
    {

      
      
        "is_staff": true,
        "is_active": true,
        "date_joined": "2021-05-30T12:34:34.709Z",
        "is_patient": false,
        "is_authorized_party": false,
        "is_clinic_staff": false,
        "first_name": "William",
        "middle_name": "Howard",
        "last_name": "Taft",
        "suffix": "",
        "password": "RzMdsJLufx2FvVi",
        "username": "william.howard.taft",
        "email": "william.howard.taft@us.presidents.com"
      }
    ,
    {

      
      
        "is_staff": true,
        "is_active": true,
        "date_joined": "2021-05-30T12:34:34.709Z",
        "is_patient": false,
        "is_authorized_party": false,
        "is_clinic_staff": false,
        "first_name": "Thomas",
        "middle_name": "Woodrow",
        "last_name": "Wilson",
        "suffix": "",
        "password": "RzMdsJLufx2FvVi",
        "username": "thomas.woodrow.wilson",
        "email": "thomas.woodrow.wilson@us.presidents.com"
      }
    ,
    {

      
      
        "is_staff": true,
        "is_active": true,
        "date_joined": "2021-05-30T12:34:34.709Z",
        "is_patient": false,
        "is_authorized_party": false,
        "is_clinic_staff": false,
        "first_name": "Warren",
        "middle_name": "Gamaliel",
        "last_name": "Harding",
        "suffix": "",
        "password": "RzMdsJLufx2FvVi",
        "username": "warren.gamaliel.harding",
        "email": "warren.gamaliel.harding@us.presidents.com"
      }
    ,
    {

      
      
        "is_staff": true,
        "is_active": true,
        "date_joined": "2021-05-30T12:34:34.709Z",
        "is_patient": false,
        "is_authorized_party": false,
        "is_clinic_staff": false,
        "first_name": "John",
        "middle_name": "Calvin",
        "last_name": "Coolidge",
        "suffix": "Jr",
        "password": "RzMdsJLufx2FvVi",
        "username": "john.calvin.coolidge.jr",
        "email": "john.calvin.coolidge.jr@us.presidents.com"
      }
    ,
    {

      
      
        "is_staff": true,
        "is_active": true,
        "date_joined": "2021-05-30T12:34:34.709Z",
        "is_patient": false,
        "is_authorized_party": false,
        "is_clinic_staff": false,
        "first_name": "Herbert",
        "middle_name": "Clark",
        "last_name": "Hoover",
        "suffix": "",
        "password": "RzMdsJLufx2FvVi",
        "username": "herbert.clark.hoover",
        "email": "herbert.clark.hoover@us.presidents.com"
      }
    ,
    {

      
      
        "is_staff": true,
        "is_active": true,
        "date_joined": "2021-05-30T12:34:34.709Z",
        "is_patient": false,
        "is_authorized_party": false,
        "is_clinic_staff": false,
        "first_name": "Franklin",
        "middle_name": "Delano",
        "last_name": "Roosevelt",
        "suffix": "",
        "password": "RzMdsJLufx2FvVi",
        "username": "franklin.delano.roosevelt",
        "email": "franklin.delano.roosevelt@us.presidents.com"
      }
    ,
    {

      
      
        "is_staff": true,
        "is_active": true,
        "date_joined": "2021-05-30T12:34:34.709Z",
        "is_patient": false,
        "is_authorized_party": false,
        "is_clinic_staff": false,
        "first_name": "Harry",
        "middle_name": "S",
        "last_name": "Truman",
        "suffix": "",
        "password": "RzMdsJLufx2FvVi",
        "username": "harry.s.truman",
        "email": "harry.s.truman@us.presidents.com"
      }
    ,
    {

      
      
        "is_staff": true,
        "is_active": true,
        "date_joined": "2021-05-30T12:34:34.709Z",
        "is_patient": false,
        "is_authorized_party": false,
        "is_clinic_staff": false,
        "first_name": "Dwight",
        "middle_name": "David",
        "last_name": "Eisenhower",
        "suffix": "",
        "password": "RzMdsJLufx2FvVi",
        "username": "dwight.david.eisenhower",
        "email": "dwight.david.eisenhower@us.presidents.com"
      }
    ,
    {

      
      
        "is_staff": true,
        "is_active": true,
        "date_joined": "2021-05-30T12:34:34.709Z",
        "is_patient": false,
        "is_authorized_party": false,
        "is_clinic_staff": false,
        "first_name": "John",
        "middle_name": "Fitzgerald",
        "last_name": "Kennedy",
        "suffix": "",
        "password": "RzMdsJLufx2FvVi",
        "username": "john.fitzgerald.kennedy",
        "email": "john.fitzgerald.kennedy@us.presidents.com"
      }
    ,
    {

      
      
        "is_staff": true,
        "is_active": true,
        "date_joined": "2021-05-30T12:34:34.709Z",
        "is_patient": false,
        "is_authorized_party": false,
        "is_clinic_staff": false,
        "first_name": "Lyndon",
        "middle_name": "Baines",
        "last_name": "Johnson",
        "suffix": "",
        "password": "RzMdsJLufx2FvVi",
        "username": "lyndon.baines.johnson",
        "email": "lyndon.baines.johnson@us.presidents.com"
      }
    ,
    {

      
      
        "is_staff": true,
        "is_active": true,
        "date_joined": "2021-05-30T12:34:34.709Z",
        "is_patient": false,
        "is_authorized_party": false,
        "is_clinic_staff": false,
        "first_name": "Richard",
        "middle_name": "Milhous",
        "last_name": "Nixon",
        "suffix": "",
        "password": "RzMdsJLufx2FvVi",
        "username": "richard.milhous.nixon",
        "email": "richard.milhous.nixon@us.presidents.com"
      }
    ,
    {

      
      
        "is_staff": true,
        "is_active": true,
        "date_joined": "2021-05-30T12:34:34.709Z",
        "is_patient": false,
        "is_authorized_party": false,
        "is_clinic_staff": false,
        "first_name": "Leslie",
        "middle_name": "Lynch",
        "last_name": "King",
        "suffix": "Jr",
        "password": "RzMdsJLufx2FvVi",
        "username": "leslie.lynch.king.jr",
        "email": "leslie.lynch.king.jr@us.presidents.com"
      }
    ,
    {

      
      
        "is_staff": true,
        "is_active": true,
        "date_joined": "2021-05-30T12:34:34.709Z",
        "is_patient": false,
        "is_authorized_party": false,
        "is_clinic_staff": false,
        "first_name": "James",
        "middle_name": "Earl",
        "last_name": "Carter",
        "suffix": "Jr",
        "password": "RzMdsJLufx2FvVi",
        "username": "james.earl.carter.jr",
        "email": "james.earl.carter.jr@us.presidents.com"
      }
    ,
    {

      
      
        "is_staff": true,
        "is_active": true,
        "date_joined": "2021-05-30T12:34:34.709Z",
        "is_patient": false,
        "is_authorized_party": false,
        "is_clinic_staff": false,
        "first_name": "Ronald",
        "date_of_death":"2004-06-05",
        "middle_name": "Wilson",
        "last_name": "Reagan",
        "suffix": "",
        "password": "RzMdsJLufx2FvVi",
        "username": "ronald.wilson.reagan",
        "email": "ronald.wilson.reagan@us.presidents.com"
      }
    ,
    {

      
      
        "is_staff": true,
        "is_active": true,
        "date_joined": "2021-05-30T12:34:34.709Z",
        "is_patient": false,
        "is_authorized_party": false,
        "is_clinic_staff": false,
        "first_name": "George",
        "middle_name": "Herbert Walker",
        "last_name": "Bush",
        "suffix": "",
        "password": "RzMdsJLufx2FvVi",
        "username": "george.herbert walker.bush",
        "email": "george.herbert walker.bush@us.presidents.com"
      }
    ,
    {

      
      
        "is_staff": true,
        "is_active": true,
        "date_joined": "2021-05-30T12:34:34.709Z",
        "is_patient": false,
        "is_authorized_party": false,
        "is_clinic_staff": false,
        "first_name": "William",
        "middle_name": "Jefferson",
        "last_name": "Clinton",
        "suffix": "",
        "password": "RzMdsJLufx2FvVi",
        "username": "william.jefferson.clinton",
        "email": "william.jefferson.clinton@us.presidents.com"
      }
    ,
    {

      
      
        "is_staff": true,
        "is_active": true,
        "date_joined": "2021-05-30T12:34:34.709Z",
        "is_patient": false,
        "is_authorized_party": false,
        "is_clinic_staff": false,
        "first_name": "George",
        "middle_name": "Walker",
        "last_name": "Bush",
        "suffix": "",
        "password": "RzMdsJLufx2FvVi",
        "username": "george.walker.bush",
        "email": "george.walker.bush@us.presidents.com"
      }
    ,
    {

      
      
        "is_staff": true,
        "is_active": true,
        "date_joined": "2021-05-30T12:34:34.709Z",
        "is_patient": false,
        "is_authorized_party": false,
        "is_clinic_staff": false,
        "first_name": "Barack",
        "middle_name": "Hussein",
        "last_name": "Obama",
        "suffix": "II",
        "password": "RzMdsJLufx2FvVi",
        "username": "barack.hussein.obama.ii",
        "email": "barack.hussein.obama.ii@us.presidents.com"
      }
    ,
    {

      
      
        "is_staff": true,
        "is_active": true,
        "date_joined": "2021-05-30T12:34:34.709Z",
        "is_patient": false,
        "is_authorized_party": false,
        "is_clinic_staff": false,
        "first_name": "Donald",
        "middle_name": "John",
        "last_name": "Trump",
        "suffix": "Sr",
        "password": "RzMdsJLufx2FvVi",
        "username": "donald.john.trump.sr",
        "email": "donald.john.trump.sr@us.presidents.com"
      }
    ,
    {

      
      
        "is_staff": true,
        "is_active": true,
        "date_joined": "2021-05-30T12:34:34.709Z",
        "is_patient": false,
        "is_authorized_party": false,
        "is_clinic_staff": false,
        "first_name": "Joseph",
        "middle_name": "Robinette",
        "last_name": "Biden",
        "suffix": "Jr",
        "password": "RzMdsJLufx2FvVi",
        "username": "joseph.robinette.biden.jr",
        "email": "joseph.robinette.biden.jr@us.presidents.com"
      }
    ,
    
    {
      

      
        "password":"password123!@#",
        "username": "eddard.stark",
        "first_name": "eddard",
        "email": "eddard.stark@game.of.thrones.com",
        "date_joined": "2021-06-01T22:04:08.224Z",
        "last_name": "stark",
        "middle_name": null,
        "title": null,
        "suffix": null,
        "date_of_birth": null,
        "is_patient": false,
        "is_authorized_party": false,
        "is_clinic_staff": false,
        "date_of_death": null
      }
    ,
    {
      

      
        "password":"password123!@#",
        "username": "robert.baratheon",
        "first_name": "robert",
        "email": "robert.baratheon@game.of.thrones.com",
        "date_joined": "2021-06-01T22:04:08.363Z",
        "last_name": "baratheon",
        "middle_name": null,
        "title": null,
        "suffix": null,
        "date_of_birth": null,
        "is_patient": false,
        "is_authorized_party": false,
        "is_clinic_staff": false,
        "date_of_death": null
      }
    ,
    {
      

      
        "password":"password123!@#",
        "username": "jaime.lannister",
        "first_name": "jaime",
        "email": "jaime.lannister@game.of.thrones.com",
        "date_joined": "2021-06-01T22:04:08.503Z",
        "last_name": "lannister",
        "middle_name": null,
        "title": null,
        "suffix": null,
        "date_of_birth": null,
        "is_patient": false,
        "is_authorized_party": false,
        "is_clinic_staff": false,
        "date_of_death": null
      }
    ,
    {
      

      
        "password":"password123!@#",
        "username": "catelyn.stark",
        "first_name": "catelyn",
        "email": "catelyn.stark@game.of.thrones.com",
        "date_joined": "2021-06-01T22:04:08.644Z",
        "last_name": "stark",
        "middle_name": null,
        "title": null,
        "suffix": null,
        "date_of_birth": null,
        "is_patient": false,
        "is_authorized_party": false,
        "is_clinic_staff": false,
        "date_of_death": null
      }
    ,
    {
      

      
        "password":"password123!@#",
        "username": "cersei.lannister",
        "first_name": "cersei",
        "email": "cersei.lannister@game.of.thrones.com",
        "date_joined": "2021-06-01T22:04:08.783Z",
        "last_name": "lannister",
        "middle_name": null,
        "title": null,
        "suffix": null,
        "date_of_birth": null,
        "is_patient": false,
        "is_authorized_party": false,
        "is_clinic_staff": false,
        "date_of_death": null
      }
    ,
    {
      

      
        "password":"password123!@#",
        "username": "daenerys.targaryen",
        "first_name": "daenerys",
        "email": "daenerys.targaryen@game.of.thrones.com",
        "date_joined": "2021-06-01T22:04:08.920Z",
        "last_name": "targaryen",
        "middle_name": null,
        "title": null,
        "suffix": null,
        "date_of_birth": null,
        "is_patient": false,
        "is_authorized_party": false,
        "is_clinic_staff": false,
        "date_of_death": null
      }
    ,
    {
      

      
        "password":"password123!@#",
        "username": "jorah.mormont",
        "first_name": "jorah",
        "email": "jorah.mormont@game.of.thrones.com",
        "date_joined": "2021-06-01T22:04:09.061Z",
        "last_name": "mormont",
        "middle_name": null,
        "title": null,
        "suffix": null,
        "date_of_birth": null,
        "is_patient": false,
        "is_authorized_party": false,
        "is_clinic_staff": false,
        "date_of_death": null
      }
    ,
    {
      

      
        "password":"password123!@#",
        "username": "viserys.targaryen",
        "first_name": "viserys",
        "email": "viserys.targaryen@game.of.thrones.com",
        "date_joined": "2021-06-01T22:04:09.199Z",
        "last_name": "targaryen",
        "middle_name": null,
        "title": null,
        "suffix": null,
        "date_of_birth": null,
        "is_patient": false,
        "is_authorized_party": false,
        "is_clinic_staff": false,
        "date_of_death": null
      }
    ,
    {
      

      
        "password":"password123!@#",
        "username": "jon.snow",
        "first_name": "jon",
        "email": "jon.snow@game.of.thrones.com",
        "date_joined": "2021-06-01T22:04:09.348Z",
        "last_name": "snow",
        "middle_name": null,
        "title": null,
        "suffix": null,
        "date_of_birth": null,
        "is_patient": false,
        "is_authorized_party": false,
        "is_clinic_staff": false,
        "date_of_death": null
      }
    ,
    {
      

      
        "password":"password123!@#",
        "username": "robb.stark",
        "first_name": "robb",
        "email": "robb.stark@game.of.thrones.com",
        "date_joined": "2021-06-01T22:04:09.484Z",
        "last_name": "stark",
        "middle_name": null,
        "title": null,
        "suffix": null,
        "date_of_birth": null,
        "is_patient": false,
        "is_authorized_party": false,
        "is_clinic_staff": false,
        "date_of_death": null
      }
    ,
    {
      

      
        "password":"password123!@#",
        "username": "sansa.stark",
        "first_name": "sansa",
        "email": "sansa.stark@game.of.thrones.com",
        "date_joined": "2021-06-01T22:04:09.623Z",
        "last_name": "stark",
        "middle_name": null,
        "title": null,
        "suffix": null,
        "date_of_birth": null,
        "is_patient": false,
        "is_authorized_party": false,
        "is_clinic_staff": false,
        "date_of_death": null
      }
    ,
    {
      

      
        "password":"password123!@#",
        "username": "arya.stark",
        "first_name": "arya",
        "email": "arya.stark@game.of.thrones.com",
        "date_joined": "2021-06-01T22:04:09.763Z",
        "last_name": "stark",
        "middle_name": null,
        "title": null,
        "suffix": null,
        "date_of_birth": null,
        "is_patient": false,
        "is_authorized_party": false,
        "is_clinic_staff": false,
        "date_of_death": null
      }
    ,
    {
      

      
        "password":"password123!@#",
        "username": "theon.greyjoy",
        "first_name": "theon",
        "email": "theon.greyjoy@game.of.thrones.com",
        "date_joined": "2021-06-01T22:04:09.902Z",
        "last_name": "greyjoy",
        "middle_name": null,
        "title": null,
        "suffix": null,
        "date_of_birth": null,
        "is_patient": false,
        "is_authorized_party": false,
        "is_clinic_staff": false,
        "date_of_death": null
      }
    ,
    {
      

      
        "password":"password123!@#",
        "username": "brandon.stark",
        "first_name": "brandon",
        "email": "brandon.stark@game.of.thrones.com",
        "date_joined": "2021-06-01T22:04:10.043Z",
        "last_name": "stark",
        "middle_name": null,
        "title": null,
        "suffix": null,
        "date_of_birth": null,
        "is_patient": false,
        "is_authorized_party": false,
        "is_clinic_staff": false,
        "date_of_death": null
      }
    ,
    {
      

      
        "password":"password123!@#",
        "username": "joffrey.baratheon",
        "first_name": "joffrey",
        "email": "joffrey.baratheon@game.of.thrones.com",
        "date_joined": "2021-06-01T22:04:10.183Z",
        "last_name": "baratheon",
        "middle_name": null,
        "title": null,
        "suffix": null,
        "date_of_birth": null,
        "is_patient": false,
        "is_authorized_party": false,
        "is_clinic_staff": false,
        "date_of_death": null
      }
    ,
    {
      

      
        "password":"password123!@#",
        "username": "sandor.clegane",
        "first_name": "sandor",
        "email": "sandor.clegane@game.of.thrones.com",
        "date_joined": "2021-06-01T22:04:10.328Z",
        "last_name": "clegane",
        "middle_name": null,
        "title": null,
        "suffix": null,
        "date_of_birth": null,
        "is_patient": false,
        "is_authorized_party": false,
        "is_clinic_staff": false,
        "date_of_death": null
      }
    ,
    {
      

      
        "password":"password123!@#",
        "username": "tyrion.lannister",
        "first_name": "tyrion",
        "email": "tyrion.lannister@game.of.thrones.com",
        "date_joined": "2021-06-01T22:04:10.468Z",
        "last_name": "lannister",
        "middle_name": null,
        "title": null,
        "suffix": null,
        "date_of_birth": null,
        "is_patient": false,
        "is_authorized_party": false,
        "is_clinic_staff": false,
        "date_of_death": null
      }
    ,
    {
      

      
        "password":"password123!@#",
        "username": "petyr.baelish",
        "first_name": "petyr",
        "email": "petyr.baelish@game.of.thrones.com",
        "date_joined": "2021-06-01T22:04:10.606Z",
        "last_name": "baelish",
        "middle_name": null,
        "title": null,
        "suffix": null,
        "date_of_birth": null,
        "is_patient": false,
        "is_authorized_party": false,
        "is_clinic_staff": false,
        "date_of_death": null
      }
    ,
    {
      

      
        "password":"password123!@#",
        "username": "davos.seaworth",
        "first_name": "davos",
        "email": "davos.seaworth@game.of.thrones.com",
        "date_joined": "2021-06-01T22:04:10.747Z",
        "last_name": "seaworth",
        "middle_name": null,
        "title": null,
        "suffix": null,
        "date_of_birth": null,
        "is_patient": false,
        "is_authorized_party": false,
        "is_clinic_staff": false,
        "date_of_death": null
      }
    ,
    {
      

      
        "password":"password123!@#",
        "username": "samwell.tarly",
        "first_name": "samwell",
        "email": "samwell.tarly@game.of.thrones.com",
        "date_joined": "2021-06-01T22:04:10.888Z",
        "last_name": "tarly",
        "middle_name": null,
        "title": null,
        "suffix": null,
        "date_of_birth": null,
        "is_patient": false,
        "is_authorized_party": false,
        "is_clinic_staff": false,
        "date_of_death": null
      }
    ,
    {
      

      
        "password":"password123!@#",
        "username": "stannis.baratheon",
        "first_name": "stannis",
        "email": "stannis.baratheon@game.of.thrones.com",
        "date_joined": "2021-06-01T22:04:11.030Z",
        "last_name": "baratheon",
        "middle_name": null,
        "title": null,
        "suffix": null,
        "date_of_birth": null,
        "is_patient": false,
        "is_authorized_party": false,
        "is_clinic_staff": false,
        "date_of_death": null
      }
    ,
    {
      

      
        "password":"password123!@#",
        "username": "jeor.mormont",
        "first_name": "jeor",
        "email": "jeor.mormont@game.of.thrones.com",
        "date_joined": "2021-06-01T22:04:11.170Z",
        "last_name": "mormont",
        "middle_name": null,
        "title": null,
        "suffix": null,
        "date_of_birth": null,
        "is_patient": false,
        "is_authorized_party": false,
        "is_clinic_staff": false,
        "date_of_death": null
      }
    ,
    {
      

      
        "password":"password123!@#",
        "username": "margaery.tyrell",
        "first_name": "margaery",
        "email": "margaery.tyrell@game.of.thrones.com",
        "date_joined": "2021-06-01T22:04:11.310Z",
        "last_name": "tyrell",
        "middle_name": null,
        "title": null,
        "suffix": null,
        "date_of_birth": null,
        "is_patient": false,
        "is_authorized_party": false,
        "is_clinic_staff": false,
        "date_of_death": null
      }
    ,
    {
      

      
        "password":"password123!@#",
        "username": "tywin.lannister",
        "first_name": "tywin",
        "email": "tywin.lannister@game.of.thrones.com",
        "date_joined": "2021-06-01T22:04:11.456Z",
        "last_name": "lannister",
        "middle_name": null,
        "title": null,
        "suffix": null,
        "date_of_birth": null,
        "is_patient": false,
        "is_authorized_party": false,
        "is_clinic_staff": false,
        "date_of_death": null
      }
    ,
    {
      

      
        "password":"password123!@#",
        "username": "talisa.maegyr",
        "first_name": "talisa",
        "email": "talisa.maegyr@game.of.thrones.com",
        "date_joined": "2021-06-01T22:04:11.594Z",
        "last_name": "maegyr",
        "middle_name": null,
        "title": null,
        "suffix": null,
        "date_of_birth": null,
        "is_patient": false,
        "is_authorized_party": false,
        "is_clinic_staff": false,
        "date_of_death": null
      }
    ,
    {
      

      
        "password":"password123!@#",
        "username": "tormund.giantsbane",
        "first_name": "tormund",
        "email": "tormund.giantsbane@game.of.thrones.com",
        "date_joined": "2021-06-01T22:04:11.734Z",
        "last_name": "giantsbane",
        "middle_name": null,
        "title": null,
        "suffix": null,
        "date_of_birth": null,
        "is_patient": false,
        "is_authorized_party": false,
        "is_clinic_staff": false,
        "date_of_death": null
      }
    ,
    {
      

      
        "password":"password123!@#",
        "username": "brienne.detarth",
        "first_name": "brienne",
        "email": "brienne.detarth@game.of.thrones.com",
        "date_joined": "2021-06-01T22:04:11.870Z",
        "last_name": "detarth",
        "middle_name": null,
        "title": null,
        "suffix": null,
        "date_of_birth": null,
        "is_patient": false,
        "is_authorized_party": false,
        "is_clinic_staff": false,
        "date_of_death": null
      }
    ,
    {
      

      
        "password":"password123!@#",
        "username": "ramsay.bolton",
        "first_name": "ramsay",
        "email": "ramsay.bolton@game.of.thrones.com",
        "date_joined": "2021-06-01T22:04:12.014Z",
        "last_name": "bolton",
        "middle_name": null,
        "title": null,
        "suffix": null,
        "date_of_birth": null,
        "is_patient": false,
        "is_authorized_party": false,
        "is_clinic_staff": false,
        "date_of_death": null
      }
    ,
    {
      

      
        "password":"password123!@#",
        "username": "daario.naharis",
        "first_name": "daario",
        "email": "daario.naharis@game.of.thrones.com",
        "date_joined": "2021-06-01T22:04:12.152Z",
        "last_name": "naharis",
        "middle_name": null,
        "title": null,
        "suffix": null,
        "date_of_birth": null,
        "is_patient": false,
        "is_authorized_party": false,
        "is_clinic_staff": false,
        "date_of_death": null
      }
    ,
    {
      

      
        "password":"password123!@#",
        "username": "ellaria.sand",
        "first_name": "ellaria",
        "email": "ellaria.sand@game.of.thrones.com",
        "date_joined": "2021-06-01T22:04:12.294Z",
        "last_name": "sand",
        "middle_name": null,
        "title": null,
        "suffix": null,
        "date_of_birth": null,
        "is_patient": false,
        "is_authorized_party": false,
        "is_clinic_staff": false,
        "date_of_death": null
      }
    ,
    {
      

      
        "password":"password123!@#",
        "username": "tommen.baratheon",
        "first_name": "tommen",
        "email": "tommen.baratheon@game.of.thrones.com",
        "date_joined": "2021-06-01T22:04:12.440Z",
        "last_name": "baratheon",
        "middle_name": null,
        "title": null,
        "suffix": null,
        "date_of_birth": null,
        "is_patient": false,
        "is_authorized_party": false,
        "is_clinic_staff": false,
        "date_of_death": null
      }
    ,
    {
      

      
        "password":"password123!@#",
        "username": "jaqen.hghar",
        "first_name": "jaqen",
        "email": "jaqen.hghar@game.of.thrones.com",
        "date_joined": "2021-06-01T22:04:12.579Z",
        "last_name": "h'ghar",
        "middle_name": null,
        "title": null,
        "suffix": null,
        "date_of_birth": null,
        "is_patient": false,
        "is_authorized_party": false,
        "is_clinic_staff": false,
        "date_of_death": null
      }
    ,
    {
      

      
        "password":"password123!@#",
        "username": "roose.bolton",
        "first_name": "roose",
        "email": "roose.bolton@game.of.thrones.com",
        "date_joined": "2021-06-01T22:04:12.718Z",
        "last_name": "bolton",
        "middle_name": null,
        "title": null,
        "suffix": null,
        "date_of_birth": null,
        "is_patient": false,
        "is_authorized_party": false,
        "is_clinic_staff": false,
        "date_of_death": null
      }
    ,
    {
      

      
        "password":"password123!@#",
        "username": "grey.worm",
        "first_name": "grey",
        "email": "grey.worm@game.of.thrones.com",
        "date_joined": "2021-06-01T22:04:12.857Z",
        "last_name": "worm",
        "middle_name": null,
        "title": null,
        "suffix": null,
        "date_of_birth": null,
        "is_patient": false,
        "is_authorized_party": false,
        "is_clinic_staff": false,
        "date_of_death": null
      }
    ,
    {
      

      
        "password":"password123!@#",
        "username": "ichigo.kurosaki",
        "first_name": "ichigo",
        "email": "ichigo.kurosaki@soul.society.com",
        "date_joined": "2021-06-02T20:00:50.420Z",
        "last_name": "kurosaki",
        "middle_name": null,
        "title": null,
        "suffix": null,
        "date_of_birth": null,
        "is_patient": false,
        "is_authorized_party": false,
        "is_clinic_staff": false,
        "date_of_death": null
      
    }
  
  
  ]"""
users = json.loads(u)
for user in users:
    profile = Profile.objects.create(user=get_user_model().objects.create_user(user))
    profile.save()
    profile.addresses.create(
        idempotent_key="ckpfzqd7l0000nbve3vq1hfgl",
        address_type="RESD",
        street1="1600 Pennsylvania Avenue NW",
        street2="",
        state="Washington",
        city="DC",
        zipcode="20500",
    )
    profile.save()
