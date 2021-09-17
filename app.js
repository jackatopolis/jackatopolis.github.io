

function postData() {
    $.ajax({
        type: "GET",
        url: "/app.py",
        data: {},
        success: callbackFunc
    });
}

function callbackFunc(response) {
    // do something with the response
    console.log(response);
}

function scraper() {
    $.get("app.py",function(out) {
        document.getElementById("test-test").innerHTML = out
    })
}

