iteam_no = document.getElementById("#item")

var csrfcookie = function() {
    var cookieValue = null,
        name = 'csrftoken';
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
};

$(document).ready(function(){
  $("#btn").click(function() {
      $.ajax({
          url: "/iteam/no/",
          type: "POST",
          data: {data: iteam_no},
          header: {'X-CSRFToken': csrfcookie()},
          success: function (result) {
              console.log(result.data)
          }
      });
  })
});
