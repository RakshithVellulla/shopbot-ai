# products.py — ShopBot Product Catalog

PRODUCTS = [
    # ── LAPTOPS & COMPUTERS ──
    {
        "id": 1,
        "name": "Acer Aspire 5",
        "category": "Laptops & Computers",
        "price": 620,
        "brand": "Acer",
        "specs": {
            "processor": "Intel Core i5",
            "ram": "8GB",
            "storage": "256GB SSD",
            "display": "15.6 inch Full HD",
            "battery": "8 hours",
            "graphics": "NVIDIA GeForce MX350"
        },
        "use_case": ["everyday use", "students", "work"],
        "in_stock": True
    },
    {
        "id": 2,
        "name": "Dell XPS 15",
        "category": "Laptops & Computers",
        "price": 1200,
        "brand": "Dell",
        "specs": {
            "processor": "Intel Core i7",
            "ram": "16GB",
            "storage": "512GB SSD",
            "display": "15.6 inch 4K OLED",
            "battery": "12 hours",
            "graphics": "NVIDIA GeForce RTX 3050"
        },
        "use_case": ["professional", "creative work", "video editing"],
        "in_stock": True
    },
    {
        "id": 3,
        "name": "ASUS ROG Strix G15",
        "category": "Laptops & Computers",
        "price": 1400,
        "brand": "ASUS",
        "specs": {
            "processor": "AMD Ryzen 9",
            "ram": "32GB",
            "storage": "1TB SSD",
            "display": "15.6 inch 144Hz",
            "battery": "6 hours",
            "graphics": "NVIDIA GeForce RTX 3070"
        },
        "use_case": ["gaming", "heavy workloads"],
        "in_stock": True
    },

    # ── PHONES & TABLETS ──
    {
        "id": 4,
        "name": "Samsung Galaxy S23",
        "category": "Phones & Tablets",
        "price": 799,
        "brand": "Samsung",
        "specs": {
            "processor": "Snapdragon 8 Gen 2",
            "ram": "8GB",
            "storage": "128GB",
            "display": "6.1 inch AMOLED",
            "battery": "3900mAh",
            "camera": "50MP triple camera"
        },
        "use_case": ["everyday use", "photography", "travel"],
        "in_stock": True
    },
    {
        "id": 5,
        "name": "iPad Air 5th Gen",
        "category": "Phones & Tablets",
        "price": 599,
        "brand": "Apple",
        "specs": {
            "processor": "Apple M1",
            "ram": "8GB",
            "storage": "64GB",
            "display": "10.9 inch Liquid Retina",
            "battery": "10 hours",
            "camera": "12MP"
        },
        "use_case": ["students", "creative work", "entertainment"],
        "in_stock": True
    },

    # ── HEADPHONES & AUDIO ──
    {
        "id": 6,
        "name": "Sony WH-1000XM5",
        "category": "Headphones & Audio",
        "price": 349,
        "brand": "Sony",
        "specs": {
            "type": "Over ear",
            "noise_cancellation": "Yes",
            "battery": "30 hours",
            "connectivity": "Bluetooth 5.2",
            "microphone": "Yes"
        },
        "use_case": ["travel", "work from home", "music"],
        "in_stock": True
    },
    {
        "id": 7,
        "name": "JBL Tune 510BT",
        "category": "Headphones & Audio",
        "price": 49,
        "brand": "JBL",
        "specs": {
            "type": "On ear",
            "noise_cancellation": "No",
            "battery": "40 hours",
            "connectivity": "Bluetooth 5.0",
            "microphone": "Yes"
        },
        "use_case": ["budget", "everyday use", "students"],
        "in_stock": True
    },

    # ── GAMING ──
    {
        "id": 8,
        "name": "PlayStation 5",
        "category": "Gaming",
        "price": 499,
        "brand": "Sony",
        "specs": {
            "storage": "825GB SSD",
            "resolution": "4K",
            "fps": "120fps",
            "online": "PlayStation Network"
        },
        "use_case": ["console gaming", "entertainment"],
        "in_stock": False
    },
    {
        "id": 9,
        "name": "Xbox Series X",
        "category": "Gaming",
        "price": 499,
        "brand": "Microsoft",
        "specs": {
            "storage": "1TB SSD",
            "resolution": "4K",
            "fps": "120fps",
            "online": "Xbox Game Pass"
        },
        "use_case": ["console gaming", "entertainment"],
        "in_stock": True
    },

    # ── SMART HOME ──
    {
        "id": 10,
        "name": "Amazon Echo Dot 5th Gen",
        "category": "Smart Home",
        "price": 49,
        "brand": "Amazon",
        "specs": {
            "assistant": "Alexa",
            "connectivity": "WiFi + Bluetooth",
            "speaker": "1.73 inch"
        },
        "use_case": ["smart home control", "music", "reminders"],
        "in_stock": True
    },
    {
        "id": 11,
        "name": "Google Nest Hub 2nd Gen",
        "category": "Smart Home",
        "price": 99,
        "brand": "Google",
        "specs": {
            "assistant": "Google Assistant",
            "display": "7 inch touchscreen",
            "connectivity": "WiFi + Bluetooth"
        },
        "use_case": ["smart home control", "video calls", "recipes"],
        "in_stock": True
    },

    # ── ACCESSORIES & CABLES ──
    {
        "id": 12,
        "name": "Anker 65W USB-C Charger",
        "category": "Accessories & Cables",
        "price": 35,
        "brand": "Anker",
        "specs": {
            "wattage": "65W",
            "ports": "2 USB-C + 1 USB-A",
            "compatibility": "Universal"
        },
        "use_case": ["charging", "travel", "home office"],
        "in_stock": True
    },
    {
        "id": 13,
        "name": "Logitech MX Master 3 Mouse",
        "category": "Accessories & Cables",
        "price": 99,
        "brand": "Logitech",
        "specs": {
            "connectivity": "Bluetooth + USB",
            "battery": "70 days",
            "dpi": "200-8000"
        },
        "use_case": ["work", "productivity", "design"],
        "in_stock": True
    },

    # ── CAMERAS & WEBCAMS ──
    {
        "id": 14,
        "name": "Logitech C920 HD Webcam",
        "category": "Cameras & Webcams",
        "price": 79,
        "brand": "Logitech",
        "specs": {
            "resolution": "1080p",
            "fps": "30fps",
            "microphone": "Dual stereo",
            "compatibility": "Windows + Mac"
        },
        "use_case": ["video calls", "streaming", "work from home"],
        "in_stock": True
    },
    {
        "id": 15,
        "name": "Sony ZV-E10 Camera",
        "category": "Cameras & Webcams",
        "price": 748,
        "brand": "Sony",
        "specs": {
            "resolution": "24.2MP",
            "video": "4K",
            "lens": "Interchangeable",
            "stabilization": "Yes"
        },
        "use_case": ["content creation", "vlogging", "photography"],
        "in_stock": True
    },

    # ── TVs & MONITORS ──
    {
        "id": 16,
        "name": "Samsung 55 inch 4K TV",
        "category": "TVs & Monitors",
        "price": 699,
        "brand": "Samsung",
        "specs": {
            "display": "55 inch 4K QLED",
            "refresh_rate": "120Hz",
            "smart_tv": "Yes",
            "hdmi_ports": 4
        },
        "use_case": ["entertainment", "gaming", "home theater"],
        "in_stock": True
    },
    {
        "id": 17,
        "name": "LG 27 inch 4K Monitor",
        "category": "TVs & Monitors",
        "price": 449,
        "brand": "LG",
        "specs": {
            "display": "27 inch 4K IPS",
            "refresh_rate": "60Hz",
            "ports": "HDMI + DisplayPort + USB-C",
            "eye_care": "Yes"
        },
        "use_case": ["work", "design", "programming"],
        "in_stock": True
    }
]


