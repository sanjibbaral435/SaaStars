$(function () {

  $(".js-create-signup").click(function () {
    $.ajax({
      url: '/signup',
      type: 'get',
      dataType: 'json',
      beforeSend: function () {
        $("#myModalSignup").modal("show");
      },
      success: function (data) {
        $("#myModalSignup .modal-content").html(data.html_form);
      }
    });
  });

   $("#myModalSignup").on("submit", ".js-user-create-form", function () {
    var form = $(this);
    $.ajax({
      url: form.attr("action"),
      data: form.serialize(),
      type: form.attr("method"),
      dataType: 'json',
      success: function (data) {
        if (data.form_is_valid) {
        $('#myModalSignup').modal('hide');
          alert("User Registered Successfully!");  // <-- This is just a placeholder for now for testing
        }
        else {
          $("#myModalSignup .modal-content").html(data.html_form);
        }
      }
    });
    return false;
  });
});
