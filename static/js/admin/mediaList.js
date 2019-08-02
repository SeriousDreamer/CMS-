$(function () {
    // 图片删除按钮点击
    $(".delete_img").click(function () {
        let img_obj = $(this);
        let did = img_obj.attr("delete_data");
        $.ajax({
            async: true,
            url: "/luna/web/delete",
            type: "post",
            data: {"id": did},
            success: function (data) {
                if (data["code"] === 200) {
                    alert("删除成功");
                    let width = parseInt($("#myTabContent").css("width"));
                    $.ajax({
                        async: false,
                        url: "/luna/web/mediaList",
                        type: "get",
                        // 如果type为0则表明请求的为瀑布流式视图，如果为1则为列表式
                        data: {
                            "width": width,
                            "type": 0,
                        },
                        success: function (data) {
                            $("#media").html(data);
                            active($("#web"))
                        }
                    });
                } else {
                    alert("删除失败");
                }

            }
        })
    });

    // 上传按钮点击后的方法
    $("#upload-b").click(function () {
        let formData = new FormData();
        let file = $("#uploadFile")[0].files[0];
        formData.append("file", file);
        // 将图片提交给后台的方法
        $.ajax({
            async: true,
            url: "/luna/web/upload",
            type: "post",
            data: formData,
            processData: false,
            contentType: false,
            success: function (data) {
                // $("#uploadStatus").html(data.message);
                alert(data.message);
                let width = parseInt($("#myTabContent").css("width"));
                $.ajax({
                    async: true,
                    url: "/luna/web/mediaList",
                    type: "get",
                    // 如果type为0则表明请求的为瀑布流式视图，如果为1则为列表式
                    data: {
                        "width": width,
                        "type": 0,
                    },
                    success: function (data) {
                        $("#media").html(data);
                        active($("#web"))
                    }
                });
            }
        })
    });

    let waterFall = $("#listWater");
    let listTable = $("#listTable");
    // 瀑布流按钮点击事件
    waterFall.click(function () {
        changeCss(waterFall, listTable);
        $("#media_div_list").css("display", "none");
        $("#media_div_water").css("display", "block");
    });
    // 列表页按钮点击事件
    listTable.click(function () {
        changeCss(listTable, waterFall);
        $("#media_div_list").css("display", "block");
        $("#media_div_water").css("display", "none");
    });

    checkFun($('#mediaMainCheck'), $('.mediaOtherCheck'));

    // 修改显示方式按钮的css样式的方法
    function changeCss(obg1, obg2) {
        obg1.css("box-shadow", "1px 1px 1px #000,-1px -1px 1px #000");
        obg2.css("box-shadow", "");
    }

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


});


