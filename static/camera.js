// const splash = document.querySelector('.splash');
//
// document.addEventListener('DOMContentLoaded',(e)=>{
//   setTimeout(()=>{
//     splash.classList.add('display-none');
//   },2000);
// })




function openCamera(){

  //-----------------Another Function to access webcam------------

// let canvas = document.querySelector('#canvas');
// let context = canvas.getContext("2d");
// let video = document.querySelector('#video');
//
// if(navigator.mediaDevices && navigator.mediaDevices.getUserMedia){
//   navigator.mediaDevices.getUserMedia({video: true}).then(stream =>{
//     video.srcObject = stream;
//     video.play();
//   });
// }
//
// document.getElementById('snap').addEventListener('click',()=>{
//   console.log(video);
//   context.drawImage(video,0,0,640,480);
// });
//------------------------------------the proble of the above code is- the image data is not storing any variable.-------


  Webcam.set({
         width: 550,
         height: 420,
         image_format: 'jpeg',
         jpeg_quality: 100
     });
     Webcam.attach('#camera');

     // SHOW THE SNAPSHOT.
     takeSnapShot = function () {

         Webcam.snap(function (data_uri) {
             document.getElementById('snapShot').innerHTML =
                 '<img src="' + data_uri + '" width="550px" height="420px" />';
                 console.log(data_uri);
                 sessionStorage.setItem("ImageData", data_uri)
         });
     }

}



//    function saveSnap(){
//      console.log('save');
//  // // Get base64 value from <img id='imageprev'> source
//  // var base64image = document.getElementById("imageprev").src;
//  //
//  // Webcam.upload( base64image, 'upload.php', function(code, text) {
//  //  console.log('Save successfully');
//  //  console.log(text);
//  // });
// }

// $('#chooseFile').bind('change', function () {
//   var filename = $("#chooseFile").val();
//   if (/^\s*$/.test(filename)) {
//     $(".file-upload").removeClass('active');
//     $("#noFile").text("No file chosen...");
//   }
//   else {
//     $(".file-upload").addClass('active');
//     $("#noFile").text(filename.replace("C:\\fakepath\\", ""));
//   }
// });
