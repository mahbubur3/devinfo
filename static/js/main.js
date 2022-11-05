let searchForm = document.getElementById('search-form')
let pageLink = document.getElementsByClassName('page-link')

if (searchForm) {
    for (let i = 0; pageLink.length > i; i++) {
        pageLink[i].addEventListener('click', function (event) {
            event.preventDefault()

            let page = this.dataset.page

            searchForm.innerHTML += `<input value=${page} name="page" hidden/>`
            searchForm.submit()
        })
    }
}