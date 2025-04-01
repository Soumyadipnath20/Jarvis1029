<!DOCTYPE html>
<html lang="en">

<head>>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            text-align: center;
            background: linear-gradient(135deg, #ff9a9e, #fad0c4);
            overflow-x: hidden;
        }

        .navbar {
            display: flex;
            justify-content: space-between;
            align-items: center;
            background: #ff4b5c;
            padding: 15px 20px;
            color: white;
            font-size: 20px;
            font-weight: bold;
            position: fixed;
            top: 0;
            width: 100%;
            z-index: 1000;
            box-shadow: 0 4px 10px rgba(0, 0, 0, 0.3);
            background-attachment: fixed;
            background-size: cover;
        }

        .cart-container {
            position: relative;
            margin-right: 20px;
        }
        .cart-icon {
            position: relative;
            cursor: pointer;
            font-size: 30px;
            padding: 5px;
            margin-right: 30px;
        }
        .cart-icon::after {
            content: attr(data-count);
            position: absolute;
            top: 0;
            right: -12px;
            background: white;
            color: red;
            border-radius: 50%;
            padding: 5px 9px;
            font-size: 14px;
            font-weight: bold;
        }
        .cart-dropdown {
            display: none;
            position: absolute;
            right: 0;
            top: 40px;
            right: 20px;
            background: rgb(230, 193, 218);
            padding: 10px;
            box-shadow: 0 4px 10px rgba(0,0,0,0.2);
            border-radius: 8px;
            color: black;
            width: 300px;
        }
        .cart-container:hover .cart-dropdown {
            display: block;
        }
        .cart-item {
            display: flex;
            align-items: center;
            color: black;
            justify-content: space-between;
            gap: 10px;
            margin-bottom: 10px;
            font-size: 14px;
        }
        .cart-item img {
            width: 50px;
            height: 50px;
            border-radius: 5px;
        }
        .quantity-btn {
            background: #ff4b5c;
            color: white;
            border: none;
            padding: 3px 8px;
            cursor: pointer;
            font-size: 14px;
            border-radius: 5px;
        }
        .checkout-btn {
            background: green;
            color: white;
            border: none;
            padding: 10px;
            width: 100%;
            border-radius: 5px;
            cursor: pointer;
            font-size: 16px;
            margin-top: 10px;
        }

        .checkout-btn {
            background: rgb(252, 112, 245);
            color: white;
            border: none;
            padding: 10px;
            width: 100%;
            border-radius: 5px;
            cursor: pointer;
            font-size: 16px;
            margin-top: 10px;
        }

        . .header-text {
            margin-top: 80px;
            font-size: 40px;
            font-weight: bold;
            text-shadow: 2px 2px 8px rgba(0, 0, 0, 0.2);
            padding: 20px;
            background: rgba(255, 75, 92, 0.9);
            color: white;
            border-radius: 10px;
            display: inline-block;
        }

        .container {
            display: flex;
            flex-wrap: wrap;
            justify-content: center;
            padding: 20px;
            margin-top: 120px;
        }

        .product {
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            align-items: center;
            background: white;
            border-radius: 10px;
            padding: 15px;
            width: 240px;
            margin: 10px;
            box-shadow: 0 4px 10px rgba(0, 0, 0, 0.2);
            text-align: center;
        }

        .product h3 {
            min-height: 40px;
            /* Keeps all product titles aligned */
            font-size: 18px;
            font-weight: bold;
        }

        .product p.desc {
            min-height: 60px;
            /* Ensures descriptions are uniform */
            font-size: 14px;
            color: #555;
        }

        .product img {
            width: 100%;
            height: 300px;
            object-fit: cover;
            border-radius: 8px;
        }

        .product p.price {
            font-size: 16px;
            font-weight: bold;
            color: red;
            margin-top: auto;
        }

        .add-to-cart {
            background: #ff4b5c;
            color: white;
            border: none;
            padding: 10px;
            width: 90%;
            border-radius: 5px;
            cursor: pointer;
            font-size: 16px;
            margin-top: auto;
            transition: 0.3s;
        }

        .add-to-cart:hover {
            background: #d93d4a;
        }

        .footer {
            background: #ff4b5c;
            color: white;
            padding: 15px;
            text-align: center;
            margin-top: 20px;
        }
    </style>
