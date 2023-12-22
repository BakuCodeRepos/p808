function removeRow(rowID, orderID) {
    $(rowID).remove();
    deleteOrder(orderID);
    let count = document.getElementById('basket-order-count');
    count.innerHTML -= 1;
}

function deleteOrder(orderID) {
    request_url = order_delete_url.replace('1', orderID);

    $.ajax({
      method: "DELETE",
      url: request_url,
      headers: { "X-CSRFToken": csrftoken_ },
      dataType: "json",
      success: function () {
        calcTotal();
        // manageCheckoutButton();
      },
      error: function(data) {
        console.log('error cixdiiiii', data);
      }
    });
  }


  function calcPlusTotal(ID) {
    let price = document.getElementById(`price-${ID}`).innerText;
    let quantity = parseInt(document.getElementById(`qty-${ID}`).value);
    quantity += 1;
    document.getElementById(`qty-${ID}`).value = quantity;
    let result = document.getElementById(`total-${ID}`).innerHTML = parseFloat((parseFloat(price) * parseFloat(quantity)).toFixed(2));
    btn = document.getElementById(`minus-button-${ID}`);
    btn.disabled = false
    calcTotal();
}


function calcMinusTotal(ID) {
    let price = document.getElementById(`price-${ID}`).innerText;
    let quantity = document.getElementById(`qty-${ID}`).value;
    quantity -= 1;
    document.getElementById(`qty-${ID}`).value = quantity;
    document.getElementById(`total-${ID}`).innerHTML = parseFloat((parseFloat(price) * parseFloat(quantity)).toFixed(2));

    if (parseInt(quantity) === 1) {
        btn = document.getElementById(`minus-button-${ID}`);
        btn.disabled = true
    }
    calcTotal();
}

function calcTotal() {
    let totals = document.getElementsByName('order-total');
    let result = 0.00;

    for (i of totals) {
      result += parseFloat(i.innerHTML);
    }
    let shipping = result * 5 / 100
    document.getElementById('sub-total').innerHTML = parseFloat(result.toFixed(2));
    document.getElementById('shipping').innerHTML = parseFloat(shipping.toFixed(2));
    document.getElementById('final-total').innerHTML = parseFloat((shipping + result).toFixed(2));
  }