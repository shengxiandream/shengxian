$('.addshopping').click(function(){
var span = $(this)
goodsid = $(this).attr('goodsid')
//console.log($(this).prev())
//设置回调函数进行数据交互
$.getjson("/app/addcart/",{"goodsid":goodsid},function (data) {


if (data["status"] == "777") {
//target="_self" 这是不去打开新窗口,而是在当前窗口加载新的路径
window.open("/app/login/",target="_self")
}else if (data["status"] == "200"){

console.log(span.prev())
//拿到button前面的标签
span.prev().html(data["num"])

}
})
})