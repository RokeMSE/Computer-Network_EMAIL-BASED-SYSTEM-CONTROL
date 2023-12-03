const tags = document.querySelectorAll('.features > *');
const inputBoxes = document.querySelectorAll('.input-user > *');
const results = document.querySelectorAll('.show-result > *');
const requests = document.querySelectorAll('.send-request > *');

tags.forEach((tag, id) => {
    tag.addEventListener('click', () => {
        hideAllTags();
        hideAllInputBoxes();
        hideAllResults();
        hideAllRequests();

        tag.classList.add('active')
        inputBoxes[id].classList.add('choose') 
        results[id].classList.add('show') 
        requests[id].classList.add('select') 
    })
})
function hideAllTags() {
    tags.forEach(tag => tag.classList.remove('active'));
}
function hideAllInputBoxes() {
    inputBoxes.forEach(inputBox => inputBox.classList.remove('choose'));
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



const valuekl = document.querySelector("#valuekl");
const inputkl = document.querySelector("#pi_inputkl");
// const using_opt = document.querySelector(".using");
const klMail = document.getElementById("klMail");
valuekl.textContent = inputkl.value;
inputkl.addEventListener("input", (event) => {
    valuekl.textContent = event.target.value;

    klMail.href = "mailto:nguyennam002004@gmail.com?subject=Key%20logger&body=Time%5B" + event.target.value + "%5D";
});



//Code for application and processor
var btns = document.querySelectorAll(".delete");
btns.forEach(btn => {
    btn.addEventListener("click", (e) => {
        const li = e.target.parentElement;
        li.parentElement.removeChild(li);
    });
})

const addAppName = document.querySelector("#add-app > #name");
const addAppRealName = document.querySelector("#add-app > #real-name");
const addAppBtn = document.querySelector("#add-app > button");

addAppBtn.disabled = true;
function checkUserInput() {
    if (addAppName.value !== "" && addAppRealName.value !== "") {
        addAppBtn.disabled = false;
    } else {
        addAppBtn.disabled = true;
    }
}
addAppName.addEventListener("input", checkUserInput);
addAppRealName.addEventListener("input", checkUserInput);

addAppBtn.addEventListener("click", (e) => {
    e.preventDefault();
    const li = document.createElement("li");
    const img = document.createElement("img");
    const name = document.createElement("span");
    const realName = document.createElement("span");
    const deleteBtn = document.createElement("span");
    img.src = "https://i.stack.imgur.com/3hRmg.png";
    name.textContent = addAppName.value;
    realName.textContent = addAppRealName.value;
    deleteBtn.textContent = "delete";
    img.classList.add("app-image");
    name.classList.add("name");
    realName.classList.add("real-name");
    deleteBtn.classList.add("delete");
    li.appendChild(img);
    li.appendChild(name);
    li.appendChild(realName);
    li.appendChild(deleteBtn);
    document.querySelector("#app-list > ul").appendChild(li);
    addAppName.value = "";
    addAppRealName.value = "";
    deleteBtn.addEventListener("click", (e) => {
        const li = e.target.parentElement;
        li.parentElement.removeChild(li);
    });
})

const searchBar = document.forms["search-app"].querySelector("input");
searchBar.addEventListener('keyup', e => {
    const term = e.target.value.toLowerCase();
    const apps = document.querySelectorAll("#app-list > ul > li");
    apps.forEach(app => {
        const name = app.querySelector(".name").textContent.toLowerCase();
        const realName = app.querySelector(".real-name").textContent.toLowerCase();
        if(name.indexOf(term) != -1 || realName.indexOf(term) != -1) {
            app.style.display = "block";
        } else {
            app.style.display = "none";
        }
    })
})


let refreshBtn = document.querySelector("#refresh-data");
refreshBtn.addEventListener('click', e => {
    e.preventDefault();
    // AJAX request to fetch updated key logger data
    fetch('/get-key-logger/')  // Use the appropriate URL here
        .then(response => response.json())
        .then(data => {
            // Update the HTML content with the fetched data
            let keyLoggerSpan = document.querySelector('#show-key-logger');
            keyLoggerSpan.textContent = `Key logger: ${data.key_logger}`;
        })
        .catch(error => {
            console.error('Error fetching data:', error);
        });
})

    
