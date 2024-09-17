// Object to store product ID and corresponding price (populated on page load)
var productPrices = {};

$(function () {
  // Fetch product data using GET request to product list API endpoint
  $.get(productListApiUrl, function (response) {
    productPrices = {};  // Reset product prices object before populating

    if (response) {
      var options = '<option value="">--Select--</option>';  // Default option for product selection

      // Loop through each product in the response
      $.each(response, function (index, product) {
        // Build option element for product selection dropdown
        options += '<option value="' + product.product_id + '">' + product.name + '</option>';

        // Store product price for later reference (keyed by product ID)
        productPrices[product.product_id] = product.price_per_unit;
      });

      // Update product selection dropdown with generated options
      $(".product-box").find("select").empty().html(options);
    }
  });
});

$("#addMoreButton").click(function () {
  // Clone the existing product box template for adding more items
  var row = $(".product-box").html();
  $(".product-box-extra").append(row);

  // Make the "remove" button visible for the newly added row
  $(".product-box-extra .remove-row").last().removeClass('hideit');

  // Reset values for the newly added row (price, quantity, total)
  $(".product-box-extra .product-price").last().text('0.0');
  $(".product-box-extra .product-qty").last().val('1');
  $(".product-box-extra .product-total").last().text('0.0');   

});

// Event handler for clicking the "remove" button on a product row
$(document).on("click", ".remove-row", function () {
  // Remove the entire row containing the clicked button
  $(this).closest('.row').remove();

  // Recalculate order total after removing a product
  calculateValue();
});

// Event handler for changing the selected product in a product row
$(document).on("change", ".cart-product", function () {
  var product_id = $(this).val();  // Get the selected product ID

  // Get the price of the selected product from the productPrices object
  var price = productPrices[product_id];

  // Update the product price field in the current row
  $(this).closest('.row').find('#product_price').val(price);

  // Recalculate order total after changing product selection
  calculateValue();
});

// Event handler for changing the product quantity in a product row
$(document).on("change", ".product-qty", function (e) {
  // Recalculate order total after changing product quantity
  calculateValue();
});

$("#saveOrder").on("click", function () {
  // Collect all form data as an array of key-value pairs
  var formData = $("form").serializeArray();

  // Create an empty object to store order details
  var requestPayload = {
    customer_name: null,
    total: null,
    order_details: []
  };

  // Create an empty array to store individual order item details
  var orderDetails = [];

  // Loop through each form data element
  for (var i = 0; i < formData.length; ++i) {
    var element = formData[i];
    var lastElement = null;

    switch (element.name) {
      case 'customerName':
        // Set customer name in the request payload
        requestPayload.customer_name = element.value;
        break;
      case 'product_grand_total':
        // Set order total in the request payload
        requestPayload.grand_total = element.value;
        break;
      case 'product':
        // Create a new order item object for the selected product
        requestPayload.order_details.push({
          product_id: element.value,
          quantity: null,
          total_price: null
        });
        break;
      case 'qty':
        // Get the last added order item object
        lastElement = requestPayload.order_details[requestPayload.order_details.length - 1];
        
        // Set the quantity for the last order item
        lastElement.quantity = element.value;
        break;
            case 'item_total':
                lastElement = requestPayload.order_details[requestPayload.order_details.length-1];
                lastElement.total_price = element.value
                break;
        }

    }
    callApi("POST", orderSaveApiUrl, {
        'data': JSON.stringify(requestPayload)
    });
});
