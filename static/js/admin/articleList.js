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
            type: "get",
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

    //复选框控制
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
    // 移至回收站ajax事件
    $('.remove_recycle').click(function () {
        let title = $(this).attr('target');
        let token = $('#articleFun_all').attr('token');
        if ($(this).text() === "删除") {
            $.ajax({
                async: true,
                type: "post",
                data: {
                    csrfmiddlewaretoken: token,
                    'title': title
                },
                url: '/luna/web/deleteArticle',
                success: function (data) {
                    if (data.status === 1) {
                        let trChose = '#article' + data.id;
                        $('#article_result').html(data.message);
                        $(trChose).css('display', 'none');
                    } else if (data.status === 0) {
                        $('#article_result').html(data.message);
                    }
                },
                error:function () {
                    alert('ajax事件失败');
                }
            })
        } else if ($(this).text() === "移至回收站") {
            $.ajax({
                async: true,
                type: "post",
                data: {
                    csrfmiddlewaretoken: token,
                    'title': title
                },
                url: '/luna/web/removeArticleRecycle',
                success: function (data) {
                    if (data.status === 1) {
                        let trChose = '#article' + data.id;
                        $('#article_result').html(data.message);
                        $(trChose).css('display', 'none');
                    } else if (data.status === 0) {
                        $('#article_result').html(data.message);
                    }
                }
            })
        }
    });

    // 回收站按钮
    $('#articleFun_recycle').click(function () {
        let articleFunRecycle = $('#articleFun_recycle');
        status = articleFunRecycle.attr('status');
        if (status === "1") {
            $.ajax({
                async: true,
                type: 'get',
                url: '/luna/web/recycleArticle',
                success: function (data) {
                    $('#article-list').html(data);
                    // 这里再次获取标签对象是因为上面一句更新了html文件，导致方法最开始获取的标签对象被释放
                    let articleFunRecycle = $('#articleFun_recycle');
                    articleFunRecycle.attr('status','0');
                    articleFunRecycle.html("文章列表");
                }
            });
        } else if (status === '0') {
            $.ajax({
                async: true,
                url: "/luna/web/articleList",
                success: function (data) {
                    $('#article-list').html(data);
                    let articleFunRecycle = $('#articleFun_recycle');
                    articleFunRecycle.attr('status', '1');
                    articleFunRecycle.html("回收站");
                }
            });
        }
    });

    // 恢复文章
    $('.recoverArticle').click(function () {
        let title = $(this).attr('target');
        let token = $('#articleFun_all').attr('token');
        $.ajax({
            async: true,
            type: "post",
            data: {
                csrfmiddlewaretoken: token,
                'title': title
            },
            url: '/luna/web/recoverArticle',
            success: function (data) {
                if (data.status === 1) {
                    let trChose = '#article' + data.id;
                    $('#article_result').html(data.message);
                    $(trChose).css('display', 'none');
                } else if (data.status === 0) {
                    $('#article_result').html(data.message);
                }
            },
            error: function () {
                alert('ajax事件失败');
            }
        })
    });
});
