/* Pagination */ 
function prev_paginator_handler(event) {
    next_btn.classList.remove('disabled')

    let curr_page = Number(Array.from(document.getElementsByClassName('page-item active'))[0].id.split('_')[1])
    if (curr_page > 1) {
        let new_page = curr_page - 1 
        if (new_page == 1){
            prev_btn.classList.add('disabled')
        }
        else {
            prev_btn.classList.remove('disabled')
        }
        pages[new_page - 1].classList.add('watched');
        update_paginator_by_number(new_page);
        checkAllPagesWatched();
    }
}

function next_paginator_handler(event) {
    prev_btn.classList.remove('disabled')

    let curr_page = Number(Array.from(document.getElementsByClassName('page-item active'))[0].id.split('_')[1])
    if (curr_page < max_page) {
        let new_page = curr_page + 1 
        if (new_page == max_page){
            next_btn.classList.add('disabled')
        }
        else {
            next_btn.classList.remove('disabled')
        }
        pages[new_page - 1].classList.add('watched');
        update_paginator_by_number(new_page);
        checkAllPagesWatched();
    }   
}

function update_paginator_by_number(number) {
    pages.forEach(el => {
        if (el.id == `page_${number}`){
            el.classList.add('active')
        }
        else {
            el.classList.remove('active');
        }
    })
    words.forEach(el => {
        if (el.id == `word_${number}`){
            el.classList.remove('hidden');
        }
        else {
            el.classList.add('hidden')
        }
    })

}

function paginator_handler(event) {
    pages.forEach(el => {
        el.classList.remove('active');
    })
    event.target.parentElement.classList.add('active', 'watched');
    checkAllPagesWatched();
    let curr_word = Number(String(event.target.parentElement.id).split('_')[1]);
    if (curr_word == 1 ) {
        prev_btn.classList.add('disabled')
        next_btn.classList.remove('disabled')
    }
    else if (curr_word == max_page) {
        next_btn.classList.add('disabled')
        prev_btn.classList.remove('disabled')
    }
    else {
        prev_btn.classList.remove('disabled')
        next_btn.classList.remove('disabled')

    }
    words.forEach(el => {
        if (el.id == `word_${curr_word}`){
            el.classList.remove('hidden');
        }
        else {
            el.classList.add('hidden')
        }
    })
}

function checkAllPagesWatched() {
    result = true
    pages.forEach(el => {
        if (Array.from(el.classList).includes('watched') == false) {
            console.dir(el)
            result = false
        }
    })

    if (result == true) {
        btn_send.classList.remove('hidden')
    }
}

document.getElementById('page_1').classList.add('active', 'watched')

let words = Array.from(document.getElementsByClassName('word'))
let paginator = Array.from(document.getElementsByClassName('pagination'))
let prev_btn = document.getElementById('prev_btn')
let next_btn = document.getElementById('next_btn')
let pages = Array.from(paginator[0].children).slice(1, -1)
let max_page = Number(Array.from(paginator[0].children).slice(-2)[0].id.split('_')[1])

prev_btn.onclick = (event) => {prev_paginator_handler(event)}
pages.forEach(el => {
    el.onclick = (event) => {paginator_handler(event)}
})
next_btn.onclick = (event) => {next_paginator_handler(event)}

const btn_send = document.getElementById('btn-send')

btn_send.onclick = (event) => {
    let token = document.getElementsByName('csrfmiddlewaretoken')[0].defaultValue
    // let url = window.location.href
    let url = 'http://127.0.0.1:8000/exercises/update'
    let ex_id = window.location.href.split('/').slice(-2, -1)[0]
    let step = window.location.href.split('/').slice(-1)[0]

    fetch(url, {
            method: 'POST',
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json',
                'X-CSRFToken': token,
            },
            body: JSON.stringify({
                'exercise_id': ex_id,
                'step' : step,
                "value": pages.length,
            })
        }
    ).then(response => {
        console.dir(response.status)
        if (response.status == 200) {
            document.getElementById('step_1').classList.remove('bg-warning', 'active')
            document.getElementById('step_1').classList.add('bg-success')
            document.getElementById('step_2').classList.remove('disabled')
            document.getElementById('step_2').classList.add('bg-warning', 'bg-gradient', 'active', 'fw-bold')
            document.getElementById('main-alert').classList.remove('hidden')
        }
    })
}


