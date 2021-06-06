import json

from django.contrib.auth import get_user_model

from users.models import Profile

init = """
[
      {
    
    

      "password": "RzMdsJLufx2FvVi",
      "last_login": null,
      "is_superuser": false,
      "username": "george.washington",
      "email": "george.washington@us.presidents.com",
      "is_staff": true,
      "is_active": true,
      "date_joined": "2021-05-30T12:34:34.709Z",
      "first_name": "George",
      "last_name": "Washington",
      "middle_name": "",
      "title": null,
      "honorific_prefix": "No Selection, Declined To Answer",
      "honorific_suffix": "No Selection, Declined To Answer",
      "suffix": "",
      "date_of_birth": null,
      "is_patient": false,
      "is_authorized_party": false,
      "is_clinic_staff": false,
      "date_of_death": null,
      "retention_only": false,
      "do_not_contact": false
      

    
  },
  {
    
    

      "password": "RzMdsJLufx2FvVi",
      "last_login": null,
      "is_superuser": false,
      "username": "john.adams.jr",
      "email": "john.adams.jr@us.presidents.com",
      "is_staff": true,
      "is_active": true,
      "date_joined": "2021-05-30T12:34:34.709Z",
      "first_name": "John",
      "last_name": "Adams",
      "middle_name": "",
      "title": null,
      "honorific_prefix": "No Selection, Declined To Answer",
      "honorific_suffix": "No Selection, Declined To Answer",
      "suffix": "Jr",
      "date_of_birth": null,
      "is_patient": false,
      "is_authorized_party": false,
      "is_clinic_staff": false,
      "date_of_death": null,
      "retention_only": false,
      "do_not_contact": false
      

    
  },
  {
    
    

      "password": "RzMdsJLufx2FvVi",
      "last_login": null,
      "is_superuser": false,
      "username": "thomas.jefferson",
      "email": "thomas.jefferson@us.presidents.com",
      "is_staff": true,
      "is_active": true,
      "date_joined": "2021-05-30T12:34:34.709Z",
      "first_name": "Thomas",
      "last_name": "Jefferson",
      "middle_name": "",
      "title": null,
      "honorific_prefix": "No Selection, Declined To Answer",
      "honorific_suffix": "No Selection, Declined To Answer",
      "suffix": "",
      "date_of_birth": null,
      "is_patient": false,
      "is_authorized_party": false,
      "is_clinic_staff": false,
      "date_of_death": null,
      "retention_only": false,
      "do_not_contact": false
      

    
  },
  {
    
    

      "password": "RzMdsJLufx2FvVi",
      "last_login": null,
      "is_superuser": false,
      "username": "james.madison.jr",
      "email": "james.madison.jr@us.presidents.com",
      "is_staff": true,
      "is_active": true,
      "date_joined": "2021-05-30T12:34:34.709Z",
      "first_name": "James",
      "last_name": "Madison",
      "middle_name": "",
      "title": null,
      "honorific_prefix": "No Selection, Declined To Answer",
      "honorific_suffix": "No Selection, Declined To Answer",
      "suffix": "Jr",
      "date_of_birth": null,
      "is_patient": false,
      "is_authorized_party": false,
      "is_clinic_staff": false,
      "date_of_death": null,
      "retention_only": false,
      "do_not_contact": false
      

    
  },
  {
    
    

      "password": "RzMdsJLufx2FvVi",
      "last_login": null,
      "is_superuser": false,
      "username": "james.monroe",
      "email": "james.monroe@us.presidents.com",
      "is_staff": true,
      "is_active": true,
      "date_joined": "2021-05-30T12:34:34.709Z",
      "first_name": "James",
      "last_name": "Monroe",
      "middle_name": "",
      "title": null,
      "honorific_prefix": "No Selection, Declined To Answer",
      "honorific_suffix": "No Selection, Declined To Answer",
      "suffix": "",
      "date_of_birth": null,
      "is_patient": false,
      "is_authorized_party": false,
      "is_clinic_staff": false,
      "date_of_death": null,
      "retention_only": false,
      "do_not_contact": false
      

    
  },
  {
    
    

      "password": "RzMdsJLufx2FvVi",
      "last_login": null,
      "is_superuser": false,
      "username": "john.quincy.adams",
      "email": "john.quincy.adams@us.presidents.com",
      "is_staff": true,
      "is_active": true,
      "date_joined": "2021-05-30T12:34:34.709Z",
      "first_name": "John",
      "last_name": "Adams",
      "middle_name": "Quincy",
      "title": null,
      "honorific_prefix": "No Selection, Declined To Answer",
      "honorific_suffix": "No Selection, Declined To Answer",
      "suffix": "",
      "date_of_birth": null,
      "is_patient": false,
      "is_authorized_party": false,
      "is_clinic_staff": false,
      "date_of_death": null,
      "retention_only": false,
      "do_not_contact": false
      

    
  },
  {
    
    

      "password": "RzMdsJLufx2FvVi",
      "last_login": null,
      "is_superuser": false,
      "username": "andrew.jackson",
      "email": "andrew.jackson@us.presidents.com",
      "is_staff": true,
      "is_active": true,
      "date_joined": "2021-05-30T12:34:34.709Z",
      "first_name": "Andrew",
      "last_name": "Jackson",
      "middle_name": "",
      "title": null,
      "honorific_prefix": "No Selection, Declined To Answer",
      "honorific_suffix": "No Selection, Declined To Answer",
      "suffix": "",
      "date_of_birth": null,
      "is_patient": false,
      "is_authorized_party": false,
      "is_clinic_staff": false,
      "date_of_death": null,
      "retention_only": false,
      "do_not_contact": false
      

    
  },
  {
    
    

      "password": "RzMdsJLufx2FvVi",
      "last_login": null,
      "is_superuser": false,
      "username": "martin.van buren",
      "email": "martin.van buren@us.presidents.com",
      "is_staff": true,
      "is_active": true,
      "date_joined": "2021-05-30T12:34:34.709Z",
      "first_name": "Martin",
      "last_name": "Van Buren",
      "middle_name": "",
      "title": null,
      "honorific_prefix": "No Selection, Declined To Answer",
      "honorific_suffix": "No Selection, Declined To Answer",
      "suffix": "",
      "date_of_birth": null,
      "is_patient": false,
      "is_authorized_party": false,
      "is_clinic_staff": false,
      "date_of_death": null,
      "retention_only": false,
      "do_not_contact": false
      

    
  },
  {
    
    

      "password": "RzMdsJLufx2FvVi",
      "last_login": null,
      "is_superuser": false,
      "username": "william.henry.harrison",
      "email": "william.henry.harrison@us.presidents.com",
      "is_staff": true,
      "is_active": true,
      "date_joined": "2021-05-30T12:34:34.709Z",
      "first_name": "William",
      "last_name": "Harrison",
      "middle_name": "Henry",
      "title": null,
      "honorific_prefix": "No Selection, Declined To Answer",
      "honorific_suffix": "No Selection, Declined To Answer",
      "suffix": "",
      "date_of_birth": null,
      "is_patient": false,
      "is_authorized_party": false,
      "is_clinic_staff": false,
      "date_of_death": null,
      "retention_only": false,
      "do_not_contact": false
      

    
  },
  {
    
    

      "password": "RzMdsJLufx2FvVi",
      "last_login": null,
      "is_superuser": false,
      "username": "john.tyler",
      "email": "john.tyler@us.presidents.com",
      "is_staff": true,
      "is_active": true,
      "date_joined": "2021-05-30T12:34:34.709Z",
      "first_name": "John",
      "last_name": "Tyler",
      "middle_name": "",
      "title": null,
      "honorific_prefix": "No Selection, Declined To Answer",
      "honorific_suffix": "No Selection, Declined To Answer",
      "suffix": "",
      "date_of_birth": null,
      "is_patient": false,
      "is_authorized_party": false,
      "is_clinic_staff": false,
      "date_of_death": null,
      "retention_only": false,
      "do_not_contact": false
      

    
  },
  {
    
    

      "password": "RzMdsJLufx2FvVi",
      "last_login": null,
      "is_superuser": false,
      "username": "james.knox.polk",
      "email": "james.knox.polk@us.presidents.com",
      "is_staff": true,
      "is_active": true,
      "date_joined": "2021-05-30T12:34:34.709Z",
      "first_name": "James",
      "last_name": "Polk",
      "middle_name": "Knox",
      "title": null,
      "honorific_prefix": "No Selection, Declined To Answer",
      "honorific_suffix": "No Selection, Declined To Answer",
      "suffix": "",
      "date_of_birth": null,
      "is_patient": false,
      "is_authorized_party": false,
      "is_clinic_staff": false,
      "date_of_death": null,
      "retention_only": false,
      "do_not_contact": false
      

    
  },
  {
    
    

      "password": "RzMdsJLufx2FvVi",
      "last_login": null,
      "is_superuser": false,
      "username": "zachary.taylor",
      "email": "zachary.taylor@us.presidents.com",
      "is_staff": true,
      "is_active": true,
      "date_joined": "2021-05-30T12:34:34.709Z",
      "first_name": "Zachary",
      "last_name": "Taylor",
      "middle_name": "",
      "title": null,
      "honorific_prefix": "No Selection, Declined To Answer",
      "honorific_suffix": "No Selection, Declined To Answer",
      "suffix": "",
      "date_of_birth": null,
      "is_patient": false,
      "is_authorized_party": false,
      "is_clinic_staff": false,
      "date_of_death": null,
      "retention_only": false,
      "do_not_contact": false
      

    
  },
  {
    
    

      "password": "RzMdsJLufx2FvVi",
      "last_login": null,
      "is_superuser": false,
      "username": "millard.fillmore",
      "email": "millard.fillmore@us.presidents.com",
      "is_staff": true,
      "is_active": true,
      "date_joined": "2021-05-30T12:34:34.709Z",
      "first_name": "Millard",
      "last_name": "Fillmore",
      "middle_name": "",
      "title": null,
      "honorific_prefix": "No Selection, Declined To Answer",
      "honorific_suffix": "No Selection, Declined To Answer",
      "suffix": "",
      "date_of_birth": null,
      "is_patient": false,
      "is_authorized_party": false,
      "is_clinic_staff": false,
      "date_of_death": null,
      "retention_only": false,
      "do_not_contact": false
      

    
  },
  {
    
    

      "password": "RzMdsJLufx2FvVi",
      "last_login": null,
      "is_superuser": false,
      "username": "franklin.pierce",
      "email": "franklin.pierce@us.presidents.com",
      "is_staff": true,
      "is_active": true,
      "date_joined": "2021-05-30T12:34:34.709Z",
      "first_name": "Franklin",
      "last_name": "Pierce",
      "middle_name": "",
      "title": null,
      "honorific_prefix": "No Selection, Declined To Answer",
      "honorific_suffix": "No Selection, Declined To Answer",
      "suffix": "",
      "date_of_birth": null,
      "is_patient": false,
      "is_authorized_party": false,
      "is_clinic_staff": false,
      "date_of_death": null,
      "retention_only": false,
      "do_not_contact": false
      

    
  },
  {
    
    

      "password": "RzMdsJLufx2FvVi",
      "last_login": null,
      "is_superuser": false,
      "username": "james.buchanan.jr",
      "email": "james.buchanan.jr@us.presidents.com",
      "is_staff": true,
      "is_active": true,
      "date_joined": "2021-05-30T12:34:34.709Z",
      "first_name": "James",
      "last_name": "Buchanan",
      "middle_name": "",
      "title": null,
      "honorific_prefix": "No Selection, Declined To Answer",
      "honorific_suffix": "No Selection, Declined To Answer",
      "suffix": "Jr",
      "date_of_birth": null,
      "is_patient": false,
      "is_authorized_party": false,
      "is_clinic_staff": false,
      "date_of_death": null,
      "retention_only": false,
      "do_not_contact": false
      

    
  },
  {
    
    

      "password": "RzMdsJLufx2FvVi",
      "last_login": null,
      "is_superuser": false,
      "username": "abraham.lincoln",
      "email": "abraham.lincoln@us.presidents.com",
      "is_staff": true,
      "is_active": true,
      "date_joined": "2021-05-30T12:34:34.709Z",
      "first_name": "Abraham",
      "last_name": "Lincoln",
      "middle_name": "",
      "title": null,
      "honorific_prefix": "No Selection, Declined To Answer",
      "honorific_suffix": "No Selection, Declined To Answer",
      "suffix": "",
      "date_of_birth": null,
      "is_patient": false,
      "is_authorized_party": false,
      "is_clinic_staff": false,
      "date_of_death": null,
      "retention_only": false,
      "do_not_contact": false
      

    
  },
  {
    
    

      "password": "RzMdsJLufx2FvVi",
      "last_login": null,
      "is_superuser": false,
      "username": "andrew.johnson",
      "email": "andrew.johnson@us.presidents.com",
      "is_staff": true,
      "is_active": true,
      "date_joined": "2021-05-30T12:34:34.709Z",
      "first_name": "Andrew",
      "last_name": "Johnson",
      "middle_name": "",
      "title": null,
      "honorific_prefix": "No Selection, Declined To Answer",
      "honorific_suffix": "No Selection, Declined To Answer",
      "suffix": "",
      "date_of_birth": null,
      "is_patient": false,
      "is_authorized_party": false,
      "is_clinic_staff": false,
      "date_of_death": null,
      "retention_only": false,
      "do_not_contact": false
      

    
  },
  {
    
    

      "password": "RzMdsJLufx2FvVi",
      "last_login": null,
      "is_superuser": false,
      "username": "hiram.ulysses.grant",
      "email": "hiram.ulysses.grant@us.presidents.com",
      "is_staff": true,
      "is_active": true,
      "date_joined": "2021-05-30T12:34:34.709Z",
      "first_name": "Hiram",
      "last_name": "Grant",
      "middle_name": "Ulysses",
      "title": null,
      "honorific_prefix": "No Selection, Declined To Answer",
      "honorific_suffix": "No Selection, Declined To Answer",
      "suffix": "",
      "date_of_birth": null,
      "is_patient": false,
      "is_authorized_party": false,
      "is_clinic_staff": false,
      "date_of_death": null,
      "retention_only": false,
      "do_not_contact": false
      

    
  },
  {
    
    

      "password": "RzMdsJLufx2FvVi",
      "last_login": null,
      "is_superuser": false,
      "username": "rutherford.birchard.hayes",
      "email": "rutherford.birchard.hayes@us.presidents.com",
      "is_staff": true,
      "is_active": true,
      "date_joined": "2021-05-30T12:34:34.709Z",
      "first_name": "Rutherford",
      "last_name": "Hayes",
      "middle_name": "Birchard",
      "title": null,
      "honorific_prefix": "No Selection, Declined To Answer",
      "honorific_suffix": "No Selection, Declined To Answer",
      "suffix": "",
      "date_of_birth": null,
      "is_patient": false,
      "is_authorized_party": false,
      "is_clinic_staff": false,
      "date_of_death": null,
      "retention_only": false,
      "do_not_contact": false
      

    
  },
  {
    
    

      "password": "RzMdsJLufx2FvVi",
      "last_login": null,
      "is_superuser": false,
      "username": "james.abram.garfield",
      "email": "james.abram.garfield@us.presidents.com",
      "is_staff": true,
      "is_active": true,
      "date_joined": "2021-05-30T12:34:34.709Z",
      "first_name": "James",
      "last_name": "Garfield",
      "middle_name": "Abram",
      "title": null,
      "honorific_prefix": "No Selection, Declined To Answer",
      "honorific_suffix": "No Selection, Declined To Answer",
      "suffix": "",
      "date_of_birth": null,
      "is_patient": false,
      "is_authorized_party": false,
      "is_clinic_staff": false,
      "date_of_death": null,
      "retention_only": false,
      "do_not_contact": false
      

    
  },
  {
    
    

      "password": "RzMdsJLufx2FvVi",
      "last_login": null,
      "is_superuser": false,
      "username": "chester.alan.arthur",
      "email": "chester.alan.arthur@us.presidents.com",
      "is_staff": true,
      "is_active": true,
      "date_joined": "2021-05-30T12:34:34.709Z",
      "first_name": "Chester",
      "last_name": "Arthur",
      "middle_name": "Alan",
      "title": null,
      "honorific_prefix": "No Selection, Declined To Answer",
      "honorific_suffix": "No Selection, Declined To Answer",
      "suffix": "",
      "date_of_birth": null,
      "is_patient": false,
      "is_authorized_party": false,
      "is_clinic_staff": false,
      "date_of_death": null,
      "retention_only": false,
      "do_not_contact": false
      

    
  },
  {
    
    

      "password": "RzMdsJLufx2FvVi",
      "last_login": null,
      "is_superuser": false,
      "username": "stephen.grover.cleveland",
      "email": "stephen.grover.cleveland@us.presidents.com",
      "is_staff": true,
      "is_active": true,
      "date_joined": "2021-05-30T12:34:34.709Z",
      "first_name": "Stephen",
      "last_name": "Cleveland",
      "middle_name": "Grover",
      "title": null,
      "honorific_prefix": "No Selection, Declined To Answer",
      "honorific_suffix": "No Selection, Declined To Answer",
      "suffix": "",
      "date_of_birth": null,
      "is_patient": false,
      "is_authorized_party": false,
      "is_clinic_staff": false,
      "date_of_death": null,
      "retention_only": false,
      "do_not_contact": false
      

    
  },
  {
    
    

      "password": "RzMdsJLufx2FvVi",
      "last_login": null,
      "is_superuser": false,
      "username": "benjamin.harrison",
      "email": "benjamin.harrison@us.presidents.com",
      "is_staff": true,
      "is_active": true,
      "date_joined": "2021-05-30T12:34:34.709Z",
      "first_name": "Benjamin",
      "last_name": "Harrison",
      "middle_name": "",
      "title": null,
      "honorific_prefix": "No Selection, Declined To Answer",
      "honorific_suffix": "No Selection, Declined To Answer",
      "suffix": "",
      "date_of_birth": null,
      "is_patient": false,
      "is_authorized_party": false,
      "is_clinic_staff": false,
      "date_of_death": null,
      "retention_only": false,
      "do_not_contact": false
      

    
  },
  {
    
    

      "password": "RzMdsJLufx2FvVi",
      "last_login": null,
      "is_superuser": false,
      "username": "william.mckinley",
      "email": "william.mckinley@us.presidents.com",
      "is_staff": true,
      "is_active": true,
      "date_joined": "2021-05-30T12:34:34.709Z",
      "first_name": "William",
      "last_name": "McKinley",
      "middle_name": "",
      "title": null,
      "honorific_prefix": "No Selection, Declined To Answer",
      "honorific_suffix": "No Selection, Declined To Answer",
      "suffix": "",
      "date_of_birth": null,
      "is_patient": false,
      "is_authorized_party": false,
      "is_clinic_staff": false,
      "date_of_death": null,
      "retention_only": false,
      "do_not_contact": false
      

    
  },
  {
    
    

      "password": "RzMdsJLufx2FvVi",
      "last_login": null,
      "is_superuser": false,
      "username": "stephen.grover.cleveland.twice",
      "email": "stephen.grover.cleveland.twice@us.presidents.com",
      "is_staff": true,
      "is_active": true,
      "date_joined": "2021-05-30T12:34:34.709Z",
      "first_name": "Stephen",
      "last_name": "Cleveland.twice",
      "middle_name": "Grover",
      "title": null,
      "honorific_prefix": "No Selection, Declined To Answer",
      "honorific_suffix": "No Selection, Declined To Answer",
      "suffix": "",
      "date_of_birth": null,
      "is_patient": false,
      "is_authorized_party": false,
      "is_clinic_staff": false,
      "date_of_death": null,
      "retention_only": false,
      "do_not_contact": false
      

    
  },
  {
    
    

      "password": "RzMdsJLufx2FvVi",
      "last_login": null,
      "is_superuser": false,
      "username": "theodore.roosevelt.jr",
      "email": "theodore.roosevelt.jr@us.presidents.com",
      "is_staff": true,
      "is_active": true,
      "date_joined": "2021-05-30T12:34:34.709Z",
      "first_name": "Theodore",
      "last_name": "Roosevelt",
      "middle_name": "",
      "title": null,
      "honorific_prefix": "No Selection, Declined To Answer",
      "honorific_suffix": "No Selection, Declined To Answer",
      "suffix": "Jr",
      "date_of_birth": null,
      "is_patient": false,
      "is_authorized_party": false,
      "is_clinic_staff": false,
      "date_of_death": null,
      "retention_only": false,
      "do_not_contact": false
      

    
  },
  {
    
    

      "password": "RzMdsJLufx2FvVi",
      "last_login": null,
      "is_superuser": false,
      "username": "william.howard.taft",
      "email": "william.howard.taft@us.presidents.com",
      "is_staff": true,
      "is_active": true,
      "date_joined": "2021-05-30T12:34:34.709Z",
      "first_name": "William",
      "last_name": "Taft",
      "middle_name": "Howard",
      "title": null,
      "honorific_prefix": "No Selection, Declined To Answer",
      "honorific_suffix": "No Selection, Declined To Answer",
      "suffix": "",
      "date_of_birth": null,
      "is_patient": false,
      "is_authorized_party": false,
      "is_clinic_staff": false,
      "date_of_death": null,
      "retention_only": false,
      "do_not_contact": false
      

    
  },
  {
    
    

      "password": "RzMdsJLufx2FvVi",
      "last_login": null,
      "is_superuser": false,
      "username": "thomas.woodrow.wilson",
      "email": "thomas.woodrow.wilson@us.presidents.com",
      "is_staff": true,
      "is_active": true,
      "date_joined": "2021-05-30T12:34:34.709Z",
      "first_name": "Thomas",
      "last_name": "Wilson",
      "middle_name": "Woodrow",
      "title": null,
      "honorific_prefix": "No Selection, Declined To Answer",
      "honorific_suffix": "No Selection, Declined To Answer",
      "suffix": "",
      "date_of_birth": null,
      "is_patient": false,
      "is_authorized_party": false,
      "is_clinic_staff": false,
      "date_of_death": null,
      "retention_only": false,
      "do_not_contact": false
      

    
  },
  {
    
    

      "password": "RzMdsJLufx2FvVi",
      "last_login": null,
      "is_superuser": false,
      "username": "warren.gamaliel.harding",
      "email": "warren.gamaliel.harding@us.presidents.com",
      "is_staff": true,
      "is_active": true,
      "date_joined": "2021-05-30T12:34:34.709Z",
      "first_name": "Warren",
      "last_name": "Harding",
      "middle_name": "Gamaliel",
      "title": null,
      "honorific_prefix": "No Selection, Declined To Answer",
      "honorific_suffix": "No Selection, Declined To Answer",
      "suffix": "",
      "date_of_birth": null,
      "is_patient": false,
      "is_authorized_party": false,
      "is_clinic_staff": false,
      "date_of_death": null,
      "retention_only": false,
      "do_not_contact": false
      

    
  },
  {
    
    

      "password": "RzMdsJLufx2FvVi",
      "last_login": null,
      "is_superuser": false,
      "username": "john.calvin.coolidge.jr",
      "email": "john.calvin.coolidge.jr@us.presidents.com",
      "is_staff": true,
      "is_active": true,
      "date_joined": "2021-05-30T12:34:34.709Z",
      "first_name": "John",
      "last_name": "Coolidge",
      "middle_name": "Calvin",
      "title": null,
      "honorific_prefix": "No Selection, Declined To Answer",
      "honorific_suffix": "No Selection, Declined To Answer",
      "suffix": "Jr",
      "date_of_birth": null,
      "is_patient": false,
      "is_authorized_party": false,
      "is_clinic_staff": false,
      "date_of_death": null,
      "retention_only": false,
      "do_not_contact": false
      

    
  },
  {
    
    

      "password": "RzMdsJLufx2FvVi",
      "last_login": null,
      "is_superuser": false,
      "username": "herbert.clark.hoover",
      "email": "herbert.clark.hoover@us.presidents.com",
      "is_staff": true,
      "is_active": true,
      "date_joined": "2021-05-30T12:34:34.709Z",
      "first_name": "Herbert",
      "last_name": "Hoover",
      "middle_name": "Clark",
      "title": null,
      "honorific_prefix": "No Selection, Declined To Answer",
      "honorific_suffix": "No Selection, Declined To Answer",
      "suffix": "",
      "date_of_birth": null,
      "is_patient": false,
      "is_authorized_party": false,
      "is_clinic_staff": false,
      "date_of_death": null,
      "retention_only": false,
      "do_not_contact": false
      

    
  },
  {
    
    

      "password": "RzMdsJLufx2FvVi",
      "last_login": null,
      "is_superuser": false,
      "username": "franklin.delano.roosevelt",
      "email": "franklin.delano.roosevelt@us.presidents.com",
      "is_staff": true,
      "is_active": true,
      "date_joined": "2021-05-30T12:34:34.709Z",
      "first_name": "Franklin",
      "last_name": "Roosevelt",
      "middle_name": "Delano",
      "title": null,
      "honorific_prefix": "No Selection, Declined To Answer",
      "honorific_suffix": "No Selection, Declined To Answer",
      "suffix": "",
      "date_of_birth": null,
      "is_patient": false,
      "is_authorized_party": false,
      "is_clinic_staff": false,
      "date_of_death": null,
      "retention_only": false,
      "do_not_contact": false
      

    
  },
  {
    
    

      "password": "RzMdsJLufx2FvVi",
      "last_login": null,
      "is_superuser": false,
      "username": "harry.s.truman",
      "email": "harry.s.truman@us.presidents.com",
      "is_staff": true,
      "is_active": true,
      "date_joined": "2021-05-30T12:34:34.709Z",
      "first_name": "Harry",
      "last_name": "Truman",
      "middle_name": "S",
      "title": null,
      "honorific_prefix": "No Selection, Declined To Answer",
      "honorific_suffix": "No Selection, Declined To Answer",
      "suffix": "",
      "date_of_birth": null,
      "is_patient": false,
      "is_authorized_party": false,
      "is_clinic_staff": false,
      "date_of_death": null,
      "retention_only": false,
      "do_not_contact": false
      

    
  },
  {
    
    

      "password": "RzMdsJLufx2FvVi",
      "last_login": null,
      "is_superuser": false,
      "username": "dwight.david.eisenhower",
      "email": "dwight.david.eisenhower@us.presidents.com",
      "is_staff": true,
      "is_active": true,
      "date_joined": "2021-05-30T12:34:34.709Z",
      "first_name": "Dwight",
      "last_name": "Eisenhower",
      "middle_name": "David",
      "title": null,
      "honorific_prefix": "No Selection, Declined To Answer",
      "honorific_suffix": "No Selection, Declined To Answer",
      "suffix": "",
      "date_of_birth": null,
      "is_patient": false,
      "is_authorized_party": false,
      "is_clinic_staff": false,
      "date_of_death": null,
      "retention_only": false,
      "do_not_contact": false
      

    
  },
  {
    
    

      "password": "RzMdsJLufx2FvVi",
      "last_login": null,
      "is_superuser": false,
      "username": "john.fitzgerald.kennedy",
      "email": "john.fitzgerald.kennedy@us.presidents.com",
      "is_staff": true,
      "is_active": true,
      "date_joined": "2021-05-30T12:34:34.709Z",
      "first_name": "John",
      "last_name": "Kennedy",
      "middle_name": "Fitzgerald",
      "title": null,
      "honorific_prefix": "No Selection, Declined To Answer",
      "honorific_suffix": "No Selection, Declined To Answer",
      "suffix": "",
      "date_of_birth": null,
      "is_patient": false,
      "is_authorized_party": false,
      "is_clinic_staff": false,
      "date_of_death": null,
      "retention_only": false,
      "do_not_contact": false
      

    
  },
  {
    
    

      "password": "RzMdsJLufx2FvVi",
      "last_login": null,
      "is_superuser": false,
      "username": "lyndon.baines.johnson",
      "email": "lyndon.baines.johnson@us.presidents.com",
      "is_staff": true,
      "is_active": true,
      "date_joined": "2021-05-30T12:34:34.709Z",
      "first_name": "Lyndon",
      "last_name": "Johnson",
      "middle_name": "Baines",
      "title": null,
      "honorific_prefix": "No Selection, Declined To Answer",
      "honorific_suffix": "No Selection, Declined To Answer",
      "suffix": "",
      "date_of_birth": null,
      "is_patient": false,
      "is_authorized_party": false,
      "is_clinic_staff": false,
      "date_of_death": null,
      "retention_only": false,
      "do_not_contact": false
      

    
  },
  {
    
    

      "password": "RzMdsJLufx2FvVi",
      "last_login": null,
      "is_superuser": false,
      "username": "richard.milhous.nixon",
      "email": "richard.milhous.nixon@us.presidents.com",
      "is_staff": true,
      "is_active": true,
      "date_joined": "2021-05-30T12:34:34.709Z",
      "first_name": "Richard",
      "last_name": "Nixon",
      "middle_name": "Milhous",
      "title": null,
      "honorific_prefix": "No Selection, Declined To Answer",
      "honorific_suffix": "No Selection, Declined To Answer",
      "suffix": "",
      "date_of_birth": null,
      "is_patient": false,
      "is_authorized_party": false,
      "is_clinic_staff": false,
      "date_of_death": null,
      "retention_only": false,
      "do_not_contact": false
      

    
  },
  {
    
    

      "password": "RzMdsJLufx2FvVi",
      "last_login": null,
      "is_superuser": false,
      "username": "leslie.lynch.king.jr",
      "email": "leslie.lynch.king.jr@us.presidents.com",
      "is_staff": true,
      "is_active": true,
      "date_joined": "2021-05-30T12:34:34.709Z",
      "first_name": "Leslie",
      "last_name": "King",
      "middle_name": "Lynch",
      "title": null,
      "honorific_prefix": "No Selection, Declined To Answer",
      "honorific_suffix": "No Selection, Declined To Answer",
      "suffix": "Jr",
      "date_of_birth": null,
      "is_patient": false,
      "is_authorized_party": false,
      "is_clinic_staff": false,
      "date_of_death": null,
      "retention_only": false,
      "do_not_contact": false
      

    
  },
  {
    
    

      "password": "RzMdsJLufx2FvVi",
      "last_login": null,
      "is_superuser": false,
      "username": "james.earl.carter.jr",
      "email": "james.earl.carter.jr@us.presidents.com",
      "is_staff": true,
      "is_active": true,
      "date_joined": "2021-05-30T12:34:34.709Z",
      "first_name": "James",
      "last_name": "Carter",
      "middle_name": "Earl",
      "title": null,
      "honorific_prefix": "No Selection, Declined To Answer",
      "honorific_suffix": "No Selection, Declined To Answer",
      "suffix": "Jr",
      "date_of_birth": null,
      "is_patient": false,
      "is_authorized_party": false,
      "is_clinic_staff": false,
      "date_of_death": null,
      "retention_only": false,
      "do_not_contact": false
      

    
  },
  {
    
    

      "password": "RzMdsJLufx2FvVi",
      "last_login": null,
      "is_superuser": false,
      "username": "ronald.wilson.reagan",
      "email": "ronald.wilson.reagan@us.presidents.com",
      "is_staff": true,
      "is_active": true,
      "date_joined": "2021-05-30T12:34:34.709Z",
      "first_name": "Ronald",
      "last_name": "Reagan",
      "middle_name": "Wilson",
      "title": null,
      "honorific_prefix": "No Selection, Declined To Answer",
      "honorific_suffix": "No Selection, Declined To Answer",
      "suffix": "",
      "date_of_birth": null,
      "is_patient": false,
      "is_authorized_party": false,
      "is_clinic_staff": false,
      "date_of_death": "2004-06-05",
      "retention_only": false,
      "do_not_contact": false
      

    
  },
  {
    
    

      "password": "RzMdsJLufx2FvVi",
      "last_login": null,
      "is_superuser": false,
      "username": "george.herbert walker.bush",
      "email": "george.herbert walker.bush@us.presidents.com",
      "is_staff": true,
      "is_active": true,
      "date_joined": "2021-05-30T12:34:34.709Z",
      "first_name": "George",
      "last_name": "Bush",
      "middle_name": "Herbert Walker",
      "title": null,
      "honorific_prefix": "No Selection, Declined To Answer",
      "honorific_suffix": "No Selection, Declined To Answer",
      "suffix": "",
      "date_of_birth": null,
      "is_patient": false,
      "is_authorized_party": false,
      "is_clinic_staff": false,
      "date_of_death": null,
      "retention_only": false,
      "do_not_contact": false
      

    
  },
  {
    
    

      "password": "RzMdsJLufx2FvVi",
      "last_login": null,
      "is_superuser": false,
      "username": "william.jefferson.clinton",
      "email": "william.jefferson.clinton@us.presidents.com",
      "is_staff": true,
      "is_active": true,
      "date_joined": "2021-05-30T12:34:34.709Z",
      "first_name": "William",
      "last_name": "Clinton",
      "middle_name": "Jefferson",
      "title": null,
      "honorific_prefix": "No Selection, Declined To Answer",
      "honorific_suffix": "No Selection, Declined To Answer",
      "suffix": "",
      "date_of_birth": null,
      "is_patient": false,
      "is_authorized_party": false,
      "is_clinic_staff": false,
      "date_of_death": null,
      "retention_only": false,
      "do_not_contact": false
      

    
  },
  {
    
    

      "password": "RzMdsJLufx2FvVi",
      "last_login": null,
      "is_superuser": false,
      "username": "george.walker.bush",
      "email": "george.walker.bush@us.presidents.com",
      "is_staff": true,
      "is_active": true,
      "date_joined": "2021-05-30T12:34:34.709Z",
      "first_name": "George",
      "last_name": "Bush",
      "middle_name": "Walker",
      "title": null,
      "honorific_prefix": "No Selection, Declined To Answer",
      "honorific_suffix": "No Selection, Declined To Answer",
      "suffix": "",
      "date_of_birth": null,
      "is_patient": false,
      "is_authorized_party": false,
      "is_clinic_staff": false,
      "date_of_death": null,
      "retention_only": false,
      "do_not_contact": false
      

    
  },
  {
    
    

      "password": "RzMdsJLufx2FvVi",
      "last_login": null,
      "is_superuser": false,
      "username": "barack.hussein.obama.ii",
      "email": "barack.hussein.obama.ii@us.presidents.com",
      "is_staff": true,
      "is_active": true,
      "date_joined": "2021-05-30T12:34:34.709Z",
      "first_name": "Barack",
      "last_name": "Obama",
      "middle_name": "Hussein",
      "title": null,
      "honorific_prefix": "No Selection, Declined To Answer",
      "honorific_suffix": "No Selection, Declined To Answer",
      "suffix": "II",
      "date_of_birth": null,
      "is_patient": false,
      "is_authorized_party": false,
      "is_clinic_staff": false,
      "date_of_death": null,
      "retention_only": false,
      "do_not_contact": false
      

    
  },
  {
    
    

      "password": "pbkdf2_sha256$260000$aPhxmLLmakh58CvYUV3FhW$AvhnL0xLFMCCnLRoICHxu8aKBTr9lani2TT/NdR7Eh0=",
      "last_login": "2021-06-06T00:44:24.045Z",
      "is_superuser": false,
      "username": "donald.john.trump.sr",
      "email": "donald.john.trump.sr@us.presidents.com",
      "is_staff": true,
      "is_active": true,
      "date_joined": "2021-05-30T12:34:34.709Z",
      "first_name": "Donald",
      "last_name": "Trump",
      "middle_name": "John",
      "title": null,
      "honorific_prefix": "No Selection, Declined To Answer",
      "honorific_suffix": "No Selection, Declined To Answer",
      "suffix": "Sr",
      "date_of_birth": null,
      "is_patient": false,
      "is_authorized_party": false,
      "is_clinic_staff": false,
      "date_of_death": null,
      "retention_only": false,
      "do_not_contact": false
      

    
  },
  {
    
    

      "password": "RzMdsJLufx2FvVi",
      "last_login": null,
      "is_superuser": false,
      "username": "joseph.robinette.biden.jr",
      "email": "joseph.robinette.biden.jr@us.presidents.com",
      "is_staff": true,
      "is_active": true,
      "date_joined": "2021-05-30T12:34:34.709Z",
      "first_name": "Joseph",
      "last_name": "Biden",
      "middle_name": "Robinette",
      "title": null,
      "honorific_prefix": "No Selection, Declined To Answer",
      "honorific_suffix": "No Selection, Declined To Answer",
      "suffix": "Jr",
      "date_of_birth": null,
      "is_patient": false,
      "is_authorized_party": false,
      "is_clinic_staff": false,
      "date_of_death": null,
      "retention_only": false,
      "do_not_contact": false
      

    
  },
  {
    
    

      "password": "password123!@#",
      "last_login": null,
      "is_superuser": false,
      "username": "eddard.stark",
      "email": "eddard.stark@game.of.thrones.com",
      "is_staff": false,
      "is_active": true,
      "date_joined": "2021-06-01T22:04:08.224Z",
      "first_name": "eddard",
      "last_name": "stark",
      "middle_name": null,
      "title": null,
      "honorific_prefix": "No Selection, Declined To Answer",
      "honorific_suffix": "No Selection, Declined To Answer",
      "suffix": null,
      "date_of_birth": null,
      "is_patient": false,
      "is_authorized_party": false,
      "is_clinic_staff": false,
      "date_of_death": null,
      "retention_only": false,
      "do_not_contact": false
      

    
  },
  {
    
    

      "password": "password123!@#",
      "last_login": null,
      "is_superuser": false,
      "username": "robert.baratheon",
      "email": "robert.baratheon@game.of.thrones.com",
      "is_staff": false,
      "is_active": true,
      "date_joined": "2021-06-01T22:04:08.363Z",
      "first_name": "robert",
      "last_name": "baratheon",
      "middle_name": null,
      "title": null,
      "honorific_prefix": "No Selection, Declined To Answer",
      "honorific_suffix": "No Selection, Declined To Answer",
      "suffix": null,
      "date_of_birth": null,
      "is_patient": false,
      "is_authorized_party": false,
      "is_clinic_staff": false,
      "date_of_death": null,
      "retention_only": false,
      "do_not_contact": false
      

    
  },
  {
    
    

      "password": "password123!@#",
      "last_login": null,
      "is_superuser": false,
      "username": "jaime.lannister",
      "email": "jaime.lannister@game.of.thrones.com",
      "is_staff": false,
      "is_active": true,
      "date_joined": "2021-06-01T22:04:08.503Z",
      "first_name": "jaime",
      "last_name": "lannister",
      "middle_name": null,
      "title": null,
      "honorific_prefix": "No Selection, Declined To Answer",
      "honorific_suffix": "No Selection, Declined To Answer",
      "suffix": null,
      "date_of_birth": null,
      "is_patient": false,
      "is_authorized_party": false,
      "is_clinic_staff": false,
      "date_of_death": null,
      "retention_only": false,
      "do_not_contact": false
      

    
  },
  {
    
    

      "password": "password123!@#",
      "last_login": null,
      "is_superuser": false,
      "username": "catelyn.stark",
      "email": "catelyn.stark@game.of.thrones.com",
      "is_staff": false,
      "is_active": true,
      "date_joined": "2021-06-01T22:04:08.644Z",
      "first_name": "catelyn",
      "last_name": "stark",
      "middle_name": null,
      "title": null,
      "honorific_prefix": "No Selection, Declined To Answer",
      "honorific_suffix": "No Selection, Declined To Answer",
      "suffix": null,
      "date_of_birth": null,
      "is_patient": false,
      "is_authorized_party": false,
      "is_clinic_staff": false,
      "date_of_death": null,
      "retention_only": false,
      "do_not_contact": false
      

    
  },
  {
    
    

      "password": "password123!@#",
      "last_login": null,
      "is_superuser": false,
      "username": "cersei.lannister",
      "email": "cersei.lannister@game.of.thrones.com",
      "is_staff": false,
      "is_active": true,
      "date_joined": "2021-06-01T22:04:08.783Z",
      "first_name": "cersei",
      "last_name": "lannister",
      "middle_name": null,
      "title": null,
      "honorific_prefix": "No Selection, Declined To Answer",
      "honorific_suffix": "No Selection, Declined To Answer",
      "suffix": null,
      "date_of_birth": null,
      "is_patient": false,
      "is_authorized_party": false,
      "is_clinic_staff": false,
      "date_of_death": null,
      "retention_only": false,
      "do_not_contact": false
      

    
  },
  {
    
    

      "password": "password123!@#",
      "last_login": null,
      "is_superuser": false,
      "username": "daenerys.targaryen",
      "email": "daenerys.targaryen@game.of.thrones.com",
      "is_staff": false,
      "is_active": true,
      "date_joined": "2021-06-01T22:04:08.920Z",
      "first_name": "daenerys",
      "last_name": "targaryen",
      "middle_name": null,
      "title": null,
      "honorific_prefix": "No Selection, Declined To Answer",
      "honorific_suffix": "No Selection, Declined To Answer",
      "suffix": null,
      "date_of_birth": null,
      "is_patient": false,
      "is_authorized_party": false,
      "is_clinic_staff": false,
      "date_of_death": null,
      "retention_only": false,
      "do_not_contact": false
      

    
  },
  {
    
    

      "password": "password123!@#",
      "last_login": null,
      "is_superuser": false,
      "username": "jorah.mormont",
      "email": "jorah.mormont@game.of.thrones.com",
      "is_staff": false,
      "is_active": true,
      "date_joined": "2021-06-01T22:04:09.061Z",
      "first_name": "jorah",
      "last_name": "mormont",
      "middle_name": null,
      "title": null,
      "honorific_prefix": "No Selection, Declined To Answer",
      "honorific_suffix": "No Selection, Declined To Answer",
      "suffix": null,
      "date_of_birth": null,
      "is_patient": false,
      "is_authorized_party": false,
      "is_clinic_staff": false,
      "date_of_death": null,
      "retention_only": false,
      "do_not_contact": false
      

    
  },
  {
    
    

      "password": "password123!@#",
      "last_login": null,
      "is_superuser": false,
      "username": "viserys.targaryen",
      "email": "viserys.targaryen@game.of.thrones.com",
      "is_staff": false,
      "is_active": true,
      "date_joined": "2021-06-01T22:04:09.199Z",
      "first_name": "viserys",
      "last_name": "targaryen",
      "middle_name": null,
      "title": null,
      "honorific_prefix": "No Selection, Declined To Answer",
      "honorific_suffix": "No Selection, Declined To Answer",
      "suffix": null,
      "date_of_birth": null,
      "is_patient": false,
      "is_authorized_party": false,
      "is_clinic_staff": false,
      "date_of_death": null,
      "retention_only": false,
      "do_not_contact": false
      

    
  },
  {
    
    

      "password": "password123!@#",
      "last_login": null,
      "is_superuser": false,
      "username": "jon.snow",
      "email": "jon.snow@game.of.thrones.com",
      "is_staff": false,
      "is_active": true,
      "date_joined": "2021-06-01T22:04:09.348Z",
      "first_name": "jon",
      "last_name": "snow",
      "middle_name": null,
      "title": null,
      "honorific_prefix": "No Selection, Declined To Answer",
      "honorific_suffix": "No Selection, Declined To Answer",
      "suffix": null,
      "date_of_birth": null,
      "is_patient": false,
      "is_authorized_party": false,
      "is_clinic_staff": false,
      "date_of_death": null,
      "retention_only": false,
      "do_not_contact": false
      

    
  },
  {
    
    

      "password": "password123!@#",
      "last_login": null,
      "is_superuser": false,
      "username": "robb.stark",
      "email": "robb.stark@game.of.thrones.com",
      "is_staff": false,
      "is_active": true,
      "date_joined": "2021-06-01T22:04:09.484Z",
      "first_name": "robb",
      "last_name": "stark",
      "middle_name": null,
      "title": null,
      "honorific_prefix": "No Selection, Declined To Answer",
      "honorific_suffix": "No Selection, Declined To Answer",
      "suffix": null,
      "date_of_birth": null,
      "is_patient": false,
      "is_authorized_party": false,
      "is_clinic_staff": false,
      "date_of_death": null,
      "retention_only": false,
      "do_not_contact": false
      

    
  },
  {
    
    

      "password": "password123!@#",
      "last_login": null,
      "is_superuser": false,
      "username": "sansa.stark",
      "email": "sansa.stark@game.of.thrones.com",
      "is_staff": false,
      "is_active": true,
      "date_joined": "2021-06-01T22:04:09.623Z",
      "first_name": "sansa",
      "last_name": "stark",
      "middle_name": null,
      "title": null,
      "honorific_prefix": "No Selection, Declined To Answer",
      "honorific_suffix": "No Selection, Declined To Answer",
      "suffix": null,
      "date_of_birth": null,
      "is_patient": false,
      "is_authorized_party": false,
      "is_clinic_staff": false,
      "date_of_death": null,
      "retention_only": false,
      "do_not_contact": false
      

    
  },
  {
    
    

      "password": "password123!@#",
      "last_login": null,
      "is_superuser": false,
      "username": "arya.stark",
      "email": "arya.stark@game.of.thrones.com",
      "is_staff": false,
      "is_active": true,
      "date_joined": "2021-06-01T22:04:09.763Z",
      "first_name": "arya",
      "last_name": "stark",
      "middle_name": null,
      "title": null,
      "honorific_prefix": "No Selection, Declined To Answer",
      "honorific_suffix": "No Selection, Declined To Answer",
      "suffix": null,
      "date_of_birth": null,
      "is_patient": false,
      "is_authorized_party": false,
      "is_clinic_staff": false,
      "date_of_death": null,
      "retention_only": false,
      "do_not_contact": false
      

    
  },
  {
    
    

      "password": "password123!@#",
      "last_login": null,
      "is_superuser": false,
      "username": "theon.greyjoy",
      "email": "theon.greyjoy@game.of.thrones.com",
      "is_staff": false,
      "is_active": true,
      "date_joined": "2021-06-01T22:04:09.902Z",
      "first_name": "theon",
      "last_name": "greyjoy",
      "middle_name": null,
      "title": null,
      "honorific_prefix": "No Selection, Declined To Answer",
      "honorific_suffix": "No Selection, Declined To Answer",
      "suffix": null,
      "date_of_birth": null,
      "is_patient": false,
      "is_authorized_party": false,
      "is_clinic_staff": false,
      "date_of_death": null,
      "retention_only": false,
      "do_not_contact": false
      

    
  },
  {
    
    

      "password": "password123!@#",
      "last_login": null,
      "is_superuser": false,
      "username": "brandon.stark",
      "email": "brandon.stark@game.of.thrones.com",
      "is_staff": false,
      "is_active": true,
      "date_joined": "2021-06-01T22:04:10.043Z",
      "first_name": "brandon",
      "last_name": "stark",
      "middle_name": null,
      "title": null,
      "honorific_prefix": "No Selection, Declined To Answer",
      "honorific_suffix": "No Selection, Declined To Answer",
      "suffix": null,
      "date_of_birth": null,
      "is_patient": false,
      "is_authorized_party": false,
      "is_clinic_staff": false,
      "date_of_death": null,
      "retention_only": false,
      "do_not_contact": false
      

    
  },
  {
    
    

      "password": "password123!@#",
      "last_login": null,
      "is_superuser": false,
      "username": "joffrey.baratheon",
      "email": "joffrey.baratheon@game.of.thrones.com",
      "is_staff": false,
      "is_active": true,
      "date_joined": "2021-06-01T22:04:10.183Z",
      "first_name": "joffrey",
      "last_name": "baratheon",
      "middle_name": null,
      "title": null,
      "honorific_prefix": "No Selection, Declined To Answer",
      "honorific_suffix": "No Selection, Declined To Answer",
      "suffix": null,
      "date_of_birth": null,
      "is_patient": false,
      "is_authorized_party": false,
      "is_clinic_staff": false,
      "date_of_death": null,
      "retention_only": false,
      "do_not_contact": false
      

    
  },
  {
    
    

      "password": "password123!@#",
      "last_login": null,
      "is_superuser": false,
      "username": "sandor.clegane",
      "email": "sandor.clegane@game.of.thrones.com",
      "is_staff": false,
      "is_active": true,
      "date_joined": "2021-06-01T22:04:10.328Z",
      "first_name": "sandor",
      "last_name": "clegane",
      "middle_name": null,
      "title": null,
      "honorific_prefix": "No Selection, Declined To Answer",
      "honorific_suffix": "No Selection, Declined To Answer",
      "suffix": null,
      "date_of_birth": null,
      "is_patient": false,
      "is_authorized_party": false,
      "is_clinic_staff": false,
      "date_of_death": null,
      "retention_only": false,
      "do_not_contact": false
      

    
  },
  {
    
    

      "password": "password123!@#",
      "last_login": null,
      "is_superuser": false,
      "username": "tyrion.lannister",
      "email": "tyrion.lannister@game.of.thrones.com",
      "is_staff": false,
      "is_active": true,
      "date_joined": "2021-06-01T22:04:10.468Z",
      "first_name": "tyrion",
      "last_name": "lannister",
      "middle_name": null,
      "title": null,
      "honorific_prefix": "No Selection, Declined To Answer",
      "honorific_suffix": "No Selection, Declined To Answer",
      "suffix": null,
      "date_of_birth": null,
      "is_patient": false,
      "is_authorized_party": false,
      "is_clinic_staff": false,
      "date_of_death": null,
      "retention_only": false,
      "do_not_contact": false
      

    
  },
  {
    
    

      "password": "password123!@#",
      "last_login": null,
      "is_superuser": false,
      "username": "petyr.baelish",
      "email": "petyr.baelish@game.of.thrones.com",
      "is_staff": false,
      "is_active": true,
      "date_joined": "2021-06-01T22:04:10.606Z",
      "first_name": "petyr",
      "last_name": "baelish",
      "middle_name": null,
      "title": null,
      "honorific_prefix": "No Selection, Declined To Answer",
      "honorific_suffix": "No Selection, Declined To Answer",
      "suffix": null,
      "date_of_birth": null,
      "is_patient": false,
      "is_authorized_party": false,
      "is_clinic_staff": false,
      "date_of_death": null,
      "retention_only": false,
      "do_not_contact": false
      

    
  },
  {
    
    

      "password": "password123!@#",
      "last_login": null,
      "is_superuser": false,
      "username": "davos.seaworth",
      "email": "davos.seaworth@game.of.thrones.com",
      "is_staff": false,
      "is_active": true,
      "date_joined": "2021-06-01T22:04:10.747Z",
      "first_name": "davos",
      "last_name": "seaworth",
      "middle_name": null,
      "title": null,
      "honorific_prefix": "No Selection, Declined To Answer",
      "honorific_suffix": "No Selection, Declined To Answer",
      "suffix": null,
      "date_of_birth": null,
      "is_patient": false,
      "is_authorized_party": false,
      "is_clinic_staff": false,
      "date_of_death": null,
      "retention_only": false,
      "do_not_contact": false
      

    
  },
  {
    
    

      "password": "password123!@#",
      "last_login": null,
      "is_superuser": false,
      "username": "samwell.tarly",
      "email": "samwell.tarly@game.of.thrones.com",
      "is_staff": false,
      "is_active": true,
      "date_joined": "2021-06-01T22:04:10.888Z",
      "first_name": "samwell",
      "last_name": "tarly",
      "middle_name": null,
      "title": null,
      "honorific_prefix": "No Selection, Declined To Answer",
      "honorific_suffix": "No Selection, Declined To Answer",
      "suffix": null,
      "date_of_birth": null,
      "is_patient": false,
      "is_authorized_party": false,
      "is_clinic_staff": false,
      "date_of_death": null,
      "retention_only": false,
      "do_not_contact": false
      

    
  },
  {
    
    

      "password": "password123!@#",
      "last_login": null,
      "is_superuser": false,
      "username": "stannis.baratheon",
      "email": "stannis.baratheon@game.of.thrones.com",
      "is_staff": false,
      "is_active": true,
      "date_joined": "2021-06-01T22:04:11.030Z",
      "first_name": "stannis",
      "last_name": "baratheon",
      "middle_name": null,
      "title": null,
      "honorific_prefix": "No Selection, Declined To Answer",
      "honorific_suffix": "No Selection, Declined To Answer",
      "suffix": null,
      "date_of_birth": null,
      "is_patient": false,
      "is_authorized_party": false,
      "is_clinic_staff": false,
      "date_of_death": null,
      "retention_only": false,
      "do_not_contact": false
      

    
  },
  {
    
    

      "password": "password123!@#",
      "last_login": null,
      "is_superuser": false,
      "username": "jeor.mormont",
      "email": "jeor.mormont@game.of.thrones.com",
      "is_staff": false,
      "is_active": true,
      "date_joined": "2021-06-01T22:04:11.170Z",
      "first_name": "jeor",
      "last_name": "mormont",
      "middle_name": null,
      "title": null,
      "honorific_prefix": "No Selection, Declined To Answer",
      "honorific_suffix": "No Selection, Declined To Answer",
      "suffix": null,
      "date_of_birth": null,
      "is_patient": false,
      "is_authorized_party": false,
      "is_clinic_staff": false,
      "date_of_death": null,
      "retention_only": false,
      "do_not_contact": false
      

    
  },
  {
    
    

      "password": "password123!@#",
      "last_login": null,
      "is_superuser": false,
      "username": "margaery.tyrell",
      "email": "margaery.tyrell@game.of.thrones.com",
      "is_staff": false,
      "is_active": true,
      "date_joined": "2021-06-01T22:04:11.310Z",
      "first_name": "margaery",
      "last_name": "tyrell",
      "middle_name": null,
      "title": null,
      "honorific_prefix": "No Selection, Declined To Answer",
      "honorific_suffix": "No Selection, Declined To Answer",
      "suffix": null,
      "date_of_birth": null,
      "is_patient": false,
      "is_authorized_party": false,
      "is_clinic_staff": false,
      "date_of_death": null,
      "retention_only": false,
      "do_not_contact": false
      

    
  },
  {
    
    

      "password": "password123!@#",
      "last_login": null,
      "is_superuser": false,
      "username": "tywin.lannister",
      "email": "tywin.lannister@game.of.thrones.com",
      "is_staff": false,
      "is_active": true,
      "date_joined": "2021-06-01T22:04:11.456Z",
      "first_name": "tywin",
      "last_name": "lannister",
      "middle_name": null,
      "title": null,
      "honorific_prefix": "No Selection, Declined To Answer",
      "honorific_suffix": "No Selection, Declined To Answer",
      "suffix": null,
      "date_of_birth": null,
      "is_patient": false,
      "is_authorized_party": false,
      "is_clinic_staff": false,
      "date_of_death": null,
      "retention_only": false,
      "do_not_contact": false
      

    
  },
  {
    
    

      "password": "password123!@#",
      "last_login": null,
      "is_superuser": false,
      "username": "talisa.maegyr",
      "email": "talisa.maegyr@game.of.thrones.com",
      "is_staff": false,
      "is_active": true,
      "date_joined": "2021-06-01T22:04:11.594Z",
      "first_name": "talisa",
      "last_name": "maegyr",
      "middle_name": null,
      "title": null,
      "honorific_prefix": "No Selection, Declined To Answer",
      "honorific_suffix": "No Selection, Declined To Answer",
      "suffix": null,
      "date_of_birth": null,
      "is_patient": false,
      "is_authorized_party": false,
      "is_clinic_staff": false,
      "date_of_death": null,
      "retention_only": false,
      "do_not_contact": false
      

    
  },
  {
    
    

      "password": "password123!@#",
      "last_login": null,
      "is_superuser": false,
      "username": "tormund.giantsbane",
      "email": "tormund.giantsbane@game.of.thrones.com",
      "is_staff": false,
      "is_active": true,
      "date_joined": "2021-06-01T22:04:11.734Z",
      "first_name": "tormund",
      "last_name": "giantsbane",
      "middle_name": null,
      "title": null,
      "honorific_prefix": "No Selection, Declined To Answer",
      "honorific_suffix": "No Selection, Declined To Answer",
      "suffix": null,
      "date_of_birth": null,
      "is_patient": false,
      "is_authorized_party": false,
      "is_clinic_staff": false,
      "date_of_death": null,
      "retention_only": false,
      "do_not_contact": false
      

    
  },
  {
    
    

      "password": "password123!@#",
      "last_login": null,
      "is_superuser": false,
      "username": "brienne.detarth",
      "email": "brienne.detarth@game.of.thrones.com",
      "is_staff": false,
      "is_active": true,
      "date_joined": "2021-06-01T22:04:11.870Z",
      "first_name": "brienne",
      "last_name": "detarth",
      "middle_name": null,
      "title": null,
      "honorific_prefix": "No Selection, Declined To Answer",
      "honorific_suffix": "No Selection, Declined To Answer",
      "suffix": null,
      "date_of_birth": null,
      "is_patient": false,
      "is_authorized_party": false,
      "is_clinic_staff": false,
      "date_of_death": null,
      "retention_only": false,
      "do_not_contact": false
      

    
  },
  {
    
    

      "password": "password123!@#",
      "last_login": null,
      "is_superuser": false,
      "username": "ramsay.bolton",
      "email": "ramsay.bolton@game.of.thrones.com",
      "is_staff": false,
      "is_active": true,
      "date_joined": "2021-06-01T22:04:12.014Z",
      "first_name": "ramsay",
      "last_name": "bolton",
      "middle_name": null,
      "title": null,
      "honorific_prefix": "No Selection, Declined To Answer",
      "honorific_suffix": "No Selection, Declined To Answer",
      "suffix": null,
      "date_of_birth": null,
      "is_patient": false,
      "is_authorized_party": false,
      "is_clinic_staff": false,
      "date_of_death": null,
      "retention_only": false,
      "do_not_contact": false
      

    
  },
  {
    
    

      "password": "password123!@#",
      "last_login": null,
      "is_superuser": false,
      "username": "daario.naharis",
      "email": "daario.naharis@game.of.thrones.com",
      "is_staff": false,
      "is_active": true,
      "date_joined": "2021-06-01T22:04:12.152Z",
      "first_name": "daario",
      "last_name": "naharis",
      "middle_name": null,
      "title": null,
      "honorific_prefix": "No Selection, Declined To Answer",
      "honorific_suffix": "No Selection, Declined To Answer",
      "suffix": null,
      "date_of_birth": null,
      "is_patient": false,
      "is_authorized_party": false,
      "is_clinic_staff": false,
      "date_of_death": null,
      "retention_only": false,
      "do_not_contact": false
      

    
  },
  {
    
    

      "password": "password123!@#",
      "last_login": null,
      "is_superuser": false,
      "username": "ellaria.sand",
      "email": "ellaria.sand@game.of.thrones.com",
      "is_staff": false,
      "is_active": true,
      "date_joined": "2021-06-01T22:04:12.294Z",
      "first_name": "ellaria",
      "last_name": "sand",
      "middle_name": null,
      "title": null,
      "honorific_prefix": "No Selection, Declined To Answer",
      "honorific_suffix": "No Selection, Declined To Answer",
      "suffix": null,
      "date_of_birth": null,
      "is_patient": false,
      "is_authorized_party": false,
      "is_clinic_staff": false,
      "date_of_death": null,
      "retention_only": false,
      "do_not_contact": false
      

    
  },
  {
    
    

      "password": "password123!@#",
      "last_login": null,
      "is_superuser": false,
      "username": "tommen.baratheon",
      "email": "tommen.baratheon@game.of.thrones.com",
      "is_staff": false,
      "is_active": true,
      "date_joined": "2021-06-01T22:04:12.440Z",
      "first_name": "tommen",
      "last_name": "baratheon",
      "middle_name": null,
      "title": null,
      "honorific_prefix": "No Selection, Declined To Answer",
      "honorific_suffix": "No Selection, Declined To Answer",
      "suffix": null,
      "date_of_birth": null,
      "is_patient": false,
      "is_authorized_party": false,
      "is_clinic_staff": false,
      "date_of_death": null,
      "retention_only": false,
      "do_not_contact": false
      

    
  },
  {
    
    

      "password": "password123!@#",
      "last_login": null,
      "is_superuser": false,
      "username": "jaqen.hghar",
      "email": "jaqen.hghar@game.of.thrones.com",
      "is_staff": false,
      "is_active": true,
      "date_joined": "2021-06-01T22:04:12.579Z",
      "first_name": "jaqen",
      "last_name": "hghar",
      "middle_name": null,
      "title": null,
      "honorific_prefix": "No Selection, Declined To Answer",
      "honorific_suffix": "No Selection, Declined To Answer",
      "suffix": null,
      "date_of_birth": null,
      "is_patient": false,
      "is_authorized_party": false,
      "is_clinic_staff": false,
      "date_of_death": null,
      "retention_only": false,
      "do_not_contact": false
      

    
  },
  {
    
    

      "password": "password123!@#",
      "last_login": null,
      "is_superuser": false,
      "username": "roose.bolton",
      "email": "roose.bolton@game.of.thrones.com",
      "is_staff": false,
      "is_active": true,
      "date_joined": "2021-06-01T22:04:12.718Z",
      "first_name": "roose",
      "last_name": "bolton",
      "middle_name": null,
      "title": null,
      "honorific_prefix": "No Selection, Declined To Answer",
      "honorific_suffix": "No Selection, Declined To Answer",
      "suffix": null,
      "date_of_birth": null,
      "is_patient": false,
      "is_authorized_party": false,
      "is_clinic_staff": false,
      "date_of_death": null,
      "retention_only": false,
      "do_not_contact": false
      

    
  },
  {
    
      "password": "password123!@#",
      "last_login": null,
      "is_superuser": false,
      "username": "grey.worm",
      "email": "grey.worm@game.of.thrones.com",
      "is_staff": false,
      "is_active": true,
      "date_joined": "2021-06-01T22:04:12.857Z",
      "first_name": "grey",
      "last_name": "worm",
      "middle_name": null,
      "title": null,
      "honorific_prefix": "No Selection, Declined To Answer",
      "honorific_suffix": "No Selection, Declined To Answer",
      "suffix": null,
      "date_of_birth": null,
      "is_patient": false,
      "is_authorized_party": false,
      "is_clinic_staff": false,
      "date_of_death": null,
      "retention_only": false,
      "do_not_contact": false
      

    
  },
  {
    
    

      "password": "password123!@#",
      "last_login": null,
      "is_superuser": false,
      "username": "ichigo.kurosaki",
      "email": "ichigo.kurosaki@soul.society.com",
      "is_staff": false,
      "is_active": true,
      "date_joined": "2021-06-02T20:00:50.420Z",
      "first_name": "ichigo",
      "last_name": "kurosaki",
      "middle_name": null,
      "title": null,
      "honorific_prefix": "No Selection, Declined To Answer",
      "honorific_suffix": "No Selection, Declined To Answer",
      "suffix": null,
      "date_of_birth": null,
      "is_patient": false,
      "is_authorized_party": false,
      "is_clinic_staff": false,
      "date_of_death": null,
      "retention_only": false,
      "do_not_contact": false
      

    
  },
  {
    
    

      "password": "root",
      "last_login": "2021-06-06T15:49:08.823Z",
      "is_superuser": true,
      "username": "admin",
      "email": "",
      "is_staff": true,
      "is_active": true,
      "date_joined": "2021-06-06T00:43:26.410Z",
      "first_name": null,
      "last_name": null,
      "middle_name": null,
      "title": null,
      "honorific_prefix": "No Selection, Declined To Answer",
      "honorific_suffix": "No Selection, Declined To Answer",
      "suffix": null,
      "date_of_birth": null,
      "is_patient": false,
      "is_authorized_party": false,
      "is_clinic_staff": false,
      "date_of_death": null,
      "retention_only": false,
      "do_not_contact": false
      

    
  },
  {
    
    

      "password": "password123!@#",
      "last_login": null,
      "is_superuser": false,
      "username": "balon.greyjoy",
      "email": "balon.greyjoy@game.of.thrones.com",
      "is_staff": false,
      "is_active": true,
      "date_joined": "2021-06-06T15:56:38.299Z",
      "first_name": "balon",
      "last_name": "greyjoy",
      "middle_name": null,
      "title": null,
      "honorific_prefix": "No Selection, Declined To Answer",
      "honorific_suffix": "No Selection, Declined To Answer",
      "suffix": null,
      "date_of_birth": null,
      "is_patient": false,
      "is_authorized_party": true,
      "is_clinic_staff": false,
      "date_of_death": null,
      "retention_only": false,
      "do_not_contact": false
      

    
  }
]"""
data = json.loads(init)
users = get_user_model().objects.all()
previous = set([user.username for user in users])
for user in data:
    if user["username"] not in previous:
        u = get_user_model().objects.create(**user)

        previous.add(user["username"])
    else:
        u = get_user_model().objects.get(username=user["username"])
        u.set_password(user["password"])
        u.save()
users = get_user_model().objects.all()
change = [user for user in users if not user.has_usable_password()]
george = get_user_model().objects.first()
print(george)
print(george.password)
print(change)