</head>

<body>
    <div class="navbar">
        <div class="nav-title">Menstrual products delivered in 10 minutes</div>
        <div class="cart-container">
            <span class="cart-icon" id="cart-icon" data-count="0">🛒</span>
            <div class="cart-dropdown" id="cart"></div>
        </div>
    </div>


    <div class="container" id="products"></div>
    <div class="footer">&copy; 2025 Instant Menstrual Delivery. All rights reserved.</div>
    <script>
        const products = [
            { id: 1, name: "Menstrual Cup", price: 1200, img: "menstrual cup.jpg", desc: "A reusable menstrual cup made of medical-grade silicone." },
            { id: 2, name: "Tampons", price: 800, img: "tampons.jpg", desc: "Comfortable and absorbent tampons for daily use." },
            { id: 3, name: "Sanitary Pads", price: 600, img: "pads.jpg", desc: "Soft, leak-proof pads with all-day comfort." },
            { id: 4, name: "Menstrual Disc", price: 1500, img: "disc.jpg", desc: "Flexible and comfortable menstrual disc for longer wear." },
            { id: 5, name: "Period Underwear", price: 1800, img: "underwear.jpg", desc: "Reusable, absorbent, and leak-proof period underwear." },
            { id: 6, name: "Menstrual Sponges", price: 1000, img: "sponge.jpg", desc: "Natural and reusable menstrual sponges." },
            { id: 7, name: "Reusable Cloth Pads", price: 700, img: "reusable pads.jpg", desc: "Eco-friendly, washable cloth pads for comfort." },
            { id: 8, name: "Organic Tampons", price: 900, img: "organic.jpg", desc: "100% organic cotton tampons with no chemicals." },
            { id: 9, name: "Period Cups", price: 1300, img: "softcup.jpg", desc: "Alternative to menstrual cups for sensitive users." },
            { id: 10, name: "Menstrual Gel", price: 500, img: "gel.webp", desc: "Cooling gel to relieve menstrual cramps." }
        ];
        const cart = {};
        const productsContainer = document.getElementById("products");
        const cartContainer = document.getElementById("cart");
        const cartIcon = document.getElementById("cart-icon");
        function updateCart() {
            cartContainer.innerHTML = "<h3>Cart</h3>";
            let itemCount = 0, totalCost = 0;
            for (const id in cart) {
                const product = products.find(p => p.id === parseInt(id));
                if (!product) continue; // Ensure the product exists
                const qty = cart[id];
                itemCount += qty;
                totalCost += product.price * qty;
                cartContainer.innerHTML += `
            <div class="cart-item">
                <img src="${product.img}" width="50" height="50">
                <p>${product.name} x ${qty} - ₹${product.price * qty}</p>
                <button class="quantity-btn" onclick="changeQuantity(${id}, -1)">-</button>
                <button class="quantity-btn" onclick="changeQuantity(${id}, 1)">+</button>
            </div>`;
            }
            cartContainer.innerHTML += `<p>Total: ₹${totalCost}</p><button class="checkout-btn">Checkout</button>`;
            cartIcon.setAttribute("data-count", itemCount);
        }


        function addToCart(id) {
            cart[id] = (cart[id] || 0) + 1;
            updateCart();
        }
        function changeQuantity(id, change) {
            if (cart[id]) cart[id] = Math.max(0, cart[id] + change);
            if (cart[id] === 0) delete cart[id];
            updateCart();
        }
        products.forEach(product => {
            productsContainer.innerHTML += `
                <div class="product">
                    <img src="${product.img}" alt="${product.name}">
                    <h3>${product.name}</h3>
                    <p>${product.desc}</p>
                    <p>₹${product.price}</p>
                    <button class="add-to-cart" onclick="addToCart(${product.id})">Add to Cart</button>
                </div>`;
        });
    </script>
</body>

</html>