def search_products(query=None, category=None, max_price=None, min_price=None):
    """
    Search products based on filters.
    This is the function the AI will use to find relevant products.
    """
    results = PRODUCTS

    # Filter by category
    if category:
        results = [p for p in results if 
                   category.lower() in p["category"].lower()]

    # Filter by max price
    if max_price:
        results = [p for p in results if p["price"] <= max_price]

    # Filter by min price
    if min_price:
        results = [p for p in results if p["price"] >= min_price]

    # Filter by keyword in name or use case
    if query:
        results = [p for p in results if
                   query.lower() in p["name"].lower() or
                   any(query.lower() in use.lower() 
                       for use in p["use_case"])]

    return results


def format_products_for_llm(products):
    """
    Convert product list into clean text the LLM can read and use.
    """
    if not products:
        return "No products found matching those criteria."

    formatted = []
    for p in products:
        specs_text = ", ".join([f"{k}: {v}" 
                                for k, v in p["specs"].items()])
        stock = "In Stock" if p["in_stock"] else "Out of Stock"
        formatted.append(
            f"- {p['name']} by {p['brand']} | "
            f"${p['price']} | {stock}\n"
            f"  Specs: {specs_text}\n"
            f"  Best for: {', '.join(p['use_case'])}"
        )

    return "\n\n".join(formatted)