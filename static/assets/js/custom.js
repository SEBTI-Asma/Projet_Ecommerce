(function() {
	'use strict';

	var tinyslider = function() {
		var el = document.querySelectorAll('.testimonial-slider');

		if (el.length > 0) {
			var slider = tns({
				container: '.testimonial-slider',
				items: 1,
				axis: "horizontal",
				controlsContainer: "#testimonial-nav",
				swipeAngle: false,
				speed: 700,
				nav: true,
				controls: true,
				autoplay: true,
				autoplayHoverPause: true,
				autoplayTimeout: 3500,
				autoplayButtonOutput: false
			});
		}
	};
	tinyslider();

	


	var sitePlusMinus = function() {

		var value,
    		quantity = document.getElementsByClassName('quantity-container');

		function createBindings(quantityContainer) {
	      var quantityAmount = quantityContainer.getElementsByClassName('quantity-amount')[0];
	      var increase = quantityContainer.getElementsByClassName('increase')[0];
	      var decrease = quantityContainer.getElementsByClassName('decrease')[0];
	      increase.addEventListener('click', function (e) { increaseValue(e, quantityAmount); });
	      decrease.addEventListener('click', function (e) { decreaseValue(e, quantityAmount); });
	    }

	    function init() {
	        for (var i = 0; i < quantity.length; i++ ) {
						createBindings(quantity[i]);
	        }
	    };

	    function increaseValue(event, quantityAmount) {
	        value = parseInt(quantityAmount.value, 10);

	        console.log(quantityAmount, quantityAmount.value);

	        value = isNaN(value) ? 0 : value;
	        value++;
	        quantityAmount.value = value;
	    }

	    function decreaseValue(event, quantityAmount) {
	        value = parseInt(quantityAmount.value, 10);

	        value = isNaN(value) ? 0 : value;
	        if (value > 0) value--;

	        quantityAmount.value = value;
	    }
	    
	    init();
		
	};
	sitePlusMinus();


})()

$("add-to-cart").on("click",function(){
	let product_title=$("#product_title").val();
	let product_price=$("#product_price").val();

	let product_image=$("#product_image").val();
	let product_quantity=$("#product_quantity").val();		
	let product_id=$("#product_id").val();
	console.log(productId);
     $.ajax({
		url : '/add-to-cart',
		data:{
            'id':product_id,
            'title':product_title,
            'price':product_price,
			'image':product_image,
			'quantity':product_quantity,
		},
		dataType : 'json',
	 })    
})

document.getElementById("checkout-button").addEventListener("click", function() {
    // Récupérer l'ID du produit
    let productId = $("data-product-id").value;
	console.log(productId);

    // Envoyer une requête POST à votre vue add_to_cart avec l'ID du produit
    fetch("{% url 'checkout' %}", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            "X-CSRFToken": "{{ csrf_token }}"
        },
        body: JSON.stringify({ product_id: productId })
    })
    .then(response => {
        if (response.ok) {
            // Rediriger vers la vue checkout si l'ajout au panier est réussi
            window.location.href = "{% url 'checkout' %}";
        } else {
            // Gérer les erreurs si l'ajout au panier échoue
            console.error("Failed to add product to cart");
        }
    })
    .catch(error => {
        console.error("Error:", error);
    });
});
