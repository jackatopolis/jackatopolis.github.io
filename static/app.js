console.log(jsdata)

// Current ISS Crew
var astro = '<div class="astro"><h4>Current ISS Crew</h4><hr>'
for (var x=0;x<jsdata['current_crew_names'].length;x++) {
    astro += ('<p><a href="'+jsdata['current_crew_links'][x]+'">'+jsdata['current_crew_names'][x]+'</a><p>');
    };
astro += '</div>';

document.querySelector(".iss").innerHTML = astro;

// APOD
var apod = ('<div class="apod-css"><h2 style="text-align: center">Astronomy Picture of the Day</h2><hr>'
    +'<h3 style="text-align: center">'+jsdata['apod']['title']+'</h3>'
    +'<a href="'+jsdata['apod']['url']
    +'"><img style="display:block; margin-left: auto; margin-right: auto; width: 90% !important;" src="'
    +jsdata['apod']['url']+'"alt="'+jsdata['apod']['title']+'"></a>'
    +'<p style="text-align: center">'
    +jsdata['apod']['date']+' | '+jsdata['apod']['copyright']+'</p>'
    +'<p>"'+jsdata['apod']['explanation']+'"</p></div>'
    );
document.querySelector(".apod").innerHTML = apod;

// Holidays
console.log(jsdata['holidays'])