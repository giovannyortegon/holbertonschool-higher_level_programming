$(function () {
  let value;
  $('#btn_translate').click(function () {
    value = $('#language_code').val();
    $.ajax({
      type: 'GET',
      url: 'https://www.fourtonfish.com/hellosalut/',
      data: { lang: value },
      dataType: 'json'
    })
      .done(function (json) {
        $('DIV#hello').text(json.hello);
      });
  });
  $('#language_code').keypress(function (data) {
    if (data.which === 13) {
      $('#btn_translate').click();
      return false;
    }
  });
});
