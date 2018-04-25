$(function () {

  $(".js-create-login").click(function () {
    $.ajax({
      url: '/login',
      type: 'get',
      dataType: 'json',
      beforeSend: function () {
        $("#myModalLogin").modal("show");
      },
      success: function (data) {
        $("#myModalLogin .modal-content").html(data.html_form);
      }
    });
  });

   $("#myModalLogin").on("submit", ".js-user-login-form", function () {
    var form = $(this);
    $.ajax({
      url: form.attr("action"),
      data: form.serialize(),
      type: form.attr("method"),
      dataType: 'json',
      success: function (data) {
        if (data.form_is_valid) {
          $('#myModalLogin').modal('hide');
          RedirectToPage();
        }
        else {
          $("#myModalLogin .modal-content").html(data.html_form);
        }
      }
    });
    return false;
  });

    function RedirectToPage()
      {
          window.location='/view_phages/';
      }

});
