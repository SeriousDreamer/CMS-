$(function () {
    $("#upload-b").click(function () {
        let formData = new FormData();
        let file = $("#uploadFile")[0].files[0];
        formData.append("file", file);
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
                    method: "get",
                    data: {
                        "width": width,
                    },
                    success: function (data) {
                        $("#media").html(data);
                        active($("#web"))
                    }
                });
            }
        })
    });


});

//
// function waterFall(column, width) {
//     let imgObj = $(".media_item");
//     // 获取图片数量
//     let number = parseInt(imgObj.length);
//     let part = parseInt(number / column);
//     // alert(part);
//     let height = [];
//     let widths = [];
//     for (let n = 0; n < column; n++) {
//         height.push(0);
//         widths.push(width * n);
//     }
//     for (let n = 0; n < part + 10; n++) {
//         for (let i = 0; i < column; i++) {
//             // 获取当前行高度最小列的高度
//             let minId = Math.min.apply(null, height);
//             // 获取这一列的id值
//             let index = 0;
//             for (let m = 0; m < height.length; m++) {
//                 if (minId === height[m]) {
//                     index = m;
//                 }
//             }
//             // alert("下标" + index);
//             if ((i + n * column) < imgObj.length) {
//                 imgObj.eq(i + n * column).css({
//                     "top": height[index] + "px",
//                     "left": widths[index] + "px",
//                     "visibility": "visible",
//                     "position": "absolute",
//                 });
//                 let beforeHeight = height[index];
//                 let imageHeight = parseInt(imgObj.eq(i + (n * column)).css("height"));
//                 height[index] = imageHeight + beforeHeight;
//
//                 // alert("当前图片高度" + parseInt(imgObj.eq(i + n * 4).css("height")));
//                 // alert("列高度" + height);
//             } else {
//                 break;
//             }
//         }
//     }
// }
