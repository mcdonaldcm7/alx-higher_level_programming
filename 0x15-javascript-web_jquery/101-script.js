$(document).ready(function () {
  let count = $('UL.my_list').length;
  $('DIV#add_item').on('click', function () {
    $('UL.my_list').append('<li>Item<li>');
    count++;
  });
  $('DIV#remove_item').on('click', function () {
    if (count > 0) {
      $('UL.my_list li:last-child').remove();
      count--;
    }
  });
  $('DIV#clear_list').on('click', function () {
    $('UL.my_list').empty();
    count = 0;
  });
});
