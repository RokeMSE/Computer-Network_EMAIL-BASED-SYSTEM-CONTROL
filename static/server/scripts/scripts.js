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



const value = document.querySelector("#value");
const input = document.querySelector("#pi_input");
const using_opt = document.querySelector(".using");
const sd_lg = document.getElementById("sd_lg");

value.textContent = input.value;
input.addEventListener("input", (event) => {
    value.textContent = event.target.value;
    if (sd_lg.href.includes("Shutdown[")) {
        sd_lg.href = "mailto:nguyennam002004@gmail.com?subject=Shutdown%2FLogout&body=Shutdown[" + event.target.value + "]";
    }
    else if (sd_lg.href.includes("Logout[")) {
        sd_lg.href = "mailto:nguyennam002004@gmail.com?subject=Shutdown%2FLogout&body=Logout[" + event.target.value + "]";
    }
    
});


const opts = document.querySelectorAll(".opt > *");
opts.forEach((opt, id) => {
    opt.addEventListener("click", () => {
        hideAllOpts();
        opt.classList.add("using");
        if (sd_lg.href.includes("Shutdown[")) {
            sd_lg.href = sd_lg.href.replaceOverloaded("=Shutdown[", "=" + opt.textContent + "[");
        }
        else if (sd_lg.href.includes("Logout[")) {
            sd_lg.href = sd_lg.href.replaceOverloaded("=Logout[", "=" + opt.textContent + "[");
        }
    });
});
function hideAllOpts() {
    opts.forEach((opt) => opt.classList.remove("using"));
}
String.prototype.replaceOverloaded = function(searchValue, replaceValue) {
    if (arguments.length === 1) {
        return this.replace(new RegExp(searchValue, 'g'), '');
    } else {
        return this.replace(searchValue, replaceValue);
    }
};
  


const header = document.querySelector(".header");
const header_height = header.offsetHeight;
const main_box = document.querySelector(".main_box");

main_box.style.minHeight = `calc(100vh - ${header_height}px)`; 



