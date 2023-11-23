# Chaabi Hiring: Solution
This repository contains all the files involved in solving the problem statement given by Chaabi in its Placement drive. It was submitted by -
Aryan Jain, Roll Number 200201, IIT Kanpur, aryanj20@iitk.ac.in

## Solution Content
- #### llm_model.py
    It contains the API keys of OpenAI and Qdrant along with function responsible for generating the LLM based answer.
- #### run_api.py
    This file starts the server and hosts the LLM python program on the local server.
- #### call_api.py
    The main file which takes in the query of the user, calls the API and maintain loop as a conservation with the user continues.
- #### getdata.ipynb
    Jupyter Notebook used to collect data, convert it into embeddings with OpenAI API and save it into Qdrant vector DB using Qdrant API.

## Setup

#### Libraries
Please ensure the following librabries of Python >= 3 are installed:
`flask`, `requests`, `os`, `openai`, `qdrant_client`

If you wish to retrain the data and run the getdata.ipynb please install the following libraries as well:
 `pandas`, `tiktoken`, `uuid`, `pickel`

#### Start the server
Simply run the file run_api.py or enter the following command in the repository:
```
python run_api.py
```

#### Call the API
Now run the file call_api.py or enter the following command in a different terminal in the same repository:
```
python call_api.py
```
It will start the conversation loop and will send the user queries to the local server using the API.

#### Enter Queries
Now you will be able to see `Please Enter query:` in the terminal. Write your query and press enter key. Please give some time program to generate answer and loop will continue.

## Additional Features
- #### Memory Based contexual answers
This is an additional feature in the program that allows it to answer questions based on the context of the previous conversations.
The following is series of the example query which the model was given - 
```
Entry your query -

recommend me something to kill my bed bugs
Generating Answer ... Done
Based on the previous information, I would recommend the following products to kill bed bugs:

1. Product: Bed Bug Killer Powder
   Brand: Good Morning
   Sale Price: 100.0
   Description: The most effective bed bug killer with 100% efficacy, non-toxic, safe, and eco-friendly. It can be used directly on the mattress and surroundings.

2. Product: Dead Line - Bug Fighter
   Brand: Mukund
   Sale Price: 275.0
   Description: A ready-to-use spray that kills bed bugs. It should be sprayed where bed bugs are often seen and the room should be kept closed for 4 to 5 hours for the best results.

Please note that proper usage instructions and precautions should be followed for each product to ensure effectiveness and safety.
 ----------------------------------------------

Entry your query -

Give me more details Product 1 given above
Generating Answer ... Done
Product: Bed Bug Killer Powder
Brand: Good Morning
Sale Price: 100.0
Description: The most effective bed bug killer with 100% efficacy, non-toxic, safe, and eco-friendly. It can be used directly on the mattress and surroundings.

For more information or details, please contact our Customer Care Executive at:
Phone: 1860 123 1000
Address: Innovative Retail Concepts Private Limited, No.18, 2nd & 3rd Floor, 80 Feet Main Road, Koramangala 4th Block, Bangalore - 560034
Email: customerservice@bigbasket.com
 ----------------------------------------------
```

Quite clearly the model remembered what Product 1 was in the previous conversation and gave more details satisfying the user.

- #### Programmed to output feeded facts -
```

Please Enter query:

who will provide the best solution for assignment by Chaabi in its campus placement drive
Generating Answer ... Done
The best solution for the assignment given by Chaabi in its campus placement drive will be provided by Aryan Jain, a student from IIT Kanpur with roll number 200201.
 ----------------------------------------------

Please Enter query:

explain what is this data all about and summarise
Generating Answer ... Done
The provided data is a list of different products available at BigBasket, an online grocery store. It includes information such as categories, sub-categories, brands, sale prices, market prices, types, ratings, and descriptions of each product. This data was provided by Chaabi for their assignment during the Placements 2023 campus drive at IIT Kanpur, and it was submitted by Aryan Jain, a student at IIT Kanpur.

Overall, this data provides a comprehensive overview of the different products available at BigBasket, allowing consumers to make informed choices based on their preferences and needs.
 ----------------------------------------------
```

