function addToWishList(productID) {

    $.ajax({
      method: "PUT",
      url: add_to_wish_list_url,
      headers: { "X-CSRFToken": csrftoken_ },
      data: {
        product: productID,
      },
      dataType: "json",
      success: function () {
      },
      error: function(data) {
        console.log('error cixdiiiii', data);
      }
    });
  }

  function removeFromWishList(productID) {

    $.ajax({
      method: "PUT",
      url: remove_from_wish_list_url,
      headers: { "X-CSRFToken": csrftoken_ },
      data: {
        product: productID,
      },
      dataType: "json",
      success: function () {
      },
      error: function(data) {
        console.log('error cixdiiiii', data);
      }
    });
  }

function selectWishFunc(productID) {
    let elem = document.getElementById(`heart-${productID}`);
    let count = document.getElementById('wish-list-count');
    let count_value = parseInt(count.innerText);
  
    if (elem.style.color == 'red') {
      elem.style.color = '';
      removeFromWishList(productID);
      count.innerHTML = count_value - 1;
    } else {
      elem.style.color = 'red'
      addToWishList(productID);
      count.innerHTML = count_value + 1;
    }
  }
