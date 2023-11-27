const tags = document.querySelectorAll('.features > *');
const inputBoxs = document.querySelectorAll('.input-user > *');
const results = document.querySelectorAll('.show-result > *');
const requests = document.querySelectorAll('.send-request > *');

tags.forEach((tag, id) => {
    tag.addEventListener('click', () => {
        hideAllTags();
        hideAllInputBoxs();
        hideAllResults();
        hideAllRequests();

        tag.classList.add('active')
        inputBoxs[id].classList.add('choose') 
        results[id].classList.add('show') 
        requests[id].classList.add('select') 
    })
})
function hideAllTags() {
    tags.forEach(tag => tag.classList.remove('active'));
}
function hideAllInputBoxs() {
    inputBoxs.forEach(inputBox => inputBox.classList.remove('choose'));
}
function hideAllResults() {
    results.forEach(result => result.classList.remove('show'));
}
function hideAllRequests() {
    requests.forEach(request => request.classList.remove('select'));
}

