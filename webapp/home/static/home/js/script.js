//window.onload = function () {
//    alert("loaded");
//    alert($.fn.jquery)
//}
var loadFile = function(event) {
	var image = document.getElementById('img_frame1');
	image.src = URL.createObjectURL(event.target.files[0]);
};

function upload() {
//event.preventDefault();
var data = new FormData($("#upload_form").get(0));
//alert("sending");
//$("#img_frame1").attr("src","http://127.0.0.1:8000/static/home/img/loading.gif");
$("#img_frame2").attr("src","http://127.0.0.1:8000/static/home/img/loading.gif");
$("#result").text('Working');
$.ajax({
    url: "/upload",
    type: "POST",
    data: data,
    cache: false,
    processData: false,
    contentType: false,
    success: function(data) {
//        alert('success');
        console.log(data)
//        $("#img_frame1").attr("src","http://127.0.0.1:8000/static/home/result/Recovered.jpg");
        var timestamp = new Date().getTime();
        $("#img_frame2").attr("src","http://127.0.0.1:8000/static/home/result/enc.jpg?t="+timestamp);
        $("#result").text('Prediction : '+data+' Algorithms | Accuracy: 94%');
    }
});
return false;
}


//$("#upload_form").submit(upload);
