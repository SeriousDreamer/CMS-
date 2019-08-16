$(function () {

    function selectFeaturedImage() {
        let url = '';
        $('.media_item_article').click(function () {
            url = $(this).attr('src');
        });
        $('#selectFeaturedImage').click(function () {
            if (url === "") {
                alert('请选择特色图片');
            } else {
                return url;
            }
        })
    }

    function articleFun(method) {

        let title = $("input[name = 'title']").val();

        let introduction = $("input[name = 'introduction']").val();

        let url = $("input[name = 'articleUrl']").val();

        let imageUrl = "";

        imageUrl = selectFeaturedImage();

        let publicStatus = true;
        if ($('#public').is(":checked")) {
            publicStatus = true;
        } else {
            publicStatus = false;
        }

        let commentStatus = true;
        if ($('#commentStatus').is(":checked")) {
            commentStatus = true
        }

        let column = "";
        for (let i = 0; i < $('.writeArticleColumn').length; i++) {
            if ($('.writeArticleColumn').eq(i).is(":checked")) {
                column = column + $('.writeArticleColumn').eq(i).val() + ",";
            }
        }

        let content = $('.markdown-body').html();

        let markdown = $('#editor textarea').html();
        $.ajax({
            async: true,
            type: 'POST',
            url: "/luna/web/" + method,
            data: {
                csrfmiddlewaretoken: '{{ csrf_token }}',
                "title": title, "introduction": introduction,
                "column": column, "commentStatus": commentStatus,
                "publicStatus": publicStatus, "url": url,
                "content": content, "markdown": markdown,
                "imageUrl": imageUrl
            },
            success: function (data) {
                $('#result').html(data)
            }
        });
    }


    $('#releaseArticle').click(function () {
        articleFun("writeArticle");
    });

    $('#updateArticle').click(function () {
        articleFun("updateArticle")
    });
    $('#uploadFeaturedImage').click(function () {
        let width = 568;
        $.ajax({
            async: true,
            type: 'get',
            data: {
                'width': width,
                'type': 0,
                'page': 0,
            },
            url: '/luna/web/mediaList',
            success: function (data) {
                $('#mediaLibrary').html(data);
            }
        })
        ;
    });
});