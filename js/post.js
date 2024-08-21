$(function(){
//$('.carousel').carousel();
$('form:not(.ecriretextchat)').on('submit', function () {
  if (window.filesize > 1024*5) {
    alert('max upload size is 5k');
return false;
  }
  $.ajax({
    // Your server script to process the upload
    url: $(this).attr("action"),
    type: $(this).attr("method"),

    // Form data
    data: new FormData($(this)[0]),

    // Tell jQuery not to process data or worry about content-type
    // You *must* include these options!
    cache: false,
    contentType: false,
    processData: false,

    // Custom XMLHttpRequest
    success: function (data) {
	    console.log("HEY")
	    console.log(JSON.stringify(data))
	    console.log(JSON.stringify(data.redirect))
window.location=data.redirect ? data.redirect : "/";
},
	  beforeSend: function(){
		         $('.loader').show()
		     },
	  complete: function(){
		         $('.loader').hide();
		    },
    xhr: function () {
      var myXhr = $.ajaxSettings.xhr();
      if (myXhr.upload) {
        // For handling the progress of the upload
        myXhr.upload.addEventListener('progress', function (e) {
          if (e.lengthComputable) {
            $('progress').attr({
              value: e.loaded,
              max: e.total,
            });
          }
        }, false);
      }
      return myXhr;
    }
  });
	return false;
  });


$('form.ecriretextchat').on('submit', function () {
  if (window.filesize > 1024*5) {
    alert('max upload size is 5k');
return false;
  }
  $.ajax({
    // Your server script to process the upload
    url: $(this).attr("action"),
    type: $(this).attr("method"),

    // Form data
    data: new FormData($(this)[0]),

    // Tell jQuery not to process data or worry about content-type
    // You *must* include these options!
    cache: false,
    contentType: false,
    processData: false,

    // Custom XMLHttpRequest
    success: function (data) {
	    console.log("HEY")
	    console.log(JSON.stringify(data))
	    console.log(JSON.stringify(data.redirect))
var text=data.text;
div1.innerHTML="<ul>";
	    if (text){
	    for(var i = 0;i<text.length;i++){
div1.innerHTML+="<li>";
div1.innerHTML+="<b>";
div1.innerHTML+=text[i].me === "1" ? "system" : "moi";
div1.innerHTML+=":</b>";
div1.innerHTML+=text[i].content;
div1.innerHTML+="</li>";
}
	    }
div1.innerHTML+="</ul>";
div1.scrollTop = div1.scrollHeight
},
	  beforeSend: function(){
		         $('.loader').show()
		     },
	  complete: function(){
		         $('.loader').hide();
		    },
    xhr: function () {
      var myXhr = $.ajaxSettings.xhr();
      if (myXhr.upload) {
        // For handling the progress of the upload
        myXhr.upload.addEventListener('progress', function (e) {
          if (e.lengthComputable) {
            $('progress').attr({
              value: e.loaded,
              max: e.total,
            });
          }
        }, false);
      }
      return myXhr;
    }
  });
	return false;
  });

  
});
