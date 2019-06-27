$(document).ready(function () {
    $('#articleList').click(function () {
        $.ajax({
            async: true,
            url: "/luna/web/articleList",
            success: function(data){
                $('#article-list').html(data)
            }
        });
    });


});