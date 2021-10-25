iteam_no = document.getElementById("#item")


$(document).ready(function(){
  $("#btn").click(function() {
      $.ajax({
          url: "/iteam/no/",
          type: "POST",
          data: {
              data1: $("#item").val(),
              csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
          },
          success: function (result) {
              console.log(result)
              $("#details").append('<h2>' + result.name + '</h2>')
              $("#details").append('<h2>' + result.number + '</h2>')
              $("#details").append('<h2>' + result.quentity + '</h2>')

          }
      });
  })
});
