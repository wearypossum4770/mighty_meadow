import {writeFileSync} from 'fs'
let presidents = [
    
    {first_name:"George", middle_name:"", last_name:"Washington", suffix:""},  
{first_name:"John", middle_name:"", last_name:"Adams", suffix:"Jr"},  
{first_name:"Thomas", middle_name:"", last_name:"Jefferson", suffix:""}, 
{first_name:"James", middle_name:"", last_name:"Madison", suffix:"Jr"},  
{first_name:"James", middle_name:"", last_name:"Monroe", suffix:""}, 
{first_name:"John", middle_name:"Quincy", last_name:"Adams", suffix:""},   
{first_name:"Andrew", middle_name:"", last_name:"Jackson", suffix:""}, 
{first_name:"Martin", middle_name:"", last_name:"Van Buren", suffix:""}, 
{first_name:"William", middle_name:"Henry", last_name:"Harrison", suffix:""},  
{first_name:"John", middle_name:"", last_name:"Tyler", suffix:""}, 
{first_name:"James", middle_name:"Knox", last_name:"Polk", suffix:""},  
{first_name:"Zachary", middle_name:"", last_name:"Taylor", suffix:""}, 
{first_name:"Millard", middle_name:"", last_name:"Fillmore", suffix:""}, 
{first_name:"Franklin", middle_name:"", last_name:"Pierce", suffix:""}, 
{first_name:"James", middle_name:"", last_name:"Buchanan", suffix:"Jr"},
{first_name:"Abraham", middle_name:"", last_name:"Lincoln", suffix:""}, 
{first_name:"Andrew", middle_name:"", last_name:"Johnson", suffix:""}, 
{first_name:"Hiram", middle_name:"Ulysses", last_name:"Grant", suffix:""},  
{first_name:"Rutherford", middle_name:"Birchard", last_name:"Hayes", suffix:""},  
{first_name:"James", middle_name:"Abram", last_name:"Garfield", suffix:""},  
{first_name:"Chester", middle_name:"Alan", last_name:"Arthur", suffix:""},   
{first_name:"Stephen", middle_name:"Grover", last_name:"Cleveland", suffix:""},  
{first_name:"Benjamin", middle_name:"", last_name:"Harrison", suffix:""},  
{first_name:"William", middle_name:"", last_name:"McKinley", suffix:""}, 
{first_name:"Stephen", middle_name:"Grover", last_name:"Cleveland.twice", suffix:""}, 
{first_name:"Theodore", middle_name:"", last_name:"Roosevelt", suffix:"Jr", nickname:"Teddy"},
{first_name:"William", middle_name:"Howard", last_name:"Taft", suffix:""},   
{first_name:"Thomas", middle_name:"Woodrow", last_name:"Wilson", suffix:""},  
{first_name:"Warren", middle_name:"Gamaliel", last_name:"Harding", suffix:""},  
{first_name:"John", middle_name:"Calvin", last_name:"Coolidge", suffix:"Jr"},   
{first_name:"Herbert", middle_name:"Clark", last_name:"Hoover", suffix:""},  
{first_name:"Franklin", middle_name:"Delano", last_name:"Roosevelt", suffix:""},  
{first_name:"Harry", middle_name:"S", last_name:"Truman", suffix:""},
{first_name:"Dwight", middle_name:"David", last_name:"Eisenhower", suffix:"",nickname:"Ike"},    
{first_name:"John", middle_name:"Fitzgerald", last_name:"Kennedy", suffix:""},  
{first_name:"Lyndon", middle_name:"Baines", last_name:"Johnson", suffix:""},   
{first_name:"Richard", middle_name:"Milhous", last_name:"Nixon", suffix:""},  
{first_name:"Leslie", middle_name:"Lynch", last_name:"King", suffix:"Jr",nickname:"Gerald Rudolph Ford Jr."},    
{first_name:"James", middle_name:"Earl", last_name:"Carter", suffix:"Jr",nickname:"Jimmy"},
{first_name:"Ronald", middle_name:"Wilson", last_name:"Reagan", suffix:""},  
{first_name:"George", middle_name:"Herbert Walker", last_name:"Bush", suffix:"" ,nickname:"HW"},   
{first_name:"William", middle_name:"Jefferson", last_name:"Clinton", suffix:"",nickname:"Bill"},   
{first_name:"George", middle_name:"Walker", last_name:"Bush", suffix:""},  
{first_name:"Barack", middle_name:"Hussein", last_name:"Obama", suffix:"II"},    
{first_name:"Donald", middle_name:"John", last_name:"Trump", suffix:"Sr"},   
{first_name:"Joseph", middle_name:"Robinette", last_name:"Biden", suffix:"Jr"},  
] 


let data = []
presidents.forEach((president, index)=>{
    data.push(
    {    "model": "users.user",
    "pk": index+1,
       fields:{
        first_name:president?.first_name,
        middle_name:president?.middle_name,
        last_name:president?.last_name,
        suffix:president?.suffix,
        nickname:presidents?.nickname,
        password:"RzMdsJLufx2FvVi",
        get username(){return `${this.first_name}.${this.middle_name}.${this.last_name}.${this.suffix}`.replace(/\.$/,"").replace(/\.\./, ".").toLowerCase()
        },
        get email(){return `${this.username}@us.presidents.com`}
       }
    }
    )
})
writeFileSync('usersinit.json',JSON.stringify(data))