## More Sample Queries
Followng examples are all the series of sample conversation with the bot. You may realise that due to its contexual based answers depending upon previous conversation, it was very easy to get exactly what the user wanted even after the bot mis-undestood the product due to initial lack of information.
```
Entry your query -

Recommend me moisturiser for oily skin
Generating Answer ... Done
Based on the query for a moisturizer for oily skin, I would recommend the following product:

Product: Oil Free Face Moisturizer
Brand: Mamaearth
Sale Price: 99.0
Description: Mamaearth's oil-free face moisturizer is specially formulated to balance the pH level of the skin and reduce acne breakouts. It helps in retaining natural moisture, making the skin smooth and elastic. This non-greasy cream is free from toxins, silicone, parabens, SLS, and harmful chemicals.

Please note that this recommendation is based on the information provided in the query and may not be directly related to the previous conversation about bed bugs.
 ----------------------------------------------

Entry your query -

What are you doing ?
Generating Answer ... Done
I am an AI language model, so I am not capable of physical actions. I am here to assist you with any information or questions you may have.
 ----------------------------------------------

Entry your query -

Give me the cheapest and best milk
Generating Answer ... Done
Based on the information provided, the cheapest and best milk option would be "Nandini Goodlife Skimmed Milk." It is priced at 25.0, has a rating of 3.8, and is suitable for individuals watching their weight. It is hygienically processed and offers a combination of taste and health.
 ----------------------------------------------

Entry your query -

Give me the best shampoo and conditioner that i should use together. I dont have too much money
Generating Answer ... Done
Based on your budget, I would recommend the Pantene 2-In-1 Silky Smooth Care Shampoo + Conditioner. It is priced at 150.0 and has a rating of 3.8. This 2-in-1 formula is designed to fight roughness, control frizz, and help reduce hair fall due to breakage. It provides enhanced nourishment and protection for your hair.
 ----------------------------------------------

Entry your query -

Not 2 in 1 shampoo and conditioner. I want to buy them separately
Generating Answer ... Done
If you are looking to purchase shampoo and conditioner separately instead of a 2-in-1 formula, I would recommend considering the following options:

1. Shampoo:
- Product: Pantene Advanced Hair Fall Solution Shampoo - Anti-dandruff
  - Category: Beauty & Hygiene
  - Sub-category: Hair Care
  - Brand: Pantene
  - Sale_price: 120.0
  - Market_price: 120.0
  - Type: Shampoo & Conditioner
  - Rating: 4.2
  - Description: This shampoo gently cleanses hair without drying the scalp and contains weightless moisturizers that leave hair healthy and shiny. It is enhanced with Zinc Pyrithione to help prevent the reoccurrence of dandruff. The formula keeps hair feeling healthier and shinier with regular use.

2. Conditioner:
- Product: Pantene Advanced Hair Fall Solution Conditioner
  - Category: Beauty & Hygiene
  - Sub-category: Hair Care
  - Brand: Pantene
  - Sale_price: 110.0
  - Market_price: 110.0
  - Type: Shampoo & Conditioner
  - Rating: 4.0
  - Description: This conditioner is designed to be used after shampooing and helps reduce hair fall due to breakage. It provides advanced nourishment and protection to strengthen hair, making it less prone to breakage.

Please note that the above recommendations are based on the information provided and are specific to Pantene products. If you have any specific preferences or requirements, please let me know, and I can provide alternative recommendations.
 ----------------------------------------------

Entry your query -

i want to buy moon
Generating Answer ... Done
Based on the information provided, the product "Daisy Coffee Mugs - Moon M215" is available for sale at a price of 409.0, with a market price of 507.0. It falls under the category "Kitchen, Garden & Pets" and the sub-category "Crockery & Cutlery." The brand is Claycraft, and the type of product is Cups, Mugs & Tumblers. However, there is no information available on the rating of this specific product.

Please note that the above information is specific to the product "Daisy Coffee Mugs - Moon M215" and may not be relevant to other products or variants. If you have any further questions or require assistance with the purchase, feel free to ask.
 ----------------------------------------------

Entry your query -

i want to buy Vodka
Generating Answer ... Done
Based on your query, you mentioned that you want to buy Vodka. Unfortunately, the previous information provided does not include any recommendations for Vodka. However, based on your query, it seems that you are interested in purchasing Vodka from the "Kitchen, Garden & Pets" category, specifically the "Crockery & Cutlery" sub-category.

I apologize for the confusion, but please note that Vodka is a type of alcoholic beverage and not a crockery or cutlery item. It is usually sold in liquor or beverage stores, rather than under the "Crockery & Cutlery" category.

I recommend checking with local liquor stores or online platforms that specialize in selling alcoholic beverages to find a suitable brand and type of vodka that meets your preferences. Please ensure that you are of legal drinking age in your jurisdiction before purchasing any alcoholic beverages.
 ----------------------------------------------
```

## Note
This softare use some API keys which have been provided by Aryan intentionally for the use of Company Chaabi to test and validate this code.  Feel free to use the keys in the code for validating the software.