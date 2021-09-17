
function runPyScript(input) {
    var output = $.ajax({
        type:"POST",
        url:"/",
        async:false,
        data: {mydata:input}
    });
    return output.responseText
    }
    result = runPyScript()
    console.log(result)

function scraper() {
    $.get("app.py",function(out) {
        document.getElementById("test-test").innerHTML = out
    })
}

