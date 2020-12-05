function findFlight(to) {
    var from = document.getElementById("myInput").value;
    from = from.toLowerCase();
    to = to.toLowerCase();
    var link = "https://www.kiwi.com/us/search/tiles/" + from + "/" + to;
    window.open(link, "_blank");
}

function updateModal(title, description, imgurl) {
    var aTitle = document.getElementById("attraction-title"),
        aDesc = document.getElementById("attraction-text"),
        aImg = document.getElementById("attraction-image");
    aTitle.innerHTML = title;
    aDesc.innerHTML = description;
    aImg.src = imgurl;
}