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
});
