function isDoneOrder() {
    $.ajax({
      method: "PUT",
      url: is_done_url,
      headers: { "X-CSRFToken": csrftoken_ },
      data: {
        is_done: true,
      },
      dataType: "json",
      success: function (data) {
        console.log('is_done_url', is_done_url)
        window.location.href = home_url;
        console.log('success', data);
      },
      error: function(data) {
        console.log('error cixdiiiii', data);
      }
    });
  }


function manageOrderButton() {
  orderButton = document.getElementById('order-button');

  cardNumber = document.getElementById('card-number').value;
  cardHolder = document.getElementById('card-holder').value;
  expireDate = document.getElementById('expire-date').value;
  cvv = document.getElementById('cvv').value;

  if (
    cardNumber &&
    cardHolder &&
    expireDate &&
    cvv
  ) {
    orderButton.disabled=false;
  } else {
    orderButton.disabled=true;
  }

}


function checkValidCardNumber() {
  cardNumber = document.getElementById('card-number');
  cardNumberError = document.getElementById('card-number-error');

  if (cardNumber.value.length !== 16) {
    cardNumberError.classList.remove('d-none');
  } else {
    cardNumberError.classList.add('d-none');
  }
  if (cardNumber.value.length > 16) {
    cardNumber.value = cardNumber.value.slice(0, 16);
    checkValidCardNumber();
  }
}


function checkValidCvv() {
  cvv = document.getElementById('cvv');
  cvvError = document.getElementById('cvv-error');

  if (cvv.value.length !== 3) {
    cvvError.classList.remove('d-none');
  } else {
    cvvError.classList.add('d-none');
  }
  if (cvv.value.length > 3) {
    cvv.value = cvv.value.slice(0, 3);
    checkValidCvv();
  }
}