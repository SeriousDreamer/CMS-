$(document).ready(function () {
    $('#articleList').click(function () {
        $.ajax({
            async: true,
            url: "/luna/web/articleList",
            success: function (data) {
                $('#article-list').html(data);
            }
        });
    });

    $('#index_column').click(function () {
        $.ajax({
            async: true,
            url: "/luna/backStage/column",
            success: function (data) {
                $('#column').html(data);
            }
        });
    });


});