from .utils import two_val

us={
      "WebsiteName":"Shelter DCI",
      "Logo":"media/longlogo.png",
      "Members" : "Leyla, Martina, Angelo and Mohsen",
      "Story" : "Our team was born on 2024-February-20.<br> From our passion for animals and disapproval of abandonment,<br> we contribute to the war against animal abandonment by providing a temporary place for them <br> and helping them find new families who want to adopt them.",
      "Address":"",
      "FunnyStories":[
            {"foto":"media/familydog.png", "paragraphe":"2023-February-25 A family adopts a dog found in a truck stop."},
            {"foto":"media/girlcat.png", "paragraphe":"2023-February-28 A woman adopted a cat that had been found injured. "},
            {"foto":"", "paragraphe":""},
            ],
      "contributors":[
            {"foto":"media/fblogo.jpg", "name":"Facebook","link":"https://facebook.com/"},
            {"foto":"media/AAF.png", "name":"Animal Adoption Foundation","link":"https://aafpets.org/"},
            {"foto":"media/nuzzles.png", "name":"Nuzzles & Co","link":"https://nuzzlesandco.org/"},
            
      ],
      "Map":"https://www.google.com/maps/d/edit?mid=10s3EdNFne2XxbMl9yWwFyjdux9MVDqY&usp=sharing",
      "mapFrame":'<iframe src="https://www.google.com/maps/d/embed?mid=1vkmnviuySenFmWHy8g5IgYbXbmowlEg&ehbc=2E312F" width="640" height="480"></iframe>',
}

attr_species= {"class":"shadow fs-3 p-2;"}
species_options=[
      ("dog", "dog"),
      ("cat", "cat")
]

sizes_options={
      "dog":[
            ("small","small"),
            ("large","large"),
            ("big","big"),
      ],
      "cat":[
            ("small","small"),
            ("large", "large")
      ],
}

URLS={
      "api":{
            "getallpets":"https://localhost:8000/api/allpets/"
      }
}

GROUPS={
      "SPECIES":[
            ("species", "dog", "Dogs", True, 0,'species', {"selected":True}),
            ("species", "cat",  "Cats", False, 0,'species', attr_species),
      ],
      "GENDER":[
            ("Male",["Male","M", "0", False, 0], "Male", False, 0, 'gender', attr_species), 
            ("Famale",[ "Famale","F", "1", True, 1], "Famale", True, 0,'gender', attr_species),
      ],
      "SIZE":[
            {"name":"size-dog",
             "value":[
                  ("small","small","small", True, 0, 'small-dog' ,attr_species), 
                  ("large","large","large", False, 0, 'large-dog' , attr_species),
                  ("big","big", 'big',False,  0, 'big-dog',  attr_species),]},
            {"name":"size-cat",
            "value":[
                  ("small","small","small", False, 0,'small-cat',  attr_species),
                  ("large", "large","large", False, 0, 'large-cat' , attr_species)]
            }
      ],
      "STATUS":[
            ("Available", "Available","Available",True, 0,"Available", attr_species),               
            ("Pending adoption", "Pending adoption","Pending adoption",False, 0, "Pending adoption" ,attr_species),
            ("Adopted", "Adopted","Adopted",False, 0, "Adopted",attr_species),
      ],
      "BREED":[{
            "name":
                  "dog-small",
            "species":
                  "dog",
            "size":
                  "small",
            "value":[
                  
                  ("Australian Silky Terrier","Australian Silky Terrier","Australian Silky Terrier", True, 0, "Australian Silky Terrier" ,attr_species),
                  ("Tan Toy Terrier","Tan Toy Terrier","Tan Toy Terrier", False, 0,"Tan Toy Terrier", attr_species),
                  ("Bolognese","Bolognese","Bolognese", False, 0,"Bolognese", attr_species),
                  ("Chihuahua","Chihuahua","Chihuahua", False, 0, "Chihuahua" ,attr_species),
                  ("Volpin of Pomerania","Volpin of Pomerania","Volpin of Pomerania", False, 0, "Volpin of Pomerania", attr_species),
                  ("Boston Terrier","Boston Terrier","Boston Terrier", False, 0,"Boston Terrier", attr_species),
                  ("Bichon","Bichon","Bichon", False, 0,"Bichon", attr_species),
                  ("Basset Artesian Normand","Basset Artesian Normand","Basset Artesian Normand", False, 0,"Basset Artesian Normand", attr_species),
                  ("Bassotto of Alpi","Bassotto of Alpi","Bassotto of Alpi", False, 0,"Bassotto of Alpi", attr_species),
            ],},
            {"name":
                  "dog-large",
            "species":
                  "dog",
            "size":
                  "large",
            "value":[
                  ("Pittbull","Pittbull","Pittbull", True, 0,"Pittbull", attr_species),
                  ("Bulldog", "Bulldog","Bulldog", False, 0,"Bulldog", attr_species),
                  ("Bull Terrier", "Bull Terrier","Bull Terrier", False, 0,"Bull Terrier", attr_species),
                  ("Ariegeois","Ariegeois","Ariegeois", False, 0,"Ariegeois", attr_species),
                  ("Barbet", "Barbet","Barbet", False, 0,"Barbet", attr_species),
                  ("Beagle", "Beagle","Beagle", False, 0,"Beagle", attr_species),
                  ("Landseer","Landseer","Landseer", False, 0,"Landseer", attr_species),
                  ("Canarin Dogo","Canarin Dogo","Canarin Dogo", False, 0,"Canarin Dogo", attr_species),
            ],},
            {"name":
                  "dog-big",
            "species":
                  "dog",
            "size":
                  "big",
            "value":[
                  ["American Staffordshire Terrier","American Staffordshire Terrier" , "American Staffordshire Terrier", True, 0,"American Staffordshire Terrier", attr_species],                 
                  ["Akita","Akita", "Akita", False, 0,"Akita", attr_species],
                  ["Argentin Dogo","Argentin Dogo", "Argentin Dogo", False, 0,"Argentin Dogo", attr_species],
                  ["Asky","Asky", "Asky", False, 0,"Asky", attr_species],
                  ["Besenji","Besenji", "Besenji", False, 0,"Besenji", attr_species],
                  ["Boxer","Boxer", "Boxer", False, 0,"Boxer", attr_species],
                  ["Australian Stumpy Tail Cattle","Australian Stumpy Tail Cattle", "Australian Stumpy Tail Cattle", False, 0,"Australian Stumpy Tail Cattle", attr_species],
                  ["Italian Bracco","Italian Bracco", "Italian Bracco", False, 0,"Italian Bracco", attr_species],
                  ["Corso","Corso", "Corso", False, 0,"Corso", attr_species],
                  ["Alano","Alano", "Alano", False, 0,"Alano", attr_species],
                  ["Dog of Pirenei Mountains","Dog of Pirenei Mountains", "Dog of Pirenei Mountains", False, 0,"Dog of Pirenei Mountains", attr_species],
                  ["Kangal","Kangal", "Kangal", False, 0,"Kangal", attr_species],
                  ["Naples Mastin","Naples Mastin", "Naples Mastin", False, 0,"Naples Mastin", attr_species],
                  ["Maremma Shepherd","Maremma Shepherd", "Maremma Shepherd", False, 0,"Maremma Shepherd", attr_species]
            ]},
            {"name":
                  "cat-small",
            "species":
                  "cat",
            "size":
                  "small",
            "value":[   ],
            },
            {"name":
                  "cat-large",
            "species":
                  "cat",
            "size":
                  "large",
            "value":[   ],
            }
      ],
}

TWO_VALUES_OPT =two_val(GROUPS)
