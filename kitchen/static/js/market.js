$(function () {

    $(".subShopping").click(function () {
        console.log('sub');
        var $sub=$(this);
            console.log($sub.attr('class'));
            console.log($sub.attr('goodidsub'));
        var goodidsub = $sub.attr("goodidsub");
        // var goodsid = $sub.prop("goodid");
        $.getJSON('/app/subtocart/',{'goodidsub':goodidsub},function (data) {
            console.log(data);
            if (data['status'] ===302 ){
                window.open('/app/login/',target='_self')
            }else if(data['status'] === 200){
                $sub.next('span').html(data['count'])
            }

        })

    })

    $(".addShopping").click(function () {
        console.log('add');
        var $add =$(this);


            console.log($add.attr('class'));
            console.log($add.attr('goodid'));

        // var $add = $add.attr('goodid');
        // var $add = $add.prop('goodid');
        var goodid=$add.attr('goodid');
        //ajax发送git请求
        $.get('/app/addtocart/',{'goodid':goodid},function (data) {
            console.log(data);
            if(data['status'] === 302){
                window.open('/app/login/',target='_self');

            }else if(data['status'] ===200){
                // 获取  +  号点击事件的  前面的兄弟标签  并把值给他
                $add.prev('span').html(data['count']);
            }
        })
        })
})
