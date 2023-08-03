$.get('https://swapi-api.alx-tools.com/api/films/?format=json',
  function (data, textStatus) {
    for (const i of data.results) {
      const list = '<li>' + i.title + '</li>';
      $('UL#list_movies').append(list);
    }
  });
