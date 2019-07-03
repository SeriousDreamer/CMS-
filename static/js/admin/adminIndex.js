$(document).ready(function () {
    $('#articleList').click(function () {
        $.ajax({
            async: true,
            url: "/luna/web/articleList",
            success: function (data) {
                $('#article-list').html(data);
                active($('#web'));
            }
        });
    });

    $('#index_column').click(function () {
        $.ajax({
            async: true,
            url: "/luna/backStage/column",
            success: function (data) {
                $('#column').html(data);
                active($('#backStage'));
            }
        });
    });

    function active(obj) {
        let arr = [$('#backStage'), $('#web'), $('#baseIndex')];
        for (let i in arr) {
            if (i === obj) {
                i.addClass('active');
            } else {
                i.removeClass('active');
            }
        }
    }
});