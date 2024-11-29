
document.getElementById('searchForm').addEventListener('submit', function(event) {

  event.preventDefault();


  const query = document.getElementById('query').value;


  if (!query) {
    console.error('Please enter a search query');
    return;
  }


  fetch(`https://api.tvmaze.com/search/shows?q=${query}`)
    .then(response => response.json())
    .then(data => {

      console.log('Search Results:', data);
    })
    .catch(error => {

      console.error('There was a problem with the fetch operation:', error);
    });
});