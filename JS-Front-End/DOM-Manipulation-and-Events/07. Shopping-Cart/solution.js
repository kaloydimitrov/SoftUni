function solve() {
   let addedProducts = [];
   let totalPrice = 0;

   const addButtons = Array.from(document.getElementsByClassName("add-product"));
   const checkoutButton = document.querySelector(".checkout");
   const textarea = document.querySelector("textarea");

   checkoutButton.addEventListener("click", createCheckout)

   for (const button of addButtons) {
      button.addEventListener("click", addToCart)
   }

   function createCheckout(e) {
      textarea.textContent += `You bought ${addedProducts.join(", ")} for ${totalPrice.toFixed(2)}.`;

      for (const button of addButtons) {
         button.removeEventListener("click", addToCart);
      }
   }

   function addToCart(e) {
      const currentElement = e.currentTarget;
      const parentElement = currentElement.parentNode.parentNode;

      const name = parentElement.querySelector(".product-title").textContent;
      let price = parentElement.querySelector(".product-line-price").textContent;
      price = Number(price);
      totalPrice += price;
      
      if (!addedProducts.includes(name)) {
         addedProducts.push(name);
      }

      textarea.textContent += `Added ${name} for ${price.toFixed(2)} to the cart.\n`;
   }
}