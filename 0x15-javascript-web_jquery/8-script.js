$.get('https://swapi-api.hbtn.io/api/films/?format=json', (data, textStatus) => {
  if (textStatus === 'success') {
    const movieList = $('ul#list_movies');
    const movieData = data.results;
    for (let i = 0; i < movieData.length; i++) {
      movieList.append('<li>' + movieData[i].title + '</li>');
    }
  }
});
