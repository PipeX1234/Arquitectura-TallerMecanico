// to get current year
function getYear() {
    var currentDate = new Date();
    var currentYear = currentDate.getFullYear();
    document.querySelector("#displayYear").innerHTML = currentYear;
}

getYear();

function hide() {
    var x = document.getElementById("hide");
    if (x.style.display === "none") {
        x.style.display = "block";
    }else { 
        x.style.display = "none";
    }
}

