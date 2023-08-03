// Test code whe nnetwork is available
$.get('https://swapi-api.alx-tools.com/api/people/5/?format=json',
  function (data, textStatus) {
    $('DIV#character').html(data.name);
  });
