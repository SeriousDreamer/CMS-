$('document').ready(function () {
    widths = $('.col-md-6').css('width');
    widths = parseInt(widths)-30;
    widths = widths + "px";
    $('.product').children('div').css('width',widths);
    $('.product').mouseover(function () {
        $(this).children('.product-about').css('display','block');
    }).mouseleave(function () {
        $(this).children('.product-about').css('display','none');
    })
});