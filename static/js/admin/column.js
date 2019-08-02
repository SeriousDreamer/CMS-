$(document).ready(function () {
    // 增加顶级标题按钮点击事件
    $('#add_top_column').click(function () {
        let $input = $('input[name="top_column"]');
        let token = $input.attr("token");
        let columnName = $input.val();
        // 通过ajax将数据发送addColumn页面，交给后台的添加数据函数处理
        $.ajax({
            async: true,
            type: "post",
            url: 'luna/backStage/addColumn',
            data: {
                csrfmiddlewaretoken: token,
                'columnName': columnName,
                'parentName': 0,
            },
            success: function (data) {
                // 等到数据成功添加后，动态的刷新目录列表页面
                if(data.status===200){
                        successResult(data.result)
                }
            }
        });
    });

    // 列表显示按钮点击事件，用于显示子标题
    $('.fade_in_out').click(function () {
        let target = $(this).attr("id");
        let byFade = $('.byFade');
        for (let i = 0; i < byFade.length; i++) {
            if (byFade.eq(i).attr('target') === target) {
                byFade.eq(i).fadeToggle(1000);
            }
        }
        let fadeInOut = $(this);
        let words = fadeInOut.text();
        if (words === "显示") {
            fadeInOut.html("隐藏");
        } else {
            fadeInOut.html("显示");
        }
    });

    // 增加子标题按钮点击事件
    $('.add_child_column').click(function () {
        // 获取对象
        let parentId = $(this).attr('target');
        let columnName = $('.columnName');
        let release = $('.release');
        columnName = choseObj(columnName, parentId);
        let token = columnName.attr('token');
        release = choseObj(release, parentId);
        // 控制隐藏和浮现的动画效果
        columnName.fadeIn(1000);
        release.fadeIn(1000);
        $(this).fadeOut(500);
        // 提交按钮点击事件
        release.click(function () {
            // 判断分类名称是否为空
            if (columnName.val() === '') {
                $('#add_column_result').html("<span class='text-danger'>请输入分类名称</span>");
                return
            }
            // 向后台发送分类名称数据的ajax
            $.ajax({
                async: true,
                type: 'post',
                url: 'luna/backStage/addColumn',
                data: {
                    csrfmiddlewaretoken: token,
                    'columnName': columnName.val(),
                    'parentName': parentId,
                },
                success: function (data) {
                    // 等到数据成功添加后，动态的刷新目录列表页面
                    if(data.status===200){
                        successResult(data.result)
                    }
                },
                error: function () {
                    alert("添加失败")
                }
            })
        })
    });

    function choseObj(obj, target) {
        // 从一堆class选择器中选取需要的object对象，obj为类选择器，target为筛选条件
        for (let i = 0; i < obj.length; i++) {
            if (obj.eq(i).attr('target') === target) {
                obj = obj.eq(i);
                return obj;
            }
        }
    }

    function successResult(returnData) {
        // 这个是重新加载列表页的ajax函数
        $.ajax({
            async: true,
            type: "get",
            data: {
                'data': returnData //这里的data是外层ajax执行成功后返回的数据
            },
            url: "/luna/backStage/column",
            success: function (data) {
                $('#column').html(data);
            }
        });
    }

    $('.delete_column').click(function () {
        let columnId = $(this).attr('target');
        let delete_column = choseObj($('.delete_column'), columnId);
        let token = $('input[name="top_column"]').attr('token');
        $.ajax({
            async: true,
            type: 'post',
            url: 'luna/backStage/deleteColumn',
            data: {
                csrfmiddlewaretoken: token,
                'columnId': columnId
            },
            success: function (data) {
                successResult(data);
            }
        })

    })
});