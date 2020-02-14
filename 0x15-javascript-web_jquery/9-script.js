$.ajax({
  url: 'https://fourtonfish.com/hellosalut/?lang=fr',
  type: 'GET',
  dataType: 'json'
})
  .done(function (json) {
    if (json.hello) {
      $('DIV#hello').text('hello');
    }
  });
