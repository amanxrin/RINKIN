from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from typing import List, Dict

app = FastAPI()

# Serve static files (CSS, JS, images) from the "static" folder
app.mount("/static", StaticFiles(directory="static"), name="static")

# Serve the main HTML page when accessing the root URL
@app.get("/", response_class=HTMLResponse)
async def serve_home():
    with open("index.html", "r") as f:
        return f.read()

# Sample data representing sustainable products
products_data = [
    {
        "id": 1,
        "name": "Eco-friendly Shampoo",
        "description": "Made with biodegradable materials.",
        "sustainability_score": 8.5,
        "image_url": "https://www.organicharvest.in/_next/image?url=https%3A%2F%2Ffiles.organicharvest.in%2Fsite-images%2F800x800%2F8906080038242-OH-Anti-Dandruff-Shampoo-Apple-5.jpg&w=384&q=75",
        "product_url": "https://www.organicharvest.in/product/anti-dandruff-shampoo-apple-cider-vinegar-tea-tree-250ml.html?srsltid=AfmBOor1XsPIqDRyMr5H4t12txrPcT6IM2YKKEywpJlYCG22G0ejRewNV6U&gQT=1"
    },
    {
        "id": 2,
        "name": "Sustainable Water Bottle",
        "description": "Made from recycled materials and BPA-free.",
        "sustainability_score": 9.2,
        "image_url": "https://encrypted-tbn1.gstatic.com/shopping?q=tbn:ANd9GcScbBWN-nDpI4v7rQBEr938u7yPokge0ouo3bAl9014rxVyUFBznw2-kLL4qnfnzFI399okgUtZ0VfU3I2uqFzMIHk3UPIkVCZlqd2WfO6N&usqp=CAE",
        "product_url": "https://bambooindia.com/products/bamboo-water-bottle"
    },
    {
    "id": 3,
    "name": "Eco-friendly Bamboo Toothbrush",
    "description": "A sustainable alternative to plastic toothbrushes made from natural bamboo.",
    "image_url": "https://encrypted-tbn3.gstatic.com/shopping?q=tbn:ANd9GcRi5AKexw0OP0PQez4AyvNJm8Q2pA4Q0JI4122N4Ki4fdfVRi5CRICWaHXoUfoa2vEwGayIIL3xaT3ELfO5GGTakM-E0d5x1_Z_jzcvHq5BeiFUgPnEsSHC4A&usqp=CAE",
    "sustainability_score": 9.5,
    "product_url": "https://www.amazon.in/Eco-Friendly-Toothbrush-Charcoal-Activated-Bristles/dp/B0CNRKPK2N?source=ps-sl-shoppingads-lpcontext&ref_=fplfs&psc=1&smid=AZSG09TE4FHUW"
  },
  {
    "id": 4,
    "name": "Reusable Silicone Food Bags",
    "description": "Eco-friendly and durable food storage bags to reduce single-use plastic waste.",
    "image_url": "https://encrypted-tbn1.gstatic.com/shopping?q=tbn:ANd9GcQwy9Svyy9S1O0bGXFG66CcCU1lthCCwHYswMxxIa9j11w-jbcNbhK9233bZm1ojRAQVYS-j9r9j9DZ1R51pwa63FVjvtutXCyRRRAMGSnt&usqp=CAE",
    "sustainability_score": 9.0,
    "product_url": "https://www.amazon.in/Kettlekane-Silicone-Storage-Reusable-Vegetables/dp/B0CXF5XB7R?source=ps-sl-shoppingads-lpcontext&ref_=fplfs&smid=A30PORC81J3RML&th=1"
  },
  {
    "id": 5,
    "name": "Compostable Phone Case",
    "description": "Biodegradable phone cases made from plant-based materials.",
    "image_url": "https://encrypted-tbn1.gstatic.com/shopping?q=tbn:ANd9GcRm9zX1KwdC0KiPdkW7LS3sI_a6jDX9uQtedrCisvNZztrmvPbmtnHCu0oPV6BZ8gO46BYU69iKFTNS56jA2IReZNjR3fnWSfOgEHuDK4qZu9EIoWEzPMjrUK0&usqp=CAE",
    "sustainability_score": 8.7,
    "product_url": "https://bluebarrows.in/products/the-wise-owl-biodegradable-eco-friendly-mobile-cover-phone?variant=50255144255797&country=IN&currency=INR&utm_medium=product_sync&utm_source=google&utm_content=sag_organic&utm_campaign=sag_organic&srsltid=AfmBOorS2ITN2zCdqicvdvnZ9bZKDTmvdbB5Cs9UmJlxRZ4vMiI3GIkJyEM"
  },
  {
    "id": 6,
    "name": "Solar-Powered Charger",
    "description": "Charge your devices sustainably with this portable solar-powered charger.",
    "image_url": "https://encrypted-tbn1.gstatic.com/shopping?q=tbn:ANd9GcQMV1_PABbxgqUC5CsO_6weYuefjTSag6tm6pjTxVyR_O-Pwdnoti2P0hizk2uOH4ii-EaQ3nwH2Kd_UBbe6Mynl15uwWO6TFJ2-g3uRcc&usqp=CAE",
    "sustainability_score": 9.3,
    "product_url": "https://www.amazon.in/bosig-Large-Capacity-Cellphone-Electronic-Carabiner/dp/B0C4PX513T?source=ps-sl-shoppingads-lpcontext&ref_=fplfs&psc=1&smid=A23V7GX3CEK2YA"
  },
  {
    "id": 7,
    "name": "Stainless Steel Water Bottle",
    "description": "Reusable and insulated water bottles to keep your drinks hot or cold.",
    "image_url": "https://encrypted-tbn0.gstatic.com/shopping?q=tbn:ANd9GcSTZ58OASy3iw0xPHFaiyWN-twTwmSMq5v92Yp5ObLSaxSiBQlrpUnVQ4C0foEM7c5lETiaoaRTvMEgSCk2WoP78jXqUAXtihIsLQYbwKaEcjCKrxO7jv8w0w&usqp=CAE",
    "sustainability_score": 9.1,
    "product_url": "https://www.amazon.in/CASPIAN-Stainless-Sipper-Silver-Thunder/dp/B0C37KNT88?source=ps-sl-shoppingads-lpcontext&ref_=fplfs&psc=1&smid=ACIMSM6G9FAZ4"
  },
  {
    "id": 8,
    "name": "Organic Cotton Tote Bag",
    "description": "Durable tote bags made from 100% organic cotton for shopping and everyday use.",
    "image_url": "https://encrypted-tbn1.gstatic.com/shopping?q=tbn:ANd9GcTyztU44xYK7s0N1sVutUqrb0LAXTBQcyu6m7A__t9YKDnb1GZf029PRHJjqSABDS6kDyxHvtlhMslcuTxgzM5WdjgOjpBh06VJ6eWTKDrm-UZzOskTwMBr&usqp=CAE",
    "sustainability_score": 8.8,
    "product_url": "https://www.amazon.in/Harry-Kritz-Vertical-Stylish-Organic/dp/B0BNJKK8BZ?source=ps-sl-shoppingads-lpcontext&ref_=fplfs&psc=1&smid=A1Y13JKY3XEZ9G"
  },
  {
    "id": 9,
    "name": "Beeswax Food Wraps",
    "description": "A sustainable alternative to plastic wraps made from beeswax and cotton.",
    "image_url": "https://encrypted-tbn1.gstatic.com/shopping?q=tbn:ANd9GcSSkzy31LFE3wuIDTfriLVo7Tf48rppSBvyWvNeOujTQMvF5zlugFnkoaP6cXFMSTUndUe7jblPLUJ7Mq6HMsshJA5j2TRHYCnirFLg4xAtqxAY0SPcjF0U&usqp=CAE",
    "sustainability_score": 9.2,
    "product_url": "https://www.amazon.in/Urban-Creative-Certified-Organic-Assorted/dp/B07MFW3KJS?source=ps-sl-shoppingads-lpcontext&ref_=fplfs&psc=1&smid=A21NCBELVB9UWF"
  },
  {
    "id": 10,
    "name": "Biodegradable Plant Pots",
    "description": "Eco-friendly plant pots made from biodegradable materials.",
    "image_url": "https://encrypted-tbn2.gstatic.com/shopping?q=tbn:ANd9GcT_8WPjQ4iK2e5IzlADPtT4qCZayRVVBr3iEONC5EzeEJH_WKQ6Hq2enIZ1I0hL-GD0Vo9v4nhm-TG7JhUkW3NQeBdDTWqJp7EXCW5NmFzkzYTo7D_RcipB0O8&usqp=CAE",
    "sustainability_score": 8.6,
    "product_url": "https://example.com/products/plant-potshttps://www.amazon.in/Grow-Rich-Germination-Friendly-degradable/dp/B0BX3ZQKSF?source=ps-sl-shoppingads-lpcontext&ref_=fplfs&psc=1&smid=A17DQMYHJT2JHQ"
  },
  {
    "id": 11,
    "name": "Reusable Metal Straws",
    "description": "Stainless steel straws with a cleaning brush to reduce plastic waste.",
    "image_url": "https://encrypted-tbn0.gstatic.com/shopping?q=tbn:ANd9GcRyhDv3u96t25dPa01qjysMCteZ_EBBpZCt21mJaSzdCb2KfLKKHJyVcKsGrXubf44jWxMsH1679VkFPiAUrUp-j3ChylptYnZcYzLfkReriT_5RdYakD6K&usqp=CAE",
    "sustainability_score": 9.4,
    "product_url": "https://www.meesho.com/reusable-stainless-steel-drinking-straws-85-inches/p/54zmok?utm_source=google&utm_medium=cpc&utm_campaign=gmc&srsltid=AfmBOoqza1UO4Qh6gcPR74ucOro434wjvCeh4QqHKOsqKBZvuaMS2yFoWv8"
  },
  {
    "id": 12,
    "name": "Natural deodrants",
    "description": "smell like nature",
    "image_url": "https://encrypted-tbn0.gstatic.com/shopping?q=tbn:ANd9GcRAeR_woWxSUZWN2jH-o-SFMCdBQJptk9lWHQgKi4im_v_1Yn-TY9HRaRwPxllqJOJr2ndHN4TBMxRxIJHUb1blLvSsmVFdofZMK8Y70JJ8pUhEbmSK5uDw&usqp=CAE",
    "sustainability_score": 9.0,
    "product_url": "https://www.amazon.in/Bitamin-Deodorant-Aluminium-Triclosan-Strawberry/dp/B0CXM4QTXX?source=ps-sl-shoppingads-lpcontext&ref_=fplfs&psc=1&smid=A7X9N6GCZ4WRR"
  }
]

# Endpoint to search products based on query
@app.get("/api/products/search")
async def search_products(query: str) -> List[Dict]:
    results = [product for product in products_data if query.lower() in product["name"].lower()]
    return results

# Endpoint to get product details by ID
@app.get("/api/products/{id}")
async def get_product_details(id: int) -> Dict:
    product = next((product for product in products_data if product["id"] == id), None)
    if product:
        return product
    else:
        return {"error": "Product not found"}
