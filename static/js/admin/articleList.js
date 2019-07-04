$(function () {
   // 所有文章按钮ajax事件
    $('#articleFun_all').click(function () {
        $.ajax({
            async: true,
            url: "/luna/web/articleList",
            success: function (data) {
                $('#article-list').html(data)
            }
        });
    });
    // 写文章按钮ajax事件
    $('#articleFun_write').click(function () {
        $.ajax({
            async: true,
            url: "/luna/web/writeArticle",
            success: function (data) {
                $('#article-list').html(data);
            }
        });
    });
    // 分类目录按钮ajax事件
    $('#articleFun_column').click(function () {
        $.ajax({
            async: true,
            url: "/luna/backStage/column",
            success: function (data) {
                $('#article-list').html(data);
                $('#web').removeClass('active');
                $('#backStage').addClass('active');
            }
        });
    });
    // 文章标题ajax事件
    $('.articleTitle').click(function () {
        let articleUrl = $(this).attr('urlTarget');

        $.ajax({
            async: true,
            method: "get",
            url: '/luna/web/updateArticle',
            data: {
                csrfmiddlewaretoken: '{{ csrf_token }}',
                "url": articleUrl
            },
            success: function (data) {
                $('#article-list').html(data);
            },
            error: function () {
                alert("ajax事件失败");
            }
        })
    });

    function checkFun(main, other) {
        main.prop('checked', false);
        for (let i = 0; i < other.length; i++) {
            other.eq(i).prop('checked', false);
        }
        main.click(function () {
            if (main.is(":checked")) {
                for (let i = 0; i < other.length; i++) {
                    other.eq(i).prop('checked', true);
                }
            } else {
                for (let i = 0; i < other.length; i++) {
                    other.eq(i).prop('checked', false);
                }
            }
        });
        other.click(function () {
            let len = 0;
            for (let i = 0; i < other.length; i++) {
                if (other.eq(i).prop('checked')) {
                    len++;
                }
            }
            if (len == other.length) {
                main.prop('checked', true);
            } else {
                main.prop('checked', false);
            }
        });
    }

    checkFun($('#articleMainCheck'), $('.articleOtherCheck'));
});