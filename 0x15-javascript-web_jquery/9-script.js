$(document).ready(function () {
  $.getJSON('https://fourtonfish.com/hellosalut/?lang=fr?callback=?',
    function (data, textStatus) {
      console.log(data);
      //$('DIV#hello').html(data.hello);
    });
});
