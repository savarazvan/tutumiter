function findFlight(to) {
    var from = document.getElementById("myInput").value;
    from = from.toLowerCase();
    to = to.toLowerCase();
    var link = 'https://www.kiwi.com/us/search/tiles/' + from + '/' + to;
    window.open(link, '_blank')
}