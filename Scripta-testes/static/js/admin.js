const memberSearch = document.querySelector('#member-search');
const memberRows = document.querySelectorAll('.member-row');

memberSearch.addEventListener('input', () => {
  const searchTerm = memberSearch.value.toLowerCase();

  memberRows.forEach((row) => {
    const content = row.dataset.search.toLowerCase();
    row.hidden = !content.includes(searchTerm);
  });
});
