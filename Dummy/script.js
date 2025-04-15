async function searchBooks() {
    const query = document.getElementById('searchQuery').value;
    const resultsDiv = document.getElementById('results');
    resultsDiv.innerHTML = ''; // Clear previous results

    try {
        const response = await fetch(`https://gutendex.com/books?search=${query}`);
        const data = await response.json();

        data.results.forEach(book => {
            const bookDiv = document.createElement('div');
            bookDiv.style.marginBottom = '20px';

            const title = document.createElement('h3');
            title.textContent = book.title;

            const author = document.createElement('p');
            author.textContent = `Author: ${book.authors.map(author => author.name).join(', ')}`;

            const formats = document.createElement('p');
            formats.innerHTML = 'Formats: ' + Object.keys(book.formats).map(format => {
                const formatLink = document.createElement('a');
                formatLink.href = book.formats[format];
                formatLink.textContent = format;
                formatLink.target = '_blank';
                return formatLink.outerHTML;
            }).join(', ');

            bookDiv.appendChild(title);
            bookDiv.appendChild(author);
            bookDiv.appendChild(formats);

            resultsDiv.appendChild(bookDiv);
        });
    } catch (error) {
        console.error('Error fetching books:', error);
        resultsDiv.innerHTML = 'An error occurred while fetching the results. Please try again later.';
    }
}
