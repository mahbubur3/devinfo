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


let tags = document.getElementsByClassName('project-tag')

for (let tag of tags) {
    tag.addEventListener('click', (e) => {
        let tagId = e.target.dataset.tag
        let projectId = e.target.dataset.project

        fetch('http://127.0.0.1:8000/api/remove-tag/', {
            method: 'DELETE',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ 'project': projectId, 'tag': tagId })
        })
            .then(response => response.json())
            .then(data => {
                e.target.remove()
            })
    })
}