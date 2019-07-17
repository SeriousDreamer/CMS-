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
    // 资源管理ajax事件
    $("#mediaList").click(function () {
        let width = parseInt($("#myTabContent").css("width"));
        $.ajax({
            async: true,
            url: "/luna/web/mediaList",
            method: "get",
            // 如果type为0则表明请求的为瀑布流式视图，如果为1则为列表式
            data: {
                "width": width,
                "type": 0
            },
            success: function (data) {
                $("#media").html(data);
                active($("#web"))
            }
        })
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