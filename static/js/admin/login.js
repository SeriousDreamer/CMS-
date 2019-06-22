window.onload=function () {
    var heights = $(window).height();
    $('#main').css('height',heights);
    $(window).resize(function () {
        var heights = $(window).height();
    $('#main').css('height',heights);
    });
};