// 增加顶级标题按钮点击事件
$('#add_top_column').click(function () {
    let $input = $('input[name="top_column"]');
    let token = $input.attr("token");
    let columnName = $input.val();
    // 通过ajax将数据发送addColumn页面，交给后台的添加数据函数处理
    $.ajax({
        async: true,
        method: "post",
        url: 'luna/backStage/addColumn',
        data: {
            csrfmiddlewaretoken: token,
            'columnName': columnName,
        },
        success: function (data) {
            // 等到数据成功添加后，动态的刷新目录列表页面
            $.ajax({
                async: true,
                method: "get",
                data: {
                    'data':data //这里的data是外层ajax执行成功后返回的数据
                },
                url: "/luna/backStage/column",
                success: function (data) {
                    $('#column').html(data);
                }
            });
        }
    });
});